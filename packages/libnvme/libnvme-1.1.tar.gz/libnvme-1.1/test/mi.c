// SPDX-License-Identifier: LGPL-2.1-or-later
/**
 * This file is part of libnvme.
 * Copyright (c) 2022 Code Construct
 */

#undef NDEBUG
#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

#include <ccan/array_size/array_size.h>

/* we define a custom transport, so need the internal headers */
#include "nvme/private.h"

#include "libnvme-mi.h"

#include "utils.h"

typedef int (*test_submit_cb)(struct nvme_mi_ep *ep,
			      struct nvme_mi_req *req,
			      struct nvme_mi_resp *resp,
			      void *data);

struct test_transport_data {
	unsigned int	magic;
	bool		named;
	test_submit_cb	submit_cb;
	void		*submit_cb_data;
};

static const int test_transport_magic = 0x74657374;

static int test_transport_submit(struct nvme_mi_ep *ep,
				 struct nvme_mi_req *req,
				 struct nvme_mi_resp *resp)
{
	struct test_transport_data *tpd = ep->transport_data;

	assert(tpd->magic == test_transport_magic);

	/* start from a minimal response: zeroed data, nmp to match request */
	memset(resp->hdr, 0, resp->hdr_len);
	memset(resp->data, 0, resp->data_len);
	resp->hdr->type = NVME_MI_MSGTYPE_NVME;
	resp->hdr->nmp = req->hdr->nmp | (NVME_MI_ROR_RSP << 7);

	if (tpd->submit_cb)
		return tpd->submit_cb(ep, req, resp, tpd->submit_cb_data);

	return 0;
}

static void test_transport_close(struct nvme_mi_ep *ep)
{
	struct test_transport_data *tpd = ep->transport_data;
	assert(tpd->magic == test_transport_magic);
	free(tpd);
}

static int test_transport_desc_ep(struct nvme_mi_ep *ep,
				    char *buf, size_t len)
{
	struct test_transport_data *tpd = ep->transport_data;

	assert(tpd->magic == test_transport_magic);

	if (!tpd->named)
		return -1;

	snprintf(buf, len, "test endpoint 0x%x", tpd->magic);

	return 0;
}

/* internal test helper to generate correct response crc */
static void test_transport_resp_calc_mic(struct nvme_mi_resp *resp)
{
	extern __u32 nvme_mi_crc32_update(__u32 crc, void *data, size_t len);
	__u32 crc = 0xffffffff;

	crc = nvme_mi_crc32_update(crc, resp->hdr, resp->hdr_len);
	crc = nvme_mi_crc32_update(crc, resp->data, resp->data_len);

	resp->mic = ~crc;
}

static const struct nvme_mi_transport test_transport = {
	.name = "test-mi",
	.mic_enabled = true,
	.submit = test_transport_submit,
	.close = test_transport_close,
	.desc_ep = test_transport_desc_ep,
};

static void test_set_transport_callback(nvme_mi_ep_t ep, test_submit_cb cb,
					void *data)
{
	struct test_transport_data *tpd = ep->transport_data;
	assert(tpd->magic == test_transport_magic);

	tpd->submit_cb = cb;
	tpd->submit_cb_data = data;
}

nvme_mi_ep_t nvme_mi_open_test(nvme_root_t root)
{
	struct test_transport_data *tpd;
	struct nvme_mi_ep *ep;

	ep = nvme_mi_init_ep(root);
	assert(ep);

	tpd = malloc(sizeof(*tpd));
	assert(tpd);

	tpd->magic = test_transport_magic;
	tpd->named = true;

	ep->transport = &test_transport;
	ep->transport_data = tpd;

	return ep;
}

unsigned int count_root_eps(nvme_root_t root)
{
	unsigned int i = 0;
	nvme_mi_ep_t ep;

	nvme_mi_for_each_endpoint(root, ep)
		i++;

	return i;
}

/* test that the root->endpoints list is updated on endpoint
 * creation/destruction */
static void test_endpoint_lifetime(nvme_mi_ep_t ep)
{
	nvme_root_t root = ep->root;
	unsigned int count;
	nvme_mi_ep_t ep2;

	count = count_root_eps(root);
	assert(count == 1);

	ep2 = nvme_mi_open_test(root);
	count = count_root_eps(root);
	assert(count == 2);

	nvme_mi_close(ep2);
	count = count_root_eps(root);
	assert(count == 1);
}

unsigned int count_ep_controllers(nvme_mi_ep_t ep)
{
	unsigned int i = 0;
	nvme_mi_ctrl_t ctrl;

	nvme_mi_for_each_ctrl(ep, ctrl)
		i++;

	return i;
}

/* test that the ep->controllers list is updated on controller
 * creation/destruction */
static void test_ctrl_lifetime(nvme_mi_ep_t ep)
{
	nvme_mi_ctrl_t c1, c2;
	int count;

	ep->controllers_scanned = true;

	count = count_ep_controllers(ep);
	assert(count == 0);

	c1 = nvme_mi_init_ctrl(ep, 1);
	count = count_ep_controllers(ep);
	assert(count == 1);

	c2 = nvme_mi_init_ctrl(ep, 2);
	count = count_ep_controllers(ep);
	assert(count == 2);

	nvme_mi_close_ctrl(c1);
	count = count_ep_controllers(ep);
	assert(count == 1);

	nvme_mi_close_ctrl(c2);
	count = count_ep_controllers(ep);
	assert(count == 0);
}


/* test: basic read MI datastructure command */
static int test_read_mi_data_cb(struct nvme_mi_ep *ep,
				 struct nvme_mi_req *req,
				 struct nvme_mi_resp *resp,
				 void *data)
{
	__u8 ror, mt, *hdr, *buf;

	assert(req->hdr->type == NVME_MI_MSGTYPE_NVME);

	ror = req->hdr->nmp >> 7;
	mt = req->hdr->nmp >> 3 & 0x7;
	assert(ror == NVME_MI_ROR_REQ);
	assert(mt == NVME_MI_MT_MI);

	/* do we have enough for a mi header? */
	assert(req->hdr_len == sizeof(struct nvme_mi_mi_req_hdr));

	/* inspect response as raw bytes */
	hdr = (__u8 *)req->hdr;
	assert(hdr[4] == nvme_mi_mi_opcode_mi_data_read);

	/* create basic response */
	assert(resp->hdr_len >= sizeof(struct nvme_mi_mi_resp_hdr));
	assert(resp->data_len >= 4);

	hdr = (__u8 *)resp->hdr;
	hdr[4] = 0; /* status */

	buf = (__u8 *)resp->data;
	memset(buf, 0, resp->data_len);
	buf[0] = 1; /* NUMP */
	buf[1] = 1; /* MJR */
	buf[2] = 2; /* MNR */

	test_transport_resp_calc_mic(resp);

	return 0;
}

static void test_read_mi_data(nvme_mi_ep_t ep)
{
	struct nvme_mi_read_nvm_ss_info ss_info;
	int rc;

	test_set_transport_callback(ep, test_read_mi_data_cb, NULL);

	rc = nvme_mi_mi_read_mi_data_subsys(ep, &ss_info);
	assert(rc == 0);
}

/* test: failed transport */
static int test_transport_fail_cb(struct nvme_mi_ep *ep,
				  struct nvme_mi_req *req,
				  struct nvme_mi_resp *resp,
				  void *data)
{
	return -1;
}

static void test_transport_fail(nvme_mi_ep_t ep)
{
	struct nvme_mi_read_nvm_ss_info ss_info;
	int rc;

	test_set_transport_callback(ep, test_transport_fail_cb, NULL);
	rc = nvme_mi_mi_read_mi_data_subsys(ep, &ss_info);
	assert(rc != 0);
}

static void test_transport_describe(nvme_mi_ep_t ep)
{
	struct test_transport_data *tpd;
	char *str;

	tpd = (struct test_transport_data *)ep->transport_data;

	tpd->named = false;
	str = nvme_mi_endpoint_desc(ep);
	assert(str);
	assert(!strcmp(str, "test-mi endpoint"));
	free(str);

	tpd->named = true;
	str = nvme_mi_endpoint_desc(ep);
	assert(str);
	assert(!strcmp(str, "test-mi: test endpoint 0x74657374"));
	free(str);
}

/* test: invalid crc */
static int test_invalid_crc_cb(struct nvme_mi_ep *ep,
				      struct nvme_mi_req *req,
				      struct nvme_mi_resp *resp,
				      void *data)
{
	resp->mic = 0;
	return 0;
}

static void test_invalid_crc(nvme_mi_ep_t ep)
{
	struct nvme_mi_read_nvm_ss_info ss_info;
	int rc;

	test_set_transport_callback(ep, test_invalid_crc_cb, NULL);
	rc = nvme_mi_mi_read_mi_data_subsys(ep, &ss_info);
	assert(rc != 0);
}

/* test: test that the controller list populates the endpoint's list of
 * controllers */
static int test_scan_ctrl_list_cb(struct nvme_mi_ep *ep,
				  struct nvme_mi_req *req,
				  struct nvme_mi_resp *resp,
				  void *data)
{
	__u8 ror, mt, *hdr, *buf;

	assert(req->hdr->type == NVME_MI_MSGTYPE_NVME);

	ror = req->hdr->nmp >> 7;
	mt = req->hdr->nmp >> 3 & 0x7;
	assert(ror == NVME_MI_ROR_REQ);
	assert(mt == NVME_MI_MT_MI);

	/* do we have enough for a mi header? */
	assert(req->hdr_len == sizeof(struct nvme_mi_mi_req_hdr));

	/* inspect response as raw bytes */
	hdr = (__u8 *)req->hdr;
	assert(hdr[4] == nvme_mi_mi_opcode_mi_data_read);
	assert(hdr[11] == nvme_mi_dtyp_ctrl_list);

	/* create basic response */
	assert(resp->hdr_len >= sizeof(struct nvme_mi_mi_resp_hdr));
	assert(resp->data_len >= 4);

	hdr = (__u8 *)resp->hdr;
	hdr[4] = 0; /* status */

	buf = (__u8 *)resp->data;
	memset(buf, 0, resp->data_len);
	buf[0] = 3; buf[1] = 0; /* num controllers */
	buf[2] = 1; buf[3] = 0; /* id 1 */
	buf[4] = 4; buf[5] = 0; /* id 4 */
	buf[6] = 5; buf[7] = 0; /* id 5 */

	test_transport_resp_calc_mic(resp);

	return 0;
}

static void test_scan_ctrl_list(nvme_mi_ep_t ep)
{
	struct nvme_mi_ctrl *ctrl;

	ep->controllers_scanned = false;

	test_set_transport_callback(ep, test_scan_ctrl_list_cb, NULL);

	nvme_mi_scan_ep(ep, false);

	ctrl = nvme_mi_first_ctrl(ep);
	assert(ctrl);
	assert(ctrl->id == 1);

	ctrl = nvme_mi_next_ctrl(ep, ctrl);
	assert(ctrl);
	assert(ctrl->id == 4);

	ctrl = nvme_mi_next_ctrl(ep, ctrl);
	assert(ctrl);
	assert(ctrl->id == 5);

	ctrl = nvme_mi_next_ctrl(ep, ctrl);
	assert(ctrl == NULL);
}

/* test: simple NVMe admin request/response */
static int test_admin_id_cb(struct nvme_mi_ep *ep,
				  struct nvme_mi_req *req,
				  struct nvme_mi_resp *resp,
				  void *data)
{
	__u8 ror, mt, *hdr;
	__u32 dlen, cdw10;
	__u16 ctrl_id;
	__u8 flags;

	assert(req->hdr->type == NVME_MI_MSGTYPE_NVME);

	ror = req->hdr->nmp >> 7;
	mt = req->hdr->nmp >> 3 & 0x7;
	assert(ror == NVME_MI_ROR_REQ);
	assert(mt == NVME_MI_MT_ADMIN);

	/* do we have enough for a mi header? */
	assert(req->hdr_len == sizeof(struct nvme_mi_admin_req_hdr));

	/* inspect response as raw bytes */
	hdr = (__u8 *)req->hdr;
	assert(hdr[4] == nvme_admin_identify);
	flags = hdr[5];

	ctrl_id = hdr[7] << 8 | hdr[6];
	assert(ctrl_id == 0x5); /* controller id */

	/* we requested a full id; if we've set the length flag,
	 * ensure the length matches */
	dlen = hdr[35] << 24 | hdr[34] << 16 | hdr[33] << 8 | hdr[32];
	if (flags & 0x1) {
		assert(dlen == sizeof(struct nvme_id_ctrl));
	}
	assert(!(flags & 0x2));

	/* CNS value of 1 in cdw10 field */
	cdw10 = hdr[47] << 24 | hdr[46] << 16 | hdr[45] << 8 | hdr[44];
	assert(cdw10 == 0x1);

	/* create valid (but somewhat empty) response */
	hdr = (__u8 *)resp->hdr;
	hdr[4] = 0x00; /* status: success */

	test_transport_resp_calc_mic(resp);

	return 0;
}

static void test_admin_id(nvme_mi_ep_t ep)
{
	struct nvme_id_ctrl id;
	nvme_mi_ctrl_t ctrl;
	int rc;

	test_set_transport_callback(ep, test_admin_id_cb, NULL);

	ctrl = nvme_mi_init_ctrl(ep, 5);
	assert(ctrl);

	rc = nvme_mi_admin_identify_ctrl(ctrl, &id);
	assert(rc == 0);
}

/* test: simple NVMe error response */
static int test_admin_err_resp_cb(struct nvme_mi_ep *ep,
				  struct nvme_mi_req *req,
				  struct nvme_mi_resp *resp,
				  void *data)
{
	__u8 ror, mt, *hdr;

	assert(req->hdr->type == NVME_MI_MSGTYPE_NVME);

	ror = req->hdr->nmp >> 7;
	mt = req->hdr->nmp >> 3 & 0x7;
	assert(ror == NVME_MI_ROR_REQ);
	assert(mt == NVME_MI_MT_ADMIN);

	/* do we have enough for a mi header? */
	assert(req->hdr_len == sizeof(struct nvme_mi_admin_req_hdr));

	/* inspect response as raw bytes */
	hdr = (__u8 *)req->hdr;
	assert(hdr[4] == nvme_admin_identify);

	/* we need at least 8 bytes for error information */
	assert(resp->hdr_len >= 8);

	/* create error response */
	hdr = (__u8 *)resp->hdr;
	hdr[4] = 0x02; /* status: internal error */
	hdr[5] = 0;
	hdr[6] = 0;
	hdr[7] = 0;
	resp->hdr_len = 8;
	resp->data_len = 0;

	test_transport_resp_calc_mic(resp);

	return 0;
}

static void test_admin_err_resp(nvme_mi_ep_t ep)
{
	struct nvme_id_ctrl id;
	nvme_mi_ctrl_t ctrl;
	int rc;

	test_set_transport_callback(ep, test_admin_err_resp_cb, NULL);

	ctrl = nvme_mi_init_ctrl(ep, 1);
	assert(ctrl);

	rc = nvme_mi_admin_identify_ctrl(ctrl, &id);
	assert(rc != 0);
}

/* invalid Admin command transfers */
static int test_admin_invalid_formats_cb(struct nvme_mi_ep *ep,
					 struct nvme_mi_req *req,
					 struct nvme_mi_resp *resp,
					 void *data)
{
	/* none of the tests should result in message transfer */
	assert(0);
	return -1;
}

static void test_admin_invalid_formats(nvme_mi_ep_t ep)
{
	struct nvme_mi_admin_resp_hdr resp = { 0 };
	struct nvme_mi_admin_req_hdr req = { 0 };
	nvme_mi_ctrl_t ctrl;
	size_t len;
	int rc;

	test_set_transport_callback(ep, test_admin_invalid_formats_cb, NULL);

	ctrl = nvme_mi_init_ctrl(ep, 1);
	assert(ctrl);

	/* unaligned req size */
	len = 0;
	rc = nvme_mi_admin_xfer(ctrl, &req, 1, &resp, 0, &len);
	assert(rc != 0);

	/* unaligned resp size */
	len = 1;
	rc = nvme_mi_admin_xfer(ctrl, &req, 0, &resp, 0, &len);
	assert(rc != 0);

	/* unaligned resp offset */
	len = 4;
	rc = nvme_mi_admin_xfer(ctrl, &req, 0, &resp, 1, &len);
	assert(rc != 0);

	/* resp too large */
	len = 4096 + 4;
	rc = nvme_mi_admin_xfer(ctrl, &req, 0, &resp, 0, &len);
	assert(rc != 0);

	/* resp offset too large */
	len = 4;
	rc = nvme_mi_admin_xfer(ctrl, &req, 0, &resp, (off_t)1 << 32, &len);
	assert(rc != 0);

	/* resp offset with no len */
	len = 0;
	rc = nvme_mi_admin_xfer(ctrl, &req, 0, &resp, 4, &len);
	assert(rc != 0);

	/* req and resp payloads */
	len = 4;
	rc = nvme_mi_admin_xfer(ctrl, &req, 4, &resp, 0, &len);
	assert(rc != 0);
}

/* test: header length too small */
static int test_resp_hdr_small_cb(struct nvme_mi_ep *ep,
				  struct nvme_mi_req *req,
				  struct nvme_mi_resp *resp,
				  void *data)
{
	resp->hdr_len = 2;
	test_transport_resp_calc_mic(resp);
	return 0;
}

static void test_resp_hdr_small(nvme_mi_ep_t ep)
{
	struct nvme_mi_read_nvm_ss_info ss_info;
	int rc;

	test_set_transport_callback(ep, test_resp_hdr_small_cb, NULL);

	rc = nvme_mi_mi_read_mi_data_subsys(ep, &ss_info);
	assert(rc != 0);
}

/* test: respond with a request message */
static int test_resp_req_cb(struct nvme_mi_ep *ep,
			    struct nvme_mi_req *req,
			    struct nvme_mi_resp *resp,
			    void *data)
{
	resp->hdr->nmp &= ~(NVME_MI_ROR_RSP << 7);
	test_transport_resp_calc_mic(resp);
	return 0;
}

static void test_resp_req(nvme_mi_ep_t ep)
{
	struct nvme_mi_read_nvm_ss_info ss_info;
	int rc;

	test_set_transport_callback(ep, test_resp_req_cb, NULL);

	rc = nvme_mi_mi_read_mi_data_subsys(ep, &ss_info);
	assert(rc != 0);
}

/* test: invalid MCTP type in response */
static int test_resp_invalid_type_cb(struct nvme_mi_ep *ep,
				     struct nvme_mi_req *req,
				     struct nvme_mi_resp *resp,
				     void *data)
{
	resp->hdr->type = 0x3;
	test_transport_resp_calc_mic(resp);
	return 0;
}

static void test_resp_invalid_type(nvme_mi_ep_t ep)
{
	struct nvme_mi_read_nvm_ss_info ss_info;
	int rc;

	test_set_transport_callback(ep, test_resp_invalid_type_cb, NULL);

	rc = nvme_mi_mi_read_mi_data_subsys(ep, &ss_info);
	assert(rc != 0);
}

/* test: response with mis-matching command slot */
static int test_resp_csi_cb(struct nvme_mi_ep *ep,
			    struct nvme_mi_req *req,
			    struct nvme_mi_resp *resp,
			    void *data)
{
	resp->hdr->nmp ^= 0x1;
	test_transport_resp_calc_mic(resp);
	return 0;
}

static void test_resp_csi(nvme_mi_ep_t ep)
{
	struct nvme_mi_read_nvm_ss_info ss_info;
	int rc;

	test_set_transport_callback(ep, test_resp_csi_cb, NULL);

	rc = nvme_mi_mi_read_mi_data_subsys(ep, &ss_info);
	assert(rc != 0);
}

/* test: config get MTU request & response layout, ensure we're handling
 * endianness in the 3-byte NMRESP field correctly */
static int test_mi_config_get_mtu_cb(struct nvme_mi_ep *ep,
			    struct nvme_mi_req *req,
			    struct nvme_mi_resp *resp,
			    void *data)
{
	struct nvme_mi_mi_resp_hdr *mi_resp;
	uint8_t *buf;

	assert(req->hdr_len == sizeof(struct nvme_mi_mi_req_hdr));
	assert(req->data_len == 0);

	/* validate req as raw bytes */
	buf = (void *)req->hdr;
	assert(buf[4] == nvme_mi_mi_opcode_configuration_get);
	/* dword 0: port and config id */
	assert(buf[11] == 0x5);
	assert(buf[8] == NVME_MI_CONFIG_MCTP_MTU);

	/* set MTU in response */
	mi_resp = (void *)resp->hdr;
	mi_resp->nmresp[1] = 0x12;
	mi_resp->nmresp[0] = 0x34;
	resp->hdr_len = sizeof(*mi_resp);
	resp->data_len = 0;

	test_transport_resp_calc_mic(resp);
	return 0;
}

static void test_mi_config_get_mtu(nvme_mi_ep_t ep)
{
	uint16_t mtu;
	int rc;

	test_set_transport_callback(ep, test_mi_config_get_mtu_cb, NULL);

	rc = nvme_mi_mi_config_get_mctp_mtu(ep, 5, &mtu);
	assert(rc == 0);
	assert(mtu == 0x1234);
}

/* test: config set SMBus freq, both valid and invalid */
static int test_mi_config_set_freq_cb(struct nvme_mi_ep *ep,
			    struct nvme_mi_req *req,
			    struct nvme_mi_resp *resp,
			    void *data)
{
	struct nvme_mi_mi_resp_hdr *mi_resp;
	uint8_t *buf;

	assert(req->hdr_len == sizeof(struct nvme_mi_mi_req_hdr));
	assert(req->data_len == 0);

	/* validate req as raw bytes */
	buf = (void *)req->hdr;
	assert(buf[4] == nvme_mi_mi_opcode_configuration_set);
	/* dword 0: port and config id */
	assert(buf[11] == 0x5);
	assert(buf[8] == NVME_MI_CONFIG_SMBUS_FREQ);

	mi_resp = (void *)resp->hdr;
	resp->hdr_len = sizeof(*mi_resp);
	resp->data_len = 0;

	/* accept 100 & 400, reject others */
	switch (buf[9]) {
	case NVME_MI_CONFIG_SMBUS_FREQ_100kHz:
	case NVME_MI_CONFIG_SMBUS_FREQ_400kHz:
		mi_resp->status = 0;
		break;
	case NVME_MI_CONFIG_SMBUS_FREQ_1MHz:
	default:
		mi_resp->status = 0x4;
		break;
	}

	test_transport_resp_calc_mic(resp);
	return 0;
}

static void test_mi_config_set_freq(nvme_mi_ep_t ep)
{
	int rc;

	test_set_transport_callback(ep, test_mi_config_set_freq_cb, NULL);

	rc = nvme_mi_mi_config_set_smbus_freq(ep, 5,
					      NVME_MI_CONFIG_SMBUS_FREQ_100kHz);
	assert(rc == 0);
}

static void test_mi_config_set_freq_invalid(nvme_mi_ep_t ep)
{
	int rc;

	test_set_transport_callback(ep, test_mi_config_set_freq_cb, NULL);

	rc = nvme_mi_mi_config_set_smbus_freq(ep, 5,
					      NVME_MI_CONFIG_SMBUS_FREQ_1MHz);
	assert(rc == 4);
}

#define DEFINE_TEST(name) { #name, test_ ## name }
struct test {
	const char *name;
	void (*fn)(nvme_mi_ep_t);
} tests[] = {
	DEFINE_TEST(endpoint_lifetime),
	DEFINE_TEST(ctrl_lifetime),
	DEFINE_TEST(read_mi_data),
	DEFINE_TEST(transport_fail),
	DEFINE_TEST(transport_describe),
	DEFINE_TEST(scan_ctrl_list),
	DEFINE_TEST(invalid_crc),
	DEFINE_TEST(admin_id),
	DEFINE_TEST(admin_err_resp),
	DEFINE_TEST(admin_invalid_formats),
	DEFINE_TEST(resp_req),
	DEFINE_TEST(resp_hdr_small),
	DEFINE_TEST(resp_invalid_type),
	DEFINE_TEST(resp_csi),
	DEFINE_TEST(mi_config_get_mtu),
	DEFINE_TEST(mi_config_set_freq),
	DEFINE_TEST(mi_config_set_freq_invalid),
};

static void run_test(struct test *test, FILE *logfd, nvme_mi_ep_t ep)
{
	printf("Running test %s...", test->name);
	fflush(stdout);
	test->fn(ep);
	/* tests will assert on failure; if we're here, we're OK */
	printf("  OK\n");
	test_print_log_buf(logfd);
}

int main(void)
{
	nvme_root_t root;
	nvme_mi_ep_t ep;
	unsigned int i;
	FILE *fd;

	fd = test_setup_log();

	root = nvme_mi_create_root(fd, DEFAULT_LOGLEVEL);
	assert(root);

	ep = nvme_mi_open_test(root);
	assert(ep);

	for (i = 0; i < ARRAY_SIZE(tests); i++) {
		run_test(&tests[i], fd, ep);
	}

	nvme_mi_close(ep);
	nvme_mi_free_root(root);

	test_close_log(fd);

	return EXIT_SUCCESS;
}
