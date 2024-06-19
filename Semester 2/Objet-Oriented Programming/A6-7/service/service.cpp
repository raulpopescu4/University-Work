//
// Created by Rus Ilie Daniel on 08/03/2024.
//

#include "service.h"
#include "../domain/datetime.h"
#include <iterator>
#include <algorithm>

Service::Service(Repository &repo) :repository(repo){}

vector<Event> Service::getAllService() {
    return this->repository.getAllRepo();
}

int Service::getNrElemsService() {
    return this->repository.getNrElems();
}

int Service::getCapService() {
    return this->repository.getCap();
}

void Service::addService(string title, string description, DateTime dateTime, int numberOfPeople, string link) {
    this->repository.addRepo(Event(title,description,dateTime,numberOfPeople,link));
}

void Service::deleteService(string title) {
    this->repository.deleteRepo(this->repository.findByTitle(title));
}

void Service::updateService(string old_title, string new_title, string new_description, DateTime new_dateTime, int new_numberOfPeople, string new_link) {
    this->repository.updateRepo(this->repository.findByTitle(old_title), Event(new_title,new_description,new_dateTime,new_numberOfPeople,new_link));
}

Service::~Service() = default;