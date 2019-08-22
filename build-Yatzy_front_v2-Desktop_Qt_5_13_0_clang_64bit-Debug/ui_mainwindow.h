/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.13.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTableView>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QPushButton *pushButton_Dice1;
    QPushButton *pushButton_Dice2;
    QPushButton *pushButton_Dice3;
    QPushButton *pushButton_Dice4;
    QPushButton *pushButton_Dice5;
    QPushButton *pushButton_Roll;
    QTableView *tableView_scoreboard;
    QPushButton *pushButton_EndTurn;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(1100, 697);
        MainWindow->setStyleSheet(QString::fromUtf8("background-color: rgb(16, 128, 64);"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        pushButton_Dice1 = new QPushButton(centralwidget);
        pushButton_Dice1->setObjectName(QString::fromUtf8("pushButton_Dice1"));
        pushButton_Dice1->setGeometry(QRect(600, 350, 81, 71));
        pushButton_Dice1->setStyleSheet(QString::fromUtf8("border-image: url(:/Images/Images/Alea_1.png);\n"
"color: rgb(128, 0, 2);\n"
"\n"
""));
        pushButton_Dice1->setFlat(false);
        pushButton_Dice2 = new QPushButton(centralwidget);
        pushButton_Dice2->setObjectName(QString::fromUtf8("pushButton_Dice2"));
        pushButton_Dice2->setGeometry(QRect(770, 350, 81, 71));
        pushButton_Dice2->setStyleSheet(QString::fromUtf8("border-image: url(:/Images/Images/Alea_1.png);"));
        pushButton_Dice3 = new QPushButton(centralwidget);
        pushButton_Dice3->setObjectName(QString::fromUtf8("pushButton_Dice3"));
        pushButton_Dice3->setGeometry(QRect(930, 350, 81, 71));
        pushButton_Dice3->setStyleSheet(QString::fromUtf8("border-image: url(:/Images/Images/Alea_1.png);"));
        pushButton_Dice4 = new QPushButton(centralwidget);
        pushButton_Dice4->setObjectName(QString::fromUtf8("pushButton_Dice4"));
        pushButton_Dice4->setGeometry(QRect(680, 490, 81, 71));
        pushButton_Dice4->setStyleSheet(QString::fromUtf8("border-image: url(:/Images/Images/Alea_1.png);"));
        pushButton_Dice5 = new QPushButton(centralwidget);
        pushButton_Dice5->setObjectName(QString::fromUtf8("pushButton_Dice5"));
        pushButton_Dice5->setGeometry(QRect(860, 490, 81, 71));
        pushButton_Dice5->setStyleSheet(QString::fromUtf8("border-image: url(:/Images/Images/Alea_1.png);"));
        pushButton_Roll = new QPushButton(centralwidget);
        pushButton_Roll->setObjectName(QString::fromUtf8("pushButton_Roll"));
        pushButton_Roll->setGeometry(QRect(800, 20, 201, 91));
        pushButton_Roll->setStyleSheet(QString::fromUtf8("background-color: rgb(128, 0, 2);\n"
"font: 24pt \".SF NS Text\";"));
        tableView_scoreboard = new QTableView(centralwidget);
        tableView_scoreboard->setObjectName(QString::fromUtf8("tableView_scoreboard"));
        tableView_scoreboard->setGeometry(QRect(40, 10, 371, 601));
        tableView_scoreboard->setStyleSheet(QString::fromUtf8("color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);"));
        pushButton_EndTurn = new QPushButton(centralwidget);
        pushButton_EndTurn->setObjectName(QString::fromUtf8("pushButton_EndTurn"));
        pushButton_EndTurn->setGeometry(QRect(590, 20, 141, 91));
        pushButton_EndTurn->setStyleSheet(QString::fromUtf8("background-color: rgb(128, 0, 2);\n"
"font: 24pt \".SF NS Text\";"));
        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 1100, 22));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        pushButton_Dice1->setText(QString());
        pushButton_Dice2->setText(QString());
        pushButton_Dice3->setText(QString());
        pushButton_Dice4->setText(QString());
        pushButton_Dice5->setText(QString());
        pushButton_Roll->setText(QCoreApplication::translate("MainWindow", "Roll The Dice", nullptr));
        pushButton_EndTurn->setText(QCoreApplication::translate("MainWindow", "End Turn", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
