#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QLabel>
#include <QPushButton>
#include <string>
#include "dice_side.h"
#include "dice.h"
#include "alternativeswindow.h"
#include <vector>
#include <cstdlib>
#include <ctime>
#include <QStandardItem>
#include <QStandardItemModel>
#include <QNetworkAccessManager>
#include <QNetworkRequest>
#include <QNetworkReply>
#include <QJsonObject>
namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow( QJsonObject gameSetup, QWidget *parent = nullptr);
    ~MainWindow();


    void draw();
    void draw_dice();
    void roll_dice();
    std::vector<int> Dice {1, 2, 3, 4, 5};
    std::vector<int> locked_dice {0, 0, 0, 0, 0};
    std::vector<QString> Players;
    int current_player;
    int throws_left = 3;
    QStandardItemModel *mod = new QStandardItemModel;
    void draw_scoreboard();
    void draw_scoreboard(QJsonObject);

private slots:
    void on_pushButton_Roll_clicked();

    void on_pushButton_Dice1_clicked();

    void on_pushButton_Dice2_clicked();

    void on_pushButton_Dice3_clicked();

    void on_pushButton_Dice4_clicked();

    void on_pushButton_Dice5_clicked();

    void on_pushButton_EndTurn_clicked();

private:
    Ui::MainWindow *ui;
    QNetworkAccessManager *manager;
    QNetworkRequest request;
    QString game_id;
    std::vector<QString> combinations {"ones", "twos", "threes", "fours", "fives", "sixes", "_bonus","total_score","one_pair",
                                           "two_pairs","three_of_a_kind","four_of_a_kind","small_straight","large_straight",
                                           "full_house", "chance", "yatzy", "total_score", "total_score"};
    std::vector<QString> combination_choices {"ones", "twos", "threes", "fours", "fives", "sixes","one_pair",
                                           "two_pairs","three_of_a_kind","four_of_a_kind","small_straight","large_straight",
                                           "full_house", "chance", "yatzy"};
    std::vector<QString> upper_section {"ones", "twos", "threes", "fours", "fives", "sixes", "_bonus","total_score"};
    std::vector<QString> lower_section {"one_pair","two_pairs","three_of_a_kind","four_of_a_kind","small_straight","large_straight",
                                           "full_house", "chance", "yatzy", "total_score"};
    QString total_score{"total_score"};

    QJsonObject latestReply;
};

#endif // MAINWINDOW_H
