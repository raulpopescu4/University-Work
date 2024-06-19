#pragma once

#include <string>
#include <vector>
#include "Department.h"

class Volunteer {
private:
    std::string name;
    std::string email;
    std::vector<std::string> interests;
    Department* department;

public:
    Volunteer(const std::string& name, const std::string& email, const std::vector<std::string>& interests);
    std::string getName() const;
    std::string getEmail() const;
    const std::vector<std::string>& getInterests() const;
    void setInterests(const std::vector<std::string>& interests);
    void setDepartment(Department* dept);
    Department* getDepartment() const;
};
