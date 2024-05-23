---
title: "Traffic Incident Data | Microsoft Docs"
description: This article describes the Traffic Incident Data contained in TrafficIncident resources, returned by a Traffic URL, in a table that describes each field. Both JSON and XML formats are shown.
ms.custom: ""
ms.date: "09/12/2023"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: f04e3fe7-8308-4d64-8180-455780d8376e
caps.latest.revision: 21
author: "flavius-stoichescu"
ms.author: "flstoich"
manager: "ccapota"
ms.service: "bing-maps"
---

# Traffic Incident Data

[!INCLUDE [bing-maps-get-traffic-incidents-api-retirement](../../includes/bing-maps-get-traffic-incidents-api-retirement.md)]

The response returned by a Traffic URL contains one or more TrafficIncident resources. Each TrafficIncident resource contains information about a traffic issues that met the criteria specified in the URL request, such as map area, incident type and severity. This following table provides descriptions of the TrafficIncident resource fields and is followed by JSON and XML examples.  
  
## Traffic Incident Resource 
 
 The following table describes the fields in the traffic incident resource. One or more traffic incident resources are returned when you request traffic data. These resources are inside a common response wrapper for the Bing Maps REST Services.  For more information about the common response wrapper, see [Common Response Description](../common-response-description.md).  
  
 Fields marked **Required** are always provided for each traffic incident. Other fields are optional and not always included.  
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|`point`|`Point`|`Point`|**Required.** The latitude and longitude coordinates where you encounter the incident.|    
|`description`|`Description`|`string`|A description of the incident.<br /><br /> Examples:<br /><br /> -   W 95th St between Switzer Rd and Bluejacket Dr - construction<br />-   WB Johnson Dr at I-435 - bridge repair|  
|`start`|`StartTimeUTC`|UTC Time|**Required.** The time the incident occurred. For more information about the format, see the **About Time Values** section below.<br /><br /> Examples:<br /><br /> -   JSON: Date(1295704800000)<br />-   XML: 2011-06-29T23:44:56.593Z|  
|`end`|`EndTimeUTC`|UTC Time|**Required.** The time that the traffic incident will end. For more information about the format, see the **About Time Values** section below.<br /><br /> Examples:<br /><br /> -   JSON: Date(1295704800000)<br />-   XML: 2011-06-29T23:44:56.593Z|  
|`incidentId`|`IncidentId`|`long`|**Required.** A unique ID for the incident.|   
|`lastModified`|`LastModifiedUTC`|DateTime|**Required.** The time the incident information was last updated. For more information about the format, see the **About Time Values** section below.<br /><br /> Examples:<br /><br /> -   JSON: Date(1295704800000)<br />-   XML: 2011-06-29T23:44:56.593Z|  
|`roadClosed`|`RoadClosed`|`Boolean`|**Required.** A value of `true` indicates that there is a road closure.|  
|`severity`|`Severity`|`integer`|**Required.** Specifies the level of importance of incident.<br /><br /> -   1: LowImpact<br />-   2: Minor<br />-   3: Moderate<br />-   4: Serious|  
|`severityScore`|`SeverityScore`|`integer`| Integer score between  0 (least impactful) and 100 (most impactful), indicating the ranked impact of an incident to overall traffic conditions or disruption caused to motorists.|
|`toPoint`|`ToPoint`|`Point`|The coordinates of the end of a traffic incident, such as the end of a construction zone.|    
|`type`|`Type`|`integer`|**Required.** Specifies the type of incident.<br /><br /> -   1: Accident<br />-   2: Congestion<br />-   3: DisabledVehicle<br />-   4: MassTransit<br />-   5: Miscellaneous<br />-   6: OtherNews<br />-   7: PlannedEvent<br />-   8: RoadHazard<br />-   9: Construction<br />-   10: Alert<br />-   11: Weather|  
|`verified`|`Verified`|`boolean`    |**Deprecated.**<br/>*Always true.*<br/><br/>A value of `true` indicates that the incident has been visually verified or otherwise officially confirmed by a source like the local police department.|  
|`isEndTimeBackfilled`|`IsEndTimeBackfilled`|`boolean`| Flag used to determine if incident end time is calculated by adding 2 hours to the start time. A value of `false` indicates the end time is provided.|
|`title`|`Title`| `string` | Names and direction of affected roads. |
|`alertCCodes`|`AlertCCodes`| array of `integer`| **Deprecated.**<br/>*Use `eventList` instead.*<br/><br/> List of internal event codes, Microsoft mapped from Alert-C Codes.|
|`eventList`| `EventList` | array of `integer` | List of Alert-C Codes for the incident. <br/><br/> Note that this array is not ordered.|
|`icon`| `Icon` | `integer` | Icon suggestion for rendering the incident on the map.<br/> - 0: Warning <br /> - 1: RoadClosure <br/> - 2: Accident <br/> - 3: Construction <br/> - 4: HeavyTraffic <br /> - 5: ModerateTraffic <br /> - 6: Restrictions|
|`isJamcident`|`IsJamcident`|`boolean`| Flag indicating that the area of road covered by this incident is experiencing abnormal traffic conditions resulting in non-typical delays.|
### About time values  

Time values in the TrafficIncident resource data use UTC time. The format for XML and JSON responses are different.  
  
For JSON responses, the time is specified as UTC time in milliseconds using the epoch (start time) of January 1, 1970, 00:00:00.  The JSON field uses the following format.  
  
`Date(milliseconds)`  
  
 JSON Example: Date(1295704800000)  
  
 For XML responses, the time is specified as UTC time and uses the following format. A time zone offset is not specified.  
  
`YYYY-MM-DDThh:mm:ss.sZ`
  
 XML Example: 2011-06-29T23:44:56.593Z  
  
 For more information about UTC time see [W3C Date and Time Formats](https://www.w3.org/TR/NOTE-datetime).  
  
## Examples

 The following are TrafficIncident Data resource examples. To see the complete response including the common response container, see the examples in [Get Traffic Incidents](get-traffic-incidents.md) and the [Common Response Description](../common-response-description.md).  
  
### JSON Example  
  
```json
{
    "authenticationResultCode": "ValidCredentials",
    "brandLogoUri": "http://dev.virtualearth.net/Branding/logo_powered_by.png",
    "copyright": "Copyright © 2023 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",
    "resourceSets": [
        {
            "estimatedTotal": 1802,
            "resources": [
                {
                    "__type": "TrafficIncident:http://schemas.microsoft.com/search/local/ws/rest/v1",
                    "point": {
                        "type": "Point",
                        "coordinates": [
                            39.682642,
                            -104.939053
                        ]
                    },
                    "alertCCodes": [
                        4
                    ],
                    "delay": 0,
                    "description": "At CO 2/Colorado Boulevard (Denver) at Mile Point 204. Two right lanes are closed due to a crash.",
                    "end": "/Date(1694535707744)/",
                    "eventList": [
                        203
                    ],
                    "icon": 2,
                    "incidentId": 18558549332008001,
                    "isEndTimeBackfilled": true,
                    "isJamcident": false,
                    "lastModified": "/Date(1694528507744)/",
                    "roadClosed": false,
                    "severity": 4,
                    "severityScore": 99,
                    "source": 5,
                    "start": "/Date(1694526697000)/",
                    "title": "I-25 N / US-87 N",
                    "toPoint": {
                        "type": "Point",
                        "coordinates": [
                            39.68307,
                            -104.940412
                        ]
                    },
                    "type": 1,
                    "verified": true
                }
            ]
        }
    ],
    "statusCode": 200,
    "statusDescription": "OK",
    "traceId": "0e2cfdc28b554661b9539c1891244f28|DU00003090|0.0.0.0"
}
```  
  
### XML Example  
  
```xml
<?xml version="1.0" encoding="utf-8"?>
<Response xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">
    <Copyright>Copyright © 2023 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>
    <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>
    <StatusCode>200</StatusCode>
    <StatusDescription>OK</StatusDescription>
    <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>
    <TraceId>de2ccfce537149d1a946feb025d8a65c|DU00003094|0.0.0.0</TraceId>
    <ResourceSets>
        <ResourceSet>
            <EstimatedTotal>1806</EstimatedTotal>
            <Resources>
                <TrafficIncident>
                    <Point>
                        <Latitude>39.682642</Latitude>
                        <Longitude>-104.939053</Longitude>
                    </Point>
                    <Source>5</Source>
                    <IncidentId>18558549332008001</IncidentId>
                    <LastModifiedUTC>2023-09-12T14:23:33.2106067Z</LastModifiedUTC>
                    <StartTimeUTC>2023-09-12T13:51:37Z</StartTimeUTC>
                    <EndTimeUTC>2023-09-12T16:23:33.2106067Z</EndTimeUTC>
                    <Type>Accident</Type>
                    <Icon>Accident</Icon>
                    <Severity>Serious</Severity>
                    <Verified>true</Verified>
                    <RoadClosed>false</RoadClosed>
                    <Description>At CO 2/Colorado Boulevard (Denver) at Mile Point 204. Two right lanes are closed due to a crash.</Description>
                    <ToPoint>
                        <Latitude>39.68307</Latitude>
                        <Longitude>-104.940412</Longitude>
                    </ToPoint>
                    <Title>I-25 N / US-87 N</Title>
                    <IsEndTimeBackfilled>true</IsEndTimeBackfilled>
                    <IsExpired xsi:nil="true" />
                    <LevelOfDetail xsi:nil="true" />
                    <Delay>0</Delay>
                    <IsJamcident>false</IsJamcident>
                    <SeverityScore>99</SeverityScore>
                    <EventList>
                        <int>203</int>
                    </EventList>
                    <AlertCCodes>
                        <int>4</int>
                    </AlertCCodes>
                </TrafficIncident>                
            </Resources>
        </ResourceSet>
    </ResourceSets>
</Response>
  
```
