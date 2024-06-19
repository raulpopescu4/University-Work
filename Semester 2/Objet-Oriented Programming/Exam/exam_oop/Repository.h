#pragma once

#include <vector>
#include <string>
#include "Department.h"
#include "Volunteer.h"

class Repository {
private:
    std::vector<Department*> departments;
    std::vector<Volunteer*> volunteers;

public:
    void addDepartment(Department* department);
    void addVolunteer(Volunteer* volunteer);
    std::vector<Department*> getDepartments() const;
    std::vector<Volunteer*> getVolunteers() const;
    void loadDepartments(const std::string& filename);
    void loadVolunteers(const std::string& filename);
    void saveVolunteers(const std::string& filename) const;
};

