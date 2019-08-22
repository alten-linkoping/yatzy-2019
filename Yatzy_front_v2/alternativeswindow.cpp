#include "alternativeswindow.h"
#include "ui_alternativeswindow.h"
#include <QRadioButton>
#include <QWidget>
#include <QLayout>


AlternativesWindow::AlternativesWindow(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::AlternativesWindow)
{
    ui->setupUi(this);
    this->alternatives = {"Alt1", "Alt 2", "Alt 3"};

    QVBoxLayout *layout = new QVBoxLayout;

    for (int idx = 0; idx < this->alternatives.size(); idx++) {
        QRadioButton *RButton = new QRadioButton(ui->widget);
        RButton->setText(tr(this->alternatives[idx].c_str()));
        //RButton->show();
        connect(RButton, SIGNAL(clicked()), this, SLOT(is_clicked()));
        layout->addWidget(RButton);
    }
    ui->widget->setLayout(layout);
    ui->widget->show();
}


AlternativesWindow::~AlternativesWindow()
{
    delete ui;
}

void AlternativesWindow::is_clicked()
{
    this->clicked = 1;
}


void AlternativesWindow::on_buttonBox_accepted()
{
    // if alternative chosen ... skicka ... close()
    // else felmeddelande
    if(this->clicked == 1)
    {
        this->close();
    }

}

void AlternativesWindow::on_buttonBox_rejected()
{
    //ev. felmeddelande
}
