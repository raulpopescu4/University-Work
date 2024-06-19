//
// Created by Rus Ilie Daniel on 08/03/2024.
//

#include "repository.h"
#include <algorithm>
#include <fstream>

Repository::Repository(vector<Event>&adminRepo1,string eventsFile1) {
    this->adminRepo=adminRepo1;
    this->eventsFile=eventsFile1;
}

void Repository::loadEventsFromFile() {
    if (!this->eventsFile.empty()) {
        Event eventFromFile;
        ifstream fin(this->eventsFile);
        while (fin >> eventFromFile) {
            if (find(this->adminRepo.begin(), this->adminRepo.end(), eventFromFile) ==this->adminRepo.end())
                this->adminRepo.push_back(eventFromFile);
        }
        fin.close();
    }
}

void Repository::writeEventsToFile() {
    if (!this->eventsFile.empty()) {
        ofstream fout(this->eventsFile);
        for (const Event &event: this->adminRepo) {
            fout << event << "\n";
        }
        fout.close();
    }
}

void Repository::initialiseRepo() {
    this->loadEventsFromFile();
}


vector<Event>& Repository::getAllRepo() {
    if (this->adminRepo.empty()) {
        string error;
        error += string("The database is empty!");
        if(!error.empty())
            throw RepositoryException(error);
    }
    return this->adminRepo;
}

int Repository::getNrElems() {
    if (this->adminRepo.empty()) {
        string error;
        error += string("The database is empty!");
        if(!error.empty())
            throw RepositoryException(error);
    }
    return this->adminRepo.size();
}

int Repository::getCap() {
    return this->adminRepo.capacity();
}

void Repository::addRepo(const Event& event) {
    int existing = this->findByTitle(event.getTitle());
    if (existing != -1) {
        string error;
        error += string("The event already exists!");
        if(!error.empty())
            throw RepositoryException(error);
    }
    this->adminRepo.push_back(event);
    this->writeEventsToFile();
}

int Repository::findByTitle(string title) {
    int searched_index = -1;
    vector<Event>::iterator it;
    it = find_if(this->adminRepo.begin(), this->adminRepo.end(), [&title](Event&event) {return event.getTitle() == title;});
    if (it != this->adminRepo.end())
    {
        searched_index = it - this->adminRepo.begin();
    }
    return searched_index;
}

void Repository::deleteRepo(int delete_index) {
    if (delete_index == -1) {
        string error;
        error += string("The event does not exist!");
        if(!error.empty())
            throw RepositoryException(error);
    }
    this->adminRepo.erase(this->adminRepo.begin() + delete_index);
    this->writeEventsToFile();
}

void Repository::updateRepo(int update_index, const Event& new_event) {
    if (update_index == -1) {
        string error;
        error += string("The event does not exist!");
        if(!error.empty())
            throw RepositoryException(error);
    }
    this->adminRepo[update_index] = new_event;
    this->writeEventsToFile();
}

Repository::~Repository() = default;

RepositoryException::RepositoryException(std::string &_message) : message(_message){}

const char* RepositoryException::what() const noexcept {
    return message.c_str();
}