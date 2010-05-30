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


#include <cstdio>
#include <string>

#include <QDesktopWidget>
#include <QFile>
#include <QIcon>
#include <QLabel>
#include <QRect>
#include <QScrollArea>
#include <QSplitter>
#include <QString>
#include <QTextEdit>
#include <QVBoxLayout>
#include <QWidget>

#include <MainWindow.h>

#include "ActionsWidget.h"
#include "EntriesWidget.h"
#include "InfoWidget.h"
#include "IconCache.h"
#include "RollupButton.h"


/************************************************
 * class cMainWindow
 ***********************************************/
cMainWindow::cMainWindow( cHpiProvider& provider )
    : m_provider( provider )
{
    // TODO
    QRect drect =  QDesktopWidget().availableGeometry();
    int wx = ( 3 * drect.width() ) / 4;
    int wy = ( 3 * drect.height() ) / 4;
    resize( wx, wy );
    QRect frect = frameGeometry();
    frect.moveCenter( drect.center() );
    move( frect.topLeft() );

    // create widgets
    m_outer_splitter = new QSplitter( Qt::Vertical );
    m_inner_splitter = new QSplitter( Qt::Horizontal );
    m_left_widget    = new QWidget;
    m_left_layout    = new QVBoxLayout;
    m_right_widget   = new QWidget;
    m_right_layout   = new QVBoxLayout;
    m_entries_header = new QLabel( " Entries" );
    m_entries_widget = new cEntriesWidget( provider );
    m_info_header    = new QLabel( "Info" );
    m_info_widget    = new cInfoWidget( provider );
    m_actions_widget = new cActionsWidget( provider );
    m_actions_rollup = new cRollupButton( " Actions", m_actions_widget );
    m_log_widget     = new QTextEdit;

    m_log_widget->append( "Application started." );


    // name widgets
    m_outer_splitter->setObjectName( "HpiOuterSplitter" );
    m_inner_splitter->setObjectName( "HpiInnerSplitter" );
    m_left_widget->setObjectName( "HpiLeftWidget" );
    m_right_widget->setObjectName( "HpiRightWidget" );
    m_entries_header->setObjectName( "HpiEntriesHeader" );
    m_info_header->setObjectName( "HpiInfoHeader" );
    m_actions_rollup->setObjectName( "HpiActionsRollup" );
    m_log_widget->setObjectName( "HpiLogArea" );


    // configure widgets appearence
    m_actions_rollup->setSizePolicy( QSizePolicy::Expanding, QSizePolicy::Fixed );

    m_log_widget->setReadOnly( true );
    m_log_widget->setFontFamily( "monospace" );

    // apply style sheet
    QFile f( ":/application.css" );
    if ( f.open( QIODevice::ReadOnly | QIODevice::Text ) ) {
        setStyleSheet( f.readAll() );
        f.close();
    } else {
        setStyleSheet( "QPushButton { text-align: left }" );
    }


    // place widgets
    m_left_layout->addWidget( m_entries_header );
    m_left_layout->addWidget( m_entries_widget );
    m_left_widget->setLayout( m_left_layout );

    m_right_layout->addWidget( m_info_header );
    m_right_layout->addWidget( m_info_widget );
/*
    // TODO further development
    m_right_layout->addWidget( m_actions_rollup );
    m_right_layout->addWidget( m_actions_widget );
*/
    m_right_widget->setLayout( m_right_layout );

    m_inner_splitter->addWidget( m_left_widget );
    m_inner_splitter->addWidget( m_right_widget );

    m_inner_splitter->setStretchFactor( 0, 50 );
    m_inner_splitter->setStretchFactor( 1, 100 );

    m_outer_splitter->addWidget( m_inner_splitter );
/*
    // TODO further development
    m_outer_splitter->addWidget( m_log_widget );
*/

    m_outer_splitter->setStretchFactor( 0, 100 );
    m_outer_splitter->setStretchFactor( 1, 20 );

    setCentralWidget( m_outer_splitter );

    m_log_widget->append( "Ready." );

    m_provider.SetView( this );
}

void cMainWindow::Update()
{
    std::wstring txt;

    m_provider.GetInfoHeader( txt );
    m_info_header->setText( QString::fromStdWString( txt ) );

    m_info_widget->Update();
    m_actions_widget->Update();
    m_entries_widget->Update();
}

