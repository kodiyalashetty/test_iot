/*
 * daemon code
 *
 * Copyright (c) 2004 by FORCE Computers.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  This
 * file and program are licensed under a BSD style license.  See
 * the Copying file included with the OpenHPI distribution for
 * full licensing terms.
 *
 * Authors:
 *     Thomas Kanngieser <thomas.kanngieser@fci.com>
 */

#include "openhpid.h"
#include "openhpi.h"
#include "ecode_utils.h"
#include "printevent_utils.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <getopt.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>
#include <string.h>
#include <assert.h>
#include <stdarg.h>
#include <signal.h>
#include "utils.h"


////////////////////////////////////////////////////////////
//                  cConnection
////////////////////////////////////////////////////////////

cConnection::cConnection( cServerConnection *con )
  : m_con( con ), m_outstanding_pings( 0 )
{
  gettimeofday1( &m_ping_timer );
  m_ping_timer += dPingTimeout;
}


cConnection::~cConnection()
{
  if ( m_con )
       ServerConnectionRem( m_con );

  while( Num() )
     {
       cSession *s = operator[]( Num() - 1 );
       saHpiSessionClose( s->SessionId() );

       delete Rem( Num() - 1 );
     }
}


void
cConnection::Reinit()
{
  gettimeofday1( &m_ping_timer );
  m_ping_timer += dPingTimeout;
  m_outstanding_pings = 0;

  // close all sessions
  while( Num() )
     {
       cSession *s = operator[]( Num() - 1 );
       saHpiSessionClose( s->SessionId() );

       delete Rem( Num() - 1 );
     }
}


void
cConnection::GetIp( char *str )
{
  unsigned int ip = m_con->m_resend.m_ip_addr.sin_addr.s_addr;

  sprintf( str, "%d.%d.%d.%d",
           (ip & 0xff),
           ((ip >> 8 ) & 0xff),
           ((ip >> 16) & 0xff),
           ((ip >> 24) & 0xff) );
}


unsigned short
cConnection::GetPort()
{
  return m_con->m_resend.m_ip_addr.sin_port;
}


cSession *
cConnection::FindSession( SaHpiSessionIdT sid )
{
  for( int i = 0; i < Num(); i++ )
     {
       cSession *s = operator[]( i );

       if ( s->SessionId() == sid )
            return s;
      }

  return 0;
}


bool
cConnection::AddSession( SaHpiSessionIdT sid )
{
  if ( FindSession( sid ) )
       return false;

  cSession *s = new cSession( this, sid );
  cArray<cSession>::Add( s );

  return true;
}


bool
cConnection::RemSession( SaHpiSessionIdT sid )
{
  for( int i = 0; i < Num(); i++ )
     {
       cSession *s = cArray<cSession>::operator[]( i );

       if ( s->SessionId() == sid )
          {
            delete cArray<cSession>::Rem( i );
            return true;
          }
     }

  return false;
}


int
cConnection::WriteMsg( cMessageHeader &header, void *data )
{
  return ServerWriteMsg( m_con, &header, data );
}


////////////////////////////////////////////////////////////
//                  cOpenHpiDaemon
////////////////////////////////////////////////////////////


cOpenHpiDaemon::cOpenHpiDaemon()
  : m_progname( 0 ), m_daemon( true ), m_debug( 0 ),
    m_interactive( false ), m_daemon_port( dDefaultDaemonPort ),
    m_server_socket( 0 ), m_pollfd( 0 ),
    m_version( 0 ), m_session( 0 )
{
  m_config[0] = 0;
}


cOpenHpiDaemon::~cOpenHpiDaemon()
{
}


void
cOpenHpiDaemon::DbgInit( const char *fmt, ... )
{
  va_list args;
  va_start( args, fmt );

  if ( m_debug & dDebugInit )
       vprintf( fmt, args );

  va_end( args );
}


void
cOpenHpiDaemon::DbgCon( const char *fmt, ... )
{
  va_list args;
  va_start( args, fmt );

  if ( m_debug & dDebugConnection )
       vprintf( fmt, args );

  va_end( args );
}


void
cOpenHpiDaemon::DbgFunc( const char *fmt, ... )
{
  va_list args;
  va_start( args, fmt );

  if ( m_debug & dDebugFunction )
       vprintf( fmt, args );

  va_end( args );
}


void
cOpenHpiDaemon::DbgEvent( const char *fmt, ... )
{
  va_list args;
  va_start( args, fmt );

  if ( m_debug & dDebugEvent )
       vprintf( fmt, args );

  va_end( args );
}


void
cOpenHpiDaemon::DbgPing( const char *fmt, ... )
{
  va_list args;
  va_start( args, fmt );

  if ( m_debug & dDebugPing )
       vprintf( fmt, args );

  va_end( args );
}


void
cOpenHpiDaemon::Usage()
{
  fprintf( stderr, "usage: %s [OPTION] ...\n", m_progname );
  fprintf( stderr, "\t-h --help         help\n" );
  fprintf( stderr, "\t-d --debug=level  debug level\n" );
  fprintf( stderr, "\t-n --nodaemon     do not became a daemon\n" );
  fprintf( stderr, "\t-p --port=port    daemon port\n" );
  fprintf( stderr, "\t-c --config=file  use configuration file\n" );
  fprintf( stderr, "\t-i --interactive  simple user interface\n" );
}


bool
cOpenHpiDaemon::ParseArgs( int argc, char *argv[] )
{
  m_progname = "openhpid";

  if ( argc > 0 )
       m_progname = argv[0];

  // set the current working directory for relative path
  char cwd[PATH_MAX];
  getcwd( cwd, PATH_MAX);
  setenv( "OPENHPI_CWD", cwd, 1 );

  static struct option long_options[] =
  {
    { "help"       , 0, 0, 'h' },
    { "debug"      , 1, 0, 'd' },
    { "nodaemon"   , 0, 0, 'n' },
    { "port"       , 1, 0, 'p' },
    { "config"     , 1, 0, 'c' },
    { "interactive", 0, 0, 'i' },
    { 0, 0, 0, 0 }
  };

  bool help = false;

  while( true )
     {
       int option_index = 0;
       int c;

       c = getopt_long( argc, argv, "hd:c:nip:",
                        long_options, &option_index );

       if ( c == -1 )
	    break;

       switch( c )
	  {
	    case 'n':
		 m_daemon = false;
		 break;

	    case 'd':
		 m_debug = atoi( optarg );
		 break;

	    case 'c':
                 // need an absolute filename
                 if ( optarg[0] == '/' )
                      strcpy( m_config, optarg );
                 else
                    {
                      getcwd( m_config, PATH_MAX);
                      strcat( m_config, "/" );
                      strcat( m_config, optarg );
                    }

		 break;

	    case 'p':
		 m_daemon_port = atoi( optarg );
		 break;

	    case 'h':
		 help = true;
		 break;

	    case 'i':
		 m_interactive = true;
		 break;

	    default:
		 fprintf( stderr, "unknown option %s\n", 
			  argv[optind ? optind : 1] );

		 help = true;
		 break;
	  }
     }

  // check for additional arguments
  for( int i = optind; i < argc; i++ )
     {
       help = true;

       fprintf( stderr, "unknown option %s\n",
		argv[i] );
     }

  if ( help )
     {
       Usage();
       return false;
     }

  return true;
}


bool
cOpenHpiDaemon::Initialize()
{
  if ( signal( SIGPIPE, SIG_IGN ) == SIG_ERR )
     {
       DbgInit( "cannot ignore SIG_IGN !\n" );
       return false;
     }

  if ( m_daemon )
     {
       DbgInit( "become a daemon.\n" );

       pid_t pid = fork();

       if ( pid < 0 )
	  {
	    fprintf( stderr, "cannot fork: %s !\n",
		     strerror( errno ) );
	    return false;
	  }

       // parent process
       if ( pid != 0 )
	    exit( 0 );

       // become the session leader
       setsid();

       // second fork to become a real daemon
       pid = fork();

       if ( pid < 0 )
	  {
	    fprintf( stderr, "cannot fork: %s !\n",
		     strerror( errno ) );
	    return false;
	  }

       // parent process
       if ( pid != 0 )
	    exit( 0 );

       chdir( "/" );

       umask( 0 );

       for( int i = 0; i < 1024; i++ )
            close( i );

       m_interactive = false;
     }

  // use config file given by the command line
  if ( m_config[0] )
     {
       DbgInit( "using configuration file: %s.\n", m_config );
       setenv( "OPENHPI_CONF", m_config, 1 );
     }

  // initialize openhpi
  DbgInit( "initialize openhpi.\n" );
  SaErrorT rv = saHpiInitialize( &m_version );

  if ( rv != SA_OK )
     {
       DbgInit( "cannot initialize openhpi: %s !\n",
		decode_error( rv ) );
       return false;
     }

  // create a session
  rv = saHpiSessionOpen( SAHPI_DEFAULT_DOMAIN_ID, &m_session, 0 );

  if ( rv != SA_OK )
     {
       DbgInit( "cannot create session: %s !\n", 
		decode_error( rv ) );

       saHpiFinalize();
       return false;
     }

  rv = saHpiResourcesDiscover( m_session );

  if ( rv != SA_OK )
     {
       DbgInit( "cannot discover resources: %s !\n", 
		decode_error( rv ) );

       saHpiFinalize();
       return false;
     }

  // subscribe
  rv = saHpiSubscribe( m_session, SAHPI_TRUE );

  if ( rv != SA_OK )
     {
       DbgInit( "cannot subscribe: %s !\n", 
		decode_error( rv ) );

       saHpiSessionClose( m_session );
       saHpiFinalize();
       return false;
     }

  // open daemon socket
  DbgInit( "create daemon connection port %d.\n", m_daemon_port );

  m_server_socket = ServerOpen( m_daemon_port );

  if ( !m_server_socket )
     {
       fprintf( stderr, "cannot create daemon socket: %d, %s !\n",
                errno, strerror( errno ) );

       saHpiUnsubscribe( m_session );
       saHpiSessionClose( m_session );
       saHpiFinalize();
       return false;
     }

  if ( m_interactive )
       DbgInit( "interactive\n" );

  DbgInit( "daemon is up.\n" );

  return true;
}


void
cOpenHpiDaemon::Finalize()
{
  while( Num() )
       CloseConnection( operator[]( Num() - 1 ) );

  if ( m_pollfd )
       delete [] m_pollfd;

  if ( m_server_socket )
     {
       ServerClose(  m_server_socket );
       m_server_socket = 0;
     }

  saHpiUnsubscribe( m_session );
  saHpiSessionClose( m_session );
  saHpiFinalize();
}


int
cOpenHpiDaemon::MainLoop()
{
  DbgCon( "ready for incomming connections.\n" );

  int num_add = 1;

  if ( m_interactive )
     {
       m_pollfd = new pollfd[2];

       num_add++;

       m_pollfd[1].fd     = 0; // stdin
       m_pollfd[1].events = POLLIN;
       m_pollfd[1].revents = 0;
     }
  else
       m_pollfd = new pollfd[1];

  m_pollfd[0].fd     = m_server_socket->m_fd;
  m_pollfd[0].events = POLLIN;
  m_pollfd[0].revents = 0;

  cHpiTime next_idle = cHpiTime::Now();
  next_idle += 250;

  while( true )
     {
       cHpiTime now = cHpiTime::Now();

       if ( now >= next_idle )
          {
            Idle();

            next_idle = cHpiTime::Now();
            next_idle += 250;
          }

       int rv = poll( m_pollfd, num_add, 250 );

       if ( rv < 0 )
	  {
	    usleep( 100000 );

	    if ( errno != EINTR )
		 fprintf( stderr, "can't poll: %s %d !\n",
			  strerror( errno ), errno );

	    // sleep a while
	    usleep( 100 );
	    continue;
	  }

       if ( rv == 0 )
	    continue;

       if ( m_interactive && m_pollfd[1].revents )
          {
	    if ( HandleInteractive() == false )
		 break;

            continue;
          }

       //DbgCon( "read meg.\n" );

       cServerConnection *c = 0;
       cMessageHeader header;
       unsigned char data[dMaxMessageLength];

       tConnectionError r = ServerReadMsg( m_server_socket,
                                           &c, &header, data );
       cConnection *con = 0;

       switch( r )
          {
            case eConnectionNew:
                 NewConnection( c );

            case eConnectionOk:
                 con = (cConnection *)c->m_user_data;

                 if ( !HandleData( con, header, data ) )
                      CloseConnection( con );

                 break;

            case eConnectionDuplicate:
                 break;

            default:
                 DbgCon( "reading broken message %d.\n", r );

                 break;
          }
     }

  return 0;
}


void
cOpenHpiDaemon::NewConnection( cServerConnection *c )
{
  DbgCon( "creating new connection.\n" );

  cConnection *con = new cConnection( c );
  c->m_user_data = con;
  Add( con );
}


void
cOpenHpiDaemon::CloseConnection( cConnection *con )
{
  DbgCon( "closing connection.\n" );

  int idx = Find( con );

  if ( idx == - 1 )
     {
       assert( 0 );
       return;
     }

  delete Rem( idx );
}


void
cOpenHpiDaemon::Idle()
{
  // read events to keep auto insertion/extraction running
  SaHpiEventT    event;
  SaHpiRdrT      rdr;
  SaHpiRptEntryT rpt_entry;

  SaErrorT ret = saHpiEventGet( m_session, SAHPI_TIMEOUT_IMMEDIATE, &event, &rdr, &rpt_entry );

  if ( ret == SA_OK )
     {
       DbgEvent( "idle: saHpiEventGet read event\n" );

       if ( m_debug & dDebugEvent )
	    print_event( &event );
     }
  else if ( ret == SA_ERR_HPI_TIMEOUT )
       DbgEvent( "idle: saHpiEventGet timeout.\n", ret );
  else
       DbgEvent( "idle: saHpiEventGet %s.\n", decode_error( ret ) );

  SaHpiTimeT now;
  gettimeofday1( &now );

  // check for pending event get
  for( int i = Num() - 1; i >= 0; i-- )
     {
       cConnection *c = operator[]( i );

       // ping
       if ( now > c->PingTimer() )
	  {
	    if ( c->OutstandingPings() > dMaxLostPings )
	       {
		 // ping timeout
		 DbgPing( "ping timeout !\n" );
		 CloseConnection( c );
		 continue;
	       }
	    else if ( now > c->PingTimer() )
	       {
		 // send ping
                 SaHpiTimeT pt = dPingTimeout;
                 pt /= 1000000LL;

		 cMessageHeader header;
		 MessageHeaderInit( &header, eMhPing, dMhRequest, 0, (unsigned int)pt, 0 );

		 int rv = c->WriteMsg( header, 0 );

		 if ( rv )
		    {
		      DbgPing( "cannot send ping !\n" );
		      CloseConnection( c );
		      continue;
		    }

		 c->OutstandingPings() = c->OutstandingPings() + 1;

		 DbgPing( "send ping %d.\n", c->OutstandingPings() );

		 // set ping timer
		 SaHpiTimeT ti;

		 gettimeofday1( &ti );
		 ti += dPingTimeout;

		 c->PingTimer() = ti;
	       }
	  }

       for( int j = 0; j < c->Num(); j++ )
	  {
	    cSession *s = c->operator[]( j );

	    if ( !s->IsEventGet() )
		 continue;

	    // check for event
	    ret = saHpiEventGet( s->SessionId(), SAHPI_TIMEOUT_IMMEDIATE,
				 &event, &rdr, &rpt_entry );

	    if (    ret == SA_ERR_HPI_TIMEOUT
		 && now < s->Timeout() )
		 continue;

	    if ( ret == SA_ERR_HPI_TIMEOUT )
		 DbgEvent( "saHpiEventGet( %x ): TIMEOUT\n",
			   s->SessionId() );
	    else
		 DbgEvent( "saHpiEventGet( %x ): send event\n",
			   s->SessionId() );

	    s->EventGet( false );

	    // send response
	    cHpiMarshal *hm = HpiMarshalFind( eFsaHpiEventGet );
	    assert( hm );

	    cMessageHeader rh;
	    MessageHeaderInit( &rh, eMhMsg, dMhReply, s->EventGetSeq(), eFsaHpiEventGet,
			       hm->m_reply_len );

	    // alloc reply buffer
	    void *rd = calloc( 1, hm->m_reply_len );

	    rh.m_len = HpiMarshalReply3( hm, rd, &ret, &event, &rdr, &rpt_entry );

	    assert( rh.m_len >= 0 );

	    int rv = 0;

	    if ( rh.m_len >= 0 )
		 rv = c->WriteMsg( rh, rd );
            else if ( rd )
		 free( rd );

	    // cannot send message => close connection
	    if ( rv || rh.m_len < 0 )
		 CloseConnection( c );
	  }
     }
}


bool
cOpenHpiDaemon::HandleData( cConnection *c, const cMessageHeader &header,
                            const void *data )
{
  if ( IsRequestMsg( &header ) )
     {
       switch( header.m_type )
          {
            case eMhPing:
                 return HandlePing( c, header );

            case eMhReset:
                 return HandleOpen( c, header );

            case eMhMsg:
                 {
                   if ( header.m_id == eFClose )
                        return HandleClose( c, header );

                   cMessageHeader rh;
                   void *rd = 0;

                   tResult r = HandleMsg( c, header, data, rh, rd );
                   int rv = 0;

                   // marshal error ?
                   if ( rh.m_len < 0 )
                        rv = 1;
                   if ( r == eResultReply )
                      {
                        assert( rh.m_len >= 0 && rh.m_len <= dMaxMessageLength );
                        rv = c->WriteMsg( rh, rd );
                      }
                   else if ( r == eResultError )
                        rv = 1;

                   if ( rd )
                        free( rd );

                   return !rv;
                 }

            default:
                 return false;
          }

       return false;
     }

  // reply
  switch( header.m_type )
     {
       case eMhPing:
            return HandlePong( c, header );

       default:
            return false;
     }

  return false;
}


bool
cOpenHpiDaemon::HandleOpen( cConnection *c, const cMessageHeader &header )
{
  char str[100];
  c->GetIp( str );
  DbgInit( "connection open: %s,%d.\n", str, c->GetPort() );
  c->Reinit();

  cMessageHeader rh;
  MessageHeaderInit( &rh, (tMessageType)header.m_type, dMhReply, header.m_seq, header.m_id, 0 );

  if ( c->WriteMsg( rh, 0 ) )
       return false;

  return true;
}


bool 
cOpenHpiDaemon::HandleClose( cConnection *c, const cMessageHeader &header )
{   
  char str[100];
  c->GetIp( str );
  DbgInit( "connection close: %s,%d\n", str, c->GetPort() );

  return false;
}


bool
cOpenHpiDaemon::HandlePing( cConnection *c, const cMessageHeader &header )
{
  DbgPing( "read ping.\n" );

  cMessageHeader rh;
  MessageHeaderInit( &rh, (tMessageType)header.m_type, dMhReply,
                     header.m_seq, header.m_id, 0 );

  if ( c->WriteMsg( rh, 0 ) )
       return false;

  return true;
}


bool
cOpenHpiDaemon::HandlePong( cConnection *c, const cMessageHeader &header )
{
  if ( c->OutstandingPings() )
     {
       DbgPing( "read pong.\n" );
       c->OutstandingPings() = 0;

       SaHpiTimeT now;
       gettimeofday1( &now );

       now += dPingTimeout;
       c->PingTimer() = now;

       return true;
     }

  DbgPing( "read pong without ping !\n" );
  return true;
}


cOpenHpiDaemon::tResult
cOpenHpiDaemon::HandleMsg( cConnection *c,
			   const cMessageHeader &header, const void *data,
			   cMessageHeader &rh, void *&rd )
{
  cHpiMarshal *hm = HpiMarshalFind( header.m_id );

  // check for function and data length
  if ( !hm || hm->m_request_len < header.m_len )
     {
       fprintf( stderr, "wrong message length: id %d !\n", header.m_id );

       return eResultError;
     }

  assert( hm->m_reply_len );

  // init reply header
  MessageHeaderInit( &rh, (tMessageType) header.m_type, dMhReply,
                     header.m_seq, header.m_id, hm->m_reply_len );

  // alloc reply buffer
  rd = malloc( hm->m_reply_len );
  assert( rd );

  memset( rd, 0, hm->m_reply_len );

  SaErrorT ret;

  switch( header.m_id )
     {
       case eFsaHpiSessionOpen:
	    {
	      SaHpiDomainIdT domain_id;
	      SaHpiSessionIdT session_id = 0;

	      if ( HpiDemarshalRequest1( header.m_flags & dMhEndianBit, hm, data, (void *)&domain_id ) < 0 )
		   return eResultError;

	      ret = saHpiSessionOpen( domain_id, &session_id, 0 );

	      DbgFunc( "saHpiSessionOpen( %x, %x ) = %d\n",
                       domain_id, session_id, ret );

	      if ( ret == SA_OK )
		   c->AddSession( session_id );

	      rh.m_len = HpiMarshalReply1( hm, rd, &ret, &session_id );
	    }
 
	    break;

       case eFsaHpiSessionClose:
	    {
	      SaHpiSessionIdT session_id;

	      if ( HpiDemarshalRequest1( header.m_flags & dMhEndianBit, hm, data, &session_id ) < 0 )
		   return eResultError;

	      ret = saHpiSessionClose( session_id );

	      DbgFunc( "saHpiSessionClose( %x ) = %d\n", session_id, ret );

	      if ( ret == SA_OK )
		   c->RemSession( session_id );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }

	    break;

       case eFsaHpiResourcesDiscover:
	    {
	      SaHpiSessionIdT session_id;

	      if ( HpiDemarshalRequest1( header.m_flags & dMhEndianBit, hm, data, &session_id ) < 0 )
		   return eResultError;

	      ret = saHpiResourcesDiscover( session_id );

	      DbgFunc( "saHpiResourcesDiscover( %x ) = %d\n", session_id, ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }

	    break;
    
       case eFsaHpiRptInfoGet:
	    {
	      SaHpiSessionIdT session_id;
              SaHpiRptInfoT rpt_info;

	      if ( HpiDemarshalRequest1( header.m_flags & dMhEndianBit, hm, data, &session_id ) < 0 )
		   return eResultError;

	      ret = saHpiRptInfoGet( session_id, &rpt_info );

	      DbgFunc( "saHpiRptInfoGet( %x ) = %d\n", session_id, ret );

	      rh.m_len = HpiMarshalReply1( hm, rd, &ret, &rpt_info );
	    }

	    break;

       case eFsaHpiRptEntryGet:
	    {
	      SaHpiSessionIdT session_id;
              SaHpiEntryIdT   entry_id;
              SaHpiEntryIdT   next_entry_id = 0; // for valgring
              SaHpiRptEntryT  rpt_entry;

	      if ( HpiDemarshalRequest2( header.m_flags & dMhEndianBit, hm, data,
                                    &session_id, &entry_id ) < 0 )
		   return eResultError;

	      ret = saHpiRptEntryGet( session_id, entry_id, &next_entry_id, &rpt_entry );

	      DbgFunc( "saHpiRptEntryGet( %x, %x, %x ) = %d\n",
                       session_id, entry_id, next_entry_id, ret );

	      rh.m_len = HpiMarshalReply2( hm, rd, &ret, &next_entry_id, &rpt_entry );
	    }

	    break;

       case eFsaHpiRptEntryGetByResourceId:
	    {
	      SaHpiSessionIdT session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiRptEntryT   rpt_entry;

	      if ( HpiDemarshalRequest2( header.m_flags & dMhEndianBit, hm, data,
				   &session_id, &resource_id ) < 0 )
		   return eResultError;

	      ret = saHpiRptEntryGetByResourceId( session_id, resource_id, &rpt_entry );

	      DbgFunc( "saHpiRptEntryGetByResourceId( %x, %x ) = %d\n",
                       session_id, resource_id, ret );

	      rh.m_len = HpiMarshalReply1( hm, rd, &ret, &rpt_entry );
	    }

	    break;

       case eFsaHpiResourceSeveritySet:
	    {
	      SaHpiSessionIdT session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiSeverityT   severity;

	      if ( HpiDemarshalRequest3( header.m_flags & dMhEndianBit, hm, data,
				   &session_id, &resource_id, &severity ) < 0 )
		   return eResultError;

	      ret = saHpiResourceSeveritySet( session_id,
					      resource_id, severity );

	      DbgFunc( "saHpiResourceSeveritySet( %x, %x ) = %d\n",
                       session_id, resource_id, ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }

	    break;

       case eFsaHpiResourceTagSet:
	    {
	      SaHpiSessionIdT  session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiTextBufferT resource_tag;

	      if ( HpiDemarshalRequest3( header.m_flags & dMhEndianBit, hm, data,
				   &session_id, &resource_id, &resource_tag ) < 0 )
		   return eResultError;

	      ret = saHpiResourceTagSet( session_id, resource_id,
					 &resource_tag );

	      DbgFunc( "saHpiResourceTagSet( %x, %x ) = %d\n",
                       session_id, resource_id, ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }

	    break;

/*
       case eFsaHpiResourceIdGet:
	    {
	      SaHpiSessionIdT session_id;
	      SaHpiResourceIdT resource_id = 0;

	      if ( HpiDemarshalRequest1( header.m_flags & dMhEndianBit, hm, data,
				    &session_id ) < 0 )
		   return eResultError;

	      ret = saHpiResourceIdGet( session_id, &resource_id );

	      DbgFunc( "saHpiResourceIdGet( %x ) = %d, %x\n",
                       session_id, ret, resource_id );

	      rh.m_len = HpiMarshalReply1( hm, rd, &ret, &resource_id );
	    }

	    break;
*/

       case eFsaHpiEntitySchemaGet:
	    {
	      SaHpiSessionIdT session_id;
	      SaHpiUint32T    schema_id = 0;

	      if ( HpiDemarshalRequest1( header.m_flags & dMhEndianBit, hm, data,
				   &session_id ) < 0 )
		   return eResultError;

	      ret = saHpiEntitySchemaGet( session_id, &schema_id );
	      
	      DbgFunc( "saHpiEntitySchemaGet( %x ) = %d, %x\n",
                       session_id, ret, schema_id );

	      rh.m_len = HpiMarshalReply1( hm, rd, &ret, &schema_id );
	    }
	    
	    break;

       case eFsaHpiEventLogInfoGet:
 	    {
	      SaHpiSessionIdT session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiSelInfoT    info;

	      if ( HpiDemarshalRequest2( header.m_flags & dMhEndianBit, hm, data,
				    &session_id, &resource_id ) < 0 )
		   return eResultError;

	      ret = saHpiEventLogInfoGet( session_id, resource_id, &info );

	      DbgFunc( "saHpiEventLogInfoGet( %x, %x ) = %d\n",
                       session_id, resource_id, ret );

	      rh.m_len = HpiMarshalReply1( hm, rd, &ret, &info );
	    }

	    break;

       case eFsaHpiEventLogEntryGet:
	    {
	      SaHpiSessionIdT  session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiSelEntryIdT entry_id;
	      SaHpiSelEntryIdT prev_entry_id = 0;
	      SaHpiSelEntryIdT next_entry_id = 0;
	      SaHpiSelEntryT   event_log_entry;
	      SaHpiRdrT        rdr;
	      SaHpiRptEntryT   rpt_entry;

	      memset( &rdr, 0, sizeof( SaHpiRdrT ) );
	      memset( &rpt_entry, 0, sizeof( SaHpiRptEntryT ) );

	      if ( HpiDemarshalRequest3( header.m_flags & dMhEndianBit, hm, data,
				    &session_id, &resource_id, &entry_id ) < 0 )
		   return eResultError;

	      ret = saHpiEventLogEntryGet( session_id, resource_id, entry_id,
					   &prev_entry_id, &next_entry_id,
					   &event_log_entry, &rdr, &rpt_entry );

	      DbgFunc( "saHpiEventLogEntryGet( %x, %x, %x ) = %d\n",
                       session_id, resource_id, entry_id, ret );

	      rh.m_len = HpiMarshalReply5( hm, rd, &ret, &prev_entry_id, &next_entry_id,
                                           &event_log_entry, &rdr, &rpt_entry );

/*
              if ( rh.m_len < 0 )
                 {
                   rh.m_len = HpiMarshalReply5( hm, rd, &ret, &prev_entry_id, &next_entry_id,
                                                &event_log_entry, &rdr, &rpt_entry );

                   assert( 0 );
                 }
*/
	    }

	    break;

       case eFsaHpiEventLogEntryAdd:
	    {
	      SaHpiSessionIdT  session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiSelEntryT   evt_entry;

	      if ( HpiDemarshalRequest3( header.m_flags & dMhEndianBit, hm, data,
				   &session_id, &resource_id, &evt_entry ) < 0 )
		   return eResultError;

	      ret = saHpiEventLogEntryAdd( session_id, resource_id,
					   &evt_entry );
	      
	      DbgFunc( "saHpiEventLogEntryAdd( %x, %x ) = %d\n",
                       session_id, resource_id, ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }

	    break;

       case eFsaHpiEventLogEntryDelete:
	    {
	      SaHpiSessionIdT  session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiSelEntryIdT entry_id;

	      if ( HpiDemarshalRequest3( header.m_flags & dMhEndianBit, hm, data,
				   &session_id, &resource_id, &entry_id ) < 0 )
		   return eResultError;

	      ret = saHpiEventLogEntryDelete( session_id, resource_id, entry_id );

	      DbgFunc( "saHpiEventLogEntryDelete( %x, %x, %x ) = %d\n",
                       session_id, resource_id, entry_id, ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }
	    
	    break;

       case eFsaHpiEventLogClear:
	    {
	      SaHpiSessionIdT session_id;
	      SaHpiResourceIdT resource_id;

	      if ( HpiDemarshalRequest2( header.m_flags & dMhEndianBit, hm, data,
				   &session_id, &resource_id ) < 0 )
		   return eResultError;

	      ret = saHpiEventLogClear( session_id, resource_id );

	      DbgFunc( "saHpiEventLogClear( %x, %x ) = %d\n",
                       session_id, resource_id, ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }

	    break;

       case eFsaHpiEventLogTimeGet:
	    {
	      SaHpiSessionIdT session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiTimeT       ti;
	      
	      if ( HpiDemarshalRequest2( header.m_flags & dMhEndianBit, hm, data,
				    &session_id, &resource_id ) < 0 )
		   return eResultError;

	      ret = saHpiEventLogTimeGet( session_id, resource_id, &ti );

	      DbgFunc( "saHpiEventLogTimeGet( %x, %x ) = %d\n",
                       session_id, resource_id, ret );

	      rh.m_len = HpiMarshalReply1( hm, rd, &ret, &ti );
	    }

	    break;

       case eFsaHpiEventLogTimeSet:
	    {
	      SaHpiSessionIdT session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiTimeT       ti;

	      if ( HpiDemarshalRequest3( header.m_flags & dMhEndianBit, hm, data,
				    &session_id, &resource_id , &ti ) < 0 )
		   return eResultError;

	      ret = saHpiEventLogTimeSet( session_id, resource_id, ti );
 
	      DbgFunc( "saHpiEventLogTimeSet( %x, %x ) = %d\n",
                       session_id, resource_id, ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }

	    break;

       case eFsaHpiEventLogStateGet:
	    {
	      SaHpiSessionIdT session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiBoolT       enable;

	      if ( HpiDemarshalRequest2( header.m_flags & dMhEndianBit, hm, data,
				   &session_id, &resource_id ) < 0 )
		   return eResultError;

	      ret = saHpiEventLogStateGet( session_id, resource_id, &enable );

	      DbgFunc( "saHpiEventLogStateGet( %x, %x ) = %d\n",
                       session_id, resource_id, ret );

	      rh.m_len = HpiMarshalReply1( hm, rd, &ret, &enable );
	    }

	    break;

       case eFsaHpiEventLogStateSet:
	    {
	      SaHpiSessionIdT  session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiBoolT       enable;

	      if ( HpiDemarshalRequest3( header.m_flags & dMhEndianBit, hm, data,
				   &session_id, &resource_id, &enable ) < 0 )
		   return eResultError;

	      ret = saHpiEventLogStateSet( session_id, resource_id, enable );
	      
	      DbgFunc( "saHpiEventLogStateSet( %x, %x, %s ) = %d\n",
                       session_id, resource_id, enable ? "true" : "false", ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }

	    break;

       case eFsaHpiSubscribe:
	    {
	      SaHpiSessionIdT session_id;
	      SaHpiBoolT      provide_active_alarms;

	      if ( HpiDemarshalRequest2( header.m_flags & dMhEndianBit, hm, data,
				    &session_id, &provide_active_alarms ) < 0 )
		   return eResultError;

	      ret = saHpiSubscribe( session_id, provide_active_alarms );

	      DbgFunc( "saHpiSubscribe( %x, %s ) = %d\n",
                       session_id,  provide_active_alarms ? "true" : "false",
		       ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }

	    break;

       case eFsaHpiUnsubscribe:
	    {
	      SaHpiSessionIdT session_id;

	      if ( HpiDemarshalRequest1( header.m_flags & dMhEndianBit, hm, data,
				    &session_id ) < 0 )
		   return eResultError;

	      ret = saHpiUnsubscribe( session_id );

	      DbgFunc( "saHpiUnsubscribe( %x ) = %d\n",
                       session_id, ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }

	    break;

       case eFsaHpiEventGet:
	    {
	      SaHpiSessionIdT session_id;
	      SaHpiTimeoutT   timeout;
	      SaHpiEventT     event;
	      SaHpiRdrT       rdr;
	      SaHpiRptEntryT  rpt_entry;

	      if ( HpiDemarshalRequest2( header.m_flags & dMhEndianBit, hm, data,
				   &session_id, &timeout ) < 0 )
		   return eResultError;

	      if ( timeout == 0 )
		 {
		   ret = saHpiEventGet( session_id, timeout, &event, &rdr, &rpt_entry );

		   DbgFunc( "saHpiEventGet( %x ) = %d\n",
			    session_id, ret );

		   rh.m_len = HpiMarshalReply3( hm, rd, &ret, &event, &rdr, &rpt_entry );
		 }
	      else
		 {
		   cSession *s = c->FindSession( session_id );

		   if ( s && !s->IsEventGet() )
		      {
			s->EventGet( true );

			SaHpiTimeT end;
			gettimeofday1( &end );

			if ( timeout == SAHPI_TIMEOUT_BLOCK )
			     end += (SaHpiTimeT)10000*1000000000; //set a long time
			else
			     end += timeout;

			s->Timeout() = end;

			s->EventGetSeq() = header.m_seq;

			DbgEvent( "saHpiEventGet( %x ): add to event listener.\n",
				  s->SessionId() );

			return eResultOk;
		      }

		   // error
		   ret = SA_ERR_HPI_BUSY;
		   rh.m_len = HpiMarshalReply3( hm, rd, &ret, &event, &rdr, &rpt_entry );
		 }
	    }

	    break;

       case eFsaHpiRdrGet:
	    {
	      SaHpiSessionIdT  session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiEntryIdT    entry_id;
	      SaHpiEntryIdT    next_entry_id;
	      SaHpiRdrT        rdr;

	      if ( HpiDemarshalRequest3( header.m_flags & dMhEndianBit, hm, data,
				    &session_id, &resource_id, &entry_id ) < 0 )
		   return eResultError;

	      ret = saHpiRdrGet( session_id, resource_id, entry_id,
				 &next_entry_id, &rdr );

	      DbgFunc( "saHpiRdrGet( %x, %x, %x ) = %d\n",
                       session_id, resource_id, entry_id, ret );

	      rh.m_len = HpiMarshalReply2( hm, rd, &ret, &next_entry_id, &rdr );
	    }

	    break;

       case eFsaHpiSensorReadingGet:
	    {
	      SaHpiSessionIdT  session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiSensorNumT  sensor_num;
	      SaHpiSensorReadingT reading;
	      
	      if ( HpiDemarshalRequest3( header.m_flags & dMhEndianBit, hm, data,
				    &session_id, &resource_id, &sensor_num ) < 0 )
		   return eResultError;

	      ret = saHpiSensorReadingGet( session_id, resource_id,
					   sensor_num, &reading );
	      
	      DbgFunc( "saHpiSensorReadingGet( %x, %x, %x ) = %d\n",
                       session_id, resource_id, sensor_num, ret );

	      rh.m_len = HpiMarshalReply1( hm, rd, &ret, &reading );
	    }

	    break;

       case eFsaHpiSensorReadingConvert:
	    {
	      SaHpiSessionIdT session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiSensorNumT  sensor_num;
	      SaHpiSensorReadingT reading_input;
	      SaHpiSensorReadingT converted_reading;

	      if ( HpiDemarshalRequest4( header.m_flags & dMhEndianBit, hm, data,
				    &session_id, &resource_id, &sensor_num,
				    &reading_input ) < 0 )
		   return eResultError;

	      ret = saHpiSensorReadingConvert( session_id,
					       resource_id, sensor_num,
					       &reading_input,
					       &converted_reading );

	      DbgFunc( "saHpiSensorReadingConvert( %x, %x, %x ) = %d\n",
                       session_id, resource_id, sensor_num, ret );

	      rh.m_len = HpiMarshalReply1( hm, rd, &ret, &converted_reading );
	    }

	    break;

       case eFsaHpiSensorThresholdsGet:
	    {
	      SaHpiSessionIdT session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiSensorNumT  sensor_num;
	      SaHpiSensorThresholdsT sensor_thresholds;

	      if ( HpiDemarshalRequest3( header.m_flags & dMhEndianBit, hm, data,
				   &session_id, &resource_id, &sensor_num ) < 0 )
		   return eResultError;

	      ret = saHpiSensorThresholdsGet( session_id,
					      resource_id, sensor_num,
					      &sensor_thresholds);

	      DbgFunc( "saHpiSensorThresholdsGet( %x, %x, %x ) = %d\n",
                       session_id, resource_id, sensor_num,  ret );

	      rh.m_len = HpiMarshalReply1( hm, rd, &ret, &sensor_thresholds );
	    }

	    break;

       case eFsaHpiSensorThresholdsSet:
	    {
	      SaHpiSessionIdT session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiSensorNumT  sensor_num;
	      SaHpiSensorThresholdsT sensor_thresholds;

	      if ( HpiDemarshalRequest4( header.m_flags & dMhEndianBit, hm, data,
				   &session_id, &resource_id, &sensor_num,
				   &sensor_thresholds ) < 0 )
		   return eResultError;

	      ret = saHpiSensorThresholdsSet( session_id, resource_id,
					      sensor_num,
					      &sensor_thresholds );

	      DbgFunc( "saHpiSensorThresholdsSet( %x, %x, %x ) = %d\n",
                       session_id, resource_id, sensor_num, ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }

	    break;

       case eFsaHpiSensorTypeGet:
	    {
	      SaHpiResourceIdT resource_id;
	      SaHpiSessionIdT  session_id;
	      SaHpiSensorNumT  sensor_num;
	      SaHpiSensorTypeT type;
	      SaHpiEventCategoryT category;

	      if ( HpiDemarshalRequest3( header.m_flags & dMhEndianBit, hm, data,
				   &session_id, &resource_id, &sensor_num ) < 0 )
		   return eResultError;

	      ret = saHpiSensorTypeGet( session_id, resource_id,
					sensor_num, &type, &category );

	      DbgFunc( "saHpiSensorTypeGet( %x, %x, %x ) = %d\n",
                       session_id, resource_id, sensor_num, ret );

	      rh.m_len = HpiMarshalReply2( hm, rd, &ret, &type, &category );
	    }

	    break;

       case eFsaHpiSensorEventEnablesGet:
	    {
	      SaHpiSessionIdT        session_id;
	      SaHpiResourceIdT       resource_id;
	      SaHpiSensorNumT        sensor_num;
	      SaHpiSensorEvtEnablesT enables;

	      if ( HpiDemarshalRequest3( header.m_flags & dMhEndianBit, hm, data,
				   &session_id, &resource_id, &sensor_num ) < 0 )
		   return eResultError;

	      ret = saHpiSensorEventEnablesGet( session_id, resource_id,
						sensor_num, &enables );

	      DbgFunc( "saHpiSensorEventEnablesGet( %x, %x, %x ) = %d\n",
                       session_id, resource_id, sensor_num, ret );

	      rh.m_len = HpiMarshalReply1( hm, rd, &ret, &enables );
	    }

	    break;

       case eFsaHpiSensorEventEnablesSet:
	    {
	      SaHpiSessionIdT  session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiSensorNumT  sensor_num;
	      SaHpiSensorEvtEnablesT enables;

	      if ( HpiDemarshalRequest4( header.m_flags & dMhEndianBit, hm, data,
				    &session_id, &resource_id, &sensor_num,
				    &enables ) < 0 )
		   return eResultError;

	      ret = saHpiSensorEventEnablesSet( session_id, resource_id,
						sensor_num, &enables );
	      
	      DbgFunc( "saHpiSensorEventEnablesSet( %x, %x, %x ) = %d\n",
                       session_id, resource_id, sensor_num, ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }
	    
	    break;

       case eFsaHpiControlTypeGet:
	    {
	      SaHpiSessionIdT session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiCtrlNumT    ctrl_num;
	      SaHpiCtrlTypeT   type;

	      if ( HpiDemarshalRequest3( header.m_flags & dMhEndianBit, hm, data,
				   &session_id, &resource_id, &ctrl_num ) < 0 )
		   return eResultError;

	      ret = saHpiControlTypeGet( session_id, resource_id, ctrl_num,
					 &type );

	      DbgFunc( "saHpiControlTypeGet( %x, %x, %x ) = %d\n",
                       session_id, resource_id, ctrl_num, ret );

	      rh.m_len = HpiMarshalReply1( hm, rd, &ret, &type );
	    }

	    break;

       case eFsaHpiControlStateGet:
	    {
	      SaHpiSessionIdT  session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiCtrlNumT    ctrl_num;
	      SaHpiCtrlStateT  ctrl_state;

	      if ( HpiDemarshalRequest3( header.m_flags & dMhEndianBit, hm, data,
				    &session_id, &resource_id, &ctrl_num ) < 0 )
		   return eResultError;

	      ret = saHpiControlStateGet( session_id, resource_id,
					  ctrl_num, &ctrl_state );

	      DbgFunc( "saHpiControlStateGet( %x, %x, %x ) = %d\n",
                       session_id, resource_id, ctrl_num, ret );

	      rh.m_len = HpiMarshalReply1( hm, rd, &ret, &ctrl_state );
	    }

	    break;

       case eFsaHpiControlStateSet:
	    {
	      SaHpiSessionIdT  session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiCtrlNumT    ctrl_num;
	      SaHpiCtrlStateT  ctrl_state;

	      if ( HpiDemarshalRequest4( header.m_flags & dMhEndianBit, hm, data,
				    &session_id, &resource_id, &ctrl_num,
				    &ctrl_state ) < 0 )
		   return eResultError;

	      ret = saHpiControlStateSet( session_id, resource_id,
					  ctrl_num, &ctrl_state );

	      DbgFunc( "saHpiControlStateSet( %x, %x, %x ) = %d\n",
                       session_id, resource_id, ctrl_num, ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }

	    break;

       case eFsaHpiEntityInventoryDataRead:
	    {
	      SaHpiSessionIdT  session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiEirIdT      eir_id;
	      SaHpiUint32T     buffer_size;
	      unsigned char   *buffer = 0;
	      SaHpiUint32T     actual_size;

	      if ( HpiDemarshalRequest4( header.m_flags & dMhEndianBit, hm, data,
				    &session_id, &resource_id, &eir_id, &buffer_size ) < 0 )
		   return eResultError;

	      if ( buffer_size )
		   buffer = new unsigned char [buffer_size];

	      ret = saHpiEntityInventoryDataRead( session_id, resource_id, eir_id,
						  buffer_size, (SaHpiInventoryDataT *)(void *)buffer,
						  &actual_size );

	      DbgFunc( "saHpintityInventoryDataRead( %x, %x, %x, %d ) = %d\n",
                       session_id, resource_id, eir_id, buffer_size, ret );

	      const cMarshalType *reply[4];
	      reply[0] = &SaErrorType; // SA_OK
	      reply[1] = &SaHpiUint32Type;  // actual size

	      const void *params[3];
	      params[0] = &ret;
	      params[1] = &actual_size;

	      if ( ret != SA_OK || buffer == 0 )
		   reply[2] = 0;		   
	      else
		 {
  		   reply[2] = &SaHpiInventoryDataType, // inventory data
		   reply[3] = 0;		   

		   params[2] = buffer;
		 }

	      rh.m_len = MarshalArray( reply, params, rd );

	      if ( buffer )
		   delete [] buffer;
	    }

	    break;

       case eFsaHpiEntityInventoryDataWrite:
	    {
	      SaHpiSessionIdT  session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiEirIdT      eir_id;
	      unsigned char    buffer[10240];

	      if ( HpiDemarshalRequest4( header.m_flags & dMhEndianBit, hm, data,
				    &session_id, &resource_id, &eir_id, buffer ) < 0 )
		   return eResultError;

	      ret = saHpiEntityInventoryDataWrite( session_id, resource_id, eir_id,
						   (SaHpiInventoryDataT *)(void *)buffer );

	      DbgFunc( "saHpintityInventoryDataWrite( %x, %x, %x ) = %d\n",
                       session_id, resource_id, eir_id, ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }
	    break;

       case eFsaHpiWatchdogTimerGet:
	    {
	      SaHpiSessionIdT   session_id;
	      SaHpiResourceIdT  resource_id;
	      SaHpiWatchdogNumT watchdog_num;
	      SaHpiWatchdogT    watchdog;

	      if ( HpiDemarshalRequest3( header.m_flags & dMhEndianBit, hm, data,
				   &session_id, &resource_id, &watchdog_num ) < 0 )
		   return eResultError;

	      ret = saHpiWatchdogTimerGet( session_id, resource_id,
					   watchdog_num, &watchdog );

	      DbgFunc( "saHpiWatchdogTimerGet( %x, %x, %x ) = %d\n",
                       session_id, resource_id, watchdog_num, ret );

	      rh.m_len = HpiMarshalReply1( hm, rd, &ret, &watchdog );
	    }

	    break;

       case eFsaHpiWatchdogTimerSet:
	    {
	      SaHpiSessionIdT   session_id;
	      SaHpiResourceIdT  resource_id;
	      SaHpiWatchdogNumT watchdog_num;
	      SaHpiWatchdogT    watchdog;

	      if ( HpiDemarshalRequest4( header.m_flags & dMhEndianBit, hm, data,
				    &session_id, &resource_id, &watchdog_num,
				    &watchdog ) < 0 )
		   return eResultError;

	      ret = saHpiWatchdogTimerSet( session_id, resource_id,
					   watchdog_num, &watchdog );
	      
	      DbgFunc( "saHpiWatchdogTimerSet( %x, %x, %x ) = %d\n",
                       session_id, resource_id, watchdog_num, ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }
	    
	    break;

       case eFsaHpiWatchdogTimerReset:
	    {
	      SaHpiSessionIdT   session_id;
	      SaHpiResourceIdT  resource_id;
	      SaHpiWatchdogNumT watchdog_num;

	      if ( HpiDemarshalRequest3( header.m_flags & dMhEndianBit, hm, data,
				    &session_id, &resource_id, &watchdog_num ) < 0 )
		   return eResultError;

	      ret = saHpiWatchdogTimerReset( session_id, resource_id,
					     watchdog_num );

	      DbgFunc( "eFsaHpiWatchdogTimerReset( %x, %x, %x ) = %d\n",
                       session_id, resource_id, watchdog_num, ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }
	    
	    break;

       case eFsaHpiHotSwapControlRequest:
	    {
	      SaHpiSessionIdT session_id;
	      SaHpiResourceIdT resource_id;

	      if ( HpiDemarshalRequest2( header.m_flags & dMhEndianBit, hm, data,
				   &session_id, &resource_id ) < 0 )
		   return eResultError;

	      ret = saHpiHotSwapControlRequest( session_id, resource_id );

	      DbgFunc( "saHpiHotSwapControlRequest( %x, %x ) = %d\n",
                       session_id, resource_id , ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }

	    break;

       case eFsaHpiResourceActiveSet:
	    {
	      SaHpiSessionIdT session_id;
	      SaHpiResourceIdT resource_id;
	      if ( HpiDemarshalRequest2( header.m_flags & dMhEndianBit, hm, data,
				   &session_id, &resource_id ) < 0 )
		   return eResultError;

	      ret = saHpiResourceActiveSet( session_id, resource_id );
	      
	      DbgFunc( "saHpiResourceActiveSet( %x, %x ) = %d\n",
                       session_id, resource_id , ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }
	    
	    break;

       case eFsaHpiResourceInactiveSet:
	    {
	      SaHpiSessionIdT session_id;
	      SaHpiResourceIdT resource_id;
	      if ( HpiDemarshalRequest2( header.m_flags & dMhEndianBit, hm, data,
				    &session_id, &resource_id ) < 0 )
		   return eResultError;

	      ret = saHpiResourceInactiveSet( session_id, resource_id );

	      DbgFunc( "saHpiResourceInactiveSet( %x, %x ) = %d\n",
                       session_id, resource_id , ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }

	    break;

       case eFsaHpiAutoInsertTimeoutGet:
	    {
	      SaHpiSessionIdT session_id;
	      SaHpiTimeoutT   timeout;
	      
	      if ( HpiDemarshalRequest1( header.m_flags & dMhEndianBit, hm, data,
				   &session_id ) < 0 )
		   return eResultError;

	      ret = saHpiAutoInsertTimeoutGet( session_id, &timeout );
	      
	      DbgFunc( "saHpiAutoInsertTimeoutGet( %x ) = %d\n",
                       session_id, ret );

	      rh.m_len = HpiMarshalReply1( hm, rd, &ret, &timeout );
	    }

	    break;

       case eFsaHpiAutoInsertTimeoutSet:
	    {
	      SaHpiSessionIdT session_id;
	      SaHpiTimeoutT   timeout;

	      if ( HpiDemarshalRequest2( header.m_flags & dMhEndianBit, hm, data,
				    &session_id, &timeout ) < 0 )
		   return eResultError;

	      ret = saHpiAutoInsertTimeoutSet( session_id, timeout );
	      
	      DbgFunc( "saHpiAutoInsertTimeoutSet( %x ) = %d\n",
                       session_id, ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }
	    
	    break;

       case eFsaHpiAutoExtractTimeoutGet:
	    {
	      SaHpiSessionIdT  session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiTimeoutT    timeout;

	      if ( HpiDemarshalRequest2( header.m_flags & dMhEndianBit, hm, data,
				    &session_id, &resource_id ) < 0 )
		   return eResultError;

	      ret = saHpiAutoExtractTimeoutGet( session_id, resource_id, &timeout );

	      DbgFunc( "saHpiAutoExtractTimeoutGet( %x, %x ) = %d\n",
                       session_id, resource_id, ret );

	      rh.m_len = HpiMarshalReply1( hm, rd, &ret, &timeout );
	    }

	    break;

       case eFsaHpiAutoExtractTimeoutSet:
	    {
	      SaHpiSessionIdT  session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiTimeoutT    timeout;

	      if ( HpiDemarshalRequest3( header.m_flags & dMhEndianBit, hm, data,
				   &session_id, &resource_id, &timeout ) < 0 )
		   return eResultError;

	      ret = saHpiAutoExtractTimeoutSet( session_id, resource_id, timeout );

	      DbgFunc( "saHpiAutoExtractTimeoutSet( %x, %x ) = %d\n",
                       session_id, resource_id, ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }

	    break;

       case eFsaHpiHotSwapStateGet:
	    {
	      SaHpiSessionIdT  session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiHsStateT    state;

	      if ( HpiDemarshalRequest2( header.m_flags & dMhEndianBit, hm, data,
				   &session_id, &resource_id ) < 0 )
		   return eResultError;

	      ret = saHpiHotSwapStateGet( session_id, resource_id, &state );

	      DbgFunc( "saHpiHotSwapStateGet( %x, %x ) = %d\n",
                       session_id, resource_id, ret );

	      rh.m_len = HpiMarshalReply1( hm, rd, &ret, &state );
	    }
	    
	    break;

       case eFsaHpiHotSwapActionRequest:
	    {
	      SaHpiSessionIdT session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiHsActionT   action;

	      if ( HpiDemarshalRequest3( header.m_flags & dMhEndianBit, hm, data,
				   &session_id, &resource_id, &action ) < 0 )
		   return eResultError;

	      ret = saHpiHotSwapActionRequest( session_id, resource_id, action );

	      DbgFunc( "saHpiHotSwapActionRequest( %x, %x ) = %d\n",
                       session_id, resource_id , ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }
	    
	    break;

       case eFsaHpiResourcePowerStateGet:
	    {
	      SaHpiSessionIdT    session_id;
	      SaHpiResourceIdT   resource_id;
	      SaHpiHsPowerStateT state;

	      if ( HpiDemarshalRequest2( header.m_flags & dMhEndianBit, hm, data,
				   &session_id, &resource_id ) < 0 )
		   return eResultError;

	      ret = saHpiResourcePowerStateGet( session_id, resource_id, &state );
	      
	      DbgFunc( "saHpiResourcePowerStateGet( %x, %x ) = %d\n",
                       session_id, resource_id, ret );

	      rh.m_len = HpiMarshalReply1( hm, rd, &ret, &state );
	    }
	    
	    break;

       case eFsaHpiResourcePowerStateSet:
	    {
	      SaHpiSessionIdT    session_id;
	      SaHpiResourceIdT   resource_id;
	      SaHpiHsPowerStateT state;

	      if ( HpiDemarshalRequest3( header.m_flags & dMhEndianBit, hm, data,
				   &session_id, &resource_id, &state  ) < 0 )
		   return eResultError;

	      ret = saHpiResourcePowerStateSet( session_id, resource_id, state );

	      DbgFunc( "(saHpiResourcePowerStateSet %x, %x ) = %d\n",
                       session_id, resource_id , ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }

	    break;

       case eFsaHpiHotSwapIndicatorStateGet:
	    {
	      SaHpiSessionIdT        session_id;
	      SaHpiResourceIdT       resource_id;
	      SaHpiHsIndicatorStateT state;

	      if ( HpiDemarshalRequest2( header.m_flags & dMhEndianBit, hm, data,
				   &session_id, &resource_id ) < 0 )
		   return eResultError;

	      ret = saHpiHotSwapIndicatorStateGet( session_id, resource_id, &state );

	      DbgFunc( "saHpiHotSwapIndicatorStateGet( %x, %x ) = %d\n",
                       session_id, resource_id , ret );

	      rh.m_len = HpiMarshalReply1( hm, rd, &ret, &state );
	    }

	    break;

       case eFsaHpiHotSwapIndicatorStateSet:
	    {
	      SaHpiSessionIdT        session_id;
	      SaHpiResourceIdT       resource_id;
	      SaHpiHsIndicatorStateT state;

	      if ( HpiDemarshalRequest3( header.m_flags & dMhEndianBit, hm, data,
				    &session_id, &resource_id, &state ) < 0 )
		   return eResultError;

	      ret = saHpiHotSwapIndicatorStateSet( session_id, resource_id, state );

	      DbgFunc( "saHpiHotSwapIndicatorStateSet( %x, %x ) = %d\n",
                       session_id, resource_id , ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }
	    
	    break;

       case eFsaHpiParmControl:
	    {
	      SaHpiSessionIdT  session_id;
	      SaHpiResourceIdT resource_id;
	      SaHpiParmActionT action;

	      if ( HpiDemarshalRequest3( header.m_flags & dMhEndianBit, hm, data,
				    &session_id, &resource_id, &action ) < 0 )
		   return eResultError;

	      ret = saHpiParmControl( session_id, resource_id, action );

	      DbgFunc( "saHpiParmControl( %x, %x ) = %d\n",
                       session_id, resource_id, ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret  );
	    }

	    break;

       case eFsaHpiResourceResetStateGet:
	    {
	      SaHpiSessionIdT   session_id;
	      SaHpiResourceIdT  resource_id;
	      SaHpiResetActionT reset_action;

	      if ( HpiDemarshalRequest2( header.m_flags & dMhEndianBit, hm, data,
				    &session_id, &resource_id ) < 0 )
		   return eResultError;

	      ret = saHpiResourceResetStateGet( session_id, resource_id,
						&reset_action );

	      DbgFunc( "saHpiResourceResetStateGet( %x, %x ) = %d\n",
                       session_id, resource_id, ret );

	      rh.m_len = HpiMarshalReply1( hm, rd, &ret, &reset_action );
	    }

	    break;

       case eFsaHpiResourceResetStateSet:
	    {
	      SaHpiSessionIdT   session_id;
	      SaHpiResourceIdT  resource_id;
	      SaHpiResetActionT reset_action;

	      if ( HpiDemarshalRequest3( header.m_flags & dMhEndianBit, hm, data,
				    &session_id, &resource_id, &reset_action ) < 0 )
		   return eResultError;

	      ret = saHpiResourceResetStateSet( session_id, resource_id, reset_action );

	      DbgFunc( "saHpiResourceResetStateSet( %x, %x ) = %d\n",
                       session_id, resource_id, ret );

	      rh.m_len = HpiMarshalReply0( hm, rd, &ret );
	    }

	    break;

       default:
	    assert( 0 );
	    break;
     }

  assert( rh.m_len <= hm->m_reply_len );

  return eResultReply;
}


int
main( int argc, char *argv[] )
{
  int rv = 1;

  cOpenHpiDaemon *s = new cOpenHpiDaemon;

  if ( s->ParseArgs( argc, argv ) )
     {
       if ( s->Initialize() )
	  {
	    rv = s->MainLoop();
	    s->Finalize();
	  }
     }

  delete s;

  return rv;
}


bool
cOpenHpiDaemon::HandleInteractive()
{
  unsigned char ch;

  int rv = read( 0, &ch, 1 );

  if ( rv != 1 )
       return true;

  switch( ch )
     {
       case 'p': // ping
	    printf( "pong\n" );
	    break;

       case 'x': // exit
	    return false;	    
     }

  return true;
}
