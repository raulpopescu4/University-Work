#include <stdlib.h>
#include "dynamicarray/dynamicarray.h"
#include "repository/repository.h"
#include "service/service.h"
#include "console/console.h"
#include "validators/validator.h"


int main() {
    vector<Event> adminRepo;
    adminRepo.reserve(10);
    string filename = R"(../events.txt)";
    Repository repo{adminRepo, filename};
    repo.initialiseRepo();
    Service service{repo};
    UserService userService{repo};
    EventValidator validator{};
    Console console{service, userService, validator};
    console.start();
    return 0;
}