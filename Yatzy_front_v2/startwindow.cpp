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
            qDebug()<< "JSON OBJECT" << jsonObject << endl;

            this->gameSetup = jsonObject;

        }
);
}
StartWindow::~StartWindow()
{
    delete ui;
    delete manager;
}
/*
QByteArray postData;
    QJsonObject qJson;

    QJsonArray diceDataArray;
    for(int i : diceData){
        diceDataArray.append(QString::number(i));
    }

    qJson.insert("dice",diceDataArray);
    qJson.insert("player_id",playerId);

    QNetworkRequest request(qurl);
    request.setHeader(QNetworkRequest::ContentTypeHeader,"application/json");

    return network_manager.post(request,QJsonDocument(qJson).toJson());
*/

void StartWindow::on_pushButton_PLAY_clicked()
{
    QString Player = ui->lineEdit->text();
    this->Players.push_back(Player.toStdString());

    request.setUrl(QUrl("http://10.46.52.103:5000/game"));
    request.setHeader( QNetworkRequest::ContentTypeHeader,"application/json");

    QJsonObject qJson;
    QJsonArray diceDataArray;

    for(std::string i : this->Players){
        diceDataArray.append(QString::fromStdString(i));
    }

    qJson.insert("player_names", diceDataArray);
    QEventLoop loop{};
    connect(manager,SIGNAL(finished(QNetworkReply*)), &loop, SLOT(quit()));
    manager->post(request, QJsonDocument(qJson).toJson());
    loop.exec();
    qDebug() << "GENA SETIP --->>> " << this->gameSetup << endl;
    MainWindow *w = new MainWindow(this->gameSetup);
    w->show();
    this->hide();
}

void StartWindow::on_pushButton_ADD_clicked()
{
    QString Player = ui->lineEdit->text();
    this->Players.push_back(Player.toStdString());

    this->playersTosend.append(Player.toUtf8());

    ui->lineEdit->clear();
}

