#include "GUI.h"
#include <stdio.h>
#include <QtWidgets/QApplication>
#include <iostream>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Controller controller;
    controller.loadFromFile("disorders.txt");
    GUI w(controller);
    w.show();
    return a.exec();
}
