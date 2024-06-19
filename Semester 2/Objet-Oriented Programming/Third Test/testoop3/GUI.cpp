#include "GUI.h"

GUI::GUI(Controller& _controller) : controller(_controller)
{
    this->disorderListWidget = new QListWidget();
    this->searchLineEdit = new QLineEdit();
    this->symptomSearchLineEdit = new QLineEdit();
    this->symptomSearchButton = new QPushButton("&Show Symptoms");

    initializeGUI();
    populateDisorderList();
    connectSignalsAndSlots();
}

void GUI::initializeGUI()
{
    this->setWindowTitle("Medical Disorders");

    QHBoxLayout* searchLayout = new QHBoxLayout();
    this->searchLineEdit->setPlaceholderText("Search by category or name...");
    searchLayout->addWidget(this->searchLineEdit);

    QHBoxLayout* symptomSearchLayout = new QHBoxLayout();
    this->symptomSearchLineEdit->setPlaceholderText("Enter disorder name...");
    symptomSearchLayout->addWidget(this->symptomSearchLineEdit);
    symptomSearchLayout->addWidget(this->symptomSearchButton);

    this->mainLayout = new QVBoxLayout(this);
    this->mainLayout->addLayout(searchLayout);
    this->mainLayout->addLayout(symptomSearchLayout);
    this->mainLayout->addWidget(this->disorderListWidget);

}

void GUI::populateDisorderList()
{
    QList<MedicalDisorder> disorders = controller.getAllSortedByCategory();

    this->disorderListWidget->clear();
    for (const MedicalDisorder& disorder : disorders) {
        QListWidgetItem* newItem = new QListWidgetItem;
        newItem->setText(disorder.name + " | " + disorder.category);
        this->disorderListWidget->addItem(newItem);
    }
}

void GUI::connectSignalsAndSlots()
{
    QObject::connect(this->searchLineEdit, &QLineEdit::textChanged, this, &GUI::refreshListBasedOnSearch);
    QObject::connect(this->symptomSearchButton, &QPushButton::clicked, this, &GUI::showSymptomsForDisorder);
}

void GUI::refreshListBasedOnSearch()
{
    QString searchTerm = this->searchLineEdit->text();
    QList<MedicalDisorder> filteredDisorders = controller.searchByCategoryOrName(searchTerm);

    this->disorderListWidget->clear();
    for (const MedicalDisorder& disorder : filteredDisorders) {
        QListWidgetItem* newItem = new QListWidgetItem;
        newItem->setText(disorder.name + " | " + disorder.category);
        this->disorderListWidget->addItem(newItem);
    }
}

void GUI::showSymptomsForDisorder()
{
    QString disorderName = this->symptomSearchLineEdit->text();
    QList<MedicalDisorder> filteredDisorders = controller.searchByName(disorderName);

    this->disorderListWidget->clear();
    for (const MedicalDisorder& disorder : filteredDisorders) {
        QListWidgetItem* newItem = new QListWidgetItem;
        newItem->setText(disorder.name + ": " + disorder.symptoms.join(", "));
        this->disorderListWidget->addItem(newItem);
    }

   
}

GUI::~GUI()
{
}
