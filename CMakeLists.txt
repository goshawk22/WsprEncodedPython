cmake_minimum_required(VERSION 3.15...3.31)

set(CMAKE_EXPORT_COMPILE_COMMANDS TRUE)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

project(WsprEncodedPython LANGUAGES CXX)


# Make external libraries available
include(FetchContent)


# Get WsprEncoded library
FetchContent_Declare(
    WsprEncoded
    GIT_REPOSITORY https://github.com/traquito/WsprEncoded.git
    GIT_TAG        4.2.3
)
FetchContent_MakeAvailable(WsprEncoded)


# Python Development library
find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
include_directories(${Python3_INCLUDE_DIRS})
link_directories(${Python3_LIBRARY_DIRS})

# Learn the Python site-packages directory
execute_process(
  COMMAND ${Python3_EXECUTABLE} -c "import site; print(site.getsitepackages()[0])"
  RESULT_VARIABLE result
  OUTPUT_VARIABLE SITE_PACKAGES_PATH
  OUTPUT_STRIP_TRAILING_WHITESPACE
)

if(result)
  message(FATAL_ERROR "Failed to get site-packages path")
endif()

message("WsprEncodedPython will be installed to python site-packages dir ${SITE_PACKAGES_PATH}")


# Get pybind11 library
FetchContent_Declare(
    pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11.git
    GIT_TAG        v2.13.6
)
FetchContent_MakeAvailable(pybind11)


# Build bindings
pybind11_add_module(WsprEncodedPython WsprEncodedPython.cpp)
target_link_libraries(WsprEncodedPython PRIVATE
    WsprEncoded
)


# Install the .pyd (DLL) file to Python site-packages
install(TARGETS WsprEncodedPython
    LIBRARY DESTINATION ${SITE_PACKAGES_PATH}
)

