//
// Created by Rus Ilie Daniel on 08/03/2024.
//

#ifndef A45OOP_SERVICE_H
#define A45OOP_SERVICE_H
#include "../repository/repository.h"
#include "../domain/datetime.h"

class Service{
private:
    Repository &repository;
public:
    ///Constructor for the Service class
    ///\param repo - the admin repository
    explicit Service(Repository &repo);

    ///Method to get all the elements of the repository
    ///\return - the elements from the repository
    vector<Event> getAllService();

    ///Method to get the number of elements from the repository
    ///\return - the number of elements from the repository
    int getNrElemsService();

    ///Method to get the capacity of the repository
    ///\return - the capacity
    int getCapService();

    ///Method to add an element to the repository
    ///\param title - the title of the event
    ///\param description - the description of the event
    ///\param dateTime - the date and time of the event
    ///\param numberOfPeople - the number of people at the event
    ///\param link - the link to the event
    ///\return - 1 if not added, 0 otherwise
    void addService(string title, string description, DateTime dateTime, int numberOfPeople, string link);

    ///Method to delete an element from the repository
    ///\param title - the title of the event to be deleted
    ///\return - 1 if not deleted, 0 otherwise
    void deleteService(string title);

    ///Method to update an element from the repository
    ///\param old_title - the old title of the event
    ///\param new_title - the new title of the event
    ///\param new_description - the new description of the event
    ///\param new_dateTime - the new date and time of the event
    ///\param new_numberOfPeople - the new number of people at the event
    ///\param new_link - the new link to the event
    ///\return - 1 if not updated, 0 otherwise
    void updateService(string old_title, string new_title, string new_description, DateTime new_dateTime, int new_numberOfPeople, string new_link);

    ///Destructor
    ~Service();
};


#endif //A45OOP_SERVICE_H
