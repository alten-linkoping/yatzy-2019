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

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();


    void draw();
    void draw_dice();
    void roll_dice();
    std::vector<int> Dice {1, 2, 3, 4, 5};
    std::vector<int> locked_dice {0, 0, 0, 0, 0};
    std::vector<std::string> Players;
    int current_player;
    int throws_left = 3;
    QStandardItemModel *mod = new QStandardItemModel;
    void draw_scoreboard();

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
};

#endif // MAINWINDOW_H
