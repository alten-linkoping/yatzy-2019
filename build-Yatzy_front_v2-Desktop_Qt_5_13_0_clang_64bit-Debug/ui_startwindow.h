/********************************************************************************
** Form generated from reading UI file 'startwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.13.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_STARTWINDOW_H
#define UI_STARTWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_StartWindow
{
public:
    QWidget *centralwidget;
    QTextBrowser *textBrowser;
    QTextBrowser *textBrowser_2;
    QPushButton *pushButton_ADD;
    QPushButton *pushButton_PLAY;
    QLineEdit *lineEdit;
    QMenuBar *menubar;
    QMenu *menuYatzy;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *StartWindow)
    {
        if (StartWindow->objectName().isEmpty())
            StartWindow->setObjectName(QString::fromUtf8("StartWindow"));
        StartWindow->resize(897, 545);
        StartWindow->setStyleSheet(QString::fromUtf8("background-color: rgb(16, 128, 64);"));
        centralwidget = new QWidget(StartWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        textBrowser = new QTextBrowser(centralwidget);
        textBrowser->setObjectName(QString::fromUtf8("textBrowser"));
        textBrowser->setGeometry(QRect(290, 20, 291, 101));
        textBrowser_2 = new QTextBrowser(centralwidget);
        textBrowser_2->setObjectName(QString::fromUtf8("textBrowser_2"));
        textBrowser_2->setGeometry(QRect(270, 210, 161, 51));
        pushButton_ADD = new QPushButton(centralwidget);
        pushButton_ADD->setObjectName(QString::fromUtf8("pushButton_ADD"));
        pushButton_ADD->setGeometry(QRect(520, 230, 181, 51));
        pushButton_ADD->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"));
        pushButton_PLAY = new QPushButton(centralwidget);
        pushButton_PLAY->setObjectName(QString::fromUtf8("pushButton_PLAY"));
        pushButton_PLAY->setGeometry(QRect(300, 370, 271, 91));
        pushButton_PLAY->setStyleSheet(QString::fromUtf8("background-color: rgb(128, 0, 2);\n"
"font: 34pt \".SF NS Text\";\n"
"color: rgb(255, 255, 255);"));
        lineEdit = new QLineEdit(centralwidget);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));
        lineEdit->setGeometry(QRect(270, 260, 221, 41));
        lineEdit->setStyleSheet(QString::fromUtf8("background-color: rgb(230, 230, 230);\n"
"font: 18pt \".SF NS Text\";\n"
"color: rgb(0, 0, 0);"));
        StartWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(StartWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 897, 22));
        menuYatzy = new QMenu(menubar);
        menuYatzy->setObjectName(QString::fromUtf8("menuYatzy"));
        StartWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(StartWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        StartWindow->setStatusBar(statusbar);

        menubar->addAction(menuYatzy->menuAction());

        retranslateUi(StartWindow);

        QMetaObject::connectSlotsByName(StartWindow);
    } // setupUi

    void retranslateUi(QMainWindow *StartWindow)
    {
        StartWindow->setWindowTitle(QCoreApplication::translate("StartWindow", "MainWindow", nullptr));
        textBrowser->setHtml(QCoreApplication::translate("StartWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.SF NS Text'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:64pt; font-weight:600; color:#ffffff;\">YATZY</span></p></body></html>", nullptr));
        textBrowser_2->setHtml(QCoreApplication::translate("StartWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.SF NS Text'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#ffffff;\">Enter player:</span></p></body></html>", nullptr));
        pushButton_ADD->setText(QCoreApplication::translate("StartWindow", "ADD MORE PLAYERS", nullptr));
        pushButton_PLAY->setText(QCoreApplication::translate("StartWindow", "PLAY", nullptr));
        menuYatzy->setTitle(QCoreApplication::translate("StartWindow", "Yatzy", nullptr));
    } // retranslateUi

};

namespace Ui {
    class StartWindow: public Ui_StartWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_STARTWINDOW_H
