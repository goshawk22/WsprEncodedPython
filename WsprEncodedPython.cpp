#include "WsprEncodedDynamic.h"
#include "pybind11/pybind11.h"

namespace py = pybind11;



PYBIND11_MODULE(WsprEncodedPython, m) {




    /////////////////////////////////////////////////////////////////
    // WsprMessageTelemetryExtendedCommon
    /////////////////////////////////////////////////////////////////

    using MsgCD = WsprMessageTelemetryExtendedCommonDynamic<29>;
    
    py::class_<MsgCD> msgCD(m, "WsprMessageTelemetryExtendedCommon");

    msgCD.def(py::init<>());

    msgCD.def("Reset",               &MsgCD::Reset);
    msgCD.def("SetCallsign",         &MsgCD::SetCallsign);
    msgCD.def("GetCallsign",         &MsgCD::GetCallsign);
    msgCD.def("SetGrid4",            &MsgCD::SetGrid4);
    msgCD.def("GetGrid4",            &MsgCD::GetGrid4);
    msgCD.def("SetPowerDbm",         &MsgCD::SetPowerDbm);
    msgCD.def("GetPowerDbm",         &MsgCD::GetPowerDbm);
    msgCD.def("GetPowerDbm",         &MsgCD::GetPowerDbm);

    msgCD.def("ResetEverything",     &MsgCD::ResetEverything);
    msgCD.def("DefineField",         &MsgCD::DefineField);
    msgCD.def("GetDefineFieldErr",   &MsgCD::GetDefineFieldErr);
    msgCD.def("Set",                 &MsgCD::Set);
    msgCD.def("Get",                 &MsgCD::Get);
    
    msgCD.def("SetId13",             &MsgCD::SetId13);
    msgCD.def("GetId13",             &MsgCD::GetId13);
    msgCD.def("GetHdrTelemetryType", &MsgCD::GetHdrTelemetryType);
    msgCD.def("GetHdrRESERVED",      &MsgCD::GetHdrRESERVED);
    msgCD.def("GetHdrType",          [](MsgCD& self) {
        return static_cast<uint8_t>(self.GetHdrType());
    });
    msgCD.def("SetHdrSlot",          &MsgCD::SetHdrSlot);
    msgCD.def("GetHdrSlot",          &MsgCD::GetHdrSlot);
    msgCD.def("Encode",              &MsgCD::Encode);
    msgCD.def("Decode",              &MsgCD::Decode);


    /////////////////////////////////////////////////////////////////
    // WsprMessageTelemetryExtendedUserDefined
    /////////////////////////////////////////////////////////////////

    using MsgUD = WsprMessageTelemetryExtendedUserDefined<29>;
    
    py::class_<MsgUD> msgUD(m, "WsprMessageTelemetryExtendedUserDefined");

    msgUD.def(py::init<>());

    msgUD.def("Reset",               &MsgUD::Reset);
    msgUD.def("SetCallsign",         &MsgUD::SetCallsign);
    msgUD.def("GetCallsign",         &MsgUD::GetCallsign);
    msgUD.def("SetGrid4",            &MsgUD::SetGrid4);
    msgUD.def("GetGrid4",            &MsgUD::GetGrid4);
    msgUD.def("SetPowerDbm",         &MsgUD::SetPowerDbm);
    msgUD.def("GetPowerDbm",         &MsgUD::GetPowerDbm);
    msgUD.def("GetPowerDbm",         &MsgUD::GetPowerDbm);

    msgUD.def("ResetEverything",     &MsgUD::ResetEverything);
    msgUD.def("DefineField",         &MsgUD::DefineField);
    msgUD.def("GetDefineFieldErr",   &MsgUD::GetDefineFieldErr);
    msgUD.def("Set",                 &MsgUD::Set);
    msgUD.def("Get",                 &MsgUD::Get);
    
    msgUD.def("SetId13",             &MsgUD::SetId13);
    msgUD.def("GetId13",             &MsgUD::GetId13);
    msgUD.def("GetHdrTelemetryType", &MsgUD::GetHdrTelemetryType);
    msgUD.def("GetHdrRESERVED",      &MsgUD::GetHdrRESERVED);
    msgUD.def("SetHdrSlot",          &MsgUD::SetHdrSlot);
    msgUD.def("GetHdrSlot",          &MsgUD::GetHdrSlot);
    msgUD.def("Encode",              &MsgUD::Encode);
    msgUD.def("Decode",              &MsgUD::Decode);






}
