#include "../lib_geometry/EdgeTagSet.h"

#include <pybind11/stl.h>
#include <pybind11/pybind11.h>

namespace py = pybind11;

void init_EdgeTagSet(py::module &m) {

    py::class_<EdgeTagSet>(m, "EdgeTagSet")
    .def(py::init())
    .def("addEdgeTag",&EdgeTagSet::addEdgeTag,"addEdgeTag")
    .def("setOnSpec",&EdgeTagSet::setOnSpec,"setOnSpec")
    .def("size",&EdgeTagSet::size,"size")
    .def("getSpec",&EdgeTagSet::getSpec,"getSpec")
    .def("matches",&EdgeTagSet::matches,"matches")
    .def("print",&EdgeTagSet::print,"print")   
    ;

}
