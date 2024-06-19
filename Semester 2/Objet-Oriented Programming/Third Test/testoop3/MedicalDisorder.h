#pragma once
#include <QString>
#include <QStringList>

class MedicalDisorder {
public:
    QString category;
    QString name;
    QStringList symptoms;

    MedicalDisorder() {}

    MedicalDisorder(const QString& category, const QString& name, const QStringList& symptoms)
        : category(category), name(name), symptoms(symptoms) {}
};
