# aprs - weewx extension for generating APRS-compliant packets
![alt text](img/aprs.png)![alt text](img/handshake.png)  ![alt text](img/weewx.jpg)  
This [weeWX](https://www.weewx.com/) extension allows the generation of APRS-compliant packets
containing weather information collected by weewx.
This extension was written for the purpose of easy integration with [aprx](http://thelifeofkenneth.com/aprx/).
When this extension is enabled, weewx will generate a new APRS packet every
StdArchive.archive_interval seconds.

# Installation:
> wee_extension --install aprs.tar.gz

# Configuration [WeeWX]: 
#### Add these to your weewx.conf - likely in /etc/weewx/
        # The APRS weather packet payload will be written in output_filename
        output_filename = /dev/shm/aprs.pkt
        # include_position:
        # 0: a positionless weather report will be generated (default)
        # 1: a weather report with position will be generated
        include_position = 1
        # In case of a position packet, symbol_table and symbol_code will
        # determine what symbol will be used to display the station (e.g. on
        # aprs.fi). "/_" is the default and will generate a blue WX icon.
        # A positionless packet does not include a symbol specification and
        # these two settings will be ignored
        symbol_table = /
        symbol_code = _
        # The string in comment will be appended to the end of the packet.
        comment = ''
        # If Acurite 01036, put accurite
        station_model = default
        report_luminosity = 0

# Configuration  [APRX]:
#### Add these to your aprx.conf - likely in /etc/
        Example of integration in the aprx configuration:
            <beacon>
            beaconmode both  # Send packet via APRS-IS and radio.
            cycle-size  5m
            beacon srccall N0CALL-1 via WIDE2-1 file "/dev/shm/aprs.pkt"
            </beacon>

Note: this configuration has the problem that aprx and weewx are not
syncronized, so aprx may send out the same packet twice or miss one from time
to time.

### When all is said and done, the packet should look something like this.
![alt text](/img/image.png)

# How is the weather data coded into the data packet?  

When you look at examples of APRS position weather packets [here](http://wxqa.com/callsminmax/index_callsminmax.html), or [here](http://wxqa.com/activecwd/index_activecwd.html), the part after the longitude "E" or "W" carries the weather data as symbols followed by numbers.   


@060151z3316.04<b>N</b>/09631.96<b>W</b><b>_</b>120<b>/</b>005<b>g</b>010<b>t</b>021<b>r</b>000<b>p</b>000<b>P</b>000<b>h</b>75<b>b</b>10322
- The part after the longitude "E" or "W" carries the weather data as symbols followed by numbers. - 3316.04N/09631.96W
- The underscore "_" followed by 3 numbers represents wind direction in degrees from true north. This is the direction that the wind is blowing from. - _120
- The slash "/" followed by 3 numbers represents the average wind speed in miles per hour. - /005
- The letter "g" followed by 3 numbers represents the peak instaneous value of wind in miles per hour. - g010
- The letter "t" followed by 3 characters (numbers and minus sign) represents the temperature in degrees F. - t021
- The letter "r" followed by 3 numbers represents the amount of rain in hundredths of inches that fell the past hour. - r000
- The letter "p" followed by 3 numbers represents the amount of rain in hundredths of inches that fell in the past 24 hours. Only these two precipitation values are accepted by MADIS. - p000
- The letter "P" followed by 3 numbers represents the amount of rain in hundredths of inches that fell since local midnight. - P000
- The letter "b" followed by 5 numbers represents the barometric pressure in tenths of a millibar. - b10322 
- The letter "h" followed by 2 numbers represents the relative humidity in percent, where "h00" implies 100% RH. - h75
- The letter "L" followed by 2-5 numbers represents  watts/meter squared. Conversion is not yet well understood by me.
>So this can be read as: The wind is blowing 120 degrees, the average wind speed is 5mph, the peak wind speed is 10mph, the temperature is 21 degrees, it has rained 0 inches the last hour, it has rained 0 inches the last 24 hours, it has rained 0 inches since local midnight, the pressure is 10322mb, the humidity is 75%

The first four fields (wind direction, wind speed, temperature and gust) are required, in that order, and if a particular measurement is not present, the three numbers should be replaced by "..." to indicate no data available. [Solar radiation data](http://wxqa.com/lum_search.htm) can also be coded into the data packet.

# Tested on:
GW1000/GW1100

---
http://wxqa.com/faq.html  
https://github.com/PhirePhly/aprx  
http://www.weewx.com/  
https://www.weather.gov/cle/CWOP  
http://www.aprs.org/doc/APRS101.PDF  
---