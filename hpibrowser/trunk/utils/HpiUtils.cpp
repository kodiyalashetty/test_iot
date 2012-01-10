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


#include <ctime>
#include <string.h>

#include <HpiUtils.h>


eHpiEntryType RdrType2EntryType( SaHpiRdrTypeT rdr_type )
{
    switch ( rdr_type ) {
        case SAHPI_CTRL_RDR:
            return eHpiEntryControl;
        case SAHPI_SENSOR_RDR:
            return eHpiEntrySensor;
        case SAHPI_INVENTORY_RDR:
            return eHpiEntryIdr;
        case SAHPI_WATCHDOG_RDR:
            return eHpiEntryWatchdog;
        case SAHPI_ANNUNCIATOR_RDR:
            return eHpiEntryAnnunciator;
        case SAHPI_DIMI_RDR:
            return eHpiEntryDIMI;
        case SAHPI_FUMI_RDR:
            return eHpiEntryFUMI;
        default:
            return eHpiEntryUnknown;
    }
}

SaHpiRdrTypeT EntryType2RdrType( eHpiEntryType entry_type )
{
    switch ( entry_type ) {
        case eHpiEntryControl:
            return SAHPI_CTRL_RDR;
        case eHpiEntrySensor:
            return SAHPI_SENSOR_RDR;
        case eHpiEntryIdr:
            return SAHPI_INVENTORY_RDR;
        case eHpiEntryWatchdog:
            return SAHPI_WATCHDOG_RDR;
        case eHpiEntryAnnunciator:
            return SAHPI_ANNUNCIATOR_RDR;
        case eHpiEntryDIMI:
            return SAHPI_DIMI_RDR;
        case eHpiEntryFUMI:
            return SAHPI_FUMI_RDR;
        default:
            return SAHPI_NO_RECORD;
    }
}

SaHpiInstrumentIdT GetInstrumentId( const SaHpiRdrT& rdr )
{
    switch ( rdr.RdrType ) {
        case SAHPI_CTRL_RDR:
            return rdr.RdrTypeUnion.CtrlRec.Num;
        case SAHPI_SENSOR_RDR:
            return rdr.RdrTypeUnion.SensorRec.Num;
        case SAHPI_INVENTORY_RDR:
            return rdr.RdrTypeUnion.InventoryRec.IdrId;
        case SAHPI_WATCHDOG_RDR:
            return rdr.RdrTypeUnion.WatchdogRec.WatchdogNum;
        case SAHPI_ANNUNCIATOR_RDR:
            return rdr.RdrTypeUnion.AnnunciatorRec.AnnunciatorNum;
        case SAHPI_DIMI_RDR:
            return rdr.RdrTypeUnion.DimiRec.DimiNum;
        case SAHPI_FUMI_RDR:
            return rdr.RdrTypeUnion.FumiRec.Num;
        default:
            return SAHPI_ENTRY_UNSPECIFIED;
    }
}

static SaHpiUint8T GetHpiEntityPathLength( const SaHpiEntityPathT& ep )
{
    SaHpiUint8T i;
    for ( i = 0; i < SAHPI_MAX_ENTITY_PATH; ++i ) {
        if (
             ( ep.Entry[i].EntityType == SAHPI_ENT_ROOT ) &&
             ( ep.Entry[i].EntityLocation == 0 )
           )
        {
            break;
        }
    }
    return i;
}

static inline bool CmpHpiEntities( const SaHpiEntityT& e1, const SaHpiEntityT& e2 )
{
    return ( e1.EntityType == e2.EntityType ) && ( e1.EntityLocation == e2.EntityLocation );
}

bool SubstructHpiEntityPath( const SaHpiEntityPathT& minuend_ep,
                             const SaHpiEntityPathT& subtrahend_ep,
                             SaHpiEntityPathT& result_ep )
{
    SaHpiUint8T minuend_ep_len = GetHpiEntityPathLength( minuend_ep );
    SaHpiUint8T subtrahend_ep_len = GetHpiEntityPathLength( subtrahend_ep );

    if ( minuend_ep_len < subtrahend_ep_len ) {
        return false;
    }

    SaHpiUint8T result_ep_len = minuend_ep_len - subtrahend_ep_len;
    for ( SaHpiUint8T i = 0; i < subtrahend_ep_len; ++i ) {
        bool eq = CmpHpiEntities( minuend_ep.Entry[result_ep_len + i],
                                  subtrahend_ep.Entry[i] );
        if ( !eq ) {
            return false;
        }
    }

    for ( SaHpiUint8T i = 0; i < result_ep_len; ++i ) {
        result_ep.Entry[i] = minuend_ep.Entry[i];
    }
    result_ep.Entry[result_ep_len].EntityType     = SAHPI_ENT_ROOT;
    result_ep.Entry[result_ep_len].EntityLocation = 0;

    return true;
}

void MakeMainFwInstanceInfo( const SaHpiFumiBankInfoT& bi,
                             SaHpiFumiFirmwareInstanceInfoT& main_fwii )
{
    main_fwii.InstancePresent = SAHPI_TRUE;
    main_fwii.Identifier      = bi.Identifier;
    main_fwii.Description     = bi.Description;
    main_fwii.DateTime        = bi.DateTime;
    main_fwii.MajorVersion    = bi.MajorVersion;
    main_fwii.MinorVersion    = bi.MinorVersion;
    main_fwii.AuxVersion      = bi.AuxVersion;
}


/***********************************************************
 * Formatting
 **********************************************************/


/*****************************************************
 * helpers for HPI basic type convertors
 ****************************************************/
static std::wstring txt_unknown( L"???" );


static void SaHpiBoolToTxt( SaHpiBoolT x, std::wstring& txt )
{
    txt = ( x == SAHPI_FALSE ) ? L"FALSE" : L"TRUE";
}

static void SaHpiTime2String( SaHpiTimeT t, std::wstring& txt )
{
    if ( t > SAHPI_TIME_MAX_RELATIVE ) {
        wchar_t buf[128];
        time_t tt = (time_t)( t / 1000000000LL );
        struct tm tm;
#ifndef _WIN32
        localtime_r( &tt, &tm);
#else /* _WIN32 */
        localtime_s( &tm, &tt );
#endif /* _WIN32 */
        wcsftime( buf, sizeof(buf) / sizeof(wchar_t), L"%Y-%m-%d %H:%M:%S", &tm );
        txt = buf;
    } else if ( t == SAHPI_TIME_UNSPECIFIED ) {
        txt = L"Unspecified";
    } else if ( t > SAHPI_TIME_UNSPECIFIED ) {
        txt = L"Invalid";
    } else {
        wchar_t buf[128];
        time_t tt = (time_t)( t / 1000000000LL );
        struct tm tm;
#ifndef _WIN32
        localtime_r( &tt, &tm);
#else /* _WIN32 */
        localtime_s( &tm, &tt );
#endif /* _WIN32 */
        wcsftime( buf, sizeof(buf) / sizeof(wchar_t), L"%Y-%m-%d %H:%M:%S (Relative)", &tm );
        txt = buf;
    }
}

static void SaHpiTimeout2String( SaHpiTimeoutT t, std::wstring& txt )
{
    if ( t == SAHPI_TIMEOUT_IMMEDIATE ) {
        txt = L"IMMEDIATE";
    } else if ( t == SAHPI_TIMEOUT_BLOCK ) {
        txt = L"BLOCK";
    } else {
        ToTxt( t, txt, I64_Dec );
    }
}

static void SaHpiEventCategoryToTxt( SaHpiEventCategoryT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_EC_UNSPECIFIED:
            txt = L"UNSPECIFIED";
            break;
        case SAHPI_EC_THRESHOLD:
            txt = L"THRESHOLD";
            break;
        case SAHPI_EC_USAGE:
            txt = L"USAGE";
            break;
        case SAHPI_EC_STATE:
            txt = L"STATE";
            break;
        case SAHPI_EC_PRED_FAIL:
            txt = L"PRED_FAIL";
            break;
        case SAHPI_EC_LIMIT:
            txt = L"LIMIT";
            break;
        case SAHPI_EC_PERFORMANCE:
            txt = L"PERFORMANCE";
            break;
        case SAHPI_EC_SEVERITY:
            txt = L"SEVERITY";
            break;
        case SAHPI_EC_PRESENCE:
            txt = L"PRESENCE";
            break;
        case SAHPI_EC_ENABLE:
            txt = L"ENABLE";
            break;
        case SAHPI_EC_AVAILABILITY:
            txt = L"AVAILABILITY";
            break;
        case SAHPI_EC_REDUNDANCY:
            txt = L"REDUNDANCY";
            break;
        case SAHPI_EC_SENSOR_SPECIFIC:
            txt = L"SENSOR_SPECIFIC";
            break;
        case SAHPI_EC_GENERIC:
            txt = L"GENERIC";
            break;
        default:
            txt = txt_unknown;
    }
}

static void SaHpiDimiTestPercentCompletedToTxt( SaHpiDimiTestPercentCompletedT x, std::wstring& txt )
{
    if ( x != 0xff ) {
        ToTxt( x, txt, UI8_Dec );
    } else {
        txt = L"Unspecified";
    }
}

static void SaHpiBankNumToTxt( SaHpiBankNumT x, std::wstring& txt )
{
    ToTxt( x, txt, UI8_Dec );
    if ( x == SAHPI_LOGICAL_BANK_NUM ) {
        txt += L" (Logical)";
    }
}

static void SaErrorToTxt( SaErrorT x, std::wstring& txt )
{
    switch ( x ) {
        case SA_ERR_HPI_ERROR:
            txt = L"ERROR";
            break;
        case SA_ERR_HPI_UNSUPPORTED_API:
            txt = L"UNSUPPORTED_API";
            break;
        case SA_ERR_HPI_BUSY:
            txt = L"BUSY";
            break;
        case SA_ERR_HPI_INTERNAL_ERROR:
            txt = L"INTERNAL_ERROR";
            break;
        case SA_ERR_HPI_INVALID_CMD:
            txt = L"INVALID_CMD";
            break;
        case SA_ERR_HPI_TIMEOUT:
            txt = L"TIMEOUT";
            break;
        case SA_ERR_HPI_OUT_OF_SPACE:
            txt = L"OUT_OF_SPACE";
            break;
        case SA_ERR_HPI_OUT_OF_MEMORY:
            txt = L"OUT_OF_MEMORY";
            break;
        case SA_ERR_HPI_INVALID_PARAMS:
            txt = L"INVALID_PARAMS";
            break;
        case SA_ERR_HPI_INVALID_DATA:
            txt = L"INVALID_DATA";
            break;
        case SA_ERR_HPI_NOT_PRESENT:
            txt = L"NOT_PRESENT";
            break;
        case SA_ERR_HPI_NO_RESPONSE:
            txt = L"NO_RESPONSE";
            break;
        case SA_ERR_HPI_DUPLICATE:
            txt = L"DUPLICATE";
            break;
        case SA_ERR_HPI_INVALID_SESSION:
            txt = L"INVALID_SESSION";
            break;
        case SA_ERR_HPI_INVALID_DOMAIN:
            txt = L"INVALID_DOMAIN";
            break;
        case SA_ERR_HPI_INVALID_RESOURCE:
            txt = L"INVALID_RESOURCE";
            break;
        case SA_ERR_HPI_INVALID_REQUEST:
            txt = L"INVALID_REQUEST";
            break;
        case SA_ERR_HPI_ENTITY_NOT_PRESENT:
            txt = L"ENTITY_NOT_PRESENT";
            break;
        case SA_ERR_HPI_READ_ONLY:
            txt = L"READ_ONLY";
            break;
        case SA_ERR_HPI_CAPABILITY:
            txt = L"CAPABILITY";
            break;
        case SA_ERR_HPI_UNKNOWN:
            txt = L"UNKNOWN";
            break;
        case SA_ERR_HPI_INVALID_STATE:
            txt = L"INVALID_STATE";
            break;
        case SA_ERR_HPI_UNSUPPORTED_PARAMS:
            txt = L"UNSUPPORTED_PARAMS";
            break;
        default:
            txt = txt_unknown;
    }
}

static void SaHpiVersionToTxt( SaHpiVersionT x, std::wstring& txt )
{
    unsigned int b2 = ( x >> 16 ) & 0xFF;
    unsigned int b1 = ( x >> 8 ) & 0xFF;
    unsigned int b0 = x & 0xFF;

    wchar_t buf[16];
    swprintf( buf, sizeof(buf) / sizeof(wchar_t), L"%lc.%u.%u" , L'A' - 1 + b2, b1, b0 );
    txt = buf;
}

static void SaHpiResourceIdToTxt( SaHpiResourceIdT x, std::wstring& txt )
{
    if ( x == SAHPI_UNSPECIFIED_RESOURCE_ID ) {
        txt = L"Unspecified";
    } else {
        ToTxt( x, txt, UI32_Dec );
    }
}

static void DatUserAlarmLimitToTxt( SaHpiUint32T x, std::wstring& txt )
{
    if ( x != 0 ) {
        ToTxt( x, txt, UI32_Dec );
    } else {
        txt = L"No Limit";
    }
}

static void ConditionDomainIdToTxt( SaHpiDomainIdT x, std::wstring& txt )
{
    if ( x == SAHPI_UNSPECIFIED_DOMAIN_ID ) {
        txt = L"Current or Unspecified";
    } else {
        ToTxt( x, txt, UI32_SaHpiDomainId );
    }
}

static void AnnunciatorMaxConditionsToTxt( SaHpiUint32T x, std::wstring& txt )
{
    if ( x == 0 ) {
        txt = L"No Limit";
    } else {
        ToTxt( x, txt, UI32_Dec );
    }
}

// TODO revisit
static const wchar_t * HpiLookupXtcaEntityType( SaHpiEntityTypeT value )
{
        switch( value ) {
            case XTCAHPI_ENT_POWER_SLOT:
                return L"POWER_SLOT";
            case XTCAHPI_ENT_SHELF_FRU_DEVICE_SLOT:
                return L"SHELF_FRU_DEVICE_SLOT";
            case XTCAHPI_ENT_SHELF_MANAGER_SLOT:
                return L"SHELF_MANAGER_SLOT";
            case XTCAHPI_ENT_FAN_TRAY_SLOT:
                return L"FAN_TRAY_SLOT";
            case XTCAHPI_ENT_FAN_FILTER_TRAY_SLOT:
                return L"FAN_FILTER_TRAY_SLOT";
            case XTCAHPI_ENT_ALARM_SLOT:
                return L"ALARM_SLOT";
            case XTCAHPI_ENT_AMC_SLOT:
                return L"AMC_SLOT";
            case XTCAHPI_ENT_PMC_SLOT:
                return L"PMC_SLOT";
            case XTCAHPI_ENT_RTM_SLOT:
                return L"RTM_SLOT";
            case XTCAHPI_ENT_CARRIER_MANAGER_SLOT:
                return L"CARRIER_MANAGER_SLOT";
            case XTCAHPI_ENT_CARRIER_SLOT:
                return L"CARRIER_SLOT";
            case XTCAHPI_ENT_COM_E_SLOT:
                return L"COM_E_SLOT";
            default:
                return NULL;
        }
}

// TODO revisit
static const wchar_t * HpiLookupEntityType( SaHpiEntityTypeT value )
{
        switch( value ) {
            case SAHPI_ENT_UNSPECIFIED:
                return L"UNSPECIFIED";
            case SAHPI_ENT_OTHER:
                return L"OTHER";
            case SAHPI_ENT_UNKNOWN:
                return L"UNKNOWN";
            case SAHPI_ENT_PROCESSOR:
                return L"PROCESSOR";
            case SAHPI_ENT_DISK_BAY:
                return L"DISK_BAY";
            case SAHPI_ENT_PERIPHERAL_BAY:
                return L"PERIPHERAL_BAY";
            case SAHPI_ENT_SYS_MGMNT_MODULE:
                return L"SYS_MGMNT_MODULE";
            case SAHPI_ENT_SYSTEM_BOARD:
                return L"SYSTEM_BOARD";
            case SAHPI_ENT_MEMORY_MODULE:
                return L"MEMORY_MODULE";
            case SAHPI_ENT_PROCESSOR_MODULE:
                return L"PROCESSOR_MODULE";
            case SAHPI_ENT_POWER_SUPPLY:
                return L"POWER_SUPPLY";
            case SAHPI_ENT_ADD_IN_CARD:
                return L"ADD_IN_CARD";
            case SAHPI_ENT_FRONT_PANEL_BOARD:
                return L"FRONT_PANEL_BOARD";
            case SAHPI_ENT_BACK_PANEL_BOARD:
                return L"BACK_PANEL_BOARD";
            case SAHPI_ENT_POWER_SYSTEM_BOARD:
                return L"POWER_SYSTEM_BOARD";
            case SAHPI_ENT_DRIVE_BACKPLANE:
                return L"DRIVE_BACKPLANE";
            case SAHPI_ENT_SYS_EXPANSION_BOARD:
                return L"SYS_EXPANSION_BOARD";
            case SAHPI_ENT_OTHER_SYSTEM_BOARD:
                return L"OTHER_SYSTEM_BOARD";
            case SAHPI_ENT_PROCESSOR_BOARD:
                return L"PROCESSOR_BOARD";
            case SAHPI_ENT_POWER_UNIT:
                return L"POWER_UNIT";
            case SAHPI_ENT_POWER_MODULE:
                return L"POWER_MODULE";
            case SAHPI_ENT_POWER_MGMNT:
                return L"POWER_MGMNT";
            case SAHPI_ENT_CHASSIS_BACK_PANEL_BOARD:
                return L"CHASSIS_BACK_PANEL_BOARD";
            case SAHPI_ENT_SYSTEM_CHASSIS:
                return L"SYSTEM_CHASSIS";
            case SAHPI_ENT_SUB_CHASSIS:
                return L"SUB_CHASSIS";
            case SAHPI_ENT_OTHER_CHASSIS_BOARD:
                return L"OTHER_CHASSIS_BOARD";
            case SAHPI_ENT_DISK_DRIVE_BAY:
                return L"DISK_DRIVE_BAY";
            case SAHPI_ENT_PERIPHERAL_BAY_2:
                return L"PERIPHERAL_BAY_2";
            case SAHPI_ENT_DEVICE_BAY:
                return L"DEVICE_BAY";
            case SAHPI_ENT_COOLING_DEVICE:
                return L"COOLING_DEVICE";
            case SAHPI_ENT_COOLING_UNIT:
                return L"COOLING_UNIT";
            case SAHPI_ENT_INTERCONNECT:
                return L"INTERCONNECT";
            case SAHPI_ENT_MEMORY_DEVICE:
                return L"MEMORY_DEVICE";
            case SAHPI_ENT_SYS_MGMNT_SOFTWARE:
                return L"SYS_MGMNT_SOFTWARE";
            case SAHPI_ENT_BIOS:
                return L"BIOS";
            case SAHPI_ENT_OPERATING_SYSTEM:
                return L"OPERATING_SYSTEM";
            case SAHPI_ENT_SYSTEM_BUS:
                return L"SYSTEM_BUS";
            case SAHPI_ENT_GROUP:
                return L"GROUP";
            case SAHPI_ENT_REMOTE:
                return L"REMOTE";
            case SAHPI_ENT_EXTERNAL_ENVIRONMENT:
                return L"EXTERNAL_ENVIRONMENT";
            case SAHPI_ENT_BATTERY:
                return L"BATTERY";
            case SAHPI_ENT_RESERVED_1:
                return L"RESERVED_1";
            case SAHPI_ENT_RESERVED_2:
                return L"RESERVED_2";
            case SAHPI_ENT_RESERVED_3:
                return L"RESERVED_3";
            case SAHPI_ENT_RESERVED_4:
                return L"RESERVED_4";
            case SAHPI_ENT_RESERVED_5:
                return L"RESERVED_5";
            case SAHPI_ENT_MC_FIRMWARE:
                return L"MC_FIRMWARE";
            case SAHPI_ENT_IPMI_CHANNEL:
                return L"IPMI_CHANNEL";
            case SAHPI_ENT_PCI_BUS:
                return L"PCI_BUS";
            case SAHPI_ENT_PCI_EXPRESS_BUS:
                return L"PCI_EXPRESS_BUS";
            case SAHPI_ENT_SCSI_BUS:
                return L"SCSI_BUS";
            case SAHPI_ENT_SATA_BUS:
                return L"SATA_BUS";
            case SAHPI_ENT_PROC_FSB:
                return L"PROC_FSB";
            case SAHPI_ENT_CLOCK:
                return L"CLOCK";
            case SAHPI_ENT_SYSTEM_FIRMWARE:
                return L"SYSTEM_FIRMWARE";
            case SAHPI_ENT_CHASSIS_SPECIFIC:
                return L"CHASSIS_SPECIFIC";
            case SAHPI_ENT_BOARD_SET_SPECIFIC:
                return L"BOARD_SET_SPECIFIC";
            case SAHPI_ENT_OEM_SYSINT_SPECIFIC:
                return L"OEM_SYSINT_SPECIFIC";
            case SAHPI_ENT_ROOT:
                return L"ROOT";
            case SAHPI_ENT_RACK:
                return L"RACK";
            case SAHPI_ENT_SUBRACK:
                return L"SUBRACK";
            case SAHPI_ENT_COMPACTPCI_CHASSIS:
                return L"COMPACTPCI_CHASSIS";
            case SAHPI_ENT_ADVANCEDTCA_CHASSIS:
                return L"ADVANCEDTCA_CHASSIS";
            case SAHPI_ENT_RACK_MOUNTED_SERVER:
                return L"RACK_MOUNTED_SERVER";
            case SAHPI_ENT_SYSTEM_BLADE:
                return L"SYSTEM_BLADE";
            case SAHPI_ENT_SWITCH:
                return L"SWITCH";
            case SAHPI_ENT_SWITCH_BLADE:
                return L"SWITCH_BLADE";
            case SAHPI_ENT_SBC_BLADE:
                return L"SBC_BLADE";
            case SAHPI_ENT_IO_BLADE:
                return L"IO_BLADE";
            case SAHPI_ENT_DISK_BLADE:
                return L"DISK_BLADE";
            case SAHPI_ENT_DISK_DRIVE:
                return L"DISK_DRIVE";
            case SAHPI_ENT_FAN:
                return L"FAN";
            case SAHPI_ENT_POWER_DISTRIBUTION_UNIT:
                return L"POWER_DISTRIBUTION_UNIT";
            case SAHPI_ENT_SPEC_PROC_BLADE:
                return L"SPEC_PROC_BLADE";
            case SAHPI_ENT_IO_SUBBOARD:
                return L"IO_SUBBOARD";
            case SAHPI_ENT_SBC_SUBBOARD:
                return L"SBC_SUBBOARD";
            case SAHPI_ENT_ALARM_MANAGER:
                return L"ALARM_MANAGER";
            case SAHPI_ENT_SHELF_MANAGER:
                return L"SHELF_MANAGER";
            case SAHPI_ENT_DISPLAY_PANEL:
                return L"DISPLAY_PANEL";
            case SAHPI_ENT_SUBBOARD_CARRIER_BLADE:
                return L"SUBBOARD_CARRIER_BLADE";
            case SAHPI_ENT_PHYSICAL_SLOT:
                return L"PHYSICAL_SLOT";
            case SAHPI_ENT_PICMG_FRONT_BLADE:
                return L"PICMG_FRONT_BLADE";
            case SAHPI_ENT_SYSTEM_INVENTORY_DEVICE:
                return L"SYSTEM_INVENTORY_DEVICE";
            case SAHPI_ENT_FILTRATION_UNIT:
                return L"FILTRATION_UNIT";
            case SAHPI_ENT_AMC:
                return L"AMC";
            case SAHPI_ENT_BMC:
                return L"BMC";
            case SAHPI_ENT_IPMC:
                return L"IPMC";
            case SAHPI_ENT_MMC:
                return L"MMC";
            case SAHPI_ENT_SHMC:
                return L"SHMC";
            case SAHPI_ENT_CPLD:
                return L"CPLD";
            case SAHPI_ENT_EPLD:
                return L"EPLD";
            case SAHPI_ENT_FPGA:
                return L"FPGA";
            case SAHPI_ENT_DASD:
                return L"DASD";
            case SAHPI_ENT_NIC:
                return L"NIC";
            case SAHPI_ENT_DSP:
                return L"DSP";
            case SAHPI_ENT_UCODE:
                return L"UCODE";
            case SAHPI_ENT_NPU:
                return L"NPU";
            case SAHPI_ENT_OEM:
                return L"OEM";
            case SAHPI_ENT_INTERFACE:
                return L"INTERFACE";
            case SAHPI_ENT_MICROTCA_CHASSIS:
                return L"MICROTCA_CHASSIS";
            case SAHPI_ENT_CARRIER:
                return L"CARRIER";
            case SAHPI_ENT_CARRIER_MANAGER:
                return L"CARRIER_MANAGER";
            case SAHPI_ENT_CONFIG_DATA:
                return L"CONFIG_DATA";
            case SAHPI_ENT_INDICATOR:
                return L"INDICATOR";
            default:
                return HpiLookupXtcaEntityType( value );
        }
}


/************************************************
 * class cHpiBitFieldConvertor
 ***********************************************/
class cHpiBitFieldConvertor
{
public:

    explicit cHpiBitFieldConvertor( SaHpiUint32T value, std::wstring& txt )
        : m_value( value ), m_txt( txt )
    {
        m_txt.clear();
    }

    void TestBit( SaHpiUint32T mask, const std::wstring& bit_name )
    {
        if ( ( m_value & mask ) == mask ) {
            if ( !m_txt.empty() ) {
                m_txt += L" | ";
            }
            m_txt += bit_name;
        }
    }

    void Complete()
    {
        if ( m_txt.empty() ) {
            m_txt = L"None";
        }
    }

private:

    // data
    SaHpiUint32T  m_value;
    std::wstring& m_txt;
};


/*****************************************************
 * HPI bit field convertors
 ****************************************************/
void SaHpiSensorRangeFlagsToTxt( SaHpiSensorRangeFlagsT x, std::wstring& txt )
{
    cHpiBitFieldConvertor conv( x, txt );
    conv.TestBit( SAHPI_SRF_MIN, L"MIN" );
    conv.TestBit( SAHPI_SRF_MAX, L"MAX" );
    conv.TestBit( SAHPI_SRF_NORMAL_MIN, L"NORMAL_MIN" );
    conv.TestBit( SAHPI_SRF_NORMAL_MAX, L"NORMAL_MAX" );
    conv.TestBit( SAHPI_SRF_NOMINAL, L"NOMINAL" );
    conv.Complete();
}

static void SaHpiSensorThdMaskToTxt( SaHpiSensorThdMaskT x, std::wstring& txt )
{
    cHpiBitFieldConvertor conv( x, txt );
    conv.TestBit( SAHPI_STM_LOW_MINOR, L"LOW_MINOR" );
    conv.TestBit( SAHPI_STM_LOW_MAJOR, L"LOW_MAJOR" );
    conv.TestBit( SAHPI_STM_LOW_CRIT, L"LOW_CRIT" );
    conv.TestBit( SAHPI_STM_UP_MINOR, L"UP_MINOR" );
    conv.TestBit( SAHPI_STM_UP_MAJOR, L"UP_MAJOR" );
    conv.TestBit( SAHPI_STM_UP_CRIT, L"UP_CRIT" );
    conv.TestBit( SAHPI_STM_UP_HYSTERESIS, L"UP_HYSTERESIS" );
    conv.TestBit( SAHPI_STM_LOW_HYSTERESIS, L"LOW_HYSTERESIS" );
    conv.Complete();
}

static void SaHpiWatchdogExpFlagsToTxt( SaHpiWatchdogExpFlagsT x, std::wstring& txt )
{
    cHpiBitFieldConvertor conv( x, txt );
    conv.TestBit( SAHPI_WATCHDOG_EXP_BIOS_FRB2, L"BIOS_FRB2" );
    conv.TestBit( SAHPI_WATCHDOG_EXP_BIOS_POST, L"BIOS_POST" );
    conv.TestBit( SAHPI_WATCHDOG_EXP_OS_LOAD, L"OS_LOAD" );
    conv.TestBit( SAHPI_WATCHDOG_EXP_SMS_OS, L"SMS_OS" );
    conv.TestBit( SAHPI_WATCHDOG_EXP_OEM, L"OEM" );
    conv.Complete();
}

static void SaHpiSensorOptionalDataToTxt( SaHpiSensorOptionalDataT x, std::wstring& txt )
{
    cHpiBitFieldConvertor conv( x, txt );
    conv.TestBit( SAHPI_SOD_TRIGGER_READING, L"TRIGGER_READING" );
    conv.TestBit( SAHPI_SOD_TRIGGER_THRESHOLD, L"TRIGGER_THRESHOLD" );
    conv.TestBit( SAHPI_SOD_OEM, L"OEM" );
    conv.TestBit( SAHPI_SOD_PREVIOUS_STATE, L"PREVIOUS_STATE" );
    conv.TestBit( SAHPI_SOD_CURRENT_STATE, L"CURRENT_STATE" );
    conv.TestBit( SAHPI_SOD_SENSOR_SPECIFIC, L"SENSOR_SPECIFIC" );
    conv.Complete();
}

static void SaHpiSensorEnableOptDataToTxt( SaHpiSensorEnableOptDataT x, std::wstring& txt )
{
    cHpiBitFieldConvertor conv( x, txt );
    conv.TestBit( SAHPI_SEOD_CURRENT_STATE, L"CURRENT_STATE" );
    conv.TestBit( SAHPI_SEOD_ALARM_STATES, L"ALARM_STATES" );
    conv.Complete();
}

static void SaHpiEventStateToTxt( SaHpiEventStateT x, std::wstring& txt )
{
    if ( x == SAHPI_ES_UNSPECIFIED ) {
        txt = L"UNSPECIFIED";
    } else {
        cHpiBitFieldConvertor conv( x, txt );
        conv.TestBit( SAHPI_ES_STATE_00, L"ST_00" );
        conv.TestBit( SAHPI_ES_STATE_01, L"ST_01" );
        conv.TestBit( SAHPI_ES_STATE_02, L"ST_02" );
        conv.TestBit( SAHPI_ES_STATE_03, L"ST_03" );
        conv.TestBit( SAHPI_ES_STATE_04, L"ST_04" );
        conv.TestBit( SAHPI_ES_STATE_05, L"ST_05" );
        conv.TestBit( SAHPI_ES_STATE_06, L"ST_06" );
        conv.TestBit( SAHPI_ES_STATE_07, L"ST_07" );
        conv.TestBit( SAHPI_ES_STATE_08, L"ST_08" );
        conv.TestBit( SAHPI_ES_STATE_09, L"ST_09" );
        conv.TestBit( SAHPI_ES_STATE_10, L"ST_10" );
        conv.TestBit( SAHPI_ES_STATE_11, L"ST_11" );
        conv.TestBit( SAHPI_ES_STATE_12, L"ST_12" );
        conv.TestBit( SAHPI_ES_STATE_13, L"ST_13" );
        conv.TestBit( SAHPI_ES_STATE_14, L"ST_14" );
        conv.Complete();
    }

    wchar_t buf[16];
    swprintf( buf, sizeof(buf) / sizeof(wchar_t), L"   (0x%04X)", x );
    txt += buf;
}

static void SaHpiDimiTestCapabilityToTxt( SaHpiDimiTestCapabilityT x, std::wstring& txt )
{
    cHpiBitFieldConvertor conv( x, txt );
    // TODO remove after investigation
    // conv.TestBit( SAHPI_DIMITEST_CAPABILITY_NO_CAPABILITY, L"NO_CAPABILITY" );
    conv.TestBit( SAHPI_DIMITEST_CAPABILITY_RESULTSOUTPUT, L"RESULTSOUTPUT" );
    conv.TestBit( SAHPI_DIMITEST_CAPABILITY_SERVICEMODE, L"SERVICEMODE" );
    conv.TestBit( SAHPI_DIMITEST_CAPABILITY_LOOPCOUNT, L"LOOPCOUNT" );
    conv.TestBit( SAHPI_DIMITEST_CAPABILITY_LOOPTIME, L"LOOPTIME" );
    conv.TestBit( SAHPI_DIMITEST_CAPABILITY_LOGGING, L"LOGGING" );
    conv.TestBit( SAHPI_DIMITEST_CAPABILITY_TESTCANCEL, L"TESTCANCEL" );
    conv.Complete();
}

static void SaHpiFumiLogicalBankStateFlagsToTxt( SaHpiFumiLogicalBankStateFlagsT x, std::wstring& txt )
{
    cHpiBitFieldConvertor conv( x, txt );
    conv.TestBit( SAHPI_FUMI_NO_MAIN_PERSISTENT_COPY, L"NO_MAIN_PERSISTENT_COPY" );
    conv.Complete();
}

static void SaHpiFumiProtocolToTxt( SaHpiFumiProtocolT x, std::wstring& txt )
{
    cHpiBitFieldConvertor conv( x, txt );
    conv.TestBit( SAHPI_FUMI_PROT_TFTP, L"TFTP" );
    conv.TestBit( SAHPI_FUMI_PROT_FTP, L"FTP" );
    conv.TestBit( SAHPI_FUMI_PROT_HTTP, L"HTTP" );
    conv.TestBit( SAHPI_FUMI_PROT_LDAP, L"LDAP" );
    conv.TestBit( SAHPI_FUMI_PROT_LOCAL, L"LOCAL" );
    conv.TestBit( SAHPI_FUMI_PROT_NFS, L"NFS" );
    conv.TestBit( SAHPI_FUMI_PROT_DBACCESS, L"DBACCESS" );
    conv.Complete();
}

static void SaHpiFumiCapabilityToTxt( SaHpiFumiCapabilityT x, std::wstring& txt )
{
    cHpiBitFieldConvertor conv( x, txt );
    conv.TestBit( SAHPI_FUMI_CAP_ROLLBACK, L"ROLLBACK" );
    conv.TestBit( SAHPI_FUMI_CAP_BANKCOPY, L"BANKCOPY" );
    conv.TestBit( SAHPI_FUMI_CAP_BANKREORDER, L"BANKREORDER" );
    conv.TestBit( SAHPI_FUMI_CAP_BACKUP, L"BACKUP" );
    conv.TestBit( SAHPI_FUMI_CAP_TARGET_VERIFY, L"TARGET_VERIFY" );
    conv.TestBit( SAHPI_FUMI_CAP_TARGET_VERIFY_MAIN, L"TARGET_VERIFY_MAIN" );
    conv.TestBit( SAHPI_FUMI_CAP_COMPONENTS, L"COMPONENTS" );
    conv.TestBit( SAHPI_FUMI_CAP_AUTOROLLBACK, L"AUTOROLLBACK" );
    conv.TestBit( SAHPI_FUMI_CAP_AUTOROLLBACK_CAN_BE_DISABLED, L"AUTOROLLBACK_CAN_BE_DISABLED" );
    conv.TestBit( SAHPI_FUMI_CAP_MAIN_NOT_PERSISTENT, L"MAIN_NOT_PERSISTENT" );
    conv.Complete();
}

static void SaHpiEvtQueueStatusToTxt( SaHpiEvtQueueStatusT x, std::wstring& txt )
{
    cHpiBitFieldConvertor conv( x, txt );
    conv.TestBit( SAHPI_EVT_QUEUE_OVERFLOW, L"OVERFLOW" );
    conv.Complete();
}

static void SaHpiCapabilitiesToTxt( SaHpiCapabilitiesT x, std::wstring& txt )
{
    cHpiBitFieldConvertor conv( x, txt );
    conv.TestBit( SAHPI_CAPABILITY_RESOURCE, L"RESOURCE" );
    conv.TestBit( SAHPI_CAPABILITY_FUMI, L"FUMI" );
    conv.TestBit( SAHPI_CAPABILITY_EVT_DEASSERTS, L"EVT_DEASSERTS" );
    conv.TestBit( SAHPI_CAPABILITY_DIMI, L"DIMI" );
    conv.TestBit( SAHPI_CAPABILITY_AGGREGATE_STATUS, L"AGGREGATE_STATUS" );
    conv.TestBit( SAHPI_CAPABILITY_CONFIGURATION, L"CONFIGURATION" );
    conv.TestBit( SAHPI_CAPABILITY_MANAGED_HOTSWAP, L"MANAGED_HOTSWAP" );
    conv.TestBit( SAHPI_CAPABILITY_WATCHDOG, L"WATCHDOG" );
    conv.TestBit( SAHPI_CAPABILITY_CONTROL, L"CONTROL" );
    conv.TestBit( SAHPI_CAPABILITY_FRU, L"FRU" );
    conv.TestBit( SAHPI_CAPABILITY_LOAD_ID, L"LOAD_ID" );
    conv.TestBit( SAHPI_CAPABILITY_ANNUNCIATOR, L"ANNUNCIATOR" );
    conv.TestBit( SAHPI_CAPABILITY_POWER, L"POWER" );
    conv.TestBit( SAHPI_CAPABILITY_RESET, L"RESET" );
    conv.TestBit( SAHPI_CAPABILITY_INVENTORY_DATA, L"INVENTORY_DATA" );
    conv.TestBit( SAHPI_CAPABILITY_EVENT_LOG, L"EVENT_LOG" );
    conv.TestBit( SAHPI_CAPABILITY_RDR, L"RDR" );
    conv.TestBit( SAHPI_CAPABILITY_SENSOR, L"SENSOR" );
    conv.Complete();
}

static void SaHpiHsCapabilitiesToTxt( SaHpiHsCapabilitiesT x, std::wstring& txt )
{
    cHpiBitFieldConvertor conv( x, txt );
    conv.TestBit( SAHPI_HS_CAPABILITY_AUTOEXTRACT_READ_ONLY, L"AUTOEXTRACT_READ_ONLY" );
    conv.TestBit( SAHPI_HS_CAPABILITY_INDICATOR_SUPPORTED, L"INDICATOR_SUPPORTED" );
    conv.TestBit( SAHPI_HS_CAPABILITY_AUTOINSERT_IMMEDIATE, L"AUTOINSERT_IMMEDIATE" );
    conv.Complete();
}

static void SaHpiDomainCapabilitiesToTxt( SaHpiDomainCapabilitiesT x, std::wstring& txt )
{
    cHpiBitFieldConvertor conv( x, txt );
    conv.TestBit( SAHPI_DOMAIN_CAP_AUTOINSERT_READ_ONLY, L"AUTOINSERT_READ_ONLY" );
    conv.Complete();

}

static void SaHpiEventLogCapabilitiesToTxt( SaHpiEventLogCapabilitiesT x, std::wstring& txt )
{
    cHpiBitFieldConvertor conv( x, txt );
    conv.TestBit( SAHPI_EVTLOG_CAPABILITY_ENTRY_ADD, L"ENTRY_ADD" );
    conv.TestBit( SAHPI_EVTLOG_CAPABILITY_CLEAR, L"CLEAR" );
    conv.TestBit( SAHPI_EVTLOG_CAPABILITY_TIME_SET, L"TIME_SET" );
    conv.TestBit( SAHPI_EVTLOG_CAPABILITY_STATE_SET, L"STATE_SET" );
    conv.TestBit( SAHPI_EVTLOG_CAPABILITY_OVERFLOW_RESET, L"OVERFLOW_RESET" );
    conv.Complete();
}


/*****************************************************
 * HPI basic type convertors
 ****************************************************/
void ToTxt( SaHpiUint8T x, std::wstring& txt, UI8_Fmt fmt )
{
    switch ( fmt ) {
        case UI8_Dec:
        case UI8_SaHpiTxtLineNum:
            {
                wchar_t buf[8];
                swprintf( buf, sizeof(buf) / sizeof(wchar_t), L"%u", x );
                txt = buf;
            }
            return;
        case UI8_SaHpiBool:
            SaHpiBoolToTxt( x, txt );
            return;
        case UI8_SaHpiEventCategory:
            SaHpiEventCategoryToTxt( x, txt );
            return;
        case UI8_SaHpiSensorRangeFlags:
            SaHpiSensorRangeFlagsToTxt( x, txt );
            return;
        case UI8_SaHpiSensorThdMask:
            SaHpiSensorThdMaskToTxt( x, txt );
            return;
        case UI8_SaHpiWatchdogExpFlags:
            SaHpiWatchdogExpFlagsToTxt( x, txt );
            return;
        case UI8_SaHpiDimiTestPercentCompleted:
            SaHpiDimiTestPercentCompletedToTxt( x, txt );
            return;
        case UI8_SaHpiBankNum:
            SaHpiBankNumToTxt( x, txt );
            return;
        case UI8_SaHpiSensorOptionalData:
            SaHpiSensorOptionalDataToTxt( x, txt );
            return;
        case UI8_SaHpiSensorEnableOptData:
            SaHpiSensorEnableOptDataToTxt( x, txt );
            return;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiUint16T x, std::wstring& txt, UI16_Fmt fmt )
{
    switch ( fmt ) {
        case UI16_Dec:
            {
                wchar_t buf[8];
                swprintf( buf, sizeof(buf) / sizeof(wchar_t), L"%u", x );
                txt = buf;
            }
            return;
        case UI16_Hex:
            {
                wchar_t buf[8];
                swprintf( buf, sizeof(buf) / sizeof(wchar_t), L"0x%X", x );
                txt = buf;
            }
            return;
        case UI16_SaHpiEventState:
            SaHpiEventStateToTxt( x, txt );
            return;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiInt32T x, std::wstring& txt, I32_Fmt fmt )
{
    switch ( fmt ) {
        case I32_Dec:
        case I32_SaHpiCtrlStateAnalog:
            {
                wchar_t buf[16];
                swprintf( buf, sizeof(buf) / sizeof(wchar_t), L"%d", x );
                txt = buf;
            }
            return;
        case I32_SaError:
            SaErrorToTxt( x, txt );
            return;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiUint32T x, std::wstring& txt, UI32_Fmt fmt )
{
    switch ( fmt ) {
        case UI32_Dec:
        case UI32_SaHpiEntryId:
        case UI32_SaHpiDomainId:
        case UI32_SaHpiSessionId:
        case UI32_SaHpiInstrumentId:
        case UI32_SaHpiSensorNum:
        case UI32_SaHpiCtrlNum:
        case UI32_SaHpiIdrId:
        case UI32_SaHpiWatchdogNum:
        case UI32_SaHpiAnnunciatorNum:
        case UI32_SaHpiDimiNum:
        case UI32_SaHpiFumiNum:
        case UI32_SaHpiCtrlStateDiscrete:
        case UI32_SaHpiDimiTestNum:
        case UI32_SaHpiAlarmId:
        case UI32_SaHpiLoadNumber:
        case UI32_SaHpiEventLogEntryId:
            {
                wchar_t buf[16];
                swprintf( buf, sizeof(buf) / sizeof(wchar_t), L"%u", x );
                txt = buf;
            }
            return;
        case UI32_Hex:
        case UI32_SaHpiManufacturerId:
            {
                wchar_t buf[16];
                swprintf( buf, sizeof(buf) / sizeof(wchar_t), L"0x%X", x );
                txt = buf;
            }
            return;
        case UI32_SaHpiVersion:
            SaHpiVersionToTxt( x, txt );
            return;
        case UI32_SaHpiResourceId:
            SaHpiResourceIdToTxt( x, txt );
            return;
        case UI32_SaHpiDimiTestCapability:
            SaHpiDimiTestCapabilityToTxt( x, txt );
            return;
        case UI32_SaHpiFumiLogicalBankStateFlags:
            SaHpiFumiLogicalBankStateFlagsToTxt( x, txt );
            return;
        case UI32_SaHpiFumiProtocol:
            SaHpiFumiProtocolToTxt( x, txt );
            return;
        case UI32_SaHpiFumiCapability:
            SaHpiFumiCapabilityToTxt( x, txt );
            return;
        case UI32_SaHpiEvtQueueStatus:
            SaHpiEvtQueueStatusToTxt( x, txt );
            return;
        case UI32_SaHpiCapabilities:
            SaHpiCapabilitiesToTxt( x, txt );
            return;
        case UI32_SaHpiHsCapabilities:
            SaHpiHsCapabilitiesToTxt( x, txt );
            return;
        case UI32_SaHpiDomainCapabilities:
            SaHpiDomainCapabilitiesToTxt( x, txt );
            return;
        case UI32_SaHpiEventLogCapabilities:
            SaHpiEventLogCapabilitiesToTxt( x, txt );
            return;
        case UI32_DatUserAlarmLimit:
            DatUserAlarmLimitToTxt( x, txt );
            return;
        case UI32_ConditionDomainId:
            ConditionDomainIdToTxt( x, txt );
            return;
        case UI32_AnnunciatorMaxConditions:
            AnnunciatorMaxConditionsToTxt( x, txt );
            return;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiInt64T x, std::wstring& txt, I64_Fmt fmt )
{
    switch ( fmt ) {
        case I64_Dec:
            {
                wchar_t buf[32];
                swprintf( buf, sizeof(buf) / sizeof(wchar_t), L"%lld", x );
                txt = buf;
            }
            return;
        case I64_SaHpiTime:
            SaHpiTime2String( x, txt );
            return;
        case I64_SaHpiTimeout:
            SaHpiTimeout2String( x, txt );
            return;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiUint64T x, std::wstring& txt, UI64_Fmt fmt )
{
    switch ( fmt ) {
        case UI64_Dec:
            {
                wchar_t buf[32];
                swprintf( buf, sizeof(buf) / sizeof(wchar_t), L"%llu", x );
                txt = buf;
            }
            return;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiFloat64T x, std::wstring& txt, F64_Fmt fmt )
{
    switch ( fmt ) {
        case F64_FixedPoint:
            {
                wchar_t buf[64];
                swprintf( buf, sizeof(buf) / sizeof(wchar_t), L"%f", x );
                txt = buf;
            }
            return;
        case F64_FloatingPoint:
            {
                wchar_t buf[64];
                swprintf( buf, sizeof(buf) / sizeof(wchar_t), L"%E", x );
                txt = buf;
            }
            return;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( const SaHpiUint8T * binary, SaHpiUint16T len, std::wstring& txt )
{
    txt.clear();
    txt.reserve( 3 * len );

    for ( unsigned int i = 0; i < len; ++i ) {
        wchar_t buf[4];
        if ( ( i + 1 ) != len ) {
            swprintf( buf, ( sizeof(buf) / sizeof(wchar_t) ), L"%02X-", binary[i] );
        } else {
            swprintf( buf, ( sizeof(buf) / sizeof(wchar_t) ), L"%02X", binary[i] );
        }
        txt += buf;
    }
}


/*****************************************************
 * HPI enum convertors
 ****************************************************/
void ToTxt( SaHpiLanguageT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_LANG_UNDEF:
            txt = L"UNDEF";
            break;
        case SAHPI_LANG_AFAR:
            txt = L"AFAR";
            break;
        case SAHPI_LANG_ABKHAZIAN:
            txt = L"ABKHAZIAN";
            break;
        case SAHPI_LANG_AFRIKAANS:
            txt = L"AFRIKAANS";
            break;
        case SAHPI_LANG_AMHARIC:
            txt = L"AMHARIC";
            break;
        case SAHPI_LANG_ARABIC:
            txt = L"ARABIC";
            break;
        case SAHPI_LANG_ASSAMESE:
            txt = L"ASSAMESE";
            break;
        case SAHPI_LANG_AYMARA:
            txt = L"AYMARA";
            break;
        case SAHPI_LANG_AZERBAIJANI:
            txt = L"AZERBAIJANI";
            break;
        case SAHPI_LANG_BASHKIR:
            txt = L"BASHKIR";
            break;
        case SAHPI_LANG_BYELORUSSIAN:
            txt = L"BYELORUSSIAN";
            break;
        case SAHPI_LANG_BULGARIAN:
            txt = L"BULGARIAN";
            break;
        case SAHPI_LANG_BIHARI:
            txt = L"BIHARI";
            break;
        case SAHPI_LANG_BISLAMA:
            txt = L"BISLAMA";
            break;
        case SAHPI_LANG_BENGALI:
            txt = L"BENGALI";
            break;
        case SAHPI_LANG_TIBETAN:
            txt = L"TIBETAN";
            break;
        case SAHPI_LANG_BRETON:
            txt = L"BRETON";
            break;
        case SAHPI_LANG_CATALAN:
            txt = L"CATALAN";
            break;
        case SAHPI_LANG_CORSICAN:
            txt = L"CORSICAN";
            break;
        case SAHPI_LANG_CZECH:
            txt = L"CZECH";
            break;
        case SAHPI_LANG_WELSH:
            txt = L"WELSH";
            break;
        case SAHPI_LANG_DANISH:
            txt = L"DANISH";
            break;
        case SAHPI_LANG_GERMAN:
            txt = L"GERMAN";
            break;
        case SAHPI_LANG_BHUTANI:
            txt = L"BHUTANI";
            break;
        case SAHPI_LANG_GREEK:
            txt = L"GREEK";
            break;
        case SAHPI_LANG_ENGLISH:
            txt = L"ENGLISH";
            break;
        case SAHPI_LANG_ESPERANTO:
            txt = L"ESPERANTO";
            break;
        case SAHPI_LANG_SPANISH:
            txt = L"SPANISH";
            break;
        case SAHPI_LANG_ESTONIAN:
            txt = L"ESTONIAN";
            break;
        case SAHPI_LANG_BASQUE:
            txt = L"BASQUE";
            break;
        case SAHPI_LANG_PERSIAN:
            txt = L"PERSIAN";
            break;
        case SAHPI_LANG_FINNISH:
            txt = L"FINNISH";
            break;
        case SAHPI_LANG_FIJI:
            txt = L"FIJI";
            break;
        case SAHPI_LANG_FAEROESE:
            txt = L"FAEROESE";
            break;
        case SAHPI_LANG_FRENCH:
            txt = L"FRENCH";
            break;
        case SAHPI_LANG_FRISIAN:
            txt = L"FRISIAN";
            break;
        case SAHPI_LANG_IRISH:
            txt = L"IRISH";
            break;
        case SAHPI_LANG_SCOTSGAELIC:
            txt = L"SCOTSGAELIC";
            break;
        case SAHPI_LANG_GALICIAN:
            txt = L"GALICIAN";
            break;
        case SAHPI_LANG_GUARANI:
            txt = L"GUARANI";
            break;
        case SAHPI_LANG_GUJARATI:
            txt = L"GUJARATI";
            break;
        case SAHPI_LANG_HAUSA:
            txt = L"HAUSA";
            break;
        case SAHPI_LANG_HINDI:
            txt = L"HINDI";
            break;
        case SAHPI_LANG_CROATIAN:
            txt = L"CROATIAN";
            break;
        case SAHPI_LANG_HUNGARIAN:
            txt = L"HUNGARIAN";
            break;
        case SAHPI_LANG_ARMENIAN:
            txt = L"ARMENIAN";
            break;
        case SAHPI_LANG_INTERLINGUA:
            txt = L"INTERLINGUA";
            break;
        case SAHPI_LANG_INTERLINGUE:
            txt = L"INTERLINGUE";
            break;
        case SAHPI_LANG_INUPIAK:
            txt = L"INUPIAK";
            break;
        case SAHPI_LANG_INDONESIAN:
            txt = L"INDONESIAN";
            break;
        case SAHPI_LANG_ICELANDIC:
            txt = L"ICELANDIC";
            break;
        case SAHPI_LANG_ITALIAN:
            txt = L"ITALIAN";
            break;
        case SAHPI_LANG_HEBREW:
            txt = L"HEBREW";
            break;
        case SAHPI_LANG_JAPANESE:
            txt = L"JAPANESE";
            break;
        case SAHPI_LANG_YIDDISH:
            txt = L"YIDDISH";
            break;
        case SAHPI_LANG_JAVANESE:
            txt = L"JAVANESE";
            break;
        case SAHPI_LANG_GEORGIAN:
            txt = L"GEORGIAN";
            break;
        case SAHPI_LANG_KAZAKH:
            txt = L"KAZAKH";
            break;
        case SAHPI_LANG_GREENLANDIC:
            txt = L"GREENLANDIC";
            break;
        case SAHPI_LANG_CAMBODIAN:
            txt = L"CAMBODIAN";
            break;
        case SAHPI_LANG_KANNADA:
            txt = L"KANNADA";
            break;
        case SAHPI_LANG_KOREAN:
            txt = L"KOREAN";
            break;
        case SAHPI_LANG_KASHMIRI:
            txt = L"KASHMIRI";
            break;
        case SAHPI_LANG_KURDISH:
            txt = L"KURDISH";
            break;
        case SAHPI_LANG_KIRGHIZ:
            txt = L"KIRGHIZ";
            break;
        case SAHPI_LANG_LATIN:
            txt = L"LATIN";
            break;
        case SAHPI_LANG_LINGALA:
            txt = L"LINGALA";
            break;
        case SAHPI_LANG_LAOTHIAN:
            txt = L"LAOTHIAN";
            break;
        case SAHPI_LANG_LITHUANIAN:
            txt = L"LITHUANIAN";
            break;
        case SAHPI_LANG_LATVIANLETTISH:
            txt = L"LATVIANLETTISH";
            break;
        case SAHPI_LANG_MALAGASY:
            txt = L"MALAGASY";
            break;
        case SAHPI_LANG_MAORI:
            txt = L"MAORI";
            break;
        case SAHPI_LANG_MACEDONIAN:
            txt = L"MACEDONIAN";
            break;
        case SAHPI_LANG_MALAYALAM:
            txt = L"MALAYALAM";
            break;
        case SAHPI_LANG_MONGOLIAN:
            txt = L"MONGOLIAN";
            break;
        case SAHPI_LANG_MOLDAVIAN:
            txt = L"MOLDAVIAN";
            break;
        case SAHPI_LANG_MARATHI:
            txt = L"MARATHI";
            break;
        case SAHPI_LANG_MALAY:
            txt = L"MALAY";
            break;
        case SAHPI_LANG_MALTESE:
            txt = L"MALTESE";
            break;
        case SAHPI_LANG_BURMESE:
            txt = L"BURMESE";
            break;
        case SAHPI_LANG_NAURU:
            txt = L"NAURU";
            break;
        case SAHPI_LANG_NEPALI:
            txt = L"NEPALI";
            break;
        case SAHPI_LANG_DUTCH:
            txt = L"DUTCH";
            break;
        case SAHPI_LANG_NORWEGIAN:
            txt = L"NORWEGIAN";
            break;
        case SAHPI_LANG_OCCITAN:
            txt = L"OCCITAN";
            break;
        case SAHPI_LANG_AFANOROMO:
            txt = L"AFANOROMO";
            break;
        case SAHPI_LANG_ORIYA:
            txt = L"ORIYA";
            break;
        case SAHPI_LANG_PUNJABI:
            txt = L"PUNJABI";
            break;
        case SAHPI_LANG_POLISH:
            txt = L"POLISH";
            break;
        case SAHPI_LANG_PASHTOPUSHTO:
            txt = L"PASHTOPUSHTO";
            break;
        case SAHPI_LANG_PORTUGUESE:
            txt = L"PORTUGUESE";
            break;
        case SAHPI_LANG_QUECHUA:
            txt = L"QUECHUA";
            break;
        case SAHPI_LANG_RHAETOROMANCE:
            txt = L"RHAETOROMANCE";
            break;
        case SAHPI_LANG_KIRUNDI:
            txt = L"KIRUNDI";
            break;
        case SAHPI_LANG_ROMANIAN:
            txt = L"ROMANIAN";
            break;
        case SAHPI_LANG_RUSSIAN:
            txt = L"RUSSIAN";
            break;
        case SAHPI_LANG_KINYARWANDA:
            txt = L"KINYARWANDA";
            break;
        case SAHPI_LANG_SANSKRIT:
            txt = L"SANSKRIT";
            break;
        case SAHPI_LANG_SINDHI:
            txt = L"SINDHI";
            break;
        case SAHPI_LANG_SANGRO:
            txt = L"SANGRO";
            break;
        case SAHPI_LANG_SERBOCROATIAN:
            txt = L"SERBOCROATIAN";
            break;
        case SAHPI_LANG_SINGHALESE:
            txt = L"SINGHALESE";
            break;
        case SAHPI_LANG_SLOVAK:
            txt = L"SLOVAK";
            break;
        case SAHPI_LANG_SLOVENIAN:
            txt = L"SLOVENIAN";
            break;
        case SAHPI_LANG_SAMOAN:
            txt = L"SAMOAN";
            break;
        case SAHPI_LANG_SHONA:
            txt = L"SHONA";
            break;
        case SAHPI_LANG_SOMALI:
            txt = L"SOMALI";
            break;
        case SAHPI_LANG_ALBANIAN:
            txt = L"ALBANIAN";
            break;
        case SAHPI_LANG_SERBIAN:
            txt = L"SERBIAN";
            break;
        case SAHPI_LANG_SISWATI:
            txt = L"SISWATI";
            break;
        case SAHPI_LANG_SESOTHO:
            txt = L"SESOTHO";
            break;
        case SAHPI_LANG_SUDANESE:
            txt = L"SUDANESE";
            break;
        case SAHPI_LANG_SWEDISH:
            txt = L"SWEDISH";
            break;
        case SAHPI_LANG_SWAHILI:
            txt = L"SWAHILI";
            break;
        case SAHPI_LANG_TAMIL:
            txt = L"TAMIL";
            break;
        case SAHPI_LANG_TELUGU:
            txt = L"TELUGU";
            break;
        case SAHPI_LANG_TAJIK:
            txt = L"TAJIK";
            break;
        case SAHPI_LANG_THAI:
            txt = L"THAI";
            break;
        case SAHPI_LANG_TIGRINYA:
            txt = L"TIGRINYA";
            break;
        case SAHPI_LANG_TURKMEN:
            txt = L"TURKMEN";
            break;
        case SAHPI_LANG_TAGALOG:
            txt = L"TAGALOG";
            break;
        case SAHPI_LANG_SETSWANA:
            txt = L"SETSWANA";
            break;
        case SAHPI_LANG_TONGA:
            txt = L"TONGA";
            break;
        case SAHPI_LANG_TURKISH:
            txt = L"TURKISH";
            break;
        case SAHPI_LANG_TSONGA:
            txt = L"TSONGA";
            break;
        case SAHPI_LANG_TATAR:
            txt = L"TATAR";
            break;
        case SAHPI_LANG_TWI:
            txt = L"TWI";
            break;
        case SAHPI_LANG_UKRAINIAN:
            txt = L"UKRAINIAN";
            break;
        case SAHPI_LANG_URDU:
            txt = L"URDU";
            break;
        case SAHPI_LANG_UZBEK:
            txt = L"UZBEK";
            break;
        case SAHPI_LANG_VIETNAMESE:
            txt = L"VIETNAMESE";
            break;
        case SAHPI_LANG_VOLAPUK:
            txt = L"VOLAPUK";
            break;
        case SAHPI_LANG_WOLOF:
            txt = L"WOLOF";
            break;
        case SAHPI_LANG_XHOSA:
            txt = L"XHOSA";
            break;
        case SAHPI_LANG_YORUBA:
            txt = L"YORUBA";
            break;
        case SAHPI_LANG_CHINESE:
            txt = L"CHINESE";
            break;
        case SAHPI_LANG_ZULU:
            txt = L"ZULU";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiTextTypeT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_TL_TYPE_UNICODE:
            txt = L"UNICODE";
            break;
        case SAHPI_TL_TYPE_BCDPLUS:
            txt = L"BCDPLUS";
            break;
        case SAHPI_TL_TYPE_ASCII6:
            txt = L"ASCII6";
            break;
        case SAHPI_TL_TYPE_TEXT:
            txt = L"TEXT";
            break;
        case SAHPI_TL_TYPE_BINARY:
            txt = L"BINARY";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiEntityTypeT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_ENT_UNSPECIFIED:
            txt = L"UNSPECIFIED";
            break;
        case SAHPI_ENT_OTHER:
            txt = L"OTHER";
            break;
        case SAHPI_ENT_UNKNOWN:
            txt = L"UNKNOWN";
            break;
        case SAHPI_ENT_PROCESSOR:
            txt = L"PROCESSOR";
            break;
        case SAHPI_ENT_DISK_BAY:
            txt = L"DISK_BAY";
            break;
        case SAHPI_ENT_PERIPHERAL_BAY:
            txt = L"PERIPHERAL_BAY";
            break;
        case SAHPI_ENT_SYS_MGMNT_MODULE:
            txt = L"SYS_MGMNT_MODULE";
            break;
        case SAHPI_ENT_SYSTEM_BOARD:
            txt = L"SYSTEM_BOARD";
            break;
        case SAHPI_ENT_MEMORY_MODULE:
            txt = L"MEMORY_MODULE";
            break;
        case SAHPI_ENT_PROCESSOR_MODULE:
            txt = L"PROCESSOR_MODULE";
            break;
        case SAHPI_ENT_POWER_SUPPLY:
            txt = L"POWER_SUPPLY";
            break;
        case SAHPI_ENT_ADD_IN_CARD:
            txt = L"ADD_IN_CARD";
            break;
        case SAHPI_ENT_FRONT_PANEL_BOARD:
            txt = L"FRONT_PANEL_BOARD";
            break;
        case SAHPI_ENT_BACK_PANEL_BOARD:
            txt = L"BACK_PANEL_BOARD";
            break;
        case SAHPI_ENT_POWER_SYSTEM_BOARD:
            txt = L"POWER_SYSTEM_BOARD";
            break;
        case SAHPI_ENT_DRIVE_BACKPLANE:
            txt = L"DRIVE_BACKPLANE";
            break;
        case SAHPI_ENT_SYS_EXPANSION_BOARD:
            txt = L"SYS_EXPANSION_BOARD";
            break;
        case SAHPI_ENT_OTHER_SYSTEM_BOARD:
            txt = L"OTHER_SYSTEM_BOARD";
            break;
        case SAHPI_ENT_PROCESSOR_BOARD:
            txt = L"PROCESSOR_BOARD";
            break;
        case SAHPI_ENT_POWER_UNIT:
            txt = L"POWER_UNIT";
            break;
        case SAHPI_ENT_POWER_MODULE:
            txt = L"POWER_MODULE";
            break;
        case SAHPI_ENT_POWER_MGMNT:
            txt = L"POWER_MGMNT";
            break;
        case SAHPI_ENT_CHASSIS_BACK_PANEL_BOARD:
            txt = L"CHASSIS_BACK_PANEL_BOARD";
            break;
        case SAHPI_ENT_SYSTEM_CHASSIS:
            txt = L"SYSTEM_CHASSIS";
            break;
        case SAHPI_ENT_SUB_CHASSIS:
            txt = L"SUB_CHASSIS";
            break;
        case SAHPI_ENT_OTHER_CHASSIS_BOARD:
            txt = L"OTHER_CHASSIS_BOARD";
            break;
        case SAHPI_ENT_DISK_DRIVE_BAY:
            txt = L"DISK_DRIVE_BAY";
            break;
        case SAHPI_ENT_PERIPHERAL_BAY_2:
            txt = L"PERIPHERAL_BAY_2";
            break;
        case SAHPI_ENT_DEVICE_BAY:
            txt = L"DEVICE_BAY";
            break;
        case SAHPI_ENT_COOLING_DEVICE:
            txt = L"COOLING_DEVICE";
            break;
        case SAHPI_ENT_COOLING_UNIT:
            txt = L"COOLING_UNIT";
            break;
        case SAHPI_ENT_INTERCONNECT:
            txt = L"INTERCONNECT";
            break;
        case SAHPI_ENT_MEMORY_DEVICE:
            txt = L"MEMORY_DEVICE";
            break;
        case SAHPI_ENT_SYS_MGMNT_SOFTWARE:
            txt = L"SYS_MGMNT_SOFTWARE";
            break;
        case SAHPI_ENT_BIOS:
            txt = L"BIOS";
            break;
        case SAHPI_ENT_OPERATING_SYSTEM:
            txt = L"OPERATING_SYSTEM";
            break;
        case SAHPI_ENT_SYSTEM_BUS:
            txt = L"SYSTEM_BUS";
            break;
        case SAHPI_ENT_GROUP:
            txt = L"GROUP";
            break;
        case SAHPI_ENT_REMOTE:
            txt = L"REMOTE";
            break;
        case SAHPI_ENT_EXTERNAL_ENVIRONMENT:
            txt = L"EXTERNAL_ENVIRONMENT";
            break;
        case SAHPI_ENT_BATTERY:
            txt = L"BATTERY";
            break;
        case SAHPI_ENT_RESERVED_1:
            txt = L"RESERVED_1";
            break;
        case SAHPI_ENT_RESERVED_2:
            txt = L"RESERVED_2";
            break;
        case SAHPI_ENT_RESERVED_3:
            txt = L"RESERVED_3";
            break;
        case SAHPI_ENT_RESERVED_4:
            txt = L"RESERVED_4";
            break;
        case SAHPI_ENT_RESERVED_5:
            txt = L"RESERVED_5";
            break;
        case SAHPI_ENT_MC_FIRMWARE:
            txt = L"MC_FIRMWARE";
            break;
        case SAHPI_ENT_IPMI_CHANNEL:
            txt = L"IPMI_CHANNEL";
            break;
        case SAHPI_ENT_PCI_BUS:
            txt = L"PCI_BUS";
            break;
        case SAHPI_ENT_PCI_EXPRESS_BUS:
            txt = L"PCI_EXPRESS_BUS";
            break;
        case SAHPI_ENT_SCSI_BUS:
            txt = L"SCSI_BUS";
            break;
        case SAHPI_ENT_SATA_BUS:
            txt = L"SATA_BUS";
            break;
        case SAHPI_ENT_PROC_FSB:
            txt = L"PROC_FSB";
            break;
        case SAHPI_ENT_CLOCK:
            txt = L"CLOCK";
            break;
        case SAHPI_ENT_SYSTEM_FIRMWARE:
            txt = L"SYSTEM_FIRMWARE";
            break;
        case SAHPI_ENT_CHASSIS_SPECIFIC:
            txt = L"CHASSIS_SPECIFIC";
            break;
        case SAHPI_ENT_BOARD_SET_SPECIFIC:
            txt = L"BOARD_SET_SPECIFIC";
            break;
        case SAHPI_ENT_OEM_SYSINT_SPECIFIC:
            txt = L"OEM_SYSINT_SPECIFIC";
            break;
        case SAHPI_ENT_ROOT:
            txt = L"ROOT";
            break;
        case SAHPI_ENT_RACK:
            txt = L"RACK";
            break;
        case SAHPI_ENT_SUBRACK:
            txt = L"SUBRACK";
            break;
        case SAHPI_ENT_COMPACTPCI_CHASSIS:
            txt = L"COMPACTPCI_CHASSIS";
            break;
        case SAHPI_ENT_ADVANCEDTCA_CHASSIS:
            txt = L"ADVANCEDTCA_CHASSIS";
            break;
        case SAHPI_ENT_RACK_MOUNTED_SERVER:
            txt = L"RACK_MOUNTED_SERVER";
            break;
        case SAHPI_ENT_SYSTEM_BLADE:
            txt = L"SYSTEM_BLADE";
            break;
        case SAHPI_ENT_SWITCH:
            txt = L"SWITCH";
            break;
        case SAHPI_ENT_SWITCH_BLADE:
            txt = L"SWITCH_BLADE";
            break;
        case SAHPI_ENT_SBC_BLADE:
            txt = L"SBC_BLADE";
            break;
        case SAHPI_ENT_IO_BLADE:
            txt = L"IO_BLADE";
            break;
        case SAHPI_ENT_DISK_BLADE:
            txt = L"DISK_BLADE";
            break;
        case SAHPI_ENT_DISK_DRIVE:
            txt = L"DISK_DRIVE";
            break;
        case SAHPI_ENT_FAN:
            txt = L"FAN";
            break;
        case SAHPI_ENT_POWER_DISTRIBUTION_UNIT:
            txt = L"POWER_DISTRIBUTION_UNIT";
            break;
        case SAHPI_ENT_SPEC_PROC_BLADE:
            txt = L"SPEC_PROC_BLADE";
            break;
        case SAHPI_ENT_IO_SUBBOARD:
            txt = L"IO_SUBBOARD";
            break;
        case SAHPI_ENT_SBC_SUBBOARD:
            txt = L"SBC_SUBBOARD";
            break;
        case SAHPI_ENT_ALARM_MANAGER:
            txt = L"ALARM_MANAGER";
            break;
        case SAHPI_ENT_SHELF_MANAGER:
            txt = L"SHELF_MANAGER";
            break;
        case SAHPI_ENT_DISPLAY_PANEL:
            txt = L"DISPLAY_PANEL";
            break;
        case SAHPI_ENT_SUBBOARD_CARRIER_BLADE:
            txt = L"SUBBOARD_CARRIER_BLADE";
            break;
        case SAHPI_ENT_PHYSICAL_SLOT:
            txt = L"PHYSICAL_SLOT";
            break;
        case SAHPI_ENT_PICMG_FRONT_BLADE:
            txt = L"PICMG_FRONT_BLADE";
            break;
        case SAHPI_ENT_SYSTEM_INVENTORY_DEVICE:
            txt = L"SYSTEM_INVENTORY_DEVICE";
            break;
        case SAHPI_ENT_FILTRATION_UNIT:
            txt = L"FILTRATION_UNIT";
            break;
        case SAHPI_ENT_AMC:
            txt = L"AMC";
            break;
        case SAHPI_ENT_BMC:
            txt = L"BMC";
            break;
        case SAHPI_ENT_IPMC:
            txt = L"IPMC";
            break;
        case SAHPI_ENT_MMC:
            txt = L"MMC";
            break;
        case SAHPI_ENT_SHMC:
            txt = L"SHMC";
            break;
        case SAHPI_ENT_CPLD:
            txt = L"CPLD";
            break;
        case SAHPI_ENT_EPLD:
            txt = L"EPLD";
            break;
        case SAHPI_ENT_FPGA:
            txt = L"FPGA";
            break;
        case SAHPI_ENT_DASD:
            txt = L"DASD";
            break;
        case SAHPI_ENT_NIC:
            txt = L"NIC";
            break;
        case SAHPI_ENT_DSP:
            txt = L"DSP";
            break;
        case SAHPI_ENT_UCODE:
            txt = L"UCODE";
            break;
        case SAHPI_ENT_NPU:
            txt = L"NPU";
            break;
        case SAHPI_ENT_OEM:
            txt = L"OEM";
            break;
        case SAHPI_ENT_INTERFACE:
            txt = L"INTERFACE";
            break;
        case SAHPI_ENT_MICROTCA_CHASSIS:
            txt = L"MICROTCA_CHASSIS";
            break;
        case SAHPI_ENT_CARRIER:
            txt = L"CARRIER";
            break;
        case SAHPI_ENT_CARRIER_MANAGER:
            txt = L"CARRIER_MANAGER";
            break;
        case SAHPI_ENT_CONFIG_DATA:
            txt = L"CONFIG_DATA";
            break;
        case SAHPI_ENT_INDICATOR:
            txt = L"INDICATOR";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiSensorTypeT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_TEMPERATURE:
            txt = L"TEMPERATURE";
            break;
        case SAHPI_VOLTAGE:
            txt = L"VOLTAGE";
            break;
        case SAHPI_CURRENT:
            txt = L"CURRENT";
            break;
        case SAHPI_FAN:
            txt = L"FAN";
            break;
        case SAHPI_PHYSICAL_SECURITY:
            txt = L"PHYSICAL_SECURITY";
            break;
        case SAHPI_PLATFORM_VIOLATION:
            txt = L"PLATFORM_VIOLATION";
            break;
        case SAHPI_PROCESSOR:
            txt = L"PROCESSOR";
            break;
        case SAHPI_POWER_SUPPLY:
            txt = L"POWER_SUPPLY";
            break;
        case SAHPI_POWER_UNIT:
            txt = L"POWER_UNIT";
            break;
        case SAHPI_COOLING_DEVICE:
            txt = L"COOLING_DEVICE";
            break;
        case SAHPI_OTHER_UNITS_BASED_SENSOR:
            txt = L"OTHER_UNITS_BASED_SENSOR";
            break;
        case SAHPI_MEMORY:
            txt = L"MEMORY";
            break;
        case SAHPI_DRIVE_SLOT:
            txt = L"DRIVE_SLOT";
            break;
        case SAHPI_POST_MEMORY_RESIZE:
            txt = L"POST_MEMORY_RESIZE";
            break;
        case SAHPI_SYSTEM_FW_PROGRESS:
            txt = L"SYSTEM_FW_PROGRESS";
            break;
        case SAHPI_EVENT_LOGGING_DISABLED:
            txt = L"EVENT_LOGGING_DISABLED";
            break;
        case SAHPI_RESERVED1:
            txt = L"RESERVED1";
            break;
        case SAHPI_SYSTEM_EVENT:
            txt = L"SYSTEM_EVENT";
            break;
        case SAHPI_CRITICAL_INTERRUPT:
            txt = L"CRITICAL_INTERRUPT";
            break;
        case SAHPI_BUTTON:
            txt = L"BUTTON";
            break;
        case SAHPI_MODULE_BOARD:
            txt = L"MODULE_BOARD";
            break;
        case SAHPI_MICROCONTROLLER_COPROCESSOR:
            txt = L"MICROCONTROLLER_COPROCESSOR";
            break;
        case SAHPI_ADDIN_CARD:
            txt = L"ADDIN_CARD";
            break;
        case SAHPI_CHASSIS:
            txt = L"CHASSIS";
            break;
        case SAHPI_CHIP_SET:
            txt = L"CHIP_SET";
            break;
        case SAHPI_OTHER_FRU:
            txt = L"OTHER_FRU";
            break;
        case SAHPI_CABLE_INTERCONNECT:
            txt = L"CABLE_INTERCONNECT";
            break;
        case SAHPI_TERMINATOR:
            txt = L"TERMINATOR";
            break;
        case SAHPI_SYSTEM_BOOT_INITIATED:
            txt = L"SYSTEM_BOOT_INITIATED";
            break;
        case SAHPI_BOOT_ERROR:
            txt = L"BOOT_ERROR";
            break;
        case SAHPI_OS_BOOT:
            txt = L"OS_BOOT";
            break;
        case SAHPI_OS_CRITICAL_STOP:
            txt = L"OS_CRITICAL_STOP";
            break;
        case SAHPI_SLOT_CONNECTOR:
            txt = L"SLOT_CONNECTOR";
            break;
        case SAHPI_SYSTEM_ACPI_POWER_STATE:
            txt = L"SYSTEM_ACPI_POWER_STATE";
            break;
        case SAHPI_RESERVED2:
            txt = L"RESERVED2";
            break;
        case SAHPI_PLATFORM_ALERT:
            txt = L"PLATFORM_ALERT";
            break;
        case SAHPI_ENTITY_PRESENCE:
            txt = L"ENTITY_PRESENCE";
            break;
        case SAHPI_MONITOR_ASIC_IC:
            txt = L"MONITOR_ASIC_IC";
            break;
        case SAHPI_LAN:
            txt = L"LAN";
            break;
        case SAHPI_MANAGEMENT_SUBSYSTEM_HEALTH:
            txt = L"MANAGEMENT_SUBSYSTEM_HEALTH";
            break;
        case SAHPI_BATTERY:
            txt = L"BATTERY";
            break;
        case SAHPI_SESSION_AUDIT:
            txt = L"SESSION_AUDIT";
            break;
        case SAHPI_VERSION_CHANGE:
            txt = L"VERSION_CHANGE";
            break;
        case SAHPI_OPERATIONAL:
            txt = L"OPERATIONAL";
            break;
        case SAHPI_COMM_CHANNEL_LINK_STATE:
            txt = L"COMM_CHANNEL_LINK_STATE";
            break;
        case SAHPI_MANAGEMENT_BUS_STATE:
            txt = L"MANAGEMENT_BUS_STATE";
            break;
        case SAHPI_COMM_CHANNEL_BUS_STATE:
            txt = L"COMM_CHANNEL_BUS_STATE";
            break;
        case SAHPI_CONFIG_DATA:
            txt = L"CONFIG_DATA";
            break;
        case SAHPI_POWER_BUDGET:
            txt = L"POWER_BUDGET";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiSensorReadingTypeT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_SENSOR_READING_TYPE_INT64:
            txt = L"INT64";
            break;
        case SAHPI_SENSOR_READING_TYPE_UINT64:
            txt = L"UINT64";
            break;
        case SAHPI_SENSOR_READING_TYPE_FLOAT64:
            txt = L"FLOAT64";
            break;
        case SAHPI_SENSOR_READING_TYPE_BUFFER:
            txt = L"BUFFER";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiSensorEventMaskActionT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_SENS_ADD_EVENTS_TO_MASKS:
            txt = L"ADD_EVENTS_TO_MASKS";
            break;
        case SAHPI_SENS_REMOVE_EVENTS_FROM_MASKS:
            txt = L"REMOVE_EVENTS_FROM_MASKS";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiSensorUnitsT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_SU_UNSPECIFIED:
            txt = L"UNSPECIFIED";
            break;
        case SAHPI_SU_DEGREES_C:
            txt = L"DEGREES_C";
            break;
        case SAHPI_SU_DEGREES_F:
            txt = L"DEGREES_F";
            break;
        case SAHPI_SU_DEGREES_K:
            txt = L"DEGREES_K";
            break;
        case SAHPI_SU_VOLTS:
            txt = L"VOLTS";
            break;
        case SAHPI_SU_AMPS:
            txt = L"AMPS";
            break;
        case SAHPI_SU_WATTS:
            txt = L"WATTS";
            break;
        case SAHPI_SU_JOULES:
            txt = L"JOULES";
            break;
        case SAHPI_SU_COULOMBS:
            txt = L"COULOMBS";
            break;
        case SAHPI_SU_VA:
            txt = L"VA";
            break;
        case SAHPI_SU_NITS:
            txt = L"NITS";
            break;
        case SAHPI_SU_LUMEN:
            txt = L"LUMEN";
            break;
        case SAHPI_SU_LUX:
            txt = L"LUX";
            break;
        case SAHPI_SU_CANDELA:
            txt = L"CANDELA";
            break;
        case SAHPI_SU_KPA:
            txt = L"KPA";
            break;
        case SAHPI_SU_PSI:
            txt = L"PSI";
            break;
        case SAHPI_SU_NEWTON:
            txt = L"NEWTON";
            break;
        case SAHPI_SU_CFM:
            txt = L"CFM";
            break;
        case SAHPI_SU_RPM:
            txt = L"RPM";
            break;
        case SAHPI_SU_HZ:
            txt = L"HZ";
            break;
        case SAHPI_SU_MICROSECOND:
            txt = L"MICROSECOND";
            break;
        case SAHPI_SU_MILLISECOND:
            txt = L"MILLISECOND";
            break;
        case SAHPI_SU_SECOND:
            txt = L"SECOND";
            break;
        case SAHPI_SU_MINUTE:
            txt = L"MINUTE";
            break;
        case SAHPI_SU_HOUR:
            txt = L"HOUR";
            break;
        case SAHPI_SU_DAY:
            txt = L"DAY";
            break;
        case SAHPI_SU_WEEK:
            txt = L"WEEK";
            break;
        case SAHPI_SU_MIL:
            txt = L"MIL";
            break;
        case SAHPI_SU_INCHES:
            txt = L"INCHES";
            break;
        case SAHPI_SU_FEET:
            txt = L"FEET";
            break;
        case SAHPI_SU_CU_IN:
            txt = L"CU_IN";
            break;
        case SAHPI_SU_CU_FEET:
            txt = L"CU_FEET";
            break;
        case SAHPI_SU_MM:
            txt = L"MM";
            break;
        case SAHPI_SU_CM:
            txt = L"CM";
            break;
        case SAHPI_SU_M:
            txt = L"M";
            break;
        case SAHPI_SU_CU_CM:
            txt = L"CU_CM";
            break;
        case SAHPI_SU_CU_M:
            txt = L"CU_M";
            break;
        case SAHPI_SU_LITERS:
            txt = L"LITERS";
            break;
        case SAHPI_SU_FLUID_OUNCE:
            txt = L"FLUID_OUNCE";
            break;
        case SAHPI_SU_RADIANS:
            txt = L"RADIANS";
            break;
        case SAHPI_SU_STERADIANS:
            txt = L"STERADIANS";
            break;
        case SAHPI_SU_REVOLUTIONS:
            txt = L"REVOLUTIONS";
            break;
        case SAHPI_SU_CYCLES:
            txt = L"CYCLES";
            break;
        case SAHPI_SU_GRAVITIES:
            txt = L"GRAVITIES";
            break;
        case SAHPI_SU_OUNCE:
            txt = L"OUNCE";
            break;
        case SAHPI_SU_POUND:
            txt = L"POUND";
            break;
        case SAHPI_SU_FT_LB:
            txt = L"FT_LB";
            break;
        case SAHPI_SU_OZ_IN:
            txt = L"OZ_IN";
            break;
        case SAHPI_SU_GAUSS:
            txt = L"GAUSS";
            break;
        case SAHPI_SU_GILBERTS:
            txt = L"GILBERTS";
            break;
        case SAHPI_SU_HENRY:
            txt = L"HENRY";
            break;
        case SAHPI_SU_MILLIHENRY:
            txt = L"MILLIHENRY";
            break;
        case SAHPI_SU_FARAD:
            txt = L"FARAD";
            break;
        case SAHPI_SU_MICROFARAD:
            txt = L"MICROFARAD";
            break;
        case SAHPI_SU_OHMS:
            txt = L"OHMS";
            break;
        case SAHPI_SU_SIEMENS:
            txt = L"SIEMENS";
            break;
        case SAHPI_SU_MOLE:
            txt = L"MOLE";
            break;
        case SAHPI_SU_BECQUEREL:
            txt = L"BECQUEREL";
            break;
        case SAHPI_SU_PPM:
            txt = L"PPM";
            break;
        case SAHPI_SU_RESERVED:
            txt = L"RESERVED";
            break;
        case SAHPI_SU_DECIBELS:
            txt = L"DECIBELS";
            break;
        case SAHPI_SU_DBA:
            txt = L"DBA";
            break;
        case SAHPI_SU_DBC:
            txt = L"DBC";
            break;
        case SAHPI_SU_GRAY:
            txt = L"GRAY";
            break;
        case SAHPI_SU_SIEVERT:
            txt = L"SIEVERT";
            break;
        case SAHPI_SU_COLOR_TEMP_DEG_K:
            txt = L"COLOR_TEMP_DEG_K";
            break;
        case SAHPI_SU_BIT:
            txt = L"BIT";
            break;
        case SAHPI_SU_KILOBIT:
            txt = L"KILOBIT";
            break;
        case SAHPI_SU_MEGABIT:
            txt = L"MEGABIT";
            break;
        case SAHPI_SU_GIGABIT:
            txt = L"GIGABIT";
            break;
        case SAHPI_SU_BYTE:
            txt = L"BYTE";
            break;
        case SAHPI_SU_KILOBYTE:
            txt = L"KILOBYTE";
            break;
        case SAHPI_SU_MEGABYTE:
            txt = L"MEGABYTE";
            break;
        case SAHPI_SU_GIGABYTE:
            txt = L"GIGABYTE";
            break;
        case SAHPI_SU_WORD:
            txt = L"WORD";
            break;
        case SAHPI_SU_DWORD:
            txt = L"DWORD";
            break;
        case SAHPI_SU_QWORD:
            txt = L"QWORD";
            break;
        case SAHPI_SU_LINE:
            txt = L"LINE";
            break;
        case SAHPI_SU_HIT:
            txt = L"HIT";
            break;
        case SAHPI_SU_MISS:
            txt = L"MISS";
            break;
        case SAHPI_SU_RETRY:
            txt = L"RETRY";
            break;
        case SAHPI_SU_RESET:
            txt = L"RESET";
            break;
        case SAHPI_SU_OVERRUN:
            txt = L"OVERRUN";
            break;
        case SAHPI_SU_UNDERRUN:
            txt = L"UNDERRUN";
            break;
        case SAHPI_SU_COLLISION:
            txt = L"COLLISION";
            break;
        case SAHPI_SU_PACKETS:
            txt = L"PACKETS";
            break;
        case SAHPI_SU_MESSAGES:
            txt = L"MESSAGES";
            break;
        case SAHPI_SU_CHARACTERS:
            txt = L"CHARACTERS";
            break;
        case SAHPI_SU_ERRORS:
            txt = L"ERRORS";
            break;
        case SAHPI_SU_CORRECTABLE_ERRORS:
            txt = L"CORRECTABLE_ERRORS";
            break;
        case SAHPI_SU_UNCORRECTABLE_ERRORS:
            txt = L"UNCORRECTABLE_ERRORS";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiSensorModUnitUseT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_SMUU_NONE:
            txt = L"NONE";
            break;
        case SAHPI_SMUU_BASIC_OVER_MODIFIER:
            txt = L"BASIC_OVER_MODIFIER";
            break;
        case SAHPI_SMUU_BASIC_TIMES_MODIFIER:
            txt = L"BASIC_TIMES_MODIFIER";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiSensorEventCtrlT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_SEC_PER_EVENT:
            txt = L"PER_EVENT";
            break;
        case SAHPI_SEC_READ_ONLY_MASKS:
            txt = L"READ_ONLY_MASKS";
            break;
        case SAHPI_SEC_READ_ONLY:
            txt = L"READ_ONLY";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiCtrlTypeT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_CTRL_TYPE_DIGITAL:
            txt = L"DIGITAL";
            break;
        case SAHPI_CTRL_TYPE_DISCRETE:
            txt = L"DISCRETE";
            break;
        case SAHPI_CTRL_TYPE_ANALOG:
            txt = L"ANALOG";
            break;
        case SAHPI_CTRL_TYPE_STREAM:
            txt = L"STREAM";
            break;
        case SAHPI_CTRL_TYPE_TEXT:
            txt = L"TEXT";
            break;
        case SAHPI_CTRL_TYPE_OEM:
            txt = L"OEM";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiCtrlStateDigitalT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_CTRL_STATE_OFF:
            txt = L"OFF";
            break;
        case SAHPI_CTRL_STATE_ON:
            txt = L"ON";
            break;
        case SAHPI_CTRL_STATE_PULSE_OFF:
            txt = L"PULSE_OFF";
            break;
        case SAHPI_CTRL_STATE_PULSE_ON:
            txt = L"PULSE_ON";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiCtrlModeT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_CTRL_MODE_AUTO:
            txt = L"AUTO";
            break;
        case SAHPI_CTRL_MODE_MANUAL:
            txt = L"MANUAL";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiCtrlOutputTypeT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_CTRL_GENERIC:
            txt = L"GENERIC";
            break;
        case SAHPI_CTRL_LED:
            txt = L"LED";
            break;
        case SAHPI_CTRL_FAN_SPEED:
            txt = L"FAN_SPEED";
            break;
        case SAHPI_CTRL_DRY_CONTACT_CLOSURE:
            txt = L"DRY_CONTACT_CLOSURE";
            break;
        case SAHPI_CTRL_POWER_SUPPLY_INHIBIT:
            txt = L"POWER_SUPPLY_INHIBIT";
            break;
        case SAHPI_CTRL_AUDIBLE:
            txt = L"AUDIBLE";
            break;
        case SAHPI_CTRL_FRONT_PANEL_LOCKOUT:
            txt = L"FRONT_PANEL_LOCKOUT";
            break;
        case SAHPI_CTRL_POWER_INTERLOCK:
            txt = L"POWER_INTERLOCK";
            break;
        case SAHPI_CTRL_POWER_STATE:
            txt = L"POWER_STATE";
            break;
        case SAHPI_CTRL_LCD_DISPLAY:
            txt = L"LCD_DISPLAY";
            break;
        case SAHPI_CTRL_OEM:
            txt = L"OEM";
            break;
        case SAHPI_CTRL_GENERIC_ADDRESS:
            txt = L"GENERIC_ADDRESS";
            break;
        case SAHPI_CTRL_IP_ADDRESS:
            txt = L"IP_ADDRESS";
            break;
        case SAHPI_CTRL_RESOURCE_ID:
            txt = L"RESOURCE_ID";
            break;
        case SAHPI_CTRL_POWER_BUDGET:
            txt = L"POWER_BUDGET";
            break;
        case SAHPI_CTRL_ACTIVATE:
            txt = L"ACTIVATE";
            break;
        case SAHPI_CTRL_RESET:
            txt = L"RESET";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiIdrAreaTypeT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_IDR_AREATYPE_INTERNAL_USE:
            txt = L"INTERNAL_USE";
            break;
        case SAHPI_IDR_AREATYPE_CHASSIS_INFO:
            txt = L"CHASSIS_INFO";
            break;
        case SAHPI_IDR_AREATYPE_BOARD_INFO:
            txt = L"BOARD_INFO";
            break;
        case SAHPI_IDR_AREATYPE_PRODUCT_INFO:
            txt = L"PRODUCT_INFO";
            break;
        case SAHPI_IDR_AREATYPE_OEM:
            txt = L"OEM";
            break;
        case SAHPI_IDR_AREATYPE_UNSPECIFIED:
            txt = L"UNSPECIFIED";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiIdrFieldTypeT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_IDR_FIELDTYPE_CHASSIS_TYPE:
            txt = L"CHASSIS_TYPE";
            break;
        case SAHPI_IDR_FIELDTYPE_MFG_DATETIME:
            txt = L"MFG_DATETIME";
            break;
        case SAHPI_IDR_FIELDTYPE_MANUFACTURER:
            txt = L"MANUFACTURER";
            break;
        case SAHPI_IDR_FIELDTYPE_PRODUCT_NAME:
            txt = L"PRODUCT_NAME";
            break;
        case SAHPI_IDR_FIELDTYPE_PRODUCT_VERSION:
            txt = L"PRODUCT_VERSION";
            break;
        case SAHPI_IDR_FIELDTYPE_SERIAL_NUMBER:
            txt = L"SERIAL_NUMBER";
            break;
        case SAHPI_IDR_FIELDTYPE_PART_NUMBER:
            txt = L"PART_NUMBER";
            break;
        case SAHPI_IDR_FIELDTYPE_FILE_ID:
            txt = L"FILE_ID";
            break;
        case SAHPI_IDR_FIELDTYPE_ASSET_TAG:
            txt = L"ASSET_TAG";
            break;
        case SAHPI_IDR_FIELDTYPE_CUSTOM:
            txt = L"CUSTOM";
            break;
        case SAHPI_IDR_FIELDTYPE_UNSPECIFIED:
            txt = L"UNSPECIFIED";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiWatchdogActionT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_WA_NO_ACTION:
            txt = L"NO_ACTION";
            break;
        case SAHPI_WA_RESET:
            txt = L"RESET";
            break;
        case SAHPI_WA_POWER_DOWN:
            txt = L"POWER_DOWN";
            break;
        case SAHPI_WA_POWER_CYCLE:
            txt = L"POWER_CYCLE";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiWatchdogActionEventT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_WAE_NO_ACTION:
            txt = L"NO_ACTION";
            break;
        case SAHPI_WAE_RESET:
            txt = L"RESET";
            break;
        case SAHPI_WAE_POWER_DOWN:
            txt = L"POWER_DOWN";
            break;
        case SAHPI_WAE_POWER_CYCLE:
            txt = L"POWER_CYCLE";
            break;
        case SAHPI_WAE_TIMER_INT:
            txt = L"TIMER_INT";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiWatchdogPretimerInterruptT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_WPI_NONE:
            txt = L"NONE";
            break;
        case SAHPI_WPI_SMI:
            txt = L"SMI";
            break;
        case SAHPI_WPI_NMI:
            txt = L"NMI";
            break;
        case SAHPI_WPI_MESSAGE_INTERRUPT:
            txt = L"MESSAGE_INTERRUPT";
            break;
        case SAHPI_WPI_OEM:
            txt = L"OEM";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiWatchdogTimerUseT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_WTU_NONE:
            txt = L"NONE";
            break;
        case SAHPI_WTU_BIOS_FRB2:
            txt = L"BIOS_FRB2";
            break;
        case SAHPI_WTU_BIOS_POST:
            txt = L"BIOS_POST";
            break;
        case SAHPI_WTU_OS_LOAD:
            txt = L"OS_LOAD";
            break;
        case SAHPI_WTU_SMS_OS:
            txt = L"SMS_OS";
            break;
        case SAHPI_WTU_OEM:
            txt = L"OEM";
            break;
        case SAHPI_WTU_UNSPECIFIED:
            txt = L"UNSPECIFIED";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiDimiTestServiceImpactT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_DIMITEST_NONDEGRADING:
            txt = L"NONDEGRADING";
            break;
        case SAHPI_DIMITEST_DEGRADING:
            txt = L"DEGRADING";
            break;
        case SAHPI_DIMITEST_VENDOR_DEFINED_LEVEL:
            txt = L"VENDOR_DEFINED_LEVEL";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiDimiTestRunStatusT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_DIMITEST_STATUS_NOT_RUN:
            txt = L"NOT_RUN";
            break;
        case SAHPI_DIMITEST_STATUS_FINISHED_NO_ERRORS:
            txt = L"FINISHED_NO_ERRORS";
            break;
        case SAHPI_DIMITEST_STATUS_FINISHED_ERRORS:
            txt = L"FINISHED_ERRORS";
            break;
        case SAHPI_DIMITEST_STATUS_CANCELED:
            txt = L"CANCELED";
            break;
        case SAHPI_DIMITEST_STATUS_RUNNING:
            txt = L"RUNNING";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiDimiTestErrCodeT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_DIMITEST_STATUSERR_NOERR:
            txt = L"NOERR";
            break;
        case SAHPI_DIMITEST_STATUSERR_RUNERR:
            txt = L"RUNERR";
            break;
        case SAHPI_DIMITEST_STATUSERR_UNDEF:
            txt = L"UNDEF";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiDimiTestParamTypeT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_DIMITEST_PARAM_TYPE_BOOLEAN:
            txt = L"BOOLEAN";
            break;
        case SAHPI_DIMITEST_PARAM_TYPE_INT32:
            txt = L"INT32";
            break;
        case SAHPI_DIMITEST_PARAM_TYPE_FLOAT64:
            txt = L"FLOAT64";
            break;
        case SAHPI_DIMITEST_PARAM_TYPE_TEXT:
            txt = L"TEXT";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiDimiReadyT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_DIMI_READY:
            txt = L"READY";
            break;
        case SAHPI_DIMI_WRONG_STATE:
            txt = L"WRONG_STATE";
            break;
        case SAHPI_DIMI_BUSY:
            txt = L"BUSY";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiFumiSpecInfoTypeT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_FUMI_SPEC_INFO_NONE:
            txt = L"NONE";
            break;
        case SAHPI_FUMI_SPEC_INFO_SAF_DEFINED:
            txt = L"SAF_DEFINED";
            break;
        case SAHPI_FUMI_SPEC_INFO_OEM_DEFINED:
            txt = L"OEM_DEFINED";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiFumiSafDefinedSpecIdT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_FUMI_SPEC_HPM1:
            txt = L"HPM1";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiFumiServiceImpactT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_FUMI_PROCESS_NONDEGRADING:
            txt = L"NONDEGRADING";
            break;
        case SAHPI_FUMI_PROCESS_DEGRADING:
            txt = L"DEGRADING";
            break;
        case SAHPI_FUMI_PROCESS_VENDOR_DEFINED_IMPACT_LEVEL:
            txt = L"VENDOR_DEFINED_IMPACT_LEVEL";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiFumiSourceStatusT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_FUMI_SRC_VALID:
            txt = L"VALID";
            break;
        case SAHPI_FUMI_SRC_PROTOCOL_NOT_SUPPORTED:
            txt = L"PROTOCOL_NOT_SUPPORTED";
            break;
        case SAHPI_FUMI_SRC_UNREACHABLE:
            txt = L"UNREACHABLE";
            break;
        case SAHPI_FUMI_SRC_VALIDATION_NOT_STARTED:
            txt = L"VALIDATION_NOT_STARTED";
            break;
        case SAHPI_FUMI_SRC_VALIDATION_INITIATED:
            txt = L"VALIDATION_INITIATED";
            break;
        case SAHPI_FUMI_SRC_VALIDATION_FAIL:
            txt = L"VALIDATION_FAIL";
            break;
        case SAHPI_FUMI_SRC_TYPE_MISMATCH:
            txt = L"TYPE_MISMATCH";
            break;
        case SAHPI_FUMI_SRC_INVALID:
            txt = L"INVALID";
            break;
        case SAHPI_FUMI_SRC_VALIDITY_UNKNOWN:
            txt = L"VALIDITY_UNKNOWN";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiFumiBankStateT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_FUMI_BANK_VALID:
            txt = L"VALID";
            break;
        case SAHPI_FUMI_BANK_UPGRADE_IN_PROGRESS:
            txt = L"UPGRADE_IN_PROGRESS";
            break;
        case SAHPI_FUMI_BANK_CORRUPTED:
            txt = L"CORRUPTED";
            break;
        case SAHPI_FUMI_BANK_ACTIVE:
            txt = L"ACTIVE";
            break;
        case SAHPI_FUMI_BANK_BUSY:
            txt = L"BUSY";
            break;
        case SAHPI_FUMI_BANK_UNKNOWN:
            txt = L"UNKNOWN";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiFumiUpgradeStatusT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_FUMI_OPERATION_NOTSTARTED:
            txt = L"OPERATION_NOTSTARTED";
            break;
        case SAHPI_FUMI_SOURCE_VALIDATION_INITIATED:
            txt = L"SOURCE_VALIDATION_INITIATED";
            break;
        case SAHPI_FUMI_SOURCE_VALIDATION_FAILED:
            txt = L"SOURCE_VALIDATION_FAILED";
            break;
        case SAHPI_FUMI_SOURCE_VALIDATION_DONE:
            txt = L"SOURCE_VALIDATION_DONE";
            break;
        case SAHPI_FUMI_SOURCE_VALIDATION_CANCELLED:
            txt = L"SOURCE_VALIDATION_CANCELLED";
            break;
        case SAHPI_FUMI_INSTALL_INITIATED:
            txt = L"INSTALL_INITIATED";
            break;
        case SAHPI_FUMI_INSTALL_FAILED_ROLLBACK_NEEDED:
            txt = L"INSTALL_FAILED_ROLLBACK_NEEDED";
            break;
        case SAHPI_FUMI_INSTALL_FAILED_ROLLBACK_INITIATED:
            txt = L"INSTALL_FAILED_ROLLBACK_INITIATED";
            break;
        case SAHPI_FUMI_INSTALL_FAILED_ROLLBACK_NOT_POSSIBLE:
            txt = L"INSTALL_FAILED_ROLLBACK_NOT_POSSIBLE";
            break;
        case SAHPI_FUMI_INSTALL_DONE:
            txt = L"INSTALL_DONE";
            break;
        case SAHPI_FUMI_INSTALL_CANCELLED:
            txt = L"INSTALL_CANCELLED";
            break;
        case SAHPI_FUMI_ROLLBACK_INITIATED:
            txt = L"ROLLBACK_INITIATED";
            break;
        case SAHPI_FUMI_ROLLBACK_FAILED:
            txt = L"ROLLBACK_FAILED";
            break;
        case SAHPI_FUMI_ROLLBACK_DONE:
            txt = L"ROLLBACK_DONE";
            break;
        case SAHPI_FUMI_ROLLBACK_CANCELLED:
            txt = L"ROLLBACK_CANCELLED";
            break;
        case SAHPI_FUMI_BACKUP_INITIATED:
            txt = L"BACKUP_INITIATED";
            break;
        case SAHPI_FUMI_BACKUP_FAILED:
            txt = L"BACKUP_FAILED";
            break;
        case SAHPI_FUMI_BACKUP_DONE:
            txt = L"BACKUP_DONE";
            break;
        case SAHPI_FUMI_BACKUP_CANCELLED:
            txt = L"BACKUP_CANCELLED";
            break;
        case SAHPI_FUMI_BANK_COPY_INITIATED:
            txt = L"BANK_COPY_INITIATED";
            break;
        case SAHPI_FUMI_BANK_COPY_FAILED:
            txt = L"BANK_COPY_FAILED";
            break;
        case SAHPI_FUMI_BANK_COPY_DONE:
            txt = L"BANK_COPY_DONE";
            break;
        case SAHPI_FUMI_BANK_COPY_CANCELLED:
            txt = L"BANK_COPY_CANCELLED";
            break;
        case SAHPI_FUMI_TARGET_VERIFY_INITIATED:
            txt = L"TARGET_VERIFY_INITIATED";
            break;
        case SAHPI_FUMI_TARGET_VERIFY_FAILED:
            txt = L"TARGET_VERIFY_FAILED";
            break;
        case SAHPI_FUMI_TARGET_VERIFY_DONE:
            txt = L"TARGET_VERIFY_DONE";
            break;
        case SAHPI_FUMI_TARGET_VERIFY_CANCELLED:
            txt = L"TARGET_VERIFY_CANCELLED";
            break;
        case SAHPI_FUMI_ACTIVATE_INITIATED:
            txt = L"ACTIVATE_INITIATED";
            break;
        case SAHPI_FUMI_ACTIVATE_FAILED_ROLLBACK_NEEDED:
            txt = L"ACTIVATE_FAILED_ROLLBACK_NEEDED";
            break;
        case SAHPI_FUMI_ACTIVATE_FAILED_ROLLBACK_INITIATED:
            txt = L"ACTIVATE_FAILED_ROLLBACK_INITIATED";
            break;
        case SAHPI_FUMI_ACTIVATE_FAILED_ROLLBACK_NOT_POSSIBLE:
            txt = L"ACTIVATE_FAILED_ROLLBACK_NOT_POSSIBLE";
            break;
        case SAHPI_FUMI_ACTIVATE_DONE:
            txt = L"ACTIVATE_DONE";
            break;
        case SAHPI_FUMI_ACTIVATE_CANCELLED:
            txt = L"ACTIVATE_CANCELLED";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiHsIndicatorStateT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_HS_INDICATOR_OFF:
            txt = L"OFF";
            break;
        case SAHPI_HS_INDICATOR_ON:
            txt = L"ON";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiHsActionT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_HS_ACTION_INSERTION:
            txt = L"INSERTION";
            break;
        case SAHPI_HS_ACTION_EXTRACTION:
            txt = L"EXTRACTION";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiHsStateT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_HS_STATE_INACTIVE:
            txt = L"INACTIVE";
            break;
        case SAHPI_HS_STATE_INSERTION_PENDING:
            txt = L"INSERTION_PENDING";
            break;
        case SAHPI_HS_STATE_ACTIVE:
            txt = L"ACTIVE";
            break;
        case SAHPI_HS_STATE_EXTRACTION_PENDING:
            txt = L"EXTRACTION_PENDING";
            break;
        case SAHPI_HS_STATE_NOT_PRESENT:
            txt = L"NOT_PRESENT";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiHsCauseOfStateChangeT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_HS_CAUSE_AUTO_POLICY:
            txt = L"AUTO_POLICY";
            break;
        case SAHPI_HS_CAUSE_EXT_SOFTWARE:
            txt = L"EXT_SOFTWARE";
            break;
        case SAHPI_HS_CAUSE_OPERATOR_INIT:
            txt = L"OPERATOR_INIT";
            break;
        case SAHPI_HS_CAUSE_USER_UPDATE:
            txt = L"USER_UPDATE";
            break;
        case SAHPI_HS_CAUSE_UNEXPECTED_DEACTIVATION:
            txt = L"UNEXPECTED_DEACTIVATION";
            break;
        case SAHPI_HS_CAUSE_SURPRISE_EXTRACTION:
            txt = L"SURPRISE_EXTRACTION";
            break;
        case SAHPI_HS_CAUSE_EXTRACTION_UPDATE:
            txt = L"EXTRACTION_UPDATE";
            break;
        case SAHPI_HS_CAUSE_HARDWARE_FAULT:
            txt = L"HARDWARE_FAULT";
            break;
        case SAHPI_HS_CAUSE_CONTAINING_FRU:
            txt = L"CONTAINING_FRU";
            break;
        case SAHPI_HS_CAUSE_UNKNOWN:
            txt = L"UNKNOWN";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiSeverityT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_CRITICAL:
            txt = L"CRITICAL";
            break;
        case SAHPI_MAJOR:
            txt = L"MAJOR";
            break;
        case SAHPI_MINOR:
            txt = L"MINOR";
            break;
        case SAHPI_INFORMATIONAL:
            txt = L"INFORMATIONAL";
            break;
        case SAHPI_OK:
            txt = L"OK";
            break;
        case SAHPI_DEBUG:
            txt = L"DEBUG";
            break;
        case SAHPI_ALL_SEVERITIES:
            txt = L"ALL_SEVERITIES";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiResourceEventTypeT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_RESE_RESOURCE_FAILURE:
            txt = L"RESOURCE_FAILURE";
            break;
        case SAHPI_RESE_RESOURCE_RESTORED:
            txt = L"RESOURCE_RESTORED";
            break;
        case SAHPI_RESE_RESOURCE_ADDED:
            txt = L"RESOURCE_ADDED";
            break;
        case SAHPI_RESE_RESOURCE_REMOVED:
            txt = L"RESOURCE_REMOVED";
            break;
        case SAHPI_RESE_RESOURCE_INACCESSIBLE:
            txt = L"RESOURCE_INACCESSIBLE";
            break;
        case SAHPI_RESE_RESOURCE_UPDATED:
            txt = L"RESOURCE_UPDATED";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiDomainEventTypeT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_DOMAIN_REF_ADDED:
            txt = L"DOMAIN_REF_ADDED";
            break;
        case SAHPI_DOMAIN_REF_REMOVED:
            txt = L"DOMAIN_REF_REMOVED";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiSwEventTypeT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_HPIE_AUDIT:
            txt = L"AUDIT";
            break;
        case SAHPI_HPIE_STARTUP:
            txt = L"STARTUP";
            break;
        case SAHPI_HPIE_OTHER:
            txt = L"OTHER";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiEventTypeT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_ET_RESOURCE:
            txt = L"RESOURCE";
            break;
        case SAHPI_ET_DOMAIN:
            txt = L"DOMAIN";
            break;
        case SAHPI_ET_SENSOR:
            txt = L"SENSOR";
            break;
        case SAHPI_ET_SENSOR_ENABLE_CHANGE:
            txt = L"SENSOR_ENABLE_CHANGE";
            break;
        case SAHPI_ET_HOTSWAP:
            txt = L"HOTSWAP";
            break;
        case SAHPI_ET_WATCHDOG:
            txt = L"WATCHDOG";
            break;
        case SAHPI_ET_HPI_SW:
            txt = L"HPI_SW";
            break;
        case SAHPI_ET_OEM:
            txt = L"OEM";
            break;
        case SAHPI_ET_USER:
            txt = L"USER";
            break;
        case SAHPI_ET_DIMI:
            txt = L"DIMI";
            break;
        case SAHPI_ET_DIMI_UPDATE:
            txt = L"DIMI_UPDATE";
            break;
        case SAHPI_ET_FUMI:
            txt = L"FUMI";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiStatusCondTypeT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_STATUS_COND_TYPE_SENSOR:
            txt = L"SENSOR";
            break;
        case SAHPI_STATUS_COND_TYPE_RESOURCE:
            txt = L"RESOURCE";
            break;
        case SAHPI_STATUS_COND_TYPE_OEM:
            txt = L"OEM";
            break;
        case SAHPI_STATUS_COND_TYPE_USER:
            txt = L"USER";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiAnnunciatorModeT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_ANNUNCIATOR_MODE_AUTO:
            txt = L"AUTO";
            break;
        case SAHPI_ANNUNCIATOR_MODE_USER:
            txt = L"USER";
            break;
        case SAHPI_ANNUNCIATOR_MODE_SHARED:
            txt = L"SHARED";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiAnnunciatorTypeT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_ANNUNCIATOR_TYPE_LED:
            txt = L"LED";
            break;
        case SAHPI_ANNUNCIATOR_TYPE_DRY_CONTACT_CLOSURE:
            txt = L"DRY_CONTACT_CLOSURE";
            break;
        case SAHPI_ANNUNCIATOR_TYPE_AUDIBLE:
            txt = L"AUDIBLE";
            break;
        case SAHPI_ANNUNCIATOR_TYPE_LCD_DISPLAY:
            txt = L"LCD_DISPLAY";
            break;
        case SAHPI_ANNUNCIATOR_TYPE_MESSAGE:
            txt = L"MESSAGE";
            break;
        case SAHPI_ANNUNCIATOR_TYPE_COMPOSITE:
            txt = L"COMPOSITE";
            break;
        case SAHPI_ANNUNCIATOR_TYPE_OEM:
            txt = L"OEM";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiRdrTypeT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_NO_RECORD:
            txt = L"NO_RECORD";
            break;
        case SAHPI_CTRL_RDR:
            txt = L"CTRL_RDR";
            break;
        case SAHPI_SENSOR_RDR:
            txt = L"SENSOR_RDR";
            break;
        case SAHPI_INVENTORY_RDR:
            txt = L"INVENTORY_RDR";
            break;
        case SAHPI_WATCHDOG_RDR:
            txt = L"WATCHDOG_RDR";
            break;
        case SAHPI_ANNUNCIATOR_RDR:
            txt = L"ANNUNCIATOR_RDR";
            break;
        case SAHPI_DIMI_RDR:
            txt = L"DIMI_RDR";
            break;
        case SAHPI_FUMI_RDR:
            txt = L"FUMI_RDR";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiParmActionT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_DEFAULT_PARM:
            txt = L"DEFAULT_PARM";
            break;
        case SAHPI_SAVE_PARM:
            txt = L"SAVE_PARM";
            break;
        case SAHPI_RESTORE_PARM:
            txt = L"RESTORE_PARM";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiResetActionT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_COLD_RESET:
            txt = L"COLD_RESET";
            break;
        case SAHPI_WARM_RESET:
            txt = L"WARM_RESET";
            break;
        case SAHPI_RESET_ASSERT:
            txt = L"RESET_ASSERT";
            break;
        case SAHPI_RESET_DEASSERT:
            txt = L"RESET_DEASSERT";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiPowerStateT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_POWER_OFF:
            txt = L"POWER_OFF";
            break;
        case SAHPI_POWER_ON:
            txt = L"POWER_ON";
            break;
        case SAHPI_POWER_CYCLE:
            txt = L"POWER_CYCLE";
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( SaHpiEventLogOverflowActionT x, std::wstring& txt )
{
    switch ( x ) {
        case SAHPI_EL_OVERFLOW_DROP:
            txt = L"DROP";
            break;
        case SAHPI_EL_OVERFLOW_OVERWRITE:
            txt = L"OVERWRITE";
            break;
        default:
            txt = txt_unknown;
    }
}


/*****************************************************
 * HPI complex type convertors
 ****************************************************/
void ToTxt( const SaHpiTextBufferT& tb, std::wstring& txt )
{
    txt.clear();

    switch ( tb.DataType ) {
        case SAHPI_TL_TYPE_UNICODE:
            {
                unsigned int len = ( tb.DataLength + 1 ) / 2;
                txt.reserve( len );
                for ( unsigned int i = 0; i < len; ++i ) {
                    wchar_t c = ( tb.Data[ 2 * i + 1 ] << 8 ) | tb.Data[ 2 * i ];
                    txt.push_back( c );
                }
            }
            break;

        case SAHPI_TL_TYPE_BCDPLUS:
        case SAHPI_TL_TYPE_ASCII6:
        case SAHPI_TL_TYPE_TEXT:
            txt.reserve( tb.DataLength );
            for ( unsigned int i = 0; i < tb.DataLength; ++i ) {
                txt.push_back( tb.Data[i] );
            }
            break;
        case SAHPI_TL_TYPE_BINARY:
            ToTxt( &tb.Data[0], tb.DataLength, txt );
            break;
        default:
            txt = txt_unknown;
    }
}

void ToTxt( const SaHpiGuidT& guid, std::wstring& txt )
{
    wchar_t out[64];
    swprintf( out,
              sizeof(out) / sizeof(wchar_t),
              L"%02X%02X%02X%02X-%02X%02X-%02X%02X-%02X%02X-%02X%02X%02X%02X%02X%02X",
              guid[0],
              guid[1],
              guid[2],
              guid[3],
              guid[4],
              guid[5],
              guid[6],
              guid[7],
              guid[8],
              guid[9],
              guid[10],
              guid[11],
              guid[12],
              guid[13],
              guid[14],
              guid[15] );
    txt = out;
}

void ToTxt( const SaHpiEntityPathT& ep, std::wstring& txt )
{
    // TODO revisit
    SaHpiEntityPathT unspecified;
    int i;

    txt.clear();

    for( i = 0; i < SAHPI_MAX_ENTITY_PATH; ++i ) {
        if( ep.Entry[i].EntityType == SAHPI_ENT_ROOT ) {
            break;
        }
    }

    memset( &unspecified, 0, sizeof(SaHpiEntityPathT) );
    if( memcmp( &ep, &unspecified, sizeof(SaHpiEntityPathT) ) == 0 ) {
        txt = L"{UNSPECIFIED,0}";
        return;
    }

    for( --i; i >= 0; --i ) {
        wchar_t * entity_type_str = (wchar_t *) HpiLookupEntityType( ep.Entry[i].EntityType );
        wchar_t * entity_location_str = NULL;

        if( entity_type_str == NULL ) {
            wchar_t str[128];
            swprintf( str, ( sizeof(str) / sizeof(wchar_t) ) - 1, L"0x%x", ep.Entry[i].EntityType );
            entity_type_str = str;
        }

        if( entity_location_str == NULL ) {
            wchar_t str[128];
            swprintf( str, ( sizeof(str) / sizeof(wchar_t) ) - 1, L"%u", ep.Entry[i].EntityLocation );
            entity_location_str = str;
        }

        txt += std::wstring( L"{" ) + std::wstring( entity_type_str ) + std::wstring( L"," )
             + std::wstring( entity_location_str ) + std::wstring( L"}" );
    }
}

void ToTxt( const SaHpiNameT& name, std::wstring& txt )
{
    txt.clear();
    txt.reserve( name.Length + 1 );
    for( unsigned int i = 0; i < name.Length; ++i ) {
        txt[i] = name.Value[i];
    }
    txt[name.Length] = 0;
}


FirmwareRevision::FirmwareRevision( SaHpiUint32T _MajorVersion,
                                    SaHpiUint32T _MinorVersion,
                                    SaHpiUint32T _AuxVersion )
    : MajorVersion( _MajorVersion ),
      MinorVersion( _MinorVersion ),
      AuxVersion( _AuxVersion )
{
    // empty
}

void ToTxt( const FirmwareRevision& fw, std::wstring& txt )
{
    wchar_t buf[32];
    swprintf( buf,
              sizeof(buf) / sizeof(wchar_t),
              L"%u.%u.%u",
              fw.MajorVersion,
              fw.MinorVersion,
              fw.AuxVersion );
    txt = buf;
}

void ToTxt( const SaHpiSensorReadingT& sr, std::wstring& txt )
{
    if ( sr.IsSupported == SAHPI_FALSE ) {
        txt = L"Not Supported";
        return;
    }

    std::wstring value;
    switch( sr.Type ) {
        case SAHPI_SENSOR_READING_TYPE_INT64:
            ToTxt( sr.Value.SensorInt64, txt, I64_Dec );
            break;
        case SAHPI_SENSOR_READING_TYPE_UINT64:
            ToTxt( sr.Value.SensorUint64, txt, UI64_Dec );
            break;
        case SAHPI_SENSOR_READING_TYPE_FLOAT64:
            ToTxt( sr.Value.SensorFloat64, txt, F64_FixedPoint );
            break;
        case SAHPI_SENSOR_READING_TYPE_BUFFER:
            ToTxt( sr.Value.SensorBuffer, SAHPI_SENSOR_BUFFER_LENGTH, txt );
            break;
        default:
            txt = txt_unknown;
            return;
    }

    std::wstring type_name;
    ToTxt( sr.Type, type_name );
    txt += L" (";
    txt += type_name;
    txt += L")";
}


/*****************************************************
 * Making HPI entry name
 ****************************************************/
void MakeNameForUnknown( std::wstring& txt )
{
    txt = txt_unknown;
}

void MakeNameForUp( std::wstring& txt )
{
    txt = L"..";
}

void MakeNameForDomain( SaHpiDomainIdT did, std::wstring& txt )
{
    if ( did == SAHPI_UNSPECIFIED_DOMAIN_ID ) {
        txt = L"Default Domain";
    } else {
        wchar_t buf[32];
        swprintf( buf, sizeof(buf) / sizeof(wchar_t), L"Domain %u", did );
        txt = buf;
    }
}

void MakeNameForDRT( std::wstring& txt )
{
    txt = L"Domain Reference Table";
}

void MakeNameForRPT( std::wstring& txt )
{
    txt = L"Resource Presense Table";
}

void MakeNameForDET( std::wstring& txt )
{
    txt = L"Domain Entity Tree";
}

void MakeNameForLog( SaHpiResourceIdT rid, std::wstring& txt )
{
    if ( rid == SAHPI_UNSPECIFIED_RESOURCE_ID ) {
        txt = L"Domain Event Log";
    } else {
        txt = L"Resource Event Log";
    }
}

void MakeNameForDAT( std::wstring& txt )
{
    txt = L"Domain Alarm Table";
}

void MakeNameForResource( const SaHpiRptEntryT& rpte, std::wstring& txt )
{
    wchar_t name1[32];
    swprintf( name1, sizeof(name1) / sizeof(wchar_t), L"Resource %u", rpte.ResourceId );
    std::wstring name2;
    ToTxt( rpte.ResourceTag, name2 );
    txt = name1;
    txt += L": ";
    txt += name2;
}

void MakeShortNameForResource( SaHpiResourceIdT rid, std::wstring& txt )
{
    wchar_t name[32];
    swprintf( name, sizeof(name) / sizeof(wchar_t), L"Resource %u", rid );
    txt = name;
}

void MakeNameForAlarm( const SaHpiAlarmT& a, std::wstring& txt )
{
    MakeShortNameForAlarm( a.AlarmId, txt );
    std::wstring severity;
    ToTxt( a.Severity, severity );
    txt += L" (";
    txt += severity;
    txt += L")";
}

void MakeShortNameForAlarm( const SaHpiAlarmIdT& aid, std::wstring& txt )
{
    wchar_t name[32];
    swprintf( name, sizeof(name) / sizeof(wchar_t), L"Alarm %u", aid );
    txt = name;
}

void MakeNameForLogEntry( const SaHpiEventLogEntryT& elentry, std::wstring& txt )
{
    MakeShortNameForLogEntry( elentry.EntryId, txt );
}

void MakeShortNameForLogEntry( SaHpiEventLogEntryIdT eid, std::wstring& txt )
{
    wchar_t name[32];
    swprintf( name, sizeof(name) / sizeof(wchar_t), L"Entry %u", eid );
    txt = name;
}

void MakeNameForEntity( const SaHpiEntityPathT& ep, std::wstring& txt )
{
    ToTxt( ep, txt );
}

void MakeShortNameForEntity( std::wstring& txt )
{
    txt = L"Entity";
}

void MakeNameForInstrument( const SaHpiRdrT& rdr, std::wstring& txt )
{
    MakeShortNameForInstrument( rdr.RdrType, GetInstrumentId( rdr ), txt );
    std::wstring idstring;
    ToTxt( rdr.IdString, idstring );
    txt += L": ";
    txt += idstring;
}

void MakeShortNameForInstrument( SaHpiRdrTypeT type, SaHpiInstrumentIdT id, std::wstring& txt )
{
    const wchar_t * type_name = 0;
    switch ( type ) {
        case SAHPI_CTRL_RDR:
            type_name = L"Control";
            break;
        case SAHPI_SENSOR_RDR:
            type_name = L"Sensor";
            break;
        case SAHPI_INVENTORY_RDR:
            type_name = L"Inventory";
            break;
        case SAHPI_WATCHDOG_RDR:
            type_name = L"Watchdog";
            break;
        case SAHPI_ANNUNCIATOR_RDR:
            type_name = L"Annunciator";
            break;
        case SAHPI_DIMI_RDR:
            type_name = L"DIMI";
            break;
        case SAHPI_FUMI_RDR:
            type_name = L"FUMI";
            break;
        default:
            type_name = txt_unknown.c_str();
    }
    wchar_t name[32];
    swprintf( name, sizeof(name) / sizeof(wchar_t), L"%ls %u", type_name, id );
    txt = name;
}

void MakeNameForHotSwap( std::wstring& txt )
{
    txt = L"Hot Swap Management";
}

void MakeNameForReset( std::wstring& txt )
{
    txt = L"Reset Management";
}

void MakeNameForPower( std::wstring& txt )
{
    txt = L"Power Management";
}

void MakeNameForIdrArea( const SaHpiIdrAreaHeaderT& ahdr, std::wstring& txt )
{
    MakeShortNameForIdrArea( ahdr.AreaId, txt );
}

void MakeShortNameForIdrArea( SaHpiEntryIdT aid, std::wstring& txt )
{
    wchar_t name[32];
    swprintf( name, sizeof(name) / sizeof(wchar_t), L"Area %u", aid );
    txt = name;
}

void MakeNameForAnnouncement( const SaHpiAnnouncementT& a, std::wstring& txt )
{
    MakeShortNameForAnnouncement( a.EntryId, txt );
    std::wstring severity;
    ToTxt( a.Severity, severity );
    txt += L" (";
    txt += severity;
    txt += L")";
}

void MakeShortNameForAnnouncement( const SaHpiEntryIdT& aid, std::wstring& txt )
{
    wchar_t name[32];
    swprintf( name, sizeof(name) / sizeof(wchar_t), L"Annoncement %u", aid );
    txt = name;
}

void MakeNameForDIMITest( SaHpiDimiTestNumT tnum, const SaHpiDimiTestT& dti, std::wstring& txt )
{
    MakeShortNameForDIMITest( tnum, txt );
    std::wstring name;
    ToTxt( dti.TestName, name );
    txt += L": ";
    txt += name;
}

void MakeShortNameForDIMITest( SaHpiDimiTestNumT tnum, std::wstring& txt )
{
    wchar_t name[32];
    swprintf( name, sizeof(name) / sizeof(wchar_t), L"Test %u", tnum );
    txt = name;
}


void MakeNameForFUMIBank( SaHpiBankNumT bnum, std::wstring& txt )
{
    std::wstring num;
    ToTxt( bnum, num, UI8_SaHpiBankNum );
    txt = L"Bank ";
    txt += num;
}

void MakeNameForIdrField( const SaHpiIdrFieldT& f, std::wstring& txt )
{
    MakeShortNameForIdrField( f.FieldId, txt );
}

void MakeShortNameForIdrField( SaHpiEntryIdT fid, std::wstring& txt )
{
    wchar_t name[32];
    swprintf( name, sizeof(name) / sizeof(wchar_t), L"Field %u", fid );
    txt = name;
}

void MakeNameForFUMIComponent( const SaHpiFumiComponentInfoT& ci, std::wstring& txt )
{
    MakeShortNameForFUMIComponent( ci.ComponentId, txt );
}

void MakeShortNameForFUMIComponent( SaHpiUint32T cid, std::wstring& txt )
{
    wchar_t name[32];
    swprintf( name, sizeof(name) / sizeof(wchar_t), L"Component %u", cid );
    txt = name;
}

void MakeNameForFUMISource( const SaHpiFumiSourceInfoT&, std::wstring& txt )
{
    // TODO use source info?
    MakeShortNameForFUMISource( txt );
}

void MakeShortNameForFUMISource( std::wstring& txt )
{
    txt = L"Assigned Source Image";
}

void MakeNameForFUMISourceComponent( const SaHpiFumiComponentInfoT& ci, std::wstring& txt )
{
    MakeShortNameForFUMISourceComponent( ci.ComponentId, txt );
}

void MakeShortNameForFUMISourceComponent( SaHpiUint32T cid, std::wstring& txt )
{
    wchar_t name[32];
    swprintf( name, sizeof(name) / sizeof(wchar_t), L"Source Component %u", cid );
    txt = name;
}

