//
// Created by Rus Ilie Daniel on 08/03/2024.
//

#ifndef A45OOP_REPOSITORY_H
#define A45OOP_REPOSITORY_H

#include "../dynamicarray/dynamicarray.h"
#include <vector>

class Repository{
private:
    vector<Event> adminRepo;
    string eventsFile;
public:
    void loadEventsFromFile();

    void writeEventsToFile();

    ///Constructor for the Repository class
    ///\param repo_array - the dynamic array in which the events will be stored
    explicit Repository(vector<Event>&adminRepo1,string eventsFile1);

    ///Method to initialise the repository with a number of entities
    void initialiseRepo();

    ///Method to get all the elements of the repository
    ///\return - the array of elements
    vector<Event>& getAllRepo();

    ///Method to get the number of elements in the repository
    ///\return - the number of elements
    int getNrElems();

    ///Method to get the capacity of the repository
    ///\return - the capacity
    int getCap();

    ///Method to add an element to the repository
    ///\param event - the entity to be added
    void addRepo(const Event& event);

    ///Method to find an entity by name
    ///\param title - the title of the event that we are searching for
    int findByTitle(string title);

    ///Method to delete an entity based on its index
    ///\param delete_index - the index of the event to be deleted
    void deleteRepo(int delete_index);

    ///Method to update an entity based on its index with a new entity
    ///\param update_index - the index of the event to be updated
    ///\param new_event - the new event with which the update is done
    void updateRepo(int update_index, const Event& new_event);

    ///Destructor
    ~Repository();
};

class RepositoryException: public std::exception {
private:
    std::string message;
public:
    explicit RepositoryException(std::string& _message);

    const char *what() const noexcept override;
};

#endif //A45OOP_REPOSITORY_H
