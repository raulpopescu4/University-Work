//
// Created by Rus Ilie Daniel on 08/03/2024.
//
#include <utility>
#include "domain.h"
#include <vector>
#include <sstream>

Event::Event(const string title, const string description, const DateTime &dateTime, int numberOfPeople,
             const string link) {
    this->title= move(title);
    this->description= move(description);
    this->link= move(link);
    this->numberOfPeople=numberOfPeople;
    this->dateTime=dateTime;
}

string Event::getTitle() const {
    return this->title;
}

DateTime Event::getDateTime() const {
    return this->dateTime;
}

string Event::getDescription() const {
    return this->description;
}

int Event::getNumberOfPeople() const {
    return this->numberOfPeople;
}

string Event::getLink() const {
    return this->link;
}

Event::~Event() =default;

string Event::toString() const {
    return "Title: " + this->title + "\nDescription: " + this->description +
           "\nDate and Time: " + this->dateTime.toString() +
           "\nNumber of People: " + to_string(this->numberOfPeople) +
           "\nLink: " + this->link;
}

vector<string> tokenize(const string& str, char delimiter) {
    vector<string> result;
    stringstream ss(str);
    string token;
    while (getline(ss, token, delimiter))
        result.push_back(token);

    return result;
}

bool Event::operator==(const Event& eventToCheck) const {
    return this->title == eventToCheck.title;
}

istream& operator>>(istream& inputStream, Event& event) {
    string line;
    getline(inputStream, line);
    vector<string> tokens;
    if (line.empty())
        return inputStream;
    tokens = tokenize(line, ',');
    
    event.title=tokens[0];
    event.description=tokens[1];
    event.dateTime.year=stoi(tokens[2]);
    event.dateTime.month=stoi(tokens[3]);
    event.dateTime.day=stoi(tokens[4]);
    event.dateTime.hour=stoi(tokens[5]);
    event.dateTime.minute=stoi(tokens[6]);
    event.numberOfPeople=stoi(tokens[7]);
    event.link=tokens[8];

    return inputStream;
}

ostream& operator<<(ostream& outputStream, const Event& eventOutput) {
    outputStream << eventOutput.title << "," << eventOutput.description << "," << to_string(eventOutput.dateTime.year) << "," <<to_string(eventOutput.dateTime.month)
                 <<"," <<to_string(eventOutput.dateTime.day)<<"," <<to_string(eventOutput.dateTime.hour)<<","<<to_string(eventOutput.dateTime.minute)
                 <<","<<to_string(eventOutput.numberOfPeople)<<","<<eventOutput.link;
    return outputStream;
}