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


#ifndef __ROLLUP_BUTTON_H__
#define __ROLLUP_BUTTON_H__

#include <QPushButton>

class QIcon;
class QWidget;

/************************************************
 * class cRollupButton
 ***********************************************/
class cRollupButton : public QPushButton
{
    Q_OBJECT

public:

    explicit cRollupButton( const QString & txt, QWidget * controlled_widget );

private slots:

    void clicked();

private:

    // data
    QWidget * m_controlled_widget;
    const QIcon& m_up_icon;
    const QIcon& m_down_icon;
};


#endif // __ROLLUP_BUTTON_H__

