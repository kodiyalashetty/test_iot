/*
 * (C) Copyright IBM Corp. 2004
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
 * Note: this file originally auto-generated by mib2c using
 *       : mib2c.array-user.conf,v 5.18 2003/11/07 17:03:52 rstory Exp $
 *
 * $Id$
 *
 *
 */
#include <SaHpi.h>
#include <net-snmp/net-snmp-config.h>
#include <net-snmp/net-snmp-includes.h>
#include <net-snmp/agent/net-snmp-agent-includes.h>

#include <net-snmp/library/snmp_assert.h>

#include <saHpiSensorThdPosHysteresisTable.h>


#include <hpiSubagent.h>


static netsnmp_handler_registration *my_handler = NULL;
static netsnmp_table_array_callbacks cb;

oid saHpiSensorThdPosHysteresisTable_oid[] =
  { saHpiSensorThdPosHysteresisTable_TABLE_OID };
size_t saHpiSensorThdPosHysteresisTable_oid_len =
OID_LENGTH (saHpiSensorThdPosHysteresisTable_oid);

static int
modify_saHpiSensorThdPosHysteresisTable_row (SaHpiDomainIdT domain_id,
					     SaHpiResourceIdT resource_id,
					     SaHpiSensorNumT sensor_num,
					     SaHpiSensorThdDefnT *
					     threshold_def,
					     SaHpiSensorReadingT * reading,
					     saHpiSensorThdPosHysteresisTable_context
					     * ctx);

int
delete_ThdPosHysteresis_row (SaHpiDomainIdT domain_id,
			     SaHpiResourceIdT resource_id,
			     SaHpiSensorNumT sensor_num)
{

  saHpiSensorThdPosHysteresisTable_context *ctx;
  oid index_oid[SENSOR_THD_INDEX_NR];
  netsnmp_index sensor_reading_index;
  int rc = AGENT_ERR_NOT_FOUND;

  DEBUGMSGTL ((AGENT, "delete_ThdPosHysteresis_row (%d, %d, %d). Entry.\n",
	       domain_id, resource_id, sensor_num));

  // Look at the MIB to find out what the indexs are
  index_oid[0] = domain_id;
  index_oid[1] = resource_id;
  index_oid[2] = sensor_num;
  // Possible more indexs?
  sensor_reading_index.oids = (oid *) & index_oid;
  sensor_reading_index.len = SENSOR_THD_INDEX_NR;

  ctx = CONTAINER_FIND (cb.container, &sensor_reading_index);

  if (ctx)
    {
      CONTAINER_REMOVE (cb.container, ctx);
      saHpiSensorThdPosHysteresisTable_delete_row (ctx);
      rc = AGENT_ERR_NOERROR;
    }
  DEBUGMSGTL ((AGENT, "delete_ThdPosHysteresis_row. Exit (rc: %d).\n", rc));
  return rc;
}


int
populate_ThdPosHysteresis (SaHpiDomainIdT domain_id,
			   SaHpiResourceIdT resource_id,
			   SaHpiSensorNumT sensor_id,
			   SaHpiSensorThdDefnT * threshold_def,
			   SaHpiSensorReadingT * reading)
{


  int rc = AGENT_ERR_NOERROR;

  oid index_oid[SENSOR_THD_INDEX_NR];
  netsnmp_index sensor_thd_index;
  saHpiSensorThdPosHysteresisTable_context *ctx;


  DEBUGMSGT ((AGENT, "\t--- populate_ThdPosHysteresis, Entry,\n"));

  if (reading && threshold_def)
    {

      /*
         Construct index 
       */
      sensor_thd_index.len = SENSOR_THD_INDEX_NR;
      index_oid[0] = domain_id;
      index_oid[1] = resource_id;
      index_oid[2] = sensor_id;
      sensor_thd_index.oids = (oid *) & index_oid;

      /*
       * Find the row.
       */
      ctx = NULL;
      ctx = CONTAINER_FIND (cb.container, &sensor_thd_index);

      if (!ctx)
	{
	  /* 
	     New entry. Create it.
	   */
	  ctx =
	    saHpiSensorThdPosHysteresisTable_create_row (&sensor_thd_index);
	}
      if (!ctx)
	{
	  snmp_log (LOG_ERR,
		    "Not enough memory for a sensor ThdPosHysteresis row!");
	  return AGENT_ERR_INTERNAL_ERROR;
	}

      if (modify_saHpiSensorThdPosHysteresisTable_row (domain_id,
						       resource_id,
						       sensor_id,
						       threshold_def,
						       reading,
						       ctx) ==
	  AGENT_NEW_ENTRY)
	{
	  /*
	   * Add new entry.
	   */
	  CONTAINER_INSERT (cb.container, ctx);
	}
      rc = AGENT_ERR_NOERROR;

    }
  else
    rc = AGENT_ERR_OPERATION;
  DEBUGMSGT ((AGENT, "\t--- populate_ThdPosHysteresis, Exit (rc: %d),\n",
	      rc));

  return rc;
}


int
modify_saHpiSensorThdPosHysteresisTable_row (SaHpiDomainIdT domain_id,
					     SaHpiResourceIdT resource_id,
					     SaHpiSensorNumT sensor_num,
					     SaHpiSensorThdDefnT *
					     threshold_def,
					     SaHpiSensorReadingT * reading,
					     saHpiSensorThdPosHysteresisTable_context
					     * ctx)
{

  long hash = 0;
  unsigned int update_entry = MIB_FALSE;
  //  char format[SENSOR_THD_INTER_MAX];

  DEBUGMSGTL ((AGENT,
	       "Modify saHpiSensorThdPosHysteresisTable_ctx: Entry.\n"));

  if (ctx)
    {
      hash = calculate_hash_value (reading, sizeof (SaHpiSensorReadingT));

      DEBUGMSGTL ((AGENT, " Hash value: %d, in ctx: %d\n", hash, ctx->hash));

      if (ctx->hash != 0)
	{
	  /* Only do the check if the hash value is something else than zero.
	   * 'zero' value is only for newly created records, and in some
	   * rare instances when the hash has rolled to zero - in which
	   * case we will just consider the worst-case scenario and update
	   * the record and not trust the hash value.
	   */
	  if (hash == ctx->hash)
	    {
	      /* The same data. No need to change. */
	      return AGENT_ENTRY_EXIST;
	    }
	  if ((ctx->domain_id == domain_id) &&
	      (ctx->resource_id == resource_id) &&
	      (ctx->sensor_id == sensor_num))
	    {
	      update_entry = MIB_TRUE;
	      DEBUGMSGTL ((AGENT,
			   "Posdating ThdPosHysteresisTable row [%d, %d, %d]\n",
			   domain_id, resource_id, sensor_num));
	    }
	}

      if (hash == 0)		/* Might happend - roll-over */
	hash = 1;		/* Need this - we consider hash
				 * values of '0' uninitialized */
      ctx->hash = hash;
      ctx->resource_id = resource_id;
      ctx->domain_id = domain_id;
      ctx->sensor_id = sensor_num;


      build_reading_strings (reading,
			     0,
			     &ctx->saHpiSensorThdPosHysteresisValuesPresent,
			     &ctx->saHpiSensorThdPosHysteresisRaw,
			     ctx->saHpiSensorThdPosHysteresisInterpreted,
			     &ctx->saHpiSensorThdPosHysteresisInterpreted_len,
			     SENSOR_THD_INTER_MAX, NULL, NULL, NULL, 0);
      if (threshold_def)
	{
	  ctx->saHpiSensorThdPosHysteresisIsReadable =
	    ((threshold_def->ReadThold & SAHPI_STM_UP_HYSTERESIS) ==
	     SAHPI_STM_UP_HYSTERESIS) ? MIB_TRUE : MIB_FALSE;

	  ctx->saHpiSensorThdPosHysteresisIsWritable =
	    ((threshold_def->WriteThold & SAHPI_STM_UP_HYSTERESIS) ==
	     SAHPI_STM_UP_HYSTERESIS) ? MIB_TRUE : MIB_FALSE;
	  ctx->saHpiSensorThdPosHysteresisIsFixed =
	    ((threshold_def->FixedThold & SAHPI_STM_UP_HYSTERESIS) ==
	     SAHPI_STM_UP_HYSTERESIS) ? MIB_TRUE : MIB_FALSE;
	}
      /* END */
      DEBUGMSGTL ((AGENT,
		   "Modify saHpiSensorThdPosHysteresisTable_ctx: Exit"));
      if (update_entry == MIB_TRUE)
	return AGENT_ENTRY_EXIST;
      return AGENT_NEW_ENTRY;

    }

  DEBUGMSGTL ((AGENT,
	       "Modify saHpiSensorThdPosHysteresisTable_ctx: Exit (NULL DATA)"));

  return AGENT_ERR_NULL_DATA;
}


int
set_ThdPosHysteresis (saHpiSensorThdPosHysteresisTable_context * ctx)
{

  SaHpiSensorThresholdsT thd;
  SaHpiSessionIdT session_id;
  SaErrorT rc;

  DEBUGMSGTL ((AGENT, "set_ThdPosHysteresis: Entry.\n"));
  if (ctx)
    {

      memset (&thd, 0x00, sizeof (SaHpiSensorThresholdsT));

      rc = getSaHpiSession (&session_id);
      if (rc != AGENT_ERR_NOERROR)
	{
	  DEBUGMSGTL ((AGENT, "Call to getSaHpiSession failed with rc: %d\n",
		       rc));
	  return rc;
	}
      /*
       * Get the current threshold information
       */
      DEBUGMSGTL ((AGENT, "resource_id: %d, sensor_id: %d\n",
		   ctx->resource_id, ctx->sensor_id));
      rc =
	saHpiSensorThresholdsGet (session_id, ctx->resource_id,
				  ctx->sensor_id, &thd);

      if (rc != SA_OK)
	{
	  snmp_log (LOG_ERR,
		    "Call to saHpiSensorThresholdGet fails with return code: %s.\n",
		    get_error_string (rc));
	  DEBUGMSGTL ((AGENT,
		       "Call to saHpiSensorThresholdsGet fails with return code: %s\n",
		       get_error_string (rc)));
	  return AGENT_ERR_OPERATION;
	}

      /* Posdate the correct entry.    */

      if (thd.PosThdHysteresis.ValuesPresent & SAHPI_SRF_INTERPRETED)
	{
	  thd.PosThdHysteresis.Interpreted.Type =
	    SAHPI_SENSOR_INTERPRETED_TYPE_BUFFER;
	  memcpy (&thd.PosThdHysteresis.Interpreted.Value.SensorBuffer,
		  &ctx->saHpiSensorThdPosHysteresisInterpreted,
		  ctx->saHpiSensorThdPosHysteresisInterpreted_len);

	}
      if (thd.PosThdHysteresis.ValuesPresent & SAHPI_SRF_RAW)
	{
	  thd.PosThdHysteresis.Raw = ctx->saHpiSensorThdPosHysteresisRaw;
	}

      /*
       * Set the thresholds 
       */
      rc = saHpiSensorThresholdsSet (session_id,
				     ctx->resource_id, ctx->sensor_id, &thd);

      if (rc != SA_OK)
	{
	  snmp_log (LOG_ERR,
		    "Call to saHpiSensorThresholdSet fails with return code: %s.\n",
		    get_error_string (rc));
	  DEBUGMSGTL ((AGENT,
		       "Call to saHpiSensorThresholdsSet fails with return code: %s\n",
		       get_error_string (rc)));
	  return AGENT_ERR_OPERATION;
	}

      /* 
       * Re-read the data. Might be different, so we will need
       * to populate the ctx.
       */

      memset (&thd, 0x00, sizeof (SaHpiSensorThresholdsT));
      rc = saHpiSensorThresholdsGet (session_id,
				     ctx->resource_id, ctx->sensor_id, &thd);

      if (rc != SA_OK)
	{
	  snmp_log (LOG_ERR,
		    "Call to  SensorThresholdGet fails with return code: %s.\n",
		    get_error_string (rc));
	  DEBUGMSGTL ((AGENT,
		       "Call to  SensorThresholdGet fails with return code: %s.\n",
		       get_error_string (rc)));
	  return AGENT_ERR_OPERATION;
	}
      build_reading_strings (&thd.PosThdHysteresis,
			     0,
			     &ctx->saHpiSensorThdPosHysteresisValuesPresent,
			     &ctx->saHpiSensorThdPosHysteresisRaw,
			     ctx->saHpiSensorThdPosHysteresisInterpreted,
			     &ctx->saHpiSensorThdPosHysteresisInterpreted_len,
			     SENSOR_THD_INTER_MAX, NULL, NULL, NULL, 0);


      DEBUGMSGTL ((AGENT, "set_ThdPosHysteresis: Exit.\n"));
      return AGENT_ERR_NOERROR;
    }
  DEBUGMSGTL ((AGENT, "set_sensor: Exit.\n"));

  return AGENT_ERR_NULL_DATA;


}

/************************************************************
 * the *_row_copy routine
 */
static int
  saHpiSensorThdPosHysteresisTable_row_copy
  (saHpiSensorThdPosHysteresisTable_context * dst,
   saHpiSensorThdPosHysteresisTable_context * src)
{
  if (!dst || !src)
    return 1;

  /*
   * copy index, if provided
   */
  if (dst->index.oids)
    free (dst->index.oids);
  if (snmp_clone_mem ((void *) &dst->index.oids, src->index.oids,
		      src->index.len * sizeof (oid)))
    {
      dst->index.oids = NULL;
      return 1;
    }
  dst->index.len = src->index.len;


  /*
   * copy components into the context structure
   */
  dst->saHpiSensorThdPosHysteresisIsReadable =
    src->saHpiSensorThdPosHysteresisIsReadable;

  dst->saHpiSensorThdPosHysteresisIsWritable =
    src->saHpiSensorThdPosHysteresisIsWritable;

  dst->saHpiSensorThdPosHysteresisIsFixed =
    src->saHpiSensorThdPosHysteresisIsFixed;

  dst->saHpiSensorThdPosHysteresisValuesPresent =
    src->saHpiSensorThdPosHysteresisValuesPresent;

  dst->saHpiSensorThdPosHysteresisRaw = src->saHpiSensorThdPosHysteresisRaw;

  memcpy (dst->saHpiSensorThdPosHysteresisInterpreted,
	  src->saHpiSensorThdPosHysteresisInterpreted,
	  src->saHpiSensorThdPosHysteresisInterpreted_len);
  dst->saHpiSensorThdPosHysteresisInterpreted_len =
    src->saHpiSensorThdPosHysteresisInterpreted_len;

  dst->resource_id = src->resource_id;
  dst->domain_id = src->domain_id;
  dst->sensor_id = src->sensor_id;
  dst->hash = src->hash;

  return 0;
}



/**
 * the *_extract_index routine
 *
 * This routine is called when a set request is received for an index
 * that was not found in the table container. Here, we parse the oid
 * in the the individual index components and copy those indexes to the
 * context. Then we make sure the indexes for the new row are valid.
 */
int
  saHpiSensorThdPosHysteresisTable_extract_index
  (saHpiSensorThdPosHysteresisTable_context * ctx, netsnmp_index * hdr)
{
  /*
   * temporary local storage for extracting oid index
   *
   * extract index uses varbinds (netsnmp_variable_list) to parse
   * the index OID into the individual components for each index part.
   */
  netsnmp_variable_list var_saHpiDomainID;
  netsnmp_variable_list var_saHpiResourceID;
  netsnmp_variable_list var_saHpiSensorIndex;
  int err;

  /*
   * copy index, if provided
   */
  if (hdr)
    {
      netsnmp_assert (ctx->index.oids == NULL);
      if (snmp_clone_mem ((void *) &ctx->index.oids, hdr->oids,
			  hdr->len * sizeof (oid)))
	{
	  return -1;
	}
      ctx->index.len = hdr->len;
    }

  /*
   * initialize variable that will hold each component of the index.
   * If there are multiple indexes for the table, the variable_lists
   * need to be linked together, in order.
   */
  memset (&var_saHpiDomainID, 0x00, sizeof (var_saHpiDomainID));
  var_saHpiDomainID.type = ASN_UNSIGNED;	/* type hint for parse_oid_indexes */

  var_saHpiDomainID.next_variable = &var_saHpiResourceID;

  memset (&var_saHpiResourceID, 0x00, sizeof (var_saHpiResourceID));
  var_saHpiResourceID.type = ASN_UNSIGNED;	/* type hint for parse_oid_indexes */

  var_saHpiResourceID.next_variable = &var_saHpiSensorIndex;

  memset (&var_saHpiSensorIndex, 0x00, sizeof (var_saHpiSensorIndex));
  var_saHpiSensorIndex.type = ASN_UNSIGNED;	/* type hint for parse_oid_indexes */

  var_saHpiSensorIndex.next_variable = NULL;

  /*
   * parse the oid into the individual index components
   */
  err = parse_oid_indexes (hdr->oids, hdr->len, &var_saHpiDomainID);
  if (err == SNMP_ERR_NOERROR)
    {
      /*
       * copy index components into the context structure
       */
      ctx->domain_id = *var_saHpiDomainID.val.integer;
      ctx->resource_id = *var_saHpiResourceID.val.integer;
      ctx->sensor_id = *var_saHpiSensorIndex.val.integer;
    }

  /*
   * parsing may have allocated memory. free it.
   */
  snmp_reset_var_buffers (&var_saHpiDomainID);

  return err;
}

/************************************************************
 * the *_can_delete routine is called to determine if a row
 * can be deleted.
 *
 * return 1 if the row can be deleted
 * return 0 if the row cannot be deleted
 */
int
  saHpiSensorThdPosHysteresisTable_can_delete
  (saHpiSensorThdPosHysteresisTable_context * undo_ctx,
   saHpiSensorThdPosHysteresisTable_context * row_ctx,
   netsnmp_request_group * rg)
{

  return 1;
}

/************************************************************
 * the *_create_row routine is called by the table handler
 * to create a new row for a given index. If you need more
 * information (such as column values) to make a decision
 * on creating rows, you must create an initial row here
 * (to hold the column values), and you can examine the
 * situation in more detail in the *_set_reserve1 or later
 * states of set processing. Simple check for a NULL undo_ctx
 * in those states and do detailed creation checking there.
 *
 * returns a newly allocated saHpiSensorThdPosHysteresisTable_context
 *   structure if the specified indexes are not illegal
 * returns NULL for errors or illegal index values.
 */
saHpiSensorThdPosHysteresisTable_context *
saHpiSensorThdPosHysteresisTable_create_row (netsnmp_index * hdr)
{
  saHpiSensorThdPosHysteresisTable_context *ctx =
    SNMP_MALLOC_TYPEDEF (saHpiSensorThdPosHysteresisTable_context);
  if (!ctx)
    return NULL;

  if (saHpiSensorThdPosHysteresisTable_extract_index (ctx, hdr))
    {
      free (ctx->index.oids);
      free (ctx);
      return NULL;
    }
  ctx->saHpiSensorThdPosHysteresisIsReadable = MIB_FALSE;
  ctx->saHpiSensorThdPosHysteresisIsWritable = MIB_FALSE;
  ctx->saHpiSensorThdPosHysteresisIsFixed = MIB_FALSE;
  ctx->saHpiSensorThdPosHysteresisValuesPresent = 0;
  return ctx;
}


/************************************************************
 * the *_duplicate row routine
 */
saHpiSensorThdPosHysteresisTable_context
  * saHpiSensorThdPosHysteresisTable_duplicate_row
  (saHpiSensorThdPosHysteresisTable_context * row_ctx)
{
  saHpiSensorThdPosHysteresisTable_context *dup;

  if (!row_ctx)
    return NULL;

  dup = SNMP_MALLOC_TYPEDEF (saHpiSensorThdPosHysteresisTable_context);
  if (!dup)
    return NULL;

  if (saHpiSensorThdPosHysteresisTable_row_copy (dup, row_ctx))
    {
      free (dup);
      dup = NULL;
    }

  return dup;
}

/************************************************************
 * the *_delete_row method is called to delete a row.
 */
netsnmp_index *saHpiSensorThdPosHysteresisTable_delete_row
  (saHpiSensorThdPosHysteresisTable_context * ctx)
{
  /*
   * netsnmp_mutex_destroy(ctx->lock); 
   */

  if (ctx->index.oids)
    free (ctx->index.oids);

  /*
   * release header
   */
  free (ctx);

  return NULL;
}


/************************************************************
 * RESERVE is used to check the syntax of all the variables
 * provided, that the values being set are sensible and consistent,
 * and to allocate any resources required for performing the SET.
 * After this stage, the expectation is that the set ought to
 * succeed, though this is not guaranteed. (In fact, with the UCD
 * agent, this is done in two passes - RESERVE1, and
 * RESERVE2, to allow for dependancies between variables).
 *
 * BEFORE calling this routine, the agent will call duplicate_row
 * to create a copy of the row (unless this is a new row; i.e.
 * row_created == 1).
 *
 * next state -> SET_RESERVE2 || SET_FREE
 */
void
saHpiSensorThdPosHysteresisTable_set_reserve1 (netsnmp_request_group * rg)
{
  saHpiSensorThdPosHysteresisTable_context *row_ctx =
    (saHpiSensorThdPosHysteresisTable_context *) rg->existing_row;

  netsnmp_variable_list *var;
  netsnmp_request_group_item *current;
  int rc = 0;

  DEBUGMSGTL ((AGENT,
	       "saHpiSensorThdPosHysteresisTable_set_reserve1. Entry.\n"));
  for (current = rg->list; current; current = current->next)
    {

      var = current->ri->requestvb;
      rc = SNMP_ERR_NOERROR;

      switch (current->tri->colnum)
	{

	case COLUMN_SAHPISENSORTHDPOSHYSTERESISICALISREADABLE:
	case COLUMN_SAHPISENSORTHDPOSHYSTERESISICALISWRITABLE:
	case COLUMN_SAHPISENSORTHDPOSHYSTERESISICALISFIXED:
	case COLUMN_SAHPISENSORTHDPOSHYSTERESISICALVALUESPRESENT:
	  rc = SNMP_ERR_NOTWRITABLE;
	  break;

	case COLUMN_SAHPISENSORTHDPOSHYSTERESISICALRAW:
	    /** UNSIGNED32 = ASN_UNSIGNED */
	  rc = netsnmp_check_vb_type_and_size (var, ASN_UNSIGNED,
					       sizeof (row_ctx->
						       saHpiSensorThdPosHysteresisRaw));
	  break;

	case COLUMN_SAHPISENSORTHDPOSHYSTERESISICALINTERPRETED:
	    /** OCTETSTR = ASN_OCTET_STR */
	  if (var->type != ASN_OCTET_STR)
	    {
	      rc = SNMP_ERR_WRONGTYPE;
	    }
	  break;

	default:
		/** We shouldn't get here */
	  rc = SNMP_ERR_GENERR;
	  snmp_log (LOG_ERR, "unknown column in "
		    "saHpiSensorThdPosHysteresisTable_set_reserve1\n");
	}

      if (rc)
	netsnmp_set_mode_request_error (MODE_SET_BEGIN, current->ri, rc);
      rg->status = SNMP_MAX (rg->status, current->ri->status);
    }
  DEBUGMSGTL ((AGENT,
	       "saHpiSensorThdPosHysteresisTable_set_reserve1. Exit. (rc:%d) \n",
	       rc));
}

void
saHpiSensorThdPosHysteresisTable_set_reserve2 (netsnmp_request_group * rg)
{
  saHpiSensorThdPosHysteresisTable_context *row_ctx =
    (saHpiSensorThdPosHysteresisTable_context *) rg->existing_row;
  netsnmp_request_group_item *current;
  netsnmp_variable_list *var;
  int rc = 0;

  rg->rg_void = rg->list->ri;

  DEBUGMSGTL ((AGENT,
	       "saHpiSensorThdPosHysteresisTable_set_reserve2. Entry.\n"));
  for (current = rg->list; current; current = current->next)
    {

      var = current->ri->requestvb;
      rc = SNMP_ERR_NOERROR;

      switch (current->tri->colnum)
	{
	case COLUMN_SAHPISENSORTHDPOSHYSTERESISICALINTERPRETED:
	case COLUMN_SAHPISENSORTHDPOSHYSTERESISICALRAW:
	    /** UNSIGNED32 = ASN_UNSIGNED */
	  if (row_ctx->saHpiSensorThdPosHysteresisIsWritable == MIB_FALSE)
	    {
	      rc = SNMP_ERR_NOACCESS;
	    }
	  if (row_ctx->saHpiSensorThdPosHysteresisIsFixed == MIB_TRUE)
	    {
	      rc = SNMP_ERR_NOACCESS;
	    }

	  break;


	default:
		/** We shouldn't get here */
	  netsnmp_assert (0);  /** why wasn't this caught in reserve1? */
	}

      if (rc)
	netsnmp_set_mode_request_error (MODE_SET_BEGIN, current->ri, rc);
    }

  DEBUGMSGTL ((AGENT,
	       "saHpiSensorThdPosHysteresisTable_set_reserve2. Exit (rc:%d).\n",
	       rc));
}

/************************************************************
 * Assuming that the RESERVE phases were successful, the next
 * stage is indicated by the action value ACTION. This is used
 * to actually implement the set operation. However, this must
 * either be done into temporary (persistent) storage, or the
 * previous value stored similarly, in case any of the subsequent
 * ACTION calls fail.
 *
 * In your case, changes should be made to row_ctx. A copy of
 * the original row is in undo_ctx.
 */
void
saHpiSensorThdPosHysteresisTable_set_action (netsnmp_request_group * rg)
{
  netsnmp_variable_list *var;
  saHpiSensorThdPosHysteresisTable_context *row_ctx =
    (saHpiSensorThdPosHysteresisTable_context *) rg->existing_row;
  netsnmp_request_group_item *current;

  int rc = 0;

  DEBUGMSGTL ((AGENT,
	       "saHpiSensorThdPosHysteresisTable_set_action. Entry\n"));
  for (current = rg->list; current; current = current->next)
    {

      var = current->ri->requestvb;

      switch (current->tri->colnum)
	{

	case COLUMN_SAHPISENSORTHDPOSHYSTERESISICALRAW:
	    /** UNSIGNED32 = ASN_UNSIGNED */
	  row_ctx->saHpiSensorThdPosHysteresisRaw = *var->val.integer;
	  if (set_ThdPosHysteresis (row_ctx) != AGENT_ERR_NOERROR)
	    rc = SNMP_ERR_GENERR;
	  break;

	case COLUMN_SAHPISENSORTHDPOSHYSTERESISICALINTERPRETED:
	    /** OCTETSTR = ASN_OCTET_STR */
	  memcpy (row_ctx->saHpiSensorThdPosHysteresisInterpreted,
		  var->val.string, var->val_len);
	  row_ctx->saHpiSensorThdPosHysteresisInterpreted_len = var->val_len;
	  if (set_ThdPosHysteresis (row_ctx) != AGENT_ERR_NOERROR)
	    rc = SNMP_ERR_GENERR;

	  break;

	default:
		/** We shouldn't get here */
	  netsnmp_assert (0);  /** why wasn't this caught in reserve1? */
	}
    }


  if (rc)
    {
      netsnmp_set_mode_request_error (MODE_SET_BEGIN,
				      (netsnmp_request_info *) rg->
				      rg_void, rc);
      return;
    }
  DEBUGMSGTL ((AGENT,
	       "saHpiSensorThdPosHysteresisTable_set_action. Exit (rc: %d)\n",
	       rc));
}

/************************************************************
 * Only once the ACTION phase has completed successfully, can
 * the final COMMIT phase be run. This is used to complete any
 * writes that were done into temporary storage, and then release
 * any allocated resources. Note that all the code in this phase
 * should be "safe" code that cannot possibly fail (cue
 * hysterical laughter). The whole intent of the ACTION/COMMIT
 * division is that all of the fallible code should be done in
 * the ACTION phase, so that it can be backed out if necessary.
 *
 * BEFORE calling this routine, the agent will update the
 * container (inserting a row if row_created == 1, or removing
 * the row if row_deleted == 1).
 *
 * AFTER calling this routine, the agent will delete the
 * undo_info.
 */
void
saHpiSensorThdPosHysteresisTable_set_commit (netsnmp_request_group * rg)
{


}

/************************************************************
 * If either of the RESERVE calls fail, the write routines
 * are called again with the FREE action, to release any resources
 * that have been allocated. The agent will then return a failure
 * response to the requesting application.
 *
 * AFTER calling this routine, the agent will delete undo_info.
 */
void
saHpiSensorThdPosHysteresisTable_set_free (netsnmp_request_group * rg)
{

}

/************************************************************
 * If the ACTION phase does fail (for example due to an apparently
 * valid, but unacceptable value, or an unforeseen problem), then
 * the list of write routines are called again, with the UNDO
 * action. This requires the routine to reset the value that was
 * changed to its previous value (assuming it was actually changed),
 * and then to release any resources that had been allocated. As
 * with the FREE phase, the agent will then return an indication
 * of the error to the requesting application.
 *
 * BEFORE calling this routine, the agent will update the container
 * (remove any newly inserted row, re-insert any removed row).
 *
 * AFTER calling this routing, the agent will call row_copy
 * to restore the data in existing_row from the date in undo_info.
 * Then undo_info will be deleted (or existing row, if row_created
 * == 1).
 */
void
saHpiSensorThdPosHysteresisTable_set_undo (netsnmp_request_group * rg)
{

}




/************************************************************
 *
 * Initialize the saHpiSensorThdPosHysteresisTable table by defining its contents and how it's structured
 */
void
initialize_table_saHpiSensorThdPosHysteresisTable (void)
{
  netsnmp_table_registration_info *table_info;

  if (my_handler)
    {
      snmp_log (LOG_ERR,
		"initialize_table_saHpiSensorThdPosHysteresisTable_handler called again\n");
      return;
    }

  memset (&cb, 0x00, sizeof (cb));

    /** create the table structure itself */
  table_info = SNMP_MALLOC_TYPEDEF (netsnmp_table_registration_info);

  /*
   * if your table is read only, it's easiest to change the
   * HANDLER_CAN_RWRITE definition below to HANDLER_CAN_RONLY 
   */
  my_handler =
    netsnmp_create_handler_registration
    ("saHpiSensorThdPosHysteresisTable",
     netsnmp_table_array_helper_handler,
     saHpiSensorThdPosHysteresisTable_oid,
     saHpiSensorThdPosHysteresisTable_oid_len, HANDLER_CAN_RWRITE);

  if (!my_handler || !table_info)
    {
      snmp_log (LOG_ERR, "malloc failed in "
		"initialize_table_saHpiSensorThdPosHysteresisTable_handler\n");
      return;	/** mallocs failed */
    }

    /***************************************************
     * Setting up the table's definition
     */

  /*
   * internal indexes
   */
	/** index: saHpiDomainID */
  netsnmp_table_helper_add_index (table_info, ASN_UNSIGNED);
	/** index: saHpiResourceID */
  netsnmp_table_helper_add_index (table_info, ASN_UNSIGNED);
	/** index: saHpiSensorIndex */
  netsnmp_table_helper_add_index (table_info, ASN_UNSIGNED);

  table_info->min_column = saHpiSensorThdPosHysteresisTable_COL_MIN;
  table_info->max_column = saHpiSensorThdPosHysteresisTable_COL_MAX;

    /***************************************************
     * registering the table with the master agent
     */
  cb.get_value = saHpiSensorThdPosHysteresisTable_get_value;
  cb.container =
    netsnmp_container_find ("saHpiSensorThdPosHysteresisTable_primary:"
			    "saHpiSensorThdPosHysteresisTable:"
			    "table_container");


  cb.create_row =
    (UserRowMethod *) saHpiSensorThdPosHysteresisTable_create_row;

  cb.duplicate_row =
    (UserRowMethod *) saHpiSensorThdPosHysteresisTable_duplicate_row;
  cb.delete_row =
    (UserRowMethod *) saHpiSensorThdPosHysteresisTable_delete_row;
  cb.row_copy =
    (Netsnmp_User_Row_Operation *) saHpiSensorThdPosHysteresisTable_row_copy;

  cb.can_delete =
    (Netsnmp_User_Row_Action *) saHpiSensorThdPosHysteresisTable_can_delete;

  cb.set_reserve1 = saHpiSensorThdPosHysteresisTable_set_reserve1;
  cb.set_reserve2 = saHpiSensorThdPosHysteresisTable_set_reserve2;
  cb.set_action = saHpiSensorThdPosHysteresisTable_set_action;
  cb.set_commit = saHpiSensorThdPosHysteresisTable_set_commit;
  cb.set_free = saHpiSensorThdPosHysteresisTable_set_free;
  cb.set_undo = saHpiSensorThdPosHysteresisTable_set_undo;

  DEBUGMSGTL (("initialize_table_saHpiSensorThdPosHysteresisTable",
	       "Registering table saHpiSensorThdPosHysteresisTable "
	       "as a table array\n"));
  netsnmp_table_container_register (my_handler, table_info, &cb,
				    cb.container, 1);
}

/************************************************************
 * saHpiSensorThdPosHysteresisTable_get_value
 *
 * This routine is called for get requests to copy the data
 * from the context to the varbind for the request. If the
 * context has been properly maintained, you don't need to
 * change in code in this fuction.
 */
int
saHpiSensorThdPosHysteresisTable_get_value (netsnmp_request_info * request,
					    netsnmp_index * item,
					    netsnmp_table_request_info
					    * table_info)
{
  netsnmp_variable_list *var = request->requestvb;
  saHpiSensorThdPosHysteresisTable_context *context =
    (saHpiSensorThdPosHysteresisTable_context *) item;

#ifdef GET_ROUTINE_CALLS_SNMP_GET
  SaHpiSensorThresholdsT sensor_threshold;
  SaHpiSessionIdT session_id;
  int rc = AGENT_ERR_NOERROR;
  rc = getSaHpiSession (&session_id);
  if (rc != AGENT_ERR_NOERROR)
    {
      DEBUGMSGTL ((AGENT, "Call to getSaHpiSession failed with rc: %d\n",
		   rc));
    }
  rc = saHpiSensorThresholdsGet (session_id,
				 context->resource_id,
				 context->sensor_id, &sensor_threshold);

  if (rc != SA_OK)
    {
      snmp_log (LOG_ERR,
		"Call to saHpiSensorThresholdsGet fails with return code: %s.\n",
		get_error_string (rc));
      DEBUGMSGTL ((AGENT,
		   "Call to  SensorThresholdGet fails with return code: %s.\n",
		   get_error_string (rc)));
      return AGENT_ERR_OPERATION;
    }
  if (rc == AGENT_ERR_NOERROR)
    {
      modify_saHpiSensorThdPosHysteresisTable_row (context->domain_id,
						   context->resource_id,
						   context->sensor_id,
						   NULL,
						   &sensor_threshold.
						   PosThdHysteresis, context);
    }
#endif
  switch (table_info->colnum)
    {

    case COLUMN_SAHPISENSORTHDPOSHYSTERESISICALISREADABLE:
	    /** TruthValue = ASN_INTEGER */
      snmp_set_var_typed_value (var, ASN_INTEGER,
				(char *) &context->
				saHpiSensorThdPosHysteresisIsReadable,
				sizeof (context->
					saHpiSensorThdPosHysteresisIsReadable));
      break;

    case COLUMN_SAHPISENSORTHDPOSHYSTERESISICALISWRITABLE:
	    /** TruthValue = ASN_INTEGER */
      snmp_set_var_typed_value (var, ASN_INTEGER,
				(char *) &context->
				saHpiSensorThdPosHysteresisIsWritable,
				sizeof (context->
					saHpiSensorThdPosHysteresisIsWritable));
      break;

    case COLUMN_SAHPISENSORTHDPOSHYSTERESISICALISFIXED:
	    /** TruthValue = ASN_INTEGER */
      snmp_set_var_typed_value (var, ASN_INTEGER,
				(char *) &context->
				saHpiSensorThdPosHysteresisIsFixed,
				sizeof (context->
					saHpiSensorThdPosHysteresisIsFixed));
      break;

    case COLUMN_SAHPISENSORTHDPOSHYSTERESISICALVALUESPRESENT:
	    /** INTEGER = ASN_INTEGER */
      snmp_set_var_typed_value (var, ASN_INTEGER,
				(char *) &context->
				saHpiSensorThdPosHysteresisValuesPresent,
				sizeof (context->
					saHpiSensorThdPosHysteresisValuesPresent));
      break;

    case COLUMN_SAHPISENSORTHDPOSHYSTERESISICALRAW:
	    /** UNSIGNED32 = ASN_UNSIGNED */
      if (context->saHpiSensorThdPosHysteresisIsReadable == MIB_TRUE)
	snmp_set_var_typed_value (var, ASN_UNSIGNED,
				  (char *) &context->
				  saHpiSensorThdPosHysteresisRaw,
				  sizeof (context->
					  saHpiSensorThdPosHysteresisRaw));
      break;

    case COLUMN_SAHPISENSORTHDPOSHYSTERESISICALINTERPRETED:
	    /** OCTETSTR = ASN_OCTET_STR */
      if (context->saHpiSensorThdPosHysteresisIsReadable == MIB_TRUE)
	snmp_set_var_typed_value (var, ASN_OCTET_STR,
				  (char *) &context->
				  saHpiSensorThdPosHysteresisInterpreted,
				  context->
				  saHpiSensorThdPosHysteresisInterpreted_len);
      break;

    default:
	    /** We shouldn't get here */
      snmp_log (LOG_ERR, "unknown column in "
		"saHpiSensorThdPosHysteresisTable_get_value\n");
      return SNMP_ERR_GENERR;
    }
  return SNMP_ERR_NOERROR;
}
