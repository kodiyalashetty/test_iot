#!/usr/bin/python
from openhpi import *

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

rpt.ResourceEntity = SaHpiEntityPathT()
#rpt.ResourceEntity.Entry = SaHpiEntityT()
rpt.ResourceEntity.Entry[0] = [SAHPI_ENT_SBC_BLADE,14]
rpt.ResourceEntity.Entry[1] = [SAHPI_ENT_SBC_BLADE,14]
rpt.ResourceEntity.Entry[2] = [SAHPI_ENT_SUB_CHASSIS,1]
rpt.ResourceEntity.Entry[3] = [SAHPI_ENT_SYSTEM_CHASSIS,1]
rpt.ResourceEntity.Entry[4] = [ SAHPI_ENT_ROOT,0]

rpt.ResourceCapabilities = rpt.ResourceCapabilities = SAHPI_CAPABILITY_CONTROL |SAHPI_CAPABILITY_FRU |SAHPI_CAPABILITY_INVENTORY_DATA |SAHPI_CAPABILITY_RDR |SAHPI_CAPABILITY_RESOURCE |SAHPI_CAPABILITY_SENSOR

rpt.ResourceSeverity = SAHPI_MAJOR

#rpt.ResourceTag = SaHpiTextBufferT()
rpt.ResourceTag.DataType = SAHPI_TL_TYPE_TEXT
rpt.ResourceTag.Language = SAHPI_LANG_ENGLISH
rpt.ResourceTag.DataLength = 26
rpt.ResourceTag.Data = "This is data for blade 14."

rptentries.append(rpt)

