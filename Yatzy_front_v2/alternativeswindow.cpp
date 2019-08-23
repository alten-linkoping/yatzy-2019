#include "alternativeswindow.h"
#include "ui_alternativeswindow.h"
#include <QRadioButton>
#include <QButtonGroup>
#include <QWidget>
#include <QLayout>
#include <QDebug>


AlternativesWindow::AlternativesWindow(QJsonObject combinationsObject, std::vector<QString> combinations, QWidget *parent) :
    QDialog(parent),
    ui(new Ui::AlternativesWindow)
{
    ui->setupUi(this);
    //this->alternatives = {"Alt1", "Alt 2", "Alt 3"};
    this->alternatives.clear();
    QJsonObject comb_field = combinationsObject["combinations"].toObject();
    for (QString rule: combinations){
        if(comb_field.contains(rule)){
            this->alternatives.push_back(rule);
        }
    }
    QVBoxLayout *layout = new QVBoxLayout(this);
    QButtonGroup* button_grp = new QButtonGroup(this);

    qDebug() << combinationsObject << endl;
    qDebug() << comb_field << endl;
    connect(button_grp, SIGNAL(buttonClicked(int)), this, SLOT(is_clicked(int)));
    for (int idx = 0; idx < this->alternatives.size(); idx++) {
        QRadioButton *RButton = new QRadioButton(ui->widget);
        button_grp->addButton(RButton, idx);
        QString rule_name{this->alternatives[idx]};
        RButton->setText(rule_name + ": " + QString::number(comb_field[rule_name].toInt()));
        layout->addWidget(RButton);
    }
    ui->widget->setLayout(layout);
    ui->widget->show();
}


AlternativesWindow::~AlternativesWindow()
{
    delete ui;
}

void AlternativesWindow::is_clicked(int button_id)
{
    this->clickedOption = this->alternatives[button_id];
    this->clicked = 1;
}


void AlternativesWindow::on_buttonBox_accepted()
{
    // if alternative chosen ... skicka ... close()
    // else felmeddelande
    if(this->clicked == 1)
    {
        emit(choice_made());
        this->close();
    }

}

void AlternativesWindow::on_buttonBox_rejected()
{
    //ev. felmeddelande
}
