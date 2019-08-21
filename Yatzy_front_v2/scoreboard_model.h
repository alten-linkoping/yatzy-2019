#ifndef SCOREBOARD_MODEL_H
#define SCOREBOARD_MODEL_H
#include <QAbstractTableModel>
#include <QFont>
#include <QBrush>

class scoreboard_model : public QAbstractTableModel

{
    Q_OBJECT
    public:
        scoreboard_model(QObject *parent = nullptr);
        int rowCount(const QModelIndex &parent = QModelIndex()) const override;
        int columnCount(const QModelIndex &parent = QModelIndex()) const override;
        QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const override;
};

#endif // SCOREBOARD_MODEL_H
