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
 * Authors:
 *     Renier Morales <renierm@users.sf.net>
 */

#include <glib.h>

#include <SaHpi.h>
#include <oh_utils.h>

/**
 * main: Get 10 new unique ids. Remove two. Look up removed ids by ep.
 * Passes if lookups don't find anything,
 * otherwise fails.
 *
 * Return value: 0 on success, 1 on failure
 **/
int main(int argc, char **argv)
{
	SaHpiEntityPathT ep;
	guint id[10], i;

	if (oh_uid_initialize())
		return 1;

	oh_init_ep(&ep);

        for (i = 0; i < 10; i++) {
                ep.Entry[0].EntityLocation = i;
                id[i] = oh_uid_from_entity_path(&ep);
        }

        if (oh_uid_remove(id[9]))
                return 1;

        if (oh_uid_remove(id[4]))
                return 1;

        ep.Entry[0].EntityLocation = 9;
        if (oh_uid_lookup(&ep))
                return 1;

        ep.Entry[0].EntityLocation = 4;
        if (oh_uid_lookup(&ep))
                return 1;

	return 0;
}
