/*
 *  Copyright (c) 2012 Pigeon Point Systems.
 *  All rights reserved.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  This
 * file and program are licensed under a BSD style license.  See
 * the Copying file included with this distribution for
 * full licensing terms.
 *
 * Authors:
 *     Anton Pak (Pigeon Point Systems)
 */


#ifndef __OHPI_UTILS_H__
#define __OHPI_UTILS_H__

#include <SaHpi.h>
#include <HpiEntry.h>

#include <string>


#define OPENHPI_DEFAULT_DAEMON_PORT 4743


/************************************************
 * External declarations of used oHpi API.
 * We do it to avoid oHpi.h inclusion which
 * requires Glib-2.0.
 ***********************************************/
extern "C"
{
    typedef struct {
            SaHpiDomainIdT   id;
            SaHpiTextBufferT host;
            SaHpiUint16T     port;
            SaHpiEntityPathT entity_root;
    } oHpiDomainEntryT;

    SaErrorT SAHPI_API oHpiDomainAdd (
         SAHPI_IN    const SaHpiTextBufferT *host,
         SAHPI_IN    SaHpiUint16T port,
         SAHPI_IN    const SaHpiEntityPathT *entity_root,
         SAHPI_OUT   SaHpiDomainIdT *domain_id );

    SaErrorT SAHPI_API oHpiDomainEntryGet (
         SAHPI_IN    SaHpiEntryIdT    EntryId,
         SAHPI_OUT   SaHpiEntryIdT    *NextEntryId,
         SAHPI_OUT   oHpiDomainEntryT *DomainEntry );
};


void MakeNameForOpenHpiDomain( const oHpiDomainEntryT& ode, std::wstring& txt );


#endif // __OHPI_UTILS_H__

