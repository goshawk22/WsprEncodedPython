#!/usr/bin/env -S python

import sys
import WsprEncodedPython


codec = WsprEncodedPython.WsprMessageTelemetryExtendedCommon()


def TryDecode(callsign, grid4, powerDbm):
    codec.Reset()
    codec.SetCallsign(callsign)
    codec.SetGrid4(grid4)
    codec.SetPowerDbm(powerDbm)

    print(f"Testing {callsign}, {grid4}, {powerDbm}")
    print("------------------------")
    if codec.Decode():
        print("Decode success - This is identified as Extended Telemetry")
        print(f"HdrTelemetryType: {codec.GetHdrTelemetryType()}")
        print(f"HdrRESERVED:      {codec.GetHdrRESERVED()}")
        print(f"HdrType:          {codec.GetHdrType()}")
        print(f"HdrSlot:          {codec.GetHdrSlot()}")
    else:
        print("Decode failure - This is not identified as Extended Telemetry")
    
    print()


print()

TryDecode("036KVF", "PP73", 30) # known-good extended telemetry
TryDecode("QZ0VXT", "AO08", 20) # known-bad data which decodes as extended telemetry anyway
TryDecode("1Y4PAS", "HK08", 10) # known basic telemetry
