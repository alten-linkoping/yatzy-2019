#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QHBoxLayout>
#include <QPushButton>
#include <QDebug>
#include <QNetworkAccessManager>
#include <QNetworkRequest>
#include <QNetworkReply>
#include <QUrlQuery>
#include <random>
#include <string>
#include <array>
#include <QTextCodec>
#include <QJsonDocument>
#include <QJsonValue>
#include <QJsonArray>
#include <QJsonObject>


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    this->Players.push_back("Emma");
    this->Players.push_back("Liv");

    manager = new QNetworkAccessManager();
    QObject::connect(manager, &QNetworkAccessManager::finished,
        this, [=](QNetworkReply *reply) {
            if (reply->error()) {
                qDebug() << reply->errorString();
                return;
            }

            QString answer = reply->readAll();

            qDebug() << answer;

            QJsonDocument json = QJsonDocument::fromJson(answer.toUtf8());
            QJsonObject jsonObject = json.object();
            QJsonArray jsonArrayUpper = jsonObject["upper"].toArray();

            qDebug() << jsonArrayUpper;



            QJsonObject ar1 = jsonArrayUpper.at(0).toObject();
            qDebug() << ar1["chance"].toDouble();






            //qDebug() << jsonObject["chance"].toArray();
            //qDebug() << jsonObject["OnePair"].toArray();
            //qDebug() << jsonObject["TwoPairs"].toArray();
            //qDebug() << jsonObject["ThreeOf"].toArray();
            //qDebug() << jsonObject["upper"].toArray();
            //qDebug() << jsonString;

        }
    );
}

MainWindow::~MainWindow()
{
    delete ui;
     delete manager;
}

// Tärningssidor

static Dice_side DS1 {"border-image: url(:/Images/Images/Alea_1.png); color: rgb(128, 0, 2)", 1};
static Dice_side DS2 {"border-image: url(:/Images/Images/Alea_2.png); color: rgb(128, 0, 2)", 2};
static Dice_side DS3 {"border-image: url(:/Images/Images/Alea_3.png); color: rgb(128, 0, 2)", 3};
static Dice_side DS4 {"border-image: url(:/Images/Images/Alea_4.png); color: rgb(128, 0, 2)", 4};
static Dice_side DS5 {"border-image: url(:/Images/Images/Alea_5.png); color: rgb(128, 0, 2)", 5};
static Dice_side DS6 {"border-image: url(:/Images/Images/Alea_6.png); color: rgb(128, 0, 2)", 6};

// Scoreboard


void MainWindow::roll_dice()
{
    srand(time(nullptr));

    request.setUrl(QUrl("http://127.0.0.1:5000/sign_in"));
    request.setHeader( QNetworkRequest::ContentTypeHeader, "/" );
    QByteArray dice;
    for (int idx = 0; idx < 5; ++idx)
    {
        if (this->locked_dice[idx] == 0)
        {
            int random_value = std::rand() %6 + 1;
            this->Dice[idx] = random_value;
            dice.push_back(random_value);

        }








        manager->post(request, dice);
    }


}

void MainWindow::draw_dice()
{
    static std::vector<QPushButton *> Dice_buttons {ui->pushButton_Dice1, ui->pushButton_Dice2, ui->pushButton_Dice3, ui->pushButton_Dice4, ui->pushButton_Dice5};

   //ui->pushButton_Dice1->setStyleSheet((QString::fromStdString(DS6.get_image())));

    for (int idx = 0; idx < 5; ++idx)
    {
        switch (this->Dice[idx])
        {
            case(1): Dice_buttons[idx]->setStyleSheet((QString::fromStdString(DS1.get_image())));
            break;
            case(2): Dice_buttons[idx]->setStyleSheet((QString::fromStdString(DS2.get_image())));
            break;
            case(3): Dice_buttons[idx]->setStyleSheet((QString::fromStdString(DS3.get_image())));
            break;
            case(4): Dice_buttons[idx]->setStyleSheet((QString::fromStdString(DS4.get_image())));
            break;
            case(5): Dice_buttons[idx]->setStyleSheet((QString::fromStdString(DS5.get_image())));
            break;
            case(6): Dice_buttons[idx]->setStyleSheet((QString::fromStdString(DS6.get_image())));
            break;
        }
    }
}

void MainWindow::draw()
{
    //ui->pushButton_Dice1->setStyleSheet((QString::fromStdString(DS6.get_image())));
    this->roll_dice();
    this->draw_dice();
}

void MainWindow::on_pushButton_Roll_clicked()
{
    if (this->throws_left > 0)
    {
        this->draw();
        this->throws_left = this->throws_left - 1;
    }
}


void MainWindow::on_pushButton_Dice1_clicked()
{
    if (this->locked_dice[0] == 0 && this->throws_left != 3)
    {
        this->locked_dice[0] = 1;
        ui->pushButton_Dice1->setText("LOCKED");
    }
    else {
        this->locked_dice[0] = 0;
        ui->pushButton_Dice1->setText("");
    }
}

void MainWindow::on_pushButton_Dice2_clicked()
{
    if (this->locked_dice[1] == 0 && this->throws_left != 3)
    {
        this->locked_dice[1] = 1;
        ui->pushButton_Dice2->setText("LOCKED");
    }
    else {
        this->locked_dice[1] = 0;
        ui->pushButton_Dice2->setText("");
    }
}

void MainWindow::on_pushButton_Dice3_clicked()
{
    if (this->locked_dice[2] == 0 && this->throws_left != 3)
    {
        this->locked_dice[2] = 1;
        ui->pushButton_Dice3->setText("LOCKED");
    }
    else {
        this->locked_dice[2] = 0;
        ui->pushButton_Dice3->setText("");
    }
}

void MainWindow::on_pushButton_Dice4_clicked()
{
    if (this->locked_dice[3] == 0 && this->throws_left != 3)
    {
        this->locked_dice[3] = 1;
        ui->pushButton_Dice4->setText("LOCKED");
    }
    else {
        this->locked_dice[3] = 0;
        ui->pushButton_Dice4->setText("");
    }
}

void MainWindow::on_pushButton_Dice5_clicked()
{
    if (this->locked_dice[4] == 0 && this->throws_left != 3)
    {
        this->locked_dice[4] = 1;
        ui->pushButton_Dice5->setText("LOCKED");
    }
    else {
        this->locked_dice[4] = 0;
        ui->pushButton_Dice5->setText("");
    }
}

void MainWindow::on_pushButton_EndTurn_clicked()
{







    if(this->throws_left != 3)
    {
        //Skicka tärningsvärdena till servern
        this->throws_left = 3;

        for (int i = 0; i < 5; i++) {
            this->locked_dice[i] = 0;
        }
        this->on_pushButton_Dice1_clicked();
        this->on_pushButton_Dice2_clicked();
        this->on_pushButton_Dice3_clicked();
        this->on_pushButton_Dice4_clicked();
        this->on_pushButton_Dice5_clicked();



    }

}

void MainWindow::draw_scoreboard()
{
    std::vector<std::string> Combinations {"Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "Bonus","Sum","One Pair",
                                           "Two Pairs","Three of a Kind   ","Four of a Kind ","Small Straight ","Large Straight ",
                                           "Full House", "Chance", "YATZY", "Sum", "Total"};


    for (int var = 0; var < 2; ++var) {
        QStandardItem *it1 = new QStandardItem(QObject::tr(this->Players[var].c_str()));
        this->mod->setHorizontalHeaderItem(var,it1);
    }

    for (int idx = 0; idx < Combinations.size(); idx++)
    {
        QStandardItem *it1 = new QStandardItem(QObject::tr(Combinations[idx].c_str()));
        this->mod->setVerticalHeaderItem(idx,it1);
        const QModelIndex index = this->mod->index(idx+1, 1);
        this->mod->setData(index, Qt::AlignCenter, Qt::TextAlignmentRole);
        this->mod->setData(index, "0");
    }

    ui->tableView_scoreboard->setModel(this->mod);
    ui->tableView_scoreboard->show();
}
