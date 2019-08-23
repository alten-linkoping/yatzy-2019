#ifndef STARTWINDOW_H
#define STARTWINDOW_H

#include <QMainWindow>
#include "mainwindow.h"
#include <QJsonObject>
namespace Ui {
class StartWindow;
}

class StartWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit StartWindow(QWidget *parent = nullptr);
    ~StartWindow();
    std::vector<std::string> Players;
    QByteArray playersTosend;

private slots:
    void on_pushButton_PLAY_clicked();

    void on_pushButton_ADD_clicked();

private:
    Ui::StartWindow *ui;
    QNetworkAccessManager *manager;
    QNetworkRequest request;
    QJsonObject gameSetup;
};

#endif // STARTWINDOW_H
