cmake_minimum_required(VERSION 3.21)
project(a23oop C)

set(CMAKE_C_STANDARD 99)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -g")

add_executable(a23oop main.c domain/domain.c domain/domain.h DynamicArray/dynamic_array.c DynamicArray/dynamic_array.h Repository/repository.c Repository/repository.h Repository/undoredorepository.c Repository/undoredorepository.h Service/service.c Service/service.h Tests/tests.c Tests/tests.h UI/ui.c UI/ui.h)
