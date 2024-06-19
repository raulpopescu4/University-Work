//
// Created by Rus Ilie Daniel on 26/03/2024.
//

#include "csvrepository.h"
#include <fstream>
#include "csvrepository.h"
#include <algorithm>

CSVRepo::CSVRepo(const vector<Event>& interestedList, const string& eventsFile) {
    this->interestedList = interestedList;
    this->eventsFile = eventsFile;
}

vector<Event>& CSVRepo::getAllUserRepo() {
    return this->interestedList;
}

int CSVRepo::getNrElems() {
    return this->interestedList.size();
}

int CSVRepo::getCap() {
    return this->interestedList.capacity();
}

string& CSVRepo::getFilename() {
    return this->eventsFile;
}

void CSVRepo::addUserRepo(const Event &event) {
    this->interestedList.push_back(event);
    this->writeToFile();
}

int CSVRepo::findByTitle(string title) {
    int searched_index=-1;
    vector<Event>::iterator it;
    it = find_if(this->interestedList.begin(), this->interestedList.end(), [&title](Event&event) {return event.getTitle() == title;});
    if (it != this->interestedList.end())
    {
        searched_index = it - this->interestedList.begin();
    }
    return searched_index;
}

void CSVRepo::deleteUserRepo(int delete_index) {
    this->interestedList.erase(this->interestedList.begin()+delete_index);
    this->writeToFile();
}

void CSVRepo::writeToFile() {
    ofstream fout(this->eventsFile);
    if (!this->interestedList.empty()) {
        for (const Event& event: this->interestedList) {
            fout<<event<<"\n";
        }
    }
    fout.close();
}

CSVRepo::~CSVRepo()=default;