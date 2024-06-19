#pragma once

#include <QMainWindow>
#include <QPushButton>
#include <QLineEdit>
#include <QLabel>
#include <QListWidget>
#include <QMessageBox>
#include <QVBoxLayout>
#include <QWidget>
#include "Service.h"
#include "DepartmentWindow.h"


class MainWindow : public QMainWindow {
    Q_OBJECT

public:
    explicit MainWindow(Service& service, QWidget* parent = nullptr);
    void displayDepartments();
    ~MainWindow();

private slots:
    void addVolunteer();

private:
    Service& service;
    QLineEdit* nameEdit;
    QLineEdit* emailEdit;
    QLineEdit* interestsEdit;
    QPushButton* addButton;
    std::vector<DepartmentWindow*> departmentWindows;
};
