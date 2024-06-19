#include "gui.h"
#include <QtWidgets/QApplication>

int main(int argc, char* argv[]) {
    QApplication app(argc, argv);

    Repository repo;
    repo.loadDepartments("departments.txt");
    repo.loadVolunteers("volunteers.txt");

    Service service(repo);
    MainWindow mainWindow(service);
    mainWindow.show();

    return app.exec();
}
