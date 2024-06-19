#include "gui.h"
#include <QVBoxLayout>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QMessageBox>
#include <sstream>

MainWindow::MainWindow(Service& service, QWidget* parent)
    : QMainWindow(parent), service(service) {
    QWidget* centralWidget = new QWidget(this);
    setCentralWidget(centralWidget);

    QVBoxLayout* layout = new QVBoxLayout(centralWidget);

    nameEdit = new QLineEdit(this);
    emailEdit = new QLineEdit(this);
    interestsEdit = new QLineEdit(this);
    addButton = new QPushButton("Add Volunteer", this);

    layout->addWidget(new QLabel("Name:"));
    layout->addWidget(nameEdit);
    layout->addWidget(new QLabel("Email:"));
    layout->addWidget(emailEdit);
    layout->addWidget(new QLabel("Interests (comma-separated):"));
    layout->addWidget(interestsEdit);
    layout->addWidget(addButton);

    connect(addButton, &QPushButton::clicked, this, &MainWindow::addVolunteer);

    displayDepartments();
}

void MainWindow::displayDepartments() {
    auto departments = service.getAllDepartments();
    for (auto* department : departments) {
        DepartmentWindow* window = new DepartmentWindow(service, department, this);
        departmentWindows.push_back(window);
        window->show();
    }
}

void MainWindow::addVolunteer() {
    QString name = nameEdit->text();
    QString email = emailEdit->text();
    std::string interestsStr = interestsEdit->text().toStdString();
    std::vector<std::string> interests;

    std::istringstream tokenStream(interestsStr);
    std::string token;
    while (std::getline(tokenStream, token, ',')) {
        interests.push_back(token);
    }

    if (name.isEmpty() || email.isEmpty()) {
        QMessageBox::warning(this, "Error", "Name and email cannot be empty.");
        return;
    }

    try {
        service.addNewVolunteer(name.toStdString(), email.toStdString(), interests);
        QMessageBox::information(this, "Success", "Volunteer added successfully!");
    }
    catch (const std::exception& e) {
        QMessageBox::critical(this, "Error", QString::fromStdString(e.what()));
    }
}

MainWindow::~MainWindow() {
    service.getRepository().saveVolunteers("volunteers.txt");
}
