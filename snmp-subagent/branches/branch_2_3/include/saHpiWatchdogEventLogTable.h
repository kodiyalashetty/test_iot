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
 *   Daniel de Araujo <ddearauj@us.ibm.com>
 *
 * Note: this file originally auto-generated by mib2c using
 *        : mib2c.array-user.conf,v 5.18.2.2 2004/02/09 18:21:47 rstory Exp $
 *
 * $Id$
 *
 * Yes, there is lots of code here that you might not use. But it is much
 * easier to remove code than to add it!
 */
#ifndef SAHPIWATCHDOGEVENTLOGTABLE_H
#define SAHPIWATCHDOGEVENTLOGTABLE_H

#ifdef __cplusplus
extern "C" {
#endif

    
#include <net-snmp/net-snmp-config.h>
#include <net-snmp/library/container.h>
#include <net-snmp/agent/table_array.h>

#include <hpiSubagent.h>
        /** Index saHpiDomainId is external */
        /** Index saHpiResourceId is external */
        /** Index saHpiWatchdogNum is external */
        /** Index saHpiEventSeverity is external */
        /** Index saHpiWatchdogEventEntryId is external */

typedef struct saHpiWatchdogEventLogTable_context_s {
    netsnmp_index index; /** THIS MUST BE FIRST!!! */

    /*************************************************************
     * You can store data internally in this structure.
     *
     * TODO: You will probably have to fix a few types here...
     */
    /** TODO: add storage for external index(s)! */
        /** SaHpiTime = ASN_OCTET_STR */
            unsigned char saHpiWatchdogEventLogTimestamp[SAF_UNSIGNED_64_LEN];
	    long saHpiWatchdogEventLogTimestamp_len;

        /** INTEGER = ASN_INTEGER */
            long saHpiWatchdogEventLogAction;

        /** SaHpiWatchdogPreTimerAction = ASN_INTEGER */
            long saHpiWatchdogEventLogPreTimerAction;

        /** SaHpiWatchdogTimerUse = ASN_INTEGER */
            long saHpiWatchdogEventLogUse;


    /*
     * OR
     *
     * Keep a pointer to your data
     */
    void * data;

    /*
     *add anything else you want here
     */

} saHpiWatchdogEventLogTable_context;

/*************************************************************
 * function declarations
 */
void init_saHpiWatchdogEventLogTable(void);
void initialize_table_saHpiWatchdogEventLogTable(void);
const saHpiWatchdogEventLogTable_context * saHpiWatchdogEventLogTable_get_by_idx(netsnmp_index *);
const saHpiWatchdogEventLogTable_context * saHpiWatchdogEventLogTable_get_by_idx_rs(netsnmp_index *,
                                        int row_status);
int saHpiWatchdogEventLogTable_get_value(netsnmp_request_info *, netsnmp_index *, netsnmp_table_request_info *);

/*************************************************************
 * function declarations
 */
SaErrorT populate_saHpiWatchdogEventLogTable(SaHpiSessionIdT sessionid, 
                                            SaHpiEventLogEntryT *event,
                                            oid * this_child_oid, 
                                            size_t *this_child_oid_len);

SaErrorT watchdog_event_log_clear(SaHpiSessionIdT session_id, 
                                  SaHpiResourceIdT resource_id,  
                                  oid *saHpiEventLogRowPointer, 
                                  size_t saHpiEventLogRowPointer_len,
				  int modifyTotal);

/*************************************************************
 * oid declarations
 */
extern oid saHpiWatchdogEventLogTable_oid[];
extern size_t saHpiWatchdogEventLogTable_oid_len;

#define saHpiWatchdogEventLogTable_TABLE_OID 1,3,6,1,4,1,18568,2,1,1,3,2,20
    
/*************************************************************
 * column number definitions for table saHpiWatchdogEventLogTable
 */
 
#define WATCHDOG_EVENT_LOG_INDEX_NR 5
#define COLUMN_SAHPIWATCHDOGEVENTLOGTIMESTAMP 1
#define COLUMN_SAHPIWATCHDOGEVENTLOGACTION 2
#define COLUMN_SAHPIWATCHDOGEVENTLOGPRETIMERACTION 3
#define COLUMN_SAHPIWATCHDOGEVENTLOGUSE 4
#define saHpiWatchdogEventLogTable_COL_MIN 1
#define saHpiWatchdogEventLogTable_COL_MAX 4

/* comment out the following line if you don't handle SET-REQUEST for saHpiWatchdogEventLogTable */
#define saHpiWatchdogEventLogTable_SET_HANDLING

/* comment out the following line if you can't create new rows */
#define saHpiWatchdogEventLogTable_ROW_CREATION

/* comment out the following line if you don't want the secondary index */
#define saHpiWatchdogEventLogTable_IDX2

/* uncommend the following line if you allow modifications to an
 * active row */
/** define saHpiWatchdogEventLogTable_CAN_MODIFY_ACTIVE_ROW */

#ifdef saHpiWatchdogEventLogTable_SET_HANDLING

int saHpiWatchdogEventLogTable_extract_index( saHpiWatchdogEventLogTable_context * ctx, netsnmp_index * hdr );

void saHpiWatchdogEventLogTable_set_reserve1( netsnmp_request_group * );
void saHpiWatchdogEventLogTable_set_reserve2( netsnmp_request_group * );
void saHpiWatchdogEventLogTable_set_action( netsnmp_request_group * );
void saHpiWatchdogEventLogTable_set_commit( netsnmp_request_group * );
void saHpiWatchdogEventLogTable_set_free( netsnmp_request_group * );
void saHpiWatchdogEventLogTable_set_undo( netsnmp_request_group * );

saHpiWatchdogEventLogTable_context * saHpiWatchdogEventLogTable_duplicate_row( saHpiWatchdogEventLogTable_context* );
netsnmp_index * saHpiWatchdogEventLogTable_delete_row( saHpiWatchdogEventLogTable_context* );

int saHpiWatchdogEventLogTable_can_activate(saHpiWatchdogEventLogTable_context *undo_ctx,
                      saHpiWatchdogEventLogTable_context *row_ctx,
                      netsnmp_request_group * rg);
int saHpiWatchdogEventLogTable_can_deactivate(saHpiWatchdogEventLogTable_context *undo_ctx,
                        saHpiWatchdogEventLogTable_context *row_ctx,
                        netsnmp_request_group * rg);
int saHpiWatchdogEventLogTable_can_delete(saHpiWatchdogEventLogTable_context *undo_ctx,
                    saHpiWatchdogEventLogTable_context *row_ctx,
                    netsnmp_request_group * rg);
    
    
#ifdef saHpiWatchdogEventLogTable_ROW_CREATION
saHpiWatchdogEventLogTable_context * saHpiWatchdogEventLogTable_create_row( netsnmp_index* );
#endif
#endif

#ifdef saHpiWatchdogEventLogTable_IDX2
saHpiWatchdogEventLogTable_context * saHpiWatchdogEventLogTable_get( const char *name, int len );
#endif

#ifdef __cplusplus
};
#endif

#endif /** SAHPIWATCHDOGEVENTLOGTABLE_H */
