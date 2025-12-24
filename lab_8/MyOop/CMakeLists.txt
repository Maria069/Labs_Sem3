cmake_minimum_required(VERSION 3.23)

set(project "MyOop")
project(${project})

set(CMAKE_CXX_STANDARD 17)

set(${project}_SOURCES
        GeometricFigure.cpp
        Color.cpp
        Rectangle.cpp
        Circle.cpp
        Square.cpp)

set(${project}_HEADERS
        GeometricFigure.h
        Color.h
        Rectangle.h
        Circle.h
        Square.h)

set(${project}_SOURCE_LIST
        ${${project}_SOURCES}
        ${${project}_HEADERS})

add_library(${project}
        STATIC
        ${${project}_SOURCE_LIST})