#include "../lib_geometry/XYGrid.h"

#include <pybind11/stl.h>
#include <pybind11/pybind11.h>


namespace py = pybind11;

void init_XYGrid(py::module &m) {
    
    py::class_<XYGrid>(m, "XYGrid")
    .def(py::init())

    .def("getElement", &XYGrid::getElement, py::arg("ix"))
    .def("setVal", &XYGrid::setVal, py::arg("ix"), py::arg("val"))
    .def("getVal", &XYGrid::getVal, py::arg("ix"))

    .def("getSBound", &XYGrid::getSBound)
    .def("getPBound", &XYGrid::getPBound)
    .def("getMinVal", &XYGrid::getMinVal)
    .def("getMaxVal", &XYGrid::getMaxVal)
    .def("size", &XYGrid::size)

    .def("setUtil", &XYGrid::setUtil, py::arg("ix"), py::arg("val"))
    .def("setUtilRange", &XYGrid::setUtilRange, py::arg("lval"), py::arg("hval"))
    .def("getUtil", &XYGrid::getUtil, py::arg("ix"))

    .def("getMinUtil", &XYGrid::getMinUtil)
    .def("getMaxUtil", &XYGrid::getMaxUtil)
    .def("getMaxUtilPoss", &XYGrid::getMaxUtilPoss)
    .def("getMinUtilPoss", &XYGrid::getMinUtilPoss)

    .def("initialize", py::overload_cast<std::string>(&XYGrid::initialize), py::arg("given_config_str"))
    ///.def("initialize", &XYGrid::initialize, py::arg("given_config_str"))
    .def("handleSegment", &XYGrid::handleSegment, py::arg("x1"), py::arg("y1"), py::arg("x2"), py::arg("y2"))
    .def("resetFromMin", &XYGrid::resetFromMin)

    .def("ptIntersect", &XYGrid::ptIntersect, py::arg("x"), py::arg("y"))
    .def("ptIntersectBound", &XYGrid::ptIntersectBound, py::arg("x"), py::arg("y"))
    .def("segIntersectBound", &XYGrid::segIntersectBound, py::arg("x1"), py::arg("y1"), py::arg("x2"), py::arg("y2"))
    .def("processDelta", py::overload_cast<const std::string&>(&XYGrid::processDelta))
    
    ///.def("processDelta", py::overload_cast<const std::string&, const std::string&>(&XYGrid::processDelta))
    ///unknown how void processDelta(const std::string&, const std::string&) do 
    .def("getConfigString", &XYGrid::getConfigString)
    .def("getLabel", &XYGrid::getLabel);
    ///.def("initialize", py::overload_cast<XYPolygon, const XYSquare&, double>(&XYGrid::initialize), py::arg("poly"), py::arg("unit_square"), py::arg("init_value"))
    ///.def("initialize", py::overload_cast<const XYSquare&, const XYSquare&, double>(&XYGrid::initialize), py::arg("outer_square"), py::arg("unit_square"), py::arg("init_value"))
    ///.def("clear", &XYGrid::clear)
    
}