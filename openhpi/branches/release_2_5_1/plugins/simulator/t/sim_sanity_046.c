/*      -*- linux-c -*-
*
*(C) Copyright IBM Corp. 2005
*
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  This
* file and program are licensed under a BSD style license.  See
* the Copying file included with the OpenHPI distribution for
* full licensing terms.
*
* Authors:
*     W. david Ashley <dashley@us.ibm.com>
*/

#include <stdlib.h>
#include <string.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <SaHpi.h>
#include <oh_utils.h>
#include <../sim_injector_ext.h>

#include <errno.h>

/**
 * Run a series of sanity tests on the simulator
 * Return 0 on success, otherwise return -1
 **/


/**
 * This function is standalone so you can see how to inject events from a
 * completely diferent process than the one OpenHPI is running in.
 * Notice that no simulator plugin entry points are used in this function.
 **/

static int inject_event(char *plugin_name) {
    key_t ipckey;
    int msgqueid;
    SIM_MSG_QUEUE_BUF buf;
    size_t n = 0;  // size of the data in the msg buf
    char *txtptr = buf.mtext;
    int rc;

    /* get the queue */
    ipckey = ftok(".", SIM_MSG_QUEUE_KEY);
    msgqueid = msgget(ipckey, IPC_CREAT | S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP);
    
    if (msgqueid == -1) {
        int errsv = errno;
        
	if (errsv == EACCES) {
                printf("Error: On msgget. EACCES\n");
        } else if (errsv == EEXIST) {
                printf("Error: On msgget. EEXIST\n");
        } else if (errsv == ENOENT) {
                printf("Error: On msgget. ENOENT\n");
        } else if (errsv == ENOMEM) {
                printf("Error: On msgget. ENOMEM\n");
        } else if (errsv == ENOSPC) {
                printf("Error: On msgget. ENOSPC\n");
        } else {
                printf("Error: On msgget. Unknown errno\n");
        }
        
        return -1;
    }

    /* fill out the message */
    buf.mtype = SIM_MSG_SENSOR_EVENT;
    *txtptr = '\0';
    sprintf(txtptr, "%s=%s", SIM_MSG_HANDLER_NAME, plugin_name);
    n += strlen(txtptr) + 1;
    txtptr = buf.mtext + n;
    if (n > SIM_MSG_QUEUE_BUFSIZE) {
	printf("Error: On message size 1\n");
        return -1;
    }
    sprintf(txtptr, "%s=%d", SIM_MSG_RESOURCE_ID, 1);
    n += strlen(txtptr) + 1;
    txtptr = buf.mtext + n;
    if (n > SIM_MSG_QUEUE_BUFSIZE) {
	printf("Error: On message size 2\n");
        return -1;
    }
    sprintf(txtptr, "%s=%d", SIM_MSG_EVENT_SEVERITY, SAHPI_CRITICAL);
    n += strlen(txtptr) + 1;
    txtptr = buf.mtext + n;
    if (n > SIM_MSG_QUEUE_BUFSIZE) {
	printf("Error: On message size 3\n");
        return -1;
    }
    sprintf(txtptr, "%s=%d", SIM_MSG_SENSOR_NUM, 1);
    n += strlen(txtptr) + 1;
    txtptr = buf.mtext + n;
    if (n > SIM_MSG_QUEUE_BUFSIZE) {
	printf("Error: On message size 4\n");
        return -1;
    }
    sprintf(txtptr, "%s=%d", SIM_MSG_SENSOR_TYPE, SAHPI_TEMPERATURE);
    n += strlen(txtptr) + 1;
    txtptr = buf.mtext + n;
    if (n > SIM_MSG_QUEUE_BUFSIZE) {
	printf("Error: On message size 5\n");
        return -1;
    }
    sprintf(txtptr, "%s=%d", SIM_MSG_SENSOR_EVENT_CATEGORY, SAHPI_EC_THRESHOLD);
    n += strlen(txtptr) + 1;
    txtptr = buf.mtext + n;
    if (n > SIM_MSG_QUEUE_BUFSIZE) {
	printf("Error: On message size 6\n");
        return -1;
    }
    sprintf(txtptr, "%s=%d", SIM_MSG_SENSOR_ASSERTION, SAHPI_TRUE);
    n += strlen(txtptr) + 1;
    txtptr = buf.mtext + n;
    if (n > SIM_MSG_QUEUE_BUFSIZE) {
	printf("Error: On message size 7\n");
        return -1;
    }
    sprintf(txtptr, "%s=%d", SIM_MSG_SENSOR_EVENT_STATE, SAHPI_ES_UPPER_CRIT);
    n += strlen(txtptr) + 1;
    txtptr = buf.mtext + n;
    if (n > SIM_MSG_QUEUE_BUFSIZE) {
	printf("Error: On message size 8\n");
        return -1;
    }
    sprintf(txtptr, "%s=%d", SIM_MSG_SENSOR_OPTIONAL_DATA, SAHPI_SOD_TRIGGER_READING);
    n += strlen(txtptr) + 1;
    txtptr = buf.mtext + n;
    if (n > SIM_MSG_QUEUE_BUFSIZE) {
	printf("Error: On message size 9\n");
        return -1;
    }
    sprintf(txtptr, "%s=%d", SIM_MSG_SENSOR_TRIGGER_READING_SUPPORTED, SAHPI_TRUE);
    n += strlen(txtptr) + 1;
    txtptr = buf.mtext + n;
    if (n > SIM_MSG_QUEUE_BUFSIZE) {
	printf("Error: On message size 10\n");
        return -1;
    }
    sprintf(txtptr, "%s=%d", SIM_MSG_SENSOR_TRIGGER_READING_TYPE, SAHPI_SENSOR_READING_TYPE_INT64);
    n += strlen(txtptr) + 1;
    txtptr = buf.mtext + n;
    if (n > SIM_MSG_QUEUE_BUFSIZE) {
	printf("Error: On message size 11\n");
        return -1;
    }
    sprintf(txtptr, "%s=%d", SIM_MSG_SENSOR_TRIGGER_READING, 21);
    n += strlen(txtptr) + 1;
    txtptr = buf.mtext + n;
    if (n > SIM_MSG_QUEUE_BUFSIZE) {
	printf("Error: On message size 12\n");
        return -1;
    }
    *txtptr = '\0'; // terminate buf with a zero-length string
    n++;

    /* send the msg */
    rc = msgsnd(msgqueid, &buf, n, 0);
    if (rc) {
	printf("Error: On message send\n");
        return -1;
    }

    return 0;
 }


int main(int argc, char **argv)
{
    SaHpiSessionIdT sid = 0;
    SaErrorT rc = SA_OK;
    int retc;

    rc = saHpiSessionOpen(SAHPI_UNSPECIFIED_DOMAIN_ID, &sid, NULL);
    if(rc != SA_OK) {
	printf("Error: On Session Open\n");
	return -1;
    }

    rc = saHpiDiscover(sid);
    if (rc != SA_OK) {
	printf("Error: On Discover\n");
	return -1;
    }

    /* inject an event */
    retc = inject_event("simulator");
    if (retc != 0) {
	printf("Error: On Inject\n");
        return -1;
    }

    /* sleep so the msg thread gets a chance to process the msg */
    g_usleep(100000);

    saHpiSessionClose(sid);

    return 0;
}
