#include "Service.h"
#include <stdexcept>
#include <algorithm>

Service::Service(Repository& repo) : repo(repo) {}

void Service::assignVolunteerToDepartment(Volunteer* volunteer, Department* department) {
    volunteer->setDepartment(department);
}

void Service::addNewVolunteer(const std::string& name, const std::string& email, const std::vector<std::string>& interests) {
    if (name.empty() || email.empty()) {
        throw std::runtime_error("Name and email cannot be empty.");
    }
    Volunteer* volunteer = new Volunteer(name, email, interests);

    repo.addVolunteer(volunteer);
    
    notifyObservers();
}

std::vector<Department*> Service::getAllDepartments() const {
    return repo.getDepartments();
}

std::vector<Volunteer*> Service::getAllVolunteers() const {
    return repo.getVolunteers();
}

//void sortVolunteersByName() {
//    std::vector<Volunteer*>& volunteers = repo.getVolunteers();
//    std::sort(volunteers.begin(), volunteers.end(), [](Volunteer* a, Volunteer* b) {
//        return a->getName() < b->getName();
//        });
//
//}

std::vector<Volunteer*> Service::getVolunteersForDepartment(Department* department) {
    std::vector<Volunteer*> filteredVolunteers;
    for (Volunteer* volunteer : repo.getVolunteers()) {
        if (volunteer->getDepartment() == department) {
            filteredVolunteers.push_back(volunteer);
        }
    }
    std::sort(filteredVolunteers.begin(), filteredVolunteers.end(), [](Volunteer* a, Volunteer* b) {
                return a->getName() < b->getName();
                });
    return filteredVolunteers;
}

Repository& Service::getRepository() {
    return repo;
}
