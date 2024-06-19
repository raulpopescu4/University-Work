#pragma once
#include <string>

class Department {
private:
    std::string name;
    std::string description;

public:
    Department(const std::string& name, const std::string& description);
    std::string getName() const;
    std::string getDescription() const;
};
