#pragma once

#include <QtWidgets/QMainWindow>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QListWidget>
#include <QLineEdit>
#include <QPushButton>
#include "Controller.h"

class GUI : public QWidget
{
    Q_OBJECT  

private:
    QVBoxLayout* mainLayout;
    QListWidget* disorderListWidget;
    QLineEdit* searchLineEdit;
    QLineEdit* symptomSearchLineEdit;
    QPushButton* symptomSearchButton;

    Controller& controller;

    void initializeGUI();
    void populateDisorderList();
    void connectSignalsAndSlots();

public:
    explicit GUI(Controller& _controller);
    ~GUI() override;

private slots:
    void refreshListBasedOnSearch();
    void showSymptomsForDisorder();
};