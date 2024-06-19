#include "Department.h"

Department::Department(const std::string& name, const std::string& description) : name(name), description(description) {}

std::string Department::getName() const {
    return name;
}

std::string Department::getDescription() const {
    return description;
}
