#pragma once
#include <QFile>
#include <QTextStream>
#include <QDebug>
#include <QStringList>
#include <QList>
#include "MedicalDisorder.h"
#include <algorithm>
#include <iostream>

class Controller {
private:
    QList<MedicalDisorder> disorders;

public:
     void loadFromFile(const QString& filePath);
     QList<MedicalDisorder> getAllSortedByCategory();
     QList<MedicalDisorder> searchByCategoryOrName(const QString& text);
     QList<MedicalDisorder> searchByName(const QString& name);
};
