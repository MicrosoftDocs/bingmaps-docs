---
title: "Get Traffic Incidents | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 2d23ea4d-48d1-4760-a072-436c00b3658d
caps.latest.revision: 19
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Get Traffic Incidents

Use the following URL template to request traffic incident information. A collection of traffic incidents is returned in the response.  
  
 For more information about the traffic incident data that is returned in the response, see [Traffic Incident Data](traffic-incident-data.md). You can also view the example URL and response values in the [Examples](#examples) section below. For an overview of how traffic incident information is returned by Bing Maps REST Services, see [Getting Traffic Incident Data](getting-traffic-incident-data.md).  
  
 For traffic coverage by country, see [Bing Maps Traffic Coverage](/bing-maps-docs/coverage/bing-maps-traffic-coverage.md).  
  
## Supported HTTP Methods

GET

## URL Templates  
  
[!INCLUDE [get-bing-map-key-note](../../includes/get-bing-map-key-note.md)]
  
 **Get traffic incidents.**  
  
```  
http://dev.virtualearth.net/REST/v1/Traffic/Incidents/{mapArea}/{includeLocationCodes}?severity={severity1,severity2,severityN}&type={type1,type2,typeN}&key={BingMapsKey}  
```  
  
### Template Parameters  
  
> [!NOTE]
>  See the [Common Parameters and Types](../services/common-parameters-and-types.md) section for additional common parameters to use with these URLs.  
>   
>  Common parameters include:  
>   
>  -   [Output Parameters](../services/output-parameters.md): Includes response output types and the JSON callback parameters.  
> -   [Culture Parameter](../services/culture-parameter.md): Includes a list of the supported cultures.  
>   
>  When an alias is provided, you can use the alias to shorten the length of the query parameter. For example, severity=6,9 can be shortened to s=6,9.  
>   
>  Parameter values are not case-sensitive.  
  
|Parameter|Alias|Description|Values|  
|---------------|-----------|-----------------|------------|  
|mapArea||**Required.** Specifies the area to search for traffic incident information.|A rectangular area specified as a bounding box. The size of the area can be a maximum of 500 km x 500 km.<br /><br /> A bounding box defines an area by specifying SouthLatitude, WestLongitude, NorthLatitude, and EastLongitude values. For more information, see [Location and Area Types](../services/location-and-area-types.md).<br /><br /> **Example**: 45.219,-122.325,47.610,-122.107|  
|includeLocationCodes||**Optional.** Specifies whether to include traffic location codes in the response. Traffic location codes provide traffic incident information for pre-defined road segments. A subscription is typically required to be able to interpret these codes for a geographical area or country.|One of the following values:<br /><br /> -   true<br />-   false **[default]**<br /><br /> If you want to use the default value, you can omit this parameter from the URL request.|  
|severity|s|**Optional.** Specifies severity level of traffic incidents to return.|One or more of the following integer values:<br /><br /> -   1: LowImpact<br />-   2: Minor<br />-   3: Moderate<br />-   4: Serious<br /><br /> The default is to return traffic incidents for all severity levels.<br /><br /> **Examples**:<br /><br /> severity=2,3,4<br /><br /> s=2,3,4|  
|type|t|**Optional.** Specifies the type of traffic incidents to return.|One or more of the following integer values:<br /><br /> -   1: Accident<br />-   2: Congestion<br />-   3: DisabledVehicle<br />-   4: MassTransit<br />-   5: Miscellaneous<br />-   6: OtherNews<br />-   7: PlannedEvent<br />-   8: RoadHazard<br />-   9: Construction<br />-   10: Alert<br />-   11: Weather<br /><br /> **Examples**:<br /><br /> type=2<br /><br /> t=2,9|  
  
## Response  
 A collection of TrafficIncident resources is returned when you make a request with the URL above. For more information about the TrafficIncident resource, see [Traffic Incident Data](../services/traffic-incident-data.md). For more information about the common response syntax for the Bing Maps REST Services, see [Common Response Description](../services/common-response-description.md).  
  
 These URLs support JSON (application/json) and XML (application/xml) response formats. A JSON response is provided by default, unless you request XML output by setting the output (o) parameter. For more information, see [Output Parameters](../services/output-parameters.md).  
  
 JSON and XML responses are provided for the URL examples in the following section.  
  
## Examples  
 **Get all traffic incidents in a specified area.**  
  
 The following example shows how to request all traffic incident for an area defined as a bounding box (South Latitude, West Longitude, North Latitude, East Longitude). For more information about defining a bounding box, see [Location and Area Types](../services/location-and-area-types.md). Note that the includeLocationCodes parameter is not specified in this example.  
  
```  
  
http://dev.virtualearth.net/REST/v1/Traffic/Incidents/37,-105,45,-94?key=YourBingMapsKey  
```  
  
 **JSON Response**  
  
 This URL returns a response with the following format that includes a list of traffic incidents as traffic incident resources. For more information on the fields returned for a traffic incident resource, see [Traffic Incident Data](../services/traffic-incident-data.md).  
  
```  
{  
   "authenticationResultCode":"ValidCredentials",  
   "brandLogoUri":"http:\/\/dev.virtualearth.net\/Branding\/logo_powered_by.png",  
   "copyright":"Copyright © 2011 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
   "resourceSets":[  
      {  
         "estimatedTotal":131,  
         "resources":[  
            {  
               "__type":"TrafficIncident:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "point":{  
                  "type":"Point",  
                  "coordinates":[  
                     38.85135,  
                     -94.34033  
                  ]  
               },  
               "congestion":"",  
               "description":"MO-150 is closed between 5th Ave S and Court Dr - construction",  
               "detour":"",  
               "end":"\/Date(1310396400000)\/",  
               "incidentId":210546697,  
               "lane":"",  
               "lastModified":"\/Date(1309391096593)\/",  
               "roadClosed":true,  
               "severity":3,  
               "start":"\/Date(1307365200000)\/",  
               "type":9,  
               "verified":true  
            },  
            {  
               "__type":"TrafficIncident:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "point":{  
                  "type":"Point",  
                  "coordinates":[  
                     38.85872,  
                     -94.54638  
                  ]  
               },  
               "congestion":"",  
               "description":"Botts Rd is closed between Andrews Rd and 142nd St - construction",  
               "detour":"To go north take US-71 NB to 140th St and go west on 140th St to access Botts Rd- To go south continue west on MO-150 to Thunderbird Rd to 149th St",  
               "end":"\/Date(1315244760000)\/",  
               "incidentId":191097424,  
               "lane":"",  
               "lastModified":"\/Date(1309391096593)\/",  
               "roadClosed":true,  
               "severity":1,  
               "start":"\/Date(1295704800000)\/",  
               "type":9,  
               "verified":true  
            }  
         ]  
      }  
   ],  
   "statusCode":200,  
   "statusDescription":"OK",  
   "traceId":"38491198bf6a42f5b7e60c18aa08ec02"  
}  
```  
  
 **XML Response**  
  
 If the output parameter is specified and set to xml (o=xml) in this URL, the URL returns a response with the following format.  
  
```  
<Response xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
  <Copyright>Copyright © 2011 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>  
  <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>c0f1945558bf49ceb0b35816d5bca10</TraceId>  
  <ResourceSets>  
     <<ResourceSet>  
      <EstimatedTotal>128</EstimatedTotal  
      <Resources>  
        <TrafficIncident>  
          <Point>  
            <Latitude>38.85135</Latitude>  
            <Longitude>-94.34033</Longitude>  
          </Point>  
          <IncidentId>210546697</IncidentId>  
          <LastModifiedUTC>2011-06-29T23:44:56.593Z</LastModifiedUTC>  
          <StartTimeUTC>2011-06-06T13:00:00Z</StartTimeUTC>  
          <EndTimeUTC>2011-07-11T15:00:00Z</EndTimeUTC>  
          <Type>Construction</Type>  
          <Severity>Moderate</Severity>  
          <Verified>true</Verified>  
          <RoadClosed>true</RoadClosed>  
          <Description>MO-150 is closed between 5th Ave S and Court Dr - construction</Description>  
          <DetourInfo/>  
          <LaneInfo/>  
          <CongestionInfo/>  
        </TrafficIncident>  
        <TrafficIncident>  
          <Point>  
            <Latitude>38.85872</Latitude>  
            <Longitude>-94.54638</Longitude>  
          </Point>  
          <IncidentId>191097424</IncidentId>  
          <LastModifiedUTC>2011-06-29T23:44:56.593Z</LastModifiedUTC>  
          <StartTimeUTC>2011-01-22T14:00:00Z</StartTimeUTC>  
          <EndTimeUTC>2011-09-05T17:46:00Z</EndTimeUTC>  
          <Type>Construction</Type>  
          <Severity>LowImpact</Severity>  
          <Verified>true</Verified>  
          <RoadClosed>true</RoadClosed>  
          <Description>Botts Rd is closed between Andrews Rd and 142nd St - construction</Description>  
          <DetourInfo>To go north take US-71 NB to 140th St and go west on 140th St to access Botts Rd- To go south continue west on MO-150 to Thunderbird Rd to 149th St</DetourInfo>  
          <LaneInfo/>  
          <CongestionInfo/>  
        </TrafficIncident>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
  
```  
  
 **Get traffic incidents by type and severity and request traffic location codes.**  
  
 The following example queries for congestion type traffic incidents (t=9) that are minor or moderate in severity (s=2,3) and that occur in the bounding box defined by the coordinates (37.0,-105.45,45.0,-94.0). Traffic location codes are requested by setting the includeLocationCodes value 'true' in the URL. The requested output format is XML.  
  
```  
http://dev.virtualearth.net/REST/V1/Traffic/Incidents/37,-105,45,-94/true?t=9,2&s=2,3&o=xml&key=BingMapsKey  
```  
  
 **XML Response**  
  
 This URL returns an XML response with the following format.  
  
```  
<Response xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
  <Copyright>Copyright © 2011 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>  
  <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>3f09332c6ed44048bf8e9e19198fd154</TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>91</EstimatedTotal>-<Resources>  
        <TrafficIncident>  
          <Point>  
            <Latitude>38.64829</Latitude>  
            <Longitude>-94.36405</Longitude>  
          </Point><IncidentId>214828828</IncidentId>  
          <LastModifiedUTC>2011-07-11T12:02:30.29Z</LastModifiedUTC>  
          <StartTimeUTC>2011-07-08T12:00:00Z</StartTimeUTC>  
          <EndTimeUTC>2011-09-17T00:00:00Z</EndTimeUTC>  
          <Type>Construction</Type><Severity>Minor</Severity>  
          <Verified>true</Verified><RoadClosed>false</RoadClosed>  
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
        <TrafficIncident>  
          <Point>  
            <Latitude>38.80371</Latitude>  
            <Longitude>-94.43887</Longitude>  
          </Point>  
          <IncidentId>213728243</IncidentId>  
          <LastModifiedUTC>2011-07-11T12:02:30.29Z</LastModifiedUTC>  
          <StartTimeUTC>2011-06-22T12:00:00Z</StartTimeUTC>  
          <EndTimeUTC>2011-07-31T22:00:00Z</EndTimeUTC>  
          <Type>Construction</Type>  
          <Severity>Minor</Severity>  
          <Verified>true</Verified>  
          <RoadClosed>false</RoadClosed>  
          <Description>SB MO-J between MO-58 and US-71 - construction</Description>  
          <DetourInfo/>  
          <LaneInfo>Total Lanes lane blocked</LaneInfo>  
          <CongestionInfo/>  
        </TrafficIncident>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
```  
  
 **JSON Response**  
  
 If the output parameter was not specified in this URL, a JSON response with the following format is returned.  
  
```  
{  
   "authenticationResultCode":"ValidCredentials",  
   "brandLogoUri":"http:\/\/dev.virtualearth.net\/Branding\/logo_powered_by.png",  
   "copyright":"Copyright © 2011 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
   "resourceSets":[  
      {  
         "estimatedTotal":91,  
         "resources":[  
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
            },  
            {  
               "__type":"TrafficIncident:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "point":{  
                  "type":"Point",  
                  "coordinates":[  
                     38.80371,  
                     -94.43887  
                  ]  
               },  
               "congestion":"",  
               "description":"SB MO-J between MO-58 and US-71 - construction",  
               "detour":"",  
               "end":"\/Date(1312149600000)\/",  
               "incidentId":213728243,  
               "lane":"Total Lanes lane blocked",  
               "lastModified":"\/Date(1310385750290)\/",  
               "roadClosed":false,  
               "severity":2,  
               "start":"\/Date(1308744000000)\/",  
               "type":9,  
               "verified":true  
            }  
         ]  
      }  
   ],  
   "statusCode":200,  
   "statusDescription":"OK",  
   "traceId":"9c2944a197db4457bb8d4def0007b657"  
}  
```  
  
## HTTP Status Codes  
  
[!INCLUDE [get-status-code-note](../../includes/get-status-code-note.md)]
  
 When the request is successful, the following HTTP status code is returned.  
  
-   200  
  
 When the request is not successful, the response returns one of the following errors.  
  
-   400  
  
-   401  
  
-   404  
  
-   500  
  
-   503  
  
## See Also  
 [Using the REST Services with .NET](../using-the-rest-services-with-net.md) 
 [JSON Data Contracts](../json-data-contracts.md)
