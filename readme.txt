aprs - weewx extension for generating APRS-compliant packets

This weewx[1] extension allows the generation of APRS-compliant packets
containing weather information collected by weewx.
This extension was written for the purpose of easy integration with aprx[2].
When this extension is enabled, weewx will generate a new APRS packet every
StdArchive.archive_interval seconds.

Installation:
    wee_extension --install aprs.tar.gz

Configuration:
    [APRS]
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

Example of integration in the aprx configuration:
    <beacon>
    beaconmode both  # Send packet via APRS-IS and radio.
    cycle-size  5m
    beacon srccall N0CALL-1 via WIDE2-1 file "/dev/shm/aprs.pkt"
    </beacon>

Note: this configuration has the problem that aprx and weewx are not
syncronized, so aprx may send out the same packet twice or miss one from time
to time.


[1] http://www.weewx.com/
[2] http://thelifeofkenneth.com/aprx/
