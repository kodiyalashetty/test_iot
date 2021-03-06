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
 * WARNING! This file is auto-magically generated by rsa_str2event.pl 
 *          Do not change this file manually. Update script instead
 *******************************************************************/

#ifndef __RSA_STR2EVENT_H
#define __RSA_STR2EVENT_H

#define HPIDUP_STRING  "_HPIDUP"

#define NO_OVR  0x0000
#define OVR_SEV 0x0001
#define OVR_RID 0x0010

typedef struct {
        gchar *event;
	SaHpiSeverityT event_sev;
	unsigned short event_ovr;
        short          event_dup;
} Str2EventInfoT;

/* Global String 2 Event Hash Table */
extern GHashTable * rsa_str2event_hash;

int rsa_str2event_hash_init(void);
int rsa_str2event_hash_free(void);

#endif
