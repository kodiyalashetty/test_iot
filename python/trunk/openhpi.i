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
	arg1->DataLength = datalen;
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
	arg1->BodyLength = datalen;
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
	arg1->StreamLength = datalen;
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
  			SWIG_exception_fail(SWIG_ArgError(res1),
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
                        SWIG_exception_fail(SWIG_ArgError(res1),
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
                        SWIG_exception_fail(SWIG_ArgError(res1),
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
                        SWIG_exception_fail(SWIG_ArgError(res1),
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
%typemap (in, numinputs=0) GSList **res_new (GSList *new_res) {
	new_res = NULL;
	$1 = &new_res;
}
%typemap (argout) GSList **res_new {
	GSList *node = NULL;
	int i = 0;
	PyObject *l = NULL;
	if (*$1) {
		if ($result && $result == Py_None) {
			Py_DECREF($result);
		}
		l = PyList_New(g_slist_length(*$1));
		for (node = *$1; node; node = node->next) {
			PyList_SetItem(l, i,
				SWIG_NewPointerObj(node->data,
						SWIGTYPE_p_SaHpiRptEntryT,0));
			i++;
		}
		g_slist_free(*$1);
	} else {
		l = $result;
	}
	$result = PyTuple_New(4);
        PyTuple_SetItem($result, 0, l);
}
%typemap (in, numinputs=0) GSList **rdr_new (GSList *new_rdr) {
	new_rdr = NULL;
	$1 = &new_rdr;
}
%typemap (argout) GSList **rdr_new {
	GSList *node = NULL;
	int i = 0;
	PyObject *l = NULL;
	if (*$1) {
		l = PyList_New(g_slist_length(*$1));
		for (node = *$1; node; node = node->next) {
			PyList_SetItem(l, i,
				SWIG_NewPointerObj(node->data,
						SWIGTYPE_p_SaHpiRdrT,0));
			i++;
		}
		g_slist_free(*$1);
	} else {
		l = Py_None; Py_INCREF(l);
	}
        PyTuple_SetItem($result, 1, l);
}
%typemap (in, numinputs=0) GSList **res_gone (GSList *gone_res) {
	gone_res = NULL;
	$1 = &gone_res;
}
%typemap (argout) GSList **res_gone {
	GSList *node = NULL;
	int i = 0;
	PyObject *l = NULL;
	if (*$1) {
		l = PyList_New(g_slist_length(*$1));
		for (node = *$1; node; node = node->next) {
			PyList_SetItem(l, i,
				SWIG_NewPointerObj(node->data,
						SWIGTYPE_p_SaHpiRptEntryT,0));
			i++;
		}
		g_slist_free(*$1);
	} else {
		l = Py_None; Py_INCREF(l);
	}
        PyTuple_SetItem($result, 2, l);
}
%typemap (in, numinputs=0) GSList **rdr_gone (GSList *gone_rdr) {
	gone_rdr = NULL;
	$1 = &gone_rdr;
}
%typemap (argout) GSList **rdr_gone {
	GSList *node = NULL;
	int i = 0;
	PyObject *l = NULL;
	if (*$1) {
		l = PyList_New(g_slist_length(*$1));
		for (node = *$1; node; node = node->next) {
			PyList_SetItem(l, i,
				SWIG_NewPointerObj(node->data,
						SWIGTYPE_p_SaHpiRdrT,0));
			i++;
		}
		g_slist_free(*$1);
	} else {
		l = Py_None; Py_INCREF(l);
	}
        PyTuple_SetItem($result, 3, l);
}
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
%sizeof(SaHpiUint8T)
%sizeof(SaHpiUint16T)
%sizeof(SaHpiUint32T)
%sizeof(SaHpiUint64T)
%sizeof(SaHpiInt8T)
%sizeof(SaHpiInt16T)
%sizeof(SaHpiInt32T)
%sizeof(SaHpiInt64T)
%sizeof(SaHpiFloat64T)
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
%sizeof(SaHpiHsIndicatorStateT)
%sizeof(SaHpiHsActionT)
%sizeof(SaHpiHsStateT)
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
%sizeof(SaHpiEventLogEntryIdT)
%sizeof(SaHpiEventLogEntryT)
