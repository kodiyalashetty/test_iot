/*
 *  Copyright (c) 2012 Pigeon Point Systems.
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
 */

#include <QDesktopWidget>
#include <QFile>
#include <QHBoxLayout>
#include <QLabel>
#include <QLineEdit>
#include <QListWidget>
#include <QPushButton>
#include <QRect>
#include <QString>
#include <QVBoxLayout>

#include <DomainSelector.h>
#include <OHpi.h>

#include "EntriesWidget.h"


/************************************************
 * class cDomainSelector
 ***********************************************/
cDomainSelector::cDomainSelector( cOHpi& ohpi )
    : QDialog(),
      m_ohpi( ohpi ),
      m_vlayout( new QVBoxLayout ),
      m_domains_header( new QLabel( "Select defined domain:" ) ),
      m_domains_widget( new cEntriesWidget( ohpi ) ),
      m_new_domain_header( new QLabel( "Or enter new domain address:" ) ),
      m_hlayout( new QHBoxLayout ),
      m_new_domain_edit( new QLineEdit ),
      m_new_domain_btn( new QPushButton( "Add and Go!" ) )
{
    m_ohpi.SetView( this );

    m_new_domain_header->setText( QString( "\n" ) +
                                  "Or enter new domain address:\n"
                                  "\n"
                                  "If host contains ':' (for example IPv6 address)\n"
                                  "then enclose it in square brackets.\n"
                                  "For example: \"[::1]\" or \"[::1]:4743\"" );

    m_vlayout->addWidget( m_domains_header );
    m_vlayout->addWidget( m_domains_widget );
    m_vlayout->addWidget( m_new_domain_header );
    m_vlayout->addLayout( m_hlayout );

    m_hlayout->addWidget( m_new_domain_edit );
    m_hlayout->addWidget( m_new_domain_btn );

    setLayout( m_vlayout );

    // Center widget
    QRect drect =  QDesktopWidget().availableGeometry();
    QRect frect = frameGeometry();
    frect.moveCenter( drect.center() );
    move( frect.topLeft() );

    // apply style sheet
    QFile f( ":/application.css" );
    if ( f.open( QIODevice::ReadOnly | QIODevice::Text ) ) {
        setStyleSheet( f.readAll() );
        f.close();
    } else {
        setStyleSheet( "QPushButton { text-align: left }" );
    }

    connect( m_new_domain_btn, SIGNAL( clicked() ), this, SLOT( NewDomainClicked() ) );
}

void cDomainSelector::Update()
{
    if ( m_ohpi.IsDidSelected() ) {
        accept();
    } else {
        m_domains_widget->Update();
    }
}

void cDomainSelector::NewDomainClicked()
{
    QString host_port = m_new_domain_edit->text();
    m_ohpi.EnterNew( host_port.toStdString() );
}

