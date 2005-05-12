 /*      -*- linux-c -*-
 *
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
 *     Sean Dague <http://dague.net/sean>
 */

#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <syslog.h>
#include <SaHpi.h>
#include <oh_utils.h>

int main(int argc, char **argv)
{
        SaErrorT rc = SA_OK;
        SaHpiSessionIdT sid;
        
        rc = saHpiSessionOpen(SAHPI_UNSPECIFIED_DOMAIN_ID, &sid, NULL);
        rc = saHpiSubscribe(sid);
        rc = saHpiDiscover(sid);
        openlog("hpisyslog", LOG_PID, LOG_USER);
        while(1) {
                SaHpiTimeoutT timeout = SAHPI_TIMEOUT_IMMEDIATE;
                SaHpiEventT event;
                SaHpiRdrT rdr;
                SaHpiRptEntryT res;
                oh_big_textbuffer buffer;
                while(saHpiEventGet(sid, timeout, &event, &rdr, &res, NULL) == SA_OK) {
                        char tmp[OH_MAX_TEXT_BUFFER_LENGTH];
                        memset(tmp, '\0', OH_MAX_TEXT_BUFFER_LENGTH);
                        oh_init_bigtext(&buffer);
                        oh_build_event(&buffer, &event, 0);
                        strncpy(tmp, buffer.Data, buffer.DataLength);
                        syslog(3,"%s", tmp);
                }
                sleep(5);
        }
    
    
        return 0;
}
