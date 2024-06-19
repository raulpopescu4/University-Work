#pragma once

#include <QMainWindow>
#include <QLabel>
#include <QListWidget>
#include <QPushButton>
#include <QLineEdit>
#include <QMessageBox>
#include <QVBoxLayout>
#include <QWidget>
#include "Service.h"
#include "Department.h"
#include "Observer.h"

class DepartmentWindow : public QMainWindow, public Observer {
    Q_OBJECT

public:
    DepartmentWindow(Service& service, Department* department, QWidget* parent = nullptr);
    ~DepartmentWindow();
    void updateVolunteerLists();
    void update() override;

private slots:
    void addVolunteer();
    void updateUnassignedList();

private:
    Service& service;
    Department* department;
    QListWidget* volunteerList;
    QListWidget* unassignedVolunteerList;
    QLineEdit* nameEdit;
    QLineEdit* emailEdit;
    QLineEdit* interestsEdit;
    QPushButton* addButton;
   // QPushButton* refreshButton;
};
