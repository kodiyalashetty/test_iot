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


#ifndef __ENTRIES_WIDGET_H__
#define __ENTRIES_WIDGET_H__

#include <tr1/unordered_map>

#include <QListWidget>

#include <HpiProvider.h>
#include <View.h>


/************************************************
 * class cEntriesWidget
 ***********************************************/
class cEntriesWidget : public QListWidget, public cView
{
    Q_OBJECT

public:

    explicit cEntriesWidget( cHpiProvider& provider );

    void Update();

private slots:

    void activated( QListWidgetItem * item );

private:

    // data
    cHpiProvider& m_provider;

    typedef std::tr1::unordered_map<int, HpiEntryShort> ShortEntries;
    ShortEntries m_short_entries;
};


#endif // __ENTRIES_WIDGET_H__

