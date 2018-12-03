---
title: "Traffic Incident Data Source | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 3ed74c1b-50e4-4f8c-b67d-60808d999c5a
caps.latest.revision: 12
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Traffic Incident Data Source
The TrafficIncident data source contains information traffic incidents. You can query for traffic incidents in a specified area by using the Bing Spatial Data Services[Query by Area](../query-api/query-by-area.md) API and the [Query Near a Route](../query-api/query-near-route.md) API and any Bing Maps Key.  
  
## Traffic Incident Properties  
 The following table describes the information provided for a traffic incident.  
  
|Property|Data Type|Description and Values|  
|--------------|---------------|----------------------------|  
|IncidentId|Edm.String|A unique ID for the incident.<br /><br /> **Example**: 210546697|  
|Latitude|Edm.Double|The latitude of the incident.<br /><br /> **Example**: 38.64829|  
|Longitude|Edm.Double|The longitude of the incident.<br /><br /> **Example**: -94.36405|  
|LastModifiedUTC|Edm.DateTime|The time the incident information was last updated specified as a Coordinated Universal Time (UTC) time.<br /><br /> **Example**: 2011-12-05T17:18:21.67Z|  
|StartTimeUTC|Edm.DateTime|The time the incident occurred specified as a Coordinated Universal Time (UTC) time..<br /><br /> **Example**: 2011-12-05T17:16:00Z|  
|EndTimeUTC|Edm.DateTime|The time that the traffic incident will end specified as a Coordinated Universal Time (UTC).<br /><br /> **Example**: 2011-12-05T17:46:00Z|  
|Type|Edm.String|The type of incident specified by one of the following values.<br /><br /> -   Accident<br />-   Congestion<br />-   DisabledVehicle<br />-   MassTransit<br />-   Miscellaneous<br />-   OtherNews<br />-   PlannedEvent<br />-   RoadHazard<br />-   Construction<br />-   Alert<br />-   Weather<br /><br /> **Example**: Accident|  
|Severity|Edm.String|The level of importance of incident specified by one of the following values.<br /><br /> -   LowImpact<br />-   Minor<br />-   Moderate<br />-   Serious<br /><br /> **Example**: Minor|  
|Verified|Edm.Boolean|A value of true indicates that the incident has been visually verified or otherwise officially confirmed by a source like the local police department.<br /><br /> **Example**: true|  
|RoadClosed|Edm.Boolean|A value of true indicates that there is a road closure.<br /><br /> **Example**: false|  
|Description|Edm.String|A description of the incident.<br /><br /> **Examples:**<br /><br /> -   W 95th St between Switzer Rd and Bluejacket Dr - construction<br />-   WB Johnson Dr at I-435 - bridge repair|  
|DetourInfo|Edm.String|A description of a detour.<br /><br /> **Examples**:<br /><br /> -   Take 63rd St to Roe Ave and head south to 67th St<br />-   take US-40 to Blue Ridge Cut-Off|  
|LaneInfo|Edm.String|A description specific to lanes, such as lane closures.<br /><br /> **Examples**:<br /><br /> -   All lanes blocked<br />-   Left lane blocked|  
|CongestionInfo|Edm.String|A description of the congestion.<br /><br /> **Examples**:<br /><br /> -   generally slow<br />-   sluggish|  
|ToPointLatitude|Edm.Double|The latitude of the point that specifies the end of a traffic incident, such as the end of a construction zone.<br /><br /> **Example**: 38.65831|  
|ToPointLongitude|Edm.Double|The longitude of the point that specifies the end of a traffic incident, such as the end of a construction zone.<br /><br /> **Example**: -94.36706|  
  
## How to query the TrafficIncidents data source  
 You can query the TrafficIncidents data source by using the following base URL and specifying an area to search by using the [Query by Area](../query-api/query-by-area.md) API or the [Query Near a Route](../query-api/query-near-route.md) API.  
  
 **Base Query URL**  
  
```url
http://spatial.virtualearth.net/REST/v1/data/8F77935E46704C718E45F52D0D5550A6/TrafficIncidents/TrafficIncident  
```  
  
 **Query Example**  
  
 The following query example queries for traffic incidents along a route from Houston, Texas to Galveston, Texas by using the [Query Near a Route](../query-api/query-near-route.md) API. The query key you use can be any Bing Maps Key.  
  
```url
http://spatial.virtualearth.net/REST/v1/data/8F77935E46704C718E45F52D0D5550A6/TrafficIncidents/TrafficIncident?spatialFilter=nearRoute('Houston,TX','Galveston,Tx')&key=anyBingMapsKey  
```  
  
 **XML Response**  
  
 This request returns traffic incident information in the following format.  
  
```xml
<?xml version="1.0" encoding="utf-8"?>  
<feed xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://www.w3.org/2005/Atom">  
  <title type="text"></title>  
  <id>uuid:e767cc8a-6932-4ec1-9b78-d2c36aa81989;id=45353</id>  
  <rights type="text">© 2012 Microsoft and its suppliers.  This API and any results cannot be used or accessed without Microsoft's express written permission.</rights>  
  <updated>2012-02-01T19:08:15Z</updated>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/8f77935e46704c718e45f52d0d5550a6/TrafficIncidents/TrafficIncident('277303858')</id>  
    <title type="text"></title>  
    <updated>2012-02-01T19:08:15Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:IncidentId>277303858</d:IncidentId>  
        <d:Latitude m:type="Edm.Double">29.378040</d:Latitude>  
        <d:Longitude m:type="Edm.Double">-95.020810</d:Longitude>  
        <d:LastModifiedUTC>2012-01-25T14:29:02.01Z</d:LastModifiedUTC>  
        <d:StartTimeUTC>2011-10-17T12:00:00Z</d:StartTimeUTC>  
        <d:EndTimeUTC>2012-02-12T14:00:00Z</d:EndTimeUTC>  
        <d:Type>Construction</d:Type>  
        <d:Severity>Minor</d:Severity>  
        <d:Verified>true</d:Verified>  
        <d:RoadClosed>true</d:RoadClosed>  
        <d:Description>FM-1765 is closed in both directions between Delaney Rd to FM-2004 - construction</d:Description>  
        <d:DetourInfo>follow the posted signage</d:DetourInfo>  
        <d:LaneInfo></d:LaneInfo>  
        <d:CongestionInfo></d:CongestionInfo>  
        <d:ToPointLatitude m:type="Edm.Double">0</d:ToPointLatitude>  
        <d:ToPointLongitude m:type="Edm.Double">0</d:ToPointLongitude>  
        <d:LocationCodes></d:LocationCodes>  
      </m:properties>  
    </content>  
  </entry>  
  <entry>  
    <id>https://spatial.virtualearth.net/REST/v1/data/8f77935e46704c718e45f52d0d5550a6/TrafficIncidents/TrafficIncident('277303880')</id>  
    <title type="text"></title>  
    <updated>2012-02-01T19:08:15Z</updated>  
    <content type="application/xml">  
      <m:properties>  
        <d:IncidentId>277303880</d:IncidentId>  
        <d:Latitude m:type="Edm.Double">29.769700</d:Latitude>  
        <d:Longitude m:type="Edm.Double">-95.358560</d:Longitude>  
        <d:LastModifiedUTC>2012-01-25T14:29:02.01Z</d:LastModifiedUTC>  
        <d:StartTimeUTC>2011-08-08T11:54:00Z</d:StartTimeUTC>  
        <d:EndTimeUTC>2012-10-01T22:00:00Z</d:EndTimeUTC>  
        <d:Type>Construction</d:Type>  
        <d:Severity>Minor</d:Severity>  
        <d:Verified>true</d:Verified>  
        <d:RoadClosed>true</d:RoadClosed>  
        <d:Description>N Main St is closed in both directions between Naylor St and Franklin St - construction</d:Description>  
        <d:DetourInfo>Follow posted signage</d:DetourInfo>  
        <d:LaneInfo></d:LaneInfo>  
        <d:CongestionInfo></d:CongestionInfo>  
        <d:ToPointLatitude m:type="Edm.Double">0</d:ToPointLatitude>  
        <d:ToPointLongitude m:type="Edm.Double">0</d:ToPointLongitude>  
        <d:LocationCodes></d:LocationCodes>  
      </m:properties>  
    </content>  
  </entry>  
</feed>  
  
```  
  
 **JSON Response**  
  
 When you specify $format=json in the URL, the response returns traffic incident information in the following JSON format.  
  
```json
{  
   "d":{  
      "__copyright":"\u00a9 2012 Microsoft and its suppliers.  This API and any results cannot be used or accessed without Microsoft's express written permission.",  
      "results":[  
         {  
            "__metadata":{  
               "uri":"https:\/\/spatial.virtualearth.net\/REST\/v1\/data\/8f77935e46704c718e45f52d0d5550a6\/TrafficIncidents\/TrafficIncident('277303858')"  
            },  
            "IncidentId":"277303858",  
            "Latitude":29.378040,  
            "Longitude":-95.020810,  
            "LastModifiedUTC":"2012-01-25T14:29:02.01Z",  
            "StartTimeUTC":"2011-10-17T12:00:00Z",  
            "EndTimeUTC":"2012-02-12T14:00:00Z",  
            "Type":"Construction",  
            "Severity":"Minor",  
            "Verified":"true",  
            "RoadClosed":"true",  
            "Description":"FM-1765 is closed in both directions between Delaney Rd to FM-2004 - construction",  
            "DetourInfo":"follow the posted signage",  
            "LaneInfo":"",  
            "CongestionInfo":"",  
            "ToPointLatitude":0,  
            "ToPointLongitude":0,  
            "LocationCodes":""  
         },  
         {  
            "__metadata":{  
               "uri":"https:\/\/spatial.virtualearth.net\/REST\/v1\/data\/8f77935e46704c718e45f52d0d5550a6\/TrafficIncidents\/TrafficIncident('277303880')"  
            },  
            "IncidentId":"277303880",  
            "Latitude":29.769700,  
            "Longitude":-95.358560,  
            "LastModifiedUTC":"2012-01-25T14:29:02.01Z",  
            "StartTimeUTC":"2011-08-08T11:54:00Z",  
            "EndTimeUTC":"2012-10-01T22:00:00Z",  
            "Type":"Construction",  
            "Severity":"Minor",  
            "Verified":"true",  
            "RoadClosed":"true",  
            "Description":"N Main St is closed in both directions between Naylor St and Franklin St - construction",  
            "DetourInfo":"Follow posted signage",  
            "LaneInfo":"",  
            "CongestionInfo":"",  
            "ToPointLatitude":0,  
            "ToPointLongitude":0,  
            "LocationCodes":""  
         }  
      ]  
   }  
}  
```