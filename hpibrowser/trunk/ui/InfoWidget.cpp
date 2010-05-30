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


#include <QFontMetrics>
#include <QHeaderView>
#include <QIcon>
#include <QString>
#include <QTableWidgetItem>

#include "IconCache.h"
#include "InfoWidget.h"


/************************************************
 * class cInfoWidget
 ***********************************************/
cInfoWidget::cInfoWidget( cHpiProvider& provider )
    : m_provider( provider )
{
    setObjectName( "HpiInfoWidget" );

    setColumnCount( 2 );

    horizontalHeader()->setStretchLastSection( true );
    verticalHeader()->setDefaultSectionSize( fontMetrics().height() );
    verticalHeader()->setResizeMode( QHeaderView::Fixed );
    horizontalHeader()->hide();
    verticalHeader()->hide();
}

void cInfoWidget::Update()
{
    clearContents();

    std::deque<HpiInfo> info;
    m_provider.GetInfo( info );

    setRowCount( info.size() );

    for ( unsigned int i = 0, n = info.size(); i < n; ++i ) {
        QTableWidgetItem * item;

        item = new QTableWidgetItem( QString::fromStdWString( info[i].name ) );
        item->setFlags( Qt::ItemIsEnabled );
        setItem( i, 0, item );

        item = new QTableWidgetItem( QString::fromStdWString( info[i].value ) );
        item->setFlags( Qt::ItemIsEnabled );
        setItem( i, 1, item );
    }

    resizeColumnToContents( 0 );
}

