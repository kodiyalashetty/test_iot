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
#include <stdexcept>

#include <QApplication>

#include <DomainSelector.h>
#include <Hpi.h>
#include <MainWindow.h>
#include <OHpi.h>


int main( int argc, char * argv[] )
{
	int rc = 0;
	try {

        QApplication app( argc, argv );

        cOHpi ohpi;
        cDomainSelector dsel( ohpi );
        dsel.Update();
        dsel.show();
        dsel.exec();

        cHpi hpi( ohpi.GetSelectedDid() );
        cMainWindow mw( hpi );
        mw.Update();
        mw.show();

        rc = app.exec();

	} catch ( const std::exception& ex ) {
		fprintf( stderr, "Error: %s\n", ex.what() );
	} catch ( ... ) {
		fprintf(stderr, "Error: unknown exception\n");
	}
	return rc;
}

