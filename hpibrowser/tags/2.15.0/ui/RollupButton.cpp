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


#include <QWidget>

#include "IconCache.h"
#include "RollupButton.h"


/************************************************
 * class cRollupButton
 ***********************************************/
cRollupButton::cRollupButton( const QString & txt, QWidget * controlled_widget )
    : QPushButton( txt ),
      m_controlled_widget( controlled_widget ),
      m_up_icon( cIconCache::Instance()->GetIcon( "UP" ) ),
      m_down_icon( cIconCache::Instance()->GetIcon( "DOWN" ) )
{
    setFlat( true );
    connect( this, SIGNAL( clicked() ), this, SLOT( clicked() ) );

    bool state = ( m_controlled_widget != 0 ) ? m_controlled_widget->isVisible() : false;
    setIcon( state ? m_down_icon : m_up_icon );

    setFocusPolicy( Qt::NoFocus );
}

void cRollupButton::clicked()
{
    if ( m_controlled_widget ) {
        bool new_state = !m_controlled_widget->isVisible();
        setIcon( new_state ? m_up_icon : m_down_icon );
        m_controlled_widget->setVisible ( new_state );
    }
}

