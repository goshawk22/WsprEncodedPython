#!/usr/bin/env -S python -u

import sys
import WsprEncodedPython

def test_basic_telemetry_roundtrip():
    """Test encoding and then decoding basic telemetry to verify round-trip functionality"""
    
    print("WSPR Basic Telemetry Round-Trip Test")
    print("====================================")
    
    # Create two separate codec instances for encoding and decoding
    encoder = WsprEncodedPython.WsprMessageTelemetryBasic()
    decoder = WsprEncodedPython.WsprMessageTelemetryBasic()
    
    # Set up test data
    test_data = {
        "id13": "1B",
        "grid56": "MN", 
        "altitude": 1500,
        "temperature": 25,
        "voltage": 3.85,
        "speed": 12,
        "gps_valid": True
    }
    
    print(f"\nOriginal Data:")
    print(f"-------------")
    for key, value in test_data.items():
        print(f"{key:12}: {value}")
    
    # Encode the data
    encoder.SetId13(test_data["id13"])
    encoder.SetGrid56(test_data["grid56"])
    encoder.SetAltitudeMeters(test_data["altitude"])
    encoder.SetTemperatureCelsius(test_data["temperature"])
    encoder.SetVoltageVolts(test_data["voltage"])
    encoder.SetSpeedKnots(test_data["speed"])
    encoder.SetGpsIsValid(test_data["gps_valid"])
    
    encoder.Encode()
    
    # Get encoded WSPR message
    callsign = encoder.GetCallsign()
    grid4 = encoder.GetGrid4()
    powerDbm = encoder.GetPowerDbm()
    
    print(f"\nEncoded WSPR Message:")
    print(f"--------------------")
    print(f"Callsign: {callsign}")
    print(f"Grid4   : {grid4}")
    print(f"PowerDbm: {powerDbm}")
    
    # Decode the message using the second codec instance
    decoder.SetCallsign(callsign)
    decoder.SetGrid4(grid4)
    decoder.SetPowerDbm(powerDbm)
    
    if decoder.Decode():
        print(f"\nDecoded Data:")
        print(f"------------")
        print(f"id13        : {decoder.GetId13()}")
        print(f"grid56      : {decoder.GetGrid56()}")
        print(f"altitude    : {decoder.GetAltitudeMeters()}")
        print(f"temperature : {decoder.GetTemperatureCelsius()}")
        print(f"voltage     : {decoder.GetVoltageVolts():.2f}")
        print(f"speed       : {decoder.GetSpeedKnots()}")
        print(f"gps_valid   : {decoder.GetGpsIsValid()}")
        
        # Verify data integrity
        print(f"\nData Integrity Check:")
        print(f"--------------------")
        checks = []
        checks.append(("ID13", test_data["id13"], decoder.GetId13()))
        checks.append(("Grid56", test_data["grid56"], decoder.GetGrid56()))
        checks.append(("Altitude", test_data["altitude"], decoder.GetAltitudeMeters()))
        checks.append(("Temperature", test_data["temperature"], decoder.GetTemperatureCelsius()))
        checks.append(("Voltage", test_data["voltage"], decoder.GetVoltageVolts()))
        checks.append(("Speed", test_data["speed"], decoder.GetSpeedKnots()))
        checks.append(("GPS Valid", test_data["gps_valid"], decoder.GetGpsIsValid()))
        
        all_passed = True
        for name, original, decoded in checks:
            if isinstance(original, float):
                # Allow small floating point differences
                passed = abs(original - decoded) < 0.01
            else:
                passed = original == decoded
            
            status = "✓ PASS" if passed else "✗ FAIL"
            print(f"{name:12}: {status}")
            if not passed:
                print(f"              Expected: {original}, Got: {decoded}")
                all_passed = False
        
        print(f"\nOverall Result: {'✓ ALL TESTS PASSED' if all_passed else '✗ SOME TESTS FAILED'}")
        
    else:
        print(f"\n✗ Decode failed - unable to decode the encoded message")

def test_invalid_basic_telemetry():
    """Test decoding of non-basic telemetry messages"""
    
    print(f"\n\nInvalid Basic Telemetry Test")
    print(f"============================")
    
    decoder = WsprEncodedPython.WsprMessageTelemetryBasic()
    
    # Test with extended telemetry data (should fail)
    decoder.SetCallsign("036KVF")  # Known extended telemetry
    decoder.SetGrid4("PP73")
    decoder.SetPowerDbm(30)
    
    print(f"Testing extended telemetry message:")
    print(f"Callsign: 036KVF, Grid4: PP73, PowerDbm: 30")
    
    if decoder.Decode():
        print(f"✗ Unexpected: Extended telemetry decoded as basic telemetry")
    else:
        print(f"✓ Expected: Extended telemetry correctly rejected")

if __name__ == "__main__":
    test_basic_telemetry_roundtrip()
    test_invalid_basic_telemetry()
