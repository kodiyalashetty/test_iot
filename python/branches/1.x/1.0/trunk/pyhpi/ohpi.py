# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.


#
# This file was modified manually by Vadim Reviakin <vadim.a.revyakin@intel.com>
#

import lib_ohpi

def _swig_setattr(self,class_type,name,value):
    if (name == "this"):
        if isinstance(value, class_type):
            self.__dict__[name] = value.this
            if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
            del value.thisown
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    self.__dict__[name] = value

def _swig_getattr(self,class_type,name):
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


SAHPI_TRUE = lib_ohpi.SAHPI_TRUE
SAHPI_FALSE = lib_ohpi.SAHPI_FALSE
SAHPI_MANUFACTURER_ID_UNSPECIFIED = lib_ohpi.SAHPI_MANUFACTURER_ID_UNSPECIFIED
SAHPI_INTERFACE_VERSION = lib_ohpi.SAHPI_INTERFACE_VERSION
SA_OK = lib_ohpi.SA_OK
SA_HPI_ERR_BASE = lib_ohpi.SA_HPI_ERR_BASE
SA_ERR_HPI_ERROR = lib_ohpi.SA_ERR_HPI_ERROR
SA_ERR_HPI_UNSUPPORTED_API = lib_ohpi.SA_ERR_HPI_UNSUPPORTED_API
SA_ERR_HPI_BUSY = lib_ohpi.SA_ERR_HPI_BUSY
SA_ERR_HPI_INTERNAL_ERROR = lib_ohpi.SA_ERR_HPI_INTERNAL_ERROR
SA_ERR_HPI_INVALID_CMD = lib_ohpi.SA_ERR_HPI_INVALID_CMD
SA_ERR_HPI_TIMEOUT = lib_ohpi.SA_ERR_HPI_TIMEOUT
SA_ERR_HPI_OUT_OF_SPACE = lib_ohpi.SA_ERR_HPI_OUT_OF_SPACE
SA_ERR_HPI_OUT_OF_MEMORY = lib_ohpi.SA_ERR_HPI_OUT_OF_MEMORY
SA_ERR_HPI_INVALID_PARAMS = lib_ohpi.SA_ERR_HPI_INVALID_PARAMS
SA_ERR_HPI_INVALID_DATA = lib_ohpi.SA_ERR_HPI_INVALID_DATA
SA_ERR_HPI_NOT_PRESENT = lib_ohpi.SA_ERR_HPI_NOT_PRESENT
SA_ERR_HPI_NO_RESPONSE = lib_ohpi.SA_ERR_HPI_NO_RESPONSE
SA_ERR_HPI_DUPLICATE = lib_ohpi.SA_ERR_HPI_DUPLICATE
SA_ERR_HPI_INVALID_SESSION = lib_ohpi.SA_ERR_HPI_INVALID_SESSION
SA_ERR_HPI_INVALID_DOMAIN = lib_ohpi.SA_ERR_HPI_INVALID_DOMAIN
SA_ERR_HPI_INVALID_RESOURCE = lib_ohpi.SA_ERR_HPI_INVALID_RESOURCE
SA_ERR_HPI_INVALID_REQUEST = lib_ohpi.SA_ERR_HPI_INVALID_REQUEST
SA_ERR_HPI_ENTITY_NOT_PRESENT = lib_ohpi.SA_ERR_HPI_ENTITY_NOT_PRESENT
SA_ERR_HPI_READ_ONLY = lib_ohpi.SA_ERR_HPI_READ_ONLY
SA_ERR_HPI_CAPABILITY = lib_ohpi.SA_ERR_HPI_CAPABILITY
SA_ERR_HPI_UNKNOWN = lib_ohpi.SA_ERR_HPI_UNKNOWN
SAHPI_UNSPECIFIED_DOMAIN_ID = lib_ohpi.SAHPI_UNSPECIFIED_DOMAIN_ID
SAHPI_UNSPECIFIED_RESOURCE_ID = lib_ohpi.SAHPI_UNSPECIFIED_RESOURCE_ID
SAHPI_FIRST_ENTRY = lib_ohpi.SAHPI_FIRST_ENTRY
SAHPI_LAST_ENTRY = lib_ohpi.SAHPI_LAST_ENTRY
SAHPI_ENTRY_UNSPECIFIED = lib_ohpi.SAHPI_ENTRY_UNSPECIFIED
SAHPI_TIME_UNSPECIFIED = lib_ohpi.SAHPI_TIME_UNSPECIFIED
SAHPI_TIME_MAX_RELATIVE = lib_ohpi.SAHPI_TIME_MAX_RELATIVE
SAHPI_TIMEOUT_IMMEDIATE = lib_ohpi.SAHPI_TIMEOUT_IMMEDIATE
SAHPI_TIMEOUT_BLOCK = lib_ohpi.SAHPI_TIMEOUT_BLOCK
SAHPI_LANG_UNDEF = lib_ohpi.SAHPI_LANG_UNDEF
SAHPI_LANG_AFAR = lib_ohpi.SAHPI_LANG_AFAR
SAHPI_LANG_ABKHAZIAN = lib_ohpi.SAHPI_LANG_ABKHAZIAN
SAHPI_LANG_AFRIKAANS = lib_ohpi.SAHPI_LANG_AFRIKAANS
SAHPI_LANG_AMHARIC = lib_ohpi.SAHPI_LANG_AMHARIC
SAHPI_LANG_ARABIC = lib_ohpi.SAHPI_LANG_ARABIC
SAHPI_LANG_ASSAMESE = lib_ohpi.SAHPI_LANG_ASSAMESE
SAHPI_LANG_AYMARA = lib_ohpi.SAHPI_LANG_AYMARA
SAHPI_LANG_AZERBAIJANI = lib_ohpi.SAHPI_LANG_AZERBAIJANI
SAHPI_LANG_BASHKIR = lib_ohpi.SAHPI_LANG_BASHKIR
SAHPI_LANG_BYELORUSSIAN = lib_ohpi.SAHPI_LANG_BYELORUSSIAN
SAHPI_LANG_BULGARIAN = lib_ohpi.SAHPI_LANG_BULGARIAN
SAHPI_LANG_BIHARI = lib_ohpi.SAHPI_LANG_BIHARI
SAHPI_LANG_BISLAMA = lib_ohpi.SAHPI_LANG_BISLAMA
SAHPI_LANG_BENGALI = lib_ohpi.SAHPI_LANG_BENGALI
SAHPI_LANG_TIBETAN = lib_ohpi.SAHPI_LANG_TIBETAN
SAHPI_LANG_BRETON = lib_ohpi.SAHPI_LANG_BRETON
SAHPI_LANG_CATALAN = lib_ohpi.SAHPI_LANG_CATALAN
SAHPI_LANG_CORSICAN = lib_ohpi.SAHPI_LANG_CORSICAN
SAHPI_LANG_CZECH = lib_ohpi.SAHPI_LANG_CZECH
SAHPI_LANG_WELSH = lib_ohpi.SAHPI_LANG_WELSH
SAHPI_LANG_DANISH = lib_ohpi.SAHPI_LANG_DANISH
SAHPI_LANG_GERMAN = lib_ohpi.SAHPI_LANG_GERMAN
SAHPI_LANG_BHUTANI = lib_ohpi.SAHPI_LANG_BHUTANI
SAHPI_LANG_GREEK = lib_ohpi.SAHPI_LANG_GREEK
SAHPI_LANG_ENGLISH = lib_ohpi.SAHPI_LANG_ENGLISH
SAHPI_LANG_ESPERANTO = lib_ohpi.SAHPI_LANG_ESPERANTO
SAHPI_LANG_SPANISH = lib_ohpi.SAHPI_LANG_SPANISH
SAHPI_LANG_ESTONIAN = lib_ohpi.SAHPI_LANG_ESTONIAN
SAHPI_LANG_BASQUE = lib_ohpi.SAHPI_LANG_BASQUE
SAHPI_LANG_PERSIAN = lib_ohpi.SAHPI_LANG_PERSIAN
SAHPI_LANG_FINNISH = lib_ohpi.SAHPI_LANG_FINNISH
SAHPI_LANG_FIJI = lib_ohpi.SAHPI_LANG_FIJI
SAHPI_LANG_FAEROESE = lib_ohpi.SAHPI_LANG_FAEROESE
SAHPI_LANG_FRENCH = lib_ohpi.SAHPI_LANG_FRENCH
SAHPI_LANG_FRISIAN = lib_ohpi.SAHPI_LANG_FRISIAN
SAHPI_LANG_IRISH = lib_ohpi.SAHPI_LANG_IRISH
SAHPI_LANG_SCOTSGAELIC = lib_ohpi.SAHPI_LANG_SCOTSGAELIC
SAHPI_LANG_GALICIAN = lib_ohpi.SAHPI_LANG_GALICIAN
SAHPI_LANG_GUARANI = lib_ohpi.SAHPI_LANG_GUARANI
SAHPI_LANG_GUJARATI = lib_ohpi.SAHPI_LANG_GUJARATI
SAHPI_LANG_HAUSA = lib_ohpi.SAHPI_LANG_HAUSA
SAHPI_LANG_HINDI = lib_ohpi.SAHPI_LANG_HINDI
SAHPI_LANG_CROATIAN = lib_ohpi.SAHPI_LANG_CROATIAN
SAHPI_LANG_HUNGARIAN = lib_ohpi.SAHPI_LANG_HUNGARIAN
SAHPI_LANG_ARMENIAN = lib_ohpi.SAHPI_LANG_ARMENIAN
SAHPI_LANG_INTERLINGUA = lib_ohpi.SAHPI_LANG_INTERLINGUA
SAHPI_LANG_INTERLINGUE = lib_ohpi.SAHPI_LANG_INTERLINGUE
SAHPI_LANG_INUPIAK = lib_ohpi.SAHPI_LANG_INUPIAK
SAHPI_LANG_INDONESIAN = lib_ohpi.SAHPI_LANG_INDONESIAN
SAHPI_LANG_ICELANDIC = lib_ohpi.SAHPI_LANG_ICELANDIC
SAHPI_LANG_ITALIAN = lib_ohpi.SAHPI_LANG_ITALIAN
SAHPI_LANG_HEBREW = lib_ohpi.SAHPI_LANG_HEBREW
SAHPI_LANG_JAPANESE = lib_ohpi.SAHPI_LANG_JAPANESE
SAHPI_LANG_YIDDISH = lib_ohpi.SAHPI_LANG_YIDDISH
SAHPI_LANG_JAVANESE = lib_ohpi.SAHPI_LANG_JAVANESE
SAHPI_LANG_GEORGIAN = lib_ohpi.SAHPI_LANG_GEORGIAN
SAHPI_LANG_KAZAKH = lib_ohpi.SAHPI_LANG_KAZAKH
SAHPI_LANG_GREENLANDIC = lib_ohpi.SAHPI_LANG_GREENLANDIC
SAHPI_LANG_CAMBODIAN = lib_ohpi.SAHPI_LANG_CAMBODIAN
SAHPI_LANG_KANNADA = lib_ohpi.SAHPI_LANG_KANNADA
SAHPI_LANG_KOREAN = lib_ohpi.SAHPI_LANG_KOREAN
SAHPI_LANG_KASHMIRI = lib_ohpi.SAHPI_LANG_KASHMIRI
SAHPI_LANG_KURDISH = lib_ohpi.SAHPI_LANG_KURDISH
SAHPI_LANG_KIRGHIZ = lib_ohpi.SAHPI_LANG_KIRGHIZ
SAHPI_LANG_LATIN = lib_ohpi.SAHPI_LANG_LATIN
SAHPI_LANG_LINGALA = lib_ohpi.SAHPI_LANG_LINGALA
SAHPI_LANG_LAOTHIAN = lib_ohpi.SAHPI_LANG_LAOTHIAN
SAHPI_LANG_LITHUANIAN = lib_ohpi.SAHPI_LANG_LITHUANIAN
SAHPI_LANG_LATVIANLETTISH = lib_ohpi.SAHPI_LANG_LATVIANLETTISH
SAHPI_LANG_MALAGASY = lib_ohpi.SAHPI_LANG_MALAGASY
SAHPI_LANG_MAORI = lib_ohpi.SAHPI_LANG_MAORI
SAHPI_LANG_MACEDONIAN = lib_ohpi.SAHPI_LANG_MACEDONIAN
SAHPI_LANG_MALAYALAM = lib_ohpi.SAHPI_LANG_MALAYALAM
SAHPI_LANG_MONGOLIAN = lib_ohpi.SAHPI_LANG_MONGOLIAN
SAHPI_LANG_MOLDAVIAN = lib_ohpi.SAHPI_LANG_MOLDAVIAN
SAHPI_LANG_MARATHI = lib_ohpi.SAHPI_LANG_MARATHI
SAHPI_LANG_MALAY = lib_ohpi.SAHPI_LANG_MALAY
SAHPI_LANG_MALTESE = lib_ohpi.SAHPI_LANG_MALTESE
SAHPI_LANG_BURMESE = lib_ohpi.SAHPI_LANG_BURMESE
SAHPI_LANG_NAURU = lib_ohpi.SAHPI_LANG_NAURU
SAHPI_LANG_NEPALI = lib_ohpi.SAHPI_LANG_NEPALI
SAHPI_LANG_DUTCH = lib_ohpi.SAHPI_LANG_DUTCH
SAHPI_LANG_NORWEGIAN = lib_ohpi.SAHPI_LANG_NORWEGIAN
SAHPI_LANG_OCCITAN = lib_ohpi.SAHPI_LANG_OCCITAN
SAHPI_LANG_AFANOROMO = lib_ohpi.SAHPI_LANG_AFANOROMO
SAHPI_LANG_ORIYA = lib_ohpi.SAHPI_LANG_ORIYA
SAHPI_LANG_PUNJABI = lib_ohpi.SAHPI_LANG_PUNJABI
SAHPI_LANG_POLISH = lib_ohpi.SAHPI_LANG_POLISH
SAHPI_LANG_PASHTOPUSHTO = lib_ohpi.SAHPI_LANG_PASHTOPUSHTO
SAHPI_LANG_PORTUGUESE = lib_ohpi.SAHPI_LANG_PORTUGUESE
SAHPI_LANG_QUECHUA = lib_ohpi.SAHPI_LANG_QUECHUA
SAHPI_LANG_RHAETOROMANCE = lib_ohpi.SAHPI_LANG_RHAETOROMANCE
SAHPI_LANG_KIRUNDI = lib_ohpi.SAHPI_LANG_KIRUNDI
SAHPI_LANG_ROMANIAN = lib_ohpi.SAHPI_LANG_ROMANIAN
SAHPI_LANG_RUSSIAN = lib_ohpi.SAHPI_LANG_RUSSIAN
SAHPI_LANG_KINYARWANDA = lib_ohpi.SAHPI_LANG_KINYARWANDA
SAHPI_LANG_SANSKRIT = lib_ohpi.SAHPI_LANG_SANSKRIT
SAHPI_LANG_SINDHI = lib_ohpi.SAHPI_LANG_SINDHI
SAHPI_LANG_SANGRO = lib_ohpi.SAHPI_LANG_SANGRO
SAHPI_LANG_SERBOCROATIAN = lib_ohpi.SAHPI_LANG_SERBOCROATIAN
SAHPI_LANG_SINGHALESE = lib_ohpi.SAHPI_LANG_SINGHALESE
SAHPI_LANG_SLOVAK = lib_ohpi.SAHPI_LANG_SLOVAK
SAHPI_LANG_SLOVENIAN = lib_ohpi.SAHPI_LANG_SLOVENIAN
SAHPI_LANG_SAMOAN = lib_ohpi.SAHPI_LANG_SAMOAN
SAHPI_LANG_SHONA = lib_ohpi.SAHPI_LANG_SHONA
SAHPI_LANG_SOMALI = lib_ohpi.SAHPI_LANG_SOMALI
SAHPI_LANG_ALBANIAN = lib_ohpi.SAHPI_LANG_ALBANIAN
SAHPI_LANG_SERBIAN = lib_ohpi.SAHPI_LANG_SERBIAN
SAHPI_LANG_SISWATI = lib_ohpi.SAHPI_LANG_SISWATI
SAHPI_LANG_SESOTHO = lib_ohpi.SAHPI_LANG_SESOTHO
SAHPI_LANG_SUDANESE = lib_ohpi.SAHPI_LANG_SUDANESE
SAHPI_LANG_SWEDISH = lib_ohpi.SAHPI_LANG_SWEDISH
SAHPI_LANG_SWAHILI = lib_ohpi.SAHPI_LANG_SWAHILI
SAHPI_LANG_TAMIL = lib_ohpi.SAHPI_LANG_TAMIL
SAHPI_LANG_TELUGU = lib_ohpi.SAHPI_LANG_TELUGU
SAHPI_LANG_TAJIK = lib_ohpi.SAHPI_LANG_TAJIK
SAHPI_LANG_THAI = lib_ohpi.SAHPI_LANG_THAI
SAHPI_LANG_TIGRINYA = lib_ohpi.SAHPI_LANG_TIGRINYA
SAHPI_LANG_TURKMEN = lib_ohpi.SAHPI_LANG_TURKMEN
SAHPI_LANG_TAGALOG = lib_ohpi.SAHPI_LANG_TAGALOG
SAHPI_LANG_SETSWANA = lib_ohpi.SAHPI_LANG_SETSWANA
SAHPI_LANG_TONGA = lib_ohpi.SAHPI_LANG_TONGA
SAHPI_LANG_TURKISH = lib_ohpi.SAHPI_LANG_TURKISH
SAHPI_LANG_TSONGA = lib_ohpi.SAHPI_LANG_TSONGA
SAHPI_LANG_TATAR = lib_ohpi.SAHPI_LANG_TATAR
SAHPI_LANG_TWI = lib_ohpi.SAHPI_LANG_TWI
SAHPI_LANG_UKRAINIAN = lib_ohpi.SAHPI_LANG_UKRAINIAN
SAHPI_LANG_URDU = lib_ohpi.SAHPI_LANG_URDU
SAHPI_LANG_UZBEK = lib_ohpi.SAHPI_LANG_UZBEK
SAHPI_LANG_VIETNAMESE = lib_ohpi.SAHPI_LANG_VIETNAMESE
SAHPI_LANG_VOLAPUK = lib_ohpi.SAHPI_LANG_VOLAPUK
SAHPI_LANG_WOLOF = lib_ohpi.SAHPI_LANG_WOLOF
SAHPI_LANG_XHOSA = lib_ohpi.SAHPI_LANG_XHOSA
SAHPI_LANG_YORUBA = lib_ohpi.SAHPI_LANG_YORUBA
SAHPI_LANG_CHINESE = lib_ohpi.SAHPI_LANG_CHINESE
SAHPI_LANG_ZULU = lib_ohpi.SAHPI_LANG_ZULU
SAHPI_MAX_TEXT_BUFFER_LENGTH = lib_ohpi.SAHPI_MAX_TEXT_BUFFER_LENGTH
SAHPI_TL_TYPE_UNICODE = lib_ohpi.SAHPI_TL_TYPE_UNICODE
SAHPI_TL_TYPE_BCDPLUS = lib_ohpi.SAHPI_TL_TYPE_BCDPLUS
SAHPI_TL_TYPE_ASCII6 = lib_ohpi.SAHPI_TL_TYPE_ASCII6
SAHPI_TL_TYPE_TEXT = lib_ohpi.SAHPI_TL_TYPE_TEXT
SAHPI_TL_TYPE_BINARY = lib_ohpi.SAHPI_TL_TYPE_BINARY
class SaHpiTextBufferT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiTextBufferT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiTextBufferT, name)
    def __repr__(self):
        return "<C SaHpiTextBufferT instance at %s>" % (self.this,)
    __swig_setmethods__["DataType"] = lib_ohpi.SaHpiTextBufferT_DataType_set
    __swig_getmethods__["DataType"] = lib_ohpi.SaHpiTextBufferT_DataType_get
    if _newclass:DataType = property(lib_ohpi.SaHpiTextBufferT_DataType_get, lib_ohpi.SaHpiTextBufferT_DataType_set)
    __swig_setmethods__["Language"] = lib_ohpi.SaHpiTextBufferT_Language_set
    __swig_getmethods__["Language"] = lib_ohpi.SaHpiTextBufferT_Language_get
    if _newclass:Language = property(lib_ohpi.SaHpiTextBufferT_Language_get, lib_ohpi.SaHpiTextBufferT_Language_set)
    __swig_setmethods__["DataLength"] = lib_ohpi.SaHpiTextBufferT_DataLength_set
    __swig_getmethods__["DataLength"] = lib_ohpi.SaHpiTextBufferT_DataLength_get
    if _newclass:DataLength = property(lib_ohpi.SaHpiTextBufferT_DataLength_get, lib_ohpi.SaHpiTextBufferT_DataLength_set)
    __swig_setmethods__["Data"] = lib_ohpi.SaHpiTextBufferT_Data_set
    __swig_getmethods__["Data"] = lib_ohpi.SaHpiTextBufferT_Data_get
    if _newclass:Data = property(lib_ohpi.SaHpiTextBufferT_Data_get, lib_ohpi.SaHpiTextBufferT_Data_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiTextBufferT, 'this', lib_ohpi.new_SaHpiTextBufferT(*args))
        _swig_setattr(self, SaHpiTextBufferT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiTextBufferT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiTextBufferTPtr(SaHpiTextBufferT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiTextBufferT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiTextBufferT, 'thisown', 0)
        _swig_setattr(self, SaHpiTextBufferT,self.__class__,SaHpiTextBufferT)
lib_ohpi.SaHpiTextBufferT_swigregister(SaHpiTextBufferTPtr)

SAHPI_ENT_IPMI_GROUP = lib_ohpi.SAHPI_ENT_IPMI_GROUP
SAHPI_ENT_SAFHPI_GROUP = lib_ohpi.SAHPI_ENT_SAFHPI_GROUP
SAHPI_ENT_ROOT_VALUE = lib_ohpi.SAHPI_ENT_ROOT_VALUE
SAHPI_ENT_UNSPECIFIED = lib_ohpi.SAHPI_ENT_UNSPECIFIED
SAHPI_ENT_OTHER = lib_ohpi.SAHPI_ENT_OTHER
SAHPI_ENT_UNKNOWN = lib_ohpi.SAHPI_ENT_UNKNOWN
SAHPI_ENT_PROCESSOR = lib_ohpi.SAHPI_ENT_PROCESSOR
SAHPI_ENT_DISK_BAY = lib_ohpi.SAHPI_ENT_DISK_BAY
SAHPI_ENT_PERIPHERAL_BAY = lib_ohpi.SAHPI_ENT_PERIPHERAL_BAY
SAHPI_ENT_SYS_MGMNT_MODULE = lib_ohpi.SAHPI_ENT_SYS_MGMNT_MODULE
SAHPI_ENT_SYSTEM_BOARD = lib_ohpi.SAHPI_ENT_SYSTEM_BOARD
SAHPI_ENT_MEMORY_MODULE = lib_ohpi.SAHPI_ENT_MEMORY_MODULE
SAHPI_ENT_PROCESSOR_MODULE = lib_ohpi.SAHPI_ENT_PROCESSOR_MODULE
SAHPI_ENT_POWER_SUPPLY = lib_ohpi.SAHPI_ENT_POWER_SUPPLY
SAHPI_ENT_ADD_IN_CARD = lib_ohpi.SAHPI_ENT_ADD_IN_CARD
SAHPI_ENT_FRONT_PANEL_BOARD = lib_ohpi.SAHPI_ENT_FRONT_PANEL_BOARD
SAHPI_ENT_BACK_PANEL_BOARD = lib_ohpi.SAHPI_ENT_BACK_PANEL_BOARD
SAHPI_ENT_POWER_SYSTEM_BOARD = lib_ohpi.SAHPI_ENT_POWER_SYSTEM_BOARD
SAHPI_ENT_DRIVE_BACKPLANE = lib_ohpi.SAHPI_ENT_DRIVE_BACKPLANE
SAHPI_ENT_SYS_EXPANSION_BOARD = lib_ohpi.SAHPI_ENT_SYS_EXPANSION_BOARD
SAHPI_ENT_OTHER_SYSTEM_BOARD = lib_ohpi.SAHPI_ENT_OTHER_SYSTEM_BOARD
SAHPI_ENT_PROCESSOR_BOARD = lib_ohpi.SAHPI_ENT_PROCESSOR_BOARD
SAHPI_ENT_POWER_UNIT = lib_ohpi.SAHPI_ENT_POWER_UNIT
SAHPI_ENT_POWER_MODULE = lib_ohpi.SAHPI_ENT_POWER_MODULE
SAHPI_ENT_POWER_MGMNT = lib_ohpi.SAHPI_ENT_POWER_MGMNT
SAHPI_ENT_CHASSIS_BACK_PANEL_BOARD = lib_ohpi.SAHPI_ENT_CHASSIS_BACK_PANEL_BOARD
SAHPI_ENT_SYSTEM_CHASSIS = lib_ohpi.SAHPI_ENT_SYSTEM_CHASSIS
SAHPI_ENT_SUB_CHASSIS = lib_ohpi.SAHPI_ENT_SUB_CHASSIS
SAHPI_ENT_OTHER_CHASSIS_BOARD = lib_ohpi.SAHPI_ENT_OTHER_CHASSIS_BOARD
SAHPI_ENT_DISK_DRIVE_BAY = lib_ohpi.SAHPI_ENT_DISK_DRIVE_BAY
SAHPI_ENT_PERIPHERAL_BAY_2 = lib_ohpi.SAHPI_ENT_PERIPHERAL_BAY_2
SAHPI_ENT_DEVICE_BAY = lib_ohpi.SAHPI_ENT_DEVICE_BAY
SAHPI_ENT_COOLING_DEVICE = lib_ohpi.SAHPI_ENT_COOLING_DEVICE
SAHPI_ENT_COOLING_UNIT = lib_ohpi.SAHPI_ENT_COOLING_UNIT
SAHPI_ENT_INTERCONNECT = lib_ohpi.SAHPI_ENT_INTERCONNECT
SAHPI_ENT_MEMORY_DEVICE = lib_ohpi.SAHPI_ENT_MEMORY_DEVICE
SAHPI_ENT_SYS_MGMNT_SOFTWARE = lib_ohpi.SAHPI_ENT_SYS_MGMNT_SOFTWARE
SAHPI_ENT_BIOS = lib_ohpi.SAHPI_ENT_BIOS
SAHPI_ENT_OPERATING_SYSTEM = lib_ohpi.SAHPI_ENT_OPERATING_SYSTEM
SAHPI_ENT_SYSTEM_BUS = lib_ohpi.SAHPI_ENT_SYSTEM_BUS
SAHPI_ENT_GROUP = lib_ohpi.SAHPI_ENT_GROUP
SAHPI_ENT_REMOTE = lib_ohpi.SAHPI_ENT_REMOTE
SAHPI_ENT_EXTERNAL_ENVIRONMENT = lib_ohpi.SAHPI_ENT_EXTERNAL_ENVIRONMENT
SAHPI_ENT_BATTERY = lib_ohpi.SAHPI_ENT_BATTERY
SAHPI_ENT_CHASSIS_SPECIFIC = lib_ohpi.SAHPI_ENT_CHASSIS_SPECIFIC
SAHPI_ENT_BOARD_SET_SPECIFIC = lib_ohpi.SAHPI_ENT_BOARD_SET_SPECIFIC
SAHPI_ENT_OEM_SYSINT_SPECIFIC = lib_ohpi.SAHPI_ENT_OEM_SYSINT_SPECIFIC
SAHPI_ENT_ROOT = lib_ohpi.SAHPI_ENT_ROOT
SAHPI_ENT_RACK = lib_ohpi.SAHPI_ENT_RACK
SAHPI_ENT_SUBRACK = lib_ohpi.SAHPI_ENT_SUBRACK
SAHPI_ENT_COMPACTPCI_CHASSIS = lib_ohpi.SAHPI_ENT_COMPACTPCI_CHASSIS
SAHPI_ENT_ADVANCEDTCA_CHASSIS = lib_ohpi.SAHPI_ENT_ADVANCEDTCA_CHASSIS
SAHPI_ENT_RACK_MOUNTED_SERVER = lib_ohpi.SAHPI_ENT_RACK_MOUNTED_SERVER
SAHPI_ENT_SYSTEM_BLADE = lib_ohpi.SAHPI_ENT_SYSTEM_BLADE
SAHPI_ENT_SWITCH = lib_ohpi.SAHPI_ENT_SWITCH
SAHPI_ENT_SWITCH_BLADE = lib_ohpi.SAHPI_ENT_SWITCH_BLADE
SAHPI_ENT_SBC_BLADE = lib_ohpi.SAHPI_ENT_SBC_BLADE
SAHPI_ENT_IO_BLADE = lib_ohpi.SAHPI_ENT_IO_BLADE
SAHPI_ENT_DISK_BLADE = lib_ohpi.SAHPI_ENT_DISK_BLADE
SAHPI_ENT_DISK_DRIVE = lib_ohpi.SAHPI_ENT_DISK_DRIVE
SAHPI_ENT_FAN = lib_ohpi.SAHPI_ENT_FAN
SAHPI_ENT_POWER_DISTRIBUTION_UNIT = lib_ohpi.SAHPI_ENT_POWER_DISTRIBUTION_UNIT
SAHPI_ENT_SPEC_PROC_BLADE = lib_ohpi.SAHPI_ENT_SPEC_PROC_BLADE
SAHPI_ENT_IO_SUBBOARD = lib_ohpi.SAHPI_ENT_IO_SUBBOARD
SAHPI_ENT_SBC_SUBBOARD = lib_ohpi.SAHPI_ENT_SBC_SUBBOARD
SAHPI_ENT_ALARM_MANAGER = lib_ohpi.SAHPI_ENT_ALARM_MANAGER
SAHPI_ENT_SHELF_MANAGER = lib_ohpi.SAHPI_ENT_SHELF_MANAGER
SAHPI_ENT_DISPLAY_PANEL = lib_ohpi.SAHPI_ENT_DISPLAY_PANEL
SAHPI_ENT_SUBBOARD_CARRIER_BLADE = lib_ohpi.SAHPI_ENT_SUBBOARD_CARRIER_BLADE
SAHPI_ENT_PHYSICAL_SLOT = lib_ohpi.SAHPI_ENT_PHYSICAL_SLOT
class SaHpiEntityT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiEntityT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiEntityT, name)
    def __repr__(self):
        return "<C SaHpiEntityT instance at %s>" % (self.this,)
    __swig_setmethods__["EntityType"] = lib_ohpi.SaHpiEntityT_EntityType_set
    __swig_getmethods__["EntityType"] = lib_ohpi.SaHpiEntityT_EntityType_get
    if _newclass:EntityType = property(lib_ohpi.SaHpiEntityT_EntityType_get, lib_ohpi.SaHpiEntityT_EntityType_set)
    __swig_setmethods__["EntityLocation"] = lib_ohpi.SaHpiEntityT_EntityLocation_set
    __swig_getmethods__["EntityLocation"] = lib_ohpi.SaHpiEntityT_EntityLocation_get
    if _newclass:EntityLocation = property(lib_ohpi.SaHpiEntityT_EntityLocation_get, lib_ohpi.SaHpiEntityT_EntityLocation_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiEntityT, 'this', lib_ohpi.new_SaHpiEntityT(*args))
        _swig_setattr(self, SaHpiEntityT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiEntityT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiEntityTPtr(SaHpiEntityT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiEntityT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiEntityT, 'thisown', 0)
        _swig_setattr(self, SaHpiEntityT,self.__class__,SaHpiEntityT)
lib_ohpi.SaHpiEntityT_swigregister(SaHpiEntityTPtr)

SAHPI_MAX_ENTITY_PATH = lib_ohpi.SAHPI_MAX_ENTITY_PATH
class SaHpiEntityPathT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiEntityPathT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiEntityPathT, name)
    def __repr__(self):
        return "<C SaHpiEntityPathT instance at %s>" % (self.this,)
    __swig_setmethods__["Entry"] = lib_ohpi.SaHpiEntityPathT_Entry_set
    __swig_getmethods__["Entry"] = lib_ohpi.SaHpiEntityPathT_Entry_get
    if _newclass:Entry = property(lib_ohpi.SaHpiEntityPathT_Entry_get, lib_ohpi.SaHpiEntityPathT_Entry_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiEntityPathT, 'this', lib_ohpi.new_SaHpiEntityPathT(*args))
        _swig_setattr(self, SaHpiEntityPathT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiEntityPathT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiEntityPathTPtr(SaHpiEntityPathT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiEntityPathT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiEntityPathT, 'thisown', 0)
        _swig_setattr(self, SaHpiEntityPathT,self.__class__,SaHpiEntityPathT)
lib_ohpi.SaHpiEntityPathT_swigregister(SaHpiEntityPathTPtr)

SAHPI_EC_UNSPECIFIED = lib_ohpi.SAHPI_EC_UNSPECIFIED
SAHPI_EC_THRESHOLD = lib_ohpi.SAHPI_EC_THRESHOLD
SAHPI_EC_USAGE = lib_ohpi.SAHPI_EC_USAGE
SAHPI_EC_STATE = lib_ohpi.SAHPI_EC_STATE
SAHPI_EC_PRED_FAIL = lib_ohpi.SAHPI_EC_PRED_FAIL
SAHPI_EC_LIMIT = lib_ohpi.SAHPI_EC_LIMIT
SAHPI_EC_PERFORMANCE = lib_ohpi.SAHPI_EC_PERFORMANCE
SAHPI_EC_SEVERITY = lib_ohpi.SAHPI_EC_SEVERITY
SAHPI_EC_PRESENCE = lib_ohpi.SAHPI_EC_PRESENCE
SAHPI_EC_ENABLE = lib_ohpi.SAHPI_EC_ENABLE
SAHPI_EC_AVAILABILITY = lib_ohpi.SAHPI_EC_AVAILABILITY
SAHPI_EC_REDUNDANCY = lib_ohpi.SAHPI_EC_REDUNDANCY
SAHPI_EC_SENSOR_SPECIFIC = lib_ohpi.SAHPI_EC_SENSOR_SPECIFIC
SAHPI_EC_GENERIC = lib_ohpi.SAHPI_EC_GENERIC
SAHPI_ES_UNSPECIFIED = lib_ohpi.SAHPI_ES_UNSPECIFIED
SAHPI_ES_LOWER_MINOR = lib_ohpi.SAHPI_ES_LOWER_MINOR
SAHPI_ES_LOWER_MAJOR = lib_ohpi.SAHPI_ES_LOWER_MAJOR
SAHPI_ES_LOWER_CRIT = lib_ohpi.SAHPI_ES_LOWER_CRIT
SAHPI_ES_UPPER_MINOR = lib_ohpi.SAHPI_ES_UPPER_MINOR
SAHPI_ES_UPPER_MAJOR = lib_ohpi.SAHPI_ES_UPPER_MAJOR
SAHPI_ES_UPPER_CRIT = lib_ohpi.SAHPI_ES_UPPER_CRIT
SAHPI_ES_IDLE = lib_ohpi.SAHPI_ES_IDLE
SAHPI_ES_ACTIVE = lib_ohpi.SAHPI_ES_ACTIVE
SAHPI_ES_BUSY = lib_ohpi.SAHPI_ES_BUSY
SAHPI_ES_STATE_DEASSERTED = lib_ohpi.SAHPI_ES_STATE_DEASSERTED
SAHPI_ES_STATE_ASSERTED = lib_ohpi.SAHPI_ES_STATE_ASSERTED
SAHPI_ES_PRED_FAILURE_DEASSERT = lib_ohpi.SAHPI_ES_PRED_FAILURE_DEASSERT
SAHPI_ES_PRED_FAILURE_ASSERT = lib_ohpi.SAHPI_ES_PRED_FAILURE_ASSERT
SAHPI_ES_LIMIT_NOT_EXCEEDED = lib_ohpi.SAHPI_ES_LIMIT_NOT_EXCEEDED
SAHPI_ES_LIMIT_EXCEEDED = lib_ohpi.SAHPI_ES_LIMIT_EXCEEDED
SAHPI_ES_PERFORMANCE_MET = lib_ohpi.SAHPI_ES_PERFORMANCE_MET
SAHPI_ES_PERFORMANCE_LAGS = lib_ohpi.SAHPI_ES_PERFORMANCE_LAGS
SAHPI_ES_OK = lib_ohpi.SAHPI_ES_OK
SAHPI_ES_MINOR_FROM_OK = lib_ohpi.SAHPI_ES_MINOR_FROM_OK
SAHPI_ES_MAJOR_FROM_LESS = lib_ohpi.SAHPI_ES_MAJOR_FROM_LESS
SAHPI_ES_CRITICAL_FROM_LESS = lib_ohpi.SAHPI_ES_CRITICAL_FROM_LESS
SAHPI_ES_MINOR_FROM_MORE = lib_ohpi.SAHPI_ES_MINOR_FROM_MORE
SAHPI_ES_MAJOR_FROM_CRITICAL = lib_ohpi.SAHPI_ES_MAJOR_FROM_CRITICAL
SAHPI_ES_CRITICAL = lib_ohpi.SAHPI_ES_CRITICAL
SAHPI_ES_MONITOR = lib_ohpi.SAHPI_ES_MONITOR
SAHPI_ES_INFORMATIONAL = lib_ohpi.SAHPI_ES_INFORMATIONAL
SAHPI_ES_ABSENT = lib_ohpi.SAHPI_ES_ABSENT
SAHPI_ES_PRESENT = lib_ohpi.SAHPI_ES_PRESENT
SAHPI_ES_DISABLED = lib_ohpi.SAHPI_ES_DISABLED
SAHPI_ES_ENABLED = lib_ohpi.SAHPI_ES_ENABLED
SAHPI_ES_RUNNING = lib_ohpi.SAHPI_ES_RUNNING
SAHPI_ES_TEST = lib_ohpi.SAHPI_ES_TEST
SAHPI_ES_POWER_OFF = lib_ohpi.SAHPI_ES_POWER_OFF
SAHPI_ES_ON_LINE = lib_ohpi.SAHPI_ES_ON_LINE
SAHPI_ES_OFF_LINE = lib_ohpi.SAHPI_ES_OFF_LINE
SAHPI_ES_OFF_DUTY = lib_ohpi.SAHPI_ES_OFF_DUTY
SAHPI_ES_DEGRADED = lib_ohpi.SAHPI_ES_DEGRADED
SAHPI_ES_POWER_SAVE = lib_ohpi.SAHPI_ES_POWER_SAVE
SAHPI_ES_INSTALL_ERROR = lib_ohpi.SAHPI_ES_INSTALL_ERROR
SAHPI_ES_FULLY_REDUNDANT = lib_ohpi.SAHPI_ES_FULLY_REDUNDANT
SAHPI_ES_REDUNDANCY_LOST = lib_ohpi.SAHPI_ES_REDUNDANCY_LOST
SAHPI_ES_REDUNDANCY_DEGRADED = lib_ohpi.SAHPI_ES_REDUNDANCY_DEGRADED
SAHPI_ES_REDUNDANCY_DEGRADED_FROM_FULL = lib_ohpi.SAHPI_ES_REDUNDANCY_DEGRADED_FROM_FULL
SAHPI_ES_REDUNDANCY_DEGRADED_FROM_NON = lib_ohpi.SAHPI_ES_REDUNDANCY_DEGRADED_FROM_NON
SAHPI_ES_STATE_00 = lib_ohpi.SAHPI_ES_STATE_00
SAHPI_ES_STATE_01 = lib_ohpi.SAHPI_ES_STATE_01
SAHPI_ES_STATE_02 = lib_ohpi.SAHPI_ES_STATE_02
SAHPI_ES_STATE_03 = lib_ohpi.SAHPI_ES_STATE_03
SAHPI_ES_STATE_04 = lib_ohpi.SAHPI_ES_STATE_04
SAHPI_ES_STATE_05 = lib_ohpi.SAHPI_ES_STATE_05
SAHPI_ES_STATE_06 = lib_ohpi.SAHPI_ES_STATE_06
SAHPI_ES_STATE_07 = lib_ohpi.SAHPI_ES_STATE_07
SAHPI_ES_STATE_08 = lib_ohpi.SAHPI_ES_STATE_08
SAHPI_ES_STATE_09 = lib_ohpi.SAHPI_ES_STATE_09
SAHPI_ES_STATE_10 = lib_ohpi.SAHPI_ES_STATE_10
SAHPI_ES_STATE_11 = lib_ohpi.SAHPI_ES_STATE_11
SAHPI_ES_STATE_12 = lib_ohpi.SAHPI_ES_STATE_12
SAHPI_ES_STATE_13 = lib_ohpi.SAHPI_ES_STATE_13
SAHPI_ES_STATE_14 = lib_ohpi.SAHPI_ES_STATE_14
SAHPI_STANDARD_SENSOR_MIN = lib_ohpi.SAHPI_STANDARD_SENSOR_MIN
SAHPI_STANDARD_SENSOR_MAX = lib_ohpi.SAHPI_STANDARD_SENSOR_MAX
SAHPI_TEMPERATURE = lib_ohpi.SAHPI_TEMPERATURE
SAHPI_VOLTAGE = lib_ohpi.SAHPI_VOLTAGE
SAHPI_CURRENT = lib_ohpi.SAHPI_CURRENT
SAHPI_FAN = lib_ohpi.SAHPI_FAN
SAHPI_PHYSICAL_SECURITY = lib_ohpi.SAHPI_PHYSICAL_SECURITY
SAHPI_PLATFORM_VIOLATION = lib_ohpi.SAHPI_PLATFORM_VIOLATION
SAHPI_PROCESSOR = lib_ohpi.SAHPI_PROCESSOR
SAHPI_POWER_SUPPLY = lib_ohpi.SAHPI_POWER_SUPPLY
SAHPI_POWER_UNIT = lib_ohpi.SAHPI_POWER_UNIT
SAHPI_COOLING_DEVICE = lib_ohpi.SAHPI_COOLING_DEVICE
SAHPI_OTHER_UNITS_BASED_SENSOR = lib_ohpi.SAHPI_OTHER_UNITS_BASED_SENSOR
SAHPI_MEMORY = lib_ohpi.SAHPI_MEMORY
SAHPI_DRIVE_SLOT = lib_ohpi.SAHPI_DRIVE_SLOT
SAHPI_POST_MEMORY_RESIZE = lib_ohpi.SAHPI_POST_MEMORY_RESIZE
SAHPI_SYSTEM_FW_PROGRESS = lib_ohpi.SAHPI_SYSTEM_FW_PROGRESS
SAHPI_EVENT_LOGGING_DISABLED = lib_ohpi.SAHPI_EVENT_LOGGING_DISABLED
SAHPI_RESERVED1 = lib_ohpi.SAHPI_RESERVED1
SAHPI_SYSTEM_EVENT = lib_ohpi.SAHPI_SYSTEM_EVENT
SAHPI_CRITICAL_INTERRUPT = lib_ohpi.SAHPI_CRITICAL_INTERRUPT
SAHPI_BUTTON = lib_ohpi.SAHPI_BUTTON
SAHPI_MODULE_BOARD = lib_ohpi.SAHPI_MODULE_BOARD
SAHPI_MICROCONTROLLER_COPROCESSOR = lib_ohpi.SAHPI_MICROCONTROLLER_COPROCESSOR
SAHPI_ADDIN_CARD = lib_ohpi.SAHPI_ADDIN_CARD
SAHPI_CHASSIS = lib_ohpi.SAHPI_CHASSIS
SAHPI_CHIP_SET = lib_ohpi.SAHPI_CHIP_SET
SAHPI_OTHER_FRU = lib_ohpi.SAHPI_OTHER_FRU
SAHPI_CABLE_INTERCONNECT = lib_ohpi.SAHPI_CABLE_INTERCONNECT
SAHPI_TERMINATOR = lib_ohpi.SAHPI_TERMINATOR
SAHPI_SYSTEM_BOOT_INITIATED = lib_ohpi.SAHPI_SYSTEM_BOOT_INITIATED
SAHPI_BOOT_ERROR = lib_ohpi.SAHPI_BOOT_ERROR
SAHPI_OS_BOOT = lib_ohpi.SAHPI_OS_BOOT
SAHPI_OS_CRITICAL_STOP = lib_ohpi.SAHPI_OS_CRITICAL_STOP
SAHPI_SLOT_CONNECTOR = lib_ohpi.SAHPI_SLOT_CONNECTOR
SAHPI_SYSTEM_ACPI_POWER_STATE = lib_ohpi.SAHPI_SYSTEM_ACPI_POWER_STATE
SAHPI_RESERVED2 = lib_ohpi.SAHPI_RESERVED2
SAHPI_PLATFORM_ALERT = lib_ohpi.SAHPI_PLATFORM_ALERT
SAHPI_ENTITY_PRESENCE = lib_ohpi.SAHPI_ENTITY_PRESENCE
SAHPI_MONITOR_ASIC_IC = lib_ohpi.SAHPI_MONITOR_ASIC_IC
SAHPI_LAN = lib_ohpi.SAHPI_LAN
SAHPI_MANAGEMENT_SUBSYSTEM_HEALTH = lib_ohpi.SAHPI_MANAGEMENT_SUBSYSTEM_HEALTH
SAHPI_BATTERY = lib_ohpi.SAHPI_BATTERY
SAHPI_OPERATIONAL = lib_ohpi.SAHPI_OPERATIONAL
SAHPI_OEM_SENSOR = lib_ohpi.SAHPI_OEM_SENSOR
SAHPI_SENSOR_BUFFER_LENGTH = lib_ohpi.SAHPI_SENSOR_BUFFER_LENGTH
SAHPI_SENSOR_READING_TYPE_INT64 = lib_ohpi.SAHPI_SENSOR_READING_TYPE_INT64
SAHPI_SENSOR_READING_TYPE_UINT64 = lib_ohpi.SAHPI_SENSOR_READING_TYPE_UINT64
SAHPI_SENSOR_READING_TYPE_FLOAT64 = lib_ohpi.SAHPI_SENSOR_READING_TYPE_FLOAT64
SAHPI_SENSOR_READING_TYPE_BUFFER = lib_ohpi.SAHPI_SENSOR_READING_TYPE_BUFFER
class SaHpiSensorReadingUnionT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiSensorReadingUnionT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiSensorReadingUnionT, name)
    def __repr__(self):
        return "<C SaHpiSensorReadingUnionT instance at %s>" % (self.this,)
    __swig_setmethods__["SensorInt64"] = lib_ohpi.SaHpiSensorReadingUnionT_SensorInt64_set
    __swig_getmethods__["SensorInt64"] = lib_ohpi.SaHpiSensorReadingUnionT_SensorInt64_get
    if _newclass:SensorInt64 = property(lib_ohpi.SaHpiSensorReadingUnionT_SensorInt64_get, lib_ohpi.SaHpiSensorReadingUnionT_SensorInt64_set)
    __swig_setmethods__["SensorUint64"] = lib_ohpi.SaHpiSensorReadingUnionT_SensorUint64_set
    __swig_getmethods__["SensorUint64"] = lib_ohpi.SaHpiSensorReadingUnionT_SensorUint64_get
    if _newclass:SensorUint64 = property(lib_ohpi.SaHpiSensorReadingUnionT_SensorUint64_get, lib_ohpi.SaHpiSensorReadingUnionT_SensorUint64_set)
    __swig_setmethods__["SensorFloat64"] = lib_ohpi.SaHpiSensorReadingUnionT_SensorFloat64_set
    __swig_getmethods__["SensorFloat64"] = lib_ohpi.SaHpiSensorReadingUnionT_SensorFloat64_get
    if _newclass:SensorFloat64 = property(lib_ohpi.SaHpiSensorReadingUnionT_SensorFloat64_get, lib_ohpi.SaHpiSensorReadingUnionT_SensorFloat64_set)
    __swig_setmethods__["SensorBuffer"] = lib_ohpi.SaHpiSensorReadingUnionT_SensorBuffer_set
    __swig_getmethods__["SensorBuffer"] = lib_ohpi.SaHpiSensorReadingUnionT_SensorBuffer_get
    if _newclass:SensorBuffer = property(lib_ohpi.SaHpiSensorReadingUnionT_SensorBuffer_get, lib_ohpi.SaHpiSensorReadingUnionT_SensorBuffer_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiSensorReadingUnionT, 'this', lib_ohpi.new_SaHpiSensorReadingUnionT(*args))
        _swig_setattr(self, SaHpiSensorReadingUnionT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiSensorReadingUnionT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiSensorReadingUnionTPtr(SaHpiSensorReadingUnionT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiSensorReadingUnionT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiSensorReadingUnionT, 'thisown', 0)
        _swig_setattr(self, SaHpiSensorReadingUnionT,self.__class__,SaHpiSensorReadingUnionT)
lib_ohpi.SaHpiSensorReadingUnionT_swigregister(SaHpiSensorReadingUnionTPtr)

class SaHpiSensorReadingT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiSensorReadingT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiSensorReadingT, name)
    def __repr__(self):
        return "<C SaHpiSensorReadingT instance at %s>" % (self.this,)
    __swig_setmethods__["IsSupported"] = lib_ohpi.SaHpiSensorReadingT_IsSupported_set
    __swig_getmethods__["IsSupported"] = lib_ohpi.SaHpiSensorReadingT_IsSupported_get
    if _newclass:IsSupported = property(lib_ohpi.SaHpiSensorReadingT_IsSupported_get, lib_ohpi.SaHpiSensorReadingT_IsSupported_set)
    __swig_setmethods__["Type"] = lib_ohpi.SaHpiSensorReadingT_Type_set
    __swig_getmethods__["Type"] = lib_ohpi.SaHpiSensorReadingT_Type_get
    if _newclass:Type = property(lib_ohpi.SaHpiSensorReadingT_Type_get, lib_ohpi.SaHpiSensorReadingT_Type_set)
    __swig_setmethods__["Value"] = lib_ohpi.SaHpiSensorReadingT_Value_set
    __swig_getmethods__["Value"] = lib_ohpi.SaHpiSensorReadingT_Value_get
    if _newclass:Value = property(lib_ohpi.SaHpiSensorReadingT_Value_get, lib_ohpi.SaHpiSensorReadingT_Value_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiSensorReadingT, 'this', lib_ohpi.new_SaHpiSensorReadingT(*args))
        _swig_setattr(self, SaHpiSensorReadingT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiSensorReadingT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiSensorReadingTPtr(SaHpiSensorReadingT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiSensorReadingT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiSensorReadingT, 'thisown', 0)
        _swig_setattr(self, SaHpiSensorReadingT,self.__class__,SaHpiSensorReadingT)
lib_ohpi.SaHpiSensorReadingT_swigregister(SaHpiSensorReadingTPtr)

SAHPI_SENS_ADD_EVENTS_TO_MASKS = lib_ohpi.SAHPI_SENS_ADD_EVENTS_TO_MASKS
SAHPI_SENS_REMOVE_EVENTS_FROM_MASKS = lib_ohpi.SAHPI_SENS_REMOVE_EVENTS_FROM_MASKS
SAHPI_ALL_EVENT_STATES = lib_ohpi.SAHPI_ALL_EVENT_STATES
class SaHpiSensorThresholdsT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiSensorThresholdsT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiSensorThresholdsT, name)
    def __repr__(self):
        return "<C SaHpiSensorThresholdsT instance at %s>" % (self.this,)
    __swig_setmethods__["LowCritical"] = lib_ohpi.SaHpiSensorThresholdsT_LowCritical_set
    __swig_getmethods__["LowCritical"] = lib_ohpi.SaHpiSensorThresholdsT_LowCritical_get
    if _newclass:LowCritical = property(lib_ohpi.SaHpiSensorThresholdsT_LowCritical_get, lib_ohpi.SaHpiSensorThresholdsT_LowCritical_set)
    __swig_setmethods__["LowMajor"] = lib_ohpi.SaHpiSensorThresholdsT_LowMajor_set
    __swig_getmethods__["LowMajor"] = lib_ohpi.SaHpiSensorThresholdsT_LowMajor_get
    if _newclass:LowMajor = property(lib_ohpi.SaHpiSensorThresholdsT_LowMajor_get, lib_ohpi.SaHpiSensorThresholdsT_LowMajor_set)
    __swig_setmethods__["LowMinor"] = lib_ohpi.SaHpiSensorThresholdsT_LowMinor_set
    __swig_getmethods__["LowMinor"] = lib_ohpi.SaHpiSensorThresholdsT_LowMinor_get
    if _newclass:LowMinor = property(lib_ohpi.SaHpiSensorThresholdsT_LowMinor_get, lib_ohpi.SaHpiSensorThresholdsT_LowMinor_set)
    __swig_setmethods__["UpCritical"] = lib_ohpi.SaHpiSensorThresholdsT_UpCritical_set
    __swig_getmethods__["UpCritical"] = lib_ohpi.SaHpiSensorThresholdsT_UpCritical_get
    if _newclass:UpCritical = property(lib_ohpi.SaHpiSensorThresholdsT_UpCritical_get, lib_ohpi.SaHpiSensorThresholdsT_UpCritical_set)
    __swig_setmethods__["UpMajor"] = lib_ohpi.SaHpiSensorThresholdsT_UpMajor_set
    __swig_getmethods__["UpMajor"] = lib_ohpi.SaHpiSensorThresholdsT_UpMajor_get
    if _newclass:UpMajor = property(lib_ohpi.SaHpiSensorThresholdsT_UpMajor_get, lib_ohpi.SaHpiSensorThresholdsT_UpMajor_set)
    __swig_setmethods__["UpMinor"] = lib_ohpi.SaHpiSensorThresholdsT_UpMinor_set
    __swig_getmethods__["UpMinor"] = lib_ohpi.SaHpiSensorThresholdsT_UpMinor_get
    if _newclass:UpMinor = property(lib_ohpi.SaHpiSensorThresholdsT_UpMinor_get, lib_ohpi.SaHpiSensorThresholdsT_UpMinor_set)
    __swig_setmethods__["PosThdHysteresis"] = lib_ohpi.SaHpiSensorThresholdsT_PosThdHysteresis_set
    __swig_getmethods__["PosThdHysteresis"] = lib_ohpi.SaHpiSensorThresholdsT_PosThdHysteresis_get
    if _newclass:PosThdHysteresis = property(lib_ohpi.SaHpiSensorThresholdsT_PosThdHysteresis_get, lib_ohpi.SaHpiSensorThresholdsT_PosThdHysteresis_set)
    __swig_setmethods__["NegThdHysteresis"] = lib_ohpi.SaHpiSensorThresholdsT_NegThdHysteresis_set
    __swig_getmethods__["NegThdHysteresis"] = lib_ohpi.SaHpiSensorThresholdsT_NegThdHysteresis_get
    if _newclass:NegThdHysteresis = property(lib_ohpi.SaHpiSensorThresholdsT_NegThdHysteresis_get, lib_ohpi.SaHpiSensorThresholdsT_NegThdHysteresis_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiSensorThresholdsT, 'this', lib_ohpi.new_SaHpiSensorThresholdsT(*args))
        _swig_setattr(self, SaHpiSensorThresholdsT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiSensorThresholdsT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiSensorThresholdsTPtr(SaHpiSensorThresholdsT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiSensorThresholdsT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiSensorThresholdsT, 'thisown', 0)
        _swig_setattr(self, SaHpiSensorThresholdsT,self.__class__,SaHpiSensorThresholdsT)
lib_ohpi.SaHpiSensorThresholdsT_swigregister(SaHpiSensorThresholdsTPtr)

SAHPI_SRF_MIN = lib_ohpi.SAHPI_SRF_MIN
SAHPI_SRF_MAX = lib_ohpi.SAHPI_SRF_MAX
SAHPI_SRF_NORMAL_MIN = lib_ohpi.SAHPI_SRF_NORMAL_MIN
SAHPI_SRF_NORMAL_MAX = lib_ohpi.SAHPI_SRF_NORMAL_MAX
SAHPI_SRF_NOMINAL = lib_ohpi.SAHPI_SRF_NOMINAL
class SaHpiSensorRangeT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiSensorRangeT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiSensorRangeT, name)
    def __repr__(self):
        return "<C SaHpiSensorRangeT instance at %s>" % (self.this,)
    __swig_setmethods__["Flags"] = lib_ohpi.SaHpiSensorRangeT_Flags_set
    __swig_getmethods__["Flags"] = lib_ohpi.SaHpiSensorRangeT_Flags_get
    if _newclass:Flags = property(lib_ohpi.SaHpiSensorRangeT_Flags_get, lib_ohpi.SaHpiSensorRangeT_Flags_set)
    __swig_setmethods__["Max"] = lib_ohpi.SaHpiSensorRangeT_Max_set
    __swig_getmethods__["Max"] = lib_ohpi.SaHpiSensorRangeT_Max_get
    if _newclass:Max = property(lib_ohpi.SaHpiSensorRangeT_Max_get, lib_ohpi.SaHpiSensorRangeT_Max_set)
    __swig_setmethods__["Min"] = lib_ohpi.SaHpiSensorRangeT_Min_set
    __swig_getmethods__["Min"] = lib_ohpi.SaHpiSensorRangeT_Min_get
    if _newclass:Min = property(lib_ohpi.SaHpiSensorRangeT_Min_get, lib_ohpi.SaHpiSensorRangeT_Min_set)
    __swig_setmethods__["Nominal"] = lib_ohpi.SaHpiSensorRangeT_Nominal_set
    __swig_getmethods__["Nominal"] = lib_ohpi.SaHpiSensorRangeT_Nominal_get
    if _newclass:Nominal = property(lib_ohpi.SaHpiSensorRangeT_Nominal_get, lib_ohpi.SaHpiSensorRangeT_Nominal_set)
    __swig_setmethods__["NormalMax"] = lib_ohpi.SaHpiSensorRangeT_NormalMax_set
    __swig_getmethods__["NormalMax"] = lib_ohpi.SaHpiSensorRangeT_NormalMax_get
    if _newclass:NormalMax = property(lib_ohpi.SaHpiSensorRangeT_NormalMax_get, lib_ohpi.SaHpiSensorRangeT_NormalMax_set)
    __swig_setmethods__["NormalMin"] = lib_ohpi.SaHpiSensorRangeT_NormalMin_set
    __swig_getmethods__["NormalMin"] = lib_ohpi.SaHpiSensorRangeT_NormalMin_get
    if _newclass:NormalMin = property(lib_ohpi.SaHpiSensorRangeT_NormalMin_get, lib_ohpi.SaHpiSensorRangeT_NormalMin_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiSensorRangeT, 'this', lib_ohpi.new_SaHpiSensorRangeT(*args))
        _swig_setattr(self, SaHpiSensorRangeT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiSensorRangeT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiSensorRangeTPtr(SaHpiSensorRangeT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiSensorRangeT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiSensorRangeT, 'thisown', 0)
        _swig_setattr(self, SaHpiSensorRangeT,self.__class__,SaHpiSensorRangeT)
lib_ohpi.SaHpiSensorRangeT_swigregister(SaHpiSensorRangeTPtr)

SAHPI_SU_UNSPECIFIED = lib_ohpi.SAHPI_SU_UNSPECIFIED
SAHPI_SU_DEGREES_C = lib_ohpi.SAHPI_SU_DEGREES_C
SAHPI_SU_DEGREES_F = lib_ohpi.SAHPI_SU_DEGREES_F
SAHPI_SU_DEGREES_K = lib_ohpi.SAHPI_SU_DEGREES_K
SAHPI_SU_VOLTS = lib_ohpi.SAHPI_SU_VOLTS
SAHPI_SU_AMPS = lib_ohpi.SAHPI_SU_AMPS
SAHPI_SU_WATTS = lib_ohpi.SAHPI_SU_WATTS
SAHPI_SU_JOULES = lib_ohpi.SAHPI_SU_JOULES
SAHPI_SU_COULOMBS = lib_ohpi.SAHPI_SU_COULOMBS
SAHPI_SU_VA = lib_ohpi.SAHPI_SU_VA
SAHPI_SU_NITS = lib_ohpi.SAHPI_SU_NITS
SAHPI_SU_LUMEN = lib_ohpi.SAHPI_SU_LUMEN
SAHPI_SU_LUX = lib_ohpi.SAHPI_SU_LUX
SAHPI_SU_CANDELA = lib_ohpi.SAHPI_SU_CANDELA
SAHPI_SU_KPA = lib_ohpi.SAHPI_SU_KPA
SAHPI_SU_PSI = lib_ohpi.SAHPI_SU_PSI
SAHPI_SU_NEWTON = lib_ohpi.SAHPI_SU_NEWTON
SAHPI_SU_CFM = lib_ohpi.SAHPI_SU_CFM
SAHPI_SU_RPM = lib_ohpi.SAHPI_SU_RPM
SAHPI_SU_HZ = lib_ohpi.SAHPI_SU_HZ
SAHPI_SU_MICROSECOND = lib_ohpi.SAHPI_SU_MICROSECOND
SAHPI_SU_MILLISECOND = lib_ohpi.SAHPI_SU_MILLISECOND
SAHPI_SU_SECOND = lib_ohpi.SAHPI_SU_SECOND
SAHPI_SU_MINUTE = lib_ohpi.SAHPI_SU_MINUTE
SAHPI_SU_HOUR = lib_ohpi.SAHPI_SU_HOUR
SAHPI_SU_DAY = lib_ohpi.SAHPI_SU_DAY
SAHPI_SU_WEEK = lib_ohpi.SAHPI_SU_WEEK
SAHPI_SU_MIL = lib_ohpi.SAHPI_SU_MIL
SAHPI_SU_INCHES = lib_ohpi.SAHPI_SU_INCHES
SAHPI_SU_FEET = lib_ohpi.SAHPI_SU_FEET
SAHPI_SU_CU_IN = lib_ohpi.SAHPI_SU_CU_IN
SAHPI_SU_CU_FEET = lib_ohpi.SAHPI_SU_CU_FEET
SAHPI_SU_MM = lib_ohpi.SAHPI_SU_MM
SAHPI_SU_CM = lib_ohpi.SAHPI_SU_CM
SAHPI_SU_M = lib_ohpi.SAHPI_SU_M
SAHPI_SU_CU_CM = lib_ohpi.SAHPI_SU_CU_CM
SAHPI_SU_CU_M = lib_ohpi.SAHPI_SU_CU_M
SAHPI_SU_LITERS = lib_ohpi.SAHPI_SU_LITERS
SAHPI_SU_FLUID_OUNCE = lib_ohpi.SAHPI_SU_FLUID_OUNCE
SAHPI_SU_RADIANS = lib_ohpi.SAHPI_SU_RADIANS
SAHPI_SU_STERADIANS = lib_ohpi.SAHPI_SU_STERADIANS
SAHPI_SU_REVOLUTIONS = lib_ohpi.SAHPI_SU_REVOLUTIONS
SAHPI_SU_CYCLES = lib_ohpi.SAHPI_SU_CYCLES
SAHPI_SU_GRAVITIES = lib_ohpi.SAHPI_SU_GRAVITIES
SAHPI_SU_OUNCE = lib_ohpi.SAHPI_SU_OUNCE
SAHPI_SU_POUND = lib_ohpi.SAHPI_SU_POUND
SAHPI_SU_FT_LB = lib_ohpi.SAHPI_SU_FT_LB
SAHPI_SU_OZ_IN = lib_ohpi.SAHPI_SU_OZ_IN
SAHPI_SU_GAUSS = lib_ohpi.SAHPI_SU_GAUSS
SAHPI_SU_GILBERTS = lib_ohpi.SAHPI_SU_GILBERTS
SAHPI_SU_HENRY = lib_ohpi.SAHPI_SU_HENRY
SAHPI_SU_MILLIHENRY = lib_ohpi.SAHPI_SU_MILLIHENRY
SAHPI_SU_FARAD = lib_ohpi.SAHPI_SU_FARAD
SAHPI_SU_MICROFARAD = lib_ohpi.SAHPI_SU_MICROFARAD
SAHPI_SU_OHMS = lib_ohpi.SAHPI_SU_OHMS
SAHPI_SU_SIEMENS = lib_ohpi.SAHPI_SU_SIEMENS
SAHPI_SU_MOLE = lib_ohpi.SAHPI_SU_MOLE
SAHPI_SU_BECQUEREL = lib_ohpi.SAHPI_SU_BECQUEREL
SAHPI_SU_PPM = lib_ohpi.SAHPI_SU_PPM
SAHPI_SU_RESERVED = lib_ohpi.SAHPI_SU_RESERVED
SAHPI_SU_DECIBELS = lib_ohpi.SAHPI_SU_DECIBELS
SAHPI_SU_DBA = lib_ohpi.SAHPI_SU_DBA
SAHPI_SU_DBC = lib_ohpi.SAHPI_SU_DBC
SAHPI_SU_GRAY = lib_ohpi.SAHPI_SU_GRAY
SAHPI_SU_SIEVERT = lib_ohpi.SAHPI_SU_SIEVERT
SAHPI_SU_COLOR_TEMP_DEG_K = lib_ohpi.SAHPI_SU_COLOR_TEMP_DEG_K
SAHPI_SU_BIT = lib_ohpi.SAHPI_SU_BIT
SAHPI_SU_KILOBIT = lib_ohpi.SAHPI_SU_KILOBIT
SAHPI_SU_MEGABIT = lib_ohpi.SAHPI_SU_MEGABIT
SAHPI_SU_GIGABIT = lib_ohpi.SAHPI_SU_GIGABIT
SAHPI_SU_BYTE = lib_ohpi.SAHPI_SU_BYTE
SAHPI_SU_KILOBYTE = lib_ohpi.SAHPI_SU_KILOBYTE
SAHPI_SU_MEGABYTE = lib_ohpi.SAHPI_SU_MEGABYTE
SAHPI_SU_GIGABYTE = lib_ohpi.SAHPI_SU_GIGABYTE
SAHPI_SU_WORD = lib_ohpi.SAHPI_SU_WORD
SAHPI_SU_DWORD = lib_ohpi.SAHPI_SU_DWORD
SAHPI_SU_QWORD = lib_ohpi.SAHPI_SU_QWORD
SAHPI_SU_LINE = lib_ohpi.SAHPI_SU_LINE
SAHPI_SU_HIT = lib_ohpi.SAHPI_SU_HIT
SAHPI_SU_MISS = lib_ohpi.SAHPI_SU_MISS
SAHPI_SU_RETRY = lib_ohpi.SAHPI_SU_RETRY
SAHPI_SU_RESET = lib_ohpi.SAHPI_SU_RESET
SAHPI_SU_OVERRUN = lib_ohpi.SAHPI_SU_OVERRUN
SAHPI_SU_UNDERRUN = lib_ohpi.SAHPI_SU_UNDERRUN
SAHPI_SU_COLLISION = lib_ohpi.SAHPI_SU_COLLISION
SAHPI_SU_PACKETS = lib_ohpi.SAHPI_SU_PACKETS
SAHPI_SU_MESSAGES = lib_ohpi.SAHPI_SU_MESSAGES
SAHPI_SU_CHARACTERS = lib_ohpi.SAHPI_SU_CHARACTERS
SAHPI_SU_ERRORS = lib_ohpi.SAHPI_SU_ERRORS
SAHPI_SU_CORRECTABLE_ERRORS = lib_ohpi.SAHPI_SU_CORRECTABLE_ERRORS
SAHPI_SU_UNCORRECTABLE_ERRORS = lib_ohpi.SAHPI_SU_UNCORRECTABLE_ERRORS
SAHPI_SMUU_NONE = lib_ohpi.SAHPI_SMUU_NONE
SAHPI_SMUU_BASIC_OVER_MODIFIER = lib_ohpi.SAHPI_SMUU_BASIC_OVER_MODIFIER
SAHPI_SMUU_BASIC_TIMES_MODIFIER = lib_ohpi.SAHPI_SMUU_BASIC_TIMES_MODIFIER
class SaHpiSensorDataFormatT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiSensorDataFormatT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiSensorDataFormatT, name)
    def __repr__(self):
        return "<C SaHpiSensorDataFormatT instance at %s>" % (self.this,)
    __swig_setmethods__["IsSupported"] = lib_ohpi.SaHpiSensorDataFormatT_IsSupported_set
    __swig_getmethods__["IsSupported"] = lib_ohpi.SaHpiSensorDataFormatT_IsSupported_get
    if _newclass:IsSupported = property(lib_ohpi.SaHpiSensorDataFormatT_IsSupported_get, lib_ohpi.SaHpiSensorDataFormatT_IsSupported_set)
    __swig_setmethods__["ReadingType"] = lib_ohpi.SaHpiSensorDataFormatT_ReadingType_set
    __swig_getmethods__["ReadingType"] = lib_ohpi.SaHpiSensorDataFormatT_ReadingType_get
    if _newclass:ReadingType = property(lib_ohpi.SaHpiSensorDataFormatT_ReadingType_get, lib_ohpi.SaHpiSensorDataFormatT_ReadingType_set)
    __swig_setmethods__["BaseUnits"] = lib_ohpi.SaHpiSensorDataFormatT_BaseUnits_set
    __swig_getmethods__["BaseUnits"] = lib_ohpi.SaHpiSensorDataFormatT_BaseUnits_get
    if _newclass:BaseUnits = property(lib_ohpi.SaHpiSensorDataFormatT_BaseUnits_get, lib_ohpi.SaHpiSensorDataFormatT_BaseUnits_set)
    __swig_setmethods__["ModifierUnits"] = lib_ohpi.SaHpiSensorDataFormatT_ModifierUnits_set
    __swig_getmethods__["ModifierUnits"] = lib_ohpi.SaHpiSensorDataFormatT_ModifierUnits_get
    if _newclass:ModifierUnits = property(lib_ohpi.SaHpiSensorDataFormatT_ModifierUnits_get, lib_ohpi.SaHpiSensorDataFormatT_ModifierUnits_set)
    __swig_setmethods__["ModifierUse"] = lib_ohpi.SaHpiSensorDataFormatT_ModifierUse_set
    __swig_getmethods__["ModifierUse"] = lib_ohpi.SaHpiSensorDataFormatT_ModifierUse_get
    if _newclass:ModifierUse = property(lib_ohpi.SaHpiSensorDataFormatT_ModifierUse_get, lib_ohpi.SaHpiSensorDataFormatT_ModifierUse_set)
    __swig_setmethods__["Percentage"] = lib_ohpi.SaHpiSensorDataFormatT_Percentage_set
    __swig_getmethods__["Percentage"] = lib_ohpi.SaHpiSensorDataFormatT_Percentage_get
    if _newclass:Percentage = property(lib_ohpi.SaHpiSensorDataFormatT_Percentage_get, lib_ohpi.SaHpiSensorDataFormatT_Percentage_set)
    __swig_setmethods__["Range"] = lib_ohpi.SaHpiSensorDataFormatT_Range_set
    __swig_getmethods__["Range"] = lib_ohpi.SaHpiSensorDataFormatT_Range_get
    if _newclass:Range = property(lib_ohpi.SaHpiSensorDataFormatT_Range_get, lib_ohpi.SaHpiSensorDataFormatT_Range_set)
    __swig_setmethods__["AccuracyFactor"] = lib_ohpi.SaHpiSensorDataFormatT_AccuracyFactor_set
    __swig_getmethods__["AccuracyFactor"] = lib_ohpi.SaHpiSensorDataFormatT_AccuracyFactor_get
    if _newclass:AccuracyFactor = property(lib_ohpi.SaHpiSensorDataFormatT_AccuracyFactor_get, lib_ohpi.SaHpiSensorDataFormatT_AccuracyFactor_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiSensorDataFormatT, 'this', lib_ohpi.new_SaHpiSensorDataFormatT(*args))
        _swig_setattr(self, SaHpiSensorDataFormatT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiSensorDataFormatT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiSensorDataFormatTPtr(SaHpiSensorDataFormatT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiSensorDataFormatT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiSensorDataFormatT, 'thisown', 0)
        _swig_setattr(self, SaHpiSensorDataFormatT,self.__class__,SaHpiSensorDataFormatT)
lib_ohpi.SaHpiSensorDataFormatT_swigregister(SaHpiSensorDataFormatTPtr)

SAHPI_STM_LOW_MINOR = lib_ohpi.SAHPI_STM_LOW_MINOR
SAHPI_STM_LOW_MAJOR = lib_ohpi.SAHPI_STM_LOW_MAJOR
SAHPI_STM_LOW_CRIT = lib_ohpi.SAHPI_STM_LOW_CRIT
SAHPI_STM_UP_MINOR = lib_ohpi.SAHPI_STM_UP_MINOR
SAHPI_STM_UP_MAJOR = lib_ohpi.SAHPI_STM_UP_MAJOR
SAHPI_STM_UP_CRIT = lib_ohpi.SAHPI_STM_UP_CRIT
SAHPI_STM_UP_HYSTERESIS = lib_ohpi.SAHPI_STM_UP_HYSTERESIS
SAHPI_STM_LOW_HYSTERESIS = lib_ohpi.SAHPI_STM_LOW_HYSTERESIS
class SaHpiSensorThdDefnT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiSensorThdDefnT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiSensorThdDefnT, name)
    def __repr__(self):
        return "<C SaHpiSensorThdDefnT instance at %s>" % (self.this,)
    __swig_setmethods__["IsAccessible"] = lib_ohpi.SaHpiSensorThdDefnT_IsAccessible_set
    __swig_getmethods__["IsAccessible"] = lib_ohpi.SaHpiSensorThdDefnT_IsAccessible_get
    if _newclass:IsAccessible = property(lib_ohpi.SaHpiSensorThdDefnT_IsAccessible_get, lib_ohpi.SaHpiSensorThdDefnT_IsAccessible_set)
    __swig_setmethods__["ReadThold"] = lib_ohpi.SaHpiSensorThdDefnT_ReadThold_set
    __swig_getmethods__["ReadThold"] = lib_ohpi.SaHpiSensorThdDefnT_ReadThold_get
    if _newclass:ReadThold = property(lib_ohpi.SaHpiSensorThdDefnT_ReadThold_get, lib_ohpi.SaHpiSensorThdDefnT_ReadThold_set)
    __swig_setmethods__["WriteThold"] = lib_ohpi.SaHpiSensorThdDefnT_WriteThold_set
    __swig_getmethods__["WriteThold"] = lib_ohpi.SaHpiSensorThdDefnT_WriteThold_get
    if _newclass:WriteThold = property(lib_ohpi.SaHpiSensorThdDefnT_WriteThold_get, lib_ohpi.SaHpiSensorThdDefnT_WriteThold_set)
    __swig_setmethods__["Nonlinear"] = lib_ohpi.SaHpiSensorThdDefnT_Nonlinear_set
    __swig_getmethods__["Nonlinear"] = lib_ohpi.SaHpiSensorThdDefnT_Nonlinear_get
    if _newclass:Nonlinear = property(lib_ohpi.SaHpiSensorThdDefnT_Nonlinear_get, lib_ohpi.SaHpiSensorThdDefnT_Nonlinear_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiSensorThdDefnT, 'this', lib_ohpi.new_SaHpiSensorThdDefnT(*args))
        _swig_setattr(self, SaHpiSensorThdDefnT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiSensorThdDefnT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiSensorThdDefnTPtr(SaHpiSensorThdDefnT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiSensorThdDefnT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiSensorThdDefnT, 'thisown', 0)
        _swig_setattr(self, SaHpiSensorThdDefnT,self.__class__,SaHpiSensorThdDefnT)
lib_ohpi.SaHpiSensorThdDefnT_swigregister(SaHpiSensorThdDefnTPtr)

SAHPI_SEC_PER_EVENT = lib_ohpi.SAHPI_SEC_PER_EVENT
SAHPI_SEC_READ_ONLY_MASKS = lib_ohpi.SAHPI_SEC_READ_ONLY_MASKS
SAHPI_SEC_READ_ONLY = lib_ohpi.SAHPI_SEC_READ_ONLY
class SaHpiSensorRecT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiSensorRecT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiSensorRecT, name)
    def __repr__(self):
        return "<C SaHpiSensorRecT instance at %s>" % (self.this,)
    __swig_setmethods__["Num"] = lib_ohpi.SaHpiSensorRecT_Num_set
    __swig_getmethods__["Num"] = lib_ohpi.SaHpiSensorRecT_Num_get
    if _newclass:Num = property(lib_ohpi.SaHpiSensorRecT_Num_get, lib_ohpi.SaHpiSensorRecT_Num_set)
    __swig_setmethods__["Type"] = lib_ohpi.SaHpiSensorRecT_Type_set
    __swig_getmethods__["Type"] = lib_ohpi.SaHpiSensorRecT_Type_get
    if _newclass:Type = property(lib_ohpi.SaHpiSensorRecT_Type_get, lib_ohpi.SaHpiSensorRecT_Type_set)
    __swig_setmethods__["Category"] = lib_ohpi.SaHpiSensorRecT_Category_set
    __swig_getmethods__["Category"] = lib_ohpi.SaHpiSensorRecT_Category_get
    if _newclass:Category = property(lib_ohpi.SaHpiSensorRecT_Category_get, lib_ohpi.SaHpiSensorRecT_Category_set)
    __swig_setmethods__["EnableCtrl"] = lib_ohpi.SaHpiSensorRecT_EnableCtrl_set
    __swig_getmethods__["EnableCtrl"] = lib_ohpi.SaHpiSensorRecT_EnableCtrl_get
    if _newclass:EnableCtrl = property(lib_ohpi.SaHpiSensorRecT_EnableCtrl_get, lib_ohpi.SaHpiSensorRecT_EnableCtrl_set)
    __swig_setmethods__["EventCtrl"] = lib_ohpi.SaHpiSensorRecT_EventCtrl_set
    __swig_getmethods__["EventCtrl"] = lib_ohpi.SaHpiSensorRecT_EventCtrl_get
    if _newclass:EventCtrl = property(lib_ohpi.SaHpiSensorRecT_EventCtrl_get, lib_ohpi.SaHpiSensorRecT_EventCtrl_set)
    __swig_setmethods__["Events"] = lib_ohpi.SaHpiSensorRecT_Events_set
    __swig_getmethods__["Events"] = lib_ohpi.SaHpiSensorRecT_Events_get
    if _newclass:Events = property(lib_ohpi.SaHpiSensorRecT_Events_get, lib_ohpi.SaHpiSensorRecT_Events_set)
    __swig_setmethods__["DataFormat"] = lib_ohpi.SaHpiSensorRecT_DataFormat_set
    __swig_getmethods__["DataFormat"] = lib_ohpi.SaHpiSensorRecT_DataFormat_get
    if _newclass:DataFormat = property(lib_ohpi.SaHpiSensorRecT_DataFormat_get, lib_ohpi.SaHpiSensorRecT_DataFormat_set)
    __swig_setmethods__["ThresholdDefn"] = lib_ohpi.SaHpiSensorRecT_ThresholdDefn_set
    __swig_getmethods__["ThresholdDefn"] = lib_ohpi.SaHpiSensorRecT_ThresholdDefn_get
    if _newclass:ThresholdDefn = property(lib_ohpi.SaHpiSensorRecT_ThresholdDefn_get, lib_ohpi.SaHpiSensorRecT_ThresholdDefn_set)
    __swig_setmethods__["Oem"] = lib_ohpi.SaHpiSensorRecT_Oem_set
    __swig_getmethods__["Oem"] = lib_ohpi.SaHpiSensorRecT_Oem_get
    if _newclass:Oem = property(lib_ohpi.SaHpiSensorRecT_Oem_get, lib_ohpi.SaHpiSensorRecT_Oem_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiSensorRecT, 'this', lib_ohpi.new_SaHpiSensorRecT(*args))
        _swig_setattr(self, SaHpiSensorRecT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiSensorRecT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiSensorRecTPtr(SaHpiSensorRecT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiSensorRecT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiSensorRecT, 'thisown', 0)
        _swig_setattr(self, SaHpiSensorRecT,self.__class__,SaHpiSensorRecT)
lib_ohpi.SaHpiSensorRecT_swigregister(SaHpiSensorRecTPtr)

SAHPI_DEFAGSENS_OPER = lib_ohpi.SAHPI_DEFAGSENS_OPER
SAHPI_DEFAGSENS_PWR = lib_ohpi.SAHPI_DEFAGSENS_PWR
SAHPI_DEFAGSENS_TEMP = lib_ohpi.SAHPI_DEFAGSENS_TEMP
SAHPI_DEFAGSENS_MIN = lib_ohpi.SAHPI_DEFAGSENS_MIN
SAHPI_DEFAGSENS_MAX = lib_ohpi.SAHPI_DEFAGSENS_MAX
SAHPI_CTRL_TYPE_DIGITAL = lib_ohpi.SAHPI_CTRL_TYPE_DIGITAL
SAHPI_CTRL_TYPE_DISCRETE = lib_ohpi.SAHPI_CTRL_TYPE_DISCRETE
SAHPI_CTRL_TYPE_ANALOG = lib_ohpi.SAHPI_CTRL_TYPE_ANALOG
SAHPI_CTRL_TYPE_STREAM = lib_ohpi.SAHPI_CTRL_TYPE_STREAM
SAHPI_CTRL_TYPE_TEXT = lib_ohpi.SAHPI_CTRL_TYPE_TEXT
SAHPI_CTRL_TYPE_OEM = lib_ohpi.SAHPI_CTRL_TYPE_OEM
SAHPI_CTRL_STATE_OFF = lib_ohpi.SAHPI_CTRL_STATE_OFF
SAHPI_CTRL_STATE_ON = lib_ohpi.SAHPI_CTRL_STATE_ON
SAHPI_CTRL_STATE_PULSE_OFF = lib_ohpi.SAHPI_CTRL_STATE_PULSE_OFF
SAHPI_CTRL_STATE_PULSE_ON = lib_ohpi.SAHPI_CTRL_STATE_PULSE_ON
SAHPI_CTRL_MAX_STREAM_LENGTH = lib_ohpi.SAHPI_CTRL_MAX_STREAM_LENGTH
class SaHpiCtrlStateStreamT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiCtrlStateStreamT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiCtrlStateStreamT, name)
    def __repr__(self):
        return "<C SaHpiCtrlStateStreamT instance at %s>" % (self.this,)
    __swig_setmethods__["Repeat"] = lib_ohpi.SaHpiCtrlStateStreamT_Repeat_set
    __swig_getmethods__["Repeat"] = lib_ohpi.SaHpiCtrlStateStreamT_Repeat_get
    if _newclass:Repeat = property(lib_ohpi.SaHpiCtrlStateStreamT_Repeat_get, lib_ohpi.SaHpiCtrlStateStreamT_Repeat_set)
    __swig_setmethods__["StreamLength"] = lib_ohpi.SaHpiCtrlStateStreamT_StreamLength_set
    __swig_getmethods__["StreamLength"] = lib_ohpi.SaHpiCtrlStateStreamT_StreamLength_get
    if _newclass:StreamLength = property(lib_ohpi.SaHpiCtrlStateStreamT_StreamLength_get, lib_ohpi.SaHpiCtrlStateStreamT_StreamLength_set)
    __swig_setmethods__["Stream"] = lib_ohpi.SaHpiCtrlStateStreamT_Stream_set
    __swig_getmethods__["Stream"] = lib_ohpi.SaHpiCtrlStateStreamT_Stream_get
    if _newclass:Stream = property(lib_ohpi.SaHpiCtrlStateStreamT_Stream_get, lib_ohpi.SaHpiCtrlStateStreamT_Stream_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiCtrlStateStreamT, 'this', lib_ohpi.new_SaHpiCtrlStateStreamT(*args))
        _swig_setattr(self, SaHpiCtrlStateStreamT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiCtrlStateStreamT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiCtrlStateStreamTPtr(SaHpiCtrlStateStreamT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiCtrlStateStreamT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiCtrlStateStreamT, 'thisown', 0)
        _swig_setattr(self, SaHpiCtrlStateStreamT,self.__class__,SaHpiCtrlStateStreamT)
lib_ohpi.SaHpiCtrlStateStreamT_swigregister(SaHpiCtrlStateStreamTPtr)

SAHPI_TLN_ALL_LINES = lib_ohpi.SAHPI_TLN_ALL_LINES
class SaHpiCtrlStateTextT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiCtrlStateTextT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiCtrlStateTextT, name)
    def __repr__(self):
        return "<C SaHpiCtrlStateTextT instance at %s>" % (self.this,)
    __swig_setmethods__["Line"] = lib_ohpi.SaHpiCtrlStateTextT_Line_set
    __swig_getmethods__["Line"] = lib_ohpi.SaHpiCtrlStateTextT_Line_get
    if _newclass:Line = property(lib_ohpi.SaHpiCtrlStateTextT_Line_get, lib_ohpi.SaHpiCtrlStateTextT_Line_set)
    __swig_setmethods__["Text"] = lib_ohpi.SaHpiCtrlStateTextT_Text_set
    __swig_getmethods__["Text"] = lib_ohpi.SaHpiCtrlStateTextT_Text_get
    if _newclass:Text = property(lib_ohpi.SaHpiCtrlStateTextT_Text_get, lib_ohpi.SaHpiCtrlStateTextT_Text_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiCtrlStateTextT, 'this', lib_ohpi.new_SaHpiCtrlStateTextT(*args))
        _swig_setattr(self, SaHpiCtrlStateTextT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiCtrlStateTextT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiCtrlStateTextTPtr(SaHpiCtrlStateTextT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiCtrlStateTextT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiCtrlStateTextT, 'thisown', 0)
        _swig_setattr(self, SaHpiCtrlStateTextT,self.__class__,SaHpiCtrlStateTextT)
lib_ohpi.SaHpiCtrlStateTextT_swigregister(SaHpiCtrlStateTextTPtr)

SAHPI_CTRL_MAX_OEM_BODY_LENGTH = lib_ohpi.SAHPI_CTRL_MAX_OEM_BODY_LENGTH
class SaHpiCtrlStateOemT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiCtrlStateOemT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiCtrlStateOemT, name)
    def __repr__(self):
        return "<C SaHpiCtrlStateOemT instance at %s>" % (self.this,)
    __swig_setmethods__["MId"] = lib_ohpi.SaHpiCtrlStateOemT_MId_set
    __swig_getmethods__["MId"] = lib_ohpi.SaHpiCtrlStateOemT_MId_get
    if _newclass:MId = property(lib_ohpi.SaHpiCtrlStateOemT_MId_get, lib_ohpi.SaHpiCtrlStateOemT_MId_set)
    __swig_setmethods__["BodyLength"] = lib_ohpi.SaHpiCtrlStateOemT_BodyLength_set
    __swig_getmethods__["BodyLength"] = lib_ohpi.SaHpiCtrlStateOemT_BodyLength_get
    if _newclass:BodyLength = property(lib_ohpi.SaHpiCtrlStateOemT_BodyLength_get, lib_ohpi.SaHpiCtrlStateOemT_BodyLength_set)
    __swig_setmethods__["Body"] = lib_ohpi.SaHpiCtrlStateOemT_Body_set
    __swig_getmethods__["Body"] = lib_ohpi.SaHpiCtrlStateOemT_Body_get
    if _newclass:Body = property(lib_ohpi.SaHpiCtrlStateOemT_Body_get, lib_ohpi.SaHpiCtrlStateOemT_Body_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiCtrlStateOemT, 'this', lib_ohpi.new_SaHpiCtrlStateOemT(*args))
        _swig_setattr(self, SaHpiCtrlStateOemT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiCtrlStateOemT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiCtrlStateOemTPtr(SaHpiCtrlStateOemT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiCtrlStateOemT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiCtrlStateOemT, 'thisown', 0)
        _swig_setattr(self, SaHpiCtrlStateOemT,self.__class__,SaHpiCtrlStateOemT)
lib_ohpi.SaHpiCtrlStateOemT_swigregister(SaHpiCtrlStateOemTPtr)

class SaHpiCtrlStateUnionT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiCtrlStateUnionT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiCtrlStateUnionT, name)
    def __repr__(self):
        return "<C SaHpiCtrlStateUnionT instance at %s>" % (self.this,)
    __swig_setmethods__["Digital"] = lib_ohpi.SaHpiCtrlStateUnionT_Digital_set
    __swig_getmethods__["Digital"] = lib_ohpi.SaHpiCtrlStateUnionT_Digital_get
    if _newclass:Digital = property(lib_ohpi.SaHpiCtrlStateUnionT_Digital_get, lib_ohpi.SaHpiCtrlStateUnionT_Digital_set)
    __swig_setmethods__["Discrete"] = lib_ohpi.SaHpiCtrlStateUnionT_Discrete_set
    __swig_getmethods__["Discrete"] = lib_ohpi.SaHpiCtrlStateUnionT_Discrete_get
    if _newclass:Discrete = property(lib_ohpi.SaHpiCtrlStateUnionT_Discrete_get, lib_ohpi.SaHpiCtrlStateUnionT_Discrete_set)
    __swig_setmethods__["Analog"] = lib_ohpi.SaHpiCtrlStateUnionT_Analog_set
    __swig_getmethods__["Analog"] = lib_ohpi.SaHpiCtrlStateUnionT_Analog_get
    if _newclass:Analog = property(lib_ohpi.SaHpiCtrlStateUnionT_Analog_get, lib_ohpi.SaHpiCtrlStateUnionT_Analog_set)
    __swig_setmethods__["Stream"] = lib_ohpi.SaHpiCtrlStateUnionT_Stream_set
    __swig_getmethods__["Stream"] = lib_ohpi.SaHpiCtrlStateUnionT_Stream_get
    if _newclass:Stream = property(lib_ohpi.SaHpiCtrlStateUnionT_Stream_get, lib_ohpi.SaHpiCtrlStateUnionT_Stream_set)
    __swig_setmethods__["Text"] = lib_ohpi.SaHpiCtrlStateUnionT_Text_set
    __swig_getmethods__["Text"] = lib_ohpi.SaHpiCtrlStateUnionT_Text_get
    if _newclass:Text = property(lib_ohpi.SaHpiCtrlStateUnionT_Text_get, lib_ohpi.SaHpiCtrlStateUnionT_Text_set)
    __swig_setmethods__["Oem"] = lib_ohpi.SaHpiCtrlStateUnionT_Oem_set
    __swig_getmethods__["Oem"] = lib_ohpi.SaHpiCtrlStateUnionT_Oem_get
    if _newclass:Oem = property(lib_ohpi.SaHpiCtrlStateUnionT_Oem_get, lib_ohpi.SaHpiCtrlStateUnionT_Oem_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiCtrlStateUnionT, 'this', lib_ohpi.new_SaHpiCtrlStateUnionT(*args))
        _swig_setattr(self, SaHpiCtrlStateUnionT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiCtrlStateUnionT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiCtrlStateUnionTPtr(SaHpiCtrlStateUnionT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiCtrlStateUnionT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiCtrlStateUnionT, 'thisown', 0)
        _swig_setattr(self, SaHpiCtrlStateUnionT,self.__class__,SaHpiCtrlStateUnionT)
lib_ohpi.SaHpiCtrlStateUnionT_swigregister(SaHpiCtrlStateUnionTPtr)

class SaHpiCtrlStateT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiCtrlStateT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiCtrlStateT, name)
    def __repr__(self):
        return "<C SaHpiCtrlStateT instance at %s>" % (self.this,)
    __swig_setmethods__["Type"] = lib_ohpi.SaHpiCtrlStateT_Type_set
    __swig_getmethods__["Type"] = lib_ohpi.SaHpiCtrlStateT_Type_get
    if _newclass:Type = property(lib_ohpi.SaHpiCtrlStateT_Type_get, lib_ohpi.SaHpiCtrlStateT_Type_set)
    __swig_setmethods__["StateUnion"] = lib_ohpi.SaHpiCtrlStateT_StateUnion_set
    __swig_getmethods__["StateUnion"] = lib_ohpi.SaHpiCtrlStateT_StateUnion_get
    if _newclass:StateUnion = property(lib_ohpi.SaHpiCtrlStateT_StateUnion_get, lib_ohpi.SaHpiCtrlStateT_StateUnion_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiCtrlStateT, 'this', lib_ohpi.new_SaHpiCtrlStateT(*args))
        _swig_setattr(self, SaHpiCtrlStateT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiCtrlStateT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiCtrlStateTPtr(SaHpiCtrlStateT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiCtrlStateT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiCtrlStateT, 'thisown', 0)
        _swig_setattr(self, SaHpiCtrlStateT,self.__class__,SaHpiCtrlStateT)
lib_ohpi.SaHpiCtrlStateT_swigregister(SaHpiCtrlStateTPtr)

SAHPI_CTRL_MODE_AUTO = lib_ohpi.SAHPI_CTRL_MODE_AUTO
SAHPI_CTRL_MODE_MANUAL = lib_ohpi.SAHPI_CTRL_MODE_MANUAL
SAHPI_CTRL_GENERIC = lib_ohpi.SAHPI_CTRL_GENERIC
SAHPI_CTRL_LED = lib_ohpi.SAHPI_CTRL_LED
SAHPI_CTRL_FAN_SPEED = lib_ohpi.SAHPI_CTRL_FAN_SPEED
SAHPI_CTRL_DRY_CONTACT_CLOSURE = lib_ohpi.SAHPI_CTRL_DRY_CONTACT_CLOSURE
SAHPI_CTRL_POWER_SUPPLY_INHIBIT = lib_ohpi.SAHPI_CTRL_POWER_SUPPLY_INHIBIT
SAHPI_CTRL_AUDIBLE = lib_ohpi.SAHPI_CTRL_AUDIBLE
SAHPI_CTRL_FRONT_PANEL_LOCKOUT = lib_ohpi.SAHPI_CTRL_FRONT_PANEL_LOCKOUT
SAHPI_CTRL_POWER_INTERLOCK = lib_ohpi.SAHPI_CTRL_POWER_INTERLOCK
SAHPI_CTRL_POWER_STATE = lib_ohpi.SAHPI_CTRL_POWER_STATE
SAHPI_CTRL_LCD_DISPLAY = lib_ohpi.SAHPI_CTRL_LCD_DISPLAY
SAHPI_CTRL_OEM = lib_ohpi.SAHPI_CTRL_OEM
class SaHpiCtrlRecDigitalT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiCtrlRecDigitalT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiCtrlRecDigitalT, name)
    def __repr__(self):
        return "<C SaHpiCtrlRecDigitalT instance at %s>" % (self.this,)
    __swig_setmethods__["Default"] = lib_ohpi.SaHpiCtrlRecDigitalT_Default_set
    __swig_getmethods__["Default"] = lib_ohpi.SaHpiCtrlRecDigitalT_Default_get
    if _newclass:Default = property(lib_ohpi.SaHpiCtrlRecDigitalT_Default_get, lib_ohpi.SaHpiCtrlRecDigitalT_Default_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiCtrlRecDigitalT, 'this', lib_ohpi.new_SaHpiCtrlRecDigitalT(*args))
        _swig_setattr(self, SaHpiCtrlRecDigitalT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiCtrlRecDigitalT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiCtrlRecDigitalTPtr(SaHpiCtrlRecDigitalT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiCtrlRecDigitalT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiCtrlRecDigitalT, 'thisown', 0)
        _swig_setattr(self, SaHpiCtrlRecDigitalT,self.__class__,SaHpiCtrlRecDigitalT)
lib_ohpi.SaHpiCtrlRecDigitalT_swigregister(SaHpiCtrlRecDigitalTPtr)

class SaHpiCtrlRecDiscreteT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiCtrlRecDiscreteT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiCtrlRecDiscreteT, name)
    def __repr__(self):
        return "<C SaHpiCtrlRecDiscreteT instance at %s>" % (self.this,)
    __swig_setmethods__["Default"] = lib_ohpi.SaHpiCtrlRecDiscreteT_Default_set
    __swig_getmethods__["Default"] = lib_ohpi.SaHpiCtrlRecDiscreteT_Default_get
    if _newclass:Default = property(lib_ohpi.SaHpiCtrlRecDiscreteT_Default_get, lib_ohpi.SaHpiCtrlRecDiscreteT_Default_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiCtrlRecDiscreteT, 'this', lib_ohpi.new_SaHpiCtrlRecDiscreteT(*args))
        _swig_setattr(self, SaHpiCtrlRecDiscreteT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiCtrlRecDiscreteT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiCtrlRecDiscreteTPtr(SaHpiCtrlRecDiscreteT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiCtrlRecDiscreteT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiCtrlRecDiscreteT, 'thisown', 0)
        _swig_setattr(self, SaHpiCtrlRecDiscreteT,self.__class__,SaHpiCtrlRecDiscreteT)
lib_ohpi.SaHpiCtrlRecDiscreteT_swigregister(SaHpiCtrlRecDiscreteTPtr)

class SaHpiCtrlRecAnalogT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiCtrlRecAnalogT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiCtrlRecAnalogT, name)
    def __repr__(self):
        return "<C SaHpiCtrlRecAnalogT instance at %s>" % (self.this,)
    __swig_setmethods__["Min"] = lib_ohpi.SaHpiCtrlRecAnalogT_Min_set
    __swig_getmethods__["Min"] = lib_ohpi.SaHpiCtrlRecAnalogT_Min_get
    if _newclass:Min = property(lib_ohpi.SaHpiCtrlRecAnalogT_Min_get, lib_ohpi.SaHpiCtrlRecAnalogT_Min_set)
    __swig_setmethods__["Max"] = lib_ohpi.SaHpiCtrlRecAnalogT_Max_set
    __swig_getmethods__["Max"] = lib_ohpi.SaHpiCtrlRecAnalogT_Max_get
    if _newclass:Max = property(lib_ohpi.SaHpiCtrlRecAnalogT_Max_get, lib_ohpi.SaHpiCtrlRecAnalogT_Max_set)
    __swig_setmethods__["Default"] = lib_ohpi.SaHpiCtrlRecAnalogT_Default_set
    __swig_getmethods__["Default"] = lib_ohpi.SaHpiCtrlRecAnalogT_Default_get
    if _newclass:Default = property(lib_ohpi.SaHpiCtrlRecAnalogT_Default_get, lib_ohpi.SaHpiCtrlRecAnalogT_Default_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiCtrlRecAnalogT, 'this', lib_ohpi.new_SaHpiCtrlRecAnalogT(*args))
        _swig_setattr(self, SaHpiCtrlRecAnalogT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiCtrlRecAnalogT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiCtrlRecAnalogTPtr(SaHpiCtrlRecAnalogT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiCtrlRecAnalogT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiCtrlRecAnalogT, 'thisown', 0)
        _swig_setattr(self, SaHpiCtrlRecAnalogT,self.__class__,SaHpiCtrlRecAnalogT)
lib_ohpi.SaHpiCtrlRecAnalogT_swigregister(SaHpiCtrlRecAnalogTPtr)

class SaHpiCtrlRecStreamT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiCtrlRecStreamT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiCtrlRecStreamT, name)
    def __repr__(self):
        return "<C SaHpiCtrlRecStreamT instance at %s>" % (self.this,)
    __swig_setmethods__["Default"] = lib_ohpi.SaHpiCtrlRecStreamT_Default_set
    __swig_getmethods__["Default"] = lib_ohpi.SaHpiCtrlRecStreamT_Default_get
    if _newclass:Default = property(lib_ohpi.SaHpiCtrlRecStreamT_Default_get, lib_ohpi.SaHpiCtrlRecStreamT_Default_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiCtrlRecStreamT, 'this', lib_ohpi.new_SaHpiCtrlRecStreamT(*args))
        _swig_setattr(self, SaHpiCtrlRecStreamT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiCtrlRecStreamT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiCtrlRecStreamTPtr(SaHpiCtrlRecStreamT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiCtrlRecStreamT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiCtrlRecStreamT, 'thisown', 0)
        _swig_setattr(self, SaHpiCtrlRecStreamT,self.__class__,SaHpiCtrlRecStreamT)
lib_ohpi.SaHpiCtrlRecStreamT_swigregister(SaHpiCtrlRecStreamTPtr)

class SaHpiCtrlRecTextT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiCtrlRecTextT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiCtrlRecTextT, name)
    def __repr__(self):
        return "<C SaHpiCtrlRecTextT instance at %s>" % (self.this,)
    __swig_setmethods__["MaxChars"] = lib_ohpi.SaHpiCtrlRecTextT_MaxChars_set
    __swig_getmethods__["MaxChars"] = lib_ohpi.SaHpiCtrlRecTextT_MaxChars_get
    if _newclass:MaxChars = property(lib_ohpi.SaHpiCtrlRecTextT_MaxChars_get, lib_ohpi.SaHpiCtrlRecTextT_MaxChars_set)
    __swig_setmethods__["MaxLines"] = lib_ohpi.SaHpiCtrlRecTextT_MaxLines_set
    __swig_getmethods__["MaxLines"] = lib_ohpi.SaHpiCtrlRecTextT_MaxLines_get
    if _newclass:MaxLines = property(lib_ohpi.SaHpiCtrlRecTextT_MaxLines_get, lib_ohpi.SaHpiCtrlRecTextT_MaxLines_set)
    __swig_setmethods__["Language"] = lib_ohpi.SaHpiCtrlRecTextT_Language_set
    __swig_getmethods__["Language"] = lib_ohpi.SaHpiCtrlRecTextT_Language_get
    if _newclass:Language = property(lib_ohpi.SaHpiCtrlRecTextT_Language_get, lib_ohpi.SaHpiCtrlRecTextT_Language_set)
    __swig_setmethods__["DataType"] = lib_ohpi.SaHpiCtrlRecTextT_DataType_set
    __swig_getmethods__["DataType"] = lib_ohpi.SaHpiCtrlRecTextT_DataType_get
    if _newclass:DataType = property(lib_ohpi.SaHpiCtrlRecTextT_DataType_get, lib_ohpi.SaHpiCtrlRecTextT_DataType_set)
    __swig_setmethods__["Default"] = lib_ohpi.SaHpiCtrlRecTextT_Default_set
    __swig_getmethods__["Default"] = lib_ohpi.SaHpiCtrlRecTextT_Default_get
    if _newclass:Default = property(lib_ohpi.SaHpiCtrlRecTextT_Default_get, lib_ohpi.SaHpiCtrlRecTextT_Default_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiCtrlRecTextT, 'this', lib_ohpi.new_SaHpiCtrlRecTextT(*args))
        _swig_setattr(self, SaHpiCtrlRecTextT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiCtrlRecTextT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiCtrlRecTextTPtr(SaHpiCtrlRecTextT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiCtrlRecTextT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiCtrlRecTextT, 'thisown', 0)
        _swig_setattr(self, SaHpiCtrlRecTextT,self.__class__,SaHpiCtrlRecTextT)
lib_ohpi.SaHpiCtrlRecTextT_swigregister(SaHpiCtrlRecTextTPtr)

SAHPI_CTRL_OEM_CONFIG_LENGTH = lib_ohpi.SAHPI_CTRL_OEM_CONFIG_LENGTH
class SaHpiCtrlRecOemT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiCtrlRecOemT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiCtrlRecOemT, name)
    def __repr__(self):
        return "<C SaHpiCtrlRecOemT instance at %s>" % (self.this,)
    __swig_setmethods__["MId"] = lib_ohpi.SaHpiCtrlRecOemT_MId_set
    __swig_getmethods__["MId"] = lib_ohpi.SaHpiCtrlRecOemT_MId_get
    if _newclass:MId = property(lib_ohpi.SaHpiCtrlRecOemT_MId_get, lib_ohpi.SaHpiCtrlRecOemT_MId_set)
    __swig_setmethods__["ConfigData"] = lib_ohpi.SaHpiCtrlRecOemT_ConfigData_set
    __swig_getmethods__["ConfigData"] = lib_ohpi.SaHpiCtrlRecOemT_ConfigData_get
    if _newclass:ConfigData = property(lib_ohpi.SaHpiCtrlRecOemT_ConfigData_get, lib_ohpi.SaHpiCtrlRecOemT_ConfigData_set)
    __swig_setmethods__["Default"] = lib_ohpi.SaHpiCtrlRecOemT_Default_set
    __swig_getmethods__["Default"] = lib_ohpi.SaHpiCtrlRecOemT_Default_get
    if _newclass:Default = property(lib_ohpi.SaHpiCtrlRecOemT_Default_get, lib_ohpi.SaHpiCtrlRecOemT_Default_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiCtrlRecOemT, 'this', lib_ohpi.new_SaHpiCtrlRecOemT(*args))
        _swig_setattr(self, SaHpiCtrlRecOemT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiCtrlRecOemT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiCtrlRecOemTPtr(SaHpiCtrlRecOemT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiCtrlRecOemT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiCtrlRecOemT, 'thisown', 0)
        _swig_setattr(self, SaHpiCtrlRecOemT,self.__class__,SaHpiCtrlRecOemT)
lib_ohpi.SaHpiCtrlRecOemT_swigregister(SaHpiCtrlRecOemTPtr)

class SaHpiCtrlRecUnionT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiCtrlRecUnionT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiCtrlRecUnionT, name)
    def __repr__(self):
        return "<C SaHpiCtrlRecUnionT instance at %s>" % (self.this,)
    __swig_setmethods__["Digital"] = lib_ohpi.SaHpiCtrlRecUnionT_Digital_set
    __swig_getmethods__["Digital"] = lib_ohpi.SaHpiCtrlRecUnionT_Digital_get
    if _newclass:Digital = property(lib_ohpi.SaHpiCtrlRecUnionT_Digital_get, lib_ohpi.SaHpiCtrlRecUnionT_Digital_set)
    __swig_setmethods__["Discrete"] = lib_ohpi.SaHpiCtrlRecUnionT_Discrete_set
    __swig_getmethods__["Discrete"] = lib_ohpi.SaHpiCtrlRecUnionT_Discrete_get
    if _newclass:Discrete = property(lib_ohpi.SaHpiCtrlRecUnionT_Discrete_get, lib_ohpi.SaHpiCtrlRecUnionT_Discrete_set)
    __swig_setmethods__["Analog"] = lib_ohpi.SaHpiCtrlRecUnionT_Analog_set
    __swig_getmethods__["Analog"] = lib_ohpi.SaHpiCtrlRecUnionT_Analog_get
    if _newclass:Analog = property(lib_ohpi.SaHpiCtrlRecUnionT_Analog_get, lib_ohpi.SaHpiCtrlRecUnionT_Analog_set)
    __swig_setmethods__["Stream"] = lib_ohpi.SaHpiCtrlRecUnionT_Stream_set
    __swig_getmethods__["Stream"] = lib_ohpi.SaHpiCtrlRecUnionT_Stream_get
    if _newclass:Stream = property(lib_ohpi.SaHpiCtrlRecUnionT_Stream_get, lib_ohpi.SaHpiCtrlRecUnionT_Stream_set)
    __swig_setmethods__["Text"] = lib_ohpi.SaHpiCtrlRecUnionT_Text_set
    __swig_getmethods__["Text"] = lib_ohpi.SaHpiCtrlRecUnionT_Text_get
    if _newclass:Text = property(lib_ohpi.SaHpiCtrlRecUnionT_Text_get, lib_ohpi.SaHpiCtrlRecUnionT_Text_set)
    __swig_setmethods__["Oem"] = lib_ohpi.SaHpiCtrlRecUnionT_Oem_set
    __swig_getmethods__["Oem"] = lib_ohpi.SaHpiCtrlRecUnionT_Oem_get
    if _newclass:Oem = property(lib_ohpi.SaHpiCtrlRecUnionT_Oem_get, lib_ohpi.SaHpiCtrlRecUnionT_Oem_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiCtrlRecUnionT, 'this', lib_ohpi.new_SaHpiCtrlRecUnionT(*args))
        _swig_setattr(self, SaHpiCtrlRecUnionT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiCtrlRecUnionT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiCtrlRecUnionTPtr(SaHpiCtrlRecUnionT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiCtrlRecUnionT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiCtrlRecUnionT, 'thisown', 0)
        _swig_setattr(self, SaHpiCtrlRecUnionT,self.__class__,SaHpiCtrlRecUnionT)
lib_ohpi.SaHpiCtrlRecUnionT_swigregister(SaHpiCtrlRecUnionTPtr)

class SaHpiCtrlDefaultModeT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiCtrlDefaultModeT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiCtrlDefaultModeT, name)
    def __repr__(self):
        return "<C SaHpiCtrlDefaultModeT instance at %s>" % (self.this,)
    __swig_setmethods__["Mode"] = lib_ohpi.SaHpiCtrlDefaultModeT_Mode_set
    __swig_getmethods__["Mode"] = lib_ohpi.SaHpiCtrlDefaultModeT_Mode_get
    if _newclass:Mode = property(lib_ohpi.SaHpiCtrlDefaultModeT_Mode_get, lib_ohpi.SaHpiCtrlDefaultModeT_Mode_set)
    __swig_setmethods__["ReadOnly"] = lib_ohpi.SaHpiCtrlDefaultModeT_ReadOnly_set
    __swig_getmethods__["ReadOnly"] = lib_ohpi.SaHpiCtrlDefaultModeT_ReadOnly_get
    if _newclass:ReadOnly = property(lib_ohpi.SaHpiCtrlDefaultModeT_ReadOnly_get, lib_ohpi.SaHpiCtrlDefaultModeT_ReadOnly_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiCtrlDefaultModeT, 'this', lib_ohpi.new_SaHpiCtrlDefaultModeT(*args))
        _swig_setattr(self, SaHpiCtrlDefaultModeT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiCtrlDefaultModeT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiCtrlDefaultModeTPtr(SaHpiCtrlDefaultModeT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiCtrlDefaultModeT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiCtrlDefaultModeT, 'thisown', 0)
        _swig_setattr(self, SaHpiCtrlDefaultModeT,self.__class__,SaHpiCtrlDefaultModeT)
lib_ohpi.SaHpiCtrlDefaultModeT_swigregister(SaHpiCtrlDefaultModeTPtr)

class SaHpiCtrlRecT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiCtrlRecT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiCtrlRecT, name)
    def __repr__(self):
        return "<C SaHpiCtrlRecT instance at %s>" % (self.this,)
    __swig_setmethods__["Num"] = lib_ohpi.SaHpiCtrlRecT_Num_set
    __swig_getmethods__["Num"] = lib_ohpi.SaHpiCtrlRecT_Num_get
    if _newclass:Num = property(lib_ohpi.SaHpiCtrlRecT_Num_get, lib_ohpi.SaHpiCtrlRecT_Num_set)
    __swig_setmethods__["OutputType"] = lib_ohpi.SaHpiCtrlRecT_OutputType_set
    __swig_getmethods__["OutputType"] = lib_ohpi.SaHpiCtrlRecT_OutputType_get
    if _newclass:OutputType = property(lib_ohpi.SaHpiCtrlRecT_OutputType_get, lib_ohpi.SaHpiCtrlRecT_OutputType_set)
    __swig_setmethods__["Type"] = lib_ohpi.SaHpiCtrlRecT_Type_set
    __swig_getmethods__["Type"] = lib_ohpi.SaHpiCtrlRecT_Type_get
    if _newclass:Type = property(lib_ohpi.SaHpiCtrlRecT_Type_get, lib_ohpi.SaHpiCtrlRecT_Type_set)
    __swig_setmethods__["TypeUnion"] = lib_ohpi.SaHpiCtrlRecT_TypeUnion_set
    __swig_getmethods__["TypeUnion"] = lib_ohpi.SaHpiCtrlRecT_TypeUnion_get
    if _newclass:TypeUnion = property(lib_ohpi.SaHpiCtrlRecT_TypeUnion_get, lib_ohpi.SaHpiCtrlRecT_TypeUnion_set)
    __swig_setmethods__["DefaultMode"] = lib_ohpi.SaHpiCtrlRecT_DefaultMode_set
    __swig_getmethods__["DefaultMode"] = lib_ohpi.SaHpiCtrlRecT_DefaultMode_get
    if _newclass:DefaultMode = property(lib_ohpi.SaHpiCtrlRecT_DefaultMode_get, lib_ohpi.SaHpiCtrlRecT_DefaultMode_set)
    __swig_setmethods__["WriteOnly"] = lib_ohpi.SaHpiCtrlRecT_WriteOnly_set
    __swig_getmethods__["WriteOnly"] = lib_ohpi.SaHpiCtrlRecT_WriteOnly_get
    if _newclass:WriteOnly = property(lib_ohpi.SaHpiCtrlRecT_WriteOnly_get, lib_ohpi.SaHpiCtrlRecT_WriteOnly_set)
    __swig_setmethods__["Oem"] = lib_ohpi.SaHpiCtrlRecT_Oem_set
    __swig_getmethods__["Oem"] = lib_ohpi.SaHpiCtrlRecT_Oem_get
    if _newclass:Oem = property(lib_ohpi.SaHpiCtrlRecT_Oem_get, lib_ohpi.SaHpiCtrlRecT_Oem_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiCtrlRecT, 'this', lib_ohpi.new_SaHpiCtrlRecT(*args))
        _swig_setattr(self, SaHpiCtrlRecT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiCtrlRecT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiCtrlRecTPtr(SaHpiCtrlRecT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiCtrlRecT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiCtrlRecT, 'thisown', 0)
        _swig_setattr(self, SaHpiCtrlRecT,self.__class__,SaHpiCtrlRecT)
lib_ohpi.SaHpiCtrlRecT_swigregister(SaHpiCtrlRecTPtr)

SAHPI_DEFAULT_INVENTORY_ID = lib_ohpi.SAHPI_DEFAULT_INVENTORY_ID
SAHPI_IDR_AREATYPE_INTERNAL_USE = lib_ohpi.SAHPI_IDR_AREATYPE_INTERNAL_USE
SAHPI_IDR_AREATYPE_CHASSIS_INFO = lib_ohpi.SAHPI_IDR_AREATYPE_CHASSIS_INFO
SAHPI_IDR_AREATYPE_BOARD_INFO = lib_ohpi.SAHPI_IDR_AREATYPE_BOARD_INFO
SAHPI_IDR_AREATYPE_PRODUCT_INFO = lib_ohpi.SAHPI_IDR_AREATYPE_PRODUCT_INFO
SAHPI_IDR_AREATYPE_OEM = lib_ohpi.SAHPI_IDR_AREATYPE_OEM
SAHPI_IDR_AREATYPE_UNSPECIFIED = lib_ohpi.SAHPI_IDR_AREATYPE_UNSPECIFIED
SAHPI_IDR_FIELDTYPE_CHASSIS_TYPE = lib_ohpi.SAHPI_IDR_FIELDTYPE_CHASSIS_TYPE
SAHPI_IDR_FIELDTYPE_MFG_DATETIME = lib_ohpi.SAHPI_IDR_FIELDTYPE_MFG_DATETIME
SAHPI_IDR_FIELDTYPE_MANUFACTURER = lib_ohpi.SAHPI_IDR_FIELDTYPE_MANUFACTURER
SAHPI_IDR_FIELDTYPE_PRODUCT_NAME = lib_ohpi.SAHPI_IDR_FIELDTYPE_PRODUCT_NAME
SAHPI_IDR_FIELDTYPE_PRODUCT_VERSION = lib_ohpi.SAHPI_IDR_FIELDTYPE_PRODUCT_VERSION
SAHPI_IDR_FIELDTYPE_SERIAL_NUMBER = lib_ohpi.SAHPI_IDR_FIELDTYPE_SERIAL_NUMBER
SAHPI_IDR_FIELDTYPE_PART_NUMBER = lib_ohpi.SAHPI_IDR_FIELDTYPE_PART_NUMBER
SAHPI_IDR_FIELDTYPE_FILE_ID = lib_ohpi.SAHPI_IDR_FIELDTYPE_FILE_ID
SAHPI_IDR_FIELDTYPE_ASSET_TAG = lib_ohpi.SAHPI_IDR_FIELDTYPE_ASSET_TAG
SAHPI_IDR_FIELDTYPE_CUSTOM = lib_ohpi.SAHPI_IDR_FIELDTYPE_CUSTOM
SAHPI_IDR_FIELDTYPE_UNSPECIFIED = lib_ohpi.SAHPI_IDR_FIELDTYPE_UNSPECIFIED
class SaHpiIdrFieldT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiIdrFieldT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiIdrFieldT, name)
    def __repr__(self):
        return "<C SaHpiIdrFieldT instance at %s>" % (self.this,)
    __swig_setmethods__["AreaId"] = lib_ohpi.SaHpiIdrFieldT_AreaId_set
    __swig_getmethods__["AreaId"] = lib_ohpi.SaHpiIdrFieldT_AreaId_get
    if _newclass:AreaId = property(lib_ohpi.SaHpiIdrFieldT_AreaId_get, lib_ohpi.SaHpiIdrFieldT_AreaId_set)
    __swig_setmethods__["FieldId"] = lib_ohpi.SaHpiIdrFieldT_FieldId_set
    __swig_getmethods__["FieldId"] = lib_ohpi.SaHpiIdrFieldT_FieldId_get
    if _newclass:FieldId = property(lib_ohpi.SaHpiIdrFieldT_FieldId_get, lib_ohpi.SaHpiIdrFieldT_FieldId_set)
    __swig_setmethods__["Type"] = lib_ohpi.SaHpiIdrFieldT_Type_set
    __swig_getmethods__["Type"] = lib_ohpi.SaHpiIdrFieldT_Type_get
    if _newclass:Type = property(lib_ohpi.SaHpiIdrFieldT_Type_get, lib_ohpi.SaHpiIdrFieldT_Type_set)
    __swig_setmethods__["ReadOnly"] = lib_ohpi.SaHpiIdrFieldT_ReadOnly_set
    __swig_getmethods__["ReadOnly"] = lib_ohpi.SaHpiIdrFieldT_ReadOnly_get
    if _newclass:ReadOnly = property(lib_ohpi.SaHpiIdrFieldT_ReadOnly_get, lib_ohpi.SaHpiIdrFieldT_ReadOnly_set)
    __swig_setmethods__["Field"] = lib_ohpi.SaHpiIdrFieldT_Field_set
    __swig_getmethods__["Field"] = lib_ohpi.SaHpiIdrFieldT_Field_get
    if _newclass:Field = property(lib_ohpi.SaHpiIdrFieldT_Field_get, lib_ohpi.SaHpiIdrFieldT_Field_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiIdrFieldT, 'this', lib_ohpi.new_SaHpiIdrFieldT(*args))
        _swig_setattr(self, SaHpiIdrFieldT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiIdrFieldT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiIdrFieldTPtr(SaHpiIdrFieldT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiIdrFieldT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiIdrFieldT, 'thisown', 0)
        _swig_setattr(self, SaHpiIdrFieldT,self.__class__,SaHpiIdrFieldT)
lib_ohpi.SaHpiIdrFieldT_swigregister(SaHpiIdrFieldTPtr)

class SaHpiIdrAreaHeaderT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiIdrAreaHeaderT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiIdrAreaHeaderT, name)
    def __repr__(self):
        return "<C SaHpiIdrAreaHeaderT instance at %s>" % (self.this,)
    __swig_setmethods__["AreaId"] = lib_ohpi.SaHpiIdrAreaHeaderT_AreaId_set
    __swig_getmethods__["AreaId"] = lib_ohpi.SaHpiIdrAreaHeaderT_AreaId_get
    if _newclass:AreaId = property(lib_ohpi.SaHpiIdrAreaHeaderT_AreaId_get, lib_ohpi.SaHpiIdrAreaHeaderT_AreaId_set)
    __swig_setmethods__["Type"] = lib_ohpi.SaHpiIdrAreaHeaderT_Type_set
    __swig_getmethods__["Type"] = lib_ohpi.SaHpiIdrAreaHeaderT_Type_get
    if _newclass:Type = property(lib_ohpi.SaHpiIdrAreaHeaderT_Type_get, lib_ohpi.SaHpiIdrAreaHeaderT_Type_set)
    __swig_setmethods__["ReadOnly"] = lib_ohpi.SaHpiIdrAreaHeaderT_ReadOnly_set
    __swig_getmethods__["ReadOnly"] = lib_ohpi.SaHpiIdrAreaHeaderT_ReadOnly_get
    if _newclass:ReadOnly = property(lib_ohpi.SaHpiIdrAreaHeaderT_ReadOnly_get, lib_ohpi.SaHpiIdrAreaHeaderT_ReadOnly_set)
    __swig_setmethods__["NumFields"] = lib_ohpi.SaHpiIdrAreaHeaderT_NumFields_set
    __swig_getmethods__["NumFields"] = lib_ohpi.SaHpiIdrAreaHeaderT_NumFields_get
    if _newclass:NumFields = property(lib_ohpi.SaHpiIdrAreaHeaderT_NumFields_get, lib_ohpi.SaHpiIdrAreaHeaderT_NumFields_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiIdrAreaHeaderT, 'this', lib_ohpi.new_SaHpiIdrAreaHeaderT(*args))
        _swig_setattr(self, SaHpiIdrAreaHeaderT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiIdrAreaHeaderT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiIdrAreaHeaderTPtr(SaHpiIdrAreaHeaderT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiIdrAreaHeaderT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiIdrAreaHeaderT, 'thisown', 0)
        _swig_setattr(self, SaHpiIdrAreaHeaderT,self.__class__,SaHpiIdrAreaHeaderT)
lib_ohpi.SaHpiIdrAreaHeaderT_swigregister(SaHpiIdrAreaHeaderTPtr)

class SaHpiIdrInfoT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiIdrInfoT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiIdrInfoT, name)
    def __repr__(self):
        return "<C SaHpiIdrInfoT instance at %s>" % (self.this,)
    __swig_setmethods__["IdrId"] = lib_ohpi.SaHpiIdrInfoT_IdrId_set
    __swig_getmethods__["IdrId"] = lib_ohpi.SaHpiIdrInfoT_IdrId_get
    if _newclass:IdrId = property(lib_ohpi.SaHpiIdrInfoT_IdrId_get, lib_ohpi.SaHpiIdrInfoT_IdrId_set)
    __swig_setmethods__["UpdateCount"] = lib_ohpi.SaHpiIdrInfoT_UpdateCount_set
    __swig_getmethods__["UpdateCount"] = lib_ohpi.SaHpiIdrInfoT_UpdateCount_get
    if _newclass:UpdateCount = property(lib_ohpi.SaHpiIdrInfoT_UpdateCount_get, lib_ohpi.SaHpiIdrInfoT_UpdateCount_set)
    __swig_setmethods__["ReadOnly"] = lib_ohpi.SaHpiIdrInfoT_ReadOnly_set
    __swig_getmethods__["ReadOnly"] = lib_ohpi.SaHpiIdrInfoT_ReadOnly_get
    if _newclass:ReadOnly = property(lib_ohpi.SaHpiIdrInfoT_ReadOnly_get, lib_ohpi.SaHpiIdrInfoT_ReadOnly_set)
    __swig_setmethods__["NumAreas"] = lib_ohpi.SaHpiIdrInfoT_NumAreas_set
    __swig_getmethods__["NumAreas"] = lib_ohpi.SaHpiIdrInfoT_NumAreas_get
    if _newclass:NumAreas = property(lib_ohpi.SaHpiIdrInfoT_NumAreas_get, lib_ohpi.SaHpiIdrInfoT_NumAreas_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiIdrInfoT, 'this', lib_ohpi.new_SaHpiIdrInfoT(*args))
        _swig_setattr(self, SaHpiIdrInfoT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiIdrInfoT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiIdrInfoTPtr(SaHpiIdrInfoT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiIdrInfoT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiIdrInfoT, 'thisown', 0)
        _swig_setattr(self, SaHpiIdrInfoT,self.__class__,SaHpiIdrInfoT)
lib_ohpi.SaHpiIdrInfoT_swigregister(SaHpiIdrInfoTPtr)

class SaHpiInventoryRecT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiInventoryRecT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiInventoryRecT, name)
    def __repr__(self):
        return "<C SaHpiInventoryRecT instance at %s>" % (self.this,)
    __swig_setmethods__["IdrId"] = lib_ohpi.SaHpiInventoryRecT_IdrId_set
    __swig_getmethods__["IdrId"] = lib_ohpi.SaHpiInventoryRecT_IdrId_get
    if _newclass:IdrId = property(lib_ohpi.SaHpiInventoryRecT_IdrId_get, lib_ohpi.SaHpiInventoryRecT_IdrId_set)
    __swig_setmethods__["Persistent"] = lib_ohpi.SaHpiInventoryRecT_Persistent_set
    __swig_getmethods__["Persistent"] = lib_ohpi.SaHpiInventoryRecT_Persistent_get
    if _newclass:Persistent = property(lib_ohpi.SaHpiInventoryRecT_Persistent_get, lib_ohpi.SaHpiInventoryRecT_Persistent_set)
    __swig_setmethods__["Oem"] = lib_ohpi.SaHpiInventoryRecT_Oem_set
    __swig_getmethods__["Oem"] = lib_ohpi.SaHpiInventoryRecT_Oem_get
    if _newclass:Oem = property(lib_ohpi.SaHpiInventoryRecT_Oem_get, lib_ohpi.SaHpiInventoryRecT_Oem_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiInventoryRecT, 'this', lib_ohpi.new_SaHpiInventoryRecT(*args))
        _swig_setattr(self, SaHpiInventoryRecT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiInventoryRecT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiInventoryRecTPtr(SaHpiInventoryRecT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiInventoryRecT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiInventoryRecT, 'thisown', 0)
        _swig_setattr(self, SaHpiInventoryRecT,self.__class__,SaHpiInventoryRecT)
lib_ohpi.SaHpiInventoryRecT_swigregister(SaHpiInventoryRecTPtr)

SAHPI_DEFAULT_WATCHDOG_NUM = lib_ohpi.SAHPI_DEFAULT_WATCHDOG_NUM
SAHPI_WA_NO_ACTION = lib_ohpi.SAHPI_WA_NO_ACTION
SAHPI_WA_RESET = lib_ohpi.SAHPI_WA_RESET
SAHPI_WA_POWER_DOWN = lib_ohpi.SAHPI_WA_POWER_DOWN
SAHPI_WA_POWER_CYCLE = lib_ohpi.SAHPI_WA_POWER_CYCLE
SAHPI_WAE_NO_ACTION = lib_ohpi.SAHPI_WAE_NO_ACTION
SAHPI_WAE_RESET = lib_ohpi.SAHPI_WAE_RESET
SAHPI_WAE_POWER_DOWN = lib_ohpi.SAHPI_WAE_POWER_DOWN
SAHPI_WAE_POWER_CYCLE = lib_ohpi.SAHPI_WAE_POWER_CYCLE
SAHPI_WAE_TIMER_INT = lib_ohpi.SAHPI_WAE_TIMER_INT
SAHPI_WPI_NONE = lib_ohpi.SAHPI_WPI_NONE
SAHPI_WPI_SMI = lib_ohpi.SAHPI_WPI_SMI
SAHPI_WPI_NMI = lib_ohpi.SAHPI_WPI_NMI
SAHPI_WPI_MESSAGE_INTERRUPT = lib_ohpi.SAHPI_WPI_MESSAGE_INTERRUPT
SAHPI_WPI_OEM = lib_ohpi.SAHPI_WPI_OEM
SAHPI_WTU_NONE = lib_ohpi.SAHPI_WTU_NONE
SAHPI_WTU_BIOS_FRB2 = lib_ohpi.SAHPI_WTU_BIOS_FRB2
SAHPI_WTU_BIOS_POST = lib_ohpi.SAHPI_WTU_BIOS_POST
SAHPI_WTU_OS_LOAD = lib_ohpi.SAHPI_WTU_OS_LOAD
SAHPI_WTU_SMS_OS = lib_ohpi.SAHPI_WTU_SMS_OS
SAHPI_WTU_OEM = lib_ohpi.SAHPI_WTU_OEM
SAHPI_WTU_UNSPECIFIED = lib_ohpi.SAHPI_WTU_UNSPECIFIED
SAHPI_WATCHDOG_EXP_BIOS_FRB2 = lib_ohpi.SAHPI_WATCHDOG_EXP_BIOS_FRB2
SAHPI_WATCHDOG_EXP_BIOS_POST = lib_ohpi.SAHPI_WATCHDOG_EXP_BIOS_POST
SAHPI_WATCHDOG_EXP_OS_LOAD = lib_ohpi.SAHPI_WATCHDOG_EXP_OS_LOAD
SAHPI_WATCHDOG_EXP_SMS_OS = lib_ohpi.SAHPI_WATCHDOG_EXP_SMS_OS
SAHPI_WATCHDOG_EXP_OEM = lib_ohpi.SAHPI_WATCHDOG_EXP_OEM
class SaHpiWatchdogT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiWatchdogT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiWatchdogT, name)
    def __repr__(self):
        return "<C SaHpiWatchdogT instance at %s>" % (self.this,)
    __swig_setmethods__["Log"] = lib_ohpi.SaHpiWatchdogT_Log_set
    __swig_getmethods__["Log"] = lib_ohpi.SaHpiWatchdogT_Log_get
    if _newclass:Log = property(lib_ohpi.SaHpiWatchdogT_Log_get, lib_ohpi.SaHpiWatchdogT_Log_set)
    __swig_setmethods__["Running"] = lib_ohpi.SaHpiWatchdogT_Running_set
    __swig_getmethods__["Running"] = lib_ohpi.SaHpiWatchdogT_Running_get
    if _newclass:Running = property(lib_ohpi.SaHpiWatchdogT_Running_get, lib_ohpi.SaHpiWatchdogT_Running_set)
    __swig_setmethods__["TimerUse"] = lib_ohpi.SaHpiWatchdogT_TimerUse_set
    __swig_getmethods__["TimerUse"] = lib_ohpi.SaHpiWatchdogT_TimerUse_get
    if _newclass:TimerUse = property(lib_ohpi.SaHpiWatchdogT_TimerUse_get, lib_ohpi.SaHpiWatchdogT_TimerUse_set)
    __swig_setmethods__["TimerAction"] = lib_ohpi.SaHpiWatchdogT_TimerAction_set
    __swig_getmethods__["TimerAction"] = lib_ohpi.SaHpiWatchdogT_TimerAction_get
    if _newclass:TimerAction = property(lib_ohpi.SaHpiWatchdogT_TimerAction_get, lib_ohpi.SaHpiWatchdogT_TimerAction_set)
    __swig_setmethods__["PretimerInterrupt"] = lib_ohpi.SaHpiWatchdogT_PretimerInterrupt_set
    __swig_getmethods__["PretimerInterrupt"] = lib_ohpi.SaHpiWatchdogT_PretimerInterrupt_get
    if _newclass:PretimerInterrupt = property(lib_ohpi.SaHpiWatchdogT_PretimerInterrupt_get, lib_ohpi.SaHpiWatchdogT_PretimerInterrupt_set)
    __swig_setmethods__["PreTimeoutInterval"] = lib_ohpi.SaHpiWatchdogT_PreTimeoutInterval_set
    __swig_getmethods__["PreTimeoutInterval"] = lib_ohpi.SaHpiWatchdogT_PreTimeoutInterval_get
    if _newclass:PreTimeoutInterval = property(lib_ohpi.SaHpiWatchdogT_PreTimeoutInterval_get, lib_ohpi.SaHpiWatchdogT_PreTimeoutInterval_set)
    __swig_setmethods__["TimerUseExpFlags"] = lib_ohpi.SaHpiWatchdogT_TimerUseExpFlags_set
    __swig_getmethods__["TimerUseExpFlags"] = lib_ohpi.SaHpiWatchdogT_TimerUseExpFlags_get
    if _newclass:TimerUseExpFlags = property(lib_ohpi.SaHpiWatchdogT_TimerUseExpFlags_get, lib_ohpi.SaHpiWatchdogT_TimerUseExpFlags_set)
    __swig_setmethods__["InitialCount"] = lib_ohpi.SaHpiWatchdogT_InitialCount_set
    __swig_getmethods__["InitialCount"] = lib_ohpi.SaHpiWatchdogT_InitialCount_get
    if _newclass:InitialCount = property(lib_ohpi.SaHpiWatchdogT_InitialCount_get, lib_ohpi.SaHpiWatchdogT_InitialCount_set)
    __swig_setmethods__["PresentCount"] = lib_ohpi.SaHpiWatchdogT_PresentCount_set
    __swig_getmethods__["PresentCount"] = lib_ohpi.SaHpiWatchdogT_PresentCount_get
    if _newclass:PresentCount = property(lib_ohpi.SaHpiWatchdogT_PresentCount_get, lib_ohpi.SaHpiWatchdogT_PresentCount_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiWatchdogT, 'this', lib_ohpi.new_SaHpiWatchdogT(*args))
        _swig_setattr(self, SaHpiWatchdogT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiWatchdogT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiWatchdogTPtr(SaHpiWatchdogT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiWatchdogT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiWatchdogT, 'thisown', 0)
        _swig_setattr(self, SaHpiWatchdogT,self.__class__,SaHpiWatchdogT)
lib_ohpi.SaHpiWatchdogT_swigregister(SaHpiWatchdogTPtr)

class SaHpiWatchdogRecT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiWatchdogRecT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiWatchdogRecT, name)
    def __repr__(self):
        return "<C SaHpiWatchdogRecT instance at %s>" % (self.this,)
    __swig_setmethods__["WatchdogNum"] = lib_ohpi.SaHpiWatchdogRecT_WatchdogNum_set
    __swig_getmethods__["WatchdogNum"] = lib_ohpi.SaHpiWatchdogRecT_WatchdogNum_get
    if _newclass:WatchdogNum = property(lib_ohpi.SaHpiWatchdogRecT_WatchdogNum_get, lib_ohpi.SaHpiWatchdogRecT_WatchdogNum_set)
    __swig_setmethods__["Oem"] = lib_ohpi.SaHpiWatchdogRecT_Oem_set
    __swig_getmethods__["Oem"] = lib_ohpi.SaHpiWatchdogRecT_Oem_get
    if _newclass:Oem = property(lib_ohpi.SaHpiWatchdogRecT_Oem_get, lib_ohpi.SaHpiWatchdogRecT_Oem_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiWatchdogRecT, 'this', lib_ohpi.new_SaHpiWatchdogRecT(*args))
        _swig_setattr(self, SaHpiWatchdogRecT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiWatchdogRecT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiWatchdogRecTPtr(SaHpiWatchdogRecT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiWatchdogRecT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiWatchdogRecT, 'thisown', 0)
        _swig_setattr(self, SaHpiWatchdogRecT,self.__class__,SaHpiWatchdogRecT)
lib_ohpi.SaHpiWatchdogRecT_swigregister(SaHpiWatchdogRecTPtr)

SAHPI_HS_INDICATOR_OFF = lib_ohpi.SAHPI_HS_INDICATOR_OFF
SAHPI_HS_INDICATOR_ON = lib_ohpi.SAHPI_HS_INDICATOR_ON
SAHPI_HS_ACTION_INSERTION = lib_ohpi.SAHPI_HS_ACTION_INSERTION
SAHPI_HS_ACTION_EXTRACTION = lib_ohpi.SAHPI_HS_ACTION_EXTRACTION
SAHPI_HS_STATE_INACTIVE = lib_ohpi.SAHPI_HS_STATE_INACTIVE
SAHPI_HS_STATE_INSERTION_PENDING = lib_ohpi.SAHPI_HS_STATE_INSERTION_PENDING
SAHPI_HS_STATE_ACTIVE = lib_ohpi.SAHPI_HS_STATE_ACTIVE
SAHPI_HS_STATE_EXTRACTION_PENDING = lib_ohpi.SAHPI_HS_STATE_EXTRACTION_PENDING
SAHPI_HS_STATE_NOT_PRESENT = lib_ohpi.SAHPI_HS_STATE_NOT_PRESENT
SAHPI_CRITICAL = lib_ohpi.SAHPI_CRITICAL
SAHPI_MAJOR = lib_ohpi.SAHPI_MAJOR
SAHPI_MINOR = lib_ohpi.SAHPI_MINOR
SAHPI_INFORMATIONAL = lib_ohpi.SAHPI_INFORMATIONAL
SAHPI_OK = lib_ohpi.SAHPI_OK
SAHPI_DEBUG = lib_ohpi.SAHPI_DEBUG
SAHPI_ALL_SEVERITIES = lib_ohpi.SAHPI_ALL_SEVERITIES
SAHPI_RESE_RESOURCE_FAILURE = lib_ohpi.SAHPI_RESE_RESOURCE_FAILURE
SAHPI_RESE_RESOURCE_RESTORED = lib_ohpi.SAHPI_RESE_RESOURCE_RESTORED
SAHPI_RESE_RESOURCE_ADDED = lib_ohpi.SAHPI_RESE_RESOURCE_ADDED
class SaHpiResourceEventT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiResourceEventT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiResourceEventT, name)
    def __repr__(self):
        return "<C SaHpiResourceEventT instance at %s>" % (self.this,)
    __swig_setmethods__["ResourceEventType"] = lib_ohpi.SaHpiResourceEventT_ResourceEventType_set
    __swig_getmethods__["ResourceEventType"] = lib_ohpi.SaHpiResourceEventT_ResourceEventType_get
    if _newclass:ResourceEventType = property(lib_ohpi.SaHpiResourceEventT_ResourceEventType_get, lib_ohpi.SaHpiResourceEventT_ResourceEventType_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiResourceEventT, 'this', lib_ohpi.new_SaHpiResourceEventT(*args))
        _swig_setattr(self, SaHpiResourceEventT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiResourceEventT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiResourceEventTPtr(SaHpiResourceEventT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiResourceEventT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiResourceEventT, 'thisown', 0)
        _swig_setattr(self, SaHpiResourceEventT,self.__class__,SaHpiResourceEventT)
lib_ohpi.SaHpiResourceEventT_swigregister(SaHpiResourceEventTPtr)

SAHPI_DOMAIN_REF_ADDED = lib_ohpi.SAHPI_DOMAIN_REF_ADDED
SAHPI_DOMAIN_REF_REMOVED = lib_ohpi.SAHPI_DOMAIN_REF_REMOVED
class SaHpiDomainEventT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiDomainEventT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiDomainEventT, name)
    def __repr__(self):
        return "<C SaHpiDomainEventT instance at %s>" % (self.this,)
    __swig_setmethods__["Type"] = lib_ohpi.SaHpiDomainEventT_Type_set
    __swig_getmethods__["Type"] = lib_ohpi.SaHpiDomainEventT_Type_get
    if _newclass:Type = property(lib_ohpi.SaHpiDomainEventT_Type_get, lib_ohpi.SaHpiDomainEventT_Type_set)
    __swig_setmethods__["DomainId"] = lib_ohpi.SaHpiDomainEventT_DomainId_set
    __swig_getmethods__["DomainId"] = lib_ohpi.SaHpiDomainEventT_DomainId_get
    if _newclass:DomainId = property(lib_ohpi.SaHpiDomainEventT_DomainId_get, lib_ohpi.SaHpiDomainEventT_DomainId_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiDomainEventT, 'this', lib_ohpi.new_SaHpiDomainEventT(*args))
        _swig_setattr(self, SaHpiDomainEventT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiDomainEventT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiDomainEventTPtr(SaHpiDomainEventT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiDomainEventT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiDomainEventT, 'thisown', 0)
        _swig_setattr(self, SaHpiDomainEventT,self.__class__,SaHpiDomainEventT)
lib_ohpi.SaHpiDomainEventT_swigregister(SaHpiDomainEventTPtr)

SAHPI_SOD_TRIGGER_READING = lib_ohpi.SAHPI_SOD_TRIGGER_READING
SAHPI_SOD_TRIGGER_THRESHOLD = lib_ohpi.SAHPI_SOD_TRIGGER_THRESHOLD
SAHPI_SOD_OEM = lib_ohpi.SAHPI_SOD_OEM
SAHPI_SOD_PREVIOUS_STATE = lib_ohpi.SAHPI_SOD_PREVIOUS_STATE
SAHPI_SOD_CURRENT_STATE = lib_ohpi.SAHPI_SOD_CURRENT_STATE
SAHPI_SOD_SENSOR_SPECIFIC = lib_ohpi.SAHPI_SOD_SENSOR_SPECIFIC
class SaHpiSensorEventT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiSensorEventT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiSensorEventT, name)
    def __repr__(self):
        return "<C SaHpiSensorEventT instance at %s>" % (self.this,)
    __swig_setmethods__["SensorNum"] = lib_ohpi.SaHpiSensorEventT_SensorNum_set
    __swig_getmethods__["SensorNum"] = lib_ohpi.SaHpiSensorEventT_SensorNum_get
    if _newclass:SensorNum = property(lib_ohpi.SaHpiSensorEventT_SensorNum_get, lib_ohpi.SaHpiSensorEventT_SensorNum_set)
    __swig_setmethods__["SensorType"] = lib_ohpi.SaHpiSensorEventT_SensorType_set
    __swig_getmethods__["SensorType"] = lib_ohpi.SaHpiSensorEventT_SensorType_get
    if _newclass:SensorType = property(lib_ohpi.SaHpiSensorEventT_SensorType_get, lib_ohpi.SaHpiSensorEventT_SensorType_set)
    __swig_setmethods__["EventCategory"] = lib_ohpi.SaHpiSensorEventT_EventCategory_set
    __swig_getmethods__["EventCategory"] = lib_ohpi.SaHpiSensorEventT_EventCategory_get
    if _newclass:EventCategory = property(lib_ohpi.SaHpiSensorEventT_EventCategory_get, lib_ohpi.SaHpiSensorEventT_EventCategory_set)
    __swig_setmethods__["Assertion"] = lib_ohpi.SaHpiSensorEventT_Assertion_set
    __swig_getmethods__["Assertion"] = lib_ohpi.SaHpiSensorEventT_Assertion_get
    if _newclass:Assertion = property(lib_ohpi.SaHpiSensorEventT_Assertion_get, lib_ohpi.SaHpiSensorEventT_Assertion_set)
    __swig_setmethods__["EventState"] = lib_ohpi.SaHpiSensorEventT_EventState_set
    __swig_getmethods__["EventState"] = lib_ohpi.SaHpiSensorEventT_EventState_get
    if _newclass:EventState = property(lib_ohpi.SaHpiSensorEventT_EventState_get, lib_ohpi.SaHpiSensorEventT_EventState_set)
    __swig_setmethods__["OptionalDataPresent"] = lib_ohpi.SaHpiSensorEventT_OptionalDataPresent_set
    __swig_getmethods__["OptionalDataPresent"] = lib_ohpi.SaHpiSensorEventT_OptionalDataPresent_get
    if _newclass:OptionalDataPresent = property(lib_ohpi.SaHpiSensorEventT_OptionalDataPresent_get, lib_ohpi.SaHpiSensorEventT_OptionalDataPresent_set)
    __swig_setmethods__["TriggerReading"] = lib_ohpi.SaHpiSensorEventT_TriggerReading_set
    __swig_getmethods__["TriggerReading"] = lib_ohpi.SaHpiSensorEventT_TriggerReading_get
    if _newclass:TriggerReading = property(lib_ohpi.SaHpiSensorEventT_TriggerReading_get, lib_ohpi.SaHpiSensorEventT_TriggerReading_set)
    __swig_setmethods__["TriggerThreshold"] = lib_ohpi.SaHpiSensorEventT_TriggerThreshold_set
    __swig_getmethods__["TriggerThreshold"] = lib_ohpi.SaHpiSensorEventT_TriggerThreshold_get
    if _newclass:TriggerThreshold = property(lib_ohpi.SaHpiSensorEventT_TriggerThreshold_get, lib_ohpi.SaHpiSensorEventT_TriggerThreshold_set)
    __swig_setmethods__["PreviousState"] = lib_ohpi.SaHpiSensorEventT_PreviousState_set
    __swig_getmethods__["PreviousState"] = lib_ohpi.SaHpiSensorEventT_PreviousState_get
    if _newclass:PreviousState = property(lib_ohpi.SaHpiSensorEventT_PreviousState_get, lib_ohpi.SaHpiSensorEventT_PreviousState_set)
    __swig_setmethods__["CurrentState"] = lib_ohpi.SaHpiSensorEventT_CurrentState_set
    __swig_getmethods__["CurrentState"] = lib_ohpi.SaHpiSensorEventT_CurrentState_get
    if _newclass:CurrentState = property(lib_ohpi.SaHpiSensorEventT_CurrentState_get, lib_ohpi.SaHpiSensorEventT_CurrentState_set)
    __swig_setmethods__["Oem"] = lib_ohpi.SaHpiSensorEventT_Oem_set
    __swig_getmethods__["Oem"] = lib_ohpi.SaHpiSensorEventT_Oem_get
    if _newclass:Oem = property(lib_ohpi.SaHpiSensorEventT_Oem_get, lib_ohpi.SaHpiSensorEventT_Oem_set)
    __swig_setmethods__["SensorSpecific"] = lib_ohpi.SaHpiSensorEventT_SensorSpecific_set
    __swig_getmethods__["SensorSpecific"] = lib_ohpi.SaHpiSensorEventT_SensorSpecific_get
    if _newclass:SensorSpecific = property(lib_ohpi.SaHpiSensorEventT_SensorSpecific_get, lib_ohpi.SaHpiSensorEventT_SensorSpecific_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiSensorEventT, 'this', lib_ohpi.new_SaHpiSensorEventT(*args))
        _swig_setattr(self, SaHpiSensorEventT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiSensorEventT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiSensorEventTPtr(SaHpiSensorEventT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiSensorEventT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiSensorEventT, 'thisown', 0)
        _swig_setattr(self, SaHpiSensorEventT,self.__class__,SaHpiSensorEventT)
lib_ohpi.SaHpiSensorEventT_swigregister(SaHpiSensorEventTPtr)

SAHPI_SEOD_CURRENT_STATE = lib_ohpi.SAHPI_SEOD_CURRENT_STATE
class SaHpiSensorEnableChangeEventT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiSensorEnableChangeEventT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiSensorEnableChangeEventT, name)
    def __repr__(self):
        return "<C SaHpiSensorEnableChangeEventT instance at %s>" % (self.this,)
    __swig_setmethods__["SensorNum"] = lib_ohpi.SaHpiSensorEnableChangeEventT_SensorNum_set
    __swig_getmethods__["SensorNum"] = lib_ohpi.SaHpiSensorEnableChangeEventT_SensorNum_get
    if _newclass:SensorNum = property(lib_ohpi.SaHpiSensorEnableChangeEventT_SensorNum_get, lib_ohpi.SaHpiSensorEnableChangeEventT_SensorNum_set)
    __swig_setmethods__["SensorType"] = lib_ohpi.SaHpiSensorEnableChangeEventT_SensorType_set
    __swig_getmethods__["SensorType"] = lib_ohpi.SaHpiSensorEnableChangeEventT_SensorType_get
    if _newclass:SensorType = property(lib_ohpi.SaHpiSensorEnableChangeEventT_SensorType_get, lib_ohpi.SaHpiSensorEnableChangeEventT_SensorType_set)
    __swig_setmethods__["EventCategory"] = lib_ohpi.SaHpiSensorEnableChangeEventT_EventCategory_set
    __swig_getmethods__["EventCategory"] = lib_ohpi.SaHpiSensorEnableChangeEventT_EventCategory_get
    if _newclass:EventCategory = property(lib_ohpi.SaHpiSensorEnableChangeEventT_EventCategory_get, lib_ohpi.SaHpiSensorEnableChangeEventT_EventCategory_set)
    __swig_setmethods__["SensorEnable"] = lib_ohpi.SaHpiSensorEnableChangeEventT_SensorEnable_set
    __swig_getmethods__["SensorEnable"] = lib_ohpi.SaHpiSensorEnableChangeEventT_SensorEnable_get
    if _newclass:SensorEnable = property(lib_ohpi.SaHpiSensorEnableChangeEventT_SensorEnable_get, lib_ohpi.SaHpiSensorEnableChangeEventT_SensorEnable_set)
    __swig_setmethods__["SensorEventEnable"] = lib_ohpi.SaHpiSensorEnableChangeEventT_SensorEventEnable_set
    __swig_getmethods__["SensorEventEnable"] = lib_ohpi.SaHpiSensorEnableChangeEventT_SensorEventEnable_get
    if _newclass:SensorEventEnable = property(lib_ohpi.SaHpiSensorEnableChangeEventT_SensorEventEnable_get, lib_ohpi.SaHpiSensorEnableChangeEventT_SensorEventEnable_set)
    __swig_setmethods__["AssertEventMask"] = lib_ohpi.SaHpiSensorEnableChangeEventT_AssertEventMask_set
    __swig_getmethods__["AssertEventMask"] = lib_ohpi.SaHpiSensorEnableChangeEventT_AssertEventMask_get
    if _newclass:AssertEventMask = property(lib_ohpi.SaHpiSensorEnableChangeEventT_AssertEventMask_get, lib_ohpi.SaHpiSensorEnableChangeEventT_AssertEventMask_set)
    __swig_setmethods__["DeassertEventMask"] = lib_ohpi.SaHpiSensorEnableChangeEventT_DeassertEventMask_set
    __swig_getmethods__["DeassertEventMask"] = lib_ohpi.SaHpiSensorEnableChangeEventT_DeassertEventMask_get
    if _newclass:DeassertEventMask = property(lib_ohpi.SaHpiSensorEnableChangeEventT_DeassertEventMask_get, lib_ohpi.SaHpiSensorEnableChangeEventT_DeassertEventMask_set)
    __swig_setmethods__["OptionalDataPresent"] = lib_ohpi.SaHpiSensorEnableChangeEventT_OptionalDataPresent_set
    __swig_getmethods__["OptionalDataPresent"] = lib_ohpi.SaHpiSensorEnableChangeEventT_OptionalDataPresent_get
    if _newclass:OptionalDataPresent = property(lib_ohpi.SaHpiSensorEnableChangeEventT_OptionalDataPresent_get, lib_ohpi.SaHpiSensorEnableChangeEventT_OptionalDataPresent_set)
    __swig_setmethods__["CurrentState"] = lib_ohpi.SaHpiSensorEnableChangeEventT_CurrentState_set
    __swig_getmethods__["CurrentState"] = lib_ohpi.SaHpiSensorEnableChangeEventT_CurrentState_get
    if _newclass:CurrentState = property(lib_ohpi.SaHpiSensorEnableChangeEventT_CurrentState_get, lib_ohpi.SaHpiSensorEnableChangeEventT_CurrentState_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiSensorEnableChangeEventT, 'this', lib_ohpi.new_SaHpiSensorEnableChangeEventT(*args))
        _swig_setattr(self, SaHpiSensorEnableChangeEventT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiSensorEnableChangeEventT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiSensorEnableChangeEventTPtr(SaHpiSensorEnableChangeEventT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiSensorEnableChangeEventT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiSensorEnableChangeEventT, 'thisown', 0)
        _swig_setattr(self, SaHpiSensorEnableChangeEventT,self.__class__,SaHpiSensorEnableChangeEventT)
lib_ohpi.SaHpiSensorEnableChangeEventT_swigregister(SaHpiSensorEnableChangeEventTPtr)

class SaHpiHotSwapEventT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiHotSwapEventT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiHotSwapEventT, name)
    def __repr__(self):
        return "<C SaHpiHotSwapEventT instance at %s>" % (self.this,)
    __swig_setmethods__["HotSwapState"] = lib_ohpi.SaHpiHotSwapEventT_HotSwapState_set
    __swig_getmethods__["HotSwapState"] = lib_ohpi.SaHpiHotSwapEventT_HotSwapState_get
    if _newclass:HotSwapState = property(lib_ohpi.SaHpiHotSwapEventT_HotSwapState_get, lib_ohpi.SaHpiHotSwapEventT_HotSwapState_set)
    __swig_setmethods__["PreviousHotSwapState"] = lib_ohpi.SaHpiHotSwapEventT_PreviousHotSwapState_set
    __swig_getmethods__["PreviousHotSwapState"] = lib_ohpi.SaHpiHotSwapEventT_PreviousHotSwapState_get
    if _newclass:PreviousHotSwapState = property(lib_ohpi.SaHpiHotSwapEventT_PreviousHotSwapState_get, lib_ohpi.SaHpiHotSwapEventT_PreviousHotSwapState_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiHotSwapEventT, 'this', lib_ohpi.new_SaHpiHotSwapEventT(*args))
        _swig_setattr(self, SaHpiHotSwapEventT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiHotSwapEventT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiHotSwapEventTPtr(SaHpiHotSwapEventT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiHotSwapEventT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiHotSwapEventT, 'thisown', 0)
        _swig_setattr(self, SaHpiHotSwapEventT,self.__class__,SaHpiHotSwapEventT)
lib_ohpi.SaHpiHotSwapEventT_swigregister(SaHpiHotSwapEventTPtr)

class SaHpiWatchdogEventT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiWatchdogEventT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiWatchdogEventT, name)
    def __repr__(self):
        return "<C SaHpiWatchdogEventT instance at %s>" % (self.this,)
    __swig_setmethods__["WatchdogNum"] = lib_ohpi.SaHpiWatchdogEventT_WatchdogNum_set
    __swig_getmethods__["WatchdogNum"] = lib_ohpi.SaHpiWatchdogEventT_WatchdogNum_get
    if _newclass:WatchdogNum = property(lib_ohpi.SaHpiWatchdogEventT_WatchdogNum_get, lib_ohpi.SaHpiWatchdogEventT_WatchdogNum_set)
    __swig_setmethods__["WatchdogAction"] = lib_ohpi.SaHpiWatchdogEventT_WatchdogAction_set
    __swig_getmethods__["WatchdogAction"] = lib_ohpi.SaHpiWatchdogEventT_WatchdogAction_get
    if _newclass:WatchdogAction = property(lib_ohpi.SaHpiWatchdogEventT_WatchdogAction_get, lib_ohpi.SaHpiWatchdogEventT_WatchdogAction_set)
    __swig_setmethods__["WatchdogPreTimerAction"] = lib_ohpi.SaHpiWatchdogEventT_WatchdogPreTimerAction_set
    __swig_getmethods__["WatchdogPreTimerAction"] = lib_ohpi.SaHpiWatchdogEventT_WatchdogPreTimerAction_get
    if _newclass:WatchdogPreTimerAction = property(lib_ohpi.SaHpiWatchdogEventT_WatchdogPreTimerAction_get, lib_ohpi.SaHpiWatchdogEventT_WatchdogPreTimerAction_set)
    __swig_setmethods__["WatchdogUse"] = lib_ohpi.SaHpiWatchdogEventT_WatchdogUse_set
    __swig_getmethods__["WatchdogUse"] = lib_ohpi.SaHpiWatchdogEventT_WatchdogUse_get
    if _newclass:WatchdogUse = property(lib_ohpi.SaHpiWatchdogEventT_WatchdogUse_get, lib_ohpi.SaHpiWatchdogEventT_WatchdogUse_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiWatchdogEventT, 'this', lib_ohpi.new_SaHpiWatchdogEventT(*args))
        _swig_setattr(self, SaHpiWatchdogEventT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiWatchdogEventT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiWatchdogEventTPtr(SaHpiWatchdogEventT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiWatchdogEventT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiWatchdogEventT, 'thisown', 0)
        _swig_setattr(self, SaHpiWatchdogEventT,self.__class__,SaHpiWatchdogEventT)
lib_ohpi.SaHpiWatchdogEventT_swigregister(SaHpiWatchdogEventTPtr)

SAHPI_HPIE_AUDIT = lib_ohpi.SAHPI_HPIE_AUDIT
SAHPI_HPIE_STARTUP = lib_ohpi.SAHPI_HPIE_STARTUP
SAHPI_HPIE_OTHER = lib_ohpi.SAHPI_HPIE_OTHER
class SaHpiHpiSwEventT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiHpiSwEventT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiHpiSwEventT, name)
    def __repr__(self):
        return "<C SaHpiHpiSwEventT instance at %s>" % (self.this,)
    __swig_setmethods__["MId"] = lib_ohpi.SaHpiHpiSwEventT_MId_set
    __swig_getmethods__["MId"] = lib_ohpi.SaHpiHpiSwEventT_MId_get
    if _newclass:MId = property(lib_ohpi.SaHpiHpiSwEventT_MId_get, lib_ohpi.SaHpiHpiSwEventT_MId_set)
    __swig_setmethods__["Type"] = lib_ohpi.SaHpiHpiSwEventT_Type_set
    __swig_getmethods__["Type"] = lib_ohpi.SaHpiHpiSwEventT_Type_get
    if _newclass:Type = property(lib_ohpi.SaHpiHpiSwEventT_Type_get, lib_ohpi.SaHpiHpiSwEventT_Type_set)
    __swig_setmethods__["EventData"] = lib_ohpi.SaHpiHpiSwEventT_EventData_set
    __swig_getmethods__["EventData"] = lib_ohpi.SaHpiHpiSwEventT_EventData_get
    if _newclass:EventData = property(lib_ohpi.SaHpiHpiSwEventT_EventData_get, lib_ohpi.SaHpiHpiSwEventT_EventData_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiHpiSwEventT, 'this', lib_ohpi.new_SaHpiHpiSwEventT(*args))
        _swig_setattr(self, SaHpiHpiSwEventT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiHpiSwEventT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiHpiSwEventTPtr(SaHpiHpiSwEventT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiHpiSwEventT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiHpiSwEventT, 'thisown', 0)
        _swig_setattr(self, SaHpiHpiSwEventT,self.__class__,SaHpiHpiSwEventT)
lib_ohpi.SaHpiHpiSwEventT_swigregister(SaHpiHpiSwEventTPtr)

class SaHpiOemEventT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiOemEventT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiOemEventT, name)
    def __repr__(self):
        return "<C SaHpiOemEventT instance at %s>" % (self.this,)
    __swig_setmethods__["MId"] = lib_ohpi.SaHpiOemEventT_MId_set
    __swig_getmethods__["MId"] = lib_ohpi.SaHpiOemEventT_MId_get
    if _newclass:MId = property(lib_ohpi.SaHpiOemEventT_MId_get, lib_ohpi.SaHpiOemEventT_MId_set)
    __swig_setmethods__["OemEventData"] = lib_ohpi.SaHpiOemEventT_OemEventData_set
    __swig_getmethods__["OemEventData"] = lib_ohpi.SaHpiOemEventT_OemEventData_get
    if _newclass:OemEventData = property(lib_ohpi.SaHpiOemEventT_OemEventData_get, lib_ohpi.SaHpiOemEventT_OemEventData_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiOemEventT, 'this', lib_ohpi.new_SaHpiOemEventT(*args))
        _swig_setattr(self, SaHpiOemEventT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiOemEventT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiOemEventTPtr(SaHpiOemEventT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiOemEventT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiOemEventT, 'thisown', 0)
        _swig_setattr(self, SaHpiOemEventT,self.__class__,SaHpiOemEventT)
lib_ohpi.SaHpiOemEventT_swigregister(SaHpiOemEventTPtr)

class SaHpiUserEventT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiUserEventT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiUserEventT, name)
    def __repr__(self):
        return "<C SaHpiUserEventT instance at %s>" % (self.this,)
    __swig_setmethods__["UserEventData"] = lib_ohpi.SaHpiUserEventT_UserEventData_set
    __swig_getmethods__["UserEventData"] = lib_ohpi.SaHpiUserEventT_UserEventData_get
    if _newclass:UserEventData = property(lib_ohpi.SaHpiUserEventT_UserEventData_get, lib_ohpi.SaHpiUserEventT_UserEventData_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiUserEventT, 'this', lib_ohpi.new_SaHpiUserEventT(*args))
        _swig_setattr(self, SaHpiUserEventT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiUserEventT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiUserEventTPtr(SaHpiUserEventT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiUserEventT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiUserEventT, 'thisown', 0)
        _swig_setattr(self, SaHpiUserEventT,self.__class__,SaHpiUserEventT)
lib_ohpi.SaHpiUserEventT_swigregister(SaHpiUserEventTPtr)

SAHPI_ET_RESOURCE = lib_ohpi.SAHPI_ET_RESOURCE
SAHPI_ET_DOMAIN = lib_ohpi.SAHPI_ET_DOMAIN
SAHPI_ET_SENSOR = lib_ohpi.SAHPI_ET_SENSOR
SAHPI_ET_SENSOR_ENABLE_CHANGE = lib_ohpi.SAHPI_ET_SENSOR_ENABLE_CHANGE
SAHPI_ET_HOTSWAP = lib_ohpi.SAHPI_ET_HOTSWAP
SAHPI_ET_WATCHDOG = lib_ohpi.SAHPI_ET_WATCHDOG
SAHPI_ET_HPI_SW = lib_ohpi.SAHPI_ET_HPI_SW
SAHPI_ET_OEM = lib_ohpi.SAHPI_ET_OEM
SAHPI_ET_USER = lib_ohpi.SAHPI_ET_USER
class SaHpiEventUnionT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiEventUnionT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiEventUnionT, name)
    def __repr__(self):
        return "<C SaHpiEventUnionT instance at %s>" % (self.this,)
    __swig_setmethods__["ResourceEvent"] = lib_ohpi.SaHpiEventUnionT_ResourceEvent_set
    __swig_getmethods__["ResourceEvent"] = lib_ohpi.SaHpiEventUnionT_ResourceEvent_get
    if _newclass:ResourceEvent = property(lib_ohpi.SaHpiEventUnionT_ResourceEvent_get, lib_ohpi.SaHpiEventUnionT_ResourceEvent_set)
    __swig_setmethods__["DomainEvent"] = lib_ohpi.SaHpiEventUnionT_DomainEvent_set
    __swig_getmethods__["DomainEvent"] = lib_ohpi.SaHpiEventUnionT_DomainEvent_get
    if _newclass:DomainEvent = property(lib_ohpi.SaHpiEventUnionT_DomainEvent_get, lib_ohpi.SaHpiEventUnionT_DomainEvent_set)
    __swig_setmethods__["SensorEvent"] = lib_ohpi.SaHpiEventUnionT_SensorEvent_set
    __swig_getmethods__["SensorEvent"] = lib_ohpi.SaHpiEventUnionT_SensorEvent_get
    if _newclass:SensorEvent = property(lib_ohpi.SaHpiEventUnionT_SensorEvent_get, lib_ohpi.SaHpiEventUnionT_SensorEvent_set)
    __swig_setmethods__["SensorEnableChangeEvent"] = lib_ohpi.SaHpiEventUnionT_SensorEnableChangeEvent_set
    __swig_getmethods__["SensorEnableChangeEvent"] = lib_ohpi.SaHpiEventUnionT_SensorEnableChangeEvent_get
    if _newclass:SensorEnableChangeEvent = property(lib_ohpi.SaHpiEventUnionT_SensorEnableChangeEvent_get, lib_ohpi.SaHpiEventUnionT_SensorEnableChangeEvent_set)
    __swig_setmethods__["HotSwapEvent"] = lib_ohpi.SaHpiEventUnionT_HotSwapEvent_set
    __swig_getmethods__["HotSwapEvent"] = lib_ohpi.SaHpiEventUnionT_HotSwapEvent_get
    if _newclass:HotSwapEvent = property(lib_ohpi.SaHpiEventUnionT_HotSwapEvent_get, lib_ohpi.SaHpiEventUnionT_HotSwapEvent_set)
    __swig_setmethods__["WatchdogEvent"] = lib_ohpi.SaHpiEventUnionT_WatchdogEvent_set
    __swig_getmethods__["WatchdogEvent"] = lib_ohpi.SaHpiEventUnionT_WatchdogEvent_get
    if _newclass:WatchdogEvent = property(lib_ohpi.SaHpiEventUnionT_WatchdogEvent_get, lib_ohpi.SaHpiEventUnionT_WatchdogEvent_set)
    __swig_setmethods__["HpiSwEvent"] = lib_ohpi.SaHpiEventUnionT_HpiSwEvent_set
    __swig_getmethods__["HpiSwEvent"] = lib_ohpi.SaHpiEventUnionT_HpiSwEvent_get
    if _newclass:HpiSwEvent = property(lib_ohpi.SaHpiEventUnionT_HpiSwEvent_get, lib_ohpi.SaHpiEventUnionT_HpiSwEvent_set)
    __swig_setmethods__["OemEvent"] = lib_ohpi.SaHpiEventUnionT_OemEvent_set
    __swig_getmethods__["OemEvent"] = lib_ohpi.SaHpiEventUnionT_OemEvent_get
    if _newclass:OemEvent = property(lib_ohpi.SaHpiEventUnionT_OemEvent_get, lib_ohpi.SaHpiEventUnionT_OemEvent_set)
    __swig_setmethods__["UserEvent"] = lib_ohpi.SaHpiEventUnionT_UserEvent_set
    __swig_getmethods__["UserEvent"] = lib_ohpi.SaHpiEventUnionT_UserEvent_get
    if _newclass:UserEvent = property(lib_ohpi.SaHpiEventUnionT_UserEvent_get, lib_ohpi.SaHpiEventUnionT_UserEvent_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiEventUnionT, 'this', lib_ohpi.new_SaHpiEventUnionT(*args))
        _swig_setattr(self, SaHpiEventUnionT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiEventUnionT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiEventUnionTPtr(SaHpiEventUnionT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiEventUnionT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiEventUnionT, 'thisown', 0)
        _swig_setattr(self, SaHpiEventUnionT,self.__class__,SaHpiEventUnionT)
lib_ohpi.SaHpiEventUnionT_swigregister(SaHpiEventUnionTPtr)

class SaHpiEventT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiEventT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiEventT, name)
    def __repr__(self):
        return "<C SaHpiEventT instance at %s>" % (self.this,)
    __swig_setmethods__["Source"] = lib_ohpi.SaHpiEventT_Source_set
    __swig_getmethods__["Source"] = lib_ohpi.SaHpiEventT_Source_get
    if _newclass:Source = property(lib_ohpi.SaHpiEventT_Source_get, lib_ohpi.SaHpiEventT_Source_set)
    __swig_setmethods__["EventType"] = lib_ohpi.SaHpiEventT_EventType_set
    __swig_getmethods__["EventType"] = lib_ohpi.SaHpiEventT_EventType_get
    if _newclass:EventType = property(lib_ohpi.SaHpiEventT_EventType_get, lib_ohpi.SaHpiEventT_EventType_set)
    __swig_setmethods__["Timestamp"] = lib_ohpi.SaHpiEventT_Timestamp_set
    __swig_getmethods__["Timestamp"] = lib_ohpi.SaHpiEventT_Timestamp_get
    if _newclass:Timestamp = property(lib_ohpi.SaHpiEventT_Timestamp_get, lib_ohpi.SaHpiEventT_Timestamp_set)
    __swig_setmethods__["Severity"] = lib_ohpi.SaHpiEventT_Severity_set
    __swig_getmethods__["Severity"] = lib_ohpi.SaHpiEventT_Severity_get
    if _newclass:Severity = property(lib_ohpi.SaHpiEventT_Severity_get, lib_ohpi.SaHpiEventT_Severity_set)
    __swig_setmethods__["EventDataUnion"] = lib_ohpi.SaHpiEventT_EventDataUnion_set
    __swig_getmethods__["EventDataUnion"] = lib_ohpi.SaHpiEventT_EventDataUnion_get
    if _newclass:EventDataUnion = property(lib_ohpi.SaHpiEventT_EventDataUnion_get, lib_ohpi.SaHpiEventT_EventDataUnion_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiEventT, 'this', lib_ohpi.new_SaHpiEventT(*args))
        _swig_setattr(self, SaHpiEventT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiEventT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiEventTPtr(SaHpiEventT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiEventT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiEventT, 'thisown', 0)
        _swig_setattr(self, SaHpiEventT,self.__class__,SaHpiEventT)
lib_ohpi.SaHpiEventT_swigregister(SaHpiEventTPtr)

SAHPI_EVT_QUEUE_OVERFLOW = lib_ohpi.SAHPI_EVT_QUEUE_OVERFLOW
SA_HPI_MAX_NAME_LENGTH = lib_ohpi.SA_HPI_MAX_NAME_LENGTH
class SaHpiNameT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiNameT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiNameT, name)
    def __repr__(self):
        return "<C SaHpiNameT instance at %s>" % (self.this,)
    __swig_setmethods__["Length"] = lib_ohpi.SaHpiNameT_Length_set
    __swig_getmethods__["Length"] = lib_ohpi.SaHpiNameT_Length_get
    if _newclass:Length = property(lib_ohpi.SaHpiNameT_Length_get, lib_ohpi.SaHpiNameT_Length_set)
    __swig_setmethods__["Value"] = lib_ohpi.SaHpiNameT_Value_set
    __swig_getmethods__["Value"] = lib_ohpi.SaHpiNameT_Value_get
    if _newclass:Value = property(lib_ohpi.SaHpiNameT_Value_get, lib_ohpi.SaHpiNameT_Value_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiNameT, 'this', lib_ohpi.new_SaHpiNameT(*args))
        _swig_setattr(self, SaHpiNameT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiNameT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiNameTPtr(SaHpiNameT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiNameT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiNameT, 'thisown', 0)
        _swig_setattr(self, SaHpiNameT,self.__class__,SaHpiNameT)
lib_ohpi.SaHpiNameT_swigregister(SaHpiNameTPtr)

SAHPI_STATUS_COND_TYPE_SENSOR = lib_ohpi.SAHPI_STATUS_COND_TYPE_SENSOR
SAHPI_STATUS_COND_TYPE_RESOURCE = lib_ohpi.SAHPI_STATUS_COND_TYPE_RESOURCE
SAHPI_STATUS_COND_TYPE_OEM = lib_ohpi.SAHPI_STATUS_COND_TYPE_OEM
SAHPI_STATUS_COND_TYPE_USER = lib_ohpi.SAHPI_STATUS_COND_TYPE_USER
class SaHpiConditionT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiConditionT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiConditionT, name)
    def __repr__(self):
        return "<C SaHpiConditionT instance at %s>" % (self.this,)
    __swig_setmethods__["Type"] = lib_ohpi.SaHpiConditionT_Type_set
    __swig_getmethods__["Type"] = lib_ohpi.SaHpiConditionT_Type_get
    if _newclass:Type = property(lib_ohpi.SaHpiConditionT_Type_get, lib_ohpi.SaHpiConditionT_Type_set)
    __swig_setmethods__["Entity"] = lib_ohpi.SaHpiConditionT_Entity_set
    __swig_getmethods__["Entity"] = lib_ohpi.SaHpiConditionT_Entity_get
    if _newclass:Entity = property(lib_ohpi.SaHpiConditionT_Entity_get, lib_ohpi.SaHpiConditionT_Entity_set)
    __swig_setmethods__["DomainId"] = lib_ohpi.SaHpiConditionT_DomainId_set
    __swig_getmethods__["DomainId"] = lib_ohpi.SaHpiConditionT_DomainId_get
    if _newclass:DomainId = property(lib_ohpi.SaHpiConditionT_DomainId_get, lib_ohpi.SaHpiConditionT_DomainId_set)
    __swig_setmethods__["ResourceId"] = lib_ohpi.SaHpiConditionT_ResourceId_set
    __swig_getmethods__["ResourceId"] = lib_ohpi.SaHpiConditionT_ResourceId_get
    if _newclass:ResourceId = property(lib_ohpi.SaHpiConditionT_ResourceId_get, lib_ohpi.SaHpiConditionT_ResourceId_set)
    __swig_setmethods__["SensorNum"] = lib_ohpi.SaHpiConditionT_SensorNum_set
    __swig_getmethods__["SensorNum"] = lib_ohpi.SaHpiConditionT_SensorNum_get
    if _newclass:SensorNum = property(lib_ohpi.SaHpiConditionT_SensorNum_get, lib_ohpi.SaHpiConditionT_SensorNum_set)
    __swig_setmethods__["EventState"] = lib_ohpi.SaHpiConditionT_EventState_set
    __swig_getmethods__["EventState"] = lib_ohpi.SaHpiConditionT_EventState_get
    if _newclass:EventState = property(lib_ohpi.SaHpiConditionT_EventState_get, lib_ohpi.SaHpiConditionT_EventState_set)
    __swig_setmethods__["Name"] = lib_ohpi.SaHpiConditionT_Name_set
    __swig_getmethods__["Name"] = lib_ohpi.SaHpiConditionT_Name_get
    if _newclass:Name = property(lib_ohpi.SaHpiConditionT_Name_get, lib_ohpi.SaHpiConditionT_Name_set)
    __swig_setmethods__["Mid"] = lib_ohpi.SaHpiConditionT_Mid_set
    __swig_getmethods__["Mid"] = lib_ohpi.SaHpiConditionT_Mid_get
    if _newclass:Mid = property(lib_ohpi.SaHpiConditionT_Mid_get, lib_ohpi.SaHpiConditionT_Mid_set)
    __swig_setmethods__["Data"] = lib_ohpi.SaHpiConditionT_Data_set
    __swig_getmethods__["Data"] = lib_ohpi.SaHpiConditionT_Data_get
    if _newclass:Data = property(lib_ohpi.SaHpiConditionT_Data_get, lib_ohpi.SaHpiConditionT_Data_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiConditionT, 'this', lib_ohpi.new_SaHpiConditionT(*args))
        _swig_setattr(self, SaHpiConditionT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiConditionT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiConditionTPtr(SaHpiConditionT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiConditionT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiConditionT, 'thisown', 0)
        _swig_setattr(self, SaHpiConditionT,self.__class__,SaHpiConditionT)
lib_ohpi.SaHpiConditionT_swigregister(SaHpiConditionTPtr)

class SaHpiAnnouncementT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiAnnouncementT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiAnnouncementT, name)
    def __repr__(self):
        return "<C SaHpiAnnouncementT instance at %s>" % (self.this,)
    __swig_setmethods__["EntryId"] = lib_ohpi.SaHpiAnnouncementT_EntryId_set
    __swig_getmethods__["EntryId"] = lib_ohpi.SaHpiAnnouncementT_EntryId_get
    if _newclass:EntryId = property(lib_ohpi.SaHpiAnnouncementT_EntryId_get, lib_ohpi.SaHpiAnnouncementT_EntryId_set)
    __swig_setmethods__["Timestamp"] = lib_ohpi.SaHpiAnnouncementT_Timestamp_set
    __swig_getmethods__["Timestamp"] = lib_ohpi.SaHpiAnnouncementT_Timestamp_get
    if _newclass:Timestamp = property(lib_ohpi.SaHpiAnnouncementT_Timestamp_get, lib_ohpi.SaHpiAnnouncementT_Timestamp_set)
    __swig_setmethods__["AddedByUser"] = lib_ohpi.SaHpiAnnouncementT_AddedByUser_set
    __swig_getmethods__["AddedByUser"] = lib_ohpi.SaHpiAnnouncementT_AddedByUser_get
    if _newclass:AddedByUser = property(lib_ohpi.SaHpiAnnouncementT_AddedByUser_get, lib_ohpi.SaHpiAnnouncementT_AddedByUser_set)
    __swig_setmethods__["Severity"] = lib_ohpi.SaHpiAnnouncementT_Severity_set
    __swig_getmethods__["Severity"] = lib_ohpi.SaHpiAnnouncementT_Severity_get
    if _newclass:Severity = property(lib_ohpi.SaHpiAnnouncementT_Severity_get, lib_ohpi.SaHpiAnnouncementT_Severity_set)
    __swig_setmethods__["Acknowledged"] = lib_ohpi.SaHpiAnnouncementT_Acknowledged_set
    __swig_getmethods__["Acknowledged"] = lib_ohpi.SaHpiAnnouncementT_Acknowledged_get
    if _newclass:Acknowledged = property(lib_ohpi.SaHpiAnnouncementT_Acknowledged_get, lib_ohpi.SaHpiAnnouncementT_Acknowledged_set)
    __swig_setmethods__["StatusCond"] = lib_ohpi.SaHpiAnnouncementT_StatusCond_set
    __swig_getmethods__["StatusCond"] = lib_ohpi.SaHpiAnnouncementT_StatusCond_get
    if _newclass:StatusCond = property(lib_ohpi.SaHpiAnnouncementT_StatusCond_get, lib_ohpi.SaHpiAnnouncementT_StatusCond_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiAnnouncementT, 'this', lib_ohpi.new_SaHpiAnnouncementT(*args))
        _swig_setattr(self, SaHpiAnnouncementT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiAnnouncementT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiAnnouncementTPtr(SaHpiAnnouncementT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiAnnouncementT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiAnnouncementT, 'thisown', 0)
        _swig_setattr(self, SaHpiAnnouncementT,self.__class__,SaHpiAnnouncementT)
lib_ohpi.SaHpiAnnouncementT_swigregister(SaHpiAnnouncementTPtr)

SAHPI_ANNUNCIATOR_MODE_AUTO = lib_ohpi.SAHPI_ANNUNCIATOR_MODE_AUTO
SAHPI_ANNUNCIATOR_MODE_USER = lib_ohpi.SAHPI_ANNUNCIATOR_MODE_USER
SAHPI_ANNUNCIATOR_MODE_SHARED = lib_ohpi.SAHPI_ANNUNCIATOR_MODE_SHARED
SAHPI_ANNUNCIATOR_TYPE_LED = lib_ohpi.SAHPI_ANNUNCIATOR_TYPE_LED
SAHPI_ANNUNCIATOR_TYPE_DRY_CONTACT_CLOSURE = lib_ohpi.SAHPI_ANNUNCIATOR_TYPE_DRY_CONTACT_CLOSURE
SAHPI_ANNUNCIATOR_TYPE_AUDIBLE = lib_ohpi.SAHPI_ANNUNCIATOR_TYPE_AUDIBLE
SAHPI_ANNUNCIATOR_TYPE_LCD_DISPLAY = lib_ohpi.SAHPI_ANNUNCIATOR_TYPE_LCD_DISPLAY
SAHPI_ANNUNCIATOR_TYPE_MESSAGE = lib_ohpi.SAHPI_ANNUNCIATOR_TYPE_MESSAGE
SAHPI_ANNUNCIATOR_TYPE_COMPOSITE = lib_ohpi.SAHPI_ANNUNCIATOR_TYPE_COMPOSITE
SAHPI_ANNUNCIATOR_TYPE_OEM = lib_ohpi.SAHPI_ANNUNCIATOR_TYPE_OEM
class SaHpiAnnunciatorRecT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiAnnunciatorRecT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiAnnunciatorRecT, name)
    def __repr__(self):
        return "<C SaHpiAnnunciatorRecT instance at %s>" % (self.this,)
    __swig_setmethods__["AnnunciatorNum"] = lib_ohpi.SaHpiAnnunciatorRecT_AnnunciatorNum_set
    __swig_getmethods__["AnnunciatorNum"] = lib_ohpi.SaHpiAnnunciatorRecT_AnnunciatorNum_get
    if _newclass:AnnunciatorNum = property(lib_ohpi.SaHpiAnnunciatorRecT_AnnunciatorNum_get, lib_ohpi.SaHpiAnnunciatorRecT_AnnunciatorNum_set)
    __swig_setmethods__["AnnunciatorType"] = lib_ohpi.SaHpiAnnunciatorRecT_AnnunciatorType_set
    __swig_getmethods__["AnnunciatorType"] = lib_ohpi.SaHpiAnnunciatorRecT_AnnunciatorType_get
    if _newclass:AnnunciatorType = property(lib_ohpi.SaHpiAnnunciatorRecT_AnnunciatorType_get, lib_ohpi.SaHpiAnnunciatorRecT_AnnunciatorType_set)
    __swig_setmethods__["ModeReadOnly"] = lib_ohpi.SaHpiAnnunciatorRecT_ModeReadOnly_set
    __swig_getmethods__["ModeReadOnly"] = lib_ohpi.SaHpiAnnunciatorRecT_ModeReadOnly_get
    if _newclass:ModeReadOnly = property(lib_ohpi.SaHpiAnnunciatorRecT_ModeReadOnly_get, lib_ohpi.SaHpiAnnunciatorRecT_ModeReadOnly_set)
    __swig_setmethods__["MaxConditions"] = lib_ohpi.SaHpiAnnunciatorRecT_MaxConditions_set
    __swig_getmethods__["MaxConditions"] = lib_ohpi.SaHpiAnnunciatorRecT_MaxConditions_get
    if _newclass:MaxConditions = property(lib_ohpi.SaHpiAnnunciatorRecT_MaxConditions_get, lib_ohpi.SaHpiAnnunciatorRecT_MaxConditions_set)
    __swig_setmethods__["Oem"] = lib_ohpi.SaHpiAnnunciatorRecT_Oem_set
    __swig_getmethods__["Oem"] = lib_ohpi.SaHpiAnnunciatorRecT_Oem_get
    if _newclass:Oem = property(lib_ohpi.SaHpiAnnunciatorRecT_Oem_get, lib_ohpi.SaHpiAnnunciatorRecT_Oem_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiAnnunciatorRecT, 'this', lib_ohpi.new_SaHpiAnnunciatorRecT(*args))
        _swig_setattr(self, SaHpiAnnunciatorRecT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiAnnunciatorRecT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiAnnunciatorRecTPtr(SaHpiAnnunciatorRecT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiAnnunciatorRecT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiAnnunciatorRecT, 'thisown', 0)
        _swig_setattr(self, SaHpiAnnunciatorRecT,self.__class__,SaHpiAnnunciatorRecT)
lib_ohpi.SaHpiAnnunciatorRecT_swigregister(SaHpiAnnunciatorRecTPtr)

SAHPI_NO_RECORD = lib_ohpi.SAHPI_NO_RECORD
SAHPI_CTRL_RDR = lib_ohpi.SAHPI_CTRL_RDR
SAHPI_SENSOR_RDR = lib_ohpi.SAHPI_SENSOR_RDR
SAHPI_INVENTORY_RDR = lib_ohpi.SAHPI_INVENTORY_RDR
SAHPI_WATCHDOG_RDR = lib_ohpi.SAHPI_WATCHDOG_RDR
SAHPI_ANNUNCIATOR_RDR = lib_ohpi.SAHPI_ANNUNCIATOR_RDR
class SaHpiRdrTypeUnionT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiRdrTypeUnionT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiRdrTypeUnionT, name)
    def __repr__(self):
        return "<C SaHpiRdrTypeUnionT instance at %s>" % (self.this,)
    __swig_setmethods__["CtrlRec"] = lib_ohpi.SaHpiRdrTypeUnionT_CtrlRec_set
    __swig_getmethods__["CtrlRec"] = lib_ohpi.SaHpiRdrTypeUnionT_CtrlRec_get
    if _newclass:CtrlRec = property(lib_ohpi.SaHpiRdrTypeUnionT_CtrlRec_get, lib_ohpi.SaHpiRdrTypeUnionT_CtrlRec_set)
    __swig_setmethods__["SensorRec"] = lib_ohpi.SaHpiRdrTypeUnionT_SensorRec_set
    __swig_getmethods__["SensorRec"] = lib_ohpi.SaHpiRdrTypeUnionT_SensorRec_get
    if _newclass:SensorRec = property(lib_ohpi.SaHpiRdrTypeUnionT_SensorRec_get, lib_ohpi.SaHpiRdrTypeUnionT_SensorRec_set)
    __swig_setmethods__["InventoryRec"] = lib_ohpi.SaHpiRdrTypeUnionT_InventoryRec_set
    __swig_getmethods__["InventoryRec"] = lib_ohpi.SaHpiRdrTypeUnionT_InventoryRec_get
    if _newclass:InventoryRec = property(lib_ohpi.SaHpiRdrTypeUnionT_InventoryRec_get, lib_ohpi.SaHpiRdrTypeUnionT_InventoryRec_set)
    __swig_setmethods__["WatchdogRec"] = lib_ohpi.SaHpiRdrTypeUnionT_WatchdogRec_set
    __swig_getmethods__["WatchdogRec"] = lib_ohpi.SaHpiRdrTypeUnionT_WatchdogRec_get
    if _newclass:WatchdogRec = property(lib_ohpi.SaHpiRdrTypeUnionT_WatchdogRec_get, lib_ohpi.SaHpiRdrTypeUnionT_WatchdogRec_set)
    __swig_setmethods__["AnnunciatorRec"] = lib_ohpi.SaHpiRdrTypeUnionT_AnnunciatorRec_set
    __swig_getmethods__["AnnunciatorRec"] = lib_ohpi.SaHpiRdrTypeUnionT_AnnunciatorRec_get
    if _newclass:AnnunciatorRec = property(lib_ohpi.SaHpiRdrTypeUnionT_AnnunciatorRec_get, lib_ohpi.SaHpiRdrTypeUnionT_AnnunciatorRec_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiRdrTypeUnionT, 'this', lib_ohpi.new_SaHpiRdrTypeUnionT(*args))
        _swig_setattr(self, SaHpiRdrTypeUnionT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiRdrTypeUnionT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiRdrTypeUnionTPtr(SaHpiRdrTypeUnionT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiRdrTypeUnionT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiRdrTypeUnionT, 'thisown', 0)
        _swig_setattr(self, SaHpiRdrTypeUnionT,self.__class__,SaHpiRdrTypeUnionT)
lib_ohpi.SaHpiRdrTypeUnionT_swigregister(SaHpiRdrTypeUnionTPtr)

class SaHpiRdrT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiRdrT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiRdrT, name)
    def __repr__(self):
        return "<C SaHpiRdrT instance at %s>" % (self.this,)
    __swig_setmethods__["RecordId"] = lib_ohpi.SaHpiRdrT_RecordId_set
    __swig_getmethods__["RecordId"] = lib_ohpi.SaHpiRdrT_RecordId_get
    if _newclass:RecordId = property(lib_ohpi.SaHpiRdrT_RecordId_get, lib_ohpi.SaHpiRdrT_RecordId_set)
    __swig_setmethods__["RdrType"] = lib_ohpi.SaHpiRdrT_RdrType_set
    __swig_getmethods__["RdrType"] = lib_ohpi.SaHpiRdrT_RdrType_get
    if _newclass:RdrType = property(lib_ohpi.SaHpiRdrT_RdrType_get, lib_ohpi.SaHpiRdrT_RdrType_set)
    __swig_setmethods__["Entity"] = lib_ohpi.SaHpiRdrT_Entity_set
    __swig_getmethods__["Entity"] = lib_ohpi.SaHpiRdrT_Entity_get
    if _newclass:Entity = property(lib_ohpi.SaHpiRdrT_Entity_get, lib_ohpi.SaHpiRdrT_Entity_set)
    __swig_setmethods__["IsFru"] = lib_ohpi.SaHpiRdrT_IsFru_set
    __swig_getmethods__["IsFru"] = lib_ohpi.SaHpiRdrT_IsFru_get
    if _newclass:IsFru = property(lib_ohpi.SaHpiRdrT_IsFru_get, lib_ohpi.SaHpiRdrT_IsFru_set)
    __swig_setmethods__["RdrTypeUnion"] = lib_ohpi.SaHpiRdrT_RdrTypeUnion_set
    __swig_getmethods__["RdrTypeUnion"] = lib_ohpi.SaHpiRdrT_RdrTypeUnion_get
    if _newclass:RdrTypeUnion = property(lib_ohpi.SaHpiRdrT_RdrTypeUnion_get, lib_ohpi.SaHpiRdrT_RdrTypeUnion_set)
    __swig_setmethods__["IdString"] = lib_ohpi.SaHpiRdrT_IdString_set
    __swig_getmethods__["IdString"] = lib_ohpi.SaHpiRdrT_IdString_get
    if _newclass:IdString = property(lib_ohpi.SaHpiRdrT_IdString_get, lib_ohpi.SaHpiRdrT_IdString_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiRdrT, 'this', lib_ohpi.new_SaHpiRdrT(*args))
        _swig_setattr(self, SaHpiRdrT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiRdrT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiRdrTPtr(SaHpiRdrT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiRdrT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiRdrT, 'thisown', 0)
        _swig_setattr(self, SaHpiRdrT,self.__class__,SaHpiRdrT)
lib_ohpi.SaHpiRdrT_swigregister(SaHpiRdrTPtr)

SAHPI_DEFAULT_PARM = lib_ohpi.SAHPI_DEFAULT_PARM
SAHPI_SAVE_PARM = lib_ohpi.SAHPI_SAVE_PARM
SAHPI_RESTORE_PARM = lib_ohpi.SAHPI_RESTORE_PARM
SAHPI_COLD_RESET = lib_ohpi.SAHPI_COLD_RESET
SAHPI_WARM_RESET = lib_ohpi.SAHPI_WARM_RESET
SAHPI_RESET_ASSERT = lib_ohpi.SAHPI_RESET_ASSERT
SAHPI_RESET_DEASSERT = lib_ohpi.SAHPI_RESET_DEASSERT
SAHPI_POWER_OFF = lib_ohpi.SAHPI_POWER_OFF
SAHPI_POWER_ON = lib_ohpi.SAHPI_POWER_ON
SAHPI_POWER_CYCLE = lib_ohpi.SAHPI_POWER_CYCLE
class SaHpiResourceInfoT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiResourceInfoT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiResourceInfoT, name)
    def __repr__(self):
        return "<C SaHpiResourceInfoT instance at %s>" % (self.this,)
    __swig_setmethods__["ResourceRev"] = lib_ohpi.SaHpiResourceInfoT_ResourceRev_set
    __swig_getmethods__["ResourceRev"] = lib_ohpi.SaHpiResourceInfoT_ResourceRev_get
    if _newclass:ResourceRev = property(lib_ohpi.SaHpiResourceInfoT_ResourceRev_get, lib_ohpi.SaHpiResourceInfoT_ResourceRev_set)
    __swig_setmethods__["SpecificVer"] = lib_ohpi.SaHpiResourceInfoT_SpecificVer_set
    __swig_getmethods__["SpecificVer"] = lib_ohpi.SaHpiResourceInfoT_SpecificVer_get
    if _newclass:SpecificVer = property(lib_ohpi.SaHpiResourceInfoT_SpecificVer_get, lib_ohpi.SaHpiResourceInfoT_SpecificVer_set)
    __swig_setmethods__["DeviceSupport"] = lib_ohpi.SaHpiResourceInfoT_DeviceSupport_set
    __swig_getmethods__["DeviceSupport"] = lib_ohpi.SaHpiResourceInfoT_DeviceSupport_get
    if _newclass:DeviceSupport = property(lib_ohpi.SaHpiResourceInfoT_DeviceSupport_get, lib_ohpi.SaHpiResourceInfoT_DeviceSupport_set)
    __swig_setmethods__["ManufacturerId"] = lib_ohpi.SaHpiResourceInfoT_ManufacturerId_set
    __swig_getmethods__["ManufacturerId"] = lib_ohpi.SaHpiResourceInfoT_ManufacturerId_get
    if _newclass:ManufacturerId = property(lib_ohpi.SaHpiResourceInfoT_ManufacturerId_get, lib_ohpi.SaHpiResourceInfoT_ManufacturerId_set)
    __swig_setmethods__["ProductId"] = lib_ohpi.SaHpiResourceInfoT_ProductId_set
    __swig_getmethods__["ProductId"] = lib_ohpi.SaHpiResourceInfoT_ProductId_get
    if _newclass:ProductId = property(lib_ohpi.SaHpiResourceInfoT_ProductId_get, lib_ohpi.SaHpiResourceInfoT_ProductId_set)
    __swig_setmethods__["FirmwareMajorRev"] = lib_ohpi.SaHpiResourceInfoT_FirmwareMajorRev_set
    __swig_getmethods__["FirmwareMajorRev"] = lib_ohpi.SaHpiResourceInfoT_FirmwareMajorRev_get
    if _newclass:FirmwareMajorRev = property(lib_ohpi.SaHpiResourceInfoT_FirmwareMajorRev_get, lib_ohpi.SaHpiResourceInfoT_FirmwareMajorRev_set)
    __swig_setmethods__["FirmwareMinorRev"] = lib_ohpi.SaHpiResourceInfoT_FirmwareMinorRev_set
    __swig_getmethods__["FirmwareMinorRev"] = lib_ohpi.SaHpiResourceInfoT_FirmwareMinorRev_get
    if _newclass:FirmwareMinorRev = property(lib_ohpi.SaHpiResourceInfoT_FirmwareMinorRev_get, lib_ohpi.SaHpiResourceInfoT_FirmwareMinorRev_set)
    __swig_setmethods__["AuxFirmwareRev"] = lib_ohpi.SaHpiResourceInfoT_AuxFirmwareRev_set
    __swig_getmethods__["AuxFirmwareRev"] = lib_ohpi.SaHpiResourceInfoT_AuxFirmwareRev_get
    if _newclass:AuxFirmwareRev = property(lib_ohpi.SaHpiResourceInfoT_AuxFirmwareRev_get, lib_ohpi.SaHpiResourceInfoT_AuxFirmwareRev_set)
    __swig_setmethods__["Guid"] = lib_ohpi.SaHpiResourceInfoT_Guid_set
    __swig_getmethods__["Guid"] = lib_ohpi.SaHpiResourceInfoT_Guid_get
    if _newclass:Guid = property(lib_ohpi.SaHpiResourceInfoT_Guid_get, lib_ohpi.SaHpiResourceInfoT_Guid_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiResourceInfoT, 'this', lib_ohpi.new_SaHpiResourceInfoT(*args))
        _swig_setattr(self, SaHpiResourceInfoT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiResourceInfoT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiResourceInfoTPtr(SaHpiResourceInfoT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiResourceInfoT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiResourceInfoT, 'thisown', 0)
        _swig_setattr(self, SaHpiResourceInfoT,self.__class__,SaHpiResourceInfoT)
lib_ohpi.SaHpiResourceInfoT_swigregister(SaHpiResourceInfoTPtr)

SAHPI_CAPABILITY_RESOURCE = lib_ohpi.SAHPI_CAPABILITY_RESOURCE
SAHPI_CAPABILITY_EVT_DEASSERTS = lib_ohpi.SAHPI_CAPABILITY_EVT_DEASSERTS
SAHPI_CAPABILITY_AGGREGATE_STATUS = lib_ohpi.SAHPI_CAPABILITY_AGGREGATE_STATUS
SAHPI_CAPABILITY_CONFIGURATION = lib_ohpi.SAHPI_CAPABILITY_CONFIGURATION
SAHPI_CAPABILITY_MANAGED_HOTSWAP = lib_ohpi.SAHPI_CAPABILITY_MANAGED_HOTSWAP
SAHPI_CAPABILITY_WATCHDOG = lib_ohpi.SAHPI_CAPABILITY_WATCHDOG
SAHPI_CAPABILITY_CONTROL = lib_ohpi.SAHPI_CAPABILITY_CONTROL
SAHPI_CAPABILITY_FRU = lib_ohpi.SAHPI_CAPABILITY_FRU
SAHPI_CAPABILITY_ANNUNCIATOR = lib_ohpi.SAHPI_CAPABILITY_ANNUNCIATOR
SAHPI_CAPABILITY_POWER = lib_ohpi.SAHPI_CAPABILITY_POWER
SAHPI_CAPABILITY_RESET = lib_ohpi.SAHPI_CAPABILITY_RESET
SAHPI_CAPABILITY_INVENTORY_DATA = lib_ohpi.SAHPI_CAPABILITY_INVENTORY_DATA
SAHPI_CAPABILITY_EVENT_LOG = lib_ohpi.SAHPI_CAPABILITY_EVENT_LOG
SAHPI_CAPABILITY_RDR = lib_ohpi.SAHPI_CAPABILITY_RDR
SAHPI_CAPABILITY_SENSOR = lib_ohpi.SAHPI_CAPABILITY_SENSOR
class SaHpiRptEntryT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiRptEntryT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiRptEntryT, name)
    def __repr__(self):
        return "<C SaHpiRptEntryT instance at %s>" % (self.this,)
    __swig_setmethods__["EntryId"] = lib_ohpi.SaHpiRptEntryT_EntryId_set
    __swig_getmethods__["EntryId"] = lib_ohpi.SaHpiRptEntryT_EntryId_get
    if _newclass:EntryId = property(lib_ohpi.SaHpiRptEntryT_EntryId_get, lib_ohpi.SaHpiRptEntryT_EntryId_set)
    __swig_setmethods__["ResourceId"] = lib_ohpi.SaHpiRptEntryT_ResourceId_set
    __swig_getmethods__["ResourceId"] = lib_ohpi.SaHpiRptEntryT_ResourceId_get
    if _newclass:ResourceId = property(lib_ohpi.SaHpiRptEntryT_ResourceId_get, lib_ohpi.SaHpiRptEntryT_ResourceId_set)
    __swig_setmethods__["ResourceInfo"] = lib_ohpi.SaHpiRptEntryT_ResourceInfo_set
    __swig_getmethods__["ResourceInfo"] = lib_ohpi.SaHpiRptEntryT_ResourceInfo_get
    if _newclass:ResourceInfo = property(lib_ohpi.SaHpiRptEntryT_ResourceInfo_get, lib_ohpi.SaHpiRptEntryT_ResourceInfo_set)
    __swig_setmethods__["ResourceEntity"] = lib_ohpi.SaHpiRptEntryT_ResourceEntity_set
    __swig_getmethods__["ResourceEntity"] = lib_ohpi.SaHpiRptEntryT_ResourceEntity_get
    if _newclass:ResourceEntity = property(lib_ohpi.SaHpiRptEntryT_ResourceEntity_get, lib_ohpi.SaHpiRptEntryT_ResourceEntity_set)
    __swig_setmethods__["ResourceCapabilities"] = lib_ohpi.SaHpiRptEntryT_ResourceCapabilities_set
    __swig_getmethods__["ResourceCapabilities"] = lib_ohpi.SaHpiRptEntryT_ResourceCapabilities_get
    if _newclass:ResourceCapabilities = property(lib_ohpi.SaHpiRptEntryT_ResourceCapabilities_get, lib_ohpi.SaHpiRptEntryT_ResourceCapabilities_set)
    __swig_setmethods__["HotSwapCapabilities"] = lib_ohpi.SaHpiRptEntryT_HotSwapCapabilities_set
    __swig_getmethods__["HotSwapCapabilities"] = lib_ohpi.SaHpiRptEntryT_HotSwapCapabilities_get
    if _newclass:HotSwapCapabilities = property(lib_ohpi.SaHpiRptEntryT_HotSwapCapabilities_get, lib_ohpi.SaHpiRptEntryT_HotSwapCapabilities_set)
    __swig_setmethods__["ResourceSeverity"] = lib_ohpi.SaHpiRptEntryT_ResourceSeverity_set
    __swig_getmethods__["ResourceSeverity"] = lib_ohpi.SaHpiRptEntryT_ResourceSeverity_get
    if _newclass:ResourceSeverity = property(lib_ohpi.SaHpiRptEntryT_ResourceSeverity_get, lib_ohpi.SaHpiRptEntryT_ResourceSeverity_set)
    __swig_setmethods__["ResourceFailed"] = lib_ohpi.SaHpiRptEntryT_ResourceFailed_set
    __swig_getmethods__["ResourceFailed"] = lib_ohpi.SaHpiRptEntryT_ResourceFailed_get
    if _newclass:ResourceFailed = property(lib_ohpi.SaHpiRptEntryT_ResourceFailed_get, lib_ohpi.SaHpiRptEntryT_ResourceFailed_set)
    __swig_setmethods__["ResourceTag"] = lib_ohpi.SaHpiRptEntryT_ResourceTag_set
    __swig_getmethods__["ResourceTag"] = lib_ohpi.SaHpiRptEntryT_ResourceTag_get
    if _newclass:ResourceTag = property(lib_ohpi.SaHpiRptEntryT_ResourceTag_get, lib_ohpi.SaHpiRptEntryT_ResourceTag_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiRptEntryT, 'this', lib_ohpi.new_SaHpiRptEntryT(*args))
        _swig_setattr(self, SaHpiRptEntryT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiRptEntryT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiRptEntryTPtr(SaHpiRptEntryT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiRptEntryT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiRptEntryT, 'thisown', 0)
        _swig_setattr(self, SaHpiRptEntryT,self.__class__,SaHpiRptEntryT)
lib_ohpi.SaHpiRptEntryT_swigregister(SaHpiRptEntryTPtr)

class SaHpiDomainInfoT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiDomainInfoT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiDomainInfoT, name)
    def __repr__(self):
        return "<C SaHpiDomainInfoT instance at %s>" % (self.this,)
    __swig_setmethods__["DomainId"] = lib_ohpi.SaHpiDomainInfoT_DomainId_set
    __swig_getmethods__["DomainId"] = lib_ohpi.SaHpiDomainInfoT_DomainId_get
    if _newclass:DomainId = property(lib_ohpi.SaHpiDomainInfoT_DomainId_get, lib_ohpi.SaHpiDomainInfoT_DomainId_set)
    __swig_setmethods__["DomainCapabilities"] = lib_ohpi.SaHpiDomainInfoT_DomainCapabilities_set
    __swig_getmethods__["DomainCapabilities"] = lib_ohpi.SaHpiDomainInfoT_DomainCapabilities_get
    if _newclass:DomainCapabilities = property(lib_ohpi.SaHpiDomainInfoT_DomainCapabilities_get, lib_ohpi.SaHpiDomainInfoT_DomainCapabilities_set)
    __swig_setmethods__["IsPeer"] = lib_ohpi.SaHpiDomainInfoT_IsPeer_set
    __swig_getmethods__["IsPeer"] = lib_ohpi.SaHpiDomainInfoT_IsPeer_get
    if _newclass:IsPeer = property(lib_ohpi.SaHpiDomainInfoT_IsPeer_get, lib_ohpi.SaHpiDomainInfoT_IsPeer_set)
    __swig_setmethods__["DomainTag"] = lib_ohpi.SaHpiDomainInfoT_DomainTag_set
    __swig_getmethods__["DomainTag"] = lib_ohpi.SaHpiDomainInfoT_DomainTag_get
    if _newclass:DomainTag = property(lib_ohpi.SaHpiDomainInfoT_DomainTag_get, lib_ohpi.SaHpiDomainInfoT_DomainTag_set)
    __swig_setmethods__["DrtUpdateCount"] = lib_ohpi.SaHpiDomainInfoT_DrtUpdateCount_set
    __swig_getmethods__["DrtUpdateCount"] = lib_ohpi.SaHpiDomainInfoT_DrtUpdateCount_get
    if _newclass:DrtUpdateCount = property(lib_ohpi.SaHpiDomainInfoT_DrtUpdateCount_get, lib_ohpi.SaHpiDomainInfoT_DrtUpdateCount_set)
    __swig_setmethods__["DrtUpdateTimestamp"] = lib_ohpi.SaHpiDomainInfoT_DrtUpdateTimestamp_set
    __swig_getmethods__["DrtUpdateTimestamp"] = lib_ohpi.SaHpiDomainInfoT_DrtUpdateTimestamp_get
    if _newclass:DrtUpdateTimestamp = property(lib_ohpi.SaHpiDomainInfoT_DrtUpdateTimestamp_get, lib_ohpi.SaHpiDomainInfoT_DrtUpdateTimestamp_set)
    __swig_setmethods__["RptUpdateCount"] = lib_ohpi.SaHpiDomainInfoT_RptUpdateCount_set
    __swig_getmethods__["RptUpdateCount"] = lib_ohpi.SaHpiDomainInfoT_RptUpdateCount_get
    if _newclass:RptUpdateCount = property(lib_ohpi.SaHpiDomainInfoT_RptUpdateCount_get, lib_ohpi.SaHpiDomainInfoT_RptUpdateCount_set)
    __swig_setmethods__["RptUpdateTimestamp"] = lib_ohpi.SaHpiDomainInfoT_RptUpdateTimestamp_set
    __swig_getmethods__["RptUpdateTimestamp"] = lib_ohpi.SaHpiDomainInfoT_RptUpdateTimestamp_get
    if _newclass:RptUpdateTimestamp = property(lib_ohpi.SaHpiDomainInfoT_RptUpdateTimestamp_get, lib_ohpi.SaHpiDomainInfoT_RptUpdateTimestamp_set)
    __swig_setmethods__["DatUpdateCount"] = lib_ohpi.SaHpiDomainInfoT_DatUpdateCount_set
    __swig_getmethods__["DatUpdateCount"] = lib_ohpi.SaHpiDomainInfoT_DatUpdateCount_get
    if _newclass:DatUpdateCount = property(lib_ohpi.SaHpiDomainInfoT_DatUpdateCount_get, lib_ohpi.SaHpiDomainInfoT_DatUpdateCount_set)
    __swig_setmethods__["DatUpdateTimestamp"] = lib_ohpi.SaHpiDomainInfoT_DatUpdateTimestamp_set
    __swig_getmethods__["DatUpdateTimestamp"] = lib_ohpi.SaHpiDomainInfoT_DatUpdateTimestamp_get
    if _newclass:DatUpdateTimestamp = property(lib_ohpi.SaHpiDomainInfoT_DatUpdateTimestamp_get, lib_ohpi.SaHpiDomainInfoT_DatUpdateTimestamp_set)
    __swig_setmethods__["ActiveAlarms"] = lib_ohpi.SaHpiDomainInfoT_ActiveAlarms_set
    __swig_getmethods__["ActiveAlarms"] = lib_ohpi.SaHpiDomainInfoT_ActiveAlarms_get
    if _newclass:ActiveAlarms = property(lib_ohpi.SaHpiDomainInfoT_ActiveAlarms_get, lib_ohpi.SaHpiDomainInfoT_ActiveAlarms_set)
    __swig_setmethods__["CriticalAlarms"] = lib_ohpi.SaHpiDomainInfoT_CriticalAlarms_set
    __swig_getmethods__["CriticalAlarms"] = lib_ohpi.SaHpiDomainInfoT_CriticalAlarms_get
    if _newclass:CriticalAlarms = property(lib_ohpi.SaHpiDomainInfoT_CriticalAlarms_get, lib_ohpi.SaHpiDomainInfoT_CriticalAlarms_set)
    __swig_setmethods__["MajorAlarms"] = lib_ohpi.SaHpiDomainInfoT_MajorAlarms_set
    __swig_getmethods__["MajorAlarms"] = lib_ohpi.SaHpiDomainInfoT_MajorAlarms_get
    if _newclass:MajorAlarms = property(lib_ohpi.SaHpiDomainInfoT_MajorAlarms_get, lib_ohpi.SaHpiDomainInfoT_MajorAlarms_set)
    __swig_setmethods__["MinorAlarms"] = lib_ohpi.SaHpiDomainInfoT_MinorAlarms_set
    __swig_getmethods__["MinorAlarms"] = lib_ohpi.SaHpiDomainInfoT_MinorAlarms_get
    if _newclass:MinorAlarms = property(lib_ohpi.SaHpiDomainInfoT_MinorAlarms_get, lib_ohpi.SaHpiDomainInfoT_MinorAlarms_set)
    __swig_setmethods__["DatUserAlarmLimit"] = lib_ohpi.SaHpiDomainInfoT_DatUserAlarmLimit_set
    __swig_getmethods__["DatUserAlarmLimit"] = lib_ohpi.SaHpiDomainInfoT_DatUserAlarmLimit_get
    if _newclass:DatUserAlarmLimit = property(lib_ohpi.SaHpiDomainInfoT_DatUserAlarmLimit_get, lib_ohpi.SaHpiDomainInfoT_DatUserAlarmLimit_set)
    __swig_setmethods__["DatOverflow"] = lib_ohpi.SaHpiDomainInfoT_DatOverflow_set
    __swig_getmethods__["DatOverflow"] = lib_ohpi.SaHpiDomainInfoT_DatOverflow_get
    if _newclass:DatOverflow = property(lib_ohpi.SaHpiDomainInfoT_DatOverflow_get, lib_ohpi.SaHpiDomainInfoT_DatOverflow_set)
    __swig_setmethods__["Guid"] = lib_ohpi.SaHpiDomainInfoT_Guid_set
    __swig_getmethods__["Guid"] = lib_ohpi.SaHpiDomainInfoT_Guid_get
    if _newclass:Guid = property(lib_ohpi.SaHpiDomainInfoT_Guid_get, lib_ohpi.SaHpiDomainInfoT_Guid_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiDomainInfoT, 'this', lib_ohpi.new_SaHpiDomainInfoT(*args))
        _swig_setattr(self, SaHpiDomainInfoT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiDomainInfoT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiDomainInfoTPtr(SaHpiDomainInfoT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiDomainInfoT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiDomainInfoT, 'thisown', 0)
        _swig_setattr(self, SaHpiDomainInfoT,self.__class__,SaHpiDomainInfoT)
lib_ohpi.SaHpiDomainInfoT_swigregister(SaHpiDomainInfoTPtr)

class SaHpiDrtEntryT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiDrtEntryT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiDrtEntryT, name)
    def __repr__(self):
        return "<C SaHpiDrtEntryT instance at %s>" % (self.this,)
    __swig_setmethods__["EntryId"] = lib_ohpi.SaHpiDrtEntryT_EntryId_set
    __swig_getmethods__["EntryId"] = lib_ohpi.SaHpiDrtEntryT_EntryId_get
    if _newclass:EntryId = property(lib_ohpi.SaHpiDrtEntryT_EntryId_get, lib_ohpi.SaHpiDrtEntryT_EntryId_set)
    __swig_setmethods__["DomainId"] = lib_ohpi.SaHpiDrtEntryT_DomainId_set
    __swig_getmethods__["DomainId"] = lib_ohpi.SaHpiDrtEntryT_DomainId_get
    if _newclass:DomainId = property(lib_ohpi.SaHpiDrtEntryT_DomainId_get, lib_ohpi.SaHpiDrtEntryT_DomainId_set)
    __swig_setmethods__["IsPeer"] = lib_ohpi.SaHpiDrtEntryT_IsPeer_set
    __swig_getmethods__["IsPeer"] = lib_ohpi.SaHpiDrtEntryT_IsPeer_get
    if _newclass:IsPeer = property(lib_ohpi.SaHpiDrtEntryT_IsPeer_get, lib_ohpi.SaHpiDrtEntryT_IsPeer_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiDrtEntryT, 'this', lib_ohpi.new_SaHpiDrtEntryT(*args))
        _swig_setattr(self, SaHpiDrtEntryT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiDrtEntryT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiDrtEntryTPtr(SaHpiDrtEntryT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiDrtEntryT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiDrtEntryT, 'thisown', 0)
        _swig_setattr(self, SaHpiDrtEntryT,self.__class__,SaHpiDrtEntryT)
lib_ohpi.SaHpiDrtEntryT_swigregister(SaHpiDrtEntryTPtr)

class SaHpiAlarmT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiAlarmT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiAlarmT, name)
    def __repr__(self):
        return "<C SaHpiAlarmT instance at %s>" % (self.this,)
    __swig_setmethods__["AlarmId"] = lib_ohpi.SaHpiAlarmT_AlarmId_set
    __swig_getmethods__["AlarmId"] = lib_ohpi.SaHpiAlarmT_AlarmId_get
    if _newclass:AlarmId = property(lib_ohpi.SaHpiAlarmT_AlarmId_get, lib_ohpi.SaHpiAlarmT_AlarmId_set)
    __swig_setmethods__["Timestamp"] = lib_ohpi.SaHpiAlarmT_Timestamp_set
    __swig_getmethods__["Timestamp"] = lib_ohpi.SaHpiAlarmT_Timestamp_get
    if _newclass:Timestamp = property(lib_ohpi.SaHpiAlarmT_Timestamp_get, lib_ohpi.SaHpiAlarmT_Timestamp_set)
    __swig_setmethods__["Severity"] = lib_ohpi.SaHpiAlarmT_Severity_set
    __swig_getmethods__["Severity"] = lib_ohpi.SaHpiAlarmT_Severity_get
    if _newclass:Severity = property(lib_ohpi.SaHpiAlarmT_Severity_get, lib_ohpi.SaHpiAlarmT_Severity_set)
    __swig_setmethods__["Acknowledged"] = lib_ohpi.SaHpiAlarmT_Acknowledged_set
    __swig_getmethods__["Acknowledged"] = lib_ohpi.SaHpiAlarmT_Acknowledged_get
    if _newclass:Acknowledged = property(lib_ohpi.SaHpiAlarmT_Acknowledged_get, lib_ohpi.SaHpiAlarmT_Acknowledged_set)
    __swig_setmethods__["AlarmCond"] = lib_ohpi.SaHpiAlarmT_AlarmCond_set
    __swig_getmethods__["AlarmCond"] = lib_ohpi.SaHpiAlarmT_AlarmCond_get
    if _newclass:AlarmCond = property(lib_ohpi.SaHpiAlarmT_AlarmCond_get, lib_ohpi.SaHpiAlarmT_AlarmCond_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiAlarmT, 'this', lib_ohpi.new_SaHpiAlarmT(*args))
        _swig_setattr(self, SaHpiAlarmT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiAlarmT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiAlarmTPtr(SaHpiAlarmT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiAlarmT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiAlarmT, 'thisown', 0)
        _swig_setattr(self, SaHpiAlarmT,self.__class__,SaHpiAlarmT)
lib_ohpi.SaHpiAlarmT_swigregister(SaHpiAlarmTPtr)

SAHPI_EL_OVERFLOW_DROP = lib_ohpi.SAHPI_EL_OVERFLOW_DROP
SAHPI_EL_OVERFLOW_OVERWRITE = lib_ohpi.SAHPI_EL_OVERFLOW_OVERWRITE
class SaHpiEventLogInfoT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiEventLogInfoT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiEventLogInfoT, name)
    def __repr__(self):
        return "<C SaHpiEventLogInfoT instance at %s>" % (self.this,)
    __swig_setmethods__["Entries"] = lib_ohpi.SaHpiEventLogInfoT_Entries_set
    __swig_getmethods__["Entries"] = lib_ohpi.SaHpiEventLogInfoT_Entries_get
    if _newclass:Entries = property(lib_ohpi.SaHpiEventLogInfoT_Entries_get, lib_ohpi.SaHpiEventLogInfoT_Entries_set)
    __swig_setmethods__["Size"] = lib_ohpi.SaHpiEventLogInfoT_Size_set
    __swig_getmethods__["Size"] = lib_ohpi.SaHpiEventLogInfoT_Size_get
    if _newclass:Size = property(lib_ohpi.SaHpiEventLogInfoT_Size_get, lib_ohpi.SaHpiEventLogInfoT_Size_set)
    __swig_setmethods__["UserEventMaxSize"] = lib_ohpi.SaHpiEventLogInfoT_UserEventMaxSize_set
    __swig_getmethods__["UserEventMaxSize"] = lib_ohpi.SaHpiEventLogInfoT_UserEventMaxSize_get
    if _newclass:UserEventMaxSize = property(lib_ohpi.SaHpiEventLogInfoT_UserEventMaxSize_get, lib_ohpi.SaHpiEventLogInfoT_UserEventMaxSize_set)
    __swig_setmethods__["UpdateTimestamp"] = lib_ohpi.SaHpiEventLogInfoT_UpdateTimestamp_set
    __swig_getmethods__["UpdateTimestamp"] = lib_ohpi.SaHpiEventLogInfoT_UpdateTimestamp_get
    if _newclass:UpdateTimestamp = property(lib_ohpi.SaHpiEventLogInfoT_UpdateTimestamp_get, lib_ohpi.SaHpiEventLogInfoT_UpdateTimestamp_set)
    __swig_setmethods__["CurrentTime"] = lib_ohpi.SaHpiEventLogInfoT_CurrentTime_set
    __swig_getmethods__["CurrentTime"] = lib_ohpi.SaHpiEventLogInfoT_CurrentTime_get
    if _newclass:CurrentTime = property(lib_ohpi.SaHpiEventLogInfoT_CurrentTime_get, lib_ohpi.SaHpiEventLogInfoT_CurrentTime_set)
    __swig_setmethods__["Enabled"] = lib_ohpi.SaHpiEventLogInfoT_Enabled_set
    __swig_getmethods__["Enabled"] = lib_ohpi.SaHpiEventLogInfoT_Enabled_get
    if _newclass:Enabled = property(lib_ohpi.SaHpiEventLogInfoT_Enabled_get, lib_ohpi.SaHpiEventLogInfoT_Enabled_set)
    __swig_setmethods__["OverflowFlag"] = lib_ohpi.SaHpiEventLogInfoT_OverflowFlag_set
    __swig_getmethods__["OverflowFlag"] = lib_ohpi.SaHpiEventLogInfoT_OverflowFlag_get
    if _newclass:OverflowFlag = property(lib_ohpi.SaHpiEventLogInfoT_OverflowFlag_get, lib_ohpi.SaHpiEventLogInfoT_OverflowFlag_set)
    __swig_setmethods__["OverflowResetable"] = lib_ohpi.SaHpiEventLogInfoT_OverflowResetable_set
    __swig_getmethods__["OverflowResetable"] = lib_ohpi.SaHpiEventLogInfoT_OverflowResetable_get
    if _newclass:OverflowResetable = property(lib_ohpi.SaHpiEventLogInfoT_OverflowResetable_get, lib_ohpi.SaHpiEventLogInfoT_OverflowResetable_set)
    __swig_setmethods__["OverflowAction"] = lib_ohpi.SaHpiEventLogInfoT_OverflowAction_set
    __swig_getmethods__["OverflowAction"] = lib_ohpi.SaHpiEventLogInfoT_OverflowAction_get
    if _newclass:OverflowAction = property(lib_ohpi.SaHpiEventLogInfoT_OverflowAction_get, lib_ohpi.SaHpiEventLogInfoT_OverflowAction_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiEventLogInfoT, 'this', lib_ohpi.new_SaHpiEventLogInfoT(*args))
        _swig_setattr(self, SaHpiEventLogInfoT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiEventLogInfoT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiEventLogInfoTPtr(SaHpiEventLogInfoT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiEventLogInfoT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiEventLogInfoT, 'thisown', 0)
        _swig_setattr(self, SaHpiEventLogInfoT,self.__class__,SaHpiEventLogInfoT)
lib_ohpi.SaHpiEventLogInfoT_swigregister(SaHpiEventLogInfoTPtr)

SAHPI_OLDEST_ENTRY = lib_ohpi.SAHPI_OLDEST_ENTRY
SAHPI_NEWEST_ENTRY = lib_ohpi.SAHPI_NEWEST_ENTRY
SAHPI_NO_MORE_ENTRIES = lib_ohpi.SAHPI_NO_MORE_ENTRIES
class SaHpiEventLogEntryT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaHpiEventLogEntryT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SaHpiEventLogEntryT, name)
    def __repr__(self):
        return "<C SaHpiEventLogEntryT instance at %s>" % (self.this,)
    __swig_setmethods__["EntryId"] = lib_ohpi.SaHpiEventLogEntryT_EntryId_set
    __swig_getmethods__["EntryId"] = lib_ohpi.SaHpiEventLogEntryT_EntryId_get
    if _newclass:EntryId = property(lib_ohpi.SaHpiEventLogEntryT_EntryId_get, lib_ohpi.SaHpiEventLogEntryT_EntryId_set)
    __swig_setmethods__["Timestamp"] = lib_ohpi.SaHpiEventLogEntryT_Timestamp_set
    __swig_getmethods__["Timestamp"] = lib_ohpi.SaHpiEventLogEntryT_Timestamp_get
    if _newclass:Timestamp = property(lib_ohpi.SaHpiEventLogEntryT_Timestamp_get, lib_ohpi.SaHpiEventLogEntryT_Timestamp_set)
    __swig_setmethods__["Event"] = lib_ohpi.SaHpiEventLogEntryT_Event_set
    __swig_getmethods__["Event"] = lib_ohpi.SaHpiEventLogEntryT_Event_get
    if _newclass:Event = property(lib_ohpi.SaHpiEventLogEntryT_Event_get, lib_ohpi.SaHpiEventLogEntryT_Event_set)
    def __init__(self, *args):
        _swig_setattr(self, SaHpiEventLogEntryT, 'this', lib_ohpi.new_SaHpiEventLogEntryT(*args))
        _swig_setattr(self, SaHpiEventLogEntryT, 'thisown', 1)
    def __del__(self, destroy=lib_ohpi.delete_SaHpiEventLogEntryT):
        try:
            if self.thisown: destroy(self)
        except: pass

class SaHpiEventLogEntryTPtr(SaHpiEventLogEntryT):
    def __init__(self, this):
        _swig_setattr(self, SaHpiEventLogEntryT, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SaHpiEventLogEntryT, 'thisown', 0)
        _swig_setattr(self, SaHpiEventLogEntryT,self.__class__,SaHpiEventLogEntryT)
lib_ohpi.SaHpiEventLogEntryT_swigregister(SaHpiEventLogEntryTPtr)


saHpiVersionGet = lib_ohpi.saHpiVersionGet

saHpiSessionOpen = lib_ohpi.saHpiSessionOpen

saHpiSessionClose = lib_ohpi.saHpiSessionClose

saHpiDiscover = lib_ohpi.saHpiDiscover

saHpiDomainInfoGet = lib_ohpi.saHpiDomainInfoGet

saHpiDrtEntryGet = lib_ohpi.saHpiDrtEntryGet

saHpiDomainTagSet = lib_ohpi.saHpiDomainTagSet

saHpiRptEntryGet = lib_ohpi.saHpiRptEntryGet

saHpiRptEntryGetByResourceId = lib_ohpi.saHpiRptEntryGetByResourceId

saHpiResourceSeveritySet = lib_ohpi.saHpiResourceSeveritySet

saHpiResourceTagSet = lib_ohpi.saHpiResourceTagSet

saHpiResourceIdGet = lib_ohpi.saHpiResourceIdGet

saHpiEventLogInfoGet = lib_ohpi.saHpiEventLogInfoGet

saHpiEventLogEntryGet = lib_ohpi.saHpiEventLogEntryGet

saHpiEventLogEntryAdd = lib_ohpi.saHpiEventLogEntryAdd

saHpiEventLogClear = lib_ohpi.saHpiEventLogClear

saHpiEventLogTimeGet = lib_ohpi.saHpiEventLogTimeGet

saHpiEventLogTimeSet = lib_ohpi.saHpiEventLogTimeSet

saHpiEventLogStateGet = lib_ohpi.saHpiEventLogStateGet

saHpiEventLogStateSet = lib_ohpi.saHpiEventLogStateSet

saHpiEventLogOverflowReset = lib_ohpi.saHpiEventLogOverflowReset

saHpiSubscribe = lib_ohpi.saHpiSubscribe

saHpiUnsubscribe = lib_ohpi.saHpiUnsubscribe

saHpiEventGet = lib_ohpi.saHpiEventGet

saHpiEventAdd = lib_ohpi.saHpiEventAdd

saHpiAlarmGetNext = lib_ohpi.saHpiAlarmGetNext

saHpiAlarmGet = lib_ohpi.saHpiAlarmGet

saHpiAlarmAcknowledge = lib_ohpi.saHpiAlarmAcknowledge

saHpiAlarmAdd = lib_ohpi.saHpiAlarmAdd

saHpiAlarmDelete = lib_ohpi.saHpiAlarmDelete

saHpiRdrGet = lib_ohpi.saHpiRdrGet

saHpiRdrGetByInstrumentId = lib_ohpi.saHpiRdrGetByInstrumentId

saHpiSensorReadingGet = lib_ohpi.saHpiSensorReadingGet

saHpiSensorThresholdsGet = lib_ohpi.saHpiSensorThresholdsGet

saHpiSensorThresholdsSet = lib_ohpi.saHpiSensorThresholdsSet

saHpiSensorTypeGet = lib_ohpi.saHpiSensorTypeGet

saHpiSensorEnableGet = lib_ohpi.saHpiSensorEnableGet

saHpiSensorEnableSet = lib_ohpi.saHpiSensorEnableSet

saHpiSensorEventEnableGet = lib_ohpi.saHpiSensorEventEnableGet

saHpiSensorEventEnableSet = lib_ohpi.saHpiSensorEventEnableSet

saHpiSensorEventMasksGet = lib_ohpi.saHpiSensorEventMasksGet

saHpiSensorEventMasksSet = lib_ohpi.saHpiSensorEventMasksSet

saHpiControlTypeGet = lib_ohpi.saHpiControlTypeGet

saHpiControlGet = lib_ohpi.saHpiControlGet

saHpiControlSet = lib_ohpi.saHpiControlSet

saHpiIdrInfoGet = lib_ohpi.saHpiIdrInfoGet

saHpiIdrAreaHeaderGet = lib_ohpi.saHpiIdrAreaHeaderGet

saHpiIdrAreaAdd = lib_ohpi.saHpiIdrAreaAdd

saHpiIdrAreaDelete = lib_ohpi.saHpiIdrAreaDelete

saHpiIdrFieldGet = lib_ohpi.saHpiIdrFieldGet

saHpiIdrFieldAdd = lib_ohpi.saHpiIdrFieldAdd

saHpiIdrFieldSet = lib_ohpi.saHpiIdrFieldSet

saHpiIdrFieldDelete = lib_ohpi.saHpiIdrFieldDelete

saHpiWatchdogTimerGet = lib_ohpi.saHpiWatchdogTimerGet

saHpiWatchdogTimerSet = lib_ohpi.saHpiWatchdogTimerSet

saHpiWatchdogTimerReset = lib_ohpi.saHpiWatchdogTimerReset

saHpiAnnunciatorGetNext = lib_ohpi.saHpiAnnunciatorGetNext

saHpiAnnunciatorGet = lib_ohpi.saHpiAnnunciatorGet

saHpiAnnunciatorAcknowledge = lib_ohpi.saHpiAnnunciatorAcknowledge

saHpiAnnunciatorAdd = lib_ohpi.saHpiAnnunciatorAdd

saHpiAnnunciatorDelete = lib_ohpi.saHpiAnnunciatorDelete

saHpiAnnunciatorModeGet = lib_ohpi.saHpiAnnunciatorModeGet

saHpiAnnunciatorModeSet = lib_ohpi.saHpiAnnunciatorModeSet

saHpiHotSwapPolicyCancel = lib_ohpi.saHpiHotSwapPolicyCancel

saHpiResourceActiveSet = lib_ohpi.saHpiResourceActiveSet

saHpiResourceInactiveSet = lib_ohpi.saHpiResourceInactiveSet

saHpiAutoInsertTimeoutGet = lib_ohpi.saHpiAutoInsertTimeoutGet

saHpiAutoInsertTimeoutSet = lib_ohpi.saHpiAutoInsertTimeoutSet

saHpiAutoExtractTimeoutGet = lib_ohpi.saHpiAutoExtractTimeoutGet

saHpiAutoExtractTimeoutSet = lib_ohpi.saHpiAutoExtractTimeoutSet

saHpiHotSwapStateGet = lib_ohpi.saHpiHotSwapStateGet

saHpiHotSwapActionRequest = lib_ohpi.saHpiHotSwapActionRequest

saHpiHotSwapIndicatorStateGet = lib_ohpi.saHpiHotSwapIndicatorStateGet

saHpiHotSwapIndicatorStateSet = lib_ohpi.saHpiHotSwapIndicatorStateSet

saHpiParmControl = lib_ohpi.saHpiParmControl

saHpiResourceResetStateGet = lib_ohpi.saHpiResourceResetStateGet

saHpiResourceResetStateSet = lib_ohpi.saHpiResourceResetStateSet

saHpiResourcePowerStateGet = lib_ohpi.saHpiResourcePowerStateGet

saHpiResourcePowerStateSet = lib_ohpi.saHpiResourcePowerStateSet

And = lib_ohpi.And
Or = lib_ohpi.Or
Not = lib_ohpi.Not
StrTime = lib_ohpi.StrTime
oh_get_default_domain_id = lib_ohpi.oh_get_default_domain_id

oh_lookup_language = lib_ohpi.oh_lookup_language
oh_lookup_texttype = lib_ohpi.oh_lookup_texttype
oh_lookup_entitytype = lib_ohpi.oh_lookup_entitytype
oh_lookup_sensortype = lib_ohpi.oh_lookup_sensortype
oh_lookup_sensorreadingtype = lib_ohpi.oh_lookup_sensorreadingtype
oh_lookup_sensoreventmaskaction = lib_ohpi.oh_lookup_sensoreventmaskaction
oh_lookup_sensorunits = lib_ohpi.oh_lookup_sensorunits
oh_lookup_sensormodunituse = lib_ohpi.oh_lookup_sensormodunituse
oh_lookup_sensoreventctrl = lib_ohpi.oh_lookup_sensoreventctrl
oh_lookup_ctrltype = lib_ohpi.oh_lookup_ctrltype
oh_lookup_ctrlstatedigital = lib_ohpi.oh_lookup_ctrlstatedigital
oh_lookup_ctrlmode = lib_ohpi.oh_lookup_ctrlmode
oh_lookup_ctrloutputtype = lib_ohpi.oh_lookup_ctrloutputtype
oh_lookup_idrareatype = lib_ohpi.oh_lookup_idrareatype
oh_lookup_idrfieldtype = lib_ohpi.oh_lookup_idrfieldtype
oh_lookup_watchdogaction = lib_ohpi.oh_lookup_watchdogaction
oh_lookup_watchdogactionevent = lib_ohpi.oh_lookup_watchdogactionevent
oh_lookup_watchdogpretimerinterrupt = lib_ohpi.oh_lookup_watchdogpretimerinterrupt
oh_lookup_watchdogtimeruse = lib_ohpi.oh_lookup_watchdogtimeruse
oh_lookup_hsindicatorstate = lib_ohpi.oh_lookup_hsindicatorstate
oh_lookup_hsaction = lib_ohpi.oh_lookup_hsaction
oh_lookup_hsstate = lib_ohpi.oh_lookup_hsstate
oh_lookup_severity = lib_ohpi.oh_lookup_severity
oh_lookup_resourceeventtype = lib_ohpi.oh_lookup_resourceeventtype
oh_lookup_domaineventtype = lib_ohpi.oh_lookup_domaineventtype
oh_lookup_sweventtype = lib_ohpi.oh_lookup_sweventtype
oh_lookup_eventtype = lib_ohpi.oh_lookup_eventtype
oh_lookup_statuscondtype = lib_ohpi.oh_lookup_statuscondtype
oh_lookup_annunciatormode = lib_ohpi.oh_lookup_annunciatormode
oh_lookup_annunciatortype = lib_ohpi.oh_lookup_annunciatortype
oh_lookup_rdrtype = lib_ohpi.oh_lookup_rdrtype
oh_lookup_parmaction = lib_ohpi.oh_lookup_parmaction
oh_lookup_resetaction = lib_ohpi.oh_lookup_resetaction
oh_lookup_powerstate = lib_ohpi.oh_lookup_powerstate
oh_lookup_eventlogoverflowaction = lib_ohpi.oh_lookup_eventlogoverflowaction
oh_lookup_error = lib_ohpi.oh_lookup_error
oh_lookup_eventcategory = lib_ohpi.oh_lookup_eventcategory

oh_lookup_eventcatstate = lib_ohpi.oh_lookup_eventcatstate


