/*
 * Note: this file originally auto-generated by mib2c using
 *       : mib2c.array-user.conf,v 5.18.2.2 2004/02/09 18:21:47 rstory Exp $
 *
 * $Id$
 *
 *
 * For help understanding NET-SNMP in general, please check the 
 *     documentation and FAQ at:
 *
 *     http://www.net-snmp.org/
 *
 *
 * For help understanding this code, the agent and how it processes
 *     requests, please check the following references.
 *
 *     http://www.net-snmp.org/tutorial-5/
 *
 *
 * You can also join the #net-snmp channel on irc.freenode.net
 *     and ask for help there.
 *
 *
 * And if all else fails, send a detailed message to the developers
 *     describing the problem you are having to:
 *
 *    net-snmp-coders@lists.sourceforge.net
 *
 *
 * Yes, there is lots of code here that you might not use. But it is much
 * easier to remove code than to add it!
 */
#include <net-snmp/net-snmp-config.h>
#include <net-snmp/net-snmp-includes.h>
#include <net-snmp/agent/net-snmp-agent-includes.h>

#include <net-snmp/library/snmp_assert.h>

#include <SaHpi.h>
#include "saHpiDomainEventLogTable.h"
#include <hpiSubagent.h>
#include <hpiCheckIndice.h>
#include <session_info.h>
#include <oh_utils.h>

static     netsnmp_handler_registration *my_handler = NULL;
static     netsnmp_table_array_callbacks cb;

oid saHpiDomainEventLogTable_oid[] = { saHpiDomainEventLogTable_TABLE_OID };
size_t saHpiDomainEventLogTable_oid_len = OID_LENGTH(saHpiDomainEventLogTable_oid);


/************************************************************/
/************************************************************/
/************************************************************/
/************************************************************/

/*************************************************************
 * objects for hash table
 */
static int initialized = FALSE;		      
static GHashTable *dr_table;

/*************************************************************
 * oid and fucntion declarations scalars
 */
static u_long domain_event_log_entry_count_total = 0;
static u_long domain_event_log_entry_count = 0;

static oid saHpiDomainEventLogEntryCountTotal_oid[] = { 1,3,6,1,4,1,18568,2,1,1,3,2,6 };
static oid saHpiDomainEventLogEntryCount_oid[] = { 1,3,6,1,4,1,18568,2,1,1,3,2,7 };

int handle_saHpiDomainEventLogEntryCountTotal(netsnmp_mib_handler *handler,
                                        netsnmp_handler_registration *reginfo,
                                        netsnmp_agent_request_info   *reqinfo,
                                        netsnmp_request_info         *requests);
			  
int handle_saHpiDomainEventLogEntryCount(netsnmp_mib_handler *handler,
                                        netsnmp_handler_registration *reginfo,
                                        netsnmp_agent_request_info   *reqinfo,
                                        netsnmp_request_info         *requests);			  

int initialize_table_saHpiDomainEventLogEntryCountTotal(void);
int initialize_table_saHpiDomainEventLogEntryCount(void); 

SaErrorT populate_saHpiDomainEventLogTable(SaHpiSessionIdT sessionid, 
                                            SaHpiEventLogEntryT *event,
                                            oid * this_child_oid, 
                                            size_t *this_child_oid_len)
{
	SaErrorT rv = SA_OK;

	oid domain_evt_oid[DOMAIN_EVENT_LOG_INDEX_NR];
	netsnmp_index domain_evt_idx;
	saHpiDomainEventLogTable_context *domain_evt_ctx;

	oid column[2];
	int column_len = 2;
	
	int isNewRow = MIB_TRUE;

        DR_XREF *dr_entry;
	SaHpiDomainIdResourceIdArrayT dr_pair;

        DEBUGMSGTL ((AGENT, "populate_saHpiDomainEventLogTable, called\n"));

	/* check for NULL pointers */
	if (!event) {
		DEBUGMSGTL ((AGENT, 
		"ERROR: populate_saHpiDomainEventLogTable() passed NULL event pointer\n"));
		return AGENT_ERR_INTERNAL_ERROR;
	}    


	/* BUILD oid for new row */
		/* assign the number of indices */
	domain_evt_idx.len = DOMAIN_EVENT_LOG_INDEX_NR;
		/** Index saHpiDomainId is external */
	domain_evt_oid[0] = get_domain_id(sessionid);
                /** Index saHpiDomainEventEntryId is external */	
	dr_pair.domainId_resourceId_arry[0] = get_domain_id(sessionid);
	dr_pair.domainId_resourceId_arry[1] = event->Event.Source;
	dr_entry = domain_resource_pair_get(&dr_pair, &dr_table); 
	if (dr_entry == NULL) {
		DEBUGMSGTL ((AGENT, 
		"ERROR: populate_saHpiDomainEventLogTable() domain_resource_pair_get returned NULL\n"));
		return AGENT_ERR_INTERNAL_ERROR;
	}
	domain_evt_oid[1] = dr_entry->entry_id++;
		/** Index saHpiEventSeverity is external */
	domain_evt_oid[2] = event->Event.Severity + 1;
		/* assign the indices to the index */
	domain_evt_idx.oids = (oid *) & domain_evt_oid;
	
	/* create full oid on This row for parent RowPointer */
	column[0] = 1;
	column[1] = COLUMN_SAHPIDOMAINEVENTLOGTIMESTAMP;
	memset(this_child_oid, 0, sizeof(this_child_oid));
	build_full_oid(saHpiDomainEventLogTable_oid, saHpiDomainEventLogTable_oid_len,
			column, column_len,
			&domain_evt_idx,
			this_child_oid, MAX_OID_LEN, this_child_oid_len);	

	/* See if Row exists. */
	domain_evt_ctx = NULL;
	domain_evt_ctx = CONTAINER_FIND(cb.container, &domain_evt_idx);

	if (!domain_evt_ctx) { 
		// New entry. Add it
		domain_evt_ctx = 
			saHpiDomainEventLogTable_create_row(&domain_evt_idx);
	}
	else {
		isNewRow = MIB_FALSE;
	}
		
	if (!domain_evt_ctx) {
		snmp_log (LOG_ERR, "Not enough memory for a Domain Event Log row!");
		rv = AGENT_ERR_INTERNAL_ERROR;
	}

        /** SaHpiEntryId = ASN_UNSIGNED */
        domain_evt_ctx->saHpiDomainEventLogEntryId = domain_evt_oid[1];

        /** SaHpiTime = ASN_COUNTER64 */
        domain_evt_ctx->saHpiDomainEventLogTimestamp = event->Timestamp;              

        /** INTEGER = ASN_INTEGER */
        domain_evt_ctx->saHpiDomainEventLogType = 
	                event->Event.EventDataUnion.DomainEvent.Type + 1;

	
	if (isNewRow == MIB_TRUE) {
		CONTAINER_INSERT (cb.container, domain_evt_ctx);
		domain_event_log_entry_count = CONTAINER_SIZE (cb.container);		
	}
	
        return SA_OK;
}  

/**
 * 
 * @session_id
 * @resource_id
 * @saHpiEventLogRowPointer
 * @aHpiEventLogRowPointer_len
 * 
 * @return 
 */
SaErrorT domain_event_log_clear(SaHpiSessionIdT session_id, 
                                SaHpiResourceIdT resource_id,  
                                oid *saHpiEventLogRowPointer, 
                                size_t saHpiEventLogRowPointer_len)
{
     
	oid domain_evt_oid[DOMAIN_EVENT_LOG_INDEX_NR];
	netsnmp_index domain_evt_idx;
	netsnmp_index *domain_index;
	saHpiDomainEventLogTable_context *domain_evt_ctx;

	int column_len = 2;

        DEBUGMSGTL ((AGENT, "domain_event_log_clear, called\n"));
	DEBUGMSGTL ((AGENT, "Attempting to delete domain el row with the following indexes:\n"));
        printf("     Domain   [%ld]\n", saHpiEventLogRowPointer[saHpiDomainEventLogTable_oid_len + column_len]);
        printf("     Entry id [%ld]\n", saHpiEventLogRowPointer[saHpiDomainEventLogTable_oid_len + column_len + 1]);
	printf("     Severity [%s]\n",  oh_lookup_severity(
						saHpiEventLogRowPointer[saHpiDomainEventLogTable_oid_len + column_len + 2]-1));	
	/* BUILD oid for new row */
		/* assign the number of indices */
	domain_evt_idx.len = DOMAIN_EVENT_LOG_INDEX_NR;
		/** Index saHpiDomainId is external */
	domain_evt_oid[0] = saHpiEventLogRowPointer[saHpiDomainEventLogTable_oid_len + column_len];
                /** Index saHpiDomainEventEntryId is external */	
	domain_evt_oid[1] = saHpiEventLogRowPointer[saHpiDomainEventLogTable_oid_len + column_len + 1];
		/** Index saHpiEventSeverity is external */
	domain_evt_oid[2] = saHpiEventLogRowPointer[saHpiDomainEventLogTable_oid_len + column_len + 2];
		/* assign the indices to the index */
	domain_evt_idx.oids = (oid *) & domain_evt_oid;
			
	domain_index = CONTAINER_FIRST(cb.container);
	domain_evt_ctx = CONTAINER_FIND(cb.container, domain_index);
	
	if (!domain_evt_ctx) {
		DEBUGMSGTL ((AGENT, "domain_event_log_clear did not find a row to delete\n"));
	}
	else {
		
		DEBUGMSGTL ((AGENT, "domain_event_log_clear found row to delete\n"));
		CONTAINER_REMOVE(cb.container, domain_evt_ctx);
		saHpiDomainEventLogTable_delete_row(domain_evt_ctx);
		
		domain_event_log_entry_count = CONTAINER_SIZE (cb.container);	
		domain_event_log_entry_count_total--;
	}	
	
        return SA_OK;
}


/**
 * 
 * @handler:
 * @reginfo:
 * @reqinfo:
 * @requests:
 * 
 * @return:
 */
int
handle_saHpiDomainEventLogEntryCountTotal(netsnmp_mib_handler *handler,
                                        netsnmp_handler_registration *reginfo,
                                        netsnmp_agent_request_info   *reqinfo,
                                        netsnmp_request_info         *requests)
{
        /* We are never called for a GETNEXT if it's registered as a
           "instance", as it's "magically" handled for us.  */
        /* a instance handler also only hands us one request at a time, so
           we don't need to loop over a list of requests; we'll only get one. */

        DEBUGMSGTL ((AGENT, "handle_saHpiDomainEventLogEntryCountTotal, called\n"));

        
        switch(reqinfo->mode) {

        case MODE_GET:
                snmp_set_var_typed_value(requests->requestvb, ASN_COUNTER,
        			        (u_char *) &domain_event_log_entry_count_total,
        			        sizeof(domain_event_log_entry_count_total));
                break;


        default:
                /* we should never get here, so this is a really bad error */
                return SNMP_ERR_GENERR;
        }

        return SNMP_ERR_NOERROR;
} 
 
 /**
 * 
 * @handler:
 * @reginfo:
 * @reqinfo:
 * @requests:
 * 
 * @return:
 */
int
handle_saHpiDomainEventLogEntryCount(netsnmp_mib_handler *handler,
                                netsnmp_handler_registration *reginfo,
                                netsnmp_agent_request_info   *reqinfo,
                                netsnmp_request_info         *requests)
{
        /* We are never called for a GETNEXT if it's registered as a
           "instance", as it's "magically" handled for us.  */
        /* a instance handler also only hands us one request at a time, so
           we don't need to loop over a list of requests; we'll only get one. */
 
        DEBUGMSGTL ((AGENT, "handle_saHpiDomainEventLogEntryCount, called\n"));

        domain_event_log_entry_count = CONTAINER_SIZE (cb.container);
        
        switch(reqinfo->mode) {

        case MODE_GET:
                snmp_set_var_typed_value(requests->requestvb, ASN_COUNTER,
        			        (u_char *) &domain_event_log_entry_count,
        			        sizeof(domain_event_log_entry_count));
                break;


        default:
                /* we should never get here, so this is a really bad error */
                return SNMP_ERR_GENERR;
        }

        return SNMP_ERR_NOERROR;
}

 
/**
 * 
 * @return: 
 */
int initialize_table_saHpiDomainEventLogEntryCountTotal(void)
{

        DEBUGMSGTL ((AGENT, "initialize_table_saHpiDomainEventLogEntryCountTotal, called\n"));

        netsnmp_register_scalar(
                                netsnmp_create_handler_registration(
				        "saHpiDomainEventLogEntryCountTotal", 
					handle_saHpiDomainEventLogEntryCountTotal,
                                        saHpiDomainEventLogEntryCountTotal_oid, 
					OID_LENGTH(saHpiDomainEventLogEntryCountTotal_oid),
                                        HANDLER_CAN_RONLY ));
        return SNMP_ERR_NOERROR;
}


 
/**
 * 
 * @return: 
 */  
int initialize_table_saHpiDomainEventLogEntryCount(void)
{

        DEBUGMSGTL ((AGENT, "initialize_table_saHpiDomainEventLogEntryCount, called\n"));

        netsnmp_register_scalar(
	                        netsnmp_create_handler_registration(
				        "saHpiDomainEventLogEntryCount", 
					handle_saHpiDomainEventLogEntryCount,
			                saHpiDomainEventLogEntryCount_oid, 
					OID_LENGTH(saHpiDomainEventLogEntryCount_oid),
			                HANDLER_CAN_RONLY ));

        return SNMP_ERR_NOERROR;
}


/************************************************************/
/************************************************************/
/************************************************************/
/************************************************************/

/************************************************************
 * keep binary tree to find context by name
 */
static int saHpiDomainEventLogTable_cmp( const void *lhs, const void *rhs );

/************************************************************
 * compare two context pointers here. Return -1 if lhs < rhs,
 * 0 if lhs == rhs, and 1 if lhs > rhs.
 */
static int
saHpiDomainEventLogTable_cmp( const void *lhs, const void *rhs )
{
        saHpiDomainEventLogTable_context *context_l =
        (saHpiDomainEventLogTable_context *)lhs;
        saHpiDomainEventLogTable_context *context_r =
        (saHpiDomainEventLogTable_context *)rhs;

        /*
         * check primary key, then secondary. Add your own code if
         * there are more than 2 indexes
         */
        DEBUGMSGTL ((AGENT, "saHpiDomainEventLogTable_cmp, called\n"));

        /* check for NULL pointers */
        if (lhs == NULL || rhs == NULL ) {
                DEBUGMSGTL((AGENT,"saHpiDomainEventLogTable_cmp() NULL pointer ERROR\n" ));
                return 0;
        }
        /* CHECK FIRST INDEX,  saHpiDomainId */
        if ( context_l->index.oids[0] < context_r->index.oids[0])
                return -1;

        if ( context_l->index.oids[0] > context_r->index.oids[0])
                return 1;

        if ( context_l->index.oids[0] == context_r->index.oids[0]) {
                /* If saHpiDomainId index is equal sort by second index */
                /* CHECK SECOND INDEX,  saHpiDomainEventEntryId */
                if ( context_l->index.oids[1] < context_r->index.oids[1])
                        return -1;

                if ( context_l->index.oids[1] > context_r->index.oids[1])
                        return 1;

                if ( context_l->index.oids[1] == context_r->index.oids[1]) {
                        /* If saHpiDomainEventEntryId index is equal sort by third index */
                        /* CHECK THIRD INDEX,  saHpiEventSeverity */
                        if ( context_l->index.oids[2] < context_r->index.oids[2])
                                return -1;

                        if ( context_l->index.oids[2] > context_r->index.oids[2])
                                return 1;

                        if ( context_l->index.oids[2] == context_r->index.oids[2])
			        return 0;
		}
	}
	
	return 0;
}

/************************************************************
 * Initializes the saHpiDomainEventLogTable module
 */
void
init_saHpiDomainEventLogTable(void)
{
        
        DEBUGMSGTL ((AGENT, "init_saHpiDomainEventLogTable, called\n"));
		
	initialize_table_saHpiDomainEventLogTable();

        initialize_table_saHpiDomainEventLogEntryCountTotal();
        initialize_table_saHpiDomainEventLogEntryCount();
	
        domain_resource_pair_initialize(&initialized, &dr_table);
	
}

/************************************************************
 * the *_row_copy routine
 */
static int saHpiDomainEventLogTable_row_copy(saHpiDomainEventLogTable_context * dst,
                         saHpiDomainEventLogTable_context * src)
{
    if(!dst||!src)
        return 1;
        
    /*
     * copy index, if provided
     */
    if(dst->index.oids)
        free(dst->index.oids);
    if(snmp_clone_mem( (void*)&dst->index.oids, src->index.oids,
                           src->index.len * sizeof(oid) )) {
        dst->index.oids = NULL;
        return 1;
    }
    dst->index.len = src->index.len;
    

    /*
     * copy components into the context structure
     */
    /** TODO: add code for external index(s)! */
    dst->saHpiDomainEventLogEntryId = src->saHpiDomainEventLogEntryId;

    dst->saHpiDomainEventLogTimestamp = src->saHpiDomainEventLogTimestamp;

    dst->saHpiDomainEventLogType = src->saHpiDomainEventLogType;

    return 0;
}

#ifdef saHpiDomainEventLogTable_SET_HANDLING

/**
 * the *_extract_index routine
 *
 * This routine is called when a set request is received for an index
 * that was not found in the table container. Here, we parse the oid
 * in the the individual index components and copy those indexes to the
 * context. Then we make sure the indexes for the new row are valid.
 */
int
saHpiDomainEventLogTable_extract_index( saHpiDomainEventLogTable_context * ctx, netsnmp_index * hdr )
{
        /*
         * temporary local storage for extracting oid index
         *
         * extract index uses varbinds (netsnmp_variable_list) to parse
         * the index OID into the individual components for each index part.
         */
        /** TODO: add storage for external index(s)! */
        netsnmp_variable_list var_saHpiDomainId;
        netsnmp_variable_list var_saHpiDomainEventEntryId;
        netsnmp_variable_list var_saHpiEventSeverity;
        int err;
	
        DEBUGMSGTL ((AGENT, "saHpiDomainEventLogTable_extract_index, called\n"));	

        /*
         * copy index, if provided
         */
        if (hdr) {
                netsnmp_assert(ctx->index.oids == NULL);
                if (snmp_clone_mem( (void*)&ctx->index.oids, hdr->oids,
                                    hdr->len * sizeof(oid) )) {
                        return -1;
                }
                ctx->index.len = hdr->len;
        }

        /*
         * initialize variable that will hold each component of the index.
         * If there are multiple indexes for the table, the variable_lists
         * need to be linked together, in order.
         */
        /** TODO: add code for external index(s)! */	
        memset( &var_saHpiDomainId, 0x00, sizeof(var_saHpiDomainId) );
        var_saHpiDomainId.type = ASN_UNSIGNED; /* type hint for parse_oid_indexes */
        /** TODO: link this index to the next, or NULL for the last one */
        var_saHpiDomainId.next_variable = &var_saHpiDomainEventEntryId;

        memset( &var_saHpiDomainEventEntryId, 0x00, sizeof(var_saHpiDomainEventEntryId) );
        var_saHpiDomainEventEntryId.type = ASN_UNSIGNED; /* type hint for parse_oid_indexes */
        /** TODO: link this index to the next, or NULL for the last one */
        var_saHpiDomainEventEntryId.next_variable = &var_saHpiEventSeverity;

        memset( &var_saHpiEventSeverity, 0x00, sizeof(var_saHpiEventSeverity) );
        var_saHpiEventSeverity.type = ASN_INTEGER; /* type hint for parse_oid_indexes */
        /** TODO: link this index to the next, or NULL for the last one */
        var_saHpiEventSeverity.next_variable = NULL;

        /*
         * parse the oid into the individual index components
         */
        err = parse_oid_indexes( hdr->oids, hdr->len, &var_saHpiDomainId );
        if (err == SNMP_ERR_NOERROR) {
                /*
                 * copy index components into the context structure
                 */
                /** skipping external index saHpiDomainId */
   
                /** skipping external index saHpiDomainEventEntryId */
   
                /** skipping external index saHpiEventSeverity */

                err = saHpiDomainId_check_index(*var_saHpiDomainId.val.integer);
		err = saHpiDomainEventEntryId_check_index(*var_saHpiDomainEventEntryId.val.integer);
		err = saHpiEventSeverity_check_index(*var_saHpiEventSeverity.val.integer);   
        }

        /*
         * parsing may have allocated memory. free it.
         */
        snmp_reset_var_buffers( &var_saHpiDomainId );

        return err;
}

/************************************************************
 * the *_can_activate routine is called
 * when a row is changed to determine if all the values
 * set are consistent with the row's rules for a row status
 * of ACTIVE.
 *
 * return 1 if the row could be ACTIVE
 * return 0 if the row is not ready for the ACTIVE state
 */
int saHpiDomainEventLogTable_can_activate(saHpiDomainEventLogTable_context *undo_ctx,
                      saHpiDomainEventLogTable_context *row_ctx,
                      netsnmp_request_group * rg)
{
    /*
     * TODO: check for activation requirements here
     */


    /*
     * be optimistic.
     */
    return 1;
}

/************************************************************
 * the *_can_deactivate routine is called when a row that is
 * currently ACTIVE is set to a state other than ACTIVE. If
 * there are conditions in which a row should not be allowed
 * to transition out of the ACTIVE state (such as the row being
 * referred to by another row or table), check for them here.
 *
 * return 1 if the row can be set to a non-ACTIVE state
 * return 0 if the row must remain in the ACTIVE state
 */
int saHpiDomainEventLogTable_can_deactivate(saHpiDomainEventLogTable_context *undo_ctx,
                        saHpiDomainEventLogTable_context *row_ctx,
                        netsnmp_request_group * rg)
{
    /*
     * TODO: check for deactivation requirements here
     */
    return 1;
}

/************************************************************
 * the *_can_delete routine is called to determine if a row
 * can be deleted.
 *
 * return 1 if the row can be deleted
 * return 0 if the row cannot be deleted
 */
int saHpiDomainEventLogTable_can_delete(saHpiDomainEventLogTable_context *undo_ctx,
                    saHpiDomainEventLogTable_context *row_ctx,
                    netsnmp_request_group * rg)
{
    /*
     * probably shouldn't delete a row that we can't
     * deactivate.
     */
    if(saHpiDomainEventLogTable_can_deactivate(undo_ctx,row_ctx,rg) != 1)
        return 0;
    
    /*
     * TODO: check for other deletion requirements here
     */
    return 1;
}

#ifdef saHpiDomainEventLogTable_ROW_CREATION
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
 * returns a newly allocated saHpiDomainEventLogTable_context
 *   structure if the specified indexes are not illegal
 * returns NULL for errors or illegal index values.
 */
saHpiDomainEventLogTable_context *
saHpiDomainEventLogTable_create_row( netsnmp_index* hdr)
{
    saHpiDomainEventLogTable_context * ctx =
        SNMP_MALLOC_TYPEDEF(saHpiDomainEventLogTable_context);
    if(!ctx)
        return NULL;


        
    /*
     * TODO: check indexes, if necessary.
     */
    if(saHpiDomainEventLogTable_extract_index( ctx, hdr )) {
        free(ctx->index.oids);
        free(ctx);
        return NULL;
    }

    /* netsnmp_mutex_init(ctx->lock);
       netsnmp_mutex_lock(ctx->lock); */

    /*
     * TODO: initialize any default values here. This is also
     * first place you really should allocate any memory for
     * yourself to use.  If you allocated memory earlier,
     * make sure you free it for earlier error cases!
     */
    /**
    */
    
    domain_event_log_entry_count_total++;
    return ctx;
}
#endif

/************************************************************
 * the *_duplicate row routine
 */
saHpiDomainEventLogTable_context *
saHpiDomainEventLogTable_duplicate_row( saHpiDomainEventLogTable_context * row_ctx)
{
    saHpiDomainEventLogTable_context * dup;

    if(!row_ctx)
        return NULL;

    dup = SNMP_MALLOC_TYPEDEF(saHpiDomainEventLogTable_context);
    if(!dup)
        return NULL;
        
    if(saHpiDomainEventLogTable_row_copy(dup,row_ctx)) {
        free(dup);
        dup = NULL;
    }

    return dup;
}

/************************************************************
 * the *_delete_row method is called to delete a row.
 */
netsnmp_index * saHpiDomainEventLogTable_delete_row( saHpiDomainEventLogTable_context * ctx )
{
  /* netsnmp_mutex_destroy(ctx->lock); */

    if(ctx->index.oids)
        free(ctx->index.oids);

    /*
     * TODO: release any memory you allocated here...
     */

    /*
     * release header
     */
    free( ctx );

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
void saHpiDomainEventLogTable_set_reserve1( netsnmp_request_group *rg )
{
    saHpiDomainEventLogTable_context *row_ctx =
            (saHpiDomainEventLogTable_context *)rg->existing_row;
    saHpiDomainEventLogTable_context *undo_ctx =
            (saHpiDomainEventLogTable_context *)rg->undo_info;
    netsnmp_variable_list *var;
    netsnmp_request_group_item *current;
    int rc;


    /*
     * TODO: loop through columns, check syntax and lengths. For
     * columns which have no dependencies, you could also move
     * the value/range checking here to attempt to catch error
     * cases as early as possible.
     */
    for( current = rg->list; current; current = current->next ) {

        var = current->ri->requestvb;
        rc = SNMP_ERR_NOERROR;

        switch(current->tri->colnum) {

        default: /** We shouldn't get here */
            rc = SNMP_ERR_GENERR;
            snmp_log(LOG_ERR, "unknown column in "
                     "saHpiDomainEventLogTable_set_reserve1\n");
        }

        if (rc)
           netsnmp_set_mode_request_error(MODE_SET_BEGIN, current->ri, rc );
        rg->status = SNMP_MAX( rg->status, current->ri->status );
    }

    /*
     * done with all the columns. Could check row related
     * requirements here.
     */
}

void saHpiDomainEventLogTable_set_reserve2( netsnmp_request_group *rg )
{
    saHpiDomainEventLogTable_context *row_ctx = (saHpiDomainEventLogTable_context *)rg->existing_row;
    saHpiDomainEventLogTable_context *undo_ctx = (saHpiDomainEventLogTable_context *)rg->undo_info;
    netsnmp_request_group_item *current;
    netsnmp_variable_list *var;
    int rc;

    rg->rg_void = rg->list->ri;

    /*
     * TODO: loop through columns, check for valid
     * values and any range constraints.
     */
    for( current = rg->list; current; current = current->next ) {

        var = current->ri->requestvb;
        rc = SNMP_ERR_NOERROR;

        switch(current->tri->colnum) {

        default: /** We shouldn't get here */
            netsnmp_assert(0); /** why wasn't this caught in reserve1? */
        }

        if (rc)
           netsnmp_set_mode_request_error(MODE_SET_BEGIN, current->ri, rc);
    }

    /*
     * done with all the columns. Could check row related
     * requirements here.
     */
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
void saHpiDomainEventLogTable_set_action( netsnmp_request_group *rg )
{
    netsnmp_variable_list *var;
    saHpiDomainEventLogTable_context *row_ctx = (saHpiDomainEventLogTable_context *)rg->existing_row;
    saHpiDomainEventLogTable_context *undo_ctx = (saHpiDomainEventLogTable_context *)rg->undo_info;
    netsnmp_request_group_item *current;

    int            row_err = 0;

    /*
     * TODO: loop through columns, copy varbind values
     * to context structure for the row.
     */
    for( current = rg->list; current; current = current->next ) {

        var = current->ri->requestvb;

        switch(current->tri->colnum) {

        default: /** We shouldn't get here */
            netsnmp_assert(0); /** why wasn't this caught in reserve1? */
        }
    }

    /*
     * done with all the columns. Could check row related
     * requirements here.
     */
    if(row_err) {
        netsnmp_set_mode_request_error(MODE_SET_BEGIN,
                                       (netsnmp_request_info*)rg->rg_void,
                                       row_err);
        return;
    }

    /*
     * TODO: if you have dependencies on other tables, this would be
     * a good place to check those, too.
     */
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
void saHpiDomainEventLogTable_set_commit( netsnmp_request_group *rg )
{
    netsnmp_variable_list *var;
    saHpiDomainEventLogTable_context *row_ctx = (saHpiDomainEventLogTable_context *)rg->existing_row;
    saHpiDomainEventLogTable_context *undo_ctx = (saHpiDomainEventLogTable_context *)rg->undo_info;
    netsnmp_request_group_item *current;

    /*
     * loop through columns
     */
    for( current = rg->list; current; current = current->next ) {

        var = current->ri->requestvb;

        switch(current->tri->colnum) {

        default: /** We shouldn't get here */
            netsnmp_assert(0); /** why wasn't this caught in reserve1? */
        }
    }

    /*
     * done with all the columns. Could check row related
     * requirements here.
     */
}

/************************************************************
 * If either of the RESERVE calls fail, the write routines
 * are called again with the FREE action, to release any resources
 * that have been allocated. The agent will then return a failure
 * response to the requesting application.
 *
 * AFTER calling this routine, the agent will delete undo_info.
 */
void saHpiDomainEventLogTable_set_free( netsnmp_request_group *rg )
{
    netsnmp_variable_list *var;
    saHpiDomainEventLogTable_context *row_ctx = (saHpiDomainEventLogTable_context *)rg->existing_row;
    saHpiDomainEventLogTable_context *undo_ctx = (saHpiDomainEventLogTable_context *)rg->undo_info;
    netsnmp_request_group_item *current;

    /*
     * loop through columns
     */
    for( current = rg->list; current; current = current->next ) {

        var = current->ri->requestvb;

        switch(current->tri->colnum) {

        default: /** We shouldn't get here */
	        break;
            /** should have been logged in reserve1 */
        }
    }

    /*
     * done with all the columns. Could check row related
     * requirements here.
     */
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
void saHpiDomainEventLogTable_set_undo( netsnmp_request_group *rg )
{
    netsnmp_variable_list *var;
    saHpiDomainEventLogTable_context *row_ctx = (saHpiDomainEventLogTable_context *)rg->existing_row;
    saHpiDomainEventLogTable_context *undo_ctx = (saHpiDomainEventLogTable_context *)rg->undo_info;
    netsnmp_request_group_item *current;

    /*
     * loop through columns
     */
    for( current = rg->list; current; current = current->next ) {

        var = current->ri->requestvb;

        switch(current->tri->colnum) {

        default: /** We shouldn't get here */
            netsnmp_assert(0); /** why wasn't this caught in reserve1? */
        }
    }

    /*
     * done with all the columns. Could check row related
     * requirements here.
     */
}

#endif /** saHpiDomainEventLogTable_SET_HANDLING */


/************************************************************
 *
 * Initialize the saHpiDomainEventLogTable table by defining its contents and how it's structured
 */
void
initialize_table_saHpiDomainEventLogTable(void)
{
    netsnmp_table_registration_info *table_info;

    if(my_handler) {
        snmp_log(LOG_ERR, "initialize_table_saHpiDomainEventLogTable_handler called again\n");
        return;
    }

    memset(&cb, 0x00, sizeof(cb));

    /** create the table structure itself */
    table_info = SNMP_MALLOC_TYPEDEF(netsnmp_table_registration_info);

    /* if your table is read only, it's easiest to change the
       HANDLER_CAN_RWRITE definition below to HANDLER_CAN_RONLY */
    my_handler = netsnmp_create_handler_registration("saHpiDomainEventLogTable",
                                             netsnmp_table_array_helper_handler,
                                             saHpiDomainEventLogTable_oid,
                                             saHpiDomainEventLogTable_oid_len,
                                             HANDLER_CAN_RWRITE);
            
    if (!my_handler || !table_info) {
        snmp_log(LOG_ERR, "malloc failed in "
                 "initialize_table_saHpiDomainEventLogTable_handler\n");
        return; /** mallocs failed */
    }

    /***************************************************
     * Setting up the table's definition
     */
    /*
     * TODO: add any external indexes here.
     */
        /** TODO: add code for external index(s)! */

    /*
     * internal indexes
     */
        /** index: saHpiDomainId */
        netsnmp_table_helper_add_index(table_info, ASN_UNSIGNED);
        /** index: saHpiDomainEventEntryId */
        netsnmp_table_helper_add_index(table_info, ASN_UNSIGNED);
        /** index: saHpiEventSeverity */
        netsnmp_table_helper_add_index(table_info, ASN_INTEGER);

    table_info->min_column = saHpiDomainEventLogTable_COL_MIN;
    table_info->max_column = saHpiDomainEventLogTable_COL_MAX;

    /***************************************************
     * registering the table with the master agent
     */
    cb.get_value = saHpiDomainEventLogTable_get_value;
    cb.container = netsnmp_container_find("saHpiDomainEventLogTable_primary:"
                                          "saHpiDomainEventLogTable:"
                                          "table_container");
#ifdef saHpiDomainEventLogTable_IDX2
    netsnmp_container_add_index(cb.container,
                                netsnmp_container_find("saHpiDomainEventLogTable_secondary:"
                                                       "saHpiDomainEventLogTable:"
                                                       "table_container"));
    cb.container->next->compare = saHpiDomainEventLogTable_cmp;
#endif
#ifdef saHpiDomainEventLogTable_SET_HANDLING
    cb.can_set = 1;
#ifdef saHpiDomainEventLogTable_ROW_CREATION
    cb.create_row = (UserRowMethod*)saHpiDomainEventLogTable_create_row;
#endif
    cb.duplicate_row = (UserRowMethod*)saHpiDomainEventLogTable_duplicate_row;
    cb.delete_row = (UserRowMethod*)saHpiDomainEventLogTable_delete_row;
    cb.row_copy = (Netsnmp_User_Row_Operation *)saHpiDomainEventLogTable_row_copy;

    cb.can_activate = (Netsnmp_User_Row_Action *)saHpiDomainEventLogTable_can_activate;
    cb.can_deactivate = (Netsnmp_User_Row_Action *)saHpiDomainEventLogTable_can_deactivate;
    cb.can_delete = (Netsnmp_User_Row_Action *)saHpiDomainEventLogTable_can_delete;

    cb.set_reserve1 = saHpiDomainEventLogTable_set_reserve1;
    cb.set_reserve2 = saHpiDomainEventLogTable_set_reserve2;
    cb.set_action = saHpiDomainEventLogTable_set_action;
    cb.set_commit = saHpiDomainEventLogTable_set_commit;
    cb.set_free = saHpiDomainEventLogTable_set_free;
    cb.set_undo = saHpiDomainEventLogTable_set_undo;
#endif
    DEBUGMSGTL(("initialize_table_saHpiDomainEventLogTable",
                "Registering table saHpiDomainEventLogTable "
                "as a table array\n"));
    netsnmp_table_container_register(my_handler, table_info, &cb,
                                     cb.container, 1);
}

/************************************************************
 * saHpiDomainEventLogTable_get_value
 *
 * This routine is called for get requests to copy the data
 * from the context to the varbind for the request. If the
 * context has been properly maintained, you don't need to
 * change in code in this fuction.
 */
int saHpiDomainEventLogTable_get_value(
            netsnmp_request_info *request,
            netsnmp_index *item,
            netsnmp_table_request_info *table_info )
{
    netsnmp_variable_list *var = request->requestvb;
    saHpiDomainEventLogTable_context *context = (saHpiDomainEventLogTable_context *)item;

    switch(table_info->colnum) {

        case COLUMN_SAHPIDOMAINEVENTLOGENTRYID:
            /** SaHpiEntryId = ASN_UNSIGNED */
            snmp_set_var_typed_value(var, ASN_UNSIGNED,
                         (char*)&context->saHpiDomainEventLogEntryId,
                         sizeof(context->saHpiDomainEventLogEntryId) );
        break;
    
        case COLUMN_SAHPIDOMAINEVENTLOGTIMESTAMP:
            /** SaHpiTime = ASN_COUNTER64 */
            snmp_set_var_typed_value(var, ASN_COUNTER64,
                         (char*)&context->saHpiDomainEventLogTimestamp,
                         sizeof(context->saHpiDomainEventLogTimestamp) );
        break;
    
        case COLUMN_SAHPIDOMAINEVENTLOGTYPE:
            /** INTEGER = ASN_INTEGER */
            snmp_set_var_typed_value(var, ASN_INTEGER,
                         (char*)&context->saHpiDomainEventLogType,
                         sizeof(context->saHpiDomainEventLogType) );
        break;
    
    default: /** We shouldn't get here */
        snmp_log(LOG_ERR, "unknown column in "
                 "saHpiDomainEventLogTable_get_value\n");
        return SNMP_ERR_GENERR;
    }
    return SNMP_ERR_NOERROR;
}

/************************************************************
 * saHpiDomainEventLogTable_get_by_idx
 */
const saHpiDomainEventLogTable_context *
saHpiDomainEventLogTable_get_by_idx(netsnmp_index * hdr)
{
    return (const saHpiDomainEventLogTable_context *)
        CONTAINER_FIND(cb.container, hdr );
}


