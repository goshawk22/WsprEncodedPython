#include "WsprEncoded.h"
#include "pybind11/pybind11.h"

namespace py = pybind11;



PYBIND11_MODULE(WsprEncodedPython, m) {




    /////////////////////////////////////////////////////////////////
    // WsprMessageTelemetryExtendedUserDefined
    /////////////////////////////////////////////////////////////////

    using MsgUDD = WsprMessageTelemetryExtendedUserDefinedDynamic<29>;
    
    py::class_<MsgUDD> msgUDD(m, "WsprMessageTelemetryExtendedUserDefined");

    msgUDD.def(py::init<>());

    msgUDD.def("Reset",               &MsgUDD::Reset);
    msgUDD.def("SetCallsign",         &MsgUDD::SetCallsign);
    msgUDD.def("GetCallsign",         &MsgUDD::GetCallsign);
    msgUDD.def("SetGrid4",            &MsgUDD::SetGrid4);
    msgUDD.def("GetGrid4",            &MsgUDD::GetGrid4);
    msgUDD.def("SetPowerDbm",         &MsgUDD::SetPowerDbm);
    msgUDD.def("GetPowerDbm",         &MsgUDD::GetPowerDbm);
    msgUDD.def("GetPowerDbm",         &MsgUDD::GetPowerDbm);

    msgUDD.def("ResetEverything",     &MsgUDD::ResetEverything);
    msgUDD.def("DefineField",         &MsgUDD::DefineField);
    msgUDD.def("GetDefineFieldErr",   &MsgUDD::GetDefineFieldErr);
    msgUDD.def("Set",                 &MsgUDD::Set);
    msgUDD.def("Get",                 &MsgUDD::Get);
    
    msgUDD.def("SetId13",             &MsgUDD::SetId13);
    msgUDD.def("GetId13",             &MsgUDD::GetId13);
    msgUDD.def("GetHdrTelemetryType", &MsgUDD::GetHdrTelemetryType);
    msgUDD.def("GetHdrRESERVED",      &MsgUDD::GetHdrRESERVED);
    msgUDD.def("SetHdrSlot",          &MsgUDD::SetHdrSlot);
    msgUDD.def("GetHdrSlot",          &MsgUDD::GetHdrSlot);
    msgUDD.def("Encode",              &MsgUDD::Encode);
    msgUDD.def("Decode",              &MsgUDD::Decode);






}
