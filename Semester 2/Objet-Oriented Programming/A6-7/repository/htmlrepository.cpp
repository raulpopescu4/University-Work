//
// Created by Rus Ilie Daniel on 26/03/2024.
//

#include <fstream>
#include "htmlrepository.h"
#include <algorithm>

HTMLRepo::HTMLRepo(const vector<Event> &interestedList, const string &eventsFile) {
    this->interestedList = interestedList;
    this->eventsFile = eventsFile;
}

vector<Event>& HTMLRepo::getAllUserRepo() {
    return this->interestedList;
}

int HTMLRepo::getNrElems() {
    return this->interestedList.size();
}

int HTMLRepo::getCap() {
    return this->interestedList.capacity();
}

string& HTMLRepo::getFilename() {
    return this->eventsFile;
}

void HTMLRepo::addUserRepo(const Event &event) {
    this->interestedList.push_back(event);
    this->writeToFile();
}

int HTMLRepo::findByTitle(string title) {
    int searched_index=-1;
    vector<Event>::iterator it;
    it = find_if(this->interestedList.begin(), this->interestedList.end(), [&title](Event&event) {return event.getTitle() == title;});
    if (it != this->interestedList.end())
    {
        searched_index = it - this->interestedList.begin();
    }
    return searched_index;
}

void HTMLRepo::deleteUserRepo(int delete_index) {
    this->interestedList.erase(this->interestedList.begin()+delete_index);
    this->writeToFile();
}

void HTMLRepo::writeToFile() {
    ofstream fout(this->eventsFile);
    fout << "<!DOCTYPE html>\n<html><head><title>Events List</title></head><body>\n";
    fout << "<table border=\"1\">\n";
    fout << "<tr><td>Title</td><td>Description</td><td>Year</td><td>Month</td><td>Day</td><td>Hour</td><td>Minute</td><td>Number of people</td><td>Link</td></tr>\n";
    for (const Event& event: this->interestedList) {
        fout << "<tr><td>" << event.getTitle() << "</td>"
             << "<td>" << event.getDescription() << "</td>"
             << "<td>" << to_string(event.getDateTime().year) << "</td>"
             << "<td>" << to_string(event.getDateTime().month) << "</td>"
             << "<td>" << to_string(event.getDateTime().day) << "</td>"
             << "<td>" << to_string(event.getDateTime().hour) << "</td>"
             << "<td>" << to_string(event.getDateTime().minute) << "</td>"
             << "<td>" << to_string(event.getNumberOfPeople()) << "</td>"
             << "<td><a href=\"" << event.getLink() << "\">"<<event.getLink()<<"</a></td>" << '\n';
    }
    fout << "</table></body></html>";
    fout.close();
}

HTMLRepo::~HTMLRepo()=default;