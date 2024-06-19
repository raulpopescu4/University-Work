//
// Created by Rus Ilie Daniel on 08/03/2024.
//

#ifndef A45OOP_CONSOLE_H
#define A45OOP_CONSOLE_H

#include "../service/service.h"
#include "../service/userservice.h"
#include "../validators/validator.h"

class Console {
private:
    Service &service;
    UserService & userService;
    EventValidator&eventValidator;
public:
    Console(Service &service, UserService & userService, EventValidator&eventValidator);

    void addUi();

    void deleteUi();

    void updateUi();

    void listAll();

    void listAllUser();

    void listFilteredUser();

    void listInterestedList();

    void deleteUserEvent();

    void openFile();

    static void printAdministratorSubmenu();

    static void printUserSubmenu();

    void AdministratorMode();

    void UserMode();

    static void printMenu();

    void start();

    ~Console();
};

#endif //A45OOP_CONSOLE_H
