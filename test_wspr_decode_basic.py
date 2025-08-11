#!/usr/bin/env -S python -u

import sys
import WsprEncodedPython

# Create Basic Telemetry object
codecBasic = WsprEncodedPython.WsprMessageTelemetryBasic()

#################################################################
# Get encoded WSPR message fields (sourced elsewhere)
#################################################################

# Example encoded message data from a basic telemetry transmission
codecBasic.SetCallsign("1B4PAS")  # Example callsign from basic telemetry
codecBasic.SetGrid4("HK08")       # Example grid from basic telemetry
codecBasic.SetPowerDbm(10)        # Example power from basic telemetry

#################################################################
# Decode
#################################################################

if codecBasic.Decode():
    print(f"Basic Telemetry Decoded Data")
    print(f"=============================")
    print(f"Decode successful!")
    print()
    print(f"Decoded Values:")
    print(f"--------------")
    print(f"ID13            : {codecBasic.GetId13()}")
    print(f"Grid56          : {codecBasic.GetGrid56()}")
    print(f"Altitude (m)    : {codecBasic.GetAltitudeMeters()}")
    print(f"Temperature (°C): {codecBasic.GetTemperatureCelsius()}")
    print(f"Voltage (V)     : {codecBasic.GetVoltageVolts():.2f}")
    print(f"Speed (knots)   : {codecBasic.GetSpeedKnots()}")
    print(f"GPS Valid       : {codecBasic.GetGpsIsValid()}")
    print()
    print(f"Original WSPR Message:")
    print(f"---------------------")
    print(f"Callsign: {codecBasic.GetCallsign()}")
    print(f"Grid4   : {codecBasic.GetGrid4()}")
    print(f"PowerDbm: {codecBasic.GetPowerDbm()}")
else:
    print(f"Basic Telemetry Decode Failed")
    print(f"=============================")
    print(f"The provided WSPR message does not appear to be basic telemetry format.")
    print()
    print(f"Input WSPR Message:")
    print(f"------------------")
    print(f"Callsign: {codecBasic.GetCallsign()}")
    print(f"Grid4   : {codecBasic.GetGrid4()}")
    print(f"PowerDbm: {codecBasic.GetPowerDbm()}")
