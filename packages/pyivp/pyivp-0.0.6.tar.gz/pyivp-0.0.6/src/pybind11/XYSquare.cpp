#include "../lib_geometry/XYSquare.h"

#include <pybind11/stl.h>
#include <pybind11/pybind11.h>

namespace py = pybind11;

void init_XYSquare(py::module &m) {
    py::class_<XYSquare>(m, "XYSquare")
    .def(py::init())
    .def(py::init<double>(), py::arg("xylen"))
    .def(py::init<double, double>(), py::arg("xlen"), py::arg("ylen"))
    .def(py::init<double, double, double, double>(), py::arg("xl"), py::arg("hx"), py::arg("yl"), py::arg("yh"))

    .def("operator==", &XYSquare::operator==)
    .def("operator!=", &XYSquare::operator!=)
    .def("set", &XYSquare::set, py::arg("gxl"), py::arg("gxh"), py::arg("gyl"), py::arg("gyh"))
    .def("containsPoint", &XYSquare::containsPoint, py::arg("gx"), py::arg("gy"))
    .def("segIntersectLength", &XYSquare::segIntersectLength, py::arg("x1"), py::arg("y1"), py::arg("x2"), py::arg("y2"))
    .def("segDistToSquare", &XYSquare::segDistToSquare, py::arg("x1"), py::arg("y1"), py::arg("x2"), py::arg("y2"))
    .def("ptDistToSquareCtr", &XYSquare::ptDistToSquareCtr, py::arg("x1"), py::arg("y1"))

    .def("get_min_x", &XYSquare::get_min_x)
    .def("get_max_x", &XYSquare::get_max_x)
    .def("get_min_y", &XYSquare::get_min_y)
    .def("get_max_y", &XYSquare::get_max_y)

    .def("getVal", &XYSquare::getVal, py::arg("xy"), py::arg("lh"))
    .def("shiftX", &XYSquare::shiftX, py::arg("v"))
    .def("shiftY", &XYSquare::shiftY, py::arg("v"))
    .def("getLengthX", &XYSquare::getLengthX)
    .def("getLengthY", &XYSquare::getLengthY)
    .def("valid", &XYSquare::valid)

    .def("getCenterX", &XYSquare::getCenterX)
    .def("getCenterY", &XYSquare::getCenterY)
    
    .def("get_spec", &XYSquare::get_spec, py::arg("param"))
    .def("get_spec_as_poly", &XYSquare::get_spec_as_poly, py::arg("parm"));

}
