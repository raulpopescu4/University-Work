#pragma once

#include "Repository.h"
#include "Subject.h"

class Service : public Subject {
private:
    Repository& repo;

public:
    Service(Repository& repo);
    void assignVolunteerToDepartment(Volunteer* volunteer, Department* department);
    void addNewVolunteer(const std::string& name, const std::string& email, const std::vector<std::string>& interests);
    std::vector<Department*> getAllDepartments() const;
    std::vector<Volunteer*> getAllVolunteers() const;
    std::vector<Volunteer*> getVolunteersForDepartment(Department* department);
    Repository& getRepository();
};
