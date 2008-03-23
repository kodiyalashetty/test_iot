#!/usr/bin/python
from openhpi import *

rptentries = [
    SaHpiRptEntryT( # RPT Entry 1
        EntryId=1,
        ResourceId=1,
        ResourceInfo=SaHpiResourceInfoT(
            ResourceRev=1,
            SpecificVer=1,
            DeviceSupport=1,
            ManufacturerId=1,
            ProductId=1,
            FirmwareMajorRev=1,
            FirmwareMinorRev=1,
            AuxFirmwareRev=1
        ),
        ResourceEntity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        ResourceCapabilities=(
            SAHPI_CAPABILITY_CONTROL|
            SAHPI_CAPABILITY_FRU|
            SAHPI_CAPABILITY_INVENTORY_DATA|
            SAHPI_CAPABILITY_RDR|
            SAHPI_CAPABILITY_RESOURCE|
            SAHPI_CAPABILITY_SENSOR
        ),
        ResourceSeverity=SAHPI_MAJOR,
        ResourceTag=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=26,
            Data='This is data for blade 14.'
        )
    ),
    SaHpiRptEntryT( # RPT Entry 2
        EntryId=2,
        ResourceId=2,
        ResourceInfo=SaHpiResourceInfoT(
            ResourceRev=2,
            SpecificVer=2,
            DeviceSupport=2,
            ManufacturerId=2,
            ProductId=2,
            FirmwareMajorRev=2,
            FirmwareMinorRev=2,
            AuxFirmwareRev=2
        ),
        ResourceEntity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=13),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        ResourceCapabilities=(
            SAHPI_CAPABILITY_CONTROL|
            SAHPI_CAPABILITY_FRU|
            SAHPI_CAPABILITY_INVENTORY_DATA|
            SAHPI_CAPABILITY_RDR|
            SAHPI_CAPABILITY_RESOURCE|
            SAHPI_CAPABILITY_SENSOR
        ),
        ResourceSeverity=SAHPI_MAJOR,
        ResourceTag=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=26,
            Data='This is data for blade 13.'
        )
    ),
    SaHpiRptEntryT( # RPT Entry 3
        EntryId=3,
        ResourceId=3,
        ResourceInfo=SaHpiResourceInfoT(
            ResourceRev=3,
            SpecificVer=3,
            DeviceSupport=3,
            ManufacturerId=3,
            ProductId=3,
            FirmwareMajorRev=3,
            FirmwareMinorRev=3,
            AuxFirmwareRev=3
        ),
        ResourceEntity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=12),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        ResourceCapabilities=(
            SAHPI_CAPABILITY_CONTROL|
            SAHPI_CAPABILITY_FRU|
            SAHPI_CAPABILITY_INVENTORY_DATA|
            SAHPI_CAPABILITY_RDR|
            SAHPI_CAPABILITY_RESOURCE|
            SAHPI_CAPABILITY_SENSOR
        ),
        ResourceSeverity=SAHPI_MAJOR,
        ResourceTag=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=26,
            Data='This is data for blade 12.'
        )
    ),
    SaHpiRptEntryT( # RPT Entry 4
        EntryId=4,
        ResourceId=4,
        ResourceInfo=SaHpiResourceInfoT(
            ResourceRev=4,
            SpecificVer=4,
            DeviceSupport=4,
            ManufacturerId=4,
            ProductId=4,
            FirmwareMajorRev=4,
            FirmwareMinorRev=4,
            AuxFirmwareRev=4
        ),
        ResourceEntity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=11),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=2),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        ResourceCapabilities=(
            SAHPI_CAPABILITY_CONTROL|
            SAHPI_CAPABILITY_FRU|
            SAHPI_CAPABILITY_INVENTORY_DATA|
            SAHPI_CAPABILITY_RDR|
            SAHPI_CAPABILITY_RESOURCE|
            SAHPI_CAPABILITY_SENSOR
        ),
        ResourceSeverity=SAHPI_MAJOR,
        ResourceTag=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=26,
            Data='This is data for blade 11.'
        )
    ),
    SaHpiRptEntryT( # RPT Entry 5
        EntryId=5,
        ResourceId=5,
        ResourceInfo=SaHpiResourceInfoT(
            ResourceRev=5,
            SpecificVer=5,
            DeviceSupport=5,
            ManufacturerId=5,
            ProductId=5,
            FirmwareMajorRev=5,
            FirmwareMinorRev=5,
            AuxFirmwareRev=5
        ),
        ResourceEntity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=10),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=2),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        ResourceCapabilities=(
            SAHPI_CAPABILITY_CONTROL|
            SAHPI_CAPABILITY_FRU|
            SAHPI_CAPABILITY_INVENTORY_DATA|
            SAHPI_CAPABILITY_RDR|
            SAHPI_CAPABILITY_RESOURCE|
            SAHPI_CAPABILITY_SENSOR
        ),
        ResourceSeverity=SAHPI_MAJOR,
        ResourceTag=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=26,
            Data='This is data for blade 10.'
        )
    ),
    SaHpiRptEntryT( # RPT Entry 6
        EntryId=6,
        ResourceId=6,
        ResourceInfo=SaHpiResourceInfoT(
            ResourceRev=6,
            SpecificVer=6,
            DeviceSupport=6,
            ManufacturerId=6,
            ProductId=6,
            FirmwareMajorRev=6,
            FirmwareMinorRev=6,
            AuxFirmwareRev=6
        ),
        ResourceEntity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=9),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=2),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        ResourceCapabilities=(
            SAHPI_CAPABILITY_CONTROL|
            SAHPI_CAPABILITY_FRU|
            SAHPI_CAPABILITY_INVENTORY_DATA|
            SAHPI_CAPABILITY_RDR|
            SAHPI_CAPABILITY_RESOURCE|
            SAHPI_CAPABILITY_SENSOR
        ),
        ResourceSeverity=SAHPI_MAJOR,
        ResourceTag=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=25,
            Data='This is data for blade 9.'
        )
    ),
    SaHpiRptEntryT( # RPT Entry 7
        EntryId=7,
        ResourceId=7,
        ResourceInfo=SaHpiResourceInfoT(
            ResourceRev=7,
            SpecificVer=7,
            DeviceSupport=7,
            ManufacturerId=7,
            ProductId=7,
            FirmwareMajorRev=7,
            FirmwareMinorRev=7,
            AuxFirmwareRev=7
        ),
        ResourceEntity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SYS_MGMNT_MODULE, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        ResourceCapabilities=(
            SAHPI_CAPABILITY_FRU|
            SAHPI_CAPABILITY_INVENTORY_DATA|
            SAHPI_CAPABILITY_RDR|
            SAHPI_CAPABILITY_RESOURCE
        ),
        ResourceSeverity=SAHPI_MAJOR,
        ResourceTag=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=39,
            Data='This is data for the management module.'
        )
    ),
    SaHpiRptEntryT( # RPT Entry 8
        EntryId=8,
        ResourceId=8,
        ResourceInfo=SaHpiResourceInfoT(
            ResourceRev=8,
            SpecificVer=8,
            DeviceSupport=8,
            ManufacturerId=8,
            ProductId=8,
            FirmwareMajorRev=8,
            FirmwareMinorRev=8,
            AuxFirmwareRev=8
        ),
        ResourceEntity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_INTERCONNECT, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        ResourceCapabilities=(
            SAHPI_CAPABILITY_FRU|
            SAHPI_CAPABILITY_INVENTORY_DATA|
            SAHPI_CAPABILITY_RDR|
            SAHPI_CAPABILITY_RESOURCE
        ),
        ResourceSeverity=SAHPI_MAJOR,
        ResourceTag=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=35,
            Data='This is data for the switch module.'
        )
    ),
    SaHpiRptEntryT( # RPT Entry 9
        EntryId=9,
        ResourceId=9,
        ResourceInfo=SaHpiResourceInfoT(
            ResourceRev=9,
            SpecificVer=9,
            DeviceSupport=9,
            ManufacturerId=9,
            ProductId=9,
            FirmwareMajorRev=9,
            FirmwareMinorRev=9,
            AuxFirmwareRev=9
        ),
        ResourceEntity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_POWER_SUPPLY, EntityLocation=3),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=2),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        ResourceCapabilities=(
            SAHPI_CAPABILITY_FRU|
            SAHPI_CAPABILITY_INVENTORY_DATA|
            SAHPI_CAPABILITY_RDR|
            SAHPI_CAPABILITY_RESOURCE
        ),
        ResourceSeverity=SAHPI_MAJOR,
        ResourceTag=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=34,
            Data='This is data for the power module.'
        )
    ),
    SaHpiRptEntryT( # RPT Entry 10
        EntryId=10,
        ResourceId=10,
        ResourceInfo=SaHpiResourceInfoT(
            ResourceRev=10,
            SpecificVer=10,
            DeviceSupport=10,
            ManufacturerId=10,
            ProductId=10,
            FirmwareMajorRev=10,
            FirmwareMinorRev=10,
            AuxFirmwareRev=10
        ),
        ResourceEntity=SaHpiEntityPathT(
            Entry=[                
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        ResourceCapabilities=(
            SAHPI_CAPABILITY_CONTROL|
            SAHPI_CAPABILITY_EVENT_LOG|
            SAHPI_CAPABILITY_INVENTORY_DATA|
            SAHPI_CAPABILITY_RDR|
            SAHPI_CAPABILITY_RESOURCE|
            SAHPI_CAPABILITY_SENSOR
        ),
        ResourceSeverity=SAHPI_CRITICAL,
        ResourceTag=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=25,
            Data='This is data for the chassis.'
        )
    ),
]

#********************** SENSORS ********************
sensors = [
    SaHpiRdrT( # Sensor RDR 1 
        RdrType=SAHPI_SENSOR_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            SensorRec=SaHpiSensorRecT(
                Num=1, Oem=1,
                Type=SAHPI_PLATFORM_VIOLATION,
                Category=SAHPI_EC_SEVERITY,
                EventCtrl=SAHPI_SEC_PER_EVENT,
                Events=SAHPI_ES_OK | SAHPI_ES_CRITICAL,
                EnableCtrl=SAHPI_FALSE,            
                DataFormat=SaHpiSensorDataFormatT(
                    BaseUnits=SAHPI_SU_UNSPECIFIED,
                    ModifierUnits=SAHPI_SU_UNSPECIFIED,
                    ModifierUse=SAHPI_SMUU_NONE,
                    Percentage=SAHPI_FALSE,
                    Range=SaHpiSensorRangeT(
                        Flags=SAHPI_SRF_MIN|SAHPI_SRF_MAX,
                        Max=SaHpiSensorReadingT(
                            IsSupported=SAHPI_TRUE,
                            Type=SAHPI_SENSOR_READING_TYPE_FLOAT64,
                            Value=SaHpiSensorReadingUnionT(SensorFloat64=1.0)
                        ),
                        Min=SaHpiSensorReadingT(
                            IsSupported=SAHPI_TRUE,
                            Type=SAHPI_SENSOR_READING_TYPE_FLOAT64,
                            Value=SaHpiSensorReadingUnionT(SensorFloat64=0.0)
                        )
                    )
                )
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=22,
            Data='Sensor 1 for Blade 14.'
        )
    ),
    SaHpiRdrT( # Sensor RDR 2 
        RdrType=SAHPI_SENSOR_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            SensorRec=SaHpiSensorRecT(
                Num=2, Oem=2,
                Type=SAHPI_PLATFORM_VIOLATION,
                Category=SAHPI_EC_SEVERITY,
                EventCtrl=SAHPI_SEC_PER_EVENT,
                Events=SAHPI_ES_OK | SAHPI_ES_CRITICAL,
                EnableCtrl=SAHPI_FALSE,            
                DataFormat=SaHpiSensorDataFormatT(
                    BaseUnits=SAHPI_SU_UNSPECIFIED,
                    ModifierUnits=SAHPI_SU_UNSPECIFIED,
                    ModifierUse=SAHPI_SMUU_NONE,
                    Percentage=SAHPI_FALSE,
                    Range=SaHpiSensorRangeT(
                        Flags=SAHPI_SRF_MIN|SAHPI_SRF_MAX,
                        Max=SaHpiSensorReadingT(
                            IsSupported=SAHPI_TRUE,
                            Type=SAHPI_SENSOR_READING_TYPE_FLOAT64,
                            Value=SaHpiSensorReadingUnionT(SensorFloat64=1.0)
                        ),
                        Min=SaHpiSensorReadingT(
                            IsSupported=SAHPI_TRUE,
                            Type=SAHPI_SENSOR_READING_TYPE_FLOAT64,
                            Value=SaHpiSensorReadingUnionT(SensorFloat64=0.0)
                        )
                    )
                )
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=22,
            Data='Sensor 2 for Blade 14.'
        )
    ),
    SaHpiRdrT( # Sensor RDR 3 
        RdrType=SAHPI_SENSOR_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            SensorRec=SaHpiSensorRecT(
                Num=3, Oem=3,
                Type=SAHPI_PLATFORM_VIOLATION,
                Category=SAHPI_EC_SEVERITY,
                EventCtrl=SAHPI_SEC_PER_EVENT,
                Events=SAHPI_ES_OK | SAHPI_ES_CRITICAL,
                EnableCtrl=SAHPI_FALSE,            
                DataFormat=SaHpiSensorDataFormatT(
                    BaseUnits=SAHPI_SU_UNSPECIFIED,
                    ModifierUnits=SAHPI_SU_UNSPECIFIED,
                    ModifierUse=SAHPI_SMUU_NONE,
                    Percentage=SAHPI_FALSE,
                    Range=SaHpiSensorRangeT(
                        Flags=SAHPI_SRF_MIN|SAHPI_SRF_MAX,
                        Max=SaHpiSensorReadingT(
                            IsSupported=SAHPI_TRUE,
                            Type=SAHPI_SENSOR_READING_TYPE_FLOAT64,
                            Value=SaHpiSensorReadingUnionT(SensorFloat64=1.0)
                        ),
                        Min=SaHpiSensorReadingT(
                            IsSupported=SAHPI_TRUE,
                            Type=SAHPI_SENSOR_READING_TYPE_FLOAT64,
                            Value=SaHpiSensorReadingUnionT(SensorFloat64=0.0)
                        )
                    )
                )
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=22,
            Data='Sensor 3 for Blade 14.'
        )
    ),
    SaHpiRdrT( # Sensor RDR 4 
        RdrType=SAHPI_SENSOR_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            SensorRec=SaHpiSensorRecT(
                Num=4, Oem=4,
                Type=SAHPI_PLATFORM_VIOLATION,
                Category=SAHPI_EC_SEVERITY,
                EventCtrl=SAHPI_SEC_PER_EVENT,
                Events=SAHPI_ES_OK | SAHPI_ES_CRITICAL,
                EnableCtrl=SAHPI_FALSE,            
                DataFormat=SaHpiSensorDataFormatT(
                    BaseUnits=SAHPI_SU_UNSPECIFIED,
                    ModifierUnits=SAHPI_SU_UNSPECIFIED,
                    ModifierUse=SAHPI_SMUU_NONE,
                    Percentage=SAHPI_FALSE,
                    Range=SaHpiSensorRangeT(
                        Flags=SAHPI_SRF_MIN|SAHPI_SRF_MAX,
                        Max=SaHpiSensorReadingT(
                            IsSupported=SAHPI_TRUE,
                            Type=SAHPI_SENSOR_READING_TYPE_FLOAT64,
                            Value=SaHpiSensorReadingUnionT(SensorFloat64=1.0)
                        ),
                        Min=SaHpiSensorReadingT(
                            IsSupported=SAHPI_TRUE,
                            Type=SAHPI_SENSOR_READING_TYPE_FLOAT64,
                            Value=SaHpiSensorReadingUnionT(SensorFloat64=0.0)
                        )
                    )
                )
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=22,
            Data='Sensor 4 for Blade 14.'
        )
    ),
    SaHpiRdrT( # Sensor RDR 5 
        RdrType=SAHPI_SENSOR_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            SensorRec=SaHpiSensorRecT(
                Num=5, Oem=5,
                Type=SAHPI_PLATFORM_VIOLATION,
                Category=SAHPI_EC_SEVERITY,
                EventCtrl=SAHPI_SEC_PER_EVENT,
                Events=SAHPI_ES_OK | SAHPI_ES_CRITICAL,
                EnableCtrl=SAHPI_FALSE,            
                DataFormat=SaHpiSensorDataFormatT(
                    BaseUnits=SAHPI_SU_UNSPECIFIED,
                    ModifierUnits=SAHPI_SU_UNSPECIFIED,
                    ModifierUse=SAHPI_SMUU_NONE,
                    Percentage=SAHPI_FALSE,
                    Range=SaHpiSensorRangeT(
                        Flags=SAHPI_SRF_MIN|SAHPI_SRF_MAX,
                        Max=SaHpiSensorReadingT(
                            IsSupported=SAHPI_TRUE,
                            Type=SAHPI_SENSOR_READING_TYPE_FLOAT64,
                            Value=SaHpiSensorReadingUnionT(SensorFloat64=1.0)
                        ),
                        Min=SaHpiSensorReadingT(
                            IsSupported=SAHPI_TRUE,
                            Type=SAHPI_SENSOR_READING_TYPE_FLOAT64,
                            Value=SaHpiSensorReadingUnionT(SensorFloat64=0.0)
                        )
                    )
                )
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=22,
            Data='Sensor 5 for Blade 14.'
        )
    ),
    SaHpiRdrT( # Sensor RDR 6 
        RdrType=SAHPI_SENSOR_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)                
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            SensorRec=SaHpiSensorRecT(
                Num=1, Oem=6,
                Type=SAHPI_PLATFORM_VIOLATION,
                Category=SAHPI_EC_SEVERITY,
                EventCtrl=SAHPI_SEC_PER_EVENT,
                Events=SAHPI_ES_OK | SAHPI_ES_CRITICAL,
                EnableCtrl=SAHPI_FALSE,
                DataFormat=SaHpiSensorDataFormatT(
                    BaseUnits=SAHPI_SU_UNSPECIFIED,
                    ModifierUnits=SAHPI_SU_UNSPECIFIED,
                    ModifierUse=SAHPI_SMUU_NONE,
                    Percentage=SAHPI_FALSE,
                    Range=SaHpiSensorRangeT(
                        Flags=SAHPI_SRF_MIN|SAHPI_SRF_MAX,
                        Max=SaHpiSensorReadingT(
                            IsSupported=SAHPI_TRUE,
                            Type=SAHPI_SENSOR_READING_TYPE_FLOAT64,
                            Value=SaHpiSensorReadingUnionT(SensorFloat64=1.0)
                        ),
                        Min=SaHpiSensorReadingT(
                            IsSupported=SAHPI_TRUE,
                            Type=SAHPI_SENSOR_READING_TYPE_FLOAT64,
                            Value=SaHpiSensorReadingUnionT(SensorFloat64=0.0)
                        )
                    )
                )
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=21,
            Data='Sensor 1 for Chassis.'
        )
    ),
    SaHpiRdrT( # Sensor RDR 7 
        RdrType=SAHPI_SENSOR_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)                
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            SensorRec=SaHpiSensorRecT(
                Num=2, Oem=7,
                Type=SAHPI_PLATFORM_VIOLATION,
                Category=SAHPI_EC_SEVERITY,
                EventCtrl=SAHPI_SEC_PER_EVENT,
                Events=SAHPI_ES_OK | SAHPI_ES_CRITICAL,
                EnableCtrl=SAHPI_FALSE,
                DataFormat=SaHpiSensorDataFormatT(
                    BaseUnits=SAHPI_SU_UNSPECIFIED,
                    ModifierUnits=SAHPI_SU_UNSPECIFIED,
                    ModifierUse=SAHPI_SMUU_NONE,
                    Percentage=SAHPI_FALSE,
                    Range=SaHpiSensorRangeT(
                        Flags=SAHPI_SRF_MIN|SAHPI_SRF_MAX,
                        Max=SaHpiSensorReadingT(
                            IsSupported=SAHPI_TRUE,
                            Type=SAHPI_SENSOR_READING_TYPE_FLOAT64,
                            Value=SaHpiSensorReadingUnionT(SensorFloat64=1.0)
                        ),
                        Min=SaHpiSensorReadingT(
                            IsSupported=SAHPI_TRUE,
                            Type=SAHPI_SENSOR_READING_TYPE_FLOAT64,
                            Value=SaHpiSensorReadingUnionT(SensorFloat64=0.0)
                        )
                    )
                )
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=22,
            Data='Sensor 2 for Chassis.'
        )
    )
] 
 
#********************** CONTROLS ********************
controls = [
    SaHpiRdrT( # Control RDR 1
        RdrType=SAHPI_CTRL_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            CtrlRec=SaHpiCtrlRecT(
                Num=1,
                OutputType=SAHPI_CTRL_GENERIC,
                Type=SAHPI_CTRL_TYPE_DIGITAL,
                TypeUnion=SaHpiCtrlRecUnionT(
                    Digital=SaHpiCtrlRecDigitalT(Default=SAHPI_CTRL_STATE_OFF)
                ),
                DefaultMode=SaHpiCtrlDefaultModeT(
                    Mode=SAHPI_CTRL_MODE_MANUAL,
                    ReadOnly=SAHPI_TRUE
                ),
                WriteOnly=SAHPI_FALSE,
                Oem=1
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=23,
            Data='Control 1 for Blade 14.'
        )
    ),
    SaHpiRdrT( # Control RDR 2
        RdrType=SAHPI_CTRL_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            CtrlRec=SaHpiCtrlRecT(
                Num=2,
                OutputType=SAHPI_CTRL_GENERIC,
                Type=SAHPI_CTRL_TYPE_DIGITAL,
                TypeUnion=SaHpiCtrlRecUnionT(
                    Digital=SaHpiCtrlRecDigitalT(Default=SAHPI_CTRL_STATE_OFF)
                ),
                DefaultMode=SaHpiCtrlDefaultModeT(
                    Mode=SAHPI_CTRL_MODE_MANUAL,
                    ReadOnly=SAHPI_TRUE
                ),
                WriteOnly=SAHPI_FALSE,
                Oem=2
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=23,
            Data='Control 2 for Blade 14.'
        )
    ),
    SaHpiRdrT( # Control RDR 3
        RdrType=SAHPI_CTRL_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            CtrlRec=SaHpiCtrlRecT(
                Num=3,
                OutputType=SAHPI_CTRL_GENERIC,
                Type=SAHPI_CTRL_TYPE_DIGITAL,
                TypeUnion=SaHpiCtrlRecUnionT(
                    Digital=SaHpiCtrlRecDigitalT(Default=SAHPI_CTRL_STATE_OFF)
                ),
                DefaultMode=SaHpiCtrlDefaultModeT(
                    Mode=SAHPI_CTRL_MODE_MANUAL,
                    ReadOnly=SAHPI_TRUE
                ),
                WriteOnly=SAHPI_FALSE,
                Oem=3
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=23,
            Data='Control 3 for Blade 14.'
        )
    ),
    SaHpiRdrT( # Control RDR 4
        RdrType=SAHPI_CTRL_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            CtrlRec=SaHpiCtrlRecT(
                Num=4,
                OutputType=SAHPI_CTRL_GENERIC,
                Type=SAHPI_CTRL_TYPE_DIGITAL,
                TypeUnion=SaHpiCtrlRecUnionT(
                    Digital=SaHpiCtrlRecDigitalT(Default=SAHPI_CTRL_STATE_OFF)
                ),
                DefaultMode=SaHpiCtrlDefaultModeT(
                    Mode=SAHPI_CTRL_MODE_MANUAL,
                    ReadOnly=SAHPI_TRUE
                ),
                WriteOnly=SAHPI_FALSE,
                Oem=4
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=23,
            Data='Control 4 for Blade 14.'
        )
    ),
    SaHpiRdrT( # Control RDR 5
        RdrType=SAHPI_CTRL_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            CtrlRec=SaHpiCtrlRecT(
                Num=5,
                OutputType=SAHPI_CTRL_GENERIC,
                Type=SAHPI_CTRL_TYPE_DIGITAL,
                TypeUnion=SaHpiCtrlRecUnionT(
                    Digital=SaHpiCtrlRecDigitalT(Default=SAHPI_CTRL_STATE_OFF)
                ),
                DefaultMode=SaHpiCtrlDefaultModeT(
                    Mode=SAHPI_CTRL_MODE_MANUAL,
                    ReadOnly=SAHPI_TRUE
                ),
                WriteOnly=SAHPI_FALSE,
                Oem=5
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=23,
            Data='Control 5 for Blade 14.'
        )
    )
] 
 
#********************** INVENTORIES ********************
inventories = [
    SaHpiRdrT( # Inventory RDR 1
        RdrType=SAHPI_INVENTORY_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            InventoryRec=SaHpiInventoryRecT(
                IdrId=1,
                Persistent=SAHPI_TRUE,
                Oem=1
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=25,
            Data='Inventory 1 for Blade 14.'
        )
    ),
    SaHpiRdrT( # Inventory RDR 2
        RdrType=SAHPI_INVENTORY_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            InventoryRec=SaHpiInventoryRecT(
                IdrId=2,
                Persistent=SAHPI_TRUE,
                Oem=2
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=25,
            Data='Inventory 2 for Blade 14.'
        )
    ),
    SaHpiRdrT( # Inventory RDR 3
        RdrType=SAHPI_INVENTORY_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            InventoryRec=SaHpiInventoryRecT(
                IdrId=3,
                Persistent=SAHPI_TRUE,
                Oem=3
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=25,
            Data='Inventory 3 for Blade 14.'
        )
    ),
    SaHpiRdrT( # Inventory RDR 4
        RdrType=SAHPI_INVENTORY_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            InventoryRec=SaHpiInventoryRecT(
                IdrId=4,
                Persistent=SAHPI_TRUE,
                Oem=4
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=25,
            Data='Inventory 4 for Blade 14.'
        )
    ),
    SaHpiRdrT( # Inventory RDR 5
        RdrType=SAHPI_INVENTORY_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            InventoryRec=SaHpiInventoryRecT(
                IdrId=5,
                Persistent=SAHPI_TRUE,
                Oem=5
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=25,
            Data='Inventory 5 for Blade 14.'
        )
    )
]

#********************** WATCHDOGS ********************
watchdogs = [
    SaHpiRdrT( # Watchdog RDR 1
        RdrType=SAHPI_WATCHDOG_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            WatchdogRec=SaHpiWatchdogRecT(
                WatchdogNum=1,
                Oem=1
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=24,
            Data='Watchdog 1 for Blade 14.'
        )
    ),
    SaHpiRdrT( # Watchdog RDR 2
        RdrType=SAHPI_WATCHDOG_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            WatchdogRec=SaHpiWatchdogRecT(
                WatchdogNum=2,
                Oem=2
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=24,
            Data='Watchdog 2 for Blade 14.'
        )
    ),
    SaHpiRdrT( # Watchdog RDR 3
        RdrType=SAHPI_WATCHDOG_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            WatchdogRec=SaHpiWatchdogRecT(
                WatchdogNum=3,
                Oem=3
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=24,
            Data='Watchdog 3 for Blade 14.'
        )
    ),
    SaHpiRdrT( # Watchdog RDR 4
        RdrType=SAHPI_WATCHDOG_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            WatchdogRec=SaHpiWatchdogRecT(
                WatchdogNum=4,
                Oem=4
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=24,
            Data='Watchdog 4 for Blade 14.'
        )
    ),
    SaHpiRdrT( # Watchdog RDR 5
        RdrType=SAHPI_WATCHDOG_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            WatchdogRec=SaHpiWatchdogRecT(
                WatchdogNum=5,
                Oem=5
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=24,
            Data='Watchdog 5 for Blade 14.'
        )
    )
]

#********************** ANNUNCIATORS ********************
annunciators = [
    SaHpiRdrT( # Annunciator RDR 1
        RdrType=SAHPI_ANNUNCIATOR_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            AnnunciatorRec=SaHpiAnnunciatorRecT(
                AnnunciatorNum=1,
                AnnunciatorType=SAHPI_ANNUNCIATOR_TYPE_LED,
                ModeReadOnly=SAHPI_FALSE,
                MaxConditions=2,
                Oem=1
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=27,
            Data='Annunciator 1 for Blade 14.'
        )
    ),
    SaHpiRdrT( # Annunciator RDR 2
        RdrType=SAHPI_ANNUNCIATOR_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            AnnunciatorRec=SaHpiAnnunciatorRecT(
                AnnunciatorNum=2,
                AnnunciatorType=SAHPI_ANNUNCIATOR_TYPE_LED,
                ModeReadOnly=SAHPI_FALSE,
                MaxConditions=2,
                Oem=2
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=27,
            Data='Annunciator 2 for Blade 14.'
        )
    ),
    SaHpiRdrT( # Annunciator RDR 3
        RdrType=SAHPI_ANNUNCIATOR_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            AnnunciatorRec=SaHpiAnnunciatorRecT(
                AnnunciatorNum=3,
                AnnunciatorType=SAHPI_ANNUNCIATOR_TYPE_LED,
                ModeReadOnly=SAHPI_FALSE,
                MaxConditions=2,
                Oem=3
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=27,
            Data='Annunciator 3 for Blade 14.'
        )
    ),
    SaHpiRdrT( # Annunciator RDR 4
        RdrType=SAHPI_ANNUNCIATOR_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            AnnunciatorRec=SaHpiAnnunciatorRecT(
                AnnunciatorNum=4,
                AnnunciatorType=SAHPI_ANNUNCIATOR_TYPE_LED,
                ModeReadOnly=SAHPI_FALSE,
                MaxConditions=2,
                Oem=4
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=27,
            Data='Annunciator 4 for Blade 14.'
        )
    ),
    SaHpiRdrT( # Annunciator RDR 5
        RdrType=SAHPI_ANNUNCIATOR_RDR,
        Entity=SaHpiEntityPathT(
            Entry=[
                SaHpiEntityT(EntityType=SAHPI_ENT_SBC_BLADE, EntityLocation=14),
                SaHpiEntityT(EntityType=SAHPI_ENT_SUB_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_SYSTEM_CHASSIS, EntityLocation=1),
                SaHpiEntityT(EntityType=SAHPI_ENT_ROOT, EntityLocation=0)
            ]
        ),
        RdrTypeUnion=SaHpiRdrTypeUnionT(
            AnnunciatorRec=SaHpiAnnunciatorRecT(
                AnnunciatorNum=5,
                AnnunciatorType=SAHPI_ANNUNCIATOR_TYPE_LED,
                ModeReadOnly=SAHPI_FALSE,
                MaxConditions=2,
                Oem=5
            )
        ),
        IdString=SaHpiTextBufferT(
            DataType=SAHPI_TL_TYPE_TEXT,
            Language=SAHPI_LANG_ENGLISH,
            DataLength=27,
            Data='Annunciator 5 for Blade 14.'
        )
    )
] 
