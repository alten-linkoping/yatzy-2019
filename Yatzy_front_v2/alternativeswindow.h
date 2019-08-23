#ifndef ALTERNATIVESWINDOW_H
#define ALTERNATIVESWINDOW_H

#include <QDialog>
#include <QJsonObject>
#include <QAbstractButton>
#include <vector>
namespace Ui {
class AlternativesWindow;
}

class AlternativesWindow : public QDialog
{
    Q_OBJECT

public:
    explicit AlternativesWindow(QJsonObject combinationsObject, std::vector<QString> combinations, QWidget *parent = nullptr);
    ~AlternativesWindow();
    std::vector<QString> alternatives;
    QString clickedOption;

private slots:
    void on_buttonBox_accepted();
    void is_clicked(int button_id);
    void on_buttonBox_rejected();

private:
    Ui::AlternativesWindow *ui;
    int clicked = 0;


signals:
    void choice_made();
};
#endif // ALTERNATIVESWINDOW_H
