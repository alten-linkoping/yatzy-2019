#ifndef ALTERNATIVESWINDOW_H
#define ALTERNATIVESWINDOW_H

#include <QDialog>

namespace Ui {
class AlternativesWindow;
}

class AlternativesWindow : public QDialog
{
    Q_OBJECT

public:
    explicit AlternativesWindow(QWidget *parent = nullptr);
    ~AlternativesWindow();
    std::vector<std::string> alternatives;

private slots:
    void on_buttonBox_accepted();
    void is_clicked();
    void on_buttonBox_rejected();

private:
    Ui::AlternativesWindow *ui;
    int clicked = 0;
};

#endif // ALTERNATIVESWINDOW_H
