/*
 * (C) Copyright IBM Corp. 2003
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  This
 * file and program are licensed under a BSD style license.  See
 * the Copying file included with the OpenHPI distribution for
 * full licensing terms.
 *
 * Authors:
 *   Konrad Rzeszutek <konradr@us.ibm.com>
 *
 * Note: this file originally auto-generated by mib2c using
 *        : mib2c.arrkay-user.conf,v 5.15.2.1 2003/02/27 05:59:41 rstory Exp $
 *
 * $Id$
 *
 */
#ifndef SAHPIINVENTORYTABLE_H
#define SAHPIINVENTORYTABLE_H

#ifdef __cplusplus
extern          "C" {
#endif

#include <net-snmp/net-snmp-config.h>
#include <net-snmp/library/container.h>
#include <net-snmp/agent/table_array.h>
#include <SaHpi.h>

  /*
   * Max values are defined in the MIB
   */

#define SAHPI_INVENTORY_ATTRIBUTES_MAX SNMP_MAX_MSG_SIZE
#define SAHPI_STRING_MAX 255
#define MIB_VALID 1
#define MIB_INVALID 0
#define MIB_OVERFLOW 2
#define MAXBUF (1024*16)
#define SAHPI_INVENT_RECTYPE_INTERNAL_USE_MAX 1
#define SAHPI_INVENT_RECTYPE_CHASSIS_INFO_MAX 5
#define SAHPI_INVENT_RECTYPE_BOARD_INFO_MAX 4
#define SAHPI_INVENT_RECTYPE_PRODUCT_INFO_MAX 4
#define SAHPI_INVENT_RECTYPE_OEM_MAX 4

    typedef struct saHpiInventoryTable_context_s {
        netsnmp_index   index;
                   
        /** UNSIGNED32 = ASN_UNSIGNED */
        unsigned long   saHpiInventoryEirId;
      /** UNSIGNED32 */
      unsigned long saHpiInventoryIndex;
        /** INTEGER = ASN_INTEGER */
        long            saHpiInventoryRecordType;

        /** INTEGER = ASN_INTEGER */
        long            saHpiInventoryValidity;

        /** OCTETSTR = ASN_OCTET_STR */
        unsigned char   saHpiInventoryAttributes[SAHPI_INVENTORY_ATTRIBUTES_MAX];
        long            saHpiInventoryAttributes_len;

        /** INTEGER = ASN_INTEGER */
        long            saHpiInventoryTextType;

        /** INTEGER = ASN_INTEGER */
        long            saHpiInventoryTextLanguage;

        /** OCTETSTR = ASN_OCTET_STR */
        unsigned char   saHpiInventoryManufacturer[SAHPI_STRING_MAX];
        long            saHpiInventoryManufacturer_len;

        /** OCTETSTR = ASN_OCTET_STR */
        unsigned char   saHpiInventoryProductName[SAHPI_STRING_MAX];
        long            saHpiInventoryProductName_len;

        /** OCTETSTR = ASN_OCTET_STR */
        unsigned char   saHpiInventoryProductVersion[SAHPI_STRING_MAX];
        long            saHpiInventoryProductVersion_len;

        /** OCTETSTR = ASN_OCTET_STR */
        unsigned char   saHpiInventoryModelNumber[SAHPI_STRING_MAX];
        long            saHpiInventoryModelNumber_len;

        /** OCTETSTR = ASN_OCTET_STR */
        unsigned char   saHpiInventorySerialNumber[SAHPI_STRING_MAX];
        long            saHpiInventorySerialNumber_len;

        /** OCTETSTR = ASN_OCTET_STR */
        unsigned char   saHpiInventoryPartNumber[SAHPI_STRING_MAX];
        long            saHpiInventoryPartNumber_len;

        /** OCTETSTR = ASN_OCTET_STR */
        unsigned char   saHpiInventoryFileId[SAHPI_STRING_MAX];
        long            saHpiInventoryFileId_len;

        /** OCTETSTR = ASN_OCTET_STR */
        unsigned char   saHpiInventoryAssetTag[SAHPI_STRING_MAX];
        long            saHpiInventoryAssetTag_len;

        /** OCTETSTR = ASN_OCTET_STR */
        unsigned char   saHpiInventoryCustomField[SAHPI_STRING_MAX];
        long            saHpiInventoryCustomField_len;

        /** RowPointer = ASN_OBJECT_ID */
        oid             saHpiInventoryRDR[MAX_OID_LEN];
        long            saHpiInventoryRDR_len;
      long domain_id;
      long resource_id;
      long hash;

      long count_of_subitems;
    } saHpiInventoryTable_context;

/*************************************************************
 * function declarations
 */

    void            initialize_table_saHpiInventoryTable(void);
    const saHpiInventoryTable_context
        *saHpiInventoryTable_get_by_idx(netsnmp_index *);
    const saHpiInventoryTable_context
        *saHpiInventoryTable_get_by_idx_rs(netsnmp_index *,
                                           int row_status);
    int             saHpiInventoryTable_get_value(netsnmp_request_info *,
                                                  netsnmp_index *,
                                                  netsnmp_table_request_info
                                                  *);

int  populate_inventory(
		      SaHpiInventoryRecT *control,
		      SaHpiRptEntryT *rpt_entry,
		       oid *rdr_oid, size_t rdr_oid_len,
		       oid *control_oid, 
		       size_t *control_oid_len);



void
update_context_on_inventory_data(SaHpiInventGeneralDataT *data,
                                saHpiInventoryTable_context *ctx);

int
 update_inventory_data_on_context(SaHpiInventGeneralDataT *gen_data,
				  saHpiInventoryTable_context *ctx,
				  //size_t sahpi_length,
				  char *out,
				  size_t max_octets,
				  size_t *length);


int
delete_inventory_rows(SaHpiDomainIdT domain_id,
		     SaHpiResourceIdT resource_id,
		     SaHpiEirIdT num);
int set_inventory(saHpiInventoryTable_context *ctx);


/*************************************************************
 * oid declarations
 */
    extern oid      saHpiInventoryTable_oid[];
    extern size_t   saHpiInventoryTable_oid_len;
// 1,3,6,1,3,90,3,8
#define saHpiInventoryTable_TABLE_OID hpiResources_OID,8

/*************************************************************
 * column number definitions for table saHpiInventoryTable
 */

#define COLUMN_SAHPIINVENTORYEIRID 1
#define COLUMN_SAHPIINVENTORYINDEX 2
#define COLUMN_SAHPIINVENTORYRECORDTYPE 3
#define COLUMN_SAHPIINVENTORYVALIDITY 4
#define COLUMN_SAHPIINVENTORYATTRIBUTES 5
#define COLUMN_SAHPIINVENTORYTEXTTYPE 6
#define COLUMN_SAHPIINVENTORYTEXTLANGUAGE 7
#define COLUMN_SAHPIINVENTORYMANUFACTURER 8
#define COLUMN_SAHPIINVENTORYPRODUCTNAME 9
#define COLUMN_SAHPIINVENTORYPRODUCTVERSION 10
#define COLUMN_SAHPIINVENTORYMODELNUMBER 11
#define COLUMN_SAHPIINVENTORYSERIALNUMBER 12
#define COLUMN_SAHPIINVENTORYPARTNUMBER 13
#define COLUMN_SAHPIINVENTORYFILEID 14
#define COLUMN_SAHPIINVENTORYASSETTAG 15
#define COLUMN_SAHPIINVENTORYCUSTOMFIELD 16
#define COLUMN_SAHPIINVENTORYRDR 17
#define saHpiInventoryTable_COL_MIN 1
#define saHpiInventoryTable_COL_MAX 17

 

    int            
        saHpiInventoryTable_extract_index(saHpiInventoryTable_context *
                                          ctx, netsnmp_index * hdr);
  
    void            saHpiInventoryTable_set_reserve1(netsnmp_request_group
                                                     *);
    void            saHpiInventoryTable_set_reserve2(netsnmp_request_group
                                                     *);
    void            saHpiInventoryTable_set_action(netsnmp_request_group
                                                   *);
    void            saHpiInventoryTable_set_commit(netsnmp_request_group
                                                   *);
    void            saHpiInventoryTable_set_free(netsnmp_request_group *);
    void            saHpiInventoryTable_set_undo(netsnmp_request_group *);

    saHpiInventoryTable_context
        *saHpiInventoryTable_duplicate_row(saHpiInventoryTable_context *);
	
    netsnmp_index 
        *saHpiInventoryTable_delete_row(saHpiInventoryTable_context *);
  
    int            
        saHpiInventoryTable_can_delete(saHpiInventoryTable_context *
                                       undo_ctx,
                                       saHpiInventoryTable_context *
                                       row_ctx,
                                       netsnmp_request_group * rg);
  

    saHpiInventoryTable_context
        *saHpiInventoryTable_create_row(netsnmp_index *);


#ifdef __cplusplus
};
#endif

#endif /** SAHPIINVENTORYTABLE_H */
