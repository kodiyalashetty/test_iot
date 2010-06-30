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


#ifndef __INFO_WIDGET_H__
#define __INFO_WIDGET_H__

#include <QTableWidget>

#include <HpiProvider.h>
#include <View.h>


/************************************************
 * class cInfoWidget
 ***********************************************/
class cInfoWidget : public QTableWidget, public cView
{
    Q_OBJECT

public:

    explicit cInfoWidget( cHpiProvider& provider );

    void Update();

private:

    // data
    cHpiProvider& m_provider;
};


#endif // __INFO_WIDGET_H__

