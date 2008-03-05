#!/usr/bin/python
from openhpi import *
from types import *

def objcmp(obj1, obj2):
	"""
	Compare two object instances and return True if they are equivalent
	"""

	# Check that the two objects are instances of a class
	if not repr(type(obj1)).startswith('<class ') or not repr(type(obj2)).startswith('<class '):
		print 'Object check failed: not a class'
		print obj1
		print obj2
		return False

	# Check that the two objects are instances of the same class
	if repr(obj1.__class__) != repr(obj2.__class__):
		print 'Class check failed "%s" != "%s"' % (repr(obj1.__class__), repr(obj2.__class_))
		return False
	
	for attr in dir(obj1): # Compare objects attribute by attribute
		# Disregard special python/swig attributes
		if attr.startswith('_') or repr(type(getattr(obj1,attr))) == "<type 'PySwigObject'>":
			continue
		
		# If the attribute is an object instance, compare them recursively 
		if repr(type(getattr(obj1, attr))).startswith('<class '):
			if not objcmp(getattr(obj1, attr), getattr(obj2, attr)):
				return False
		# If the attribute is a sequence or dictionary,
		# compare elements side by side recursively
		elif type(getattr(obj1, attr)) in [TupleType, ListType, DictType]:
			if len(getattr(obj1, attr)) != len(getattr(obj2, attr)):
				return False

			for e1, e2 in zip(getattr(obj1, attr), getattr(obj2, attr)):
				if not objcmp(e1, e2): return False
				
		# If the attribute is a native type (e.g. number or string)
		# then do normal comparison.
		else:
			if getattr(obj1, attr) != getattr(obj2, attr):
				print 'Attribute check failed obj1.%s != obj2.%s' % (attr, attr)
				return False
	
	return True


num_resources = 10
rptentries = []
# rpt entry 1
rpt = SaHpiRptEntryT()
rpt.EntryId = 1
rpt.ResourceId = 1

rpt.ResourceInfo = SaHpiResourceInfoT()

rpt.ResourceInfo.ResourceRev = 1
rpt.ResourceInfo.SpecificVer = 1
rpt.ResourceInfo.DeviceSupport = 1
rpt.ResourceInfo.ManufacturerId = 1
rpt.ResourceInfo.ProductId = 1
rpt.ResourceInfo.FirmwareMajorRev = 1
rpt.ResourceInfo.FirmwareMinorRev = 1
rpt.ResourceInfo.AuxFirmwareRev = 1

#rpt.ResourceEntity = SaHpiEntityPathT()
#rpt.ResourceEntity.Entry = SaHpiEntityT()
rpt.ResourceEntity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.ResourceEntity.Entry[0].EntityLocation = 14
rpt.ResourceEntity.Entry[1].EntityType = SAHPI_ENT_SBC_BLADE
rpt.ResourceEntity.Entry[1].EntityLocation = 14
rpt.ResourceEntity.Entry[2].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.ResourceEntity.Entry[2].EntityLocation = 1
rpt.ResourceEntity.Entry[3].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.ResourceEntity.Entry[3].EntityLocation = 1
rpt.ResourceEntity.Entry[4].EntityType = SAHPI_ENT_ROOT
rpt.ResourceEntity.Entry[4].EntityLocation = 0

rpt.ResourceCapabilities = rpt.ResourceCapabilities = SAHPI_CAPABILITY_CONTROL |SAHPI_CAPABILITY_FRU |SAHPI_CAPABILITY_INVENTORY_DATA |SAHPI_CAPABILITY_RDR |SAHPI_CAPABILITY_RESOURCE |SAHPI_CAPABILITY_SENSOR

rpt.ResourceSeverity = SAHPI_MAJOR

rpt.ResourceTag.DataType = SAHPI_TL_TYPE_TEXT
rpt.ResourceTag.Language = SAHPI_LANG_ENGLISH
rpt.ResourceTag.DataLength = 26
rpt.ResourceTag.Data = "This is data for blade 14."

rptentries.append(rpt)

# rpt entry 2
rpt=SaHpiRptEntryT()
rpt.EntryId = 2
rpt.ResourceId = 2

rpt.ResourceInfo = SaHpiResourceInfoT()
rpt.ResourceInfo.ResourceRev = 2
rpt.ResourceInfo.SpecificVer = 2
rpt.ResourceInfo.DeviceSupport = 2
rpt.ResourceInfo.ManufacturerId = 2
rpt.ResourceInfo.ProductId = 2
rpt.ResourceInfo.FirmwareMajorRev = 2
rpt.ResourceInfo.FirmwareMinorRev = 2
rpt.ResourceInfo.AuxFirmwareRev = 2

##rpt.ResourceEntity = SaHpiEntityPathT()

rpt.ResourceEntity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.ResourceEntity.Entry[0].EntityLocation = 13
rpt.ResourceEntity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.ResourceEntity.Entry[1].EntityLocation = 1
rpt.ResourceEntity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.ResourceEntity.Entry[2].EntityLocation = 1
rpt.ResourceEntity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.ResourceEntity.Entry[3].EntityLocation = 0

rpt.ResourceCapabilities = SAHPI_CAPABILITY_CONTROL |SAHPI_CAPABILITY_FRU |SAHPI_CAPABILITY_INVENTORY_DATA |SAHPI_CAPABILITY_RDR |SAHPI_CAPABILITY_RESOURCE |SAHPI_CAPABILITY_SENSOR

rpt.ResourceSeverity = SAHPI_MAJOR

rpt.ResourceTag.DataType = SAHPI_TL_TYPE_TEXT
rpt.ResourceTag.Language = SAHPI_LANG_ENGLISH
rpt.ResourceTag.DataLength = 26
rpt.ResourceTag.Data = "This is data for blade 13."

rptentries.append(rpt)

# rpt entry 3
rpt=SaHpiRptEntryT()
rpt.EntryId = 3
rpt.ResourceId = 3

rpt.ResourceInfo = SaHpiResourceInfoT()
rpt.ResourceInfo.ResourceRev = 3
rpt.ResourceInfo.SpecificVer = 3
rpt.ResourceInfo.DeviceSupport = 3
rpt.ResourceInfo.ManufacturerId = 3
rpt.ResourceInfo.ProductId = 3
rpt.ResourceInfo.FirmwareMajorRev = 3
rpt.ResourceInfo.FirmwareMinorRev = 3
rpt.ResourceInfo.AuxFirmwareRev = 3

##rpt.ResourceEntity = SaHpiEntityPathT()
rpt.ResourceEntity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.ResourceEntity.Entry[0].EntityLocation = 12
rpt.ResourceEntity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.ResourceEntity.Entry[1].EntityLocation = 1
rpt.ResourceEntity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.ResourceEntity.Entry[2].EntityLocation = 1
rpt.ResourceEntity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.ResourceEntity.Entry[3].EntityLocation = 0

rpt.ResourceCapabilities = SAHPI_CAPABILITY_CONTROL |SAHPI_CAPABILITY_FRU |SAHPI_CAPABILITY_INVENTORY_DATA |SAHPI_CAPABILITY_RDR |SAHPI_CAPABILITY_RESOURCE |SAHPI_CAPABILITY_SENSOR

rpt.ResourceSeverity = SAHPI_MAJOR

rpt.ResourceTag.DataType = SAHPI_TL_TYPE_TEXT
rpt.ResourceTag.Language = SAHPI_LANG_ENGLISH
rpt.ResourceTag.DataLength = 26
rpt.ResourceTag.Data = "This is data for blade 12."

rptentries.append(rpt)

# rpt entry 4
rpt=SaHpiRptEntryT()
rpt.EntryId = 4
rpt.ResourceId = 4

rpt.ResourceInfo = SaHpiResourceInfoT()
rpt.ResourceInfo.ResourceRev = 4
rpt.ResourceInfo.SpecificVer = 4
rpt.ResourceInfo.DeviceSupport = 4
rpt.ResourceInfo.ManufacturerId = 4
rpt.ResourceInfo.ProductId = 4
rpt.ResourceInfo.FirmwareMajorRev = 4
rpt.ResourceInfo.FirmwareMinorRev = 4
rpt.ResourceInfo.AuxFirmwareRev = 4

##rpt.ResourceEntity = SaHpiEntityPathT()
rpt.ResourceEntity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.ResourceEntity.Entry[0].EntityLocation = 11
rpt.ResourceEntity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.ResourceEntity.Entry[1].EntityLocation = 2
rpt.ResourceEntity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.ResourceEntity.Entry[2].EntityLocation = 1
rpt.ResourceEntity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.ResourceEntity.Entry[3].EntityLocation = 0

rpt.ResourceCapabilities = SAHPI_CAPABILITY_CONTROL |SAHPI_CAPABILITY_FRU |SAHPI_CAPABILITY_INVENTORY_DATA |SAHPI_CAPABILITY_RDR |SAHPI_CAPABILITY_RESOURCE |SAHPI_CAPABILITY_SENSOR


rpt.ResourceSeverity = SAHPI_MAJOR

rpt.ResourceTag.DataType = SAHPI_TL_TYPE_TEXT
rpt.ResourceTag.Language = SAHPI_LANG_ENGLISH
rpt.ResourceTag.DataLength = 26
rpt.ResourceTag.Data = "This is data for blade 11."

rptentries.append(rpt)

# rpt entry 5
rpt=SaHpiRptEntryT()
rpt.EntryId = 5
rpt.ResourceId = 5

rpt.ResourceInfo = SaHpiResourceInfoT()
rpt.ResourceInfo.ResourceRev = 5
rpt.ResourceInfo.SpecificVer = 5
rpt.ResourceInfo.DeviceSupport = 5
rpt.ResourceInfo.ManufacturerId = 5
rpt.ResourceInfo.ProductId = 5
rpt.ResourceInfo.FirmwareMajorRev = 5
rpt.ResourceInfo.FirmwareMinorRev = 5
rpt.ResourceInfo.AuxFirmwareRev = 5

##rpt.ResourceEntity = SaHpiEntityPathT()
rpt.ResourceEntity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.ResourceEntity.Entry[0].EntityLocation = 10
rpt.ResourceEntity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.ResourceEntity.Entry[1].EntityLocation = 2
rpt.ResourceEntity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.ResourceEntity.Entry[2].EntityLocation = 1
rpt.ResourceEntity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.ResourceEntity.Entry[3].EntityLocation = 0


rpt.ResourceCapabilities = SAHPI_CAPABILITY_CONTROL |SAHPI_CAPABILITY_FRU |SAHPI_CAPABILITY_INVENTORY_DATA |SAHPI_CAPABILITY_RDR |SAHPI_CAPABILITY_RESOURCE |SAHPI_CAPABILITY_SENSOR

rpt.ResourceSeverity = SAHPI_MAJOR

rpt.ResourceTag.DataType = SAHPI_TL_TYPE_TEXT
rpt.ResourceTag.Language = SAHPI_LANG_ENGLISH
rpt.ResourceTag.DataLength = 26
rpt.ResourceTag.Data = "This is data for blade 10."

rptentries.append(rpt)

# rpt entry 6
rpt=SaHpiRptEntryT()
rpt.EntryId = 6
rpt.ResourceId = 6

rpt.ResourceInfo = SaHpiResourceInfoT()
rpt.ResourceInfo.ResourceRev = 6
rpt.ResourceInfo.SpecificVer = 6
rpt.ResourceInfo.DeviceSupport = 6
rpt.ResourceInfo.ManufacturerId = 6
rpt.ResourceInfo.ProductId = 6
rpt.ResourceInfo.FirmwareMajorRev = 6
rpt.ResourceInfo.FirmwareMinorRev = 6
rpt.ResourceInfo.AuxFirmwareRev = 6

##rpt.ResourceEntity = SaHpiEntityPathT()
rpt.ResourceEntity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.ResourceEntity.Entry[0].EntityLocation = 9
rpt.ResourceEntity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.ResourceEntity.Entry[1].EntityLocation = 2
rpt.ResourceEntity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.ResourceEntity.Entry[2].EntityLocation = 1
rpt.ResourceEntity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.ResourceEntity.Entry[3].EntityLocation = 0

rpt.ResourceCapabilities = SAHPI_CAPABILITY_CONTROL |SAHPI_CAPABILITY_FRU |SAHPI_CAPABILITY_INVENTORY_DATA |SAHPI_CAPABILITY_RDR |SAHPI_CAPABILITY_RESOURCE |SAHPI_CAPABILITY_SENSOR


rpt.ResourceSeverity = SAHPI_MAJOR

rpt.ResourceTag.DataType = SAHPI_TL_TYPE_TEXT
rpt.ResourceTag.Language = SAHPI_LANG_ENGLISH
rpt.ResourceTag.DataLength = 25
rpt.ResourceTag.Data = "This is data for blade 9."

rptentries.append(rpt)

# rpt entry 7
rpt=SaHpiRptEntryT()
rpt.EntryId = 7
rpt.ResourceId = 7

rpt.ResourceInfo = SaHpiResourceInfoT()
rpt.ResourceInfo.ResourceRev = 7
rpt.ResourceInfo.SpecificVer = 7
rpt.ResourceInfo.DeviceSupport = 7
rpt.ResourceInfo.ManufacturerId = 7
rpt.ResourceInfo.ProductId = 7
rpt.ResourceInfo.FirmwareMajorRev = 7
rpt.ResourceInfo.FirmwareMinorRev = 7
rpt.ResourceInfo.AuxFirmwareRev = 7

##rpt.ResourceEntity = SaHpiEntityPathT()

rpt.ResourceEntity.Entry[0].EntityType = SAHPI_ENT_SYS_MGMNT_MODULE
rpt.ResourceEntity.Entry[0].EntityLocation = 1
rpt.ResourceEntity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.ResourceEntity.Entry[1].EntityLocation = 1
rpt.ResourceEntity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.ResourceEntity.Entry[2].EntityLocation = 1
rpt.ResourceEntity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.ResourceEntity.Entry[3].EntityLocation = 0

rpt.ResourceCapabilities = SAHPI_CAPABILITY_FRU |SAHPI_CAPABILITY_INVENTORY_DATA |SAHPI_CAPABILITY_RDR |SAHPI_CAPABILITY_RESOURCE

rpt.ResourceSeverity = SAHPI_MAJOR

rpt.ResourceTag.DataType = SAHPI_TL_TYPE_TEXT
rpt.ResourceTag.Language = SAHPI_LANG_ENGLISH
rpt.ResourceTag.DataLength = 39
rpt.ResourceTag.Data = "This is data for the management module."

rptentries.append(rpt)

# rpt entry 8
rpt=SaHpiRptEntryT()
rpt.EntryId = 8
rpt.ResourceId = 8

rpt.ResourceInfo = SaHpiResourceInfoT()
rpt.ResourceInfo.ResourceRev = 8
rpt.ResourceInfo.SpecificVer = 8
rpt.ResourceInfo.DeviceSupport = 8
rpt.ResourceInfo.ManufacturerId = 8
rpt.ResourceInfo.ProductId = 8
rpt.ResourceInfo.FirmwareMajorRev = 8
rpt.ResourceInfo.FirmwareMinorRev = 8
rpt.ResourceInfo.AuxFirmwareRev = 8

##rpt.ResourceEntity = SaHpiEntityPathT()

rpt.ResourceEntity.Entry[0].EntityType = SAHPI_ENT_INTERCONNECT
rpt.ResourceEntity.Entry[0].EntityLocation = 1
rpt.ResourceEntity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.ResourceEntity.Entry[1].EntityLocation = 1
rpt.ResourceEntity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.ResourceEntity.Entry[2].EntityLocation = 1
rpt.ResourceEntity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.ResourceEntity.Entry[3].EntityLocation = 0

rpt.ResourceCapabilities = SAHPI_CAPABILITY_FRU |SAHPI_CAPABILITY_INVENTORY_DATA |SAHPI_CAPABILITY_RDR |SAHPI_CAPABILITY_RESOURCE

rpt.ResourceSeverity = SAHPI_MAJOR

rpt.ResourceTag.DataType = SAHPI_TL_TYPE_TEXT
rpt.ResourceTag.Language = SAHPI_LANG_ENGLISH
rpt.ResourceTag.DataLength = 35
rpt.ResourceTag.Data = "This is data for the switch module."

rptentries.append(rpt)

# rpt entry 9
rpt=SaHpiRptEntryT()
rpt.EntryId = 9
rpt.ResourceId = 9

rpt.ResourceInfo = SaHpiResourceInfoT()
rpt.ResourceInfo.ResourceRev = 9
rpt.ResourceInfo.SpecificVer = 9
rpt.ResourceInfo.DeviceSupport = 9
rpt.ResourceInfo.ManufacturerId = 9
rpt.ResourceInfo.ProductId = 9
rpt.ResourceInfo.FirmwareMajorRev = 9
rpt.ResourceInfo.FirmwareMinorRev = 9
rpt.ResourceInfo.AuxFirmwareRev = 9

##rpt.ResourceEntity = SaHpiEntityPathT()

rpt.ResourceEntity.Entry[0].EntityType = SAHPI_ENT_POWER_SUPPLY
rpt.ResourceEntity.Entry[0].EntityLocation = 3
rpt.ResourceEntity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.ResourceEntity.Entry[1].EntityLocation = 2
rpt.ResourceEntity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.ResourceEntity.Entry[2].EntityLocation = 1
rpt.ResourceEntity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.ResourceEntity.Entry[3].EntityLocation = 0

rpt.ResourceCapabilities = SAHPI_CAPABILITY_FRU |SAHPI_CAPABILITY_INVENTORY_DATA |SAHPI_CAPABILITY_RDR |SAHPI_CAPABILITY_RESOURCE

rpt.ResourceSeverity = SAHPI_MAJOR

rpt.ResourceTag.DataType = SAHPI_TL_TYPE_TEXT
rpt.ResourceTag.Language = SAHPI_LANG_ENGLISH
rpt.ResourceTag.DataLength = 34
rpt.ResourceTag.Data = "This is data for the power module."

rptentries.append(rpt)

# rpt entry 10
rpt=SaHpiRptEntryT()
rpt.EntryId = 10
rpt.ResourceId = 10

rpt.ResourceInfo = SaHpiResourceInfoT()
rpt.ResourceInfo.ResourceRev = 10
rpt.ResourceInfo.SpecificVer = 10
rpt.ResourceInfo.DeviceSupport = 10
rpt.ResourceInfo.ManufacturerId = 10
rpt.ResourceInfo.ProductId = 10
rpt.ResourceInfo.FirmwareMajorRev = 10
rpt.ResourceInfo.FirmwareMinorRev = 10
rpt.ResourceInfo.AuxFirmwareRev = 10

##rpt.ResourceEntity = SaHpiEntityPathT()
rpt.ResourceEntity.Entry[0].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.ResourceEntity.Entry[0].EntityLocation = 1
rpt.ResourceEntity.Entry[1].EntityType = SAHPI_ENT_ROOT
rpt.ResourceEntity.Entry[1].EntityLocation = 0

rpt.ResourceCapabilities = SAHPI_CAPABILITY_CONTROL |SAHPI_CAPABILITY_INVENTORY_DATA |SAHPI_CAPABILITY_RDR |SAHPI_CAPABILITY_RESOURCE |SAHPI_CAPABILITY_EVENT_LOG |SAHPI_CAPABILITY_SENSOR

rpt.ResourceSeverity = SAHPI_CRITICAL

rpt.ResourceTag.DataType = SAHPI_TL_TYPE_TEXT
rpt.ResourceTag.Language = SAHPI_LANG_ENGLISH
rpt.ResourceTag.DataLength = 25
rpt.ResourceTag.Data = "This is data for chassis."

rptentries.append(rpt)

  #***************** * Start of RDRs * *****************
 #**********************SENSORS********************
 # Sensor RDR 1 

num_sensors=7 
sensors = [] 
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_SENSOR_RDR

##rpt.Entity = SaHpiEntityPathT()
rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.Entity.Entry[0].EntityLocation = 14
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.Entity.Entry[1].EntityLocation = 1
rpt.Entity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[2].EntityLocation = 1
rpt.Entity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[3].EntityLocation = 0

#rpt.RdrTypeUnion.SensorRec = SaHpiSensorRecT()

rpt.RdrTypeUnion.SensorRec.Num = 1
rpt.RdrTypeUnion.SensorRec.Type = SAHPI_PLATFORM_VIOLATION
rpt.RdrTypeUnion.SensorRec.Category = SAHPI_EC_SEVERITY
rpt.RdrTypeUnion.SensorRec.EventCtrl = SAHPI_SEC_PER_EVENT
rpt.RdrTypeUnion.SensorRec.Events = SAHPI_ES_OK | SAHPI_ES_CRITICAL
rpt.RdrTypeUnion.SensorRec.EnableCtrl = SAHPI_FALSE

#rpt.RdrTypeUnion.SensorRec.DataFormat = SaHpiSensorDataFormatT()

rpt.RdrTypeUnion.SensorRec.DataFormat.BaseUnits = SAHPI_SU_UNSPECIFIED
rpt.RdrTypeUnion.SensorRec.DataFormat.ModifierUnits = SAHPI_SU_UNSPECIFIED
rpt.RdrTypeUnion.SensorRec.DataFormat.ModifierUse = SAHPI_SMUU_NONE
rpt.RdrTypeUnion.SensorRec.DataFormat.Percentage = SAHPI_FALSE
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Flags = SAHPI_SRF_MIN | SAHPI_SRF_MAX
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Max.ISSupported = SAHPI_TRUE
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Max.Type = SAHPI_SENSOR_READING_TYPE_FLOAT64
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Max.Value.SensorFloat64 = 1.0
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Min.ISSupported = SAHPI_TRUE
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Min.Type = SAHPI_SENSOR_READING_TYPE_FLOAT64
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Min.Value.SensorFloat64 = 0.0

rpt.RdrTypeUnion.SensorRec.Oem = 1

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 22
rpt.IdString.Data = "Sensor 1 for Blade 14."

sensors.append(rpt)
 
# Sensor RDR 2 
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_SENSOR_RDR

##rpt.Entity = SaHpiEntityT()

rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.Entity.Entry[0].EntityLocation = 14
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.Entity.Entry[1].EntityLocation = 1
rpt.Entity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[2].EntityLocation = 1
rpt.Entity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[3].EntityLocation = 0
#rpt.RdrTypeUnion.SensorRec = SaHpiSensorRecT()

rpt.RdrTypeUnion.SensorRec.Num = 2
rpt.RdrTypeUnion.SensorRec.Type = SAHPI_PLATFORM_VIOLATION
rpt.RdrTypeUnion.SensorRec.Category = SAHPI_EC_SEVERITY
rpt.RdrTypeUnion.SensorRec.EventCtrl = SAHPI_SEC_PER_EVENT
rpt.RdrTypeUnion.SensorRec.Events = SAHPI_ES_OK | SAHPI_ES_CRITICAL
rpt.RdrTypeUnion.SensorRec.EnableCtrl = SAHPI_FALSE


rpt.RdrTypeUnion.SensorRec.DataFormat = SaHpiSensorDataFormatT()

rpt.RdrTypeUnion.SensorRec.DataFormat.BaseUnits = SAHPI_SU_UNSPECIFIED
rpt.RdrTypeUnion.SensorRec.DataFormat.ModifierUnits = SAHPI_SU_UNSPECIFIED
rpt.RdrTypeUnion.SensorRec.DataFormat.ModifierUse = SAHPI_SMUU_NONE
rpt.RdrTypeUnion.SensorRec.DataFormat.Percentage = SAHPI_FALSE
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Flags = SAHPI_SRF_MIN | SAHPI_SRF_MAX
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Max.ISSupported = SAHPI_TRUE
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Max.Type = SAHPI_SENSOR_READING_TYPE_FLOAT64
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Max.Value.SensorFloat64 = 1.0
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Min.ISSupported = SAHPI_TRUE
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Min.Type = SAHPI_SENSOR_READING_TYPE_FLOAT64
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Min.Value.SensorFloat64 = 0.0

rpt.RdrTypeUnion.SensorRec.Oem = 2

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 22
rpt.IdString.Data = "Sensor 2 for Blade 14."

sensors.append(rpt)
 
 # Sensor RDR 3
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_SENSOR_RDR

##rpt.Entity = SaHpiEntityT()

rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.Entity.Entry[0].EntityLocation = 14
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.Entity.Entry[1].EntityLocation = 1
rpt.Entity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[2].EntityLocation = 1
rpt.Entity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[3].EntityLocation = 0

##rpt.RdrTypeUnion.SensorRec = SaHpiSensorRecT()

rpt.RdrTypeUnion.SensorRec.Num = 3
rpt.RdrTypeUnion.SensorRec.Type = SAHPI_PLATFORM_VIOLATION
rpt.RdrTypeUnion.SensorRec.Category = SAHPI_EC_SEVERITY
rpt.RdrTypeUnion.SensorRec.EventCtrl = SAHPI_SEC_PER_EVENT
rpt.RdrTypeUnion.SensorRec.Events = SAHPI_ES_OK | SAHPI_ES_CRITICAL
rpt.RdrTypeUnion.SensorRec.EnableCtrl = SAHPI_FALSE

rpt.RdrTypeUnion.SensorRec.DataFormat = SaHpiSensorDataFormatT()

rpt.RdrTypeUnion.SensorRec.DataFormat.BaseUnits = SAHPI_SU_UNSPECIFIED
rpt.RdrTypeUnion.SensorRec.DataFormat.ModifierUnits = SAHPI_SU_UNSPECIFIED
rpt.RdrTypeUnion.SensorRec.DataFormat.ModifierUse = SAHPI_SMUU_NONE
rpt.RdrTypeUnion.SensorRec.DataFormat.Percentage = SAHPI_FALSE
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Flags = SAHPI_SRF_MIN | SAHPI_SRF_MAX
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Max.ISSupported = SAHPI_TRUE
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Max.Type = SAHPI_SENSOR_READING_TYPE_FLOAT64
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Max.Value.SensorFloat64 = 1.0
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Min.ISSupported = SAHPI_TRUE
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Min.Type = SAHPI_SENSOR_READING_TYPE_FLOAT64
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Min.Value.SensorFloat64 = 0.0

rpt.RdrTypeUnion.SensorRec.Oem = 3

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 22
rpt.IdString.Data = "Sensor 3 for Blade 14."

sensors.append(rpt)
 
# Sensor RDR 4
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_SENSOR_RDR

##rpt.Entity = SaHpiEntityT()

rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.Entity.Entry[0].EntityLocation = 14
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.Entity.Entry[1].EntityLocation = 1
rpt.Entity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[2].EntityLocation = 1
rpt.Entity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[3].EntityLocation = 0

##rpt.RdrTypeUnion.SensorRec = SaHpiSensorRecT()

rpt.RdrTypeUnion.SensorRec.Num = 4
rpt.RdrTypeUnion.SensorRec.Type = SAHPI_PLATFORM_VIOLATION
rpt.RdrTypeUnion.SensorRec.Category = SAHPI_EC_SEVERITY
rpt.RdrTypeUnion.SensorRec.EventCtrl = SAHPI_SEC_PER_EVENT
rpt.RdrTypeUnion.SensorRec.Events = SAHPI_ES_OK | SAHPI_ES_CRITICAL
rpt.RdrTypeUnion.SensorRec.EnableCtrl = SAHPI_FALSE

rpt.RdrTypeUnion.SensorRec.DataFormat = SaHpiSensorDataFormatT()

rpt.RdrTypeUnion.SensorRec.DataFormat.BaseUnits = SAHPI_SU_UNSPECIFIED
rpt.RdrTypeUnion.SensorRec.DataFormat.ModifierUnits = SAHPI_SU_UNSPECIFIED
rpt.RdrTypeUnion.SensorRec.DataFormat.ModifierUse = SAHPI_SMUU_NONE
rpt.RdrTypeUnion.SensorRec.DataFormat.Percentage = SAHPI_FALSE
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Flags = SAHPI_SRF_MIN | SAHPI_SRF_MAX
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Max.ISSupported = SAHPI_TRUE
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Max.Type = SAHPI_SENSOR_READING_TYPE_FLOAT64
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Max.Value.SensorFloat64 = 1.0
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Min.ISSupported = SAHPI_TRUE
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Min.Type = SAHPI_SENSOR_READING_TYPE_FLOAT64
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Min.Value.SensorFloat64 = 0.0

rpt.RdrTypeUnion.SensorRec.Oem = 4

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 22
rpt.IdString.Data = "Sensor 4 for Blade 14."

sensors.append(rpt)
 
 # Sensor RDR 5
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_SENSOR_RDR
 
##rpt.Entity = SaHpiEntityT() 

rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.Entity.Entry[0].EntityLocation = 14
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.Entity.Entry[1].EntityLocation = 1
rpt.Entity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[2].EntityLocation = 1
rpt.Entity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[3].EntityLocation = 0
 
##rpt.RdrTypeUnion.SensorRec = SaHpiSensorRecT() 
rpt.RdrTypeUnion.SensorRec.Num = 5
rpt.RdrTypeUnion.SensorRec.Type = SAHPI_PLATFORM_VIOLATION
rpt.RdrTypeUnion.SensorRec.Category = SAHPI_EC_SEVERITY
rpt.RdrTypeUnion.SensorRec.EventCtrl = SAHPI_SEC_PER_EVENT
rpt.RdrTypeUnion.SensorRec.Events = SAHPI_ES_OK | SAHPI_ES_CRITICAL
rpt.RdrTypeUnion.SensorRec.EnableCtrl = SAHPI_FALSE

rpt.RdrTypeUnion.SensorRec.DataFormat = SaHpiSensorDataFormatT()

rpt.RdrTypeUnion.SensorRec.DataFormat.BaseUnits = SAHPI_SU_UNSPECIFIED
rpt.RdrTypeUnion.SensorRec.DataFormat.ModifierUnits = SAHPI_SU_UNSPECIFIED
rpt.RdrTypeUnion.SensorRec.DataFormat.ModifierUse = SAHPI_SMUU_NONE
rpt.RdrTypeUnion.SensorRec.DataFormat.Percentage = SAHPI_FALSE
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Flags = SAHPI_SRF_MIN | SAHPI_SRF_MAX
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Max.ISSupported = SAHPI_TRUE
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Max.Type = SAHPI_SENSOR_READING_TYPE_FLOAT64
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Max.Value.SensorFloat64 = 1.0
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Min.ISSupported = SAHPI_TRUE
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Min.Type = SAHPI_SENSOR_READING_TYPE_FLOAT64
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Min.Value.SensorFloat64 = 0.0

rpt.RdrTypeUnion.SensorRec.Oem = 5

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 22
rpt.IdString.Data = "Sensor 5 for Blade 14."

sensors.append(rpt) 
 
# Sensor RDR 6
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_SENSOR_RDR

##rpt.Entity = SaHpiEntityT()
rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[0].EntityLocation = 1
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[1].EntityLocation = 0

##rpt.RdrTypeUnion.SensorRec = SaHpiSensorRecT()
rpt.RdrTypeUnion.SensorRec.Num = 1
rpt.RdrTypeUnion.SensorRec.Type = SAHPI_PLATFORM_VIOLATION
rpt.RdrTypeUnion.SensorRec.Category = SAHPI_EC_SEVERITY
rpt.RdrTypeUnion.SensorRec.EventCtrl = SAHPI_SEC_PER_EVENT
rpt.RdrTypeUnion.SensorRec.Events = SAHPI_ES_OK | SAHPI_ES_CRITICAL
rpt.RdrTypeUnion.SensorRec.EnableCtrl = SAHPI_FALSE

rpt.RdrTypeUnion.SensorRec.DataFormat = SaHpiSensorDataFormatT()

rpt.RdrTypeUnion.SensorRec.DataFormat.BaseUnits = SAHPI_SU_UNSPECIFIED
rpt.RdrTypeUnion.SensorRec.DataFormat.ModifierUnits = SAHPI_SU_UNSPECIFIED
rpt.RdrTypeUnion.SensorRec.DataFormat.ModifierUse = SAHPI_SMUU_NONE
rpt.RdrTypeUnion.SensorRec.DataFormat.Percentage = SAHPI_FALSE
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Flags = SAHPI_SRF_MIN | SAHPI_SRF_MAX
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Max.ISSupported = SAHPI_TRUE
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Max.Type = SAHPI_SENSOR_READING_TYPE_FLOAT64
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Max.Value.SensorFloat64 = 1.0
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Min.ISSupported = SAHPI_TRUE
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Min.Type = SAHPI_SENSOR_READING_TYPE_FLOAT64
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Min.Value.SensorFloat64 = 0.0

rpt.RdrTypeUnion.SensorRec.Oem = 6

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 21
rpt.IdString.Data = "Sensor 1 for Chassis."

sensors.append(rpt)
 
# Sensor RDR 7
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_SENSOR_RDR

##rpt.Entity = SaHpiEntityT()

rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[0].EntityLocation = 1
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[1].EntityLocation = 0

##rpt.RdrTypeUnion.SensorRec = SaHpiSensorRecT()

rpt.RdrTypeUnion.SensorRec.Num = 2
rpt.RdrTypeUnion.SensorRec.Type = SAHPI_PLATFORM_VIOLATION
rpt.RdrTypeUnion.SensorRec.Category = SAHPI_EC_SEVERITY
rpt.RdrTypeUnion.SensorRec.EventCtrl = SAHPI_SEC_PER_EVENT
rpt.RdrTypeUnion.SensorRec.Events = SAHPI_ES_OK | SAHPI_ES_CRITICAL
rpt.RdrTypeUnion.SensorRec.EnableCtrl = SAHPI_FALSE

rpt.RdrTypeUnion.SensorRec.DataFormat = SaHpiSensorDataFormatT()

rpt.RdrTypeUnion.SensorRec.DataFormat.BaseUnits = SAHPI_SU_UNSPECIFIED
rpt.RdrTypeUnion.SensorRec.DataFormat.ModifierUnits = SAHPI_SU_UNSPECIFIED
rpt.RdrTypeUnion.SensorRec.DataFormat.ModifierUse = SAHPI_SMUU_NONE
rpt.RdrTypeUnion.SensorRec.DataFormat.Percentage = SAHPI_FALSE
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Flags = SAHPI_SRF_MIN | SAHPI_SRF_MAX
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Max.ISSupported = SAHPI_TRUE
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Max.Type = SAHPI_SENSOR_READING_TYPE_FLOAT64
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Max.Value.SensorFloat64 = 1.0
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Min.ISSupported = SAHPI_TRUE
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Min.Type = SAHPI_SENSOR_READING_TYPE_FLOAT64
rpt.RdrTypeUnion.SensorRec.DataFormat.Range.Min.Value.SensorFloat64 = 0.0

rpt.RdrTypeUnion.SensorRec.Oem = 7

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 22
rpt.IdString.Data = "Sensor 2 for Chassis."
 
sensors.append(rpt)
 
 #**********************CONTROLS********************

num_controls=5 
controls=[] 

# Control RDR 1
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_CTRL_RDR

##rpt.Entity = SaHpiEntityT()

rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.Entity.Entry[0].EntityLocation = 14
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.Entity.Entry[1].EntityLocation = 1
rpt.Entity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[2].EntityLocation = 1
rpt.Entity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[3].EntityLocation = 0

#rpt.RdrTypeUnion.CtrlRec = SaHpiCtrlRecT()

rpt.RdrTypeUnion.CtrlRec.Num = 1
rpt.RdrTypeUnion.CtrlRec.OutputType = SAHPI_CTRL_GENERIC
rpt.RdrTypeUnion.CtrlRec.Type = SAHPI_CTRL_TYPE_DIGITAL
rpt.RdrTypeUnion.CtrlRec.TypeUnion.Digital.Default = SAHPI_CTRL_STATE_OFF
rpt.RdrTypeUnion.CtrlRec.DefaultMode.Mode = SAHPI_CTRL_MODE_MANUAL
rpt.RdrTypeUnion.CtrlRec.DefaultMode.ReadOnly = SAHPI_TRUE
rpt.RdrTypeUnion.CtrlRec.WriteOnly = SAHPI_FALSE
rpt.RdrTypeUnion.CtrlRec.Oem = 1

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 23
rpt.IdString.Data = "Control 1 for Blade 14."

controls.append(rpt)
 
# Control RDR 2 
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_CTRL_RDR

##rpt.Entity = SaHpiEntityT()

rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.Entity.Entry[0].EntityLocation = 14
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.Entity.Entry[1].EntityLocation = 1
rpt.Entity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[2].EntityLocation = 1
rpt.Entity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[3].EntityLocation = 0

#rpt.RdrTypeUnion.CtrlRec = SaHpiCtrlRecT()

rpt.RdrTypeUnion.CtrlRec.Num = 2
rpt.RdrTypeUnion.CtrlRec.OutputType = SAHPI_CTRL_GENERIC
rpt.RdrTypeUnion.CtrlRec.Type = SAHPI_CTRL_TYPE_DIGITAL

rpt.RdrTypeUnion.CtrlRec.TypeUnion.Digital.Default = SAHPI_CTRL_STATE_OFF
rpt.RdrTypeUnion.CtrlRec.DefaultMode.Mode = SAHPI_CTRL_MODE_MANUAL
rpt.RdrTypeUnion.CtrlRec.DefaultMode.ReadOnly = SAHPI_TRUE
rpt.RdrTypeUnion.CtrlRec.WriteOnly = SAHPI_FALSE
rpt.RdrTypeUnion.CtrlRec.Oem = 2

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 23
rpt.IdString.Data = "Control 2 for Blade 14."
 
controls.append(rpt)
 
# Control RDR 3 
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_CTRL_RDR

##rpt.Entity = SaHpiEntityT()

rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.Entity.Entry[0].EntityLocation = 14
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.Entity.Entry[1].EntityLocation = 1
rpt.Entity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[2].EntityLocation = 1
rpt.Entity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[3].EntityLocation = 0

#rpt.RdrTypeUnion.CtrlRec = SaHpiCtrlRecT()

rpt.RdrTypeUnion.CtrlRec.Num = 3
rpt.RdrTypeUnion.CtrlRec.OutputType = SAHPI_CTRL_GENERIC
rpt.RdrTypeUnion.CtrlRec.Type = SAHPI_CTRL_TYPE_DIGITAL

rpt.RdrTypeUnion.CtrlRec.TypeUnion.Digital.Default = SAHPI_CTRL_STATE_OFF
rpt.RdrTypeUnion.CtrlRec.DefaultMode.Mode = SAHPI_CTRL_MODE_MANUAL
rpt.RdrTypeUnion.CtrlRec.DefaultMode.ReadOnly = SAHPI_TRUE
rpt.RdrTypeUnion.CtrlRec.WriteOnly = SAHPI_FALSE
rpt.RdrTypeUnion.CtrlRec.Oem = 3

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 23
rpt.IdString.Data = "Control 3 for Blade 14."

controls.append(rpt)
 
 # Control RDR 4
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_CTRL_RDR

##rpt.Entity = SaHpiEntityT()

rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.Entity.Entry[0].EntityLocation = 14
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.Entity.Entry[1].EntityLocation = 1
rpt.Entity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[2].EntityLocation = 1
rpt.Entity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[3].EntityLocation = 0

#rpt.RdrTypeUnion.CtrlRec = SaHpiCtrlRecT()
rpt.RdrTypeUnion.CtrlRec.Num = 4
rpt.RdrTypeUnion.CtrlRec.OutputType = SAHPI_CTRL_GENERIC
rpt.RdrTypeUnion.CtrlRec.Type = SAHPI_CTRL_TYPE_DIGITAL

rpt.RdrTypeUnion.CtrlRec.TypeUnion.Digital.Default = SAHPI_CTRL_STATE_OFF
rpt.RdrTypeUnion.CtrlRec.DefaultMode.Mode = SAHPI_CTRL_MODE_MANUAL
rpt.RdrTypeUnion.CtrlRec.DefaultMode.ReadOnly = SAHPI_TRUE
rpt.RdrTypeUnion.CtrlRec.WriteOnly = SAHPI_FALSE
rpt.RdrTypeUnion.CtrlRec.Oem = 4

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 23
rpt.IdString.Data = "Control 4 for Blade 14."

controls.append(rpt)
 
# Control RDR 5 
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_CTRL_RDR

##rpt.Entity = SaHpiEntityT()

rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.Entity.Entry[0].EntityLocation = 14
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.Entity.Entry[1].EntityLocation = 1
rpt.Entity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[2].EntityLocation = 1
rpt.Entity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[3].EntityLocation = 0

##rpt.RdrTypeUnion.CtrlRec = SaHpiCtrlRecT()
rpt.RdrTypeUnion.CtrlRec.Num = 5
rpt.RdrTypeUnion.CtrlRec.OutputType = SAHPI_CTRL_GENERIC
rpt.RdrTypeUnion.CtrlRec.Type = SAHPI_CTRL_TYPE_DIGITAL

rpt.RdrTypeUnion.CtrlRec.TypeUnion.Digital.Default = SAHPI_CTRL_STATE_OFF
rpt.RdrTypeUnion.CtrlRec.DefaultMode.Mode = SAHPI_CTRL_MODE_MANUAL
rpt.RdrTypeUnion.CtrlRec.DefaultMode.ReadOnly = SAHPI_TRUE
rpt.RdrTypeUnion.CtrlRec.WriteOnly = SAHPI_FALSE
rpt.RdrTypeUnion.CtrlRec.Oem = 5

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 23
rpt.IdString.Data = "Control 5 for Blade 14."

controls.append(rpt)

#**********************INVENTORIES********************
# Inventory RDR 1

num_inventories=5
inventories= []
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_INVENTORY_RDR

##rpt.Entity = SaHpiEntityT()

rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.Entity.Entry[0].EntityLocation = 14
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.Entity.Entry[1].EntityLocation = 1
rpt.Entity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[2].EntityLocation = 1
rpt.Entity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[3].EntityLocation = 0

rpt.RdrTypeUnion.InventoryRec.IdrId = 1
rpt.RdrTypeUnion.InventoryRec.Persistent = SAHPI_TRUE
rpt.RdrTypeUnion.InventoryRec.Oem = 1

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 25
rpt.IdString.Data = "Inventory 1 for Blade 14."
 
inventories.append(rpt)

# Inventory RDR 2
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_INVENTORY_RDR

##rpt.Entity = SaHpiEntityT()

rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.Entity.Entry[0].EntityLocation = 14
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.Entity.Entry[1].EntityLocation = 1
rpt.Entity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[2].EntityLocation = 1
rpt.Entity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[3].EntityLocation = 0

rpt.RdrTypeUnion.InventoryRec.IdrId = 2
rpt.RdrTypeUnion.InventoryRec.Persistent = SAHPI_TRUE
rpt.RdrTypeUnion.InventoryRec.Oem = 2

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 25
rpt.IdString.Data = "Inventory 2 for Blade 14."

inventories.append(rpt)

# Inventory RDR 3
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_INVENTORY_RDR

##rpt.Entity = SaHpiEntityT()

rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.Entity.Entry[0].EntityLocation = 14
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.Entity.Entry[1].EntityLocation = 1
rpt.Entity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[2].EntityLocation = 1
rpt.Entity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[3].EntityLocation = 0

rpt.RdrTypeUnion.InventoryRec.IdrId = 3
rpt.RdrTypeUnion.InventoryRec.Persistent = SAHPI_TRUE
rpt.RdrTypeUnion.InventoryRec.Oem = 3

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 25
rpt.IdString.Data = "Inventory 3 for Blade 14."

inventories.append(rpt)

# Inventory RDR 4
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_INVENTORY_RDR

##rpt.Entity = SaHpiEntityT()

rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.Entity.Entry[0].EntityLocation = 14
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.Entity.Entry[1].EntityLocation = 1
rpt.Entity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[2].EntityLocation = 1
rpt.Entity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[3].EntityLocation = 0

rpt.RdrTypeUnion.InventoryRec.IdrId = 4
rpt.RdrTypeUnion.InventoryRec.Persistent = SAHPI_TRUE
rpt.RdrTypeUnion.InventoryRec.Oem = 4

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 25
rpt.IdString.Data = "Inventory 4 for Blade 14."

inventories.append(rpt)

# Inventory RDR 5
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_INVENTORY_RDR

##rpt.Entity = SaHpiEntityT()

rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.Entity.Entry[0].EntityLocation = 14
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.Entity.Entry[1].EntityLocation = 1
rpt.Entity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[2].EntityLocation = 1
rpt.Entity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[3].EntityLocation = 0

rpt.RdrTypeUnion.InventoryRec.IdrId = 5
rpt.RdrTypeUnion.InventoryRec.Persistent = SAHPI_TRUE
rpt.RdrTypeUnion.InventoryRec.Oem = 5

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 25
rpt.IdString.Data = "Inventory 5 for Blade 14."

inventories.append(rpt)

#**********************WATCHDOG********************

num_watchdogs=5
watchdogs=[]
# Watchdog RDR 1
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_WATCHDOG_RDR

##rpt.Entity = SaHpiEntityT()

rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.Entity.Entry[0].EntityLocation = 14
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.Entity.Entry[1].EntityLocation = 1
rpt.Entity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[2].EntityLocation = 1
rpt.Entity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[3].EntityLocation = 0

rpt.RdrTypeUnion.WatchdogRec.WatchdogNum = 1
rpt.RdrTypeUnion.WatchdogRec.Oem = 1

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 24
rpt.IdString.Data = "Watchdog 1 for Blade 14."

watchdogs.append(rpt)

# Watchdog RDR 2
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_WATCHDOG_RDR

##rpt.Entity = SaHpiEntityT()

rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.Entity.Entry[0].EntityLocation = 14
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.Entity.Entry[1].EntityLocation = 1
rpt.Entity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[2].EntityLocation = 1
rpt.Entity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[3].EntityLocation = 0

rpt.RdrTypeUnion.WatchdogRec.WatchdogNum = 2
rpt.RdrTypeUnion.WatchdogRec.Oem = 2

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 24
rpt.IdString.Data = "Watchdog 2 for Blade 14."

watchdogs.append(rpt)

# Watchdog RDR 3
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_WATCHDOG_RDR

##rpt.Entity = SaHpiEntityT()

rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.Entity.Entry[0].EntityLocation = 14
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.Entity.Entry[1].EntityLocation = 1
rpt.Entity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[2].EntityLocation = 1
rpt.Entity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[3].EntityLocation = 0

rpt.RdrTypeUnion.WatchdogRec.WatchdogNum = 3
rpt.RdrTypeUnion.WatchdogRec.Oem = 3

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 24
rpt.IdString.Data = "Watchdog 3 for Blade 14."

watchdogs.append(rpt)

# Watchdog RDR 4
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_WATCHDOG_RDR

##rpt.Entity = SaHpiEntityT()

rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.Entity.Entry[0].EntityLocation = 14
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.Entity.Entry[1].EntityLocation = 1
rpt.Entity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[2].EntityLocation = 1
rpt.Entity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[3].EntityLocation = 0

rpt.RdrTypeUnion.WatchdogRec.WatchdogNum = 4
rpt.RdrTypeUnion.WatchdogRec.Oem = 4

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 24
rpt.IdString.Data = "Watchdog 4 for Blade 14."

watchdogs.append(rpt)

# Watchdog RDR 5
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_WATCHDOG_RDR

##rpt.Entity = SaHpiEntityT()

rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.Entity.Entry[0].EntityLocation = 14
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.Entity.Entry[1].EntityLocation = 1
rpt.Entity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[2].EntityLocation = 1
rpt.Entity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[3].EntityLocation = 0

rpt.RdrTypeUnion.WatchdogRec.WatchdogNum = 5
rpt.RdrTypeUnion.WatchdogRec.Oem = 5

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 24
rpt.IdString.Data = "Watchdog 5 for Blade 14."

watchdogs.append(rpt)


#**********************ANNUNCIATOR********************


num_annunciators=5
annunciators=[] 

# Annunciator RDR 1
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_ANNUNCIATOR_RDR

##rpt.Entity = SaHpiEntityT()

rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.Entity.Entry[0].EntityLocation = 14
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.Entity.Entry[1].EntityLocation = 1
rpt.Entity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[2].EntityLocation = 1
rpt.Entity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[3].EntityLocation = 0

rpt.RdrTypeUnion.AnnunciatorRec.AnnunciatorNum = 1
rpt.RdrTypeUnion.AnnunciatorRec.AnnunciatorType = SAHPI_ANNUNCIATOR_TYPE_LED
rpt.RdrTypeUnion.AnnunciatorRec.ModeReadOnly = SAHPI_FALSE
rpt.RdrTypeUnion.AnnunciatorRec.MaxConditions = 2
rpt.RdrTypeUnion.AnnunciatorRec.Oem = 1

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 27
rpt.IdString.Data = "Annunciator 1 for Blade 14."

annunciators.append(rpt)

# Annunciator RDR 2
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_ANNUNCIATOR_RDR

##rpt.Entity = SaHpiEntityT()

rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.Entity.Entry[0].EntityLocation = 14
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.Entity.Entry[1].EntityLocation = 1
rpt.Entity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[2].EntityLocation = 1
rpt.Entity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[3].EntityLocation = 0

rpt.RdrTypeUnion.AnnunciatorRec.AnnunciatorNum = 2
rpt.RdrTypeUnion.AnnunciatorRec.AnnunciatorType = SAHPI_ANNUNCIATOR_TYPE_LED
rpt.RdrTypeUnion.AnnunciatorRec.ModeReadOnly = SAHPI_FALSE
rpt.RdrTypeUnion.AnnunciatorRec.MaxConditions = 2
rpt.RdrTypeUnion.AnnunciatorRec.Oem = 2

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 27
rpt.IdString.Data = "Annunciator 2 for Blade 14."

annunciators.append(rpt)

# Annunciator RDR 3
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_ANNUNCIATOR_RDR

##rpt.Entity = SaHpiEntityT()

rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.Entity.Entry[0].EntityLocation = 14
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.Entity.Entry[1].EntityLocation = 1
rpt.Entity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[2].EntityLocation = 1
rpt.Entity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[3].EntityLocation = 0

rpt.RdrTypeUnion.AnnunciatorRec.AnnunciatorNum = 3
rpt.RdrTypeUnion.AnnunciatorRec.AnnunciatorType = SAHPI_ANNUNCIATOR_TYPE_LED
rpt.RdrTypeUnion.AnnunciatorRec.ModeReadOnly = SAHPI_FALSE
rpt.RdrTypeUnion.AnnunciatorRec.MaxConditions = 2
rpt.RdrTypeUnion.AnnunciatorRec.Oem = 3

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 27
rpt.IdString.Data = "Annunciator 3 for Blade 14."

annunciators.append(rpt)

# Annunciator RDR 4
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_ANNUNCIATOR_RDR

##rpt.Entity = SaHpiEntityT()

rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.Entity.Entry[0].EntityLocation = 14
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.Entity.Entry[1].EntityLocation = 1
rpt.Entity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[2].EntityLocation = 1
rpt.Entity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[3].EntityLocation = 0

rpt.RdrTypeUnion.AnnunciatorRec.AnnunciatorNum = 4
rpt.RdrTypeUnion.AnnunciatorRec.AnnunciatorType = SAHPI_ANNUNCIATOR_TYPE_LED
rpt.RdrTypeUnion.AnnunciatorRec.ModeReadOnly = SAHPI_FALSE
rpt.RdrTypeUnion.AnnunciatorRec.MaxConditions = 2
rpt.RdrTypeUnion.AnnunciatorRec.Oem = 4

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 27
rpt.IdString.Data = "Annunciator 4 for Blade 14."

annunciators.append(rpt)

# Annunciator RDR 5
rpt = SaHpiRdrT()
rpt.RdrType = SAHPI_ANNUNCIATOR_RDR

##rpt.Entity = SaHpiEntityT()

rpt.Entity.Entry[0].EntityType = SAHPI_ENT_SBC_BLADE
rpt.Entity.Entry[0].EntityLocation = 14
rpt.Entity.Entry[1].EntityType = SAHPI_ENT_SUB_CHASSIS
rpt.Entity.Entry[1].EntityLocation = 1
rpt.Entity.Entry[2].EntityType = SAHPI_ENT_SYSTEM_CHASSIS
rpt.Entity.Entry[2].EntityLocation = 1
rpt.Entity.Entry[3].EntityType = SAHPI_ENT_ROOT
rpt.Entity.Entry[3].EntityLocation = 0

rpt.RdrTypeUnion.AnnunciatorRec.AnnunciatorNum = 5
rpt.RdrTypeUnion.AnnunciatorRec.AnnunciatorType = SAHPI_ANNUNCIATOR_TYPE_LED
rpt.RdrTypeUnion.AnnunciatorRec.ModeReadOnly = SAHPI_FALSE
rpt.RdrTypeUnion.AnnunciatorRec.MaxConditions = 2
rpt.RdrTypeUnion.AnnunciatorRec.Oem = 5

rpt.IdString.DataType = SAHPI_TL_TYPE_TEXT
rpt.IdString.Language = SAHPI_LANG_ENGLISH
rpt.IdString.DataLength = 27
rpt.IdString.Data = "Annunciator 5 for Blade 14."

annunciators.append(rpt)
#end  RPT_RESOURCES

