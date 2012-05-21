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


#ifndef __DOMAIN_SELECTOR_H__
#define __DOMAIN_SELECTOR_H__

#include <QDialog>

#include <View.h>


/************************************************
 * class cDomainSelector
 ***********************************************/
class QLabel;
class QLineEdit;
class QListWidget;
class QPushButton;
class QHBoxLayout;
class QVBoxLayout;

class cEntriesWidget;
class cOHpi;

class cDomainSelector : public QDialog, public cView
{
    Q_OBJECT

public:

    explicit cDomainSelector( cOHpi& ohpi );

    virtual void Update();

private slots:

    void NewDomainClicked();

private:

    cOHpi&           m_ohpi;
    QVBoxLayout *    m_vlayout;
    QLabel *         m_domains_header;
    cEntriesWidget * m_domains_widget;
    QLabel *         m_new_domain_header;
    QHBoxLayout *    m_hlayout;
    QLineEdit *      m_new_domain_edit;
    QPushButton *    m_new_domain_btn;
};


#endif // __DOMAIN_SELECTOR_H__

