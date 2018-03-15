---
title: "Traffic Incident Data | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: f04e3fe7-8308-4d64-8180-455780d8376e
caps.latest.revision: 21
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Traffic Incident Data
The response returned by a Traffic URL contains one or more TrafficIncident resources. Each TrafficIncident resource contains information about a traffic issues that met the criteria specified in the URL request, such as map area, incident type and severity. This following table provides descriptions of the TrafficIncident resource fields and is followed by JSON and XML examples.  
  
## Traffic Incident Resource  
 The following table describes the fields in the traffic incident resource. One or more traffic incident resources are returned when you request traffic data. These resources are inside a common response wrapper for the Bing Maps REST Services.  For more information about the common response wrapper, see [Common Response Description](../rest-services/common-response-description.md).  
  
 Fields marked **Required** are always provided for each traffic incident. Other fields are optional and not always included.  
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|point|Point|Point|**Required.** The latitude and longitude coordinates where you encounter the incident.|  
|congestion|CongestionInfo|string|A description of the congestion.<br /><br /> Examples:<br /><br /> -   generally slow<br />-   sluggish|  
|description|Description|string|A description of the incident.<br /><br /> Examples:<br /><br /> -   W 95th St between Switzer Rd and Bluejacket Dr - construction<br />-   WB Johnson Dr at I-435 - bridge repair|  
|detour|detourInfo|string|A description of a detour.<br /><br /> Examples:<br /><br /> -   Take 63rd St to Roe Ave and head south to 67th St<br />-   take US-40 to Blue Ridge Cut-Off|  
|start|StartTimeUTC|UTC Time|**Required.** The time the incident occurred. For more information about the format, see the **About Time Values** section below.<br /><br /> Examples:<br /><br /> -   JSON: Date(1295704800000)<br />-   XML: 2011-06-29T23:44:56.593Z|  
|end|EndTimeUTC|UTC Time|**Required.** The time that the traffic incident will end. For more information about the format, see the **About Time Values** section below.<br /><br /> Examples:<br /><br /> -   JSON: Date(1295704800000)<br />-   XML: 2011-06-29T23:44:56.593Z|  
|incidentId|IncidentId|long|**Required.** A unique ID for the incident.|  
|lane|LaneInfo|string|A description specific to lanes, such as lane closures.<br /><br /> Examples:<br /><br /> -   All lanes blocked<br />-   Left lane blocked|  
|lastModified|LastModifiedUTC|DateTime|**Required.** The time the incident information was last updated. For more information about the format, see the **About Time Values** section below.<br /><br /> Examples:<br /><br /> -   JSON: Date(1295704800000)<br />-   XML: 2011-06-29T23:44:56.593Z|  
|roadClosed|RoadClosed|Boolean|**Required.** A value of `true` indicates that there is a road closure.|  
|severity|Severity|integer|**Required.** Specifies the level of importance of incident.<br /><br /> -   1: LowImpact<br />-   2: Minor<br />-   3: Moderate<br />-   4: Serious|  
|toPoint|ToPoint|Point|The coordinates of the end of a traffic incident, such as the end of a construction zone.|  
|locationCodes|LocationCodes|string collection|A collection of traffic location codes. This field is provided when you set the includeLocationCodes parameter to true in the request. These codes associate an incident with pre-defined road segments. A subscription is typically required to be able to interpret these codes for a geographical area or country.|  
|type|Type|integer|**Required.** Specifies the type of incident.<br /><br /> -   1: Accident<br />-   2: Congestion<br />-   3: DisabledVehicle<br />-   4: MassTransit<br />-   5: Miscellaneous<br />-   6: OtherNews<br />-   7: PlannedEvent<br />-   8: RoadHazard<br />-   9: Construction<br />-   10: Alert<br />-   11: Weather|  
|verified|Verified|Boolean|**Required.** A value of `true` indicates that the incident has been visually verified or otherwise officially confirmed by a source like the local police department.|  
  
### About time values  
 Time values in the TrafficIncident resource data use UTC time. The format for XML and JSON responses are different.  
  
 For JSON responses, the time is specified as UTC time in milliseconds using the epoch (start time) of January 1, 1970, 00:00:00.  The JSON field uses the following format.  
  
```  
Date(milliseconds)  
```  
  
 JSON Example: Date(1295704800000)  
  
 For XML responses, the time is specified as UTC time and uses the following format. A time zone offset is not specified.  
  
```  
YYYY-MM-DDThh:mm:ss.sZ  
```  
  
 XML Example: 2011-06-29T23:44:56.593Z  
  
 For more information about UTC time see [W3C Date and Time Formats](http://www.w3.org/TR/NOTE-datetime).  
  
## Examples  
 The following are TrafficIncident Data resource examples. To see the complete response including the common response container, see the examples in [Get Traffic Incidents](../rest-services/get-traffic-incidents.md) and the [Common Response Description](../rest-services/common-response-description.md).  
  
### JSON Example  
  
```  
{  
   "__type":"TrafficIncident:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
   "point":{  
      "type":"Point",  
      "coordinates":[  
         38.64829,  
         -94.36405  
      ]  
   },  
   "congestion":"",  
   "description":"in both directions between MO-2\/MO-7 and MO-291\/Cantrell Rd - construction",  
   "detour":"",  
   "end":"\/Date(1316217600000)\/",  
   "incidentId":214828828,  
   "lane":"Total Lanes lane blocked",  
   "lastModified":"\/Date(1310385750290)\/",  
   "roadClosed":false,  
   "severity":2,  
   "start":"\/Date(1310126400000)\/",  
   "toPoint":{  
      "type":"Point",  
      "coordinates":[  
         38.65831,  
         -94.36706  
      ]  
   },  
   "locationCodes":[  
      "119+05041",  
      "119+05042",  
      "119-05041",  
      "119-05042",  
      "119N05041",  
      "119N05042",  
      "119P05041",  
      "119P05042"  
   ],  
   "type":9,  
   "verified":true  
}  
```  
  
### XML Example  
  
```  
<TrafficIncident>  
  <Point>  
    <Latitude>38.64829</Latitude>  
    <Longitude>-94.36405</Longitude>  
  </Point>  
  <IncidentId>214828828</IncidentId>  
  <LastModifiedUTC>2011-07-11T12:02:30.29Z</LastModifiedUTC>  
  <StartTimeUTC>2011-07-08T12:00:00Z</StartTimeUTC>  
  <EndTimeUTC>2011-09-17T00:00:00Z</EndTimeUTC>  
  <Type>Construction</Type>  
  <Severity>Minor</Severity>  
  <Verified>true</Verified>  
  <RoadClosed>false</RoadClosed>  
  <Description>in both directions between MO-2/MO-7 and MO-291/Cantrell Rd - construction</Description>  
  <DetourInfo/>  
  <LaneInfo>Total Lanes lane blocked</LaneInfo>  
  <CongestionInfo/>  
  <ToPoint>  
    <Latitude>38.65831</Latitude>  
    <Longitude>-94.36706</Longitude>  
  </ToPoint>  
  <LocationCodes>  
    <string>119+05041</string>  
    <string>119+05042</string>  
    <string>119-05041</string>  
    <string>119-05042</string>  
    <string>119N05041</string>  
    <string>119N05042</string>  
    <string>119P05041</string>  
    <string>119P05042</string>  
  </LocationCodes>  
</TrafficIncident>  
  
```