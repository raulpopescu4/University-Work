cmake_minimum_required(VERSION 3.21)
project(a45oop)

set(CMAKE_CXX_STANDARD 14)

add_executable(a45oop main.cpp domain/domain.cpp domain/domain.h domain/datetime.h dynamicarray/dynamicarray.cpp dynamicarray/dynamicarray.h repository/repository.cpp repository/repository.h repository/userrepository.cpp repository/userrepository.h service/service.cpp service/service.h service/userservice.cpp service/userservice.h console/console.cpp console/console.h repository/htmlrepository.cpp repository/htmlrepository.h repository/csvrepository.cpp repository/csvrepository.h validators/validator.cpp validators/validator.h)
