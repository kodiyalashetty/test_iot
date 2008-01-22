from distutils.core import setup, Extension

setup(name='hpiview2',
      version='1.0',
      description='GUI interface to OpenHPI',
      author='Jayashree Padmanabhan',
      author_email='jayshree@in.ibm.com',
      url='http://www.openhpi.org',
      #py_modules=[
      #	'ControlPref',
#	'CustomEvent',
#	'eventGetThread',
#	'FrmHelpAbout',
#	'hpiview_callbacks',
#	'hpiview_window',
#	'InventoryPref',
#	'PrefEvtLogTimestamp',
#	'ResEventLog',
#	'ResourcePref',
#	'SensorPref',
#	'WatchDogPref'
#	],
      packages=['openhpi_view'],
      scripts=['hpiview.py']
     )

