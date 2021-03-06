from GoogleMercatorProjection import LatLng
from PyQt4.QtGui import QColor

# LOCATION(S) 
# Further radar configuration (zoom, marker location) can be completed under the RADAR section
primary_coordinates = 43.745757,-79.601224 # Change to your Lat/Lon

wuprefix = 'http://api.wunderground.com/api/'
wulocation = LatLng(primary_coordinates[0],primary_coordinates[1]) # Location for weather report
primary_location = LatLng(primary_coordinates[0],primary_coordinates[1]) # Default radar location
noaastream = 'http://audioplayer.wunderground.com/SN072A/oshawa.mp3'
background = 'images/bb.jpg'
squares1 = 'images/squares1-green.png'
squares2 = 'images/squares2-green.png'
icons = 'icons-darkgreen'
textcolor = '#206225'
clockface = 'images/clockface3-darkgreen.png'
hourhand = 'images/hourhand-darkgreen.png'
minhand = 'images/minhand-darkgreen.png'
sechand = 'images/sechand-darkgreen.png'

digital = 0             # 1 = Digtal Clock, 0 = Analog Clock
 
digitalcolor = "#154018"            
#digitalformat = "{0:%I:%M\n%S %p}"  # The format of the time
#digitalsize = 200
# The above example shows in this way: https://github.com/n0bel/PiClock/blob/master/Documentation/Digital%20Clock%20v1.jpg
# ( specifications of the time string are documented here: https://docs.python.org/2/library/time.html#time.strftime )

digitalformat = "{0:%I:%M}"
digitalsize = 200
# The above example shows in this way: https://github.com/n0bel/PiClock/blob/master/Documentation/Digital%20Clock%20v2.jpg


metric = 0  #0 = English, 1 = Metric
radar_refresh = 10      # minutes
weather_refresh = 30    # minutes
wind_degrees = 0        # Wind in degrees instead of cardinal 0 = cardinal, 1 = degrees
satellite = 0           # Depreciated: use 'satellite' key in radar section, on a per radar basis
                        # if this is used, all radar blocks will get satellite images
                        

fontattr = 'font-weight: bold; '
dimcolor = QColor('#103125')
dimcolor.setAlpha(192)

brightness = 15

# Language Specific wording
wuLanguage = "EN"   # Weather Undeground Language code (https://www.wunderground.com/weather/api/d/docs?d=language-support&MR=1)
DateLocale = ''  # The Python Locale for date/time (locale.setlocale) -- '' for default Pi Setting
                            # Locales must be installed in your Pi.. to check what is installed
                            # locale -a
                            # to install locales
                            # sudo dpkg-reconfigure locales
LPressure = "Pressure "
LHumidity = "Humidity "
LWind = "Wind "
Lgusting = " gusting "
LFeelslike = "Feels like "
LPrecip1hr = " Precip 1hr:"
LToday = "Today: "
LSunRise = "Sun Rise:"
LSet = " Set: "
LMoonPhase = " Moon Phase:"
LInsideTemp = "Inside Temp "
LRain = " Rain: "
LSnow = " Snow: "


# RADAR
# By default, primary_location entered will be the center and marker of all radar images.
# To update centers/markers, change radar sections below the desired lat/lon as:
# -FROM-
# primary_location,
# -TO-
# LatLng(44.9764016,-93.2486732),
radar1 = {
    'center' : primary_location,  # the center of your radar block
    'zoom' : 7, # this is a google maps zoom factor, bigger = smaller area
    'satellite' : 0,    # 1 => show satellite images instead of radar (colorized IR images)
    'markers' : (   # google maps markers can be overlayed
        {
        'location' : primary_location, 
        'color' : 'red',
        'size' : 'small',
        },          # dangling comma is on purpose.
        )
    }

    
radar2 = {
    'center' : primary_location,
    'zoom' : 11,
    'satellite' : 0,
    'markers' : (
        {
        'location' : primary_location, 
        'color' : 'red',
        'size' : 'small',
        },
        )
    }

    
radar3 = {
    'center' : primary_location, 
    'zoom' : 7,
    'satellite' : 0,
    'markers' : (
        {
        'location' : primary_location, 
        'color' : 'red',
        'size' : 'small',
        },
        )
    }

radar4 = {
    'center' : primary_location, 
    'zoom' : 11,
    'satellite' : 0,
    'markers' : (
        {
        'location' : primary_location, 
        'color' : 'red',
        'size' : 'small',
        },
        )
    }
