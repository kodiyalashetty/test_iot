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


#include <algorithm>

#include <QIcon>
#include <QPushButton>
#include <QSignalMapper>
#include <QString>
#include <QVBoxLayout>

#include "ActionsWidget.h"
#include "IconCache.h"


/************************************************
 * class cActionsWidget
 ***********************************************/
cActionsWidget::cActionsWidget( cHpiProvider& provider )
    : m_provider( provider ), m_anum( 0 )
{
    setObjectName( "HpiActionsWidget" );

    m_mapper = new QSignalMapper( this );

    m_layout = new QVBoxLayout;
    m_layout->setSpacing( 0 );
    setLayout( m_layout );

    const QIcon& aicon = cIconCache::Instance()->GetIcon( "XXX" );

    for ( unsigned int i = 0; i < MAX_ACTIONS; ++i ) {
        QPushButton * btn = new QPushButton( aicon, "Action" );
        btn->hide();
        btn->setObjectName( "HpiAction" );
        btn->setFlat( true );
        btn->setFocusPolicy( Qt::NoFocus );
        m_layout->addWidget( btn );
        connect( btn, SIGNAL( clicked() ), m_mapper, SLOT( map() ) );
        m_abuttons[i] = btn;
    }

    // TODO
    //m_layout->addStretch();

    connect( m_mapper, SIGNAL( mapped( int ) ), this, SLOT( clicked( int ) ) );
}

void cActionsWidget::Update()
{
    std::deque<HpiAction> actions;
    m_provider.GetActions( actions );

    m_anum = 0;
    for ( unsigned int i = 0; i < MAX_ACTIONS; ++i ) {
        m_mapper->removeMappings( m_abuttons[i] );
        m_abuttons[i]->hide();
    }
    m_anum = std::min( MAX_ACTIONS, actions.size() );
    for ( unsigned int i = 0; i < m_anum; ++i ) {
        m_mapper->setMapping( m_abuttons[i], i );
        m_short_actions[i] = HpiActionShort( actions[i] );
        m_abuttons[i]->setText( QString::fromStdWString( actions[i].description ) );
        m_abuttons[i]->show();
    }
}

void cActionsWidget::clicked( int button_id )
{
    if ( ( button_id >= 0 ) && ( button_id < m_anum ) ) {
        m_provider.ExecuteAction( m_short_actions[button_id] );
    } else {
        // TODO
    }
}

