#!/usr/bin/env -S python -u

import sys
import WsprEncodedPython

# Create Basic Telemetry object
codecBasic = WsprEncodedPython.WsprMessageTelemetryBasic()

#################################################################
# Set identification
#################################################################

# Set the ID13 (tracker identifier)
codecBasic.SetId13("1B")  # Example tracker ID

#################################################################
# Set telemetry fields
#################################################################

# Grid square extension (5th and 6th characters)
# Valid values are 'A' through 'X' for each character
codecBasic.SetGrid56("MN")

# Altitude in meters (0 through 21,340, steps of 20)
codecBasic.SetAltitudeMeters(1500)

# Temperature in Celsius (-50 through 39)
codecBasic.SetTemperatureCelsius(25)

# Voltage in volts (3.0v through 4.95v, steps of 0.05v)
codecBasic.SetVoltageVolts(3.85)

# Speed in knots (0 through 82, steps of 2)
codecBasic.SetSpeedKnots(12)

# GPS validity flag
codecBasic.SetGpsIsValid(True)

#################################################################
# Encode the data in preparation to transmit
#################################################################

codecBasic.Encode()

#################################################################
# Extract the now-encoded WSPR message fields
#################################################################

callsign = codecBasic.GetCallsign()
grid4    = codecBasic.GetGrid4()
powerDbm = codecBasic.GetPowerDbm()

print(f"Basic Telemetry Encoded Data")
print(f"=============================")
print(f"Callsign: {callsign}")
print(f"Grid4   : {grid4}")
print(f"PowerDbm: {powerDbm}")
print()
print(f"Original Values:")
print(f"---------------")
print(f"ID13            : {codecBasic.GetId13()}")
print(f"Grid56          : {codecBasic.GetGrid56()}")
print(f"Altitude (m)    : {codecBasic.GetAltitudeMeters()}")
print(f"Temperature (°C): {codecBasic.GetTemperatureCelsius()}")
print(f"Voltage (V)     : {codecBasic.GetVoltageVolts():.2f}")
print(f"Speed (knots)   : {codecBasic.GetSpeedKnots()}")
print(f"GPS Valid       : {codecBasic.GetGpsIsValid()}")
