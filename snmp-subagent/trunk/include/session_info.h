/*
 * (C) Copyright IBM Corp. 2005
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  This
 * file and program are licensed under a BSD style license.  See
 * the Copying file included with the OpenHPI distribution for
 * full licensing terms.
 *
 * Authors:
 *   David Judkovics  <djudkovi@us.ibm.com>
 *
 *					  
 */

#ifndef _SESSION_INFO_H_
#define _SESSION_INFO_H_

#include <net-snmp/net-snmp-config.h>
#include <net-snmp/net-snmp-includes.h>
#include <net-snmp/agent/net-snmp-agent-includes.h>
#include <signal.h>

#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

#include <hpiSubagent.h>

#include <SaHpi.h> 
#include <oh_utils.h>

#include <alarm.h>
#include <oh_error.h>

/**************************************************/
/*** BEGIN: ***************************************/
/*** Session Domian mappings                    ***/
/**************************************************/
/**************************************************/
void store_session_info(SaHpiSessionIdT session_id, SaHpiDomainIdT domain_id);

SaHpiSessionIdT get_session_id(SaHpiDomainIdT domain_id);

SaHpiDomainIdT get_domain_id(SaHpiSessionIdT session_id);

/**************************************************/
/*** BEGIN: ***************************************/
/*** Creates full oid, used for such things as  ***/
/*** RowPointers and Notifications              ***/
/**************************************************/
/**************************************************/
int build_full_oid (oid * prefix, size_t prefix_len,
		    oid * column, size_t column_len,
		    netsnmp_index * index,
		    oid * out_oid, size_t in_len, size_t * out_len);

/**************************************************/
/*** BEGIN: ***************************************/
/*** Translates from HPI to SNMP Error Codes s  ***/
/**************************************************/
/**************************************************/
int get_snmp_error(SaErrorT val);

/**************************************************/
/*** BEGIN: ***************************************/
/*** Hash Table Used for generating and         ***/
/*** tracking unique indices when required      ***/
/**************************************************/
/**************************************************/
typedef struct {
	SaHpiEntryIdT domainId_resourceId_arry[2];
} SaHpiDomainIdResourceIdArrayT;


typedef struct {
        SaHpiEntryIdT entry_id;
        SaHpiDomainIdResourceIdArrayT dr_pair;
} DR_XREF;

/* hpi internal apis */
SaErrorT domain_resource_pair_initialize(int *initialized, GHashTable **oh_ep_table); 
DR_XREF *domain_resource_pair_get(SaHpiDomainIdResourceIdArrayT *ep, GHashTable **oh_ep_table); 
DR_XREF *domain_resoruce_pair_lookup(SaHpiDomainIdResourceIdArrayT *ep, GHashTable **oh_ep_table);

#endif //_SESSION_INFO_H_
