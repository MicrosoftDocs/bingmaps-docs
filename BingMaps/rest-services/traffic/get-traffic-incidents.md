---
title: "Get Traffic Incidents | Microsoft Docs"
description: This article describes how to get traffic incidents and provides a URL template to request traffic incident information. Template parameters and examples are provided.
ms.custom: ""
ms.date: "05/21/2024"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 2d23ea4d-48d1-4760-a072-436c00b3658d
caps.latest.revision: 20
author: "flavius-stoichescu"
ms.author: "flstoich"
manager: "ccapota"
ms.service: "bing-maps"
---

# Get Traffic Incidents

[!INCLUDE [bing-maps-get-traffic-incidents-api-retirement](../../includes/bing-maps-get-traffic-incidents-api-retirement.md)]

Use the following URL template to request traffic incident information. A collection of traffic incidents is returned in the response.  
  
 For more information about the traffic incident data that is returned in the response, see [Traffic Incident Data](traffic-incident-data.md). You can also view the example URL and response values in the [Examples](#examples) section below. For an overview of how traffic incident information is returned by Bing Maps REST Services, see [Getting Traffic Incident Data](../getting-traffic-incident-data.md).  
  
 For traffic coverage by country/region, see [Bing Maps Geographic Coverage](../../coverage/geographic-coverage.md).  
  
## Supported HTTP Methods

GET

## URL Templates  
  
[!INCLUDE [get-bing-map-key-note](../../includes/get-bing-map-key-note.md)]
  
 **Get traffic incidents.**  
  
```url
http://dev.virtualearth.net/REST/v1/Traffic/Incidents/{mapArea}/?severity={severity1,severity2,severityN}&type={type1,type2,typeN}&key={BingMapsKey}  
```  
  
### Template Parameters  
  
> [!NOTE]
>  See the [Common Parameters and Types](../common-parameters-and-types/index.md) section for additional common parameters to use with these URLs.  
>   
>  Common parameters include:  
>   
>  -   [Output Parameters](../common-parameters-and-types/output-parameters.md): Includes response output types and the JSON callback parameters.  
> -   [Culture Parameter](../common-parameters-and-types/culture-parameter.md): Includes a list of the supported cultures.  
>   
>  When an alias is provided, you can use the alias to shorten the length of the query parameter. For example, severity=6,9 can be shortened to s=6,9.  
>   
>  Parameter values are not case-sensitive.  
  
|Parameter|Alias|Description|Values|  
|---------------|-----------|-----------------|------------|  
|`mapArea`||**Required.** Specifies the area to search for traffic incident information.|Defines a rectangular area of interest on the Earth's surface in the form of a bounding box that can cover an area up to 10,000 square kilometers. The sides of the rectangle are created by specifying SouthLatitude, WestLongitude, NorthLatitude, and EastLongitude values. For more information, see [Location and Area Types](../common-parameters-and-types/location-and-area-types.md).<BR><BR>Example: `45.219,-122.325,47.610,-122.107`|  
|`includeLocationCodes`||**Deprecated.** <br />*This parameter is ignored.*<br/><br/> Specifies whether to include traffic location codes in the response. Traffic location codes provide traffic incident information for pre-defined road segments. A subscription is typically required to be able to interpret these codes for a geographical area or country/region.|One of the following values:<br /><br /> -   true<br />-   false **[default]**<br /><br /> If you want to use the default value, you can omit this parameter from the URL request.| 
|`severity`|`s`|**Optional.** Specifies severity level of traffic incidents to return.|One or more of the following integer values:<br /><br /> -   1: LowImpact<br />-   2: Minor<br />-   3: Moderate<br />-   4: Serious<br /><br /> The default is to return traffic incidents for all severity levels.<br /><br /> **Examples**:<br /><br /> severity=2,3,4<br /><br /> s=2,3,4|  
|`type`|`t`|**Optional.** Specifies the type of traffic incidents to return.|One or more of the following integer values:<br /><br /> -   1: Accident<br />-   2: Congestion<br />-   3: DisabledVehicle<br />-   4: MassTransit<br />-   5: Miscellaneous<br />-   6: OtherNews<br />-   7: PlannedEvent<br />-   8: RoadHazard<br />-   9: Construction<br />-   10: Alert<br />-   11: Weather<br /><br /> **Examples**:<br /><br /> type=2<br /><br /> t=2,9|  
| `includeJamcidents` || **Optional.** Specifices if the response should include abnormal traffic conditions that result in delays.| One of the following values: <br/>- true <br /> - false **[default]**
  
## Response

A collection of TrafficIncident resources is returned when you make a request with the URL above. For more information about the TrafficIncident resource, see [Traffic Incident Data](traffic-incident-data.md). For more information about the common response syntax for the Bing Maps REST Services, see [Common Response Description](../common-response-description.md).  
  
 These URLs support JSON (`application/json`) and XML (`application/xml`) response formats. A JSON response is provided by default, unless you request XML output by setting the output (`o`) parameter. For more information, see [Output Parameters](../common-parameters-and-types/output-parameters.md).  
  
 JSON and XML responses are provided for the URL examples in the following section.  
  
## Examples

**Get all traffic incidents in a specified area.**  
  
The following example shows how to request all traffic incident for an area defined as a bounding box (South Latitude, West Longitude, North Latitude, East Longitude). For more information about defining a bounding box, see [Location and Area Types](../common-parameters-and-types/location-and-area-types.md). Note that the includeLocationCodes parameter is not specified in this example.  
  
```url  
http://dev.virtualearth.net/REST/v1/Traffic/Incidents/37,-105,45,-94?key=YourBingMapsKey  
```  
  
 **JSON Response**  
  
 This URL returns a response with the following format that includes a list of traffic incidents as traffic incident resources. For more information on the fields returned for a traffic incident resource, see [Traffic Incident Data](traffic-incident-data.md).  
  
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
                },
                {
                    "__type": "TrafficIncident:http://schemas.microsoft.com/search/local/ws/rest/v1",
                    "point": {
                        "type": "Point",
                        "coordinates": [
                            39.04460549,
                            -94.38411355
                        ]
                    },
                    "alertCCodes": [
                        4
                    ],
                    "delay": 0,
                    "description": "Accident on I-70 E from S Lees Summit Rd/Exit 14 (I-70) to I-470/MO-291/Exit 15 (I-70).",
                    "end": "/Date(1694531388000)/",
                    "eventList": [
                        201
                    ],
                    "icon": 2,
                    "incidentId": 21366103288104000,
                    "isEndTimeBackfilled": false,
                    "isJamcident": false,
                    "lastModified": "/Date(1694528507744)/",
                    "roadClosed": false,
                    "severity": 4,
                    "severityScore": 99,
                    "source": 5,
                    "start": "/Date(1694525088000)/",
                    "title": "I-70 E",
                    "toPoint": {
                        "type": "Point",
                        "coordinates": [
                            39.04075549,
                            -94.35559355
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
  
 **XML Response**  
  
 If the output parameter is specified and set to xml (o=xml) in this URL, the URL returns a response with the following format.  
  
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
                <TrafficIncident>
                    <Point>
                        <Latitude>39.04373</Latitude>
                        <Longitude>-94.377238</Longitude>
                    </Point>
                    <Source>5</Source>
                    <IncidentId>21366103288104000</IncidentId>
                    <LastModifiedUTC>2023-09-12T14:23:33.2106067Z</LastModifiedUTC>
                    <StartTimeUTC>2023-09-12T13:24:48Z</StartTimeUTC>
                    <EndTimeUTC>2023-09-12T15:09:48Z</EndTimeUTC>
                    <Type>Accident</Type>
                    <Icon>Accident</Icon>
                    <Severity>Serious</Severity>
                    <Verified>true</Verified>
                    <RoadClosed>false</RoadClosed>
                    <Description>Accident on I-70 E from S Lees Summit Rd/Exit 14 (I-70) to I-470/MO-291/Exit 15 (I-70).</Description>
                    <ToPoint>
                        <Latitude>39.041002</Latitude>
                        <Longitude>-94.357209</Longitude>
                    </ToPoint>
                    <Title>I-70 E</Title>
                    <IsEndTimeBackfilled>false</IsEndTimeBackfilled>
                    <IsExpired xsi:nil="true" />
                    <LevelOfDetail xsi:nil="true" />
                    <Delay>0</Delay>
                    <IsJamcident>false</IsJamcident>
                    <SeverityScore>99</SeverityScore>
                    <EventList>
                        <int>201</int>
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
  
## HTTP Status Codes  
  
[!INCLUDE [get-status-code-note](../../includes/get-status-code-note.md)]
  
 When the request is successful, the following HTTP status code is returned.  
  
-   200  
  
 When the request is not successful, the response returns one of the following errors.  
  
-   400  
  
-   401  
  
-   500  
  
-   503  
  
## See Also

[Using the REST Services with .NET](../using-the-rest-services-with-net.md) 
[JSON Data Contracts](../json-data-contracts.md)
