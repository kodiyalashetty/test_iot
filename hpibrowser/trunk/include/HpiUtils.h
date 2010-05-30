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


#ifndef __HPI_UTILS_H__
#define __HPI_UTILS_H__

#include <SaHpi.h>
#include <SaHpiXtca.h>
#include <HpiEntry.h>

#include <string>


static const SaHpiBankNumT SAHPI_LOGICAL_BANK_NUM = 0;


eHpiEntryType RdrType2EntryType( SaHpiRdrTypeT rdr_type );

SaHpiRdrTypeT EntryType2RdrType( eHpiEntryType entry_type );

SaHpiInstrumentIdT GetInstrumentId( const SaHpiRdrT& rdr );

bool SubstructHpiEntityPath( const SaHpiEntityPathT& minuend_ep,
                             const SaHpiEntityPathT& subtrahend_ep,
                             SaHpiEntityPathT& result_ep );

void MakeMainFwInstanceInfo( const SaHpiFumiBankInfoT& bi,
                             SaHpiFumiFirmwareInstanceInfoT& main_fwii );


/***********************************************************
 * Formatting
 **********************************************************/

/*****************************************************
 * HPI basic type convertors
 ****************************************************/
enum UI8_Fmt
{
    UI8_Dec,
    UI8_Hex,
    UI8_SaHpiBool,
    UI8_SaHpiEventCategory,
    UI8_SaHpiSensorRangeFlags,
    UI8_SaHpiSensorThdMask,
    UI8_SaHpiTxtLineNum,
    UI8_SaHpiWatchdogExpFlags,
    UI8_SaHpiDimiTestPercentCompleted,
    UI8_SaHpiBankNum,
    UI8_SaHpiSensorOptionalData,
    UI8_SaHpiSensorEnableOptData,
};

enum UI16_Fmt
{
    UI16_Dec,
    UI16_Hex,
    UI16_SaHpiEventState,
};

enum I32_Fmt
{
    I32_Dec,
    I32_SaError,
    I32_SaHpiCtrlStateAnalog,
};

enum UI32_Fmt
{
    UI32_Dec,
    UI32_Hex,
    UI32_SaHpiManufacturerId,
    UI32_SaHpiVersion,
    UI32_SaHpiDomainId,
    UI32_SaHpiSessionId,
    UI32_SaHpiResourceId,
    UI32_SaHpiEntryId,
    UI32_SaHpiInstrumentId,
    UI32_SaHpiSensorNum,
    UI32_SaHpiCtrlNum,
    UI32_SaHpiIdrId,
    UI32_SaHpiWatchdogNum,
    UI32_SaHpiAnnunciatorNum,
    UI32_SaHpiDimiNum,
    UI32_SaHpiFumiNum,
    UI32_SaHpiCtrlStateDiscrete,
    UI32_SaHpiDimiTestCapability,
    UI32_SaHpiDimiTestNum,
    UI32_SaHpiFumiLogicalBankStateFlags,
    UI32_SaHpiFumiProtocol,
    UI32_SaHpiFumiCapability,
    UI32_SaHpiEvtQueueStatus,
    UI32_SaHpiLoadNumber,
    UI32_SaHpiCapabilities,
    UI32_SaHpiHsCapabilities,
    UI32_SaHpiDomainCapabilities,
    UI32_SaHpiAlarmId,
    UI32_SaHpiEventLogCapabilities,
    UI32_SaHpiEventLogEntryId,

    // Not typedef but need special formating
    UI32_DatUserAlarmLimit,
    UI32_ConditionDomainId,
    UI32_AnnunciatorMaxConditions,
};

enum I64_Fmt
{
    I64_Dec,
    I64_SaHpiTime,
    I64_SaHpiTimeout,
};

enum UI64_Fmt
{
    UI64_Dec,
};

enum F64_Fmt
{
    F64_FixedPoint,
    F64_FloatingPoint,
};

void ToTxt( SaHpiUint8T x, std::wstring& txt, UI8_Fmt fmt );
void ToTxt( SaHpiUint16T x, std::wstring& txt, UI16_Fmt fmt );
void ToTxt( SaHpiInt32T x, std::wstring& txt, I32_Fmt fmt );
void ToTxt( SaHpiUint32T x, std::wstring& txt, UI32_Fmt fmt );
void ToTxt( SaHpiInt64T x, std::wstring& txt, I64_Fmt fmt );
void ToTxt( SaHpiUint64T x, std::wstring& txt, UI64_Fmt fmt );
void ToTxt( SaHpiFloat64T x, std::wstring& txt, F64_Fmt fmt );
void ToTxt( const SaHpiUint8T * binary, SaHpiUint16T len, std::wstring& txt );

/*****************************************************
 * HPI enum convertors
 ****************************************************/
void ToTxt( SaHpiLanguageT x, std::wstring& txt );
void ToTxt( SaHpiTextTypeT x, std::wstring& txt );
void ToTxt( SaHpiEntityTypeT x, std::wstring& txt );
void ToTxt( SaHpiSensorTypeT x, std::wstring& txt );
void ToTxt( SaHpiSensorReadingTypeT x, std::wstring& txt );
void ToTxt( SaHpiSensorEventMaskActionT x, std::wstring& txt );
void ToTxt( SaHpiSensorUnitsT x, std::wstring& txt );
void ToTxt( SaHpiSensorModUnitUseT x, std::wstring& txt );
void ToTxt( SaHpiSensorEventCtrlT x, std::wstring& txt );
void ToTxt( SaHpiCtrlTypeT x, std::wstring& txt );
void ToTxt( SaHpiCtrlStateDigitalT x, std::wstring& txt );
void ToTxt( SaHpiCtrlModeT x, std::wstring& txt );
void ToTxt( SaHpiCtrlOutputTypeT x, std::wstring& txt );
void ToTxt( SaHpiIdrAreaTypeT x, std::wstring& txt );
void ToTxt( SaHpiIdrFieldTypeT x, std::wstring& txt );
void ToTxt( SaHpiWatchdogActionT x, std::wstring& txt );
void ToTxt( SaHpiWatchdogActionEventT x, std::wstring& txt );
void ToTxt( SaHpiWatchdogPretimerInterruptT x, std::wstring& txt );
void ToTxt( SaHpiWatchdogTimerUseT x, std::wstring& txt );
void ToTxt( SaHpiDimiTestServiceImpactT x, std::wstring& txt );
void ToTxt( SaHpiDimiTestRunStatusT x, std::wstring& txt );
void ToTxt( SaHpiDimiTestErrCodeT x, std::wstring& txt );
void ToTxt( SaHpiDimiTestParamTypeT x, std::wstring& txt );
void ToTxt( SaHpiDimiReadyT x, std::wstring& txt );
void ToTxt( SaHpiFumiSpecInfoTypeT x, std::wstring& txt );
void ToTxt( SaHpiFumiSafDefinedSpecIdT x, std::wstring& txt );
void ToTxt( SaHpiFumiServiceImpactT x, std::wstring& txt );
void ToTxt( SaHpiFumiSourceStatusT x, std::wstring& txt );
void ToTxt( SaHpiFumiBankStateT x, std::wstring& txt );
void ToTxt( SaHpiFumiUpgradeStatusT x, std::wstring& txt );
void ToTxt( SaHpiHsIndicatorStateT x, std::wstring& txt );
void ToTxt( SaHpiHsActionT x, std::wstring& txt );
void ToTxt( SaHpiHsStateT x, std::wstring& txt );
void ToTxt( SaHpiHsCauseOfStateChangeT x, std::wstring& txt );
void ToTxt( SaHpiSeverityT x, std::wstring& txt );
void ToTxt( SaHpiResourceEventTypeT x, std::wstring& txt );
void ToTxt( SaHpiDomainEventTypeT x, std::wstring& txt );
void ToTxt( SaHpiSwEventTypeT x, std::wstring& txt );
void ToTxt( SaHpiEventTypeT x, std::wstring& txt );
void ToTxt( SaHpiStatusCondTypeT x, std::wstring& txt );
void ToTxt( SaHpiAnnunciatorModeT x, std::wstring& txt );
void ToTxt( SaHpiAnnunciatorTypeT x, std::wstring& txt );
void ToTxt( SaHpiRdrTypeT x, std::wstring& txt );
void ToTxt( SaHpiParmActionT x, std::wstring& txt );
void ToTxt( SaHpiResetActionT x, std::wstring& txt );
void ToTxt( SaHpiPowerStateT x, std::wstring& txt );
void ToTxt( SaHpiEventLogOverflowActionT x, std::wstring& txt );


/*****************************************************
 * HPI complex type convertors
 ****************************************************/
void ToTxt( const SaHpiTextBufferT& tb, std::wstring& txt );
void ToTxt( const SaHpiGuidT& guid, std::wstring& txt );
void ToTxt( const SaHpiEntityPathT& ep, std::wstring& txt );
void ToTxt( const SaHpiNameT& name, std::wstring& txt );


struct FirmwareRevision
{
    explicit FirmwareRevision( SaHpiUint32T _MajorVersion,
                               SaHpiUint32T _MinorVersion,
                               SaHpiUint32T _AuxVersion );

    SaHpiUint32T MajorVersion;
    SaHpiUint32T MinorVersion;
    SaHpiUint32T AuxVersion;
};

void ToTxt( const FirmwareRevision& fw, std::wstring& txt );

void ToTxt( const SaHpiSensorReadingT& sr, std::wstring& txt );


/*****************************************************
 * Making HPI entry name
 ****************************************************/
void MakeNameForUnknown( std::wstring& txt );
void MakeNameForUp( std::wstring& txt );
void MakeNameForDomain( SaHpiDomainIdT did, std::wstring& txt );
void MakeNameForDRT( std::wstring& txt );
void MakeNameForRPT( std::wstring& txt );
void MakeNameForDET( std::wstring& txt );
void MakeNameForLog( SaHpiResourceIdT rid, std::wstring& txt );
void MakeNameForDAT( std::wstring& txt );
void MakeNameForResource( const SaHpiRptEntryT& rpte, std::wstring& txt );
void MakeShortNameForResource( SaHpiResourceIdT rid, std::wstring& txt );
void MakeNameForAlarm( const SaHpiAlarmT& a, std::wstring& txt );
void MakeShortNameForAlarm( const SaHpiAlarmIdT& aid, std::wstring& txt );
void MakeNameForLogEntry( const SaHpiEventLogEntryT& elentry, std::wstring& txt );
void MakeShortNameForLogEntry( SaHpiEventLogEntryIdT eid, std::wstring& txt );
void MakeNameForEntity( const SaHpiEntityPathT& ep, std::wstring& txt );
void MakeShortNameForEntity( std::wstring& txt );
void MakeNameForInstrument( const SaHpiRdrT& rdr, std::wstring& txt );
void MakeShortNameForInstrument( SaHpiRdrTypeT type, SaHpiInstrumentIdT id, std::wstring& txt );
void MakeNameForHotSwap( std::wstring& txt );
void MakeNameForReset( std::wstring& txt );
void MakeNameForPower( std::wstring& txt );
void MakeNameForIdrArea( const SaHpiIdrAreaHeaderT& ahdr, std::wstring& txt );
void MakeShortNameForIdrArea( SaHpiEntryIdT aid, std::wstring& txt );
void MakeNameForAnnouncement( const SaHpiAnnouncementT& a, std::wstring& txt );
void MakeShortNameForAnnouncement( const SaHpiEntryIdT& aid, std::wstring& txt );
void MakeNameForDIMITest( SaHpiDimiTestNumT tnum, const SaHpiDimiTestT& dti, std::wstring& txt );
void MakeShortNameForDIMITest( SaHpiDimiTestNumT tnum, std::wstring& txt );
void MakeNameForFUMIBank( SaHpiBankNumT bnum, std::wstring& txt );
void MakeNameForIdrField( const SaHpiIdrFieldT& f, std::wstring& txt );
void MakeShortNameForIdrField( SaHpiEntryIdT fid, std::wstring& txt );
void MakeNameForFUMIComponent( const SaHpiFumiComponentInfoT& ci, std::wstring& txt );
void MakeShortNameForFUMIComponent( SaHpiUint32T cid, std::wstring& txt );
void MakeNameForFUMISource( const SaHpiFumiSourceInfoT& si, std::wstring& txt );
void MakeShortNameForFUMISource( std::wstring& txt );
void MakeNameForFUMISourceComponent( const SaHpiFumiComponentInfoT& ci, std::wstring& txt );
void MakeShortNameForFUMISourceComponent( SaHpiUint32T cid, std::wstring& txt );


#endif // __HPI_UTILS_H__

