unix {
    OPENHPI_PREFIX = /usr/local
    PREFIX = /usr/local
}

win32 {
    OPENHPI_PREFIX = ./openhpi-3.1.0-win32-x86
    PREFIX = ./hpibrowser-3.1.1-win32-x86
}

TARGET = hpibrowser
OUTPUT_DIR = .output

####################################################
# Not recommended to change the lines below
####################################################
TEMPLATE = app
OBJECTS_DIR = $$OUTPUT_DIR
MOC_DIR = $$OUTPUT_DIR
RCC_DIR = $$OUTPUT_DIR
INCLUDEPATH += ./include

unix {
    INCLUDEPATH += $$OPENHPI_PREFIX/include/openhpi
    LIBS += -L$$OPENHPI_PREFIX/lib -lopenhpi
}

win32 {
    INCLUDEPATH += $$OPENHPI_PREFIX
    LIBS += -L$$OPENHPI_PREFIX -lopenhpi
}

RESOURCES = application.qrc

unix {
    target.path = $$PREFIX/bin
}

win32 {
    target.path = $$PREFIX
}

INSTALLS += target

# Input
HEADERS += include/HpiInfo.h \
           include/HpiAction.h \
           include/HpiEntry.h \
           include/HpiProvider.h \
           include/HpiSubProvider.h \
           include/OHpi.h \
           include/Hpi.h \
           include/View.h \
           include/DomainSelector.h \
           include/MainWindow.h \
           include/OHpiUtils.h \
           include/HpiUtils.h \
           provider/HpiSubProviderUnknown.h \
           provider/HpiSubProviderDomain.h \
           provider/HpiSubProviderDRT.h \
           provider/HpiSubProviderRPT.h \
           provider/HpiSubProviderDET.h \
           provider/HpiSubProviderLog.h \
           provider/HpiSubProviderDAT.h \
           provider/HpiSubProviderResource.h \ 
           provider/HpiSubProviderAlarm.h \ 
           provider/HpiSubProviderLogEntry.h \
           provider/HpiSubProviderEntity.h \
           provider/HpiSubProviderControl.h \ 
           provider/HpiSubProviderSensor.h \ 
           provider/HpiSubProviderIdr.h \
           provider/HpiSubProviderWatchdog.h \
           provider/HpiSubProviderAnnunciator.h \
           provider/HpiSubProviderDIMI.h \
           provider/HpiSubProviderFUMI.h \
           provider/HpiSubProviderHotSwap.h \
           provider/HpiSubProviderReset.h \ 
           provider/HpiSubProviderPower.h \
           provider/HpiSubProviderIdrArea.h \
           provider/HpiSubProviderAnnouncement.h \
           provider/HpiSubProviderDIMITest.h \
           provider/HpiSubProviderFUMIBank.h \
           provider/HpiSubProviderIdrField.h \
           provider/HpiSubProviderFUMIComponent.h \
           provider/HpiSubProviderFUMISource.h \
           provider/HpiSubProviderFUMISourceComponent.h \
           provider/CommonHpiSubProviderFUMI.h \
           ui/IconCache.h \
           ui/RollupButton.h \
           ui/InfoWidget.h \
           ui/ActionsWidget.h \
           ui/EntriesWidget.h 

SOURCES += main.cpp \
           provider/HpiInfo.cpp \
           provider/OHpi.cpp \
           provider/Hpi.cpp \
           provider/HpiSubProviderUnknown.cpp \
           provider/HpiSubProviderDomain.cpp \
           provider/HpiSubProviderDRT.cpp \
           provider/HpiSubProviderRPT.cpp \
           provider/HpiSubProviderDET.cpp \
           provider/HpiSubProviderLog.cpp \
           provider/HpiSubProviderDAT.cpp \
           provider/HpiSubProviderResource.cpp \ 
           provider/HpiSubProviderAlarm.cpp \ 
           provider/HpiSubProviderLogEntry.cpp \
           provider/HpiSubProviderEntity.cpp \
           provider/HpiSubProviderControl.cpp \ 
           provider/HpiSubProviderSensor.cpp \ 
           provider/HpiSubProviderIdr.cpp \
           provider/HpiSubProviderWatchdog.cpp \
           provider/HpiSubProviderAnnunciator.cpp \
           provider/HpiSubProviderDIMI.cpp \
           provider/HpiSubProviderFUMI.cpp \
           provider/HpiSubProviderHotSwap.cpp \
           provider/HpiSubProviderReset.cpp \ 
           provider/HpiSubProviderPower.cpp \
           provider/HpiSubProviderIdrArea.cpp \
           provider/HpiSubProviderAnnouncement.cpp \
           provider/HpiSubProviderDIMITest.cpp \
           provider/HpiSubProviderFUMIBank.cpp \
           provider/HpiSubProviderIdrField.cpp \
           provider/HpiSubProviderFUMIComponent.cpp \
           provider/HpiSubProviderFUMISource.cpp \
           provider/HpiSubProviderFUMISourceComponent.cpp \
           provider/CommonHpiSubProviderFUMI.cpp \
           ui/IconCache.cpp \
           ui/DomainSelector.cpp \
           ui/MainWindow.cpp \
           ui/RollupButton.cpp \
           ui/InfoWidget.cpp \
           ui/ActionsWidget.cpp \
           ui/EntriesWidget.cpp \
           utils/OHpiUtils.cpp \
           utils/HpiUtils.cpp

