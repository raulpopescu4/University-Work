#include "Volunteer.h"


Volunteer::Volunteer(const std::string& name, const std::string& email, const std::vector<std::string>& interests)
    : name(name), email(email), interests(interests), department(nullptr) {}

std::string Volunteer::getName() const {
    return name;
}

std::string Volunteer::getEmail() const {
    return email;
}

const std::vector<std::string>& Volunteer::getInterests() const {
    return interests;
}

void Volunteer::setInterests(const std::vector<std::string>& newInterests) {
    interests = newInterests;
}

void Volunteer::setDepartment(Department* dept) {
    department = dept;
}

Department* Volunteer::getDepartment() const {
    return department;
}
