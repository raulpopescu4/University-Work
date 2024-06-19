#include "Repository.h"
#include <fstream>
#include <sstream>
#include <iostream>

void Repository::addDepartment(Department* department) {
    departments.push_back(department);
}

void Repository::addVolunteer(Volunteer* volunteer) {
    volunteers.push_back(volunteer);
}

std::vector<Department*> Repository::getDepartments() const { return departments; }
std::vector<Volunteer*> Repository::getVolunteers() const { return volunteers; }

void Repository::loadDepartments(const std::string& filename) {
    std::ifstream file(filename);
    std::string line;
    while (getline(file, line)) {
        std::istringstream iss(line);
        std::string name, description;
        getline(iss, name, ',');
        getline(iss, description);
        addDepartment(new Department(name, description));
    }
}

void Repository::loadVolunteers(const std::string& filename) {
    std::ifstream file(filename);
    std::string line;

    while (getline(file, line)) {
        std::istringstream iss(line);
        std::string name, email, interestsStr, departmentName;
        getline(iss, name, ',');
        getline(iss, email, ',');
        getline(iss, interestsStr, ',');
        getline(iss, departmentName);

        std::vector<std::string> interests;
        std::stringstream interestStream(interestsStr);
        std::string interest;
        while (getline(interestStream, interest, ';')) { 
            interests.push_back(interest);
        }

        Volunteer* volunteer = new Volunteer(name, email, interests);
        if (!departmentName.empty()) {
            for (auto* dept : getDepartments()) {
                if (dept->getName() == departmentName) {
                    volunteer->setDepartment(dept);
                    break;
                }
            }
        }
        addVolunteer(volunteer);
    }
}

void Repository::saveVolunteers(const std::string& filename) const {
    std::ofstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Failed to open file for writing: " << filename << std::endl;
        return;
    }

    for (const Volunteer* volunteer : volunteers) {
        file << volunteer->getName() << "," << volunteer->getEmail() << ",";

        const std::vector<std::string>& interests = volunteer->getInterests();
        for (size_t i = 0; i < interests.size(); ++i) {
            file << interests[i];
            if (i < interests.size() - 1) {
                file << ";";
            }
        }

        const Department* department = volunteer->getDepartment();
        if (department) {
            file << "," << department->getName();
        }

        file << std::endl;
    }
    file.close();
}