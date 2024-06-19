//
// Created by Rus Ilie Daniel on 08/03/2024.
//

#include "console.h"
#include <iostream>

using namespace std;

Console::Console(Service &service, UserService & userService, EventValidator&eventValidator):service(service),userService(userService),eventValidator(eventValidator)
{
}

void Console::addUi() {
    cout<<"Add a new event"<<endl;
    string title_string;
    string description_string;
    string year_string;
    string month_string;
    string day_string;
    string hour_string;
    string minute_string;
    string numberOfPeople_string;
    string link_string;
    int year,month,day,hour,minute,numberOfPeople;

    while(true){
        try{
            cout<<"Enter the title: "<<endl;
            getline(cin, title_string);
            this->eventValidator.validateTitle(title_string);
            break;
        }catch (ValidationException&ex){
            cout<<ex.what()<<endl;
        }
    }
    while(true){
        try{
            cout<<"Enter the description: "<<endl;
            getline(cin, description_string);
            this->eventValidator.validateDescription(description_string);
            break;
        }catch (ValidationException&ex){
            cout<<ex.what()<<endl;
        }
    }
    while(true){
        try{
            cout<<"Enter the year: "<<endl;
            getline(cin,year_string);
            this->eventValidator.validateYearString(year_string);
            year= stoi(year_string);
            this->eventValidator.validateYear(year);
            break;
        } catch (ValidationException&ex) {
            cout <<ex.what()<<endl;
        }
    }
    while(true){
        try{
            cout<<"Enter the month: "<<endl;
            getline(cin,month_string);
            this->eventValidator.validateMonthString(month_string);
            month= stoi(month_string);
            this->eventValidator.validateMonth(month);
            break;
        } catch (ValidationException&ex) {
            cout <<ex.what()<<endl;
        }
    }
    while(true){
        try{
            cout<<"Enter the day: "<<endl;
            getline(cin,day_string);
            this->eventValidator.validateDayString(day_string);
            day= stoi(day_string);
            this->eventValidator.validateDay(day);
            break;
        } catch (ValidationException&ex) {
            cout <<ex.what()<<endl;
        }
    }
    while(true){
        try{
            cout<<"Enter the hour: "<<endl;
            getline(cin,hour_string);
            this->eventValidator.validateHourString(hour_string);
            hour= stoi(hour_string);
            this->eventValidator.validateHour(hour);
            break;
        } catch (ValidationException&ex) {
            cout <<ex.what()<<endl;
        }
    }
    while(true){
        try{
            cout<<"Enter the minute: "<<endl;
            getline(cin,minute_string);
            this->eventValidator.validateMinuteString(minute_string);
            minute= stoi(minute_string);
            this->eventValidator.validateMinute(minute);
            break;
        } catch (ValidationException&ex) {
            cout <<ex.what()<<endl;
        }
    }
    while(true){
        try{
            cout<<"Enter the number of people: "<<endl;
            getline(cin,numberOfPeople_string);
            this->eventValidator.validateNumberOfPeopleString(numberOfPeople_string);
            numberOfPeople= stoi(numberOfPeople_string);
            this->eventValidator.validateNumberOfPeople(numberOfPeople);
            break;
        } catch (ValidationException&ex) {
            cout <<ex.what()<<endl;
        }
    }
    while(true){
        try{
            cout<<"Enter the link: "<<endl;
            getline(cin, link_string);
            this->eventValidator.validateLink(link_string);
            break;
        }catch (ValidationException&ex){
            cout<<ex.what()<<endl;
        }
    }
    this->service.addService(title_string,description_string, DateTime(year,month,day,hour,minute),numberOfPeople,link_string);
    cout <<"Event added successfully"<<endl;
}

void Console::deleteUi() {
    cout<<"Delete an event"<<endl;
    string title;
    while(true){
        try{
            cout<<"Enter the title:"<<endl;
            getline(cin,title);
            this->eventValidator.validateTitle(title);
            break;
        }catch (ValidationException&ex){
            cout<<ex.what()<<endl;
        }
    }
    this->service.deleteService(title);
    cout<<"Event successfully deleted!"<<endl;

}

void Console::updateUi() {
    cout<<"Update an event"<<endl;
    string old_title;
    string title_string;
    string description_string;
    string year_string;
    string month_string;
    string day_string;
    string hour_string;
    string minute_string;
    string numberOfPeople_string;
    string link_string;
    int year,month,day,hour,minute,numberOfPeople;
    while(true){
        try{
            cout<<"Enter the old title: "<<endl;
            getline(cin, old_title);
            this->eventValidator.validateTitle(old_title);
            break;
        }catch (ValidationException&ex){
            cout<<ex.what()<<endl;
        }
    }
    while(true){
        try{
            cout<<"Enter the title: "<<endl;
            getline(cin, title_string);
            this->eventValidator.validateTitle(title_string);
            break;
        }catch (ValidationException&ex){
            cout<<ex.what()<<endl;
        }
    }
    while(true){
        try{
            cout<<"Enter the description: "<<endl;
            getline(cin, description_string);
            this->eventValidator.validateDescription(description_string);
            break;
        }catch (ValidationException&ex){
            cout<<ex.what()<<endl;
        }
    }
    while(true){
        try{
            cout<<"Enter the year: "<<endl;
            getline(cin,year_string);
            this->eventValidator.validateYearString(year_string);
            year= stoi(year_string);
            this->eventValidator.validateYear(year);
            break;
        } catch (ValidationException&ex) {
            cout <<ex.what()<<endl;
        }
    }
    while(true){
        try{
            cout<<"Enter the month: "<<endl;
            getline(cin,month_string);
            this->eventValidator.validateMonthString(month_string);
            month= stoi(month_string);
            this->eventValidator.validateMonth(month);
            break;
        } catch (ValidationException&ex) {
            cout <<ex.what()<<endl;
        }
    }
    while(true){
        try{
            cout<<"Enter the day: "<<endl;
            getline(cin,day_string);
            this->eventValidator.validateDayString(day_string);
            day= stoi(day_string);
            this->eventValidator.validateDay(day);
            break;
        } catch (ValidationException&ex) {
            cout <<ex.what()<<endl;
        }
    }
    while(true){
        try{
            cout<<"Enter the hour: "<<endl;
            getline(cin,hour_string);
            this->eventValidator.validateHourString(hour_string);
            hour= stoi(hour_string);
            this->eventValidator.validateHour(hour);
            break;
        } catch (ValidationException&ex) {
            cout <<ex.what()<<endl;
        }
    }
    while(true){
        try{
            cout<<"Enter the minute: "<<endl;
            getline(cin,minute_string);
            this->eventValidator.validateMinuteString(minute_string);
            minute= stoi(minute_string);
            this->eventValidator.validateMinute(minute);
            break;
        } catch (ValidationException&ex) {
            cout <<ex.what()<<endl;
        }
    }
    while(true){
        try{
            cout<<"Enter the number of people: "<<endl;
            getline(cin,numberOfPeople_string);
            this->eventValidator.validateNumberOfPeopleString(numberOfPeople_string);
            numberOfPeople= stoi(numberOfPeople_string);
            this->eventValidator.validateNumberOfPeople(numberOfPeople);
            break;
        } catch (ValidationException&ex) {
            cout <<ex.what()<<endl;
        }
    }
    while(true){
        try{
            cout<<"Enter the link: "<<endl;
            getline(cin, link_string);
            this->eventValidator.validateLink(link_string);
            break;
        }catch (ValidationException&ex){
            cout<<ex.what()<<endl;
        }
    }
    this->service.updateService(old_title,title_string,description_string, DateTime(year,month,day,hour,minute),numberOfPeople,link_string);
    cout<<"Event updated successfully!"<<endl;
}

void Console::listAll() {
    vector<Event>events = this->service.getAllService();
    int index=0;
    for(const Event&event:events){
        cout<<index+1<<". "<<event.toString()<<endl;
        index++;
    }
}

void Console::listAllUser() {
    string option;
    bool done = false;
    int index = 0;
    int length = this->service.getNrElemsService();
    while (!done) {
        if (length == 0) {
            string error;
            error+=string("The database is empty");
            if(!error.empty())
                throw RepositoryException(error);
        }
        if (index == length)
            index = 0;
        cout<< this->service.getAllService()[index].toString() << endl;
        cout<<"Interested in the event? : yes/no/exit"<<endl;
        getline(cin, option);
        if (option == "yes") {
            Event event = this->service.getAllService()[index];
            this->service.updateService(event.getTitle(),event.getTitle(),event.getDescription(),event.getDateTime(),event.getNumberOfPeople()+1,event.getLink());
            this->userService.addUserService(Event(event.getTitle(),event.getDescription(),event.getDateTime(),event.getNumberOfPeople()+1,event.getLink()));
            length = this->service.getNrElemsService();
        }
        else if (option == "no") {
            index++;
        }
        else if (option == "exit")
            done = true;
        else
            cout<<"Invalid input"<<endl;
        if (length == 0)
            done = true;
    }
}

void Console::listFilteredUser() {
    string month_string;
    int month;
    cout<<"Enter the month: "<<endl;
    getline(cin, month_string);
    this->eventValidator.validateMonthString(month_string);
    month= stoi(month_string);
    this->eventValidator.validateMonth(month);
    vector<Event> validEvents;
    validEvents.reserve(this->service.getNrElemsService());
    int length=this->userService.getFiltered(validEvents,month);
    if (validEvents.empty()) {
        string error;
        error+=string("The list of valid events is empty!");
        if(!error.empty())
            throw UserException(error);
    }
    string option;
    bool done = false;
    int index = 0;
    while (!done){
        if (validEvents.empty()){
            string error;
            error+=string("The list of valid events is empty!");
            if(!error.empty())
                throw UserException(error);
        }
        if (index == validEvents.size())
            index = 0;
        cout<< validEvents[index].toString() << endl;
        if (index==0){
            string link = string("start ").append(validEvents[index].getLink());
            system(link.c_str());
        }
        cout<<"Interested in the event? : yes/no/exit"<<endl;
        getline(cin, option);
        if (option == "yes") {
            Event event = validEvents[index];
            this->service.updateService(event.getTitle(),event.getTitle(),event.getDescription(),event.getDateTime(),event.getNumberOfPeople()+1,event.getLink());
            this->userService.addUserService(Event(event.getTitle(),event.getDescription(),event.getDateTime(),event.getNumberOfPeople()+1,event.getLink()));
            validEvents.erase(validEvents.begin()+index);
        }
        else if (option == "no") {
            index++;
        }
        else if (option == "exit")
            done = true;
        else
            cout<<"Invalid input"<<endl;
    }
}

void Console::listInterestedList() {
    vector<Event> interestedInEvents = this->userService.getAllUserService();
    int index=0;
    for(const Event&event:interestedInEvents){
        cout<<index+1<<". "<<event.toString()<<endl;
        index++;
    }
}

void Console::openFile(){
    string link=string("start ").append(this->userService.getFileService());
    system(link.c_str());
}

void Console::deleteUserEvent() {
    cout<<"Delete event from your list"<<endl;
    string title;
    while(true){
        try{
            cout<<"Enter the title:"<<endl;
            getline(cin,title);
            this->eventValidator.validateTitle(title);
            break;
        }catch (ValidationException&ex){
            cout<<ex.what()<<endl;
        }
    }

    int deleted = this->userService.deleteUserService(title);
    if (deleted == 0){
        cout<<"Event successfully deleted!"<<endl;
    }
    else if (deleted == 1)
        throw "The event is not in your list!";
}

void Console::printAdministratorSubmenu() {
    cout<<"ADMIN: "<<endl;
    cout<<"0. Exit"<<endl;
    cout<<"1. List all the events in the database."<<endl;
    cout<<"2. Add a new event."<<endl;
    cout<<"3. Delete an event."<<endl;
    cout<<"4. Update an event."<<endl;
    cout<<"Choose an option: "<<endl;
}

void Console::printUserSubmenu() {
    cout<<"USER: "<<endl;
    cout<<"0. Exit."<<endl;
    cout<<"1. See all the events, one by one."<<endl;
    cout<<"2. See all the events from a given month, one by one."<<endl;
    cout<<"3. See the events you are interested in."<<endl;
    cout<<"4. Delete one of the events you are not interested in anymore."<<endl;
    cout<<"5. See the file of the events you are interested in: "<<endl;
    cout<<"Choose an option: "<<endl;
}

void Console::AdministratorMode() {
    cout<<"You are in admin mode"<<endl;
    bool done = false;
    while (!done) {
        try {
            printAdministratorSubmenu();
            string option;
            getline(cin, option);
            if (option == "0") {
                done = true;
                cout << "Exiting admin mode..." << endl;
            } else if (option == "1")
                this->listAll();
            else if (option == "2")
                this->addUi();
            else if (option == "3")
                this->deleteUi();
            else if (option == "4")
                this->updateUi();
            else
                cout << "Bad input!"<<endl;
        }catch (ValidationException&ex) {
            cout<<ex.what()<<endl;
        }catch (const RepositoryException&ex){
            cout<<ex.what()<<endl;
        }
    }
}

void Console::UserMode() {
    cout<<"You are in user mode"<<endl;
    bool done = false;
    while(!done) {
        try {
            printUserSubmenu();
            string option;
            getline(cin, option);
            if (option == "0") {
                done = true;
                cout<<"Exiting user mode..."<<endl;
            }
            else if (option == "1")
                this->listAllUser();
            else if (option == "2")
                this->listFilteredUser();
            else if (option == "3")
                this->listInterestedList();
            else if (option == "4")
                this->deleteUserEvent();
            else if (option == "5")
                this->openFile();
            else
                cout<<"Bad input!"<<endl;
        }catch (ValidationException&ex) {
            cout<<ex.what()<<endl;
        }catch (UserException&ex) {
            cout<<ex.what()<<endl;
        }catch (RepositoryException&ex){
            cout<<ex.what()<<endl;
        }
    }
}

void Console::printMenu() {
    cout<<"MENU:"<<endl;
    cout<<"0. Exit."<<endl;
    cout<<"1. Administrator mode."<<endl;
    cout<<"2. User mode."<<endl;
    cout<<"Choose an option: "<<endl;
}

void Console::start() {
    cout<<"Life after school app"<<endl;
    int firstTimeUser=0;
    bool done = false;
    while (!done) {
        printMenu();
        string option;
        getline(cin,option);
        if (option == "1")
            AdministratorMode();
        else if (option == "2") {
            if (firstTimeUser == 0) {
                cout << "Enter the type of the file in which you want to save the list of your events(csv or html):"
                          << endl;
                string fileType;
                while (true) {
                    try {
                        getline(cin, fileType);
                        this->userService.repositoryType(fileType);
                        break;
                    } catch (UserException &ex) {
                        cout << ex.what() << std::endl;
                    }
                }
                firstTimeUser = 1;
            }
            UserMode();
        }else if (option == "0") {
            done = true;
            cout << "Goodbye!" << endl;
        }else
            cout<<"Bad input!"<<endl;
    }


}

Console::~Console() = default;