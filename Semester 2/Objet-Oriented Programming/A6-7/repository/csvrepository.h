//
// Created by Rus Ilie Daniel on 26/03/2024.
//

#ifndef A45OOP_CSVREPOSITORY_H
#define A45OOP_CSVREPOSITORY_H
#include "userrepository.h"

class CSVRepo: public UserRepository {
public:
    CSVRepo(const vector<Event>& interestedList, const string& userFile);

    vector<Event>& getAllUserRepo() override;

    int getNrElems() override;

    int getCap() override;

    void addUserRepo(const Event &event) override;

    int findByTitle(string title) override;

    void deleteUserRepo(int delete_index)override;

    void writeToFile() override;

    string& getFilename() override;

    ~CSVRepo();
};
#endif //A45OOP_CSVREPOSITORY_H
