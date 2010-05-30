/*
 *  Copyright (c) 2010 Pigeon Point Systems.
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
 *     Sergey Ivushkin (Pigeon Point Systems)
 */


#include "CommonHpiSubProviderFUMI.h"
#include "HpiSubProvider.h"


/************************************************
 * Common stuff for FUMI* sub-providers
 ***********************************************/
void GetFwInstanceInfo( const wchar_t * name,
                        const SaHpiFumiFirmwareInstanceInfoT& fwii,
                        std::deque<HpiInfo>& info )
{
    if ( fwii.InstancePresent == SAHPI_FALSE ) {
        return;
    }
    Line( info, name, L"" );
    Line( info, L"  Identifier", fwii.Identifier );
    Line( info, L"  Description", fwii.Description );
    Line( info, L"  Firmware Build Date-Time", fwii.DateTime );
    FirmwareRevision fw( fwii.MajorVersion, fwii.MinorVersion, fwii.AuxVersion );
    Line( info, L"  Firmware Revision", fw );
}

