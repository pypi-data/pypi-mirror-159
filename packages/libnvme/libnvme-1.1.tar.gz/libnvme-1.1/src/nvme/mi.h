// SPDX-License-Identifier: LGPL-2.1-or-later
/*
 * This file is part of libnvme.
 * Copyright (c) 2021 Code Construct Pty Ltd
 *
 * Authors: Jeremy Kerr <jk@codeconstruct.com.au>
 */

/**
 * DOC: mi.h - NVMe Management Interface library (libnvme-mi) definitions.
 *
 * These provide an abstraction for the MI messaging between controllers
 * and a host, typically over an MCTP-over-i2c link to a NVMe device, used
 * as part of the out-of-band management of a system.
 *
 * We have a few data structures define here to reflect the topology
 * of a MI connection with an NVMe subsystem:
 *
 *  - &nvme_mi_ep_t: an MI endpoint - our mechanism of communication with a
 *    NVMe subsystem. For MCTP, an endpoint will be the component that
 *    holds the MCTP address (EID), and receives our request message.
 *
 *    endpoints are defined in the NVMe-MI spec, and are specific to the MI
 *    interface.
 *
 *    Each endpoint will provide access to one or more of:
 *
 *  - &nvme_mi_ctrl_t: a NVMe controller, as defined by the NVMe base spec.
 *    The controllers are responsible for processing any NVMe standard
 *    commands (eg, the Admin command set). An endpoint (&nvme_mi_ep_t)
 *    may provide access to multiple controllers - so each of the controller-
 *    type commands will require a &nvme_mi_ctrl_t to be specified, rather than
 *    an endpoint
 *
 * A couple of conventions with the libnvme-mi API:
 *
 *  - All types and functions have the nvme_mi prefix, to distinguish from
 *    the libnvme core.
 *
 *  - We currently support either MI commands and Admin commands. The
 *    former adds a _mi prefix, the latter an _admin prefix. [This does
 *    result in the MI functions having a double _mi, like
 *    &nvme_mi_mi_subsystem_health_status_poll, which is apparently amusing
 *    for our German-speaking readers]
 *
 * For return values: unless specified in the per-function documentation,
 * all functions:
 *
 *  - return 0 on success
 *
 *  - return -1, with errno set, for errors communicating with the MI device,
 *    either in request or response data
 *
 *  - return >1 on MI status errors. This value is the 8-bit MI status
 *    value, represented by &enum nvme_mi_resp_status. Note that the
 *    status values may be vendor-defined above 0xe0.
 *
 * For the second case, we have a few conventions for errno values:
 *
 *  - EPROTO: response data violated the MI protocol, and libnvme cannot
 *    validly interpret the response
 *
 *  - EIO: Other I/O error communicating with device (eg., valid but
 *    unexpected response data)
 *
 *  - EINVAL: invalid input arguments for a command
 *
 * In line with the core NVMe API, the Admin command functions take an
 * `_args` structure to provide the command-specific parameters. However,
 * for the MI interface, the fd and timeout members of these _args structs
 * are ignored.
 *
 * References to the specifications here will either to be the NVM Express
 * Management Interface ("NVMe-MI") or the NVM Express Base specification
 * ("NVMe"). At the time of writing, the versions we're referencing here
 * are:
 *  - NVMe-MI 1.2b
 *  - NVMe 2.0b
 * with a couple of accommodations for older spec types, particularly NVMe-MI
 * 1.1, where possible.
 *
 */

#ifndef _LIBNVME_MI_MI_H
#define _LIBNVME_MI_MI_H

#include <endian.h>
#include <stdint.h>

#include "types.h"
#include "tree.h"

/**
 * NVME_MI_MSGTYPE_NVME - MCTP message type for NVMe-MI messages.
 *
 * This is defined by MCTP, but is referenced as part of the NVMe-MI message
 * spec. This is the MCTP NVMe message type (0x4), with the message-integrity
 * bit (0x80) set.
 */
#define NVME_MI_MSGTYPE_NVME 0x84

/* Basic MI message definitions */

/**
 * enum nvme_mi_message_type - NVMe-MI message type field.
 * @NVME_MI_MT_CONTROL: NVME-MI Control Primitive
 * @NVME_MI_MT_MI: NVMe-MI command
 * @NVME_MI_MT_ADMIN: NVMe Admin command
 * @NVME_MI_MT_PCIE: PCIe command
 *
 * Used as byte 1 of both request and response messages (NMIMT bits of NMP
 * byte). Not to be confused with the MCTP message type in byte 0.
 */
enum nvme_mi_message_type {
	NVME_MI_MT_CONTROL = 0,
	NVME_MI_MT_MI = 1,
	NVME_MI_MT_ADMIN = 2,
	NVME_MI_MT_PCIE = 4,
};

/**
 * enum nvme_mi_ror: Request or response field.
 * @NVME_MI_ROR_REQ: request message
 * @NVME_MI_ROR_RSP: response message
 */
enum nvme_mi_ror {
	NVME_MI_ROR_REQ = 0,
	NVME_MI_ROR_RSP = 1,
};

/**
 * enum nvme_mi_resp_status - values for the response status field
 * @NVME_MI_RESP_SUCCESS: success
 * @NVME_MI_RESP_MPR: More Processing Required
 * @NVME_MI_RESP_INTERNAL_ERR: Internal Error
 * @NVME_MI_RESP_INVALID_OPCODE: Invalid command opcode
 * @NVME_MI_RESP_INVALID_PARAM: Invalid command parameter
 * @NVME_MI_RESP_INVALID_CMD_SIZE: Invalid command size
 * @NVME_MI_RESP_INVALID_INPUT_SIZE: Invalid command input data size
 * @NVME_MI_RESP_ACCESS_DENIED: Access Denied
 * @NVME_MI_RESP_VPD_UPDATES_EXCEEDED: More VPD updates than allowed
 * @NVME_MI_RESP_PCIE_INACCESSIBLE: PCIe functionality currently unavailable
 * @NVME_MI_RESP_MEB_SANITIZED: MEB has been cleared due to sanitize
 * @NVME_MI_RESP_ENC_SERV_FAILURE: Enclosure services process failed
 * @NVME_MI_RESP_ENC_SERV_XFER_FAILURE: Transfer with enclosure services failed
 * @NVME_MI_RESP_ENC_FAILURE: Unreoverable enclosure failure
 * @NVME_MI_RESP_ENC_XFER_REFUSED: Enclosure services transfer refused
 * @NVME_MI_RESP_ENC_FUNC_UNSUP: Unsupported enclosure services function
 * @NVME_MI_RESP_ENC_SERV_UNAVAIL: Enclosure services unavailable
 * @NVME_MI_RESP_ENC_DEGRADED: Noncritical failure detected by enc. services
 * @NVME_MI_RESP_SANITIZE_IN_PROGRESS: Command prohibited during sanitize
 */
enum nvme_mi_resp_status {
	NVME_MI_RESP_SUCCESS = 0x00,
	NVME_MI_RESP_MPR = 0x01,
	NVME_MI_RESP_INTERNAL_ERR = 0x02,
	NVME_MI_RESP_INVALID_OPCODE = 0x03,
	NVME_MI_RESP_INVALID_PARAM = 0x04,
	NVME_MI_RESP_INVALID_CMD_SIZE = 0x05,
	NVME_MI_RESP_INVALID_INPUT_SIZE = 0x06,
	NVME_MI_RESP_ACCESS_DENIED = 0x07,
	/* 0x08 - 0x1f: reserved */
	NVME_MI_RESP_VPD_UPDATES_EXCEEDED = 0x20,
	NVME_MI_RESP_PCIE_INACCESSIBLE = 0x21,
	NVME_MI_RESP_MEB_SANITIZED = 0x22,
	NVME_MI_RESP_ENC_SERV_FAILURE = 0x23,
	NVME_MI_RESP_ENC_SERV_XFER_FAILURE = 0x24,
	NVME_MI_RESP_ENC_FAILURE = 0x25,
	NVME_MI_RESP_ENC_XFER_REFUSED = 0x26,
	NVME_MI_RESP_ENC_FUNC_UNSUP = 0x27,
	NVME_MI_RESP_ENC_SERV_UNAVAIL = 0x28,
	NVME_MI_RESP_ENC_DEGRADED = 0x29,
	NVME_MI_RESP_SANITIZE_IN_PROGRESS = 0x2a,
	/* 0x2b - 0xdf: reserved */
	/* 0xe0 - 0xff: vendor specific */
};

/**
 * struct nvme_mi_msg_hdr - General MI message header.
 * @type: MCTP message type, will always be NVME_MI_MSGTYPE_NVME
 * @nmp: NVMe-MI message parameters (including MI message type)
 * @meb: Management Endpoint Buffer flag; unused for libnvme-mi implementation
 * @rsvd0: currently reserved
 *
 * Wire format shared by both request and response messages, per NVMe-MI
 * section 3.1. This is used for all message types, MI and Admin.
 */
struct nvme_mi_msg_hdr {
	__u8	type;
	__u8	nmp;
	__u8	meb;
	__u8	rsvd0;
} __attribute__((packed));

/**
 * struct nvme_mi_msg_resp - Generic response type.
 * @hdr: the general request/response message header
 * @status: response status value (see &enum nvme_mi_resp_status)
 * @rsvd0: reserved data, may be defined by specific response
 *
 * Every response will start with one of these; command-specific responses
 * will define parts of the reserved data, and may add further fields.
 */
struct nvme_mi_msg_resp {
	struct nvme_mi_msg_hdr hdr;
	__u8	status;
	__u8	rsvd0[3];
};

/**
 * enum nvme_mi_mi_opcode - Operation code for supported NVMe-MI commands.
 * @nvme_mi_mi_opcode_mi_data_read: Read NVMe-MI Data Structure
 * @nvme_mi_mi_opcode_subsys_health_status_poll: Subsystem Health Status Poll
 * @nvme_mi_mi_opcode_configuration_set: MI Configuration Set
 * @nvme_mi_mi_opcode_configuration_get: MI Configuration Get
 */
enum nvme_mi_mi_opcode {
	nvme_mi_mi_opcode_mi_data_read = 0x00,
	nvme_mi_mi_opcode_subsys_health_status_poll = 0x01,
	nvme_mi_mi_opcode_configuration_set = 0x03,
	nvme_mi_mi_opcode_configuration_get = 0x04,
};

/**
 * struct nvme_mi_mi_req_hdr - MI request message header.
 * @hdr: generic MI message header
 * @opcode: opcode (OPC) for the specific MI command
 * @rsvd0: reserved bytes
 * @cdw0: Management Request Doubleword 0 - command specific usage
 * @cdw1: Management Request Doubleword 1 - command specific usage
 *
 * Wire format for MI request message headers, defined in section 5 of NVMe-MI.
 */
struct nvme_mi_mi_req_hdr {
	struct nvme_mi_msg_hdr hdr;
	__u8	opcode;
	__u8	rsvd0[3];
	__le32	cdw0, cdw1;
};

/**
 * struct nvme_mi_mi_resp_hdr - MI response message header.
 * @hdr: generic MI message header
 * @status: generic response status from command; non-zero on failure.
 * @nmresp: NVMe Management Response: command-type-specific response data
 *
 * Wire format for MI response message header, defined in section 5 of NVMe-MI.
 */
struct nvme_mi_mi_resp_hdr {
	struct nvme_mi_msg_hdr hdr;
	__u8	status;
	__u8	nmresp[3];
};

/**
 * enum nvme_mi_dtyp - Data Structure Type field.
 * @nvme_mi_dtyp_subsys_info: NVM Subsystem Information
 * @nvme_mi_dtyp_port_info: Port information
 * @nvme_mi_dtyp_ctrl_list: Controller List
 * @nvme_mi_dtyp_ctrl_info: Controller Information
 * @nvme_mi_dtyp_opt_cmd_support: Optionally Supported Command List
 * @nvme_mi_dtyp_meb_support: Management Endpoint Buffer Command Support List
 *
 * Data Structure Type field for Read NVMe-MI Data Structure command, used to
 * indicate the particular structure to query from the endpoint.
 */
enum nvme_mi_dtyp {
	nvme_mi_dtyp_subsys_info = 0x00,
	nvme_mi_dtyp_port_info = 0x01,
	nvme_mi_dtyp_ctrl_list = 0x02,
	nvme_mi_dtyp_ctrl_info = 0x03,
	nvme_mi_dtyp_opt_cmd_support = 0x04,
	nvme_mi_dtyp_meb_support = 0x05,
};

/**
 * enum nvme_mi_config_id - NVMe-MI Configuration identifier.
 * @NVME_MI_CONFIG_SMBUS_FREQ: Current SMBus/I2C frequency
 * @NVME_MI_CONFIG_HEALTH_STATUS_CHANGE: Health Status change - used to clear
 *                                       health status bits in CCS bits of
 *                                       status poll. Only for Set ops.
 * @NVME_MI_CONFIG_MCTP_MTU: MCTP maximum transmission unit size of port
 *                           specified in dw 0
 *
 * Configuration parameters for the MI Get/Set Configuration commands.
 *
 * See &nvme_mi_mi_config_get() and &nvme_mi_config_set().
 */
enum nvme_mi_config_id {
	NVME_MI_CONFIG_SMBUS_FREQ = 0x1,
	NVME_MI_CONFIG_HEALTH_STATUS_CHANGE = 0x2,
	NVME_MI_CONFIG_MCTP_MTU = 0x3,
};

/**
 * enum nvme_mi_config_smbus_freq - SMBus/I2C frequency values
 * @NVME_MI_CONFIG_SMBUS_FREQ_100kHz: 100kHz
 * @NVME_MI_CONFIG_SMBUS_FREQ_400kHz: 400kHz
 * @NVME_MI_CONFIG_SMBUS_FREQ_1MHz: 1MHz
 *
 * Values used in the SMBus Frequency device configuration. See
 * &nvme_mi_mi_config_get_smbus_freq() and &nvme_mi_mi_config_set_smbus_freq().
 */
enum nvme_mi_config_smbus_freq {
	NVME_MI_CONFIG_SMBUS_FREQ_100kHz = 0x1,
	NVME_MI_CONFIG_SMBUS_FREQ_400kHz = 0x2,
	NVME_MI_CONFIG_SMBUS_FREQ_1MHz = 0x3,
};

/* Admin command definitions */

/**
 * struct nvme_mi_admin_req_hdr - Admin command request header.
 * @hdr: Generic MI message header
 * @opcode: Admin command opcode (using enum nvme_admin_opcode)
 * @flags: Command Flags, indicating dlen and doff validity; Only defined in
 *         NVMe-MI version 1.1, no fields defined in 1.2 (where the dlen/doff
 *         are always considered valid).
 * @ctrl_id: Controller ID target of command
 * @cdw1: Submission Queue Entry doubleword 1
 * @cdw2: Submission Queue Entry doubleword 2
 * @cdw3: Submission Queue Entry doubleword 3
 * @cdw4: Submission Queue Entry doubleword 4
 * @cdw5: Submission Queue Entry doubleword 5
 * @doff: Offset of data to return from command
 * @dlen: Length of sent/returned data
 * @rsvd0: Reserved
 * @rsvd1: Reserved
 * @cdw10: Submission Queue Entry doubleword 10
 * @cdw11: Submission Queue Entry doubleword 11
 * @cdw12: Submission Queue Entry doubleword 12
 * @cdw13: Submission Queue Entry doubleword 13
 * @cdw14: Submission Queue Entry doubleword 14
 * @cdw15: Submission Queue Entry doubleword 15
 *
 * Wire format for Admin command message headers, defined in section 6 of
 * NVMe-MI.
 */
struct nvme_mi_admin_req_hdr {
	struct nvme_mi_msg_hdr hdr;
	__u8	opcode;
	__u8	flags;
	__le16	ctrl_id;
	__le32	cdw1, cdw2, cdw3, cdw4, cdw5;
	__le32	doff;
	__le32	dlen;
	__le32	rsvd0, rsvd1;
	__le32	cdw10, cdw11, cdw12, cdw13, cdw14, cdw15;
} __attribute((packed));

/**
 * struct nvme_mi_admin_resp_hdr - Admin command response header.
 * @hdr: Generic MI message header
 * @status: Generic response code, non-zero on failure
 * @rsvd0: Reserved
 * @cdw0: Completion Queue Entry doubleword 0
 * @cdw1: Completion Queue Entry doubleword 1
 * @cdw3: Completion Queue Entry doubleword 3
 *
 * This is the generic response format with the three doublewords of completion
 * queue data, plus optional response data.
 */
struct nvme_mi_admin_resp_hdr {
	struct nvme_mi_msg_hdr hdr;
	__u8	status;
	__u8	rsvd0[3];
	__le32	cdw0, cdw1, cdw3;
} __attribute__((packed));


/**
 * nvme_mi_create_root() - Create top-level MI (root) handle.
 * @fp:		File descriptor for logging messages
 * @log_level:	Logging level to use
 *
 * Create the top-level (library) handle for creating subsequent endpoint
 * objects. Similar to nvme_create_root(), but we provide this to allow linking
 * without the core libnvme.
 *
 * Return: new root object, or NULL on failure.
 *
 * See &nvme_create_root.
 */
nvme_root_t nvme_mi_create_root(FILE *fp, int log_level);

/**
 * nvme_mi_free_root() - Free root object.
 * @root: root to free
 */
void nvme_mi_free_root(nvme_root_t root);

/* Top level management object: NVMe-MI Management Endpoint */
struct nvme_mi_ep;

/**
 * typedef nvme_mi_ep_t - MI Endpoint object.
 *
 * Represents our communication endpoint on the remote MI-capable device.
 * To be used for direct MI commands for the endpoint (through the
 * nvme_mi_mi_* functions(), or to communicate with individual controllers
 * (see &nvme_mi_init_ctrl).
 *
 * Endpoints are created through a transport-specific constructor; currently
 * only MCTP-connected endpoints are supported, through &nvme_mi_open_mctp.
 * Subsequent operations on the endpoint (and related controllers) are
 * transport-independent.
 */
typedef struct nvme_mi_ep * nvme_mi_ep_t;

/**
 * nvme_mi_first_endpoint - Start endpoint iterator
 * @m: &nvme_root_t object
 *
 * Return: first MI endpoint object under this root, or NULL if no endpoints
 *         are present.
 *
 * See: &nvme_mi_next_endpoint, &nvme_mi_for_each_endpoint
 */
nvme_mi_ep_t nvme_mi_first_endpoint(nvme_root_t m);

/**
 * nvme_mi_next_endpoint - Continue endpoint iterator
 * @m: &nvme_root_t object
 * @e: &nvme_mi_ep_t current position of iterator
 *
 * Return: next endpoint MI endpoint object after @e under this root, or NULL
 *         if no further endpoints are present.
 *
 * See: &nvme_mi_first_endpoint, &nvme_mi_for_each_endpoint
 */
nvme_mi_ep_t nvme_mi_next_endpoint(nvme_root_t m, nvme_mi_ep_t e);

/**
 * nvme_mi_for_each_endpoint - Iterator for NVMe-MI endpoints.
 * @m: &nvme_root_t containing endpoints
 * @e: &nvme_mi_ep_t object, set on each iteration
 */
#define nvme_mi_for_each_endpoint(m, e)			\
	for (e = nvme_mi_first_endpoint(m); e != NULL;	\
	     e = nvme_mi_next_endpoint(m, e))

/**
 * nvme_mi_for_each_endpoint_safe - Iterator for NVMe-MI endpoints, allowing
 * deletion during traversal
 * @m: &nvme_root_t containing endpoints
 * @e: &nvme_mi_ep_t object, set on each iteration
 * @_e: &nvme_mi_ep_t object used as temporary storage
 */
#define nvme_mi_for_each_endpoint_safe(m, e, _e)			      \
	for (e = nvme_mi_first_endpoint(m), _e = nvme_mi_next_endpoint(m, e); \
	     e != NULL;							      \
	     e = _e, _e = nvme_mi_next_endpoint(m, e))

struct nvme_mi_ctrl;

/**
 * typedef nvme_mi_ctrl_t - NVMe-MI Controller object.
 *
 * Provides NVMe command functionality, through the MI interface.
 */
typedef struct nvme_mi_ctrl * nvme_mi_ctrl_t;

/**
 * nvme_mi_first_ctrl - Start controller iterator
 * @ep: &nvme_mi_ep_t object
 *
 * Return: first MI controller object under this root, or NULL if no controllers
 *         are present.
 *
 * See: &nvme_mi_next_ctrl, &nvme_mi_for_each_ctrl
 */
nvme_mi_ctrl_t nvme_mi_first_ctrl(nvme_mi_ep_t ep);

/**
 * nvme_mi_next_ctrl - Continue ctrl iterator
 * @ep: &nvme_mi_ep_t object
 * @c: &nvme_mi_ctrl_t current position of iterator
 *
 * Return: next MI controller object after @c under this endpoint, or NULL
 *         if no further controllers are present.
 *
 * See: &nvme_mi_first_ctrl, &nvme_mi_for_each_ctrl
 */
nvme_mi_ctrl_t nvme_mi_next_ctrl(nvme_mi_ep_t ep, nvme_mi_ctrl_t c);

/**
 * nvme_mi_for_each_ctrl - Iterator for NVMe-MI controllers.
 * @ep: &nvme_mi_ep_t containing endpoints
 * @c: &nvme_mi_ctrl_t object, set on each iteration
 *
 * Allows iteration of the list of controllers behind an endpoint. Unless the
 * controllers have already been created explicitly, you'll probably want to
 * call &nvme_mi_scan_ep() to scan for the controllers first.
 *
 * See: &nvme_mi_scan_ep()
 */
#define nvme_mi_for_each_ctrl(ep, c)			\
	for (c = nvme_mi_first_ctrl(ep); c != NULL;	\
	     c = nvme_mi_next_ctrl(ep, c))

/**
 * nvme_mi_for_each_ctrl_safe - Iterator for NVMe-MI controllers, allowing
 * deletion during traversal
 * @ep: &nvme_mi_ep_t containing controllers
 * @c: &nvme_mi_ctrl_t object, set on each iteration
 * @_c: &nvme_mi_ctrl_t object used as temporary storage
 *
 * Allows iteration of the list of controllers behind an endpoint, safe against
 * deletion during iteration. Unless the controllers have already been created
 * explicitly (or you're just iterating to destroy controllers) you'll probably
 * want to call &nvme_mi_scan_ep() to scan for the controllers first.
 *
 * See: &nvme_mi_scan_ep()
 */
#define nvme_mi_for_each_ctrl_safe(ep, c, _c)			      \
	for (c = nvme_mi_first_ctrl(ep), _c = nvme_mi_next_ctrl(ep, c);	      \
	     c != NULL;							      \
	     c = _c, _c = nvme_mi_next_ctrl(ep, c))

/**
 * nvme_mi_open_mctp() - Create an endpoint using a MCTP connection.
 * @root: root object to create under
 * @netid: MCTP network ID on this system
 * @eid: MCTP endpoint ID
 *
 * Transport-specific endpoint initialization for MI-connected endpoints. Once
 * an endpoint is created, the rest of the API is transport-independent.
 *
 * Return: New endpoint object for @netid & @eid, or NULL on failure.
 *
 * See &nvme_mi_close
 */
nvme_mi_ep_t nvme_mi_open_mctp(nvme_root_t root, unsigned int netid, uint8_t eid);

/**
 * nvme_mi_close() - Close an endpoint connection and release resources,
 * including controller objects.
 *
 * @ep: Endpoint object to close
 */
void nvme_mi_close(nvme_mi_ep_t ep);

/**
 * nvme_mi_scan_mctp - look for MCTP-connected NVMe-MI endpoints.
 *
 * Description: This function queries the system MCTP daemon ("mctpd") over
 * D-Bus, to find MCTP endpoints that report support for NVMe-MI over MCTP.
 *
 * This requires libvnme-mi to be compiled with D-Bus support; if not, this
 * will return NULL.
 *
 * Return: A @nvme_root_t populated with a set of MCTP-connected endpoints,
 *         or NULL on failure
 */
nvme_root_t nvme_mi_scan_mctp(void);

/**
 * nvme_mi_scan_ep - query an endpoint for its NVMe controllers.
 * @ep: Endpoint to scan
 * @force_rescan: close existing controllers and rescan
 *
 * This function queries an MI endpoint for the controllers available, by
 * performing an MI Read MI Data Structure command (requesting the
 * controller list). The controllers are stored in the endpoint's internal
 * list, and can be iterated with nvme_mi_for_each_ctrl.
 *
 * This will only scan the endpoint once, unless @force_rescan is set. If
 * so, all existing controller objects will be freed - the caller must not
 * hold a reference to those across this call.
 *
 * Return: 0 on success, non-zero on failure
 *
 * See: &nvme_mi_for_each_ctrl
 */
int nvme_mi_scan_ep(nvme_mi_ep_t ep, bool force_rescan);

/**
 * nvme_mi_init_ctrl() - initialise a NVMe controller.
 * @ep: Endpoint to create under
 * @ctrl_id: ID of controller to initialize.
 *
 * Create a connection to a controller behind the endpoint specified in @ep.
 * Controller IDs may be queried from the endpoint through
 * &nvme_mi_mi_read_mi_data_ctrl_list.
 *
 * Return: New controller object, or NULL on failure.
 *
 * See &nvme_mi_close_ctrl
 */
nvme_mi_ctrl_t nvme_mi_init_ctrl(nvme_mi_ep_t ep, __u16 ctrl_id);

/**
 * nvme_mi_close_ctrl() - free a controller
 * @ctrl: controller to free
 */
void nvme_mi_close_ctrl(nvme_mi_ctrl_t ctrl);

/**
 * nvme_mi_endpoint_desc - Get a string describing a MI endpoint.
 * @ep: endpoint to describe
 *
 * Generates a human-readable string describing the endpoint, with possibly
 * transport-specific data. The string is allocated during the call, and the
 * caller is responsible for free()-ing the string.
 *
 * Return: a newly-allocated string containing the endpoint description, or
 *         NULL on failure.
 */
char *nvme_mi_endpoint_desc(nvme_mi_ep_t ep);

/* MI Command API: nvme_mi_mi_ prefix */

/**
 * nvme_mi_mi_read_mi_data_subsys() - Perform a Read MI Data Structure command,
 * retrieving subsystem data.
 * @ep: endpoint for MI communication
 * @s: subsystem information to populate
 *
 * Retrieves the Subsystem information - number of external ports and
 * NVMe version information. See &struct nvme_mi_read_nvm_ss_info.
 *
 * Return: 0 on success, non-zero on failure.
 */
int nvme_mi_mi_read_mi_data_subsys(nvme_mi_ep_t ep,
				   struct nvme_mi_read_nvm_ss_info *s);

/**
 * nvme_mi_mi_read_mi_data_port() - Perform a Read MI Data Structure command,
 * retrieving port data.
 * @ep: endpoint for MI communication
 * @portid: id of port data to retrieve
 * @p: port information to populate
 *
 * Retrieves the Port information, for the specified port ID. The subsystem
 * data (from &nvme_mi_mi_read_mi_data_subsys) nmp field contains the allowed
 * range of port IDs.
 *
 * See &struct nvme_mi_read_port_info.
 *
 * Return: 0 on success, non-zero on failure.
 */
int nvme_mi_mi_read_mi_data_port(nvme_mi_ep_t ep, __u8 portid,
				 struct nvme_mi_read_port_info *p);

/**
 * nvme_mi_mi_read_mi_data_ctrl_list() - Perform a Read MI Data Structure
 * command, retrieving the list of attached controllers.
 * @ep: endpoint for MI communication
 * @start_ctrlid: starting controller ID
 * @list: controller list to populate
 *
 * Retrieves the list of attached controllers, with IDs greater than or
 * equal to @start_ctrlid.
 *
 * See &struct nvme_ctrl_list.
 *
 * Return: 0 on success, non-zero on failure.
 */
int nvme_mi_mi_read_mi_data_ctrl_list(nvme_mi_ep_t ep, __u8 start_ctrlid,
				      struct nvme_ctrl_list *list);

/**
 * nvme_mi_mi_read_mi_data_ctrl() - Perform a Read MI Data Structure command,
 * retrieving controller information
 * @ep: endpoint for MI communication
 * @ctrl_id: ID of controller to query
 * @ctrl: controller data to populate
 *
 * Retrieves the Controller Information Data Structure for the attached
 * controller with ID @ctrlid.
 *
 * See &struct nvme_mi_read_ctrl_info.
 *
 * Return: 0 on success, non-zero on failure.
 */
int nvme_mi_mi_read_mi_data_ctrl(nvme_mi_ep_t ep, __u16 ctrl_id,
				 struct nvme_mi_read_ctrl_info *ctrl);

/**
 * nvme_mi_mi_subsystem_health_status_poll() - Read the Subsystem Health
 * Data Structure from the NVM subsystem
 * @ep: endpoint for MI communication
 * @clear: flag to clear the Composite Controller Status state
 * @nshds: subsystem health status data to populate
 *
 * Retrieves the Subsystem Health Data Structure into @nshds. If @clear is
 * set, requests that the Composite Controller Status bits are cleared after
 * the read. See NVMe-MI section 5.6 for details on the CCS bits.
 *
 * See &struct nvme_mi_nvm_ss_health_status.
 *
 * Return: 0 on success, non-zero on failure.
 */
int nvme_mi_mi_subsystem_health_status_poll(nvme_mi_ep_t ep, bool clear,
					    struct nvme_mi_nvm_ss_health_status *nshds);

/**
 * nvme_mi_mi_config_get - query a configuration parameter
 * @ep: endpoint for MI communication
 * @dw0: management doubleword 0, containing configuration identifier, plus
 *       config-specific fields
 * @dw1: management doubleword 0, config-specific.
 * @nmresp: set to queried configuration data in NMRESP field of response.
 *
 * Performs a MI Configuration Get command, with the configuration identifier
 * as the LSB of @dw0. Other @dw0 and @dw1 data is configuration-identifier
 * specific.
 *
 * On a successful Configuration Get, the @nmresp pointer will be populated with
 * the bytes from the 3-byte NMRESP field, converted to native endian.
 *
 * See &enum nvme_mi_config_id for identifiers.
 *
 * Return: 0 on success, non-zero on failure.
 */
int nvme_mi_mi_config_get(nvme_mi_ep_t ep, __u32 dw0, __u32 dw1,
			  __u32 *nmresp);

/**
 * nvme_mi_mi_config_set - set a configuration parameter
 * @ep: endpoint for MI communication
 * @dw0: management doubleword 0, containing configuration identifier, plus
 *       config-specific fields
 * @dw1: management doubleword 0, config-specific.
 *
 * Performs a MI Configuration Set command, with the command as the LSB of
 * @dw0. Other @dw0 and @dw1 data is configuration-identifier specific.
 *
 * See &enum nvme_mi_config_id for identifiers.
 *
 * Return: 0 on success, non-zero on failure.
 */
int nvme_mi_mi_config_set(nvme_mi_ep_t ep, __u32 dw0, __u32 dw1);

/**
 * nvme_mi_mi_config_get_smbus_freq - get configuration: SMBus port frequency
 * @ep: endpoint for MI communication
 * @port: port ID to query
 * @freq: output value for current frequency configuration
 *
 * Performs a MI Configuration Get, to query the current SMBus frequency of
 * the port specified in @port. On success, populates @freq with the port
 * frequency
 *
 * Return: 0 on success, non-zero on failure.
 */
static inline int nvme_mi_mi_config_get_smbus_freq(nvme_mi_ep_t ep, __u8 port,
						   enum nvme_mi_config_smbus_freq *freq)
{
	__u32 tmp, dw0;
	int rc;

	dw0 = port << 24 | NVME_MI_CONFIG_SMBUS_FREQ;

	rc = nvme_mi_mi_config_get(ep, dw0, 0, &tmp);
	if (!rc)
		*freq = tmp & 0x3;
	return rc;
}

/**
 * nvme_mi_mi_config_set_smbus_freq - set configuration: SMBus port frequency
 * @ep: endpoint for MI communication
 * @port: port ID to set
 * @freq: new frequency configuration
 *
 * Performs a MI Configuration Set, to update the current SMBus frequency of
 * the port specified in @port.
 *
 * See &struct nvme_mi_read_port_info for the maximum supported SMBus frequency
 * for the port.
 *
 * Return: 0 on success, non-zero on failure.
 */
static inline int nvme_mi_mi_config_set_smbus_freq(nvme_mi_ep_t ep, __u8 port,
						   enum nvme_mi_config_smbus_freq freq)
{
	__u32 dw0 = port << 24 |
		(freq & 0x3) << 8 |
		NVME_MI_CONFIG_SMBUS_FREQ;

	return nvme_mi_mi_config_set(ep, dw0, 0);
}

/**
 * nvme_mi_mi_config_set_health_status_change - clear CCS bits in health status
 * @ep: endpoint for MI communication
 * @mask: bitmask to clear
 *
 * Performs a MI Configuration Set, to update the current health status poll
 * values of the Composite Controller Status bits. Bits set in @mask will
 * be cleared from future health status poll data, and may be re-triggered by
 * a future health change event.
 *
 * See &nvme_mi_mi_subsystem_health_status_poll(), &enum nvme_mi_ccs for
 * values in @mask.
 *
 * Return: 0 on success, non-zero on failure.
 */
static inline int nvme_mi_mi_config_set_health_status_change(nvme_mi_ep_t ep,
							     __u32 mask)
{
	return nvme_mi_mi_config_set(ep, NVME_MI_CONFIG_HEALTH_STATUS_CHANGE,
				     mask);
}

/**
 * nvme_mi_mi_config_get_mctp_mtu - get configuration: MCTP MTU
 * @ep: endpoint for MI communication
 * @port: port ID to query
 * @mtu: output value for current MCTP MTU configuration
 *
 * Performs a MI Configuration Get, to query the current MCTP Maximum
 * Transmission Unit size (MTU) of the port specified in @port. On success,
 * populates @mtu with the MTU.
 *
 * The default reset value is 64, corresponding to the MCTP baseline MTU.
 *
 * Some controllers may also use this as the maximum receive unit size, and
 * may not accept MCTP messages larger than the configured MTU.
 *
 * Return: 0 on success, non-zero on failure.
 */
static inline int nvme_mi_mi_config_get_mctp_mtu(nvme_mi_ep_t ep, __u8 port,
						 __u16 *mtu)
{
	__u32 tmp, dw0;
	int rc;

	dw0 = port << 24 | NVME_MI_CONFIG_MCTP_MTU;

	rc = nvme_mi_mi_config_get(ep, dw0, 0, &tmp);
	if (!rc)
		*mtu = tmp & 0xffff;
	return rc;
}

/**
 * nvme_mi_mi_config_set_mctp_mtu - set configuration: MCTP MTU
 * @ep: endpoint for MI communication
 * @port: port ID to set
 * @mtu: new MTU configuration
 *
 * Performs a MI Configuration Set, to update the current MCTP MTU value for
 * the port specified in @port.
 *
 * Some controllers may also use this as the maximum receive unit size, and
 * may not accept MCTP messages larger than the configured MTU. When setting
 * this value, you will likely need to change the MTU of the local MCTP
 * interface(s) to match.
 *
 * Return: 0 on success, non-zero on failure.
 */
static inline int nvme_mi_mi_config_set_mctp_mtu(nvme_mi_ep_t ep, __u8 port,
						 __u16 mtu)
{
	__u32 dw0 = port << 24 | NVME_MI_CONFIG_MCTP_MTU;

	return nvme_mi_mi_config_set(ep, dw0, mtu);
}

/* Admin channel functions */

/**
 * nvme_mi_admin_xfer() -  Raw admin transfer interface.
 * @ctrl: controller to send the admin command to
 * @admin_req: request data
 * @req_data_size: size of request data payload
 * @admin_resp: buffer for response data
 * @resp_data_offset: offset into request data to retrieve from controller
 * @resp_data_size: size of response data buffer, updated to received size
 *
 * Performs an arbitrary NVMe Admin command, using the provided request data,
 * in @admin_req. The size of the request data *payload* is specified in
 * @req_data_size - this does not include the standard header length (so a
 * header-only request would have a size of 0).
 *
 * On success, response data is stored in @admin_resp, which has an optional
 * appended payload buffer of @resp_data_size bytes. The actual payload
 * transferred will be stored in @resp_data_size. These sizes do not include
 * the Admin request header, so 0 represents no payload.
 *
 * As with all Admin commands, we can request partial data from the Admin
 * Response payload, offset by @resp_data_offset.
 *
 * See: &struct nvme_mi_admin_req_hdr and &struct nvme_mi_admin_resp_hdr.
 *
 * Return: 0 on success, non-zero on failure.
 */
int nvme_mi_admin_xfer(nvme_mi_ctrl_t ctrl,
		       struct nvme_mi_admin_req_hdr *admin_req,
		       size_t req_data_size,
		       struct nvme_mi_admin_resp_hdr *admin_resp,
		       off_t resp_data_offset,
		       size_t *resp_data_size);

/**
 * nvme_mi_admin_identify_partial() - Perform an Admin identify command,
 * and retrieve partial response data.
 * @ctrl: Controller to process identify command
 * @args: Identify command arguments
 * @offset: offset of identify data to retrieve from response
 * @size: size of identify data to return
 *
 * Perform an Identify command, using the Identify command parameters in @args.
 * The @offset and @size arguments allow the caller to retrieve part of
 * the identify response. See NVMe-MI section 6.2 for the semantics (and some
 * handy diagrams) of the offset & size parameters.
 *
 * Will return an error if the length of the response data (from the controller)
 * did not match @size.
 *
 * Unless you're performing a vendor-unique identify command, You'll probably
 * want to use one of the identify helpers (nvme_mi_admin_identify,
 * nvme_mi_admin_identify_cns_nsid, or nvme_mi_admin_identify_<type>) instead
 * of this. If the type of your identify command is standardized but not
 * yet supported by libnvme-mi, please contact the maintainers.
 *
 * Return: 0 on success, non-zero on failure
 *
 * See: &struct nvme_identify_args
 */
int nvme_mi_admin_identify_partial(nvme_mi_ctrl_t ctrl,
				   struct nvme_identify_args *args,
				   off_t offset, size_t size);

/**
 * nvme_mi_admin_identify() - Perform an Admin identify command.
 * @ctrl: Controller to process identify command
 * @args: Identify command arguments
 *
 * Perform an Identify command, using the Identify command parameters in @args.
 * Stores the identify data in ->data, and (if set) the result from cdw0
 * into args->result.
 *
 * Will return an error if the length of the response data (from the
 * controller) is not a full &NVME_IDENTIFY_DATA_SIZE.
 *
 * Return: 0 on success, non-zero on failure
 *
 * See: &struct nvme_identify_args
 */
static inline int nvme_mi_admin_identify(nvme_mi_ctrl_t ctrl,
					 struct nvme_identify_args *args)
{
	return nvme_mi_admin_identify_partial(ctrl, args,
					      0, NVME_IDENTIFY_DATA_SIZE);
}

/**
 * nvme_mi_admin_identify_cns_nsid() - Perform an Admin identify command using
 * specific CNS/NSID parameters.
 * @ctrl: Controller to process identify command
 * @cns: Controller or Namespace Structure, specifying identified object
 * @nsid: namespace ID
 * @data: buffer for identify data response
 *
 * Perform an Identify command, using the CNS specifier @cns, and the
 * namespace ID @nsid if required by the CNS type.
 *
 * Stores the identify data in @data, which is expected to be a buffer of
 * &NVME_IDENTIFY_DATA_SIZE bytes.
 *
 * Will return an error if the length of the response data (from the
 * controller) is not a full &NVME_IDENTIFY_DATA_SIZE.
 *
 * Return: 0 on success, non-zero on failure
 */
static inline int nvme_mi_admin_identify_cns_nsid(nvme_mi_ctrl_t ctrl,
						  enum nvme_identify_cns cns,
						  __u32 nsid, void *data)
{
	struct nvme_identify_args args = {
		.result = NULL,
		.data = data,
		.args_size = sizeof(args),
		.cns = cns,
		.csi = NVME_CSI_NVM,
		.nsid = nsid,
		.cntid = NVME_CNTLID_NONE,
		.cns_specific_id = NVME_CNSSPECID_NONE,
		.uuidx = NVME_UUID_NONE,
	};

	return nvme_mi_admin_identify(ctrl, &args);
}

/**
 * nvme_mi_admin_identify_ctrl() - Perform an Admin identify for a controller
 * @ctrl: Controller to process identify command
 * @id: Controller identify data to populate
 *
 * Perform an Identify command, for the controller specified by @ctrl,
 * writing identify data to @id.
 *
 * Will return an error if the length of the response data (from the
 * controller) is not a full &NVME_IDENTIFY_DATA_SIZE, so @id will be
 * fully populated on success.
 *
 * Return: 0 on success, non-zero on failure
 *
 * See: &struct nvme_id_ctrl
 */
static inline int nvme_mi_admin_identify_ctrl(nvme_mi_ctrl_t ctrl,
					      struct nvme_id_ctrl *id)
{
	return nvme_mi_admin_identify_cns_nsid(ctrl, NVME_IDENTIFY_CNS_CTRL,
					       NVME_NSID_NONE, id);
}

/**
 * nvme_mi_admin_identify_ctrl_list() - Perform an Admin identify for a
 * controller list.
 * @ctrl: Controller to process identify command
 * @cntid: Controller ID to specify list start
 * @list: List data to populate
 *
 * Perform an Identify command, for the controller list starting with
 * IDs greater than or equal to @cntid.
 *
 * Will return an error if the length of the response data (from the
 * controller) is not a full &NVME_IDENTIFY_DATA_SIZE, so @id will be
 * fully populated on success.
 *
 * Return: 0 on success, non-zero on failure
 *
 * See: &struct nvme_ctrl_list
 */
static inline int nvme_mi_admin_identify_ctrl_list(nvme_mi_ctrl_t ctrl,
						   __u16 cntid,
						   struct nvme_ctrl_list *list)
{
	struct nvme_identify_args args = {
		.result = NULL,
		.data = list,
		.args_size = sizeof(args),
		.cns = NVME_IDENTIFY_CNS_CTRL_LIST,
		.csi = NVME_CSI_NVM,
		.nsid = NVME_NSID_NONE,
		.cntid = cntid,
		.cns_specific_id = NVME_CNSSPECID_NONE,
		.uuidx = NVME_UUID_NONE,
	};

	return nvme_mi_admin_identify(ctrl, &args);
}

/**
 * nvme_mi_admin_get_log_page() - Retrieve log page data from controller
 * @ctrl: Controller to query
 * @args: Get Log Page command arguments
 *
 * Performs a Get Log Page Admin command as specified by @args. Response data
 * is stored in @args->data, which should be a buffer of @args->data_len bytes.
 * Resulting data length is stored in @args->data_len on successful
 * command completion.
 *
 * This request may be implemented as multiple log page commands, in order
 * to fit within MI message-size limits.
 *
 * Return: 0 on success, non-zero on failure
 *
 * See: &struct nvme_get_log_args
 */
int nvme_mi_admin_get_log_page(nvme_mi_ctrl_t ctrl,
			       struct nvme_get_log_args *args);

/**
 * nvme_mi_admin_security_send() - Perform a Security Send command on a
 * controller.
 * @ctrl: Controller to send command to
 * @args: Security Send command arguments
 *
 * Performs a Security Send Admin command as specified by @args. Response data
 * is stored in @args->data, which should be a buffer of @args->data_len bytes.
 * Resulting data length is stored in @args->data_len on successful
 * command completion.
 *
 * Security Send data length should not be greater than 4096 bytes to
 * comply with specification limits.
 *
 * Return: 0 on success, non-zero on failure
 *
 * See: &struct nvme_get_log_args
 */
int nvme_mi_admin_security_send(nvme_mi_ctrl_t ctrl,
				struct nvme_security_send_args *args);

/**
 * nvme_mi_admin_security_recv() - Perform a Security Receive command on a
 * controller.
 * @ctrl: Controller to send command to
 * @args: Security Receive command arguments
 *
 * Performs a Security Receive Admin command as specified by @args. Response
 * data is stored in @args->data, which should be a buffer of @args->data_len
 * bytes. Resulting data length is stored in @args->data_len on successful
 * command completion.
 *
 * Security Receive data length should not be greater than 4096 bytes to
 * comply with specification limits.
 *
 * Return: 0 on success, non-zero on failure
 *
 * See: &struct nvme_get_log_args
 */
int nvme_mi_admin_security_recv(nvme_mi_ctrl_t ctrl,
				struct nvme_security_receive_args *args);


#endif /* _LIBNVME_MI_MI_H */
