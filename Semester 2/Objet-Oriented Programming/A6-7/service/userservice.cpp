//
// Created by Rus Ilie Daniel on 08/03/2024.
//

#include "userservice.h"
#include "../domain/datetime.h"
#include <algorithm>
#include "../repository/csvrepository.h"
#include "../repository/htmlrepository.h"
#include <iostream>

UserService::UserService(Repository &repository1, UserRepository *userRepository1) :repository(repository1){
    this->userRepository=userRepository1;
}

UserService::UserService(Repository &repository1) :repository(repository1){}

vector<Event> UserService::getAllUserService() {
    if (this->userRepository->getAllUserRepo().empty()) {
        string error;
        error += string("The list of events you are interested in is empty!");
        if (!error.empty())
            throw UserException(error);
    }
    return this->userRepository->getAllUserRepo();
}

int UserService::getNrElemsUserService() {
    if (this->userRepository->getNrElems() == 0) {
        string error;
        error += string("The list of events you are interested in is empty!");
        if(!error.empty())
            throw UserException(error);
    }
    return this->userRepository->getNrElems();
}

int UserService::getCapUserService() {
    return this->userRepository->getCap();
}

string& UserService::getFileService() {
    return this->userRepository->getFilename();
}

void UserService::repositoryType(const string& fileType) {
    if (fileType == "csv") {
        vector<Event> userVector;
        string userFile = R"(../InterestedList.csv)";
        auto * repo = new CSVRepo{ userVector, userFile};
        this->userRepository = repo;
    }else if (fileType == "html") {
        vector<Event> userVector ;
        string userFile = R"(../InterestedList.html)";
        auto * repo = new HTMLRepo{userVector, userFile};
        this->userRepository = repo;
    } else {
        string error;
        error += string("The filename is invalid!");
        if(!error.empty())
            throw UserException(error);
    }
}

void UserService::addUserService(Event event) {
    this->userRepository->addUserRepo(event);
    string title = event.getTitle();
    int delete_index = this->repository.findByTitle(title);
    this->repository.deleteRepo(delete_index);
}

int UserService::deleteUserService(string title) {
    int delete_index = this->userRepository->findByTitle(title);
    if (delete_index == -1)
        return 1;
    else {
        Event event=this->userRepository->getAllUserRepo()[delete_index];
        this->repository.addRepo(Event(event.getTitle(),event.getDescription(),event.getDateTime(),event.getNumberOfPeople()-1,event.getLink()));

        this->userRepository->deleteUserRepo(delete_index);
        return 0;
    }
}

int UserService::getFiltered(vector<Event>& valid_events, int month) {
    int counter = 0;

    if (month <= 0 || month > 12) {
        vector<Event> allEvents = this->repository.getAllRepo();
        sort(allEvents.begin(), allEvents.end(), [](const Event& event1, const Event& event2) {
            return event1.getDateTime() < event2.getDateTime();
        });
        for (const Event& event : allEvents) {
            valid_events.push_back(event);
            counter++;
        }
    } else {
        for (const Event& event : this->repository.getAllRepo()) {
            if (event.getDateTime().month == month) {
                valid_events.push_back(event);
                counter++;
            }
        }
    }
    return counter;
}



UserService::~UserService() = default;