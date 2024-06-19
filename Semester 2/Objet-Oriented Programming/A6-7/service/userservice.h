//
// Created by Rus Ilie Daniel on 08/03/2024.
//

#ifndef A45OOP_USERSERVICE_H
#define A45OOP_USERSERVICE_H
#include "../repository/repository.h"
#include "../repository/userrepository.h"
#include "../domain/datetime.h"

class UserService {
private:
    Repository & repository;
    UserRepository * userRepository;
public:
    ///Constructor for the UserService class
    ///\param repository1 - the admin repository
    ///\param userRepository1 - the user repository
    UserService(Repository & repository1, UserRepository * userRepository1);

    explicit UserService(Repository&repository1);

    ///Method to get all the elements from the user repository
    ///\return - the elements from the user repository
    vector<Event> getAllUserService();

    ///Method to get the number of elements from the user repository
    ///\return - the number of elements
    int getNrElemsUserService();

    ///Method to get the capacity of the user repository
    ///\return - the capacity
    int getCapUserService();

    ///Method to add a new event to the user repository
    ///\param event - the event to be added
    void addUserService(Event event);

    void repositoryType(const string &fileType);

    string & getFileService();




    ///Method to delete an element from the user repository
    ///\param title - the title of the event to be deleted from the user repository
    ///\return - 1 if not deleted, 0 otherwise
    int deleteUserService(string title);

    ///Method to get the filtered list of events, based on when they happen
    ///\param valid_events - the array of valid events
    ///\param month - the months filter
    ///\return - the number of elements from the valid_events array
    int getFiltered(vector<Event>&valid_events, int month);

    ///Destructor
    ~UserService();
};



#endif //A45OOP_USERSERVICE_H
