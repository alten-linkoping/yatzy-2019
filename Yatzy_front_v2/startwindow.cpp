#include "startwindow.h"
#include "ui_startwindow.h"

StartWindow::StartWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::StartWindow)
{
    ui->setupUi(this);
}

StartWindow::~StartWindow()
{
    delete ui;
}


void StartWindow::on_pushButton_PLAY_clicked()
{
    QString Player = ui->lineEdit->text();
    this->Players.push_back(Player.toStdString());

    MainWindow *w = new MainWindow;
    w->Players = this->Players;
    w->show();
    this->hide();
}

void StartWindow::on_pushButton_ADD_clicked()
{
    QString Player = ui->lineEdit->text();
    this->Players.push_back(Player.toStdString());
    ui->lineEdit->clear();
}

