#include <iostream>
#include <pybind11/pybind11.h>

namespace py = pybind11;

void init_XYPatternBlock(py::module &);
void init_XYPoint(py::module &);
void init_XYSegList(py::module &);
void init_XYPolygon(py::module &);
void init_CPAEngine(py::module &);
void init_EdgeTag(py::module &);
void init_EdgeTagSet(py::module &);
void init_XYGrid(py::module &);
void init_XYSquare(py::module &);

namespace ivp {

int cpp_test_plus(int x, int y){
    int result = x + y;
    std::cout << "C++ result x plus y is: " << result << '\n';
    return result;
}

PYBIND11_MODULE(pyivp, m) {
    // Optional docstring
    m.doc() = "pybind11 for cpp labs";
 
    m.def("python_test_plus", &cpp_test_plus, "plus x and y");
    init_XYPatternBlock(m);
    init_XYPoint(m);
    init_XYSegList(m);
    init_XYPolygon(m);
    init_CPAEngine(m);
    init_EdgeTag(m);
    init_EdgeTagSet(m);
    init_XYGrid(m);
    init_XYSquare(m);
}
}
