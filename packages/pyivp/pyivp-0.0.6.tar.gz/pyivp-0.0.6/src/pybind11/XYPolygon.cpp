#include "../lib_geometry/XYPolygon.h"

#include <pybind11/stl.h>
#include <pybind11/pybind11.h>

namespace py = pybind11;

void init_XYPolygon(py::module &m)
{
  py::class_<XYPolygon>(m, "XYPolygon")
      .def(py::init())
      .def("add_vertex", py::overload_cast<double, double, bool>(&XYPolygon::add_vertex), py::arg("x"), py::arg("y"), py::arg("check_convexity") = true)
      .def("add_vertex_delta", &XYPolygon::add_vertex_delta, py::arg("x"), py::arg("y"), py::arg("delta"), py::arg("check_convexity") = true)
      .def("add_vertex", py::overload_cast<double, double, double, bool>(&XYPolygon::add_vertex), py::arg("x"), py::arg("y"), py::arg("z"), py::arg("check_convexity") = true)
      .def("add_vertex", py::overload_cast<double, double, double, std::string, bool>(&XYPolygon::add_vertex), py::arg("x"), py::arg("y"), py::arg("z"), py::arg("property"), py::arg("check_convexity") = true)
      .def("alter_vertex", &XYPolygon::alter_vertex, py::arg("x"), py::arg("y"), py::arg("z"))
      .def("delete_vertex", py::overload_cast<double, double>(&XYPolygon::delete_vertex), py::arg("x"), py::arg("y"))
      .def("delete_vertex", py::overload_cast<unsigned int>(&XYPolygon::delete_vertex), py::arg("ix"))
      .def("grow_by_pct", &XYPolygon::grow_by_pct, py::arg("pct"))
      .def("grow_by_amt", &XYPolygon::grow_by_amt, py::arg("amt"))
      .def("insert_vertex", &XYPolygon::insert_vertex, py::arg("x"), py::arg("y"), py::arg("z"))

      .def("clear", &XYPolygon::clear)
      .def("apply_snap", &XYPolygon::apply_snap, py::arg("snapval"))
      .def("reverse", &XYPolygon::reverse)
      .def("rotate", py::overload_cast<double, double, double>(&XYPolygon::rotate), py::arg("val"), py::arg("cx"), py::arg("xy"))
      .def("rotate", py::overload_cast<double>(&XYPolygon::rotate), py::arg("val"))

      .def("contains", py::overload_cast<double, double>(&XYPolygon::contains, py::const_), py::arg("x"), py::arg("y"))
      .def("contains", py::overload_cast<const XYPolygon &>(&XYPolygon::contains, py::const_), py::arg("inner_poly"))
      .def("intersects", py::overload_cast<const XYPolygon &>(&XYPolygon::intersects, py::const_), py::arg("poly"))
      .def("intersects", py::overload_cast<const XYSquare &>(&XYPolygon::intersects, py::const_), py::arg("square"))
      .def("dist_to_poly", py::overload_cast<const XYPolygon &>(&XYPolygon::dist_to_poly, py::const_), py::arg("poly"))
      .def("dist_to_poly", py::overload_cast<double, double>(&XYPolygon::dist_to_poly, py::const_), py::arg("px"), py::arg("py"))
      .def("dist_to_poly", py::overload_cast<double, double, double, double>(&XYPolygon::dist_to_poly, py::const_), py::arg("x1"), py::arg("x2"), py::arg("y1"), py::arg("y2"))
      .def("dist_to_poly", py::overload_cast<double, double, double>(&XYPolygon::dist_to_poly, py::const_), py::arg("px"), py::arg("py"), py::arg("angle"))
      .def("seg_intercepts", py::overload_cast<double, double, double, double>(&XYPolygon::seg_intercepts, py::const_), py::arg("x1"), py::arg("x2"), py::arg("y1"), py::arg("y2"))
      .def("line_intersects", py::overload_cast<double, double, double, double, double &, double &, double &, double &>(&XYPolygon::line_intersects, py::const_), py::arg("x1"), py::arg("y1"), py::arg("x2"), py::arg("y2"), py::arg("ix1"), py::arg("iy1"), py::arg("ix2"), py::arg("iy2"))

      .def("vertex_is_viewable", &XYPolygon::vertex_is_viewable, py::arg("ix"), py::arg("x1"), py::arg("y1"))
      .def("is_convex", &XYPolygon::is_convex)
      .def("determine_convexity", &XYPolygon::determine_convexity)

      .def("area", &XYPolygon::area)
      .def("simplify", &XYPolygon::simplify, py::arg("range_thresh"))

      .def("max_radius", &XYPolygon::max_radius)
      .def("closest_point_on_poly", &XYPolygon::closest_point_on_poly, py::arg("sx"), py::arg("sy"), py::arg("rx"), py::arg("ry"))

      .def("exportSegList", &XYPolygon::exportSegList, py::arg("x") = 0, py::arg("y") = 0)
      .def("crossProductSettle", &XYPolygon::crossProductSettle)
      .def("min_xproduct", &XYPolygon::min_xproduct, py::arg("ok"));
}
