/*
 *  Copyright (c) 2010 Pigeon Point Systems.
 *  All rights reserved.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  This
 * file and program are licensed under a BSD style license.  See
 * the Copying file included with this distribution for
 * full licensing terms.
 *
 * Authors:
 *     Anton Pak (Pigeon Point Systems)
 *     Sergey Ivushkin (Pigeon Point Systems)
 */


#ifndef __ACTIONS_WIDGET_H__
#define __ACTIONS_WIDGET_H__

#include <QWidget>

#include <HpiProvider.h>


class QPushButton;
class QSignalMapper;
class QVBoxLayout;

/************************************************
 * class cActionsWidget
 ***********************************************/
const unsigned int MaxActionsInWidget = 13;


class cActionsWidget : public QWidget
{
    Q_OBJECT

public:

    explicit cActionsWidget( cHpiProvider& provider );

    void Update();

private slots:

    void clicked( int button_id );

private:

    // data
    cHpiProvider&   m_provider;

    QSignalMapper * m_mapper;
    unsigned int    m_anum;
    QPushButton *   m_abuttons[MaxActionsInWidget];
    HpiActionShort  m_short_actions[MaxActionsInWidget];
    QVBoxLayout *   m_layout;
};


#endif // __ACTIONS_WIDGET_H__

