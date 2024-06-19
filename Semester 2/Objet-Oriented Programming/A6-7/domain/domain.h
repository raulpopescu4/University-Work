//
// Created by Rus Ilie Daniel on 08/03/2024.
//

#ifndef A45OOP_DOMAIN_H
#define A45OOP_DOMAIN_H
#include <string>
#include "datetime.h"
using namespace std;

class Event {
private:
    string title;
    string description;
    DateTime dateTime;
    int numberOfPeople;
    string link;

public:
    Event(const string title = "empty", const string description = "empty",
          const DateTime& dateTime = DateTime(), int numberOfPeople = 0,
          const string link = "empty");

    string getTitle() const;
    string getDescription() const;
    DateTime getDateTime() const;
    int getNumberOfPeople() const;
    string getLink() const;

    void setTitle(const std::string& title);
    void setDescription(const std::string& description);
    void setDateTime(const DateTime& dateTime);
    void setNumberOfPeople(int numberOfPeople);
    void setLink(const std::string& link);

    string toString() const;

    bool operator==(const Event &eventToCheck)const;

    friend istream&operator>>(istream&inputStream, Event& event);

    friend ostream & operator<<(ostream& outputStream, const Event& eventOutput);

    ~Event();
};

#endif //A45OOP_DOMAIN_H
