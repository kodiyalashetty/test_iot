/* -*- linux-c -*-
 * 
 * (C) Copyright IBM Corp. 2004
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  This
 * file and program are licensed under a BSD style license.  See
 * the Copying file included with the OpenHPI distribution for
 * full licensing terms.
 *
 * Author(s):
 *     Peter D Phan <pdphan@users.sourceforge.net>
 */


#include <snmp_bc_plugin.h>
#include <sahpimacros.h>
#include <tsetup.h>

int main(int argc, char **argv) 
{

	/* ************************
	 * Local variables
	 * ***********************/	 
	int testfail = 0;
	SaErrorT          err;
	SaErrorT expected_err;
	SaHpiResourceIdT  id;
        SaHpiSessionIdT sessionid;
        SaHpiRptEntryT rptentry;
	SaHpiRdrT	rdr;		 
	SaHpiCtrlNumT cid = 1;
	SaHpiCtrlModeT mode = SAHPI_CTRL_MODE_AUTO;
	SaHpiCtrlStateT state;
	SaHpiEntryIdT entryid;
	SaHpiEntryIdT nextentryid;
	SaHpiBoolT foundControl;			
	struct oh_handler_state l_handle;

	/* *************************************	 	 
	 * Find a resource with Control type rdr
	 * ************************************* */
	err = tsetup(&sessionid);
	if (err != SA_OK) {
		printf("Error! Can not open session for test environment\n");
		printf("       File=%s, Line=%d\n", __FILE__, __LINE__);
		return -1;
	}
	err = tfind_resource(&sessionid, SAHPI_CAPABILITY_CONTROL, SAHPI_FIRST_ENTRY, &rptentry, SAHPI_TRUE);
	if (err != SA_OK) {
		printf("Can not find a control resource for test environment\n");
		printf("       File=%s, Line=%d\n", __FILE__, __LINE__);
		err = tcleanup(&sessionid);
		return SA_OK;
	}
	
	id = rptentry.ResourceId;
	/************************** 
	 * Test: find a control RDR
	 **************************/
	entryid = SAHPI_FIRST_ENTRY;
	foundControl = SAHPI_FALSE;			
	do {
		err = saHpiRdrGet(sessionid,id,entryid,&nextentryid, &rdr);
		if (err == SA_OK)
		{
			if (rdr.RdrType == SAHPI_CTRL_RDR) 
			{
				foundControl = SAHPI_TRUE;
				break;
														
			}
			entryid = nextentryid;
		}
	} while ((err == SA_OK) && (entryid != SAHPI_LAST_ENTRY)) ;

	if (!foundControl) {
		dbg("Did not find desired resource for test\n");
		return(SA_OK);
	} else {
		cid = rdr.RdrTypeUnion.CtrlRec.Num; 
	}	

	/************************** 
	 * Test 1: Invalid Handle    
	 *************************/
	memset(&l_handle, 0, sizeof(struct oh_handler_state));

	expected_err = SA_ERR_HPI_INVALID_PARAMS;
	err = snmp_bc_set_control_state(NULL, id, cid, mode, &state);
	checkstatus(err, expected_err, testfail);
	
	/************************** 
	 * Test 2: Resource ID with no RPT
	 *************************/

	expected_err = SA_ERR_HPI_INVALID_RESOURCE;
	err = saHpiControlSet(sessionid, 5000, cid, mode, &state);
	checkstatus(err, expected_err, testfail);
	
	/************************** 
	 * Test 3: Control ID with no RDR 
	 *************************/
	expected_err = SA_ERR_HPI_NOT_PRESENT;
	err = saHpiControlSet(sessionid, id, 5000, mode, &state);
	checkstatus(err, expected_err, testfail);
	
	/************************** 
	 * Test 4: NULL state with AUTO mode
	 *************************/
	expected_err = SA_ERR_HPI_READ_ONLY;
	err = saHpiControlSet(sessionid, id, cid, mode, NULL);
	checkstatus(err, expected_err, testfail);
	
	/************************** 
	 * Test 5: NULL state with AUTO mode
	 *************************/
	expected_err = SA_ERR_HPI_INVALID_PARAMS;
	err = saHpiControlSet(sessionid, id, cid, SAHPI_CTRL_MODE_MANUAL, NULL);
	checkstatus(err, expected_err, testfail);
	
	/************************** 
	 * Test 6: Invalid Capability
	 *************************/	
	err = tfind_resource(&sessionid, SAHPI_CAPABILITY_CONTROL, SAHPI_FIRST_ENTRY, &rptentry, SAHPI_FALSE);
	if (err != SA_OK) {
		printf("Error! Can not find resources for test environment\n");
		printf("       File=%s, Line=%d\n", __FILE__, __LINE__);
		err = tcleanup(&sessionid);
		return SA_OK;
	}

	expected_err = SA_ERR_HPI_CAPABILITY;
	err = saHpiControlSet(sessionid, rptentry.ResourceId, cid, mode, &state);
	checkstatus(err, expected_err, testfail);

	/***************************
	 * Cleanup after all tests
	 ***************************/
	 err = tcleanup(&sessionid);
	 return testfail;

}

#include <tsetup.c>

