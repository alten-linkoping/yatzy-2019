#include <QApplication>
#include "startwindow.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    StartWindow sw;
    sw.show();

    return a.exec();
}
