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


#ifndef __COMMON_HPI_SUB_PROVIDER_FUMI_H__
#define __COMMON_HPI_SUB_PROVIDER_FUMI_H__

#include <deque>

#include <SaHpi.h>

#include <HpiInfo.h>


/************************************************
 * Common stuff for FUMI* sub-providers
 ***********************************************/
void GetFwInstanceInfo( const wchar_t * name,
                        const SaHpiFumiFirmwareInstanceInfoT& fwii,
                        std::deque<HpiInfo>& info );


#endif // __COMMON_HPI_SUB_PROVIDER_FUMI_H__

