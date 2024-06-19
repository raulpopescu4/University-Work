//
// Created by Rus Ilie Daniel on 08/03/2024.
//

#ifndef A45OOP_USERREPOSITORY_H
#define A45OOP_USERREPOSITORY_H

#include "../dynamicarray/dynamicarray.h"
#include <vector>
#include "../domain/domain.h"

class UserRepository {
protected:
    vector<Event> interestedList;
    string eventsFile;
public:
    ///Constructor for the UserRepository class
    ///\param interestedList1 - the list of events that the user is interested in
    explicit UserRepository(vector<Event>&interestedList1);

    UserRepository();

    ///Method to get all the elements of the UserRepository
    ///\return - the list of elements from the UserRepository
    virtual vector<Event>& getAllUserRepo()=0;

    ///Method to get the number of elements from the UserRepository
    ///\return - the number of elements
    virtual int getNrElems()=0;

    ///Method to get the capacity of the dynamic array used in the UserRepository
    ///\return - the capacity
    virtual int getCap()=0;

    ///Method to add an element to the UserRepository
    ///\param event - the element to be added
    virtual void addUserRepo(const Event& event)=0;

    ///Method to find an entity by name
    ///\param title - the title of the event that we are searching for
    virtual int findByTitle(string title)=0;

    ///Method to delete an entity based on its index
    ///\param delete_index - the index of the event to be deleted
    virtual void deleteUserRepo(int delete_index)=0;

    virtual void writeToFile()=0;

    virtual string& getFilename()=0;

    ///Destructor
    ~UserRepository();
};

class UserException: public std::exception {
private:
    std::string message;
public:
    explicit UserException(std::string& _message);

    const char *what() const noexcept override;
};

#endif //A45OOP_USERREPOSITORY_H
