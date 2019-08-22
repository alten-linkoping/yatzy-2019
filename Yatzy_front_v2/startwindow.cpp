#include "startwindow.h"
#include "ui_startwindow.h"
#include <QJsonDocument>
#include <QJsonValue>
#include <QJsonArray>
#include <QJsonObject>

StartWindow::StartWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::StartWindow)
{
    ui->setupUi(this);
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
            QJsonArray jsonArrayUpper = jsonObject["msg"].toArray();

           qDebug() << jsonObject["msg"];
    }
);
}

StartWindow::~StartWindow()
{
    delete ui;
    delete manager;
}


void StartWindow::on_pushButton_PLAY_clicked()
{
    QString Player = ui->lineEdit->text();
    this->Players.push_back(Player.toStdString());

    MainWindow *w = new MainWindow;
    w->show();
    this->hide();
}

void StartWindow::on_pushButton_ADD_clicked()
{
    QString Player = ui->lineEdit->text();
    this->Players.push_back(Player.toStdString());

    request.setUrl(QUrl("http://127.0.0.1:5000/"));
    request.setHeader( QNetworkRequest::ContentTypeHeader, "/" );

    QByteArray dice;


    manager->post(request, dice);


    ui->lineEdit->clear();
}

