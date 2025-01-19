#!/usr/bin/env -S python

import sys

sys.path.append('.')
import WsprEncodedPython


# // Create User-Defined Telemetry object for the number of
# // fields you want, maximum of 29 1-bit fields possible.
codecGpsMsg = WsprEncodedPython.WsprMessageTelemetryExtendedUserDefined()


# /////////////////////////////////////////////////////////////////
# // Define telemetry fields
# /////////////////////////////////////////////////////////////////

# // Define counts of GPS satellites for each constellation type.
# // Values will be clamped between 0 - 128 inclusive.
# // Resolution will be in increments of 4.
codecGpsMsg.DefineField("SatCountUSA",    0, 128, 4)
codecGpsMsg.DefineField("SatCountChina",  0, 128, 4)
codecGpsMsg.DefineField("SatCountRussia", 0, 128, 4)

# // Define a metric for GPS lock times, in seconds.
# // Values will be clamped between 0 - 30 inclusive.
# // Resolution will be in increments of 0.5.
codecGpsMsg.DefineField("LockTimeSecs",    0, 30, 0.5)
codecGpsMsg.DefineField("LockTimeSecsAvg", 0, 30, 0.5)


# /////////////////////////////////////////////////////////////////
# // Get encoded WSPR message fields (sourced elsewhere)
# /////////////////////////////////////////////////////////////////

codecGpsMsg.SetCallsign("036KVF")
codecGpsMsg.SetGrid4("PP73")
codecGpsMsg.SetPowerDbm(30)


# /////////////////////////////////////////////////////////////////
# // Decode
# /////////////////////////////////////////////////////////////////

codecGpsMsg.Decode()


# /////////////////////////////////////////////////////////////////
# // Extract the now-decoded WSPR message fields
# /////////////////////////////////////////////////////////////////

satCountUsa    = codecGpsMsg.Get("SatCountUSA")
satCountChina  = codecGpsMsg.Get("SatCountChina")
satCountRussia = codecGpsMsg.Get("SatCountRussia")

lockTimeSecs    = codecGpsMsg.Get("LockTimeSecs")
lockTimeSecsAvg = codecGpsMsg.Get("LockTimeSecsAvg")

print(f"Encoded data")
print(f"------------")
print(f"satCountUsa    : {satCountUsa}")     # // 12
print(f"satCountChina  : {satCountChina}")   # // 12
print(f"satCountRussia : {satCountRussia}")  # // 0
print(f"lockTimeSecs   : {lockTimeSecs}")    # // 10.5
print(f"lockTimeSecsAvg: {lockTimeSecsAvg}") # // 13