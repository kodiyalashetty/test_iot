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


#ifndef __HPI_ENTRY_H__
#define __HPI_ENTRY_H__

#include <string>

#include <SaHpi.h>


/************************************************
 * HpiEntry Types
 ***********************************************/
enum eHpiEntryType
{
    eHpiEntryUnknown = 0,
    eHpiEntryUp,
    eHpiEntryDomain,
    eHpiEntryDRT,
    eHpiEntryRPT,
    eHpiEntryDET,
    eHpiEntryLog,
    eHpiEntryDAT,
    eHpiEntryResource,
    eHpiEntryAlarm,
    eHpiEntryLogEntry,
    eHpiEntryEntity,
    eHpiEntryControl,
    eHpiEntrySensor,
    eHpiEntryIdr,
    eHpiEntryWatchdog,
    eHpiEntryAnnunciator,
    eHpiEntryDIMI,
    eHpiEntryFUMI,
    eHpiEntryHotSwap,
    eHpiEntryReset,
    eHpiEntryPower,
    eHpiEntryIdrArea,
    eHpiEntryAnnouncement,
    eHpiEntryDIMITest,
    eHpiEntryFUMIBank,
    eHpiEntryIdrField,
    eHpiEntryFUMIComponent,
    eHpiEntryFUMISource,
    eHpiEntryFUMISourceComponent,
    NumberOfHpiEntryTypes,
};


/************************************************
 * class HpiEntry
 ***********************************************/
struct HpiEntry
{
    explicit HpiEntry( eHpiEntryType _type,
                       SaHpiUint32T _id,
                       const std::wstring& _description )
        : type( _type ), id( _id ), description( _description )
    {
        // empty
    }


    // data
    eHpiEntryType type;
    SaHpiUint32T  id;
    std::wstring  description;
};


/************************************************
 * class HpiEntryShort
 ***********************************************/
struct HpiEntryShort
{
    explicit HpiEntryShort()
        : type( eHpiEntryUnknown ), id( 0 )
    {
        // empty
    }

    explicit HpiEntryShort( eHpiEntryType _type,
                            SaHpiUint32T _id )
        : type( _type ), id( _id )
    {
        // empty
    }

    explicit HpiEntryShort( const HpiEntry& entry )
        : type( entry.type ), id( entry.id )
    {
        // empty
    }


    // data
    eHpiEntryType type;
    SaHpiUint32T  id;
};


/************************************************
 * class HpiEntryCtx
 ***********************************************/
struct HpiEntryCtx
{
    HpiEntryCtx()
        : type( eHpiEntryUnknown )
    {
        // empty
    }


    // data
    eHpiEntryType         type;
    SaHpiDomainIdT        domain_id;
    SaHpiSessionIdT       session_id;
    SaHpiResourceIdT      resource_id;
    SaHpiInstrumentIdT    instrument_id;
    SaHpiEntityPathT      entity_path;
    SaHpiAlarmIdT         alarm_id;
    SaHpiEventLogEntryIdT log_entry_id;
    SaHpiEntryIdT         announcement_id;
    SaHpiEntryIdT         area_id;
    SaHpiDimiTestNumT     test_num;
    SaHpiBankNumT         bank_num;
    SaHpiEntryIdT         field_id;
    SaHpiUint32T          component_id;
    SaHpiUint32T          source_component_id;
};


#endif // __HPI_ENTRY_H__

