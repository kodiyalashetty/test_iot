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


#ifndef __MAIN_WINDOW_H__
#define __MAIN_WINDOW_H__

#include <QMainWindow>

#include <HpiProvider.h>
#include <View.h>


class cActionsWidget;
class cEntriesWidget;
class cInfoWidget;
class cRollupButton;
class QLabel;
class QListWidget;
class QPushButton;
class QScrollArea;
class QSplitter;
class QTextEdit;
class QVBoxLayout;
class QWidget;

/************************************************
 * class cMainWindow
 ***********************************************/
class cMainWindow : public QMainWindow, public cView
{
    Q_OBJECT

public:

    explicit cMainWindow( cHpiProvider& provider );

    void Update();

private:

    // data
    cHpiProvider&     m_provider;

    QSplitter *       m_outer_splitter;
    QSplitter *       m_inner_splitter;
    QWidget *         m_left_widget;
    QVBoxLayout *     m_left_layout;
    QWidget *         m_right_widget;
    QVBoxLayout *     m_right_layout;
    QLabel *          m_entries_header;
    cEntriesWidget *  m_entries_widget;
    QLabel *          m_info_header;
    cInfoWidget *     m_info_widget;
    cRollupButton *   m_actions_rollup;
    cActionsWidget *  m_actions_widget;

    QTextEdit *       m_log_widget;
};


#endif // __MAIN_WINDOW_H__

