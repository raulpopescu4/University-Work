//
// Created by Rus Ilie Daniel on 08/03/2024.
//

#include "userrepository.h"
#include <fstream>

UserException::UserException(string &_message): message(_message) {}

const char* UserException::what() const noexcept {
    return message.c_str();
}

UserRepository::UserRepository() = default;

UserRepository::UserRepository(vector<Event>& interestedList1) {
    this->interestedList = interestedList1;
}

UserRepository::~UserRepository() = default;