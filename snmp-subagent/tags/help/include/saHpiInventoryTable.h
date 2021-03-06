/*
 * Note: this file originally auto-generated by mib2c using
 *        : mib2c.array-user.conf,v 5.18.2.2 2004/02/09 18:21:47 rstory Exp $
 *
 * $Id$
 *
 * Yes, there is lots of code here that you might not use. But it is much
 * easier to remove code than to add it!
 */
#ifndef SAHPIINVENTORYTABLE_H
#define SAHPIINVENTORYTABLE_H

#ifdef __cplusplus
extern "C" {
#endif

    
#include <net-snmp/net-snmp-config.h>
#include <net-snmp/library/container.h>
#include <net-snmp/agent/table_array.h>

        /** Index saHpiDomainId is external */
        /** Index saHpiResourceId is external */
        /** Index saHpiResourceIsHistorical is external */
        /** Index saHpiInventoryId is internal */

typedef struct saHpiInventoryTable_context_s {
    netsnmp_index index; /** THIS MUST BE FIRST!!! */

    /*************************************************************
     * You can store data internally in this structure.
     *
     * TODO: You will probably have to fix a few types here...
     */
    /** TODO: add storage for external index(s)! */
        /** SaHpiInstrumentId = ASN_UNSIGNED */
            unsigned long saHpiInventoryId;

        /** TruthValue = ASN_INTEGER */
            long saHpiInventoryPersistent;

        /** UNSIGNED32 = ASN_UNSIGNED */
            unsigned long saHpiInventoryOEM;

        /** UNSIGNED32 = ASN_UNSIGNED */
            unsigned long saHpiInventoryUpdateCount;

        /** TruthValue = ASN_INTEGER */
            long saHpiInventoryIsReadOnly;

        /** UNSIGNED32 = ASN_UNSIGNED */
            unsigned long saHpiInventoryNumAreas;

        /** RowPointer = ASN_OBJECT_ID */
            oid saHpiInventoryRDR[MAX_OID_LEN];
            long saHpiInventoryRDR_len;


    /*
     * OR
     *
     * Keep a pointer to your data
     */
    void * data;

    /*
     *add anything else you want here
     */

} saHpiInventoryTable_context;

/*************************************************************
 * function declarations
 */
SaErrorT populate_inventory (SaHpiSessionIdT sessionid, 
                             SaHpiRdrT *rdr_entry,
                             SaHpiRptEntryT *rpt_entry,
                             oid *full_oid, size_t full_oid_len,
                             oid *child_oid, size_t *child_oid_len);

/*************************************************************
 * function declarations
 */
void init_saHpiInventoryTable(void);
void initialize_table_saHpiInventoryTable(void);
const saHpiInventoryTable_context * saHpiInventoryTable_get_by_idx(netsnmp_index *);
const saHpiInventoryTable_context * saHpiInventoryTable_get_by_idx_rs(netsnmp_index *,
                                        int row_status);
int saHpiInventoryTable_get_value(netsnmp_request_info *, netsnmp_index *, netsnmp_table_request_info *);


/*************************************************************
 * oid declarations
 */
extern oid saHpiInventoryTable_oid[];
extern size_t saHpiInventoryTable_oid_len;

#define saHpiInventoryTable_TABLE_OID 1,3,6,1,4,1,18568,2,1,1,4,8,2

/* Number of table Indexes */
#define INVENTORY_INDEX_NR 4 
#define saHpiDomainId_INDEX 0
#define saHpiResourceEntryId_INDEX 1
#define saHpiResourceIsHistorical_INDEX 2
#define saHpiInventoryId_INDEX 3
    
/*************************************************************
 * column number definitions for table saHpiInventoryTable
 */
#define COLUMN_SAHPIINVENTORYID 1
#define COLUMN_SAHPIINVENTORYPERSISTENT 2
#define COLUMN_SAHPIINVENTORYOEM 3
#define COLUMN_SAHPIINVENTORYUPDATECOUNT 4
#define COLUMN_SAHPIINVENTORYISREADONLY 5
#define COLUMN_SAHPIINVENTORYNUMAREAS 6
#define COLUMN_SAHPIINVENTORYRDR 7
#define saHpiInventoryTable_COL_MIN 2
#define saHpiInventoryTable_COL_MAX 7

int saHpiInventoryTable_extract_index( saHpiInventoryTable_context * ctx, netsnmp_index * hdr );

void saHpiInventoryTable_set_reserve1( netsnmp_request_group * );
void saHpiInventoryTable_set_reserve2( netsnmp_request_group * );
void saHpiInventoryTable_set_action( netsnmp_request_group * );
void saHpiInventoryTable_set_commit( netsnmp_request_group * );
void saHpiInventoryTable_set_free( netsnmp_request_group * );
void saHpiInventoryTable_set_undo( netsnmp_request_group * );

saHpiInventoryTable_context * saHpiInventoryTable_duplicate_row( saHpiInventoryTable_context* );
netsnmp_index * saHpiInventoryTable_delete_row( saHpiInventoryTable_context* );

int saHpiInventoryTable_can_activate(saHpiInventoryTable_context *undo_ctx,
                      saHpiInventoryTable_context *row_ctx,
                      netsnmp_request_group * rg);
int saHpiInventoryTable_can_deactivate(saHpiInventoryTable_context *undo_ctx,
                        saHpiInventoryTable_context *row_ctx,
                        netsnmp_request_group * rg);
int saHpiInventoryTable_can_delete(saHpiInventoryTable_context *undo_ctx,
                    saHpiInventoryTable_context *row_ctx,
                    netsnmp_request_group * rg);
    
    
saHpiInventoryTable_context * saHpiInventoryTable_create_row( netsnmp_index* );

saHpiInventoryTable_context * saHpiInventoryTable_get( const char *name, int len );

#ifdef __cplusplus
};
#endif

#endif /** SAHPIINVENTORYTABLE_H */
