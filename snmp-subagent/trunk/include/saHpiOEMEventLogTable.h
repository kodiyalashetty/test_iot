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
#ifndef SAHPIOemEVENTLOGTABLE_H
#define SAHPIOemEVENTLOGTABLE_H

#ifdef __cplusplus
extern "C" {
#endif

    
#include <net-snmp/net-snmp-config.h>
#include <net-snmp/library/container.h>
#include <net-snmp/agent/table_array.h>

        /** Index saHpiDomainId is external */
        /** Index saHpiResourceId is external */
        /** Index saHpiEventSeverity is external */
        /** Index saHpiOemEventEntryId is external */

typedef struct saHpiOemEventLogTable_context_s {
    netsnmp_index index; /** THIS MUST BE FIRST!!! */

    /*************************************************************
     * You can store data internally in this structure.
     *
     * TODO: You will probably have to fix a few types here...
     */
    /** TODO: add storage for external index(s)! */
        /** SaHpiTime = ASN_COUNTER64 */
    /** TODO: Is this type correct? */
            struct counter64 saHpiOemEventLogTimestamp;

        /** SaHpiManufacturerId = ASN_UNSIGNED */
            unsigned long saHpiOemEventLogManufacturerIdT;

        /** SaHpiTextType = ASN_INTEGER */
            long saHpiOemEventLogTextType;

        /** SaHpiTextLanguage = ASN_INTEGER */
            long saHpiOemEventLogTextLanguage;

        /** SaHpiText = ASN_OCTET_STR */
            unsigned char saHpiOemEventLogText[SAHPI_MAX_TEXT_BUFFER_LENGTH];
            long saHpiOemEventLogText_len;


    /*
     * OR
     *
     * Keep a pointer to your data
     */
    void * data;

    /*
     *add anything else you want here
     */

} saHpiOemEventLogTable_context;

/*************************************************************
 * function declarations
 */
void init_saHpiOemEventLogTable(void);
void initialize_table_saHpiOemEventLogTable(void);
const saHpiOemEventLogTable_context * saHpiOemEventLogTable_get_by_idx(netsnmp_index *);
const saHpiOemEventLogTable_context * saHpiOemEventLogTable_get_by_idx_rs(netsnmp_index *,
                                        int row_status);
int saHpiOemEventLogTable_get_value(netsnmp_request_info *, netsnmp_index *, netsnmp_table_request_info *);


/*************************************************************
 * function declarations
 */
SaErrorT populate_saHpiOemEventLogTable(SaHpiSessionIdT sessionid, 
                                             SaHpiEventLogEntryT *event,
                                             oid * this_child_oid, 
                                             size_t *this_child_oid_len);

SaErrorT oem_event_log_clear(SaHpiSessionIdT session_id, 
                             SaHpiResourceIdT resource_id,  
                             oid *saHpiEventLogRowPointer, 
                             size_t saHpiEventLogRowPointer_len,
			     int modifyTotal);

/*************************************************************
 * oid declarations
 */
extern oid saHpiOemEventLogTable_oid[];
extern size_t saHpiOemEventLogTable_oid_len;

#define saHpiOemEventLogTable_TABLE_OID 1,3,6,1,4,1,18568,2,1,1,3,2,26
    
/*************************************************************
 * column number definitions for table saHpiOemEventLogTable
 */

#define Oem_EVENT_LOG_INDEX_NR 4
#define COLUMN_SAHPIOemEVENTLOGTIMESTAMP 1
#define COLUMN_SAHPIOemEVENTLOGMANUFACTURERIDT 2
#define COLUMN_SAHPIOemEVENTLOGTEXTTYPE 3
#define COLUMN_SAHPIOemEVENTLOGTEXTLANGUAGE 4
#define COLUMN_SAHPIOemEVENTLOGTEXT 5
#define saHpiOemEventLogTable_COL_MIN 1
#define saHpiOemEventLogTable_COL_MAX 5

/* comment out the following line if you don't handle SET-REQUEST for saHpiOemEventLogTable */
#define saHpiOemEventLogTable_SET_HANDLING

/* comment out the following line if you can't create new rows */
#define saHpiOemEventLogTable_ROW_CREATION

/* comment out the following line if you don't want the secondary index */
#define saHpiOemEventLogTable_IDX2

/* uncommend the following line if you allow modifications to an
 * active row */
/** define saHpiOemEventLogTable_CAN_MODIFY_ACTIVE_ROW */

#ifdef saHpiOemEventLogTable_SET_HANDLING

int saHpiOemEventLogTable_extract_index( saHpiOemEventLogTable_context * ctx, netsnmp_index * hdr );

void saHpiOemEventLogTable_set_reserve1( netsnmp_request_group * );
void saHpiOemEventLogTable_set_reserve2( netsnmp_request_group * );
void saHpiOemEventLogTable_set_action( netsnmp_request_group * );
void saHpiOemEventLogTable_set_commit( netsnmp_request_group * );
void saHpiOemEventLogTable_set_free( netsnmp_request_group * );
void saHpiOemEventLogTable_set_undo( netsnmp_request_group * );

saHpiOemEventLogTable_context * saHpiOemEventLogTable_duplicate_row( saHpiOemEventLogTable_context* );
netsnmp_index * saHpiOemEventLogTable_delete_row( saHpiOemEventLogTable_context* );

int saHpiOemEventLogTable_can_activate(saHpiOemEventLogTable_context *undo_ctx,
                      saHpiOemEventLogTable_context *row_ctx,
                      netsnmp_request_group * rg);
int saHpiOemEventLogTable_can_deactivate(saHpiOemEventLogTable_context *undo_ctx,
                        saHpiOemEventLogTable_context *row_ctx,
                        netsnmp_request_group * rg);
int saHpiOemEventLogTable_can_delete(saHpiOemEventLogTable_context *undo_ctx,
                    saHpiOemEventLogTable_context *row_ctx,
                    netsnmp_request_group * rg);
    
    
#ifdef saHpiOemEventLogTable_ROW_CREATION
saHpiOemEventLogTable_context * saHpiOemEventLogTable_create_row( netsnmp_index* );
#endif
#endif

#ifdef saHpiOemEventLogTable_IDX2
saHpiOemEventLogTable_context * saHpiOemEventLogTable_get( const char *name, int len );
#endif

#ifdef __cplusplus
};
#endif

#endif /** SAHPIOemEVENTLOGTABLE_H */
