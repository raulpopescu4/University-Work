#include "DepartmentWindow.h"
#include <sstream>

DepartmentWindow::DepartmentWindow(Service& service, Department* department, QWidget* parent)
    : QMainWindow(parent), service(service), department(department) {
    setWindowTitle(QString::fromStdString(department->getName()));

    QWidget* centralWidget = new QWidget(this);
    setCentralWidget(centralWidget);
    QVBoxLayout* layout = new QVBoxLayout(centralWidget);

    QLabel* descriptionLabel = new QLabel(QString::fromStdString(department->getDescription()), this);
    layout->addWidget(descriptionLabel);

    volunteerList = new QListWidget(this);
    layout->addWidget(new QLabel("Department Volunteers:"));
    layout->addWidget(volunteerList);

    unassignedVolunteerList = new QListWidget(this);
    layout->addWidget(new QLabel("Unassigned Volunteers:"));
    layout->addWidget(unassignedVolunteerList);

    nameEdit = new QLineEdit(this);
    emailEdit = new QLineEdit(this);
    interestsEdit = new QLineEdit(this);
    addButton = new QPushButton("Add Volunteer", this);
  //  refreshButton = new QPushButton("Refresh Lists", this);

    layout->addWidget(new QLabel("Name:"));
    layout->addWidget(nameEdit);
    layout->addWidget(new QLabel("Email:"));
    layout->addWidget(emailEdit);
    layout->addWidget(new QLabel("Interests (comma-separated):"));
    layout->addWidget(interestsEdit);
    layout->addWidget(addButton);
  //  layout->addWidget(refreshButton);

    connect(addButton, &QPushButton::clicked, this, &DepartmentWindow::addVolunteer);
   // connect(refreshButton, &QPushButton::clicked, this, &DepartmentWindow::updateVolunteerLists);

 
    service.addObserver(this);

    updateVolunteerLists();
}

DepartmentWindow::~DepartmentWindow() {
   
    service.removeObserver(this);
}

std::vector<std::string> split(const std::string& str, char delimiter) {
    std::vector<std::string> tokens;
    std::string token;
    std::istringstream tokenStream(str);
    while (std::getline(tokenStream, token, delimiter)) {
        tokens.push_back(token);
    }
    return tokens;
}

void DepartmentWindow::addVolunteer() {
    QString name = nameEdit->text();
    QString email = emailEdit->text();
    std::vector<std::string> interests = split(interestsEdit->text().toStdString(), ',');

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

void DepartmentWindow::updateVolunteerLists() {
    volunteerList->clear();
    unassignedVolunteerList->clear();

    auto departmentVolunteers = service.getVolunteersForDepartment(department);
    auto allVolunteers = service.getAllVolunteers();

    for (auto& volunteer : departmentVolunteers) {
        volunteerList->addItem(QString::fromStdString(volunteer->getName()));
    }

    updateUnassignedList();
}

void DepartmentWindow::updateUnassignedList() {
    unassignedVolunteerList->clear();

    auto allVolunteers = service.getAllVolunteers();

    for (auto& volunteer : allVolunteers) {
        if (volunteer->getDepartment() == nullptr) {
            unassignedVolunteerList->addItem(QString::fromStdString(volunteer->getName()));
        }
    }
}

void DepartmentWindow::update() {
    updateVolunteerLists();
}
