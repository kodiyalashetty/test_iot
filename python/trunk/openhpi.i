%module openhpi
%{
#include <SaHpi.h>
#include <SaHpiAtca.h>
#include <SaHpiBladeCenter.h>
#include <oHpi.h>
#include <oh_utils.h>
#include <string.h>
%}
int memcmp(const void *s1, const void *s2, size_t n);
%include "typemaps.i"
/* SaHpi.h, SaHpiAtca.h, SaHpiBladeCenter.h typemaps */
%apply unsigned int *OUTPUT { SaHpiSessionIdT *SessionId }
%typemap (default) void *SecurityParams {
	$1 = NULL;
}
%apply unsigned int *INOUT { SaHpiUint32T *InstanceId }
%apply unsigned int *OUTPUT { SaHpiInstrumentIdT *InstrumentId }
%apply unsigned int *OUTPUT { SaHpiUint32T *RptUpdateCount }
%apply unsigned int *OUTPUT { SaHpiEventLogCapabilitiesT *EventLogCapabilities }
%apply unsigned int *OUTPUT { SaHpiEvtQueueStatusT *EventQueueStatus }
%apply unsigned int *OUTPUT { SaHpiEntryIdT *NextEntryId }
%apply unsigned int *OUTPUT { SaHpiEntryIdT *NextAreaId }
%apply unsigned int *OUTPUT { SaHpiEntryIdT *AreaId }
%apply unsigned int *OUTPUT { SaHpiEntryIdT *NextFieldId }
%apply unsigned int *OUTPUT { SaHpiResourceIdT *ResourceId }
%apply unsigned int *OUTPUT { SaHpiEventLogEntryIdT *PrevEntryId }
%apply unsigned int *OUTPUT { SaHpiEventLogEntryIdT *NextEntryId }
%apply long long *OUTPUT { SaHpiTimeT *Time }
%apply unsigned char *OUTPUT { SaHpiBoolT *EnableState }
%apply unsigned char *OUTPUT { SaHpiBoolT *SensorEnabled }
%apply unsigned char *OUTPUT { SaHpiBoolT *SensorEventsEnabled }
%apply unsigned short *OUTPUT { SaHpiEventStateT *EventState }
%apply unsigned short *OUTPUT { SaHpiEventStateT *AssertEventMask }
%apply unsigned short *OUTPUT { SaHpiEventStateT *DeassertEventMask }
%apply int *OUTPUT { SaHpiSensorTypeT *Type }
%apply unsigned char *OUTPUT { SaHpiEventCategoryT *Category }
%apply int *OUTPUT { SaHpiCtrlTypeT *Type }
%apply int *OUTPUT { SaHpiCtrlModeT *CtrlMode }
%apply int *OUTPUT { SaHpiAnnunciatorModeT *Mode }
%apply long long *OUTPUT { SaHpiTimeoutT *Timeout }
%apply int *OUTPUT { SaHpiHsStateT *State }
%apply int *OUTPUT { SaHpiHsIndicatorStateT *State }
%apply int *OUTPUT { SaHpiResetActionT *ResetAction }
%apply int *OUTPUT { SaHpiPowerStateT *State }
%apply unsigned int *OUTPUT { SaHpiDimiReadyT *DimiReady }
%apply unsigned char *OUTPUT { SaHpiDimiTestPercentCompletedT *PercentCompleted }
%apply unsigned int *OUTPUT { SaHpiDimiTestRunStatusT *RunStatus }
%apply unsigned int *OUTPUT { SaHpiFumiUpgradeStatusT *UpgradeStatus }
%typemap (in) SaHpiUint8T Data[ANY] (int datalen) {
	datalen = PyString_Size($input);
	if (!PyString_Check($input)) {
		PyErr_SetString(PyExc_ValueError, "Expected a string");
		return NULL;
	}
	if (datalen > $1_dim0) {
		PyErr_SetString(PyExc_ValueError, "Size mismatch. Expected no more than SAHPI_MAX_TEXT_BUFFER_LENGTH characters");
		return NULL;
	}
	$1 = (SaHpiUint8T *)PyString_AsString($input);        
}
%typemap (memberin) SaHpiUint8T Data[ANY] {
	memset($1, 0, $1_dim0);
	memcpy($1, $input, datalen2);
}
%typemap (out) SaHpiUint8T Data[ANY] {
	$result = PyString_FromStringAndSize((char *)$1, arg1->DataLength);
}
%typemap (in) SaHpiUint8T ConfigData[ANY] (int datalen) {
	datalen = PyString_Size($input);
	if (!PyString_Check($input)) {
		PyErr_SetString(PyExc_ValueError, "Expected a string");
                return NULL;
	}
	if (datalen > $1_dim0) {
		PyErr_SetString(PyExc_ValueError, "Size mismatch. Got more characters than expected. Check SaHpi.h for correct length maximum.");
                return NULL;
	}
	$1 = (SaHpiUint8T *)PyString_AsString($input);
}
%typemap (memberin) SaHpiUint8T ConfigData[ANY] {
	memset($1, 0, $1_dim0);
	memcpy($1, $input, datalen2);
}
%typemap (out) SaHpiUint8T ConfigData[ANY] {
	int datalen = $1_dim0, i;
	for (i = datalen-1; i > -1; i--) {
		if ($1[i] != '\0') break;
	}
	if (i < 0) i = 0;
	else i = i + 1;
	$result = PyString_FromStringAndSize((char *)$1, i);
}
%typemap (in) unsigned char Value[ANY] (int datalen) {
	datalen = PyString_Size($input);
	if (!PyString_Check($input)) {
		PyErr_SetString(PyExc_ValueError, "Expected a string");
		return NULL;
	}
	if (datalen > $1_dim0) {
		PyErr_SetString(PyExc_ValueError, "Size mismatch. Expected no more than SA_HPI_MAX_NAME_LENGTH characters");
		return NULL;
	}
	$1 = (unsigned char *)PyString_AsString($input);
	arg1->Length = datalen;
}
%typemap (memberin) unsigned char Value[ANY] {
	memset($1, 0, $1_dim0);
	memcpy($1, $input, datalen2);
}
%typemap (out) unsigned char Value[ANY] {
	$result = PyString_FromStringAndSize((char *)$1, arg1->Length);
}
%typemap (in) SaHpiUint8T Body[ANY] (int datalen) {
	datalen = PyString_Size($input);
	if (!PyString_Check($input)) {
		PyErr_SetString(PyExc_ValueError, "Expected a string");
		return NULL;
	}
	if (datalen > $1_dim0) {
		PyErr_SetString(PyExc_ValueError, "Size mismatch. Expected no more than SAHPI_CTRL_MAX_OEM_BODY_LENGTH characters");
		return NULL;
	}
	$1 = (SaHpiUint8T *)PyString_AsString($input);
}
%typemap (memberin) SaHpiUint8T Body[ANY] {
	memset($1, 0, $1_dim0);
	memcpy($1, $input, datalen2);
}
%typemap (out) SaHpiUint8T Body[ANY] {
	$result = PyString_FromStringAndSize((char *)$1, arg1->BodyLength);
}
%apply SaHpiUint8T ConfigData[ANY] { SaHpiUint8T SensorBuffer[ANY] }
%typemap (in) SaHpiUint8T Stream[ANY] (int datalen) {
	datalen = PyString_Size($input);
	if (!PyString_Check($input)) {
		PyErr_SetString(PyExc_ValueError, "Expected a string");
		return NULL;
	}
	if (datalen > $1_dim0) {
		PyErr_SetString(PyExc_ValueError, "Size mismatch. Expected no more than SAHPI_CTRL_MAX_STREAM_LENGTH characters");
		return NULL;
	}
	$1 = (SaHpiUint8T *)PyString_AsString($input);
}
%typemap (memberin) SaHpiUint8T Stream[ANY] {
	memset($1, 0, $1_dim0);
	memcpy($1, $input, datalen2);
}
%typemap (out) SaHpiUint8T Stream[ANY] {
	$result = PyString_FromStringAndSize((char *)$1, arg1->StreamLength);
}
%typemap (in) SaHpiGuidT (int datalen) {
	datalen = PyString_Size($input);
	if (!PyString_Check($input)) {
		PyErr_SetString(PyExc_ValueError, "Expected a string");
		return NULL;
	}
	if (datalen > 16) {
		PyErr_SetString(PyExc_ValueError, "Size mismatch. Expected no more than 16 characters");
		return NULL;
	}
	$1 = (SaHpiUint8T *)PyString_AsString($input);
}
%typemap (memberin) SaHpiGuidT {
	memset($1, 0, 16);
	memcpy($1, $input, datalen2);
}
%typemap (out) SaHpiGuidT {
	$result = PyString_FromStringAndSize((char *)$1, 16);
}
%typemap (in) SaHpiEntityT Entry[ANY] {
	int i, datalen;
	SaHpiEntityT temp[SAHPI_MAX_ENTITY_PATH];
	memset(temp, 0, sizeof(SaHpiEntityT)*SAHPI_MAX_ENTITY_PATH);
	datalen = PyList_Size($input);
	if (!PyList_Check($input)) {
		PyErr_SetString(PyExc_ValueError, "Expected a list");
		return NULL;
	}
	if (datalen > $1_dim0) {
		PyErr_SetString(PyExc_ValueError, "Size mismatch. Expected no more than 16 elements");
		return NULL;
	}
	for (i = 0; i < datalen; i++) {
		PyObject *o = PyList_GetItem($input, i);
		SaHpiEntityT *entry = NULL;
		int conv_res = SWIG_ConvertPtr(o, (void *)(void *)&entry, SWIGTYPE_p_SaHpiEntityT, 0 |  0 );
		if (!SWIG_IsOK(conv_res)) {
  			SWIG_exception_fail(SWIG_ArgError(conv_res),
				"List element is not of SaHpiEntityT type");

		} else {
			temp[i].EntityType = entry->EntityType;
			temp[i].EntityLocation = entry->EntityLocation;
		}
	}
	$1 = temp;
}
%typemap (memberin) SaHpiEntityT Entry[ANY] {
	memcpy($1, $input, sizeof(SaHpiEntityT)*$1_dim0);
}
%typemap (out) SaHpiEntityT Entry[ANY] {
	int i;
	$result = PyList_New($1_dim0);
	for (i = 0; i < $1_dim0; i++) {
  		PyObject *entityobj = SWIG_NewPointerObj(SWIG_as_voidptr(&$1[i]),
					                 SWIGTYPE_p_SaHpiEntityT,
					                 0);
		PyList_SetItem($result, i, entityobj);
	}
}
%typemap (in) SaHpiUint8T ParamName[ANY] (int datalen) {
        datalen = PyString_Size($input);
        if (!PyString_Check($input)) {
                PyErr_SetString(PyExc_ValueError, "Expected a string");
                return NULL;
        }
        if (datalen > $1_dim0) {
                PyErr_SetString(PyExc_ValueError, "Size mismatch. Expected no more than SAHPI_DIMITEST_PARAM_NAME_LEN characters");
                return NULL;
        }
        $1 = (SaHpiUint8T *)PyString_AsString($input);
}
%typemap (memberin) SaHpiUint8T ParamName[ANY] {
        memset($1, 0, $1_dim0);
        memcpy($1, $input, datalen2);
}
%typemap (out) SaHpiUint8T ParamName[ANY] {
        $result = PyString_FromStringAndSize((char *)$1, strnlen((char *)$1, SAHPI_DIMITEST_PARAM_NAME_LEN));
}
%typemap (in) SaHpiDimiTestAffectedEntityT EntitiesImpacted[ANY] {
        int i, datalen;
        SaHpiDimiTestAffectedEntityT temp[SAHPI_DIMITEST_MAX_ENTITIESIMPACTED];
        memset(temp, 0, sizeof(SaHpiDimiTestAffectedEntityT)*SAHPI_DIMITEST_MAX_ENTITIESIMPACTED);
        datalen = PyList_Size($input);
        if (!PyList_Check($input)) {
                PyErr_SetString(PyExc_ValueError, "Expected a list");
                return NULL;
        }
        if (datalen > $1_dim0) {
                PyErr_SetString(PyExc_ValueError, "Size mismatch. Expected no more than 16 elements");
                return NULL;
        }
        for (i = 0; i < datalen; i++) {
                PyObject *o = PyList_GetItem($input, i);
                SaHpiDimiTestAffectedEntityT *entry = NULL;
                int conv_res = SWIG_ConvertPtr(o, (void *)(void *)&entry, SWIGTYPE_p_SaHpiDimiTestAffectedEntityT, 0 |  0 );
                if (!SWIG_IsOK(conv_res)) {
                        SWIG_exception_fail(SWIG_ArgError(conv_res),
                                "List element is not of SaHpiDimiTestAffectedEntityT type");

                } else {
                        temp[i].EntityImpacted = entry->EntityImpacted;
                        temp[i].ServiceImpact = entry->ServiceImpact;
                }
        }
        $1 = temp;
}
%typemap (memberin) SaHpiDimiTestAffectedEntityT EntitiesImpacted[ANY] {
        memcpy($1, $input, sizeof(SaHpiDimiTestAffectedEntityT)*$1_dim0);
}
%typemap (out) SaHpiDimiTestAffectedEntityT EntitiesImpacted[ANY] {
        int i;
        $result = PyList_New($1_dim0);
        for (i = 0; i < $1_dim0; i++) {
                PyObject *entityobj = SWIG_NewPointerObj(SWIG_as_voidptr(&$1[i]),
                                                         SWIGTYPE_p_SaHpiDimiTestAffectedEntityT,
                                                         0);
                PyList_SetItem($result, i, entityobj);
        }
}
%typemap (in) SaHpiDimiTestParamsDefinitionT TestParameters[ANY] {
        int i, datalen;
        SaHpiDimiTestParamsDefinitionT temp[SAHPI_DIMITEST_MAX_PARAMETERS];
        memset(temp, 0, sizeof(SaHpiDimiTestParamsDefinitionT)*SAHPI_DIMITEST_MAX_PARAMETERS);
        datalen = PyList_Size($input);
        if (!PyList_Check($input)) {
                PyErr_SetString(PyExc_ValueError, "Expected a list");
                return NULL;
        }
        if (datalen > $1_dim0) {
                PyErr_SetString(PyExc_ValueError, "Size mismatch. Expected no more than 16 elements");
                return NULL;
        }
        for (i = 0; i < datalen; i++) {
                PyObject *o = PyList_GetItem($input, i);
                SaHpiDimiTestParamsDefinitionT *entry = NULL;
                int conv_res = SWIG_ConvertPtr(o, (void *)(void *)&entry, SWIGTYPE_p_SaHpiDimiTestParamsDefinitionT, 0 |  0 );
                if (!SWIG_IsOK(conv_res)) {
                        SWIG_exception_fail(SWIG_ArgError(conv_res),
                                "List element is not of SaHpiDimiTestParamsDefinitionT type");

                } else {
                        strncpy((char *)temp[i].ParamName, (char *)entry->ParamName, SAHPI_DIMITEST_PARAM_NAME_LEN);
                        temp[i].ParamInfo = entry->ParamInfo;
                        temp[i].ParamType = entry->ParamType;
                        temp[i].MinValue = entry->MinValue;
                        temp[i].MaxValue = entry->MaxValue;
                        temp[i].DefaultParam = entry->DefaultParam;
                }
        }
        $1 = temp;
}
%typemap (memberin) SaHpiDimiTestParamsDefinitionT TestParameters[ANY] {
        memcpy($1, $input, sizeof(SaHpiDimiTestParamsDefinitionT)*$1_dim0);
}
%typemap (out) SaHpiDimiTestParamsDefinitionT TestParameters[ANY] {
        int i;
        $result = PyList_New($1_dim0);
        for (i = 0; i < $1_dim0; i++) {
                PyObject *entityobj = SWIG_NewPointerObj(SWIG_as_voidptr(&$1[i]),
                                                         SWIGTYPE_p_SaHpiDimiTestParamsDefinitionT,
                                                         0);
                PyList_SetItem($result, i, entityobj);
        }
}
%typemap (in) SaHpiDimiTestVariableParamsT *ParamsList (SaHpiDimiTestVariableParamsT *params) {
        int pos = 0;
        PyObject *value = 0;
        if ($input == Py_None) {
                params = NULL;
        } else {
                if (!PyList_Check($input)) {
                        PyErr_SetString(PyExc_ValueError, "Expected a list");
                        return NULL;
                }
                params = (SaHpiDimiTestVariableParamsT *)malloc(sizeof(SaHpiDimiTestVariableParamsT)*PyList_Size($input));
        
                for (pos = 0; pos < PyList_Size($input); pos++) {
                        value = PyList_GetItem($input, pos);
                        SaHpiDimiTestVariableParamsT *param = NULL;
                        int conv_res = SWIG_ConvertPtr(value,
                                (void *)(void *)&param,
                                SWIGTYPE_p_SaHpiDimiTestVariableParamsT,
                                0 |  0 );
                        if (!SWIG_IsOK(conv_res)) {
                                SWIG_exception_fail(SWIG_ArgError(conv_res),
                                "List element is not of SaHpiDimiTestVariableParamsT type");

                        } else {
                                params[pos] = *param;
                        }
                }
        }
        $1 = params;
}
%include "sahpi.i"
%include "sahpiatca.i"
%include "sahpibladecenter.i"
/* oHpi.h typemaps */
%apply unsigned int *OUTPUT { oHpiHandlerIdT *next_id }
%apply unsigned int *OUTPUT { oHpiHandlerIdT *id }
%typemap (in) GHashTable *config (GHashTable *stanza) {
	int pos = 0;
	PyObject *key = NULL, *value = 0;
	if (!PyDict_Check($input)) {
		PyErr_SetString(PyExc_ValueError, "Expected a dictionary");
		return NULL;
	}
	stanza = g_hash_table_new_full(g_str_hash, g_str_equal,
                                       g_free, g_free);
	while (PyDict_Next($input, &pos, &key, &value)) {
		if (!PyString_Check(key) || !PyString_Check(value)) {
			PyErr_SetString(PyExc_ValueError, "Expected strings in the dictionary");
			g_hash_table_destroy(stanza);
			return NULL;
		}
		g_hash_table_insert(stanza,
				    g_strdup(PyString_AsString(key)),
				    g_strdup(PyString_AsString(value)));
	}
	$1 = stanza;
}
%include "ohpi.i"
/* SaHpi Utils typemaps */
%apply char * { gchar * }
%apply long long *OUTPUT { SaHpiTimeT *time }
%include "sahpi_time_utils.i"
%apply unsigned short *OUTPUT { SaHpiEventStateT *event_state }
%apply unsigned char *OUTPUT { SaHpiEventCategoryT *event_cat }
%include "sahpi_event_utils.i"
%include "sahpi_struct_utils.i"
%apply int *OUTPUT { SaHpiLanguageT *type }
%apply int *OUTPUT { SaHpiTextTypeT *type }
%apply int *OUTPUT { SaHpiEntityTypeT *type }
%apply int *OUTPUT { SaHpiSensorTypeT *type }
%apply int *OUTPUT { SaHpiSensorReadingTypeT *type }
%apply int *OUTPUT { SaHpiSensorEventMaskActionT *type }
%apply int *OUTPUT { SaHpiSensorUnitsT *type }
%apply int *OUTPUT { SaHpiSensorModUnitUseT *type }
%apply int *OUTPUT { SaHpiSensorEventCtrlT *type }
%apply int *OUTPUT { SaHpiCtrlTypeT *type }
%apply int *OUTPUT { SaHpiCtrlStateDigitalT *type }
%apply int *OUTPUT { SaHpiCtrlModeT *type }
%apply int *OUTPUT { SaHpiCtrlOutputTypeT *type }
%apply int *OUTPUT { SaHpiIdrAreaTypeT *type }
%apply int *OUTPUT { SaHpiIdrFieldTypeT *type }
%apply int *OUTPUT { SaHpiWatchdogActionT *type }
%apply int *OUTPUT { SaHpiWatchdogActionEventT *type }
%apply int *OUTPUT { SaHpiWatchdogPretimerInterruptT *type }
%apply int *OUTPUT { SaHpiWatchdogTimerUseT *type }
%apply int *OUTPUT { SaHpiHsIndicatorStateT *type }
%apply int *OUTPUT { SaHpiHsActionT *type }
%apply int *OUTPUT { SaHpiHsStateT *type }
%apply int *OUTPUT { SaHpiSeverityT *type }
%apply int *OUTPUT { SaHpiResourceEventTypeT *type }
%apply int *OUTPUT { SaHpiDomainEventTypeT *type }
%apply int *OUTPUT { SaHpiSwEventTypeT *type }
%apply int *OUTPUT { SaHpiEventTypeT *type }
%apply int *OUTPUT { SaHpiStatusCondTypeT *type }
%apply int *OUTPUT { SaHpiAnnunciatorModeT *type }
%apply int *OUTPUT { SaHpiAnnunciatorTypeT *type }
%apply int *OUTPUT { SaHpiRdrTypeT *type }
%apply int *OUTPUT { SaHpiParmActionT *type }
%apply int *OUTPUT { SaHpiResetActionT *type }
%apply int *OUTPUT { SaHpiPowerStateT *type }
%apply int *OUTPUT { SaHpiEventLogOverflowActionT *type }
%apply int *OUTPUT { SaErrorT *type }
%apply unsigned char *OUTPUT { SaHpiEventCategoryT *type }
%apply int *OUTPUT { AtcaHpiLedColorT *type }
%apply int *OUTPUT { AtcaHpiResourceLedModeT *type }
%apply int *OUTPUT { AtcaHpiLedBrSupportT *type }
%apply int *OUTPUT { AtcaHpiEntityTypeT *type }
%include "sahpi_enum_utils.i"
%include "sahpiatca_enum_utils.i"
/* OpenHPI Utils typemaps */
%typemap (in) oh_entity_pattern epattern[ANY] {
        int i, datalen;
        oh_entity_pattern temp[SAHPI_MAX_ENTITY_PATH];
        memset(temp, 0, sizeof(oh_entity_pattern)*SAHPI_MAX_ENTITY_PATH);
        datalen = PyList_Size($input);
        if (!PyList_Check($input)) {
                PyErr_SetString(PyExc_ValueError, "Expected a list");
                return NULL;
        }
        if (datalen > $1_dim0) {
                PyErr_SetString(PyExc_ValueError, "Size mismatch. Expected no more than 16 elements");
                return NULL;
        }
        for (i = 0; i < datalen; i++) {
                PyObject *o = PyList_GetItem($input, i);
                oh_entity_pattern *entry = NULL;
                int conv_res = SWIG_ConvertPtr(o, (void *)(void *)&entry, SWIGTYPE_p_oh_entity_pattern, 0 |  0 );
                if (!SWIG_IsOK(conv_res)) {
                        SWIG_exception_fail(SWIG_ArgError(conv_res),
                                "List element is not of oh_entity_pattern type");

                } else {
                        memcpy(temp + i, entry, sizeof(oh_entity_pattern));
                }
        }
        $1 = temp;
}
%typemap (memberin) oh_entity_pattern epattern[ANY] {
        memcpy($1, $input, sizeof(oh_entity_pattern)*$1_dim0);
}
%typemap (out) oh_entity_pattern epattern[ANY] {
        int i;
        $result = PyList_New($1_dim0);
        for (i = 0; i < $1_dim0; i++) {
                PyObject *entityobj = SWIG_NewPointerObj(SWIG_as_voidptr(&$1[i]),
                                                         SWIGTYPE_p_oh_entity_pattern,
                                                         0);
                PyList_SetItem($result, i, entityobj);
        }
}
%include "epath_utils.i"
%include "uid_utils.i"
%typemap (in) GSList **res_new (GSList *new_res, PyListObject *new_res_list) {	
        new_res_list = NULL;
        new_res = NULL;
	$1 = &new_res;
        if (!PyList_Check($input) && $input != Py_None) {
                PyErr_SetString(PyExc_ValueError, "Expected a list or None.");
                return NULL;
        }
        if (PyList_Check($input) && PyList_Size($input) > 0) {
                PyErr_SetString(PyExc_ValueError, "list must be empty.");
                return NULL;
        }
        if ($input == Py_None) {
                $1 = NULL;
        } else {
                new_res_list = (PyListObject *)$input;
        }
}
%typemap (argout) GSList **res_new {
	GSList *node = NULL;
	if (new_res_list3) {
		for (node = *$1; node; node = node->next) {
			PyList_Append((PyObject *)new_res_list3,
                                        SWIG_NewPointerObj(node->data,
						SWIGTYPE_p_SaHpiRptEntryT,0));
		}
	}
        if ($1) g_slist_free(*$1);
}
%typemap (in) GSList **rdr_new (GSList *new_rdr, PyListObject *new_rdr_list) {
        new_rdr_list = NULL;
	new_rdr = NULL;
	$1 = &new_rdr;
        if (!PyList_Check($input) && $input != Py_None) {
                PyErr_SetString(PyExc_ValueError, "Expected a list or None.");
                return NULL;
        }
        if (PyList_Check($input) && PyList_Size($input) > 0) {
                PyErr_SetString(PyExc_ValueError, "list must be empty.");
                return NULL;
        }
        if ($input == Py_None) {
                $1 = NULL;
        } else {
                new_rdr_list = (PyListObject *)$input;
        }
}
%typemap (argout) GSList **rdr_new {
	GSList *node = NULL;
	if (new_rdr_list4) {
		for (node = *$1; node; node = node->next) {
			PyList_Append((PyObject *)new_rdr_list4,
                                        SWIG_NewPointerObj(node->data,
						SWIGTYPE_p_SaHpiRdrT,0));
		}
	}
        if ($1) g_slist_free(*$1);
}
%typemap (in) GSList **res_gone (GSList *gone_res, PyListObject *gone_res_list) {
	gone_res_list = NULL;
	gone_res = NULL;
	$1 = &gone_res;
        if (!PyList_Check($input) && $input != Py_None) {
                PyErr_SetString(PyExc_ValueError, "Expected a list or None.");
                return NULL;
        }
        if (PyList_Check($input) && PyList_Size($input) > 0) {
                PyErr_SetString(PyExc_ValueError, "list must be empty.");
                return NULL;
        }
        if ($input == Py_None) {
                $1 = NULL;
        } else {
                gone_res_list = (PyListObject *)$input;
        }
}
%typemap (argout) GSList **res_gone {
	GSList *node = NULL;
	if (gone_res_list5) {
		for (node = *$1; node; node = node->next) {
			PyList_Append((PyObject *)gone_res_list5,
                                        SWIG_NewPointerObj(node->data,
						SWIGTYPE_p_SaHpiRptEntryT,0));
		}
	}
        if ($1) g_slist_free(*$1);
}
%typemap (in) GSList **rdr_gone (GSList *gone_rdr, PyListObject *gone_rdr_list) {
        gone_rdr_list = NULL;
	gone_rdr = NULL;
	$1 = &gone_rdr;
        if (!PyList_Check($input) && $input != Py_None) {
                PyErr_SetString(PyExc_ValueError, "Expected a list or None.");
                return NULL;
        }
        if (PyList_Check($input) && PyList_Size($input) > 0) {
                PyErr_SetString(PyExc_ValueError, "list must be empty.");
                return NULL;
        }
        if ($input == Py_None) {
                $1 = NULL;
        } else {
                gone_rdr_list = (PyListObject *)$input;
        }
}
%typemap (argout) GSList **rdr_gone {
	GSList *node = NULL;
	if (gone_rdr_list6) {
		for (node = *$1; node; node = node->next) {
			PyList_Append((PyObject *)gone_rdr_list6,
                                        SWIG_NewPointerObj(node->data,
						SWIGTYPE_p_SaHpiRdrT,0));
		}
	}
        if ($1) g_slist_free(*$1);
}
%apply unsigned int *OUTPUT { SaHpiUint32T *update_count }
%apply long long *OUTPUT { SaHpiTimeT *update_timestamp }
%include "rpt_utils.i"
%apply unsigned int *OUTPUT { SaHpiEventLogEntryIdT *prev }
%apply unsigned int *OUTPUT { SaHpiEventLogEntryIdT *next }
%typemap (in, numinputs=0) oh_el_entry **entry (oh_el_entry *elentry) {
	$1 = &elentry;
}
%typemap (argout) oh_el_entry **entry {
	if (PySequence_Check($result)) {
		SWIG_Python_AppendOutput($result,
					 SWIG_NewPointerObj(SWIG_as_voidptr(*$1),
        				                    SWIGTYPE_p_oh_el_entry,0));
	}
}
%include "el_utils.i"
%include "announcement_utils.i"
/* SizeOf for all HPI types */
%include "cmalloc.i"
%sizeof(SaHpiUint64T)
%sizeof(SaHpiInt64T)
%sizeof(SaHpiFloat64T)
%sizeof(SaHpiUint8T)
%sizeof(SaHpiUint16T)
%sizeof(SaHpiUint32T)
%sizeof(SaHpiInt8T)
%sizeof(SaHpiInt16T)
%sizeof(SaHpiInt32T)
%sizeof(SaHpiBoolT)
%sizeof(SaHpiManufacturerIdT)
%sizeof(SaHpiVersionT)
%sizeof(SaErrorT)
%sizeof(SaHpiDomainIdT)
%sizeof(SaHpiSessionIdT)
%sizeof(SaHpiResourceIdT)
%sizeof(SaHpiEntryIdT)
%sizeof(SaHpiTimeT)
%sizeof(SaHpiTimeoutT)
%sizeof(SaHpiLanguageT)
%sizeof(SaHpiTextTypeT)
%sizeof(SaHpiTextBufferT)
%sizeof(SaHpiInstrumentIdT)
%sizeof(SaHpiEntityTypeT)
%sizeof(SaHpiEntityLocationT)
%sizeof(SaHpiEntityT)
%sizeof(SaHpiEntityPathT)
%sizeof(SaHpiEventCategoryT)
%sizeof(SaHpiEventStateT)
%sizeof(SaHpiSensorNumT)
%sizeof(SaHpiSensorTypeT)
%sizeof(SaHpiSensorReadingTypeT)
%sizeof(SaHpiSensorReadingUnionT)
%sizeof(SaHpiSensorReadingT)
%sizeof(SaHpiSensorEventMaskActionT)
%sizeof(SaHpiSensorThresholdsT)
%sizeof(SaHpiSensorRangeFlagsT)
%sizeof(SaHpiSensorRangeT)
%sizeof(SaHpiSensorUnitsT)
%sizeof(SaHpiSensorModUnitUseT)
%sizeof(SaHpiSensorDataFormatT)
%sizeof(SaHpiSensorThdMaskT)
%sizeof(SaHpiSensorThdDefnT)
%sizeof(SaHpiSensorEventCtrlT)
%sizeof(SaHpiSensorRecT)
%sizeof(SaHpiCtrlNumT)
%sizeof(SaHpiCtrlTypeT)
%sizeof(SaHpiCtrlStateDigitalT)
%sizeof(SaHpiCtrlStateDiscreteT)
%sizeof(SaHpiCtrlStateAnalogT)
%sizeof(SaHpiCtrlStateStreamT)
%sizeof(SaHpiTxtLineNumT)
%sizeof(SaHpiCtrlStateTextT)
%sizeof(SaHpiCtrlStateOemT)
%sizeof(SaHpiCtrlStateUnionT)
%sizeof(SaHpiCtrlStateT)
%sizeof(SaHpiCtrlModeT)
%sizeof(SaHpiCtrlOutputTypeT)
%sizeof(SaHpiCtrlRecDigitalT)
%sizeof(SaHpiCtrlRecDiscreteT)
%sizeof(SaHpiCtrlRecAnalogT)
%sizeof(SaHpiCtrlRecStreamT)
%sizeof(SaHpiCtrlRecTextT)
%sizeof(SaHpiCtrlRecOemT)
%sizeof(SaHpiCtrlRecUnionT)
%sizeof(SaHpiCtrlDefaultModeT)
%sizeof(SaHpiCtrlRecT)
%sizeof(SaHpiIdrIdT)
%sizeof(SaHpiIdrAreaTypeT)
%sizeof(SaHpiIdrFieldTypeT)
%sizeof(SaHpiIdrFieldT)
%sizeof(SaHpiIdrAreaHeaderT)
%sizeof(SaHpiIdrInfoT)
%sizeof(SaHpiInventoryRecT)
%sizeof(SaHpiWatchdogNumT)
%sizeof(SaHpiWatchdogActionT)
%sizeof(SaHpiWatchdogActionEventT)
%sizeof(SaHpiWatchdogPretimerInterruptT)
%sizeof(SaHpiWatchdogTimerUseT)
%sizeof(SaHpiWatchdogExpFlagsT)
%sizeof(SaHpiWatchdogT)
%sizeof(SaHpiWatchdogRecT)
%sizeof(SaHpiDimiNumT)
%sizeof(SaHpiDimiTestServiceImpactT)
%sizeof(SaHpiDimiTestAffectedEntityT)
%sizeof(SaHpiDimiTestRunStatusT)
%sizeof(SaHpiDimiTestErrCodeT)
%sizeof(SaHpiDimiTestResultsT)
%sizeof(SaHpiDimiTestParamTypeT)
%sizeof(SaHpiDimiTestParamValueT)
%sizeof(SaHpiDimiTestParameterValueUnionT)
%sizeof(SaHpiDimiTestParamsDefinitionT)
%sizeof(SaHpiDimiTestCapabilityT)
%sizeof(SaHpiDimiTestNumT)
%sizeof(SaHpiDimiTestT)
%sizeof(SaHpiDimiTestVariableParamsT)
%sizeof(SaHpiDimiTestPercentCompletedT)
%sizeof(SaHpiDimiReadyT)
%sizeof(SaHpiDimiTotalTestsT)
%sizeof(SaHpiDimiInfoT)
%sizeof(SaHpiDimiRecT)
%sizeof(SaHpiFumiNumT)
%sizeof(SaHpiBankNumT)
%sizeof(SaHpiFumiSourceStatusT)
%sizeof(SaHpiFumiBankStateT)
%sizeof(SaHpiFumiUpgradeStatusT)
%sizeof(SaHpiFumiSourceInfoT)
%sizeof(SaHpiFumiBankInfoT)
%sizeof(SaHpiFumiProtocolT)
%sizeof(SaHpiFumiCapabilityT)
%sizeof(SaHpiFumiRecT)
%sizeof(SaHpiHsIndicatorStateT)
%sizeof(SaHpiHsActionT)
%sizeof(SaHpiHsStateT)
%sizeof(SaHpiHsCauseOfStateChangeT)
%sizeof(SaHpiSeverityT)
%sizeof(SaHpiResourceEventTypeT)
%sizeof(SaHpiResourceEventT)
%sizeof(SaHpiDomainEventTypeT)
%sizeof(SaHpiDomainEventT)
%sizeof(SaHpiSensorOptionalDataT)
%sizeof(SaHpiSensorEventT)
%sizeof(SaHpiSensorEnableOptDataT)
%sizeof(SaHpiSensorEnableChangeEventT)
%sizeof(SaHpiHotSwapEventT)
%sizeof(SaHpiWatchdogEventT)
%sizeof(SaHpiSwEventTypeT)
%sizeof(SaHpiHpiSwEventT)
%sizeof(SaHpiOemEventT)
%sizeof(SaHpiUserEventT)
%sizeof(SaHpiDimiEventT)
%sizeof(SaHpiDimiUpdateEventT)
%sizeof(SaHpiFumiEventT)
%sizeof(SaHpiEventTypeT)
%sizeof(SaHpiEventUnionT)
%sizeof(SaHpiEventT)
%sizeof(SaHpiEvtQueueStatusT)
%sizeof(SaHpiAnnunciatorNumT)
%sizeof(SaHpiNameT)
%sizeof(SaHpiStatusCondTypeT)
%sizeof(SaHpiConditionT)
%sizeof(SaHpiAnnouncementT)
%sizeof(SaHpiAnnunciatorModeT)
%sizeof(SaHpiAnnunciatorTypeT)
%sizeof(SaHpiAnnunciatorRecT)
%sizeof(SaHpiRdrTypeT)
%sizeof(SaHpiRdrTypeUnionT)
%sizeof(SaHpiRdrT)
%sizeof(SaHpiParmActionT)
%sizeof(SaHpiResetActionT)
%sizeof(SaHpiPowerStateT)
%sizeof(SaHpiLoadNumberT)
%sizeof(SaHpiLoadIdT)
%sizeof(SaHpiResourceInfoT)
%sizeof(SaHpiCapabilitiesT)
%sizeof(SaHpiHsCapabilitiesT)
%sizeof(SaHpiRptEntryT)
%sizeof(SaHpiDomainCapabilitiesT)
%sizeof(SaHpiDomainInfoT)
%sizeof(SaHpiDrtEntryT)
%sizeof(SaHpiAlarmIdT)
%sizeof(SaHpiAlarmT)
%sizeof(SaHpiEventLogOverflowActionT)
%sizeof(SaHpiEventLogInfoT)
%sizeof(SaHpiEventLogCapabilitiesT)
%sizeof(SaHpiEventLogEntryIdT)
%sizeof(SaHpiEventLogEntryT)
%extend SaHpiRdrT {
	SaHpiRdrT(SaHpiEntryIdT RecordId = 0, SaHpiRdrTypeT RdrType = 0, SaHpiEntityPathT *Entity = NULL, SaHpiBoolT IsFru = 0, SaHpiRdrTypeUnionT *RdrTypeUnion = NULL, SaHpiTextBufferT *IdString = NULL) {
		SaHpiRdrT *o;
		o = (SaHpiRdrT *)malloc(sizeof(SaHpiRdrT));
		memset(o, 0, sizeof(SaHpiRdrT));
		o->RecordId = RecordId;
		o->RdrType = RdrType;
		if (Entity) o->Entity = *Entity;
		o->IsFru = IsFru;
		if (RdrTypeUnion) o->RdrTypeUnion = *RdrTypeUnion;
		if (IdString) o->IdString = *IdString;
		return o;
	}
};

%extend SaHpiResourceEventT {
	SaHpiResourceEventT(SaHpiResourceEventTypeT ResourceEventType = 0) {
		SaHpiResourceEventT *o;
		o = (SaHpiResourceEventT *)malloc(sizeof(SaHpiResourceEventT));
		memset(o, 0, sizeof(SaHpiResourceEventT));
		o->ResourceEventType = ResourceEventType;
		return o;
	}
};

%extend SaHpiEventLogInfoT {
	SaHpiEventLogInfoT(SaHpiUint32T Entries = 0, SaHpiUint32T Size = 0, SaHpiUint32T UserEventMaxSize = 0, SaHpiTimeT UpdateTimestamp = 0, SaHpiTimeT CurrentTime = 0, SaHpiBoolT Enabled = 0, SaHpiBoolT OverflowFlag = 0, SaHpiBoolT OverflowResetable = 0, SaHpiEventLogOverflowActionT OverflowAction = 0) {
		SaHpiEventLogInfoT *o;
		o = (SaHpiEventLogInfoT *)malloc(sizeof(SaHpiEventLogInfoT));
		memset(o, 0, sizeof(SaHpiEventLogInfoT));
		o->Entries = Entries;
		o->Size = Size;
		o->UserEventMaxSize = UserEventMaxSize;
		o->UpdateTimestamp = UpdateTimestamp;
		o->CurrentTime = CurrentTime;
		o->Enabled = Enabled;
		o->OverflowFlag = OverflowFlag;
		o->OverflowResetable = OverflowResetable;
		o->OverflowAction = OverflowAction;
		return o;
	}
};

%extend SaHpiCtrlRecDigitalT {
	SaHpiCtrlRecDigitalT(SaHpiCtrlStateDigitalT Default = 0) {
		SaHpiCtrlRecDigitalT *o;
		o = (SaHpiCtrlRecDigitalT *)malloc(sizeof(SaHpiCtrlRecDigitalT));
		memset(o, 0, sizeof(SaHpiCtrlRecDigitalT));
		o->Default = Default;
		return o;
	}
};

%extend SaHpiCtrlStateUnionT {
	SaHpiCtrlStateUnionT(SaHpiCtrlStateDigitalT Digital = 0, SaHpiCtrlStateDiscreteT Discrete = 0, SaHpiCtrlStateAnalogT Analog = 0, SaHpiCtrlStateStreamT *Stream = NULL, SaHpiCtrlStateTextT *Text = NULL, SaHpiCtrlStateOemT *Oem = NULL) {
		SaHpiCtrlStateUnionT *o;
		o = (SaHpiCtrlStateUnionT *)malloc(sizeof(SaHpiCtrlStateUnionT));
		memset(o, 0, sizeof(SaHpiCtrlStateUnionT));
		o->Digital = Digital;
		o->Discrete = Discrete;
		o->Analog = Analog;
		if (Stream) o->Stream = *Stream;
		if (Text) o->Text = *Text;
		if (Oem) o->Oem = *Oem;
		return o;
	}
};

%extend SaHpiWatchdogEventT {
	SaHpiWatchdogEventT(SaHpiWatchdogNumT WatchdogNum = 0, SaHpiWatchdogActionEventT WatchdogAction = 0, SaHpiWatchdogPretimerInterruptT WatchdogPreTimerAction = 0, SaHpiWatchdogTimerUseT WatchdogUse = 0) {
		SaHpiWatchdogEventT *o;
		o = (SaHpiWatchdogEventT *)malloc(sizeof(SaHpiWatchdogEventT));
		memset(o, 0, sizeof(SaHpiWatchdogEventT));
		o->WatchdogNum = WatchdogNum;
		o->WatchdogAction = WatchdogAction;
		o->WatchdogPreTimerAction = WatchdogPreTimerAction;
		o->WatchdogUse = WatchdogUse;
		return o;
	}
};

%extend SaHpiDimiTestT {
	SaHpiDimiTestT(SaHpiTextBufferT *TestName = NULL, SaHpiDimiTestServiceImpactT ServiceImpact = 0, SaHpiBoolT NeedServiceOS = 0, SaHpiTextBufferT *ServiceOS = NULL, SaHpiTimeT ExpectedRunDuration = 0, SaHpiDimiTestCapabilityT TestCapabilities = 0) {
		SaHpiDimiTestT *o;
		o = (SaHpiDimiTestT *)malloc(sizeof(SaHpiDimiTestT));
		memset(o, 0, sizeof(SaHpiDimiTestT));
		if (TestName) o->TestName = *TestName;
		o->ServiceImpact = ServiceImpact;
		o->NeedServiceOS = NeedServiceOS;
		if (ServiceOS) o->ServiceOS = *ServiceOS;
		o->ExpectedRunDuration = ExpectedRunDuration;
		o->TestCapabilities = TestCapabilities;
		return o;
	}
};

%extend SaHpiIdrFieldT {
	SaHpiIdrFieldT(SaHpiEntryIdT AreaId = 0, SaHpiEntryIdT FieldId = 0, SaHpiIdrFieldTypeT Type = 0, SaHpiBoolT ReadOnly = 0, SaHpiTextBufferT *Field = NULL) {
		SaHpiIdrFieldT *o;
		o = (SaHpiIdrFieldT *)malloc(sizeof(SaHpiIdrFieldT));
		memset(o, 0, sizeof(SaHpiIdrFieldT));
		o->AreaId = AreaId;
		o->FieldId = FieldId;
		o->Type = Type;
		o->ReadOnly = ReadOnly;
		if (Field) o->Field = *Field;
		return o;
	}
};

%extend SaHpiFumiEventT {
	SaHpiFumiEventT(SaHpiFumiNumT FumiNum = 0, SaHpiUint8T BankNum = 0, SaHpiFumiUpgradeStatusT UpgradeStatus = 0) {
		SaHpiFumiEventT *o;
		o = (SaHpiFumiEventT *)malloc(sizeof(SaHpiFumiEventT));
		memset(o, 0, sizeof(SaHpiFumiEventT));
		o->FumiNum = FumiNum;
		o->BankNum = BankNum;
		o->UpgradeStatus = UpgradeStatus;
		return o;
	}
};

%extend SaHpiEventUnionT {
	SaHpiEventUnionT(SaHpiResourceEventT *ResourceEvent = NULL, SaHpiDomainEventT *DomainEvent = NULL, SaHpiSensorEventT *SensorEvent = NULL, SaHpiSensorEnableChangeEventT *SensorEnableChangeEvent = NULL, SaHpiHotSwapEventT *HotSwapEvent = NULL, SaHpiWatchdogEventT *WatchdogEvent = NULL, SaHpiHpiSwEventT *HpiSwEvent = NULL, SaHpiOemEventT *OemEvent = NULL, SaHpiUserEventT *UserEvent = NULL, SaHpiDimiEventT *DimiEvent = NULL, SaHpiDimiUpdateEventT *DimiUpdateEvent = NULL, SaHpiFumiEventT *FumiEvent = NULL) {
		SaHpiEventUnionT *o;
		o = (SaHpiEventUnionT *)malloc(sizeof(SaHpiEventUnionT));
		memset(o, 0, sizeof(SaHpiEventUnionT));
		if (ResourceEvent) o->ResourceEvent = *ResourceEvent;
		if (DomainEvent) o->DomainEvent = *DomainEvent;
		if (SensorEvent) o->SensorEvent = *SensorEvent;
		if (SensorEnableChangeEvent) o->SensorEnableChangeEvent = *SensorEnableChangeEvent;
		if (HotSwapEvent) o->HotSwapEvent = *HotSwapEvent;
		if (WatchdogEvent) o->WatchdogEvent = *WatchdogEvent;
		if (HpiSwEvent) o->HpiSwEvent = *HpiSwEvent;
		if (OemEvent) o->OemEvent = *OemEvent;
		if (UserEvent) o->UserEvent = *UserEvent;
		if (DimiEvent) o->DimiEvent = *DimiEvent;
		if (DimiUpdateEvent) o->DimiUpdateEvent = *DimiUpdateEvent;
		if (FumiEvent) o->FumiEvent = *FumiEvent;
		return o;
	}
};

%extend SaHpiNameT {
	SaHpiNameT(SaHpiUint16T Length = 0, SaHpiUint8T Value[SA_HPI_MAX_NAME_LENGTH] = NULL) {
		SaHpiNameT *o;
		o = (SaHpiNameT *)malloc(sizeof(SaHpiNameT));
		memset(o, 0, sizeof(SaHpiNameT));
		o->Length = Length;
		if (Value) memcpy(o->Value, Value, sizeof(SaHpiUint8T)*SA_HPI_MAX_NAME_LENGTH);
		return o;
	}
};

%extend SaHpiCtrlStateTextT {
	SaHpiCtrlStateTextT(SaHpiTxtLineNumT Line = 0, SaHpiTextBufferT *Text = NULL) {
		SaHpiCtrlStateTextT *o;
		o = (SaHpiCtrlStateTextT *)malloc(sizeof(SaHpiCtrlStateTextT));
		memset(o, 0, sizeof(SaHpiCtrlStateTextT));
		o->Line = Line;
		if (Text) o->Text = *Text;
		return o;
	}
};

%extend SaHpiFumiBankInfoT {
	SaHpiFumiBankInfoT(SaHpiUint8T BankId = 0, SaHpiUint32T BankSize = 0, SaHpiUint32T Position = 0, SaHpiFumiBankStateT BankState = 0, SaHpiTextBufferT *Identifier = NULL, SaHpiTextBufferT *Description = NULL, SaHpiTextBufferT *DateTime = NULL, SaHpiUint32T MajorVersion = 0, SaHpiUint32T MinorVersion = 0, SaHpiUint32T AuxVersion = 0) {
		SaHpiFumiBankInfoT *o;
		o = (SaHpiFumiBankInfoT *)malloc(sizeof(SaHpiFumiBankInfoT));
		memset(o, 0, sizeof(SaHpiFumiBankInfoT));
		o->BankId = BankId;
		o->BankSize = BankSize;
		o->Position = Position;
		o->BankState = BankState;
		if (Identifier) o->Identifier = *Identifier;
		if (Description) o->Description = *Description;
		if (DateTime) o->DateTime = *DateTime;
		o->MajorVersion = MajorVersion;
		o->MinorVersion = MinorVersion;
		o->AuxVersion = AuxVersion;
		return o;
	}
};

%extend SaHpiTextBufferT {
	SaHpiTextBufferT(SaHpiTextTypeT DataType = 0, SaHpiLanguageT Language = 0, SaHpiUint8T DataLength = 0, SaHpiUint8T Data[SAHPI_MAX_TEXT_BUFFER_LENGTH] = NULL) {
		SaHpiTextBufferT *o;
		o = (SaHpiTextBufferT *)malloc(sizeof(SaHpiTextBufferT));
		memset(o, 0, sizeof(SaHpiTextBufferT));
		o->DataType = DataType;
		o->Language = Language;
		o->DataLength = DataLength;
		if (Data) memcpy(o->Data, Data, sizeof(SaHpiUint8T)*SAHPI_MAX_TEXT_BUFFER_LENGTH);
		return o;
	}
};

%extend SaHpiCtrlRecStreamT {
	SaHpiCtrlRecStreamT(SaHpiCtrlStateStreamT *Default = NULL) {
		SaHpiCtrlRecStreamT *o;
		o = (SaHpiCtrlRecStreamT *)malloc(sizeof(SaHpiCtrlRecStreamT));
		memset(o, 0, sizeof(SaHpiCtrlRecStreamT));
		if (Default) o->Default = *Default;
		return o;
	}
};

%extend SaHpiCtrlStateT {
	SaHpiCtrlStateT(SaHpiCtrlTypeT Type = 0, SaHpiCtrlStateUnionT *StateUnion = NULL) {
		SaHpiCtrlStateT *o;
		o = (SaHpiCtrlStateT *)malloc(sizeof(SaHpiCtrlStateT));
		memset(o, 0, sizeof(SaHpiCtrlStateT));
		o->Type = Type;
		if (StateUnion) o->StateUnion = *StateUnion;
		return o;
	}
};

%extend SaHpiAnnouncementT {
	SaHpiAnnouncementT(SaHpiEntryIdT EntryId = 0, SaHpiTimeT Timestamp = 0, SaHpiBoolT AddedByUser = 0, SaHpiSeverityT Severity = 0, SaHpiBoolT Acknowledged = 0, SaHpiConditionT *StatusCond = NULL) {
		SaHpiAnnouncementT *o;
		o = (SaHpiAnnouncementT *)malloc(sizeof(SaHpiAnnouncementT));
		memset(o, 0, sizeof(SaHpiAnnouncementT));
		o->EntryId = EntryId;
		o->Timestamp = Timestamp;
		o->AddedByUser = AddedByUser;
		o->Severity = Severity;
		o->Acknowledged = Acknowledged;
		if (StatusCond) o->StatusCond = *StatusCond;
		return o;
	}
};

%extend SaHpiCtrlRecDiscreteT {
	SaHpiCtrlRecDiscreteT(SaHpiCtrlStateDiscreteT Default = 0) {
		SaHpiCtrlRecDiscreteT *o;
		o = (SaHpiCtrlRecDiscreteT *)malloc(sizeof(SaHpiCtrlRecDiscreteT));
		memset(o, 0, sizeof(SaHpiCtrlRecDiscreteT));
		o->Default = Default;
		return o;
	}
};

%extend SaHpiDimiRecT {
	SaHpiDimiRecT(SaHpiDimiNumT DimiNum = 0, SaHpiUint32T Oem = 0) {
		SaHpiDimiRecT *o;
		o = (SaHpiDimiRecT *)malloc(sizeof(SaHpiDimiRecT));
		memset(o, 0, sizeof(SaHpiDimiRecT));
		o->DimiNum = DimiNum;
		o->Oem = Oem;
		return o;
	}
};

%extend SaHpiDimiTestParamsDefinitionT {
	SaHpiDimiTestParamsDefinitionT(SaHpiUint8T ParamName[SAHPI_DIMITEST_PARAM_NAME_LEN] = NULL, SaHpiTextBufferT *ParamInfo = NULL, SaHpiDimiTestParamTypeT ParamType = 0, SaHpiDimiTestParameterValueUnionT *MinValue = NULL, SaHpiDimiTestParameterValueUnionT *MaxValue = NULL, SaHpiDimiTestParamValueT *DefaultParam = NULL) {
		SaHpiDimiTestParamsDefinitionT *o;
		o = (SaHpiDimiTestParamsDefinitionT *)malloc(sizeof(SaHpiDimiTestParamsDefinitionT));
		memset(o, 0, sizeof(SaHpiDimiTestParamsDefinitionT));
		if (ParamName) memcpy(o->ParamName, ParamName, sizeof(SaHpiUint8T)*SAHPI_DIMITEST_PARAM_NAME_LEN);
		if (ParamInfo) o->ParamInfo = *ParamInfo;
		o->ParamType = ParamType;
		if (MinValue) o->MinValue = *MinValue;
		if (MaxValue) o->MaxValue = *MaxValue;
		if (DefaultParam) o->DefaultParam = *DefaultParam;
		return o;
	}
};

%extend SaHpiSensorThresholdsT {
	SaHpiSensorThresholdsT(SaHpiSensorReadingT *LowCritical = NULL, SaHpiSensorReadingT *LowMajor = NULL, SaHpiSensorReadingT *LowMinor = NULL, SaHpiSensorReadingT *UpCritical = NULL, SaHpiSensorReadingT *UpMajor = NULL, SaHpiSensorReadingT *UpMinor = NULL, SaHpiSensorReadingT *PosThdHysteresis = NULL, SaHpiSensorReadingT *NegThdHysteresis = NULL) {
		SaHpiSensorThresholdsT *o;
		o = (SaHpiSensorThresholdsT *)malloc(sizeof(SaHpiSensorThresholdsT));
		memset(o, 0, sizeof(SaHpiSensorThresholdsT));
		if (LowCritical) o->LowCritical = *LowCritical;
		if (LowMajor) o->LowMajor = *LowMajor;
		if (LowMinor) o->LowMinor = *LowMinor;
		if (UpCritical) o->UpCritical = *UpCritical;
		if (UpMajor) o->UpMajor = *UpMajor;
		if (UpMinor) o->UpMinor = *UpMinor;
		if (PosThdHysteresis) o->PosThdHysteresis = *PosThdHysteresis;
		if (NegThdHysteresis) o->NegThdHysteresis = *NegThdHysteresis;
		return o;
	}
};

%extend SaHpiRptEntryT {
	SaHpiRptEntryT(SaHpiEntryIdT EntryId = 0, SaHpiResourceIdT ResourceId = 0, SaHpiResourceInfoT *ResourceInfo = NULL, SaHpiEntityPathT *ResourceEntity = NULL, SaHpiCapabilitiesT ResourceCapabilities = 0, SaHpiHsCapabilitiesT HotSwapCapabilities = 0, SaHpiSeverityT ResourceSeverity = 0, SaHpiBoolT ResourceFailed = 0, SaHpiTextBufferT *ResourceTag = NULL) {
		SaHpiRptEntryT *o;
		o = (SaHpiRptEntryT *)malloc(sizeof(SaHpiRptEntryT));
		memset(o, 0, sizeof(SaHpiRptEntryT));
		o->EntryId = EntryId;
		o->ResourceId = ResourceId;
		if (ResourceInfo) o->ResourceInfo = *ResourceInfo;
		if (ResourceEntity) o->ResourceEntity = *ResourceEntity;
		o->ResourceCapabilities = ResourceCapabilities;
		o->HotSwapCapabilities = HotSwapCapabilities;
		o->ResourceSeverity = ResourceSeverity;
		o->ResourceFailed = ResourceFailed;
		if (ResourceTag) o->ResourceTag = *ResourceTag;
		return o;
	}
};

%extend SaHpiDimiTestParameterValueUnionT {
	SaHpiDimiTestParameterValueUnionT(SaHpiInt32T IntValue = 0, SaHpiFloat64T FloatValue = 0) {
		SaHpiDimiTestParameterValueUnionT *o;
		o = (SaHpiDimiTestParameterValueUnionT *)malloc(sizeof(SaHpiDimiTestParameterValueUnionT));
		memset(o, 0, sizeof(SaHpiDimiTestParameterValueUnionT));
		o->IntValue = IntValue;
		o->FloatValue = FloatValue;
		return o;
	}
};

%extend SaHpiDimiTestResultsT {
	SaHpiDimiTestResultsT(SaHpiTimeT ResultTimeStamp = 0, SaHpiTimeoutT RunDuration = 0, SaHpiDimiTestRunStatusT LastRunStatus = 0, SaHpiDimiTestErrCodeT TestErrorCode = 0, SaHpiTextBufferT *TestResultString = NULL, SaHpiBoolT TestResultStringIsURI = 0) {
		SaHpiDimiTestResultsT *o;
		o = (SaHpiDimiTestResultsT *)malloc(sizeof(SaHpiDimiTestResultsT));
		memset(o, 0, sizeof(SaHpiDimiTestResultsT));
		o->ResultTimeStamp = ResultTimeStamp;
		o->RunDuration = RunDuration;
		o->LastRunStatus = LastRunStatus;
		o->TestErrorCode = TestErrorCode;
		if (TestResultString) o->TestResultString = *TestResultString;
		o->TestResultStringIsURI = TestResultStringIsURI;
		return o;
	}
};

%extend SaHpiSensorThdDefnT {
	SaHpiSensorThdDefnT(SaHpiBoolT IsAccessible = 0, SaHpiSensorThdMaskT ReadThold = 0, SaHpiSensorThdMaskT WriteThold = 0, SaHpiBoolT Nonlinear = 0) {
		SaHpiSensorThdDefnT *o;
		o = (SaHpiSensorThdDefnT *)malloc(sizeof(SaHpiSensorThdDefnT));
		memset(o, 0, sizeof(SaHpiSensorThdDefnT));
		o->IsAccessible = IsAccessible;
		o->ReadThold = ReadThold;
		o->WriteThold = WriteThold;
		o->Nonlinear = Nonlinear;
		return o;
	}
};

%extend SaHpiIdrInfoT {
	SaHpiIdrInfoT(SaHpiIdrIdT IdrId = 0, SaHpiUint32T UpdateCount = 0, SaHpiBoolT ReadOnly = 0, SaHpiUint32T NumAreas = 0) {
		SaHpiIdrInfoT *o;
		o = (SaHpiIdrInfoT *)malloc(sizeof(SaHpiIdrInfoT));
		memset(o, 0, sizeof(SaHpiIdrInfoT));
		o->IdrId = IdrId;
		o->UpdateCount = UpdateCount;
		o->ReadOnly = ReadOnly;
		o->NumAreas = NumAreas;
		return o;
	}
};

%extend SaHpiSensorEventT {
	SaHpiSensorEventT(SaHpiSensorNumT SensorNum = 0, SaHpiSensorTypeT SensorType = 0, SaHpiEventCategoryT EventCategory = 0, SaHpiBoolT Assertion = 0, SaHpiEventStateT EventState = 0, SaHpiSensorOptionalDataT OptionalDataPresent = 0, SaHpiSensorReadingT *TriggerReading = NULL, SaHpiSensorReadingT *TriggerThreshold = NULL, SaHpiEventStateT PreviousState = 0, SaHpiEventStateT CurrentState = 0, SaHpiUint32T Oem = 0, SaHpiUint32T SensorSpecific = 0) {
		SaHpiSensorEventT *o;
		o = (SaHpiSensorEventT *)malloc(sizeof(SaHpiSensorEventT));
		memset(o, 0, sizeof(SaHpiSensorEventT));
		o->SensorNum = SensorNum;
		o->SensorType = SensorType;
		o->EventCategory = EventCategory;
		o->Assertion = Assertion;
		o->EventState = EventState;
		o->OptionalDataPresent = OptionalDataPresent;
		if (TriggerReading) o->TriggerReading = *TriggerReading;
		if (TriggerThreshold) o->TriggerThreshold = *TriggerThreshold;
		o->PreviousState = PreviousState;
		o->CurrentState = CurrentState;
		o->Oem = Oem;
		o->SensorSpecific = SensorSpecific;
		return o;
	}
};

%extend SaHpiAlarmT {
	SaHpiAlarmT(SaHpiAlarmIdT AlarmId = 0, SaHpiTimeT Timestamp = 0, SaHpiSeverityT Severity = 0, SaHpiBoolT Acknowledged = 0, SaHpiConditionT *AlarmCond = NULL) {
		SaHpiAlarmT *o;
		o = (SaHpiAlarmT *)malloc(sizeof(SaHpiAlarmT));
		memset(o, 0, sizeof(SaHpiAlarmT));
		o->AlarmId = AlarmId;
		o->Timestamp = Timestamp;
		o->Severity = Severity;
		o->Acknowledged = Acknowledged;
		if (AlarmCond) o->AlarmCond = *AlarmCond;
		return o;
	}
};

%extend SaHpiCtrlRecUnionT {
	SaHpiCtrlRecUnionT(SaHpiCtrlRecDigitalT *Digital = NULL, SaHpiCtrlRecDiscreteT *Discrete = NULL, SaHpiCtrlRecAnalogT *Analog = NULL, SaHpiCtrlRecStreamT *Stream = NULL, SaHpiCtrlRecTextT *Text = NULL, SaHpiCtrlRecOemT *Oem = NULL) {
		SaHpiCtrlRecUnionT *o;
		o = (SaHpiCtrlRecUnionT *)malloc(sizeof(SaHpiCtrlRecUnionT));
		memset(o, 0, sizeof(SaHpiCtrlRecUnionT));
		if (Digital) o->Digital = *Digital;
		if (Discrete) o->Discrete = *Discrete;
		if (Analog) o->Analog = *Analog;
		if (Stream) o->Stream = *Stream;
		if (Text) o->Text = *Text;
		if (Oem) o->Oem = *Oem;
		return o;
	}
};

%extend SaHpiCtrlStateStreamT {
	SaHpiCtrlStateStreamT(SaHpiBoolT Repeat = 0, SaHpiUint32T StreamLength = 0, SaHpiUint8T Stream[SAHPI_CTRL_MAX_STREAM_LENGTH] = NULL) {
		SaHpiCtrlStateStreamT *o;
		o = (SaHpiCtrlStateStreamT *)malloc(sizeof(SaHpiCtrlStateStreamT));
		memset(o, 0, sizeof(SaHpiCtrlStateStreamT));
		o->Repeat = Repeat;
		o->StreamLength = StreamLength;
		if (Stream) memcpy(o->Stream, Stream, sizeof(SaHpiUint8T)*SAHPI_CTRL_MAX_STREAM_LENGTH);
		return o;
	}
};

%extend SaHpiInventoryRecT {
	SaHpiInventoryRecT(SaHpiIdrIdT IdrId = 0, SaHpiBoolT Persistent = 0, SaHpiUint32T Oem = 0) {
		SaHpiInventoryRecT *o;
		o = (SaHpiInventoryRecT *)malloc(sizeof(SaHpiInventoryRecT));
		memset(o, 0, sizeof(SaHpiInventoryRecT));
		o->IdrId = IdrId;
		o->Persistent = Persistent;
		o->Oem = Oem;
		return o;
	}
};

%extend SaHpiDimiTestParamValueT {
	SaHpiDimiTestParamValueT(SaHpiInt32T paramint = 0, SaHpiBoolT parambool = 0, SaHpiFloat64T paramfloat = 0, SaHpiTextBufferT *paramtext = NULL) {
		SaHpiDimiTestParamValueT *o;
		o = (SaHpiDimiTestParamValueT *)malloc(sizeof(SaHpiDimiTestParamValueT));
		memset(o, 0, sizeof(SaHpiDimiTestParamValueT));
		o->paramint = paramint;
		o->parambool = parambool;
		o->paramfloat = paramfloat;
		if (paramtext) o->paramtext = *paramtext;
		return o;
	}
};

%extend SaHpiDimiEventT {
	SaHpiDimiEventT(SaHpiDimiNumT DimiNum = 0, SaHpiDimiTestNumT TestNum = 0, SaHpiDimiTestRunStatusT DimiTestRunStatus = 0, SaHpiDimiTestPercentCompletedT DimiTestPercentCompleted = 0) {
		SaHpiDimiEventT *o;
		o = (SaHpiDimiEventT *)malloc(sizeof(SaHpiDimiEventT));
		memset(o, 0, sizeof(SaHpiDimiEventT));
		o->DimiNum = DimiNum;
		o->TestNum = TestNum;
		o->DimiTestRunStatus = DimiTestRunStatus;
		o->DimiTestPercentCompleted = DimiTestPercentCompleted;
		return o;
	}
};

%extend SaHpiWatchdogRecT {
	SaHpiWatchdogRecT(SaHpiWatchdogNumT WatchdogNum = 0, SaHpiUint32T Oem = 0) {
		SaHpiWatchdogRecT *o;
		o = (SaHpiWatchdogRecT *)malloc(sizeof(SaHpiWatchdogRecT));
		memset(o, 0, sizeof(SaHpiWatchdogRecT));
		o->WatchdogNum = WatchdogNum;
		o->Oem = Oem;
		return o;
	}
};

%extend SaHpiDimiInfoT {
	SaHpiDimiInfoT(SaHpiDimiTotalTestsT NumberOfTests = 0, SaHpiUint32T TestNumUpdateCounter = 0) {
		SaHpiDimiInfoT *o;
		o = (SaHpiDimiInfoT *)malloc(sizeof(SaHpiDimiInfoT));
		memset(o, 0, sizeof(SaHpiDimiInfoT));
		o->NumberOfTests = NumberOfTests;
		o->TestNumUpdateCounter = TestNumUpdateCounter;
		return o;
	}
};

%extend SaHpiSensorRangeT {
	SaHpiSensorRangeT(SaHpiSensorRangeFlagsT Flags = 0, SaHpiSensorReadingT *Max = NULL, SaHpiSensorReadingT *Min = NULL, SaHpiSensorReadingT *Nominal = NULL, SaHpiSensorReadingT *NormalMax = NULL, SaHpiSensorReadingT *NormalMin = NULL) {
		SaHpiSensorRangeT *o;
		o = (SaHpiSensorRangeT *)malloc(sizeof(SaHpiSensorRangeT));
		memset(o, 0, sizeof(SaHpiSensorRangeT));
		o->Flags = Flags;
		if (Max) o->Max = *Max;
		if (Min) o->Min = *Min;
		if (Nominal) o->Nominal = *Nominal;
		if (NormalMax) o->NormalMax = *NormalMax;
		if (NormalMin) o->NormalMin = *NormalMin;
		return o;
	}
};

%extend SaHpiIdrAreaHeaderT {
	SaHpiIdrAreaHeaderT(SaHpiEntryIdT AreaId = 0, SaHpiIdrAreaTypeT Type = 0, SaHpiBoolT ReadOnly = 0, SaHpiUint32T NumFields = 0) {
		SaHpiIdrAreaHeaderT *o;
		o = (SaHpiIdrAreaHeaderT *)malloc(sizeof(SaHpiIdrAreaHeaderT));
		memset(o, 0, sizeof(SaHpiIdrAreaHeaderT));
		o->AreaId = AreaId;
		o->Type = Type;
		o->ReadOnly = ReadOnly;
		o->NumFields = NumFields;
		return o;
	}
};

%extend SaHpiCtrlRecTextT {
	SaHpiCtrlRecTextT(SaHpiUint8T MaxChars = 0, SaHpiUint8T MaxLines = 0, SaHpiLanguageT Language = 0, SaHpiTextTypeT DataType = 0, SaHpiCtrlStateTextT *Default = NULL) {
		SaHpiCtrlRecTextT *o;
		o = (SaHpiCtrlRecTextT *)malloc(sizeof(SaHpiCtrlRecTextT));
		memset(o, 0, sizeof(SaHpiCtrlRecTextT));
		o->MaxChars = MaxChars;
		o->MaxLines = MaxLines;
		o->Language = Language;
		o->DataType = DataType;
		if (Default) o->Default = *Default;
		return o;
	}
};

%extend SaHpiFumiRecT {
	SaHpiFumiRecT(SaHpiFumiNumT Num = 0, SaHpiFumiProtocolT AccessProt = 0, SaHpiFumiCapabilityT Capability = 0, SaHpiUint8T NumBanks = 0, SaHpiUint32T Oem = 0) {
		SaHpiFumiRecT *o;
		o = (SaHpiFumiRecT *)malloc(sizeof(SaHpiFumiRecT));
		memset(o, 0, sizeof(SaHpiFumiRecT));
		o->Num = Num;
		o->AccessProt = AccessProt;
		o->Capability = Capability;
		o->NumBanks = NumBanks;
		o->Oem = Oem;
		return o;
	}
};

%extend SaHpiCtrlStateOemT {
	SaHpiCtrlStateOemT(SaHpiManufacturerIdT MId = 0, SaHpiUint8T BodyLength = 0, SaHpiUint8T Body[SAHPI_CTRL_MAX_OEM_BODY_LENGTH] = NULL) {
		SaHpiCtrlStateOemT *o;
		o = (SaHpiCtrlStateOemT *)malloc(sizeof(SaHpiCtrlStateOemT));
		memset(o, 0, sizeof(SaHpiCtrlStateOemT));
		o->MId = MId;
		o->BodyLength = BodyLength;
		if (Body) memcpy(o->Body, Body, sizeof(SaHpiUint8T)*SAHPI_CTRL_MAX_OEM_BODY_LENGTH);
		return o;
	}
};

%extend SaHpiCtrlDefaultModeT {
	SaHpiCtrlDefaultModeT(SaHpiCtrlModeT Mode = 0, SaHpiBoolT ReadOnly = 0) {
		SaHpiCtrlDefaultModeT *o;
		o = (SaHpiCtrlDefaultModeT *)malloc(sizeof(SaHpiCtrlDefaultModeT));
		memset(o, 0, sizeof(SaHpiCtrlDefaultModeT));
		o->Mode = Mode;
		o->ReadOnly = ReadOnly;
		return o;
	}
};

%extend SaHpiWatchdogT {
	SaHpiWatchdogT(SaHpiBoolT Log = 0, SaHpiBoolT Running = 0, SaHpiWatchdogTimerUseT TimerUse = 0, SaHpiWatchdogActionT TimerAction = 0, SaHpiWatchdogPretimerInterruptT PretimerInterrupt = 0, SaHpiUint32T PreTimeoutInterval = 0, SaHpiWatchdogExpFlagsT TimerUseExpFlags = 0, SaHpiUint32T InitialCount = 0, SaHpiUint32T PresentCount = 0) {
		SaHpiWatchdogT *o;
		o = (SaHpiWatchdogT *)malloc(sizeof(SaHpiWatchdogT));
		memset(o, 0, sizeof(SaHpiWatchdogT));
		o->Log = Log;
		o->Running = Running;
		o->TimerUse = TimerUse;
		o->TimerAction = TimerAction;
		o->PretimerInterrupt = PretimerInterrupt;
		o->PreTimeoutInterval = PreTimeoutInterval;
		o->TimerUseExpFlags = TimerUseExpFlags;
		o->InitialCount = InitialCount;
		o->PresentCount = PresentCount;
		return o;
	}
};

%extend SaHpiOemEventT {
	SaHpiOemEventT(SaHpiManufacturerIdT MId = 0, SaHpiTextBufferT *OemEventData = NULL) {
		SaHpiOemEventT *o;
		o = (SaHpiOemEventT *)malloc(sizeof(SaHpiOemEventT));
		memset(o, 0, sizeof(SaHpiOemEventT));
		o->MId = MId;
		if (OemEventData) o->OemEventData = *OemEventData;
		return o;
	}
};

%extend SaHpiDimiTestAffectedEntityT {
	SaHpiDimiTestAffectedEntityT(SaHpiEntityPathT *EntityImpacted = NULL, SaHpiDimiTestServiceImpactT ServiceImpact = 0) {
		SaHpiDimiTestAffectedEntityT *o;
		o = (SaHpiDimiTestAffectedEntityT *)malloc(sizeof(SaHpiDimiTestAffectedEntityT));
		memset(o, 0, sizeof(SaHpiDimiTestAffectedEntityT));
		if (EntityImpacted) o->EntityImpacted = *EntityImpacted;
		o->ServiceImpact = ServiceImpact;
		return o;
	}
};

%extend SaHpiDimiTestVariableParamsT {
	SaHpiDimiTestVariableParamsT(SaHpiUint8T ParamName[SAHPI_DIMITEST_PARAM_NAME_LEN] = NULL, SaHpiDimiTestParamTypeT ParamType = 0, SaHpiDimiTestParamValueT *Value = NULL) {
		SaHpiDimiTestVariableParamsT *o;
		o = (SaHpiDimiTestVariableParamsT *)malloc(sizeof(SaHpiDimiTestVariableParamsT));
		memset(o, 0, sizeof(SaHpiDimiTestVariableParamsT));
		if (ParamName) memcpy(o->ParamName, ParamName, sizeof(SaHpiUint8T)*SAHPI_DIMITEST_PARAM_NAME_LEN);
		o->ParamType = ParamType;
		if (Value) o->Value = *Value;
		return o;
	}
};

%extend SaHpiLoadIdT {
	SaHpiLoadIdT(SaHpiLoadNumberT LoadNumber = 0, SaHpiTextBufferT *LoadName = NULL) {
		SaHpiLoadIdT *o;
		o = (SaHpiLoadIdT *)malloc(sizeof(SaHpiLoadIdT));
		memset(o, 0, sizeof(SaHpiLoadIdT));
		o->LoadNumber = LoadNumber;
		if (LoadName) o->LoadName = *LoadName;
		return o;
	}
};

%extend SaHpiEventLogEntryT {
	SaHpiEventLogEntryT(SaHpiEventLogEntryIdT EntryId = 0, SaHpiTimeT Timestamp = 0, SaHpiEventT *Event = NULL) {
		SaHpiEventLogEntryT *o;
		o = (SaHpiEventLogEntryT *)malloc(sizeof(SaHpiEventLogEntryT));
		memset(o, 0, sizeof(SaHpiEventLogEntryT));
		o->EntryId = EntryId;
		o->Timestamp = Timestamp;
		if (Event) o->Event = *Event;
		return o;
	}
};

%extend SaHpiAnnunciatorRecT {
	SaHpiAnnunciatorRecT(SaHpiAnnunciatorNumT AnnunciatorNum = 0, SaHpiAnnunciatorTypeT AnnunciatorType = 0, SaHpiBoolT ModeReadOnly = 0, SaHpiUint32T MaxConditions = 0, SaHpiUint32T Oem = 0) {
		SaHpiAnnunciatorRecT *o;
		o = (SaHpiAnnunciatorRecT *)malloc(sizeof(SaHpiAnnunciatorRecT));
		memset(o, 0, sizeof(SaHpiAnnunciatorRecT));
		o->AnnunciatorNum = AnnunciatorNum;
		o->AnnunciatorType = AnnunciatorType;
		o->ModeReadOnly = ModeReadOnly;
		o->MaxConditions = MaxConditions;
		o->Oem = Oem;
		return o;
	}
};

%extend SaHpiHotSwapEventT {
	SaHpiHotSwapEventT(SaHpiHsStateT HotSwapState = 0, SaHpiHsStateT PreviousHotSwapState = 0, SaHpiHsCauseOfStateChangeT CauseOfStateChange = 0) {
		SaHpiHotSwapEventT *o;
		o = (SaHpiHotSwapEventT *)malloc(sizeof(SaHpiHotSwapEventT));
		memset(o, 0, sizeof(SaHpiHotSwapEventT));
		o->HotSwapState = HotSwapState;
		o->PreviousHotSwapState = PreviousHotSwapState;
		o->CauseOfStateChange = CauseOfStateChange;
		return o;
	}
};

%extend SaHpiUserEventT {
	SaHpiUserEventT(SaHpiTextBufferT *UserEventData = NULL) {
		SaHpiUserEventT *o;
		o = (SaHpiUserEventT *)malloc(sizeof(SaHpiUserEventT));
		memset(o, 0, sizeof(SaHpiUserEventT));
		if (UserEventData) o->UserEventData = *UserEventData;
		return o;
	}
};

%extend SaHpiFumiSourceInfoT {
	SaHpiFumiSourceInfoT(SaHpiTextBufferT *SourceUri = NULL, SaHpiFumiSourceStatusT SourceStatus = 0, SaHpiTextBufferT *Identifier = NULL, SaHpiTextBufferT *Description = NULL, SaHpiTextBufferT *DateTime = NULL, SaHpiUint32T MajorVersion = 0, SaHpiUint32T MinorVersion = 0, SaHpiUint32T AuxVersion = 0) {
		SaHpiFumiSourceInfoT *o;
		o = (SaHpiFumiSourceInfoT *)malloc(sizeof(SaHpiFumiSourceInfoT));
		memset(o, 0, sizeof(SaHpiFumiSourceInfoT));
		if (SourceUri) o->SourceUri = *SourceUri;
		o->SourceStatus = SourceStatus;
		if (Identifier) o->Identifier = *Identifier;
		if (Description) o->Description = *Description;
		if (DateTime) o->DateTime = *DateTime;
		o->MajorVersion = MajorVersion;
		o->MinorVersion = MinorVersion;
		o->AuxVersion = AuxVersion;
		return o;
	}
};

%extend SaHpiCtrlRecOemT {
	SaHpiCtrlRecOemT(SaHpiManufacturerIdT MId = 0, SaHpiUint8T ConfigData[SAHPI_CTRL_OEM_CONFIG_LENGTH] = NULL, SaHpiCtrlStateOemT *Default = NULL) {
		SaHpiCtrlRecOemT *o;
		o = (SaHpiCtrlRecOemT *)malloc(sizeof(SaHpiCtrlRecOemT));
		memset(o, 0, sizeof(SaHpiCtrlRecOemT));
		o->MId = MId;
		if (ConfigData) memcpy(o->ConfigData, ConfigData, sizeof(SaHpiUint8T)*SAHPI_CTRL_OEM_CONFIG_LENGTH);
		if (Default) o->Default = *Default;
		return o;
	}
};

%extend SaHpiHpiSwEventT {
	SaHpiHpiSwEventT(SaHpiManufacturerIdT MId = 0, SaHpiSwEventTypeT Type = 0, SaHpiTextBufferT *EventData = NULL) {
		SaHpiHpiSwEventT *o;
		o = (SaHpiHpiSwEventT *)malloc(sizeof(SaHpiHpiSwEventT));
		memset(o, 0, sizeof(SaHpiHpiSwEventT));
		o->MId = MId;
		o->Type = Type;
		if (EventData) o->EventData = *EventData;
		return o;
	}
};

%extend SaHpiSensorReadingUnionT {
	SaHpiSensorReadingUnionT(SaHpiInt64T SensorInt64 = 0, SaHpiUint64T SensorUint64 = 0, SaHpiFloat64T SensorFloat64 = 0, SaHpiUint8T SensorBuffer[SAHPI_SENSOR_BUFFER_LENGTH] = NULL) {
		SaHpiSensorReadingUnionT *o;
		o = (SaHpiSensorReadingUnionT *)malloc(sizeof(SaHpiSensorReadingUnionT));
		memset(o, 0, sizeof(SaHpiSensorReadingUnionT));
		o->SensorInt64 = SensorInt64;
		o->SensorUint64 = SensorUint64;
		o->SensorFloat64 = SensorFloat64;
		if (SensorBuffer) memcpy(o->SensorBuffer, SensorBuffer, sizeof(SaHpiUint8T)*SAHPI_SENSOR_BUFFER_LENGTH);
		return o;
	}
};

%extend SaHpiConditionT {
	SaHpiConditionT(SaHpiStatusCondTypeT Type = 0, SaHpiEntityPathT *Entity = NULL, SaHpiDomainIdT DomainId = 0, SaHpiResourceIdT ResourceId = 0, SaHpiSensorNumT SensorNum = 0, SaHpiEventStateT EventState = 0, SaHpiNameT *Name = NULL, SaHpiManufacturerIdT Mid = 0, SaHpiTextBufferT *Data = NULL) {
		SaHpiConditionT *o;
		o = (SaHpiConditionT *)malloc(sizeof(SaHpiConditionT));
		memset(o, 0, sizeof(SaHpiConditionT));
		o->Type = Type;
		if (Entity) o->Entity = *Entity;
		o->DomainId = DomainId;
		o->ResourceId = ResourceId;
		o->SensorNum = SensorNum;
		o->EventState = EventState;
		if (Name) o->Name = *Name;
		o->Mid = Mid;
		if (Data) o->Data = *Data;
		return o;
	}
};

%extend SaHpiDomainEventT {
	SaHpiDomainEventT(SaHpiDomainEventTypeT Type = 0, SaHpiDomainIdT DomainId = 0) {
		SaHpiDomainEventT *o;
		o = (SaHpiDomainEventT *)malloc(sizeof(SaHpiDomainEventT));
		memset(o, 0, sizeof(SaHpiDomainEventT));
		o->Type = Type;
		o->DomainId = DomainId;
		return o;
	}
};

%extend SaHpiResourceInfoT {
	SaHpiResourceInfoT(SaHpiUint8T ResourceRev = 0, SaHpiUint8T SpecificVer = 0, SaHpiUint8T DeviceSupport = 0, SaHpiManufacturerIdT ManufacturerId = 0, SaHpiUint16T ProductId = 0, SaHpiUint8T FirmwareMajorRev = 0, SaHpiUint8T FirmwareMinorRev = 0, SaHpiUint8T AuxFirmwareRev = 0, SaHpiGuidT Guid = 0) {
		SaHpiResourceInfoT *o;
		o = (SaHpiResourceInfoT *)malloc(sizeof(SaHpiResourceInfoT));
		memset(o, 0, sizeof(SaHpiResourceInfoT));
		o->ResourceRev = ResourceRev;
		o->SpecificVer = SpecificVer;
		o->DeviceSupport = DeviceSupport;
		o->ManufacturerId = ManufacturerId;
		o->ProductId = ProductId;
		o->FirmwareMajorRev = FirmwareMajorRev;
		o->FirmwareMinorRev = FirmwareMinorRev;
		o->AuxFirmwareRev = AuxFirmwareRev;
		if (Guid) memcpy(o->Guid, Guid, sizeof(SaHpiGuidT));
		return o;
	}
};

%extend SaHpiEntityT {
	SaHpiEntityT(SaHpiEntityTypeT EntityType = 0, SaHpiEntityLocationT EntityLocation = 0) {
		SaHpiEntityT *o;
		o = (SaHpiEntityT *)malloc(sizeof(SaHpiEntityT));
		memset(o, 0, sizeof(SaHpiEntityT));
		o->EntityType = EntityType;
		o->EntityLocation = EntityLocation;
		return o;
	}
};

%extend SaHpiRdrTypeUnionT {
	SaHpiRdrTypeUnionT(SaHpiCtrlRecT *CtrlRec = NULL, SaHpiSensorRecT *SensorRec = NULL, SaHpiInventoryRecT *InventoryRec = NULL, SaHpiWatchdogRecT *WatchdogRec = NULL, SaHpiAnnunciatorRecT *AnnunciatorRec = NULL, SaHpiDimiRecT *DimiRec = NULL, SaHpiFumiRecT *FumiRec = NULL) {
		SaHpiRdrTypeUnionT *o;
		o = (SaHpiRdrTypeUnionT *)malloc(sizeof(SaHpiRdrTypeUnionT));
		memset(o, 0, sizeof(SaHpiRdrTypeUnionT));
		if (CtrlRec) o->CtrlRec = *CtrlRec;
		if (SensorRec) o->SensorRec = *SensorRec;
		if (InventoryRec) o->InventoryRec = *InventoryRec;
		if (WatchdogRec) o->WatchdogRec = *WatchdogRec;
		if (AnnunciatorRec) o->AnnunciatorRec = *AnnunciatorRec;
		if (DimiRec) o->DimiRec = *DimiRec;
		if (FumiRec) o->FumiRec = *FumiRec;
		return o;
	}
};

%extend SaHpiSensorDataFormatT {
	SaHpiSensorDataFormatT(SaHpiBoolT IsSupported = 0, SaHpiSensorReadingTypeT ReadingType = 0, SaHpiSensorUnitsT BaseUnits = 0, SaHpiSensorUnitsT ModifierUnits = 0, SaHpiSensorModUnitUseT ModifierUse = 0, SaHpiBoolT Percentage = 0, SaHpiSensorRangeT *Range = NULL, SaHpiFloat64T AccuracyFactor = 0) {
		SaHpiSensorDataFormatT *o;
		o = (SaHpiSensorDataFormatT *)malloc(sizeof(SaHpiSensorDataFormatT));
		memset(o, 0, sizeof(SaHpiSensorDataFormatT));
		o->IsSupported = IsSupported;
		o->ReadingType = ReadingType;
		o->BaseUnits = BaseUnits;
		o->ModifierUnits = ModifierUnits;
		o->ModifierUse = ModifierUse;
		o->Percentage = Percentage;
		if (Range) o->Range = *Range;
		o->AccuracyFactor = AccuracyFactor;
		return o;
	}
};

%extend SaHpiDrtEntryT {
	SaHpiDrtEntryT(SaHpiEntryIdT EntryId = 0, SaHpiDomainIdT DomainId = 0, SaHpiBoolT IsPeer = 0) {
		SaHpiDrtEntryT *o;
		o = (SaHpiDrtEntryT *)malloc(sizeof(SaHpiDrtEntryT));
		memset(o, 0, sizeof(SaHpiDrtEntryT));
		o->EntryId = EntryId;
		o->DomainId = DomainId;
		o->IsPeer = IsPeer;
		return o;
	}
};

%extend SaHpiSensorRecT {
	SaHpiSensorRecT(SaHpiSensorNumT Num = 0, SaHpiSensorTypeT Type = 0, SaHpiEventCategoryT Category = 0, SaHpiBoolT EnableCtrl = 0, SaHpiSensorEventCtrlT EventCtrl = 0, SaHpiEventStateT Events = 0, SaHpiSensorDataFormatT *DataFormat = NULL, SaHpiSensorThdDefnT *ThresholdDefn = NULL, SaHpiUint32T Oem = 0) {
		SaHpiSensorRecT *o;
		o = (SaHpiSensorRecT *)malloc(sizeof(SaHpiSensorRecT));
		memset(o, 0, sizeof(SaHpiSensorRecT));
		o->Num = Num;
		o->Type = Type;
		o->Category = Category;
		o->EnableCtrl = EnableCtrl;
		o->EventCtrl = EventCtrl;
		o->Events = Events;
		if (DataFormat) o->DataFormat = *DataFormat;
		if (ThresholdDefn) o->ThresholdDefn = *ThresholdDefn;
		o->Oem = Oem;
		return o;
	}
};

%extend SaHpiCtrlRecAnalogT {
	SaHpiCtrlRecAnalogT(SaHpiCtrlStateAnalogT Min = 0, SaHpiCtrlStateAnalogT Max = 0, SaHpiCtrlStateAnalogT Default = 0) {
		SaHpiCtrlRecAnalogT *o;
		o = (SaHpiCtrlRecAnalogT *)malloc(sizeof(SaHpiCtrlRecAnalogT));
		memset(o, 0, sizeof(SaHpiCtrlRecAnalogT));
		o->Min = Min;
		o->Max = Max;
		o->Default = Default;
		return o;
	}
};

%extend SaHpiCtrlRecT {
	SaHpiCtrlRecT(SaHpiCtrlNumT Num = 0, SaHpiCtrlOutputTypeT OutputType = 0, SaHpiCtrlTypeT Type = 0, SaHpiCtrlRecUnionT *TypeUnion = NULL, SaHpiCtrlDefaultModeT *DefaultMode = NULL, SaHpiBoolT WriteOnly = 0, SaHpiUint32T Oem = 0) {
		SaHpiCtrlRecT *o;
		o = (SaHpiCtrlRecT *)malloc(sizeof(SaHpiCtrlRecT));
		memset(o, 0, sizeof(SaHpiCtrlRecT));
		o->Num = Num;
		o->OutputType = OutputType;
		o->Type = Type;
		if (TypeUnion) o->TypeUnion = *TypeUnion;
		if (DefaultMode) o->DefaultMode = *DefaultMode;
		o->WriteOnly = WriteOnly;
		o->Oem = Oem;
		return o;
	}
};

%extend SaHpiEventT {
	SaHpiEventT(SaHpiResourceIdT Source = 0, SaHpiEventTypeT EventType = 0, SaHpiTimeT Timestamp = 0, SaHpiSeverityT Severity = 0, SaHpiEventUnionT *EventDataUnion = NULL) {
		SaHpiEventT *o;
		o = (SaHpiEventT *)malloc(sizeof(SaHpiEventT));
		memset(o, 0, sizeof(SaHpiEventT));
		o->Source = Source;
		o->EventType = EventType;
		o->Timestamp = Timestamp;
		o->Severity = Severity;
		if (EventDataUnion) o->EventDataUnion = *EventDataUnion;
		return o;
	}
};

%extend SaHpiEntityPathT {
	SaHpiEntityPathT(SaHpiEntityT Entry[SAHPI_MAX_ENTITY_PATH] = NULL) {
		SaHpiEntityPathT *o;
		o = (SaHpiEntityPathT *)malloc(sizeof(SaHpiEntityPathT));
		memset(o, 0, sizeof(SaHpiEntityPathT));
		if (Entry) memcpy(o->Entry, Entry, sizeof(SaHpiEntityT)*SAHPI_MAX_ENTITY_PATH);
		return o;
	}
};

%extend SaHpiDimiUpdateEventT {
	SaHpiDimiUpdateEventT(SaHpiDimiNumT DimiNum = 0) {
		SaHpiDimiUpdateEventT *o;
		o = (SaHpiDimiUpdateEventT *)malloc(sizeof(SaHpiDimiUpdateEventT));
		memset(o, 0, sizeof(SaHpiDimiUpdateEventT));
		o->DimiNum = DimiNum;
		return o;
	}
};

%extend SaHpiDomainInfoT {
	SaHpiDomainInfoT(SaHpiDomainIdT DomainId = 0, SaHpiDomainCapabilitiesT DomainCapabilities = 0, SaHpiBoolT IsPeer = 0, SaHpiTextBufferT *DomainTag = NULL, SaHpiUint32T DrtUpdateCount = 0, SaHpiTimeT DrtUpdateTimestamp = 0, SaHpiUint32T RptUpdateCount = 0, SaHpiTimeT RptUpdateTimestamp = 0, SaHpiUint32T DatUpdateCount = 0, SaHpiTimeT DatUpdateTimestamp = 0, SaHpiUint32T ActiveAlarms = 0, SaHpiUint32T CriticalAlarms = 0, SaHpiUint32T MajorAlarms = 0, SaHpiUint32T MinorAlarms = 0, SaHpiUint32T DatUserAlarmLimit = 0, SaHpiBoolT DatOverflow = 0, SaHpiGuidT Guid = 0) {
		SaHpiDomainInfoT *o;
		o = (SaHpiDomainInfoT *)malloc(sizeof(SaHpiDomainInfoT));
		memset(o, 0, sizeof(SaHpiDomainInfoT));
		o->DomainId = DomainId;
		o->DomainCapabilities = DomainCapabilities;
		o->IsPeer = IsPeer;
		if (DomainTag) o->DomainTag = *DomainTag;
		o->DrtUpdateCount = DrtUpdateCount;
		o->DrtUpdateTimestamp = DrtUpdateTimestamp;
		o->RptUpdateCount = RptUpdateCount;
		o->RptUpdateTimestamp = RptUpdateTimestamp;
		o->DatUpdateCount = DatUpdateCount;
		o->DatUpdateTimestamp = DatUpdateTimestamp;
		o->ActiveAlarms = ActiveAlarms;
		o->CriticalAlarms = CriticalAlarms;
		o->MajorAlarms = MajorAlarms;
		o->MinorAlarms = MinorAlarms;
		o->DatUserAlarmLimit = DatUserAlarmLimit;
		o->DatOverflow = DatOverflow;
		if (Guid) memcpy(o->Guid, Guid, sizeof(SaHpiGuidT));
		return o;
	}
};

%extend SaHpiSensorReadingT {
	SaHpiSensorReadingT(SaHpiBoolT IsSupported = 0, SaHpiSensorReadingTypeT Type = 0, SaHpiSensorReadingUnionT *Value = NULL) {
		SaHpiSensorReadingT *o;
		o = (SaHpiSensorReadingT *)malloc(sizeof(SaHpiSensorReadingT));
		memset(o, 0, sizeof(SaHpiSensorReadingT));
		o->IsSupported = IsSupported;
		o->Type = Type;
		if (Value) o->Value = *Value;
		return o;
	}
};

%extend SaHpiSensorEnableChangeEventT {
	SaHpiSensorEnableChangeEventT(SaHpiSensorNumT SensorNum = 0, SaHpiSensorTypeT SensorType = 0, SaHpiEventCategoryT EventCategory = 0, SaHpiBoolT SensorEnable = 0, SaHpiBoolT SensorEventEnable = 0, SaHpiEventStateT AssertEventMask = 0, SaHpiEventStateT DeassertEventMask = 0, SaHpiSensorEnableOptDataT OptionalDataPresent = 0, SaHpiEventStateT CurrentState = 0, SaHpiEventStateT CriticalAlarms = 0, SaHpiEventStateT MajorAlarms = 0, SaHpiEventStateT MinorAlarms = 0) {
		SaHpiSensorEnableChangeEventT *o;
		o = (SaHpiSensorEnableChangeEventT *)malloc(sizeof(SaHpiSensorEnableChangeEventT));
		memset(o, 0, sizeof(SaHpiSensorEnableChangeEventT));
		o->SensorNum = SensorNum;
		o->SensorType = SensorType;
		o->EventCategory = EventCategory;
		o->SensorEnable = SensorEnable;
		o->SensorEventEnable = SensorEventEnable;
		o->AssertEventMask = AssertEventMask;
		o->DeassertEventMask = DeassertEventMask;
		o->OptionalDataPresent = OptionalDataPresent;
		o->CurrentState = CurrentState;
		o->CriticalAlarms = CriticalAlarms;
		o->MajorAlarms = MajorAlarms;
		o->MinorAlarms = MinorAlarms;
		return o;
	}
};

