/*      -*- linux-c -*-
 *
 * (C) Copyright IBM Corp. 2004
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  This
 * file and program are licensed under a BSD style license.  See
 * the Copying file included with the OpenHPI distribution for
 * full licensing terms.
 */

/******************************************************************* 
 * WARNING! This file is auto-magically generated by bc_str2event.pl 
 *          Do not change this file manually. Update script instead
 *******************************************************************/

#ifndef __BC_STR2EVENT_H
#define __BC_STR2EVENT_H

typedef enum {
	NOOVR,
	OVR,
} BcSevOvrT;

typedef struct {
        gchar *event;
	SaHpiSeverityT event_sev;
	BcSevOvrT event_sev_ovr;
} Str2EventInfoT;

/* Global String 2 Event Hash Table */
GHashTable * str2event_hash;

int str2event_hash_init(void);
int str2event_hash_free(void);

#endif
