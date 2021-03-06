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
#ifndef SAHPISENSORTHDPOSHYSTERESISTABLE_H
#define SAHPISENSORTHDPOSHYSTERESISTABLE_H

#ifdef __cplusplus
extern "C" {
#endif


#include <net-snmp/net-snmp-config.h>
#include <net-snmp/library/container.h>
#include <net-snmp/agent/table_array.h>

/** Index saHpiDomainId is external */
/** Index saHpiResourceId is external */
/** Index saHpiResourceIsHistorical is external */
/** Index saHpiSensorNum is external */

typedef struct saHpiSensorThdPosHysteresisTable_context_s {
        netsnmp_index index; /** THIS MUST BE FIRST!!! */

        /*************************************************************
         * You can store data internally in this structure.
         *
         * TODO: You will probably have to fix a few types here...
         */
        /** TODO: add storage for external index(s)! */
        /** TruthValue = ASN_INTEGER */
        long saHpiSensorThdPosHysteresisIsReadable;

        /** TruthValue = ASN_INTEGER */
        long saHpiSensorThdPosHysteresisIsWritable;

        /** SaHpiSensorReadingType = ASN_INTEGER */
        long saHpiSensorThdPosHysteresisType;

        /** SaHpiSensorReadingValue = ASN_OCTET_STR */
        unsigned char saHpiSensorThdPosHysteresisValue[SAHPI_SENSOR_BUFFER_LENGTH];
        long saHpiSensorThdPosHysteresisValue_len;

        /** TruthValue = ASN_INTEGER */
        long saHpiSensorThdPosHysteresisNonLinear;


        /*
         * OR
         *
         * Keep a pointer to your data
         */
        void * data;

        /*
         *add anything else you want here
         */

} saHpiSensorThdPosHysteresisTable_context;

/*************************************************************
 * function declarations
 */
SaErrorT populate_sen_thd_pos_hys(SaHpiSessionIdT sessionid, 
                                          SaHpiRdrT *rdr_entry,
                                          SaHpiRptEntryT *rpt_entry,
                                          SaHpiSensorThresholdsT *sensor_thresholds);
SaErrorT clear_sen_thd_pos_hys(SaHpiDomainIdT domainId, 
                               SaHpiResourceIdT resourceId);
int set_table_sen_thds_pos_hys (saHpiSensorThdPosHysteresisTable_context *row_ctx);

/*************************************************************
 * function declarations
 */
void init_saHpiSensorThdPosHysteresisTable(void);
void initialize_table_saHpiSensorThdPosHysteresisTable(void);
const saHpiSensorThdPosHysteresisTable_context * saHpiSensorThdPosHysteresisTable_get_by_idx(netsnmp_index *);
const saHpiSensorThdPosHysteresisTable_context * saHpiSensorThdPosHysteresisTable_get_by_idx_rs(netsnmp_index *,
                                                                                                int row_status);
int saHpiSensorThdPosHysteresisTable_get_value(netsnmp_request_info *, netsnmp_index *, netsnmp_table_request_info *);


/*************************************************************
 * oid declarations
 */
extern oid saHpiSensorThdPosHysteresisTable_oid[];
extern size_t saHpiSensorThdPosHysteresisTable_oid_len;

#define saHpiSensorThdPosHysteresisTable_TABLE_OID 1,3,6,1,4,1,18568,2,1,1,4,9,15

/* Number of table Indexes */
#define SEN_THD_POS_HYS_IDX_NR 4
#define saHpiThdPosHysDomainId_INDEX 0
#define saHpiThdPosHysResourceEntryId_INDEX 1
#define saHpiThdPosHysResourceIsHistorical_INDEX 2
#define saHpiSensorThdPosHysNum_INDEX 3

/*************************************************************
 * column number definitions for table saHpiSensorThdPosHysteresisTable
 */
#define COLUMN_SAHPISENSORTHDPOSHYSTERESISISREADABLE 1
#define COLUMN_SAHPISENSORTHDPOSHYSTERESISISWRITABLE 2
#define COLUMN_SAHPISENSORTHDPOSHYSTERESISTYPE 3
#define COLUMN_SAHPISENSORTHDPOSHYSTERESISVALUE 4
#define COLUMN_SAHPISENSORTHDPOSHYSTERESISNONLINEAR 5
#define saHpiSensorThdPosHysteresisTable_COL_MIN 1
#define saHpiSensorThdPosHysteresisTable_COL_MAX 5

int saHpiSensorThdPosHysteresisTable_extract_index( saHpiSensorThdPosHysteresisTable_context * ctx, netsnmp_index * hdr );

void saHpiSensorThdPosHysteresisTable_set_reserve1( netsnmp_request_group * );
void saHpiSensorThdPosHysteresisTable_set_reserve2( netsnmp_request_group * );
void saHpiSensorThdPosHysteresisTable_set_action( netsnmp_request_group * );
void saHpiSensorThdPosHysteresisTable_set_commit( netsnmp_request_group * );
void saHpiSensorThdPosHysteresisTable_set_free( netsnmp_request_group * );
void saHpiSensorThdPosHysteresisTable_set_undo( netsnmp_request_group * );

saHpiSensorThdPosHysteresisTable_context * saHpiSensorThdPosHysteresisTable_duplicate_row( saHpiSensorThdPosHysteresisTable_context* );
netsnmp_index * saHpiSensorThdPosHysteresisTable_delete_row( saHpiSensorThdPosHysteresisTable_context* );

int saHpiSensorThdPosHysteresisTable_can_activate(saHpiSensorThdPosHysteresisTable_context *undo_ctx,
                                                  saHpiSensorThdPosHysteresisTable_context *row_ctx,
                                                  netsnmp_request_group * rg);
int saHpiSensorThdPosHysteresisTable_can_deactivate(saHpiSensorThdPosHysteresisTable_context *undo_ctx,
                                                    saHpiSensorThdPosHysteresisTable_context *row_ctx,
                                                    netsnmp_request_group * rg);
int saHpiSensorThdPosHysteresisTable_can_delete(saHpiSensorThdPosHysteresisTable_context *undo_ctx,
                                                saHpiSensorThdPosHysteresisTable_context *row_ctx,
                                                netsnmp_request_group * rg);


saHpiSensorThdPosHysteresisTable_context * saHpiSensorThdPosHysteresisTable_create_row( netsnmp_index* );

saHpiSensorThdPosHysteresisTable_context * saHpiSensorThdPosHysteresisTable_get( const char *name, int len );

#ifdef __cplusplus
};
#endif

#endif /** SAHPISENSORTHDPOSHYSTERESISTABLE_H */
