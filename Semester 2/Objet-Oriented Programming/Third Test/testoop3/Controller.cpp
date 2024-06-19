#include "Controller.h"

void Controller::loadFromFile(const QString& filePath)
{
    QFile file(filePath);
    if (!file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        qDebug() << "File could not be open :(";
        return;
    }

    QTextStream in(&file);
    while (!in.atEnd()) {
        QString line = in.readLine();
        QStringList parts = line.split("|");
        if (parts.size() >= 3) {
            QString category = parts[0].trimmed();
            QString name = parts[1].trimmed();
            QStringList symptoms = parts[2].split(",");
            for (int i = 0; i < symptoms.size(); ++i) {
                symptoms[i] = symptoms[i].trimmed();
            }
            this->disorders.append(MedicalDisorder(category, name, symptoms));
        }
    }

    file.close();
    qDebug() << this->disorders.size();
}

QList<MedicalDisorder> Controller::getAllSortedByCategory()
{
    QList<MedicalDisorder> sortedDisorders = this->disorders;
    std::sort(sortedDisorders.begin(), sortedDisorders.end(), [](const MedicalDisorder& a, const MedicalDisorder& b) {
        return a.category < b.category;
        });
    return sortedDisorders;
}

QList<MedicalDisorder> Controller::searchByCategoryOrName(const QString& text)
{
    QList<MedicalDisorder> foundDisorders;
    for (const MedicalDisorder& disorder : this->disorders) {
        if (disorder.category.contains(text, Qt::CaseInsensitive) || disorder.name.contains(text, Qt::CaseInsensitive)) {
            foundDisorders.append(disorder);
        }
    }
    return foundDisorders;
}

QList<MedicalDisorder> Controller::searchByName(const QString& name)
{
    QList<MedicalDisorder> foundDisorders;
    for (const MedicalDisorder& disorder : this->disorders) {
        if (disorder.name.contains(name, Qt::CaseInsensitive)) {
            foundDisorders.append(disorder);
        }
    }
    return foundDisorders;
}
