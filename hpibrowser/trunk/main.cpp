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
#include <sstream>
#include <string>

#include <SaHpi.h>

#include <QApplication>

#include <Hpi.h>
#include <MainWindow.h>

int main( int argc, char * argv[] )
{
	int rc = 0;
	try {

        QApplication app( argc, argv );

        SaHpiDomainIdT startup_did = SAHPI_UNSPECIFIED_DOMAIN_ID;
        // TODO redo command line parsing with cross-platform API
        do {
            if ( argc == 1 ) {
                break;
            } else if ( argc == 3 ) {
                if ( std::string( argv[1] ) == "-did" ) {
                    std::istringstream ss( argv[2] );
                    ss >> startup_did;
                    if ( ( !ss.fail() ) && ss.eof() ) {
                        break;
                    }
                }
            }

            printf( "Usage: %s [-did <domain_id>]\n", argv[0] );
            return 0;
        } while ( false );

        cHpi hpi( startup_did );
        cMainWindow mw( hpi );
        mw.Update();
        mw.show();
        rc = app.exec();

	} catch ( const std::exception& ex ) {
		fprintf( stderr, "Error: %s\n", ex.what() );
	} catch ( ... ) {
		fprintf(stderr, "Error: unknown exception catched\n");
	}
	return rc;
}

