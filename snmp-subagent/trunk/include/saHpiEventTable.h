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
 *        : mib2c.array-user.conf,v 5.15.2.1 2003/02/27 05:59:41 rstory Exp $
 *
 * $Id$
 *
 */
#ifndef SAHPIEVENTTABLE_H
#define SAHPIEVENTTABLE_H

#ifdef __cplusplus
extern "C"
{
#endif


#include <net-snmp/net-snmp-config.h>
#include <net-snmp/library/container.h>
#include <net-snmp/agent/table_array.h>
#include <SaHpi.h>
#include <hpiSubagent.h>

/*
   * Number of index values in this table.
   * Consult the HPI-MIB
   *
   * If this number changes, look in the src code for this 
   * define, and make sure to add/remove the new index value(s).
   */
#define EVENT_INDEX_NR 3

#define EVENT_TRIGGER_READING_INTERPRETED_MAX 32
#define EVENT_TRIGGER_READING_EVENT_STATE_MAX 3
#define EVENT_TRIGGER_THRESHOLD_INTERPRETED_MAX 32
#define EVENT_TRIGGER_THRESHOLD_EVENT_STATE_MAX 3
#define EVENT_SENSOR_STATE_MAX 255

	/** Index saHpiDomainID is external */
	/** Index saHpiResourceID is external */
	/** Index saHpiEntryID is external */

  typedef struct saHpiEventTable_context_s
  {
    netsnmp_index index;

	/** UNSIGNED32 = ASN_UNSIGNED */
    unsigned long saHpiEventIndex;

	/** INTEGER = ASN_INTEGER */
    long saHpiEventType;

	/** HpiTimeStamp = ASN_COUNTER64 */
    integer64 saHpiEventTimestamp;

	/** INTEGER = ASN_INTEGER */
    long saHpiEventSeverity;


    // SENSOR TYPE information only: BEGIN
	/** UNSIGNED32 = ASN_UNSIGNED */
    unsigned long saHpiEventSensorNum;

	/** INTEGER = ASN_INTEGER */
    long saHpiEventSensorType;

	/** INTEGER = ASN_INTEGER */
    long saHpiEventSensorCategory;

	/** TruthValue = ASN_INTEGER */
    long saHpiEventSensorAssertion;


        /** OCTETSTR = ASN_OCTET_STR */
    unsigned char   saHpiEventSensorState[EVENT_SENSOR_STATE_MAX];
    size_t            saHpiEventSensorState_len;

	/** UNSIGNED32 = ASN_UNSIGNED */
    unsigned long saHpiEventSensorOptionalData;

	/** UNSIGNED32 = ASN_UNSIGNED */
    unsigned long saHpiEventSensorTriggerReadingType;

	/** UNSIGNED32 = ASN_UNSIGNED */
    unsigned long saHpiEventSensorTriggerReadingRaw;

	/** INTEGER = ASN_INTEGER */
    long saHpiEventSensorTriggerReadingInterpretedType;


	/** OCTETSTR = ASN_OCTET_STR */
    unsigned char
      saHpiEventSensorTriggerReadingInterpreted
      [EVENT_TRIGGER_READING_INTERPRETED_MAX];
    long saHpiEventSensorTriggerReadingInterpreted_len;

    /** INTEGER = ASN_INTEGER */
    long            saHpiEventSensorTriggerReadingEventStateFlag;

	/** OCTETSTR = ASN_OCTET_STR */
    unsigned char
      saHpiEventSensorTriggerReadingEventState
      [EVENT_SENSOR_STATE_MAX];
    size_t saHpiEventSensorTriggerReadingEventState_len;

	/** UNSIGNED32 = ASN_UNSIGNED */
    unsigned long saHpiEventSensorTriggerThresholdType;

	/** UNSIGNED32 = ASN_UNSIGNED */
    unsigned long saHpiEventSensorTriggerThresholdRaw;

	/** INTEGER = ASN_INTEGER */
    long saHpiEventSensorTriggerThresholdInterpretedType;

	/** OCTETSTR = ASN_OCTET_STR */
    unsigned char
      saHpiEventSensorTriggerThresholdInterpreted
      [EVENT_TRIGGER_THRESHOLD_INTERPRETED_MAX];
    long saHpiEventSensorTriggerThresholdInterpreted_len;

   /** INTEGER = ASN_INTEGER */
        long            saHpiEventSensorTriggerThresholdEventStateFlag;

	/** OCTETSTR = ASN_OCTET_STR */
    unsigned char
      saHpiEventSensorTriggerThresholdEventState
      [EVENT_SENSOR_STATE_MAX];
    size_t saHpiEventSensorTriggerThresholdEventState_len;

	/** UNSIGNED32 = ASN_OCTET_STR */
    unsigned char saHpiEventSensorPreviousState[EVENT_SENSOR_STATE_MAX];
    size_t saHpiEventSensorPreviousState_len;

	/** UNSIGNED32 = ASN_UNSIGNED */
    unsigned long saHpiEventSensorOem;

	/** UNSIGNED32 = ASN_UNSIGNED */
    unsigned long saHpiEventSensorSpecific;

    // SENSOR END 
	/** INTEGER = ASN_INTEGER */
    long saHpiEventHotSwapState;

	/** INTEGER = ASN_INTEGER */
    long saHpiEventPreviousHotSwapState;

	/** UNSIGNED32 = ASN_UNSIGNED */
    unsigned long saHpiEventWatchdogNum;

	/** INTEGER = ASN_INTEGER */
    long saHpiEventWatchdogAction;

	/** INTEGER = ASN_INTEGER */
    long saHpiEventWatchdogPreTimerAction;

	/** INTEGER = ASN_INTEGER */
    long saHpiEventWatchdogUse;

	/** UNSIGNED32 = ASN_UNSIGNED */
    unsigned long saHpiEventOemManufacturerIdT;

	/** OCTETSTR = ASN_OCTET_STR */
    unsigned char saHpiEventOemEventData[SAHPI_OEM_EVENT_DATA_SIZE];
    long saHpiEventOemEventData_len;

	/** OCTETSTR = ASN_OCTET_STR */
    unsigned char saHpiEventUserEventData[SAHPI_USER_EVENT_DATA_SIZE];
    long saHpiEventUserEventData_len;


	/** TruthValue = ASN_INTEGER */
    long saHpiEventDelete;

    long hash;
    long resource_id;
    long domain_id;
  } saHpiEventTable_context;

/*************************************************************
 * function declarations
 */

  void initialize_table_saHpiEventTable (void);

  int saHpiEventTable_get_value (netsnmp_request_info *,
				 netsnmp_index *,
				 netsnmp_table_request_info *);

  /*
     int
     populate_event(SaHpiSelEntryIdT,
     SaHpiEventT *,
     SaHpiRptEntryT *t,
     SaHpiRdrT *,
     oid *,  size_t *,
     oid *, const size_t,
     oid *, const size_t);

   */
  int populate_event (void);

  unsigned long purge_event (void);

  //int delete_event_entry(saHpiEventTable_context *ctx);



  int
    delete_event_row (SaHpiDomainIdT domain_id,
		      SaHpiResourceIdT resource_id, unsigned long num);


  int
    event_count_entries_handler (netsnmp_mib_handler * handler,
				 netsnmp_handler_registration * reginfo,
				 netsnmp_agent_request_info * reqinfo,
				 netsnmp_request_info * requests);
/*************************************************************
 * oid declarations
 */
  extern oid saHpiEventTable_oid[];
  extern size_t saHpiEventTable_oid_len;

#define saHpiEventTable_TABLE_OID events_OID,2


/*************************************************************
 * column number definitions for table saHpiEventTable
 */
#define COLUMN_SAHPIEVENTINDEX 1
#define COLUMN_SAHPIEVENTTYPE 2
#define COLUMN_SAHPIEVENTTIMESTAMP 3
#define COLUMN_SAHPIEVENTSEVERITY 4
#define COLUMN_SAHPIEVENTSENSORNUM 5
#define COLUMN_SAHPIEVENTSENSORTYPE 6
#define COLUMN_SAHPIEVENTSENSORCATEGORY 7
#define COLUMN_SAHPIEVENTSENSORASSERTION 8
#define COLUMN_SAHPIEVENTSENSORSTATE 9
#define COLUMN_SAHPIEVENTSENSOROPTIONALDATA 10
#define COLUMN_SAHPIEVENTSENSORTRIGGERREADINGTYPE 11
#define COLUMN_SAHPIEVENTSENSORTRIGGERREADINGRAW 12
#define COLUMN_SAHPIEVENTSENSORTRIGGERREADINGINTERPRETEDTYPE 13
#define COLUMN_SAHPIEVENTSENSORTRIGGERREADINGINTERPRETED 14
#define COLUMN_SAHPIEVENTSENSORTRIGGERREADINGEVENTSTATEFLAG 15
#define COLUMN_SAHPIEVENTSENSORTRIGGERREADINGEVENTSTATE 16
#define COLUMN_SAHPIEVENTSENSORTRIGGERTHRESHOLDTYPE 17
#define COLUMN_SAHPIEVENTSENSORTRIGGERTHRESHOLDRAW 18
#define COLUMN_SAHPIEVENTSENSORTRIGGERTHRESHOLDINTERPRETEDTYPE 19
#define COLUMN_SAHPIEVENTSENSORTRIGGERTHRESHOLDINTERPRETED 20
#define COLUMN_SAHPIEVENTSENSORTRIGGERTHRESHOLDEVENTSTATEFLAG 21
#define COLUMN_SAHPIEVENTSENSORTRIGGERTHRESHOLDEVENTSTATE 22
#define COLUMN_SAHPIEVENTSENSORPREVIOUSSTATE 23
#define COLUMN_SAHPIEVENTSENSOROEM 24
#define COLUMN_SAHPIEVENTSENSORSPECIFIC 25
#define COLUMN_SAHPIEVENTHOTSWAPSTATE 26
#define COLUMN_SAHPIEVENTPREVIOUSHOTSWAPSTATE 27
#define COLUMN_SAHPIEVENTWATCHDOGNUM 28
#define COLUMN_SAHPIEVENTWATCHDOGACTION 29
#define COLUMN_SAHPIEVENTWATCHDOGPRETIMERACTION 30
#define COLUMN_SAHPIEVENTWATCHDOGUSE 31
#define COLUMN_SAHPIEVENTOEMMANUFACTURERIDT 32
#define COLUMN_SAHPIEVENTOEMEVENTDATA 33
#define COLUMN_SAHPIEVENTUSEREVENTDATA 34
#define COLUMN_SAHPIEVENTDELETE 35
#define saHpiEventTable_COL_MIN 1
#define saHpiEventTable_COL_MAX 35



  int saHpiEventTable_extract_index (saHpiEventTable_context *
				     ctx, netsnmp_index * hdr);

  void saHpiEventTable_set_reserve1 (netsnmp_request_group *);
  void saHpiEventTable_set_reserve2 (netsnmp_request_group *);
  void saHpiEventTable_set_action (netsnmp_request_group *);
  void saHpiEventTable_set_commit (netsnmp_request_group *);
  void saHpiEventTable_set_free (netsnmp_request_group *);
  void saHpiEventTable_set_undo (netsnmp_request_group *);

    saHpiEventTable_context
    * saHpiEventTable_duplicate_row (saHpiEventTable_context *);


  netsnmp_index *saHpiEventTable_delete_row (saHpiEventTable_context *);


  int saHpiEventTable_can_delete (saHpiEventTable_context *
				  undo_ctx,
				  saHpiEventTable_context *
				  row_ctx, netsnmp_request_group * rg);



  saHpiEventTable_context *saHpiEventTable_create_row (netsnmp_index *);

  /*
     saHpiEventTable_context *saHpiEventTable_get(const char *name,
     int len);
   */

#ifdef __cplusplus
};
#endif

#endif /** SAHPIEVENTTABLE_H */
