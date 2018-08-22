---
title: "Calculate Routes from Major Roads | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: e84b8799-28f7-4976-b098-da91b75e6b16
caps.latest.revision: 22
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Calculate Routes from Major Roads

Use the following URL template to return a driving route to a location from major roads in four directions (West, North, East and South). You can use this URL for routes in the United States, Canada and Mexico.  
  
When you make a request using the following URL template, the response can return either only the starting points for the routes from major roads or detailed information for each route. Starting points are latitude and longitude pairs while detailed route information includes detailed directions and waypoints, travel time and duration and other information specific to the route. Specify the `exclude` parameter when you do not want to return detailed route information.  
  
Starting points are specified in the response by using the Location Resource. Detailed route information is provided by using the Route Resource. You can also request a route path that additionally returns a series of latitude and longitude points that define the route. For information about the Location Resource, see [Location Data](../locaitons/location-data.md). For information about the Route Resource, see [Route Data](route-data.md). Examples are also provided below.  
  
 When you use this URL, an attempt is made to create four driving routes to the specified location. Ideally these routes are from the west, north, east and south directions. However, major routes may not exist in each direction. If routes from all four directions cannot be found, the response may contain more than one route from the same direction or fewer than four routes may be returned.  
  
 For more information about the Route resource, see [Route Data](route-data.md). You can also view the example URL and response values in the Examples section.  
  
## URL Templates  
  
> [!NOTE]
>  These templates support both HTTP and HTTPS protocols.  
  
 **Find routes from major roads in four directions (West, North, East, South).**  
  
```url
http://dev.virtualearth.net/REST/v1/Routes/FromMajorRoads?destination={destination}&exclude=routes&routePathOutput={routePathOutput}&distanceUnit={distanceUnit}&key={BingMapsKey}
```  
  
### Template Parameters  
  
> [!NOTE]
>  See the [Common Parameters and Types]../common-parameters-and-types/index.md) section for additional common parameters to use with these URLs.  
>   
>  Common parameters include:  
>   
>  -   [Output Parameters](../common-parameters-and-types/output-parameters.md): Includes response output types and the JSON callback parameters.  
> -   [Culture Parameter]../common-parameters-and-types/culture-parameter.md): Includes a list of the supported cultures.  
> -   [User Context Parameters](../common-parameters-and-types/user-context-parameters.md): Includes parameters that set user location and viewport values to help determine locations. For example, these values may help prioritize a set of possible locations when you specify a partial address for a destination.  
>   
>  When an alias is provided, you can use the alias to shorten the length of the query parameter. For example, destination=47.610,-122.107 can be shortened to dest=47.610,-122.107.  
>   
>  Parameter values are not case-sensitive.  
  
|Parameter|Alias|Description|Values|  
|---------------|-----------|-----------------|------------|  
|destination|dest|**Required.** Specifies the final location for all the routes.|A destination can be specified as a Point, a landmark, or an address. For more information about Point values, see [Location and Area Types](../common-parameters-and-types/location-and-area-types.md).<br /><br /> **Examples**:<br /><br /> destination=47.610,-122.107 [Point]<br /><br /> destination=Eiffel%20Tower [landmark]<br /><br /> dest=1%20Microsoft%20Way%20Redmond%20WA [address]|  
|exclude|excl|**Optional.** Specifies to return only starting points for each major route in the response. When this option is not specified, detailed directions for each route are returned.|The only value for this parameter is routes.<br /><br /> **Examples**:<br /><br /> exclude=routes<br /><br /> excl=routes|  
|routeAttributes|ra|**Optional.** Specify to include or exclude parts of the routes response.|One or more of the following values:<br /><br /> -   **excludeItinerary**: Do not include detailed directions in the response. Detailed directions are provided as itinerary items and contain details such as written instructions and traffic location codes.<br />-   **routePath**: Include a set of point (latitude and longitude) values that describe the route’s path in the response.<br /><br /> **Note**: When you set the routeAttributes parameter, the routePathOutput parameter is ignored.|  
|routePathOutput|rpo|**Optional.**  Specifies whether the response should include information about Point (latitude and longitude) values for each route’s path. **Note:**  When the exclude parameter is specified, the routePathOutput parameter is not used.|One of the following values:<br /><br /> -   Points: A list of Point values for each route’s path is provided in the response.<br />-   None **[default]**: No route path information is provided in the response.<br /><br /> **Example**: routePathOutput=Points|  
|distanceUnit|du|**Optional.** The units to use for distance. **Note:**  When the exclude parameter is specified, the distanceUnit parameter is not used.|One of the following values:<br /><br /> -   Mile or mi<br />-   Kilometer or km **[default]**<br /><br /> **Example**: distanceUnit=mi|  
  
## Response
 
A set of Route resources that contain route information from major roads is returned when you make a request using this template and do not specify the `exclude=routes` parameter value. If you specify the `exclude=routes`, a set of Location resources are returned that contain starting points (latitude and longitude values) for routes to your destination from major roads. For more information about the Route resource, see [Route Data](route-data.md). For more information about the Locations resource, see [Location Data](../locations/location-data.md). For more information about the common response syntax for the Bing Maps REST Services, see [Common Response Description](../common-response-description.md). JSON and XML responses are provided for the URL examples in the following section.  
  
 These URLs support JSON (application/json) and XML (application/xml) response formats. A JSON response is provided by default, unless you request XML output by setting the output (o) parameter. For more information, see [Output Parameters](../common-parameters-and-types/output-parameters.md).  
  
## Examples

**Find starting points of the driving routes from major roads to a street address.**  
  
 This example returns starting points for routes from major roads for the specified street address. The `exclude=routes` parameter is specified so that only the starting points of the major routes are returned. If you do not include this parameter, detailed route instructions are also provided in the response.  
  
```url
http://dev.virtualearth.net/REST/V1/Routes/FromMajorRoads?dest=1%20Microsoft%20Way%20Redmond%20WA%2098052&exclude=routes&output=xml&key=BingMapsKey  
```  
  
 **XML response**  
  
 The response for this example contains a set of Location resources that specify the starting points of the major routes. The `Name` field defines the route that corresponds with the starting location. For example, the first `Name` value below specifies that this is the starting point of a route from the north and uses Interstate I-405 South.  
  
```xml
<Response xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>Copyright © 2010 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>  
  <BrandLogoUri>http://veintplat3.live-int.com/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>d9c83b7e348e41c0b93255e36cb944f3</TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>4</EstimatedTotal>  
      <Resources>  
        <Location>  
          <Name>the north (on I-405 S)</Name>  
          <Point>  
            <Latitude>47.684789299964905</Latitude>  
            <Longitude>-122.18332171440125</Longitude>  
          </Point>  
          <Confidence>High</Confidence>  
        </Location>  
        <Location>  
          <Name>the south (on I-405 N)</Name>  
          <Point>  
            <Latitude>47.615979909896851</Latitude>  
            <Longitude>-122.18860030174255</Longitude>  
          </Point>  
          <Confidence>High</Confidence>  
        </Location>  
        <Location>  
          <Name>the east (on SR-520 W)</Name>  
          <Point>  
            <Latitude>47.671131491661072</Latitude>  
            <Longitude>-122.10670173168182</Longitude>  
          </Point>  
          <Confidence>High</Confidence>  
        </Location>  
        <Location>  
          <Name>the west (on SR-520 E)</Name>  
          <Point>  
            <Latitude>47.636691927909851</Latitude>  
            <Longitude>-122.19275772571564</Longitude>  
          </Point>  
          <Confidence>High</Confidence>  
        </Location>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
  
```  
  
 **JSON Response**  
  
 You would receive the following JSON response if the output=xml parameter was not set in this example.  
  
```json
{  
   "authenticationResultCode":"ValidCredentials",  
   "brandLogoUri":"http:\/\/dev.virtualearth.net\/Branding\/logo_powered_by.png",  
   "copyright":"Copyright © 2010 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
   "resourceSets":[  
      {  
         "estimatedTotal":4,  
         "resources":[  
            {  
               "__type":"Location:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "name":"the north (on I-405 S)",  
               "point":{  
                  "type":"Point",  
                  "coordinates":[  
                     47.684789299964905,  
                     -122.18332171440125  
                  ]  
               },  
               "confidence":"High",  
               "entityType":null  
            },  
            {  
               "__type":"Location:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "name":"the south (on I-405 N)",  
               "point":{  
                  "type":"Point",  
                  "coordinates":[  
                     47.615979909896851,  
                     -122.18860030174255  
                  ]  
               },  
               "confidence":"High",  
               "entityType":null  
            },  
            {  
               "__type":"Location:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "name":"the east (on SR-520 W)",  
               "point":{  
                  "type":"Point",  
                  "coordinates":[  
                     47.671131491661072,  
                     -122.10670173168182  
                  ]  
               },  
               "confidence":"High",  
               "entityType":null  
            },  
            {  
               "__type":"Location:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "name":"the west (on SR-520 E)",  
               "point":{  
                  "type":"Point",  
                  "coordinates":[  
                     47.636691927909851,  
                     -122.19275772571564  
                  ]  
               },  
               "confidence":"High",  
               "entityType":null  
            }  
         ]  
      }  
   ],  
   "statusCode":200,  
   "statusDescription":"OK",  
   "traceId":"e2bbc0171d224d85bbf5f41a91233b72"  
}  
```  
  
 **Find driving routes from major roads.**  
  
 This example returns routes to Spokane, Washington from major roads.  
  
```url
http://dev.virtualearth.net/REST/V1/Routes/FromMajorRoads?dest=Spokane%20WA&output=xml&key=BingMapsKey  
```  
  
 **XML response**  
  
 The response for this example contains a set of Route resources that provide directions for routes to Spokane, Washington from major roads.  
  
```xml
<Response xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>Copyright © 2010 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>  
  <BrandLogoUri>http://veintplat3.live-int.com/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>b081f10cb6194b54865e9eace7789385|BR1M006800</TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>4</EstimatedTotal>  
      <Resources>  
        <Route>  
          <Id>v60,i0,a0,cen-US,dAAAAAAAAAAA=,y0,s1,m0,o0,t0,woGQ8BOjrkPU=~kmIi/8mBtAAAAA4BAAAAAAA=~dGhlIGVhc3QgKG9uIEktOTAgVyk=~~~,wqXc8BOY3kPU=~kmIi/8ntswAAAA4BjKv/PgA=~U3Bva2FuZSwgV0E=~0~~,k1</Id>  
          <BoundingBox>  
            <SouthLatitude>47.65221118927002</SouthLatitude>  
            <WestLongitude>-117.41227939724922</WestLongitude>  
            <NorthLatitude>47.657259106636047</NorthLatitude>  
            <EastLongitude>-117.38137900829315</EastLongitude>  
          </BoundingBox>  
          <DistanceUnit>Kilometer</DistanceUnit>  
          <DurationUnit>Second</DurationUnit>  
          <TravelDistance>2.844</TravelDistance>  
          <TravelDuration>214</TravelDuration>  
          <RouteLeg>  
            <TravelDistance>2.844</TravelDistance>  
            <TravelDuration>214</TravelDuration>  
            <ActualStart>  
              <Latitude>47.653992176055908</Latitude>  
              <Longitude>-117.38137900829315</Longitude>  
            </ActualStart>  
            <ActualEnd>  
              <Latitude>47.657259106636047</Latitude>  
              <Longitude>-117.41227939724922</Longitude>  
            </ActualEnd>  
            <StartLocation>  
              <Name>the east (on I-90 W)</Name>  
              <Point>  
                <Latitude>47.653992176055908</Latitude>  
                <Longitude>-117.38137900829315</Longitude>  
              </Point>  
              <Confidence>High</Confidence>  
            </StartLocation>  
            <EndLocation>  
              <Name>Spokane, WA</Name>  
              <Point>  
                <Latitude>47.6572597771883</Latitude>  
                <Longitude>-117.41227939724922</Longitude>  
              </Point>  
              <Confidence>High</Confidence>  
            </EndLocation>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>1.866</TravelDistance>  
              <TravelDuration>67</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.653992176055908</Latitude>  
                <Longitude>-117.38137900829315</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="DepartStart">Depart I-90 West</Instruction>  
              <CompassDirection>west</CompassDirection>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>0.482</TravelDistance>  
              <TravelDuration>66</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.652361392974854</Latitude>  
                <Longitude>-117.40572810173035</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TakeRampRight">At exit 281, take ramp right for US-395 North / US-2 North toward Newport / Colville</Instruction>  
              <CompassDirection>west</CompassDirection>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>0.418</TravelDistance>  
              <TravelDuration>57</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.653520107269287</Latitude>  
                <Longitude>-117.41123735904694</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="BearRight">Bear right onto US-2 East / US-395 North / S Division St</Instruction>  
              <CompassDirection>north</CompassDirection>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>0.078</TravelDistance>  
              <TravelDuration>22</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.657259106636047</Latitude>  
                <Longitude>-117.41123735904694</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TurnLeft">Turn left onto W Sprague Ave</Instruction>  
              <CompassDirection>west</CompassDirection>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>0</TravelDistance>  
              <TravelDuration>0</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.657259106636047</Latitude>  
                <Longitude>-117.41227939724922</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="ArriveFinish">Arrive at Spokane, WA</Instruction>  
              <CompassDirection>west</CompassDirection>  
              <Hint hintType="PreviousIntersection">The last intersection is US-2 North / US-395 East / N Division St</Hint>  
              <Hint hintType="NextIntersection">If you reach US-2 South / US-395 West / N Browne St, you've gone too far</Hint>  
            </ItineraryItem>  
          </RouteLeg>  
        </Route>  
        <Route>  
          <Id>v60,i0,a0,cen-US,dAAAAAAAAAAA=,y0,s1,m0,o0,t0,wqNg8BHg+kPU=~kmIi/zEItAAAAA4BAAAAAAA=~dGhlIG5vcnRoIChvbiBVUy0yIFcgLyBVUy0zOTUgUyAvIE4gRGl2aXNpb24gU3Qp~~~,wqXc8BOY3kPU=~kmIi/8ntswAAAA4BjKv/PgA=~U3Bva2FuZSwgV0E=~0~~,k1</Id>  
          <BoundingBox>  
            <SouthLatitude>47.657259106636047</SouthLatitude>  
            <WestLongitude>-117.41332948207855</WestLongitude>  
            <NorthLatitude>47.6739102602005</NorthLatitude>  
            <EastLongitude>-117.41115152835846</EastLongitude>  
          </BoundingBox>  
          <DistanceUnit>Kilometer</DistanceUnit>  
          <DurationUnit>Second</DurationUnit>  
          <TravelDistance>2.032</TravelDistance>  
          <TravelDuration>199</TravelDuration>  
          <RouteLeg>  
            <TravelDistance>2.032</TravelDistance>  
            <TravelDuration>199</TravelDuration>  
            <ActualStart>  
              <Latitude>47.6739102602005</Latitude>  
              <Longitude>-117.41115152835846</Longitude>  
            </ActualStart>  
            <ActualEnd>  
              <Latitude>47.657259106636047</Latitude>  
              <Longitude>-117.41227939724922</Longitude>  
            </ActualEnd>  
            <StartLocation>  
              <Name>the north (on US-2 W / US-395 S / N Division St)</Name>  
              <Point>  
                <Latitude>47.6739102602005</Latitude>  
                <Longitude>-117.41115152835846</Longitude>  
              </Point>  
              <Confidence>High</Confidence>  
            </StartLocation>  
            <EndLocation>  
              <Name>Spokane, WA</Name>  
              <Point>  
                <Latitude>47.6572597771883</Latitude>  
                <Longitude>-117.41227939724922</Longitude>  
              </Point>  
              <Confidence>High</Confidence>  
            </EndLocation>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>1.954</TravelDistance>  
              <TravelDuration>176</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.6739102602005</Latitude>  
                <Longitude>-117.41115152835846</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="DepartStart">Depart US-2 West / US-395 South / N Division St toward W Augusta Ave</Instruction>  
              <CompassDirection>south</CompassDirection>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>0.078</TravelDistance>  
              <TravelDuration>22</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.657259106636047</Latitude>  
                <Longitude>-117.41331875324249</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TurnLeft">Turn left onto W Sprague Ave</Instruction>  
              <CompassDirection>east</CompassDirection>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>0</TravelDistance>  
              <TravelDuration>0</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.657259106636047</Latitude>  
                <Longitude>-117.41227939724922</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="ArriveFinish">Arrive at Spokane, WA</Instruction>  
              <CompassDirection>east</CompassDirection>  
              <Hint hintType="PreviousIntersection">The last intersection is US-2 South / US-395 West / N Browne St</Hint>  
              <Hint hintType="NextIntersection">If you reach US-2 North / US-395 East / N Division St, you've gone too far</Hint>  
            </ItineraryItem>  
          </RouteLeg>  
        </Route>  
        <Route>  
          <Id>v60,i0,a0,cen-US,dAAAAAAAAAAA=,y0,s1,m0,o0,t0,wCLc7BHCbj/U=~kmIi/8k0swAAAA4BAAAAAAA=~dGhlIHNvdXRoIChvbiBVUy0xOTUgTik=~~~,wqXc8BOY3kPU=~kmIi/8ntswAAAA4BjKv/PgA=~U3Bva2FuZSwgV0E=~0~~,k1</Id>  
          <BoundingBox>  
            <SouthLatitude>47.624192833900452</SouthLatitude>  
            <WestLongitude>-117.4500972032547</WestLongitude>  
            <NorthLatitude>47.657259106636047</NorthLatitude>  
            <EastLongitude>-117.41123735904694</EastLongitude>  
          </BoundingBox>  
          <DistanceUnit>Kilometer</DistanceUnit>  
          <DurationUnit>Second</DurationUnit>  
          <TravelDistance>6.357</TravelDistance>  
          <TravelDuration>352</TravelDuration>  
          <RouteLeg>  
            <TravelDistance>6.357</TravelDistance>  
            <TravelDuration>352</TravelDuration>  
            <ActualStart>  
              <Latitude>47.624192833900452</Latitude>  
              <Longitude>-117.43913769721985</Longitude>  
            </ActualStart>  
            <ActualEnd>  
              <Latitude>47.657259106636047</Latitude>  
              <Longitude>-117.41227939724922</Longitude>  
            </ActualEnd>  
            <StartLocation>  
              <Name>the south (on US-195 N)</Name>  
              <Point>  
                <Latitude>47.624192833900452</Latitude>  
                <Longitude>-117.43913769721985</Longitude>  
              </Point>  
              <Confidence>High</Confidence>  
            </StartLocation>  
            <EndLocation>  
              <Name>Spokane, WA</Name>  
              <Point>  
                <Latitude>47.6572597771883</Latitude>  
                <Longitude>-117.41227939724922</Longitude>  
              </Point>  
              <Confidence>High</Confidence>  
            </EndLocation>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>2.366</TravelDistance>  
              <TravelDuration>92</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.624192833900452</Latitude>  
                <Longitude>-117.43913769721985</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="DepartStart">Depart US-195 North toward W Thorpe Rd</Instruction>  
              <CompassDirection>northwest</CompassDirection>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>2.88</TravelDistance>  
              <TravelDuration>126</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.644169926643372</Latitude>  
                <Longitude>-117.44960904121399</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="RampThenHighwayRight">Take ramp right for I-90 East / US-2 North / US-395 East toward Spokane</Instruction>  
              <CompassDirection>north</CompassDirection>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>0.457</TravelDistance>  
              <TravelDuration>24</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.652651071548462</Latitude>  
                <Longitude>-117.41769075393677</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TakeRampRight">At exit 281, take ramp right for Division St / US-2 East / US-395 North toward Newport / Colville</Instruction>  
              <CompassDirection>east</CompassDirection>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>0.57600000000000007</TravelDistance>  
              <TravelDuration>86</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.652232646942139</Latitude>  
                <Longitude>-117.41167724132538</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TurnLeft">Turn left onto US-2 East / US-395 North / S Division St</Instruction>  
              <CompassDirection>north</CompassDirection>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>0.078</TravelDistance>  
              <TravelDuration>22</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.657259106636047</Latitude>  
                <Longitude>-117.41123735904694</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TurnLeft">Turn left onto W Sprague Ave</Instruction>  
              <CompassDirection>west</CompassDirection>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>0</TravelDistance>  
              <TravelDuration>0</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.657259106636047</Latitude>  
                <Longitude>-117.41227939724922</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="ArriveFinish">Arrive at Spokane, WA</Instruction>  
              <CompassDirection>west</CompassDirection>  
              <Hint hintType="PreviousIntersection">The last intersection is US-2 North / US-395 East / N Division St</Hint>  
              <Hint hintType="NextIntersection">If you reach US-2 South / US-395 West / N Browne St, you've gone too far</Hint>  
            </ItineraryItem>  
          </RouteLeg>  
        </Route>  
        <Route>  
          <Id>v60,i0,a0,cen-US,dAAAAAAAAAAA=,y0,s1,m0,o0,t0,wqBg8BIBJjvU=~kmIi/7masgAAAA4BAAAAAAA=~dGhlIHdlc3QgKG9uIFVTLTIgRSk=~~~,wqXc8BOY3kPU=~kmIi/8ntswAAAA4BjKv/PgA=~U3Bva2FuZSwgV0E=~0~~,k1</Id>  
          <BoundingBox>  
            <SouthLatitude>47.632818818092346</SouthLatitude>  
            <WestLongitude>-117.49714851379395</WestLongitude>  
            <NorthLatitude>47.657259106636047</NorthLatitude>  
            <EastLongitude>-117.41123735904694</EastLongitude>  
          </BoundingBox>  
          <DistanceUnit>Kilometer</DistanceUnit>  
          <DurationUnit>Second</DurationUnit>  
          <TravelDistance>8.071</TravelDistance>  
          <TravelDuration>406</TravelDuration>  
          <RouteLeg>  
            <TravelDistance>8.071</TravelDistance>  
            <TravelDuration>406</TravelDuration>  
            <ActualStart>  
              <Latitude>47.6409512758255</Latitude>  
              <Longitude>-117.49714851379395</Longitude>  
            </ActualStart>  
            <ActualEnd>  
              <Latitude>47.657259106636047</Latitude>  
              <Longitude>-117.41227939724922</Longitude>  
            </ActualEnd>  
            <StartLocation>  
              <Name>the west (on US-2 E)</Name>  
              <Point>  
                <Latitude>47.6409512758255</Latitude>  
                <Longitude>-117.49714851379395</Longitude>  
              </Point>  
              <Confidence>High</Confidence>  
            </StartLocation>  
            <EndLocation>  
              <Name>Spokane, WA</Name>  
              <Point>  
                <Latitude>47.6572597771883</Latitude>  
                <Longitude>-117.41227939724922</Longitude>  
              </Point>  
              <Confidence>High</Confidence>  
            </EndLocation>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>1.183</TravelDistance>  
              <TravelDuration>43</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.6409512758255</Latitude>  
                <Longitude>-117.49714851379395</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="DepartStart">Depart US-2 East</Instruction>  
              <CompassDirection>southeast</CompassDirection>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>5.777</TravelDistance>  
              <TravelDuration>229</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.635141611099243</Latitude>  
                <Longitude>-117.48395204544067</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="RampThenHighwayLeft">Take ramp left for I-90 East / US-2 North / US-395 East toward Spokane</Instruction>  
              <CompassDirection>southeast</CompassDirection>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>0.457</TravelDistance>  
              <TravelDuration>24</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.652651071548462</Latitude>  
                <Longitude>-117.41769075393677</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TakeRampRight">At exit 281, take ramp right for Division St / US-2 East / US-395 North toward Newport / Colville</Instruction>  
              <CompassDirection>east</CompassDirection>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>0.57600000000000007</TravelDistance>  
              <TravelDuration>86</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.652232646942139</Latitude>  
                <Longitude>-117.41167724132538</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TurnLeft">Turn left onto US-2 East / US-395 North / S Division St</Instruction>  
              <CompassDirection>north</CompassDirection>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>0.078</TravelDistance>  
              <TravelDuration>22</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.657259106636047</Latitude>  
                <Longitude>-117.41123735904694</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TurnLeft">Turn left onto W Sprague Ave</Instruction>  
              <CompassDirection>west</CompassDirection>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>0</TravelDistance>  
              <TravelDuration>0</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.657259106636047</Latitude>  
                <Longitude>-117.41227939724922</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="ArriveFinish">Arrive at Spokane, WA</Instruction>  
              <CompassDirection>west</CompassDirection>  
              <Hint hintType="PreviousIntersection">The last intersection is US-2 North / US-395 East / N Division St</Hint>  
              <Hint hintType="NextIntersection">If you reach US-2 South / US-395 West / N Browne St, you've gone too far</Hint>  
            </ItineraryItem>  
          </RouteLeg>  
        </Route>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
  
```  
  
 **JSON Response**  
  
 You would receive the following JSON response if the output=xml parameter was not set in this example.  
  
```json
{  
   "authenticationResultCode":"ValidCredentials",  
   "brandLogoUri":"http:\/\/veintplat3.live-int.com\/Branding\/logo_powered_by.png",  
   "copyright":"Copyright © 2010 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
   "resourceSets":[  
      {  
         "estimatedTotal":4,  
         "resources":[  
            {  
               "__type":"Route:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "bbox":[  
                  47.624192833900452,  
                  -117.4500972032547,  
                  47.657259106636047,  
                  -117.41123735904694  
               ],  
               "id":"v60,i0,a0,cen-US,dAAAAAAAAAAA=,y0,s1,m0,o0,t0,wCLc7BHCbj\/U=~kmIi\/8k0swAAAA4BAAAAAAA=~dGhlIHNvdXRoIChvbiBVUy0xOTUgTik=~~~,wqXc8BOc3kPU=~kmIi\/8ntswAAAA4BkMT\/PgA=~U3Bva2FuZSwgV0E=~0~~,k1",  
               "distanceUnit":"Kilometer",  
               "durationUnit":"Second",  
               "routeLegs":[  
                  {  
                     "actualEnd":{  
                        "type":"Point",  
                        "coordinates":[  
                           47.657259106636047,  
                           -117.41227872669697  
                        ]  
                     },  
                     "actualStart":{  
                        "type":"Point",  
                        "coordinates":[  
                           47.624192833900452,  
                           -117.43913769721985  
                        ]  
                     },  
                     "endLocation":{  
                        "name":"Spokane, WA",  
                        "point":{  
                           "type":"Point",  
                           "coordinates":[  
                              47.65726,  
                              -117.412279  
                           ]  
                        },  
                        "confidence":"High",  
                        "entityType":null  
                     },  
                     "itineraryItems":[  
                        {  
                           "compassDirection":"northwest",  
                           "instruction":{  
                              "maneuverType":"DepartStart",  
                              "text":"Depart US-195 North toward W Thorpe Rd"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.624192833900452,  
                                 -117.43913769721985  
                              ]  
                           },  
                           "travelDistance":2.366,  
                           "travelDuration":92,  
                           "travelMode":"Driving"  
                        },  
                        {  
                           "compassDirection":"north",  
                           "instruction":{  
                              "maneuverType":"RampThenHighwayRight",  
                              "text":"Take ramp right for I-90 East \/ US-2 North \/ US-395 East toward Spokane"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.644169926643372,  
                                 -117.44960904121399  
                              ]  
                           },  
                           "travelDistance":2.88,  
                           "travelDuration":126,  
                           "travelMode":"Driving"  
                        },  
                        {  
                           "compassDirection":"east",  
                           "instruction":{  
                              "maneuverType":"TakeRampRight",  
                              "text":"At exit 281, take ramp right for Division St \/ US-2 East \/ US-395 North toward Newport \/ Colville"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.652651071548462,  
                                 -117.41769075393677  
                              ]  
                           },  
                           "travelDistance":0.457,  
                           "travelDuration":24,  
                           "travelMode":"Driving"  
                        },  
                        {  
                           "compassDirection":"north",  
                           "instruction":{  
                              "maneuverType":"TurnLeft",  
                              "text":"Turn left onto US-2 East \/ US-395 North \/ S Division St"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.652232646942139,  
                                 -117.41167724132538  
                              ]  
                           },  
                           "travelDistance":0.57600000000000007,  
                           "travelDuration":86,  
                           "travelMode":"Driving"  
                        },  
                        {  
                           "compassDirection":"west",  
                           "instruction":{  
                              "maneuverType":"TurnLeft",  
                              "text":"Turn left onto W Sprague Ave"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.657259106636047,  
                                 -117.41123735904694  
                              ]  
                           },  
                           "travelDistance":0.078,  
                           "travelDuration":22,  
                           "travelMode":"Driving"  
                        },  
                        {  
                           "compassDirection":"west",  
                           "hints":[  
                              {  
                                 "hintType":"PreviousIntersection",  
                                 "text":"The last intersection is US-2 North \/ US-395 East \/ N Division St"  
                              },  
                              {  
                                 "hintType":"NextIntersection",  
                                 "text":"If you reach US-2 South \/ US-395 West \/ N Browne St, you've gone too far"  
                              }  
                           ],  
                           "instruction":{  
                              "maneuverType":"ArriveFinish",  
                              "text":"Arrive at Spokane, WA"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.657259106636047,  
                                 -117.41227872669697  
                              ]  
                           },  
                           "travelDistance":0,  
                           "travelDuration":0,  
                           "travelMode":"Driving"  
                        }  
                     ],  
                     "startLocation":{  
                        "name":"the south (on US-195 N)",  
                        "point":{  
                           "type":"Point",  
                           "coordinates":[  
                              47.624192833900452,  
                              -117.43913769721985  
                           ]  
                        },  
                        "confidence":"High",  
                        "entityType":null  
                     },  
                     "travelDistance":6.357,  
                     "travelDuration":352  
                  }  
               ],  
               "travelDistance":6.357,  
               "travelDuration":352  
            },  
            {  
               "__type":"Route:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "bbox":[  
                  47.657259106636047,  
                  -117.41332948207855,  
                  47.6739102602005,  
                  -117.41115152835846  
               ],  
               "id":"v60,i0,a0,cen-US,dAAAAAAAAAAA=,y0,s1,m0,o0,t0,wqNg8BHg+kPU=~kmIi\/zEItAAAAA4BAAAAAAA=~dGhlIG5vcnRoIChvbiBVUy0yIFcgLyBVUy0zOTUgUyAvIE4gRGl2aXNpb24gU3Qp~~~,wqXc8BOc3kPU=~kmIi\/8ntswAAAA4BkMT\/PgA=~U3Bva2FuZSwgV0E=~0~~,k1",  
               "distanceUnit":"Kilometer",  
               "durationUnit":"Second",  
               "routeLegs":[  
                  {  
                     "actualEnd":{  
                        "type":"Point",  
                        "coordinates":[  
                           47.657259106636047,  
                           -117.41227872669697  
                        ]  
                     },  
                     "actualStart":{  
                        "type":"Point",  
                        "coordinates":[  
                           47.6739102602005,  
                           -117.41115152835846  
                        ]  
                     },  
                     "endLocation":{  
                        "name":"Spokane, WA",  
                        "point":{  
                           "type":"Point",  
                           "coordinates":[  
                              47.65726,  
                              -117.412279  
                           ]  
                        },  
                        "confidence":"High",  
                        "entityType":null  
                     },  
                     "itineraryItems":[  
                        {  
                           "compassDirection":"south",  
                           "instruction":{  
                              "maneuverType":"DepartStart",  
                              "text":"Depart US-2 West \/ US-395 South \/ N Division St toward W Augusta Ave"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.6739102602005,  
                                 -117.41115152835846  
                              ]  
                           },  
                           "travelDistance":1.954,  
                           "travelDuration":176,  
                           "travelMode":"Driving"  
                        },  
                        {  
                           "compassDirection":"east",  
                           "instruction":{  
                              "maneuverType":"TurnLeft",  
                              "text":"Turn left onto W Sprague Ave"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.657259106636047,  
                                 -117.41331875324249  
                              ]  
                           },  
                           "travelDistance":0.078,  
                           "travelDuration":22,  
                           "travelMode":"Driving"  
                        },  
                        {  
                           "compassDirection":"east",  
                           "hints":[  
                              {  
                                 "hintType":"PreviousIntersection",  
                                 "text":"The last intersection is US-2 South \/ US-395 West \/ N Browne St"  
                              },  
                              {  
                                 "hintType":"NextIntersection",  
                                 "text":"If you reach US-2 North \/ US-395 East \/ N Division St, you've gone too far"  
                              }  
                           ],  
                           "instruction":{  
                              "maneuverType":"ArriveFinish",  
                              "text":"Arrive at Spokane, WA"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.657259106636047,  
                                 -117.41227872669697  
                              ]  
                           },  
                           "travelDistance":0,  
                           "travelDuration":0,  
                           "travelMode":"Driving"  
                        }  
                     ],  
                     "startLocation":{  
                        "name":"the north (on US-2 W \/ US-395 S \/ N Division St)",  
                        "point":{  
                           "type":"Point",  
                           "coordinates":[  
                              47.6739102602005,  
                              -117.41115152835846  
                           ]  
                        },  
                        "confidence":"High",  
                        "entityType":null  
                     },  
                     "travelDistance":2.032,  
                     "travelDuration":199  
                  }  
               ],  
               "travelDistance":2.032,  
               "travelDuration":199  
            },  
            {  
               "__type":"Route:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "bbox":[  
                  47.632818818092346,  
                  -117.49714851379395,  
                  47.657259106636047,  
                  -117.41123735904694  
               ],  
               "id":"v60,i0,a0,cen-US,dAAAAAAAAAAA=,y0,s1,m0,o0,t0,wqBg8BIBJjvU=~kmIi\/7masgAAAA4BAAAAAAA=~dGhlIHdlc3QgKG9uIFVTLTIgRSk=~~~,wqXc8BOc3kPU=~kmIi\/8ntswAAAA4BkMT\/PgA=~U3Bva2FuZSwgV0E=~0~~,k1",  
               "distanceUnit":"Kilometer",  
               "durationUnit":"Second",  
               "routeLegs":[  
                  {  
                     "actualEnd":{  
                        "type":"Point",  
                        "coordinates":[  
                           47.657259106636047,  
                           -117.41227872669697  
                        ]  
                     },  
                     "actualStart":{  
                        "type":"Point",  
                        "coordinates":[  
                           47.6409512758255,  
                           -117.49714851379395  
                        ]  
                     },  
                     "endLocation":{  
                        "name":"Spokane, WA",  
                        "point":{  
                           "type":"Point",  
                           "coordinates":[  
                              47.65726,  
                              -117.412279  
                           ]  
                        },  
                        "confidence":"High",  
                        "entityType":null  
                     },  
                     "itineraryItems":[  
                        {  
                           "compassDirection":"southeast",  
                           "instruction":{  
                              "maneuverType":"DepartStart",  
                              "text":"Depart US-2 East"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.6409512758255,  
                                 -117.49714851379395  
                              ]  
                           },  
                           "travelDistance":1.183,  
                           "travelDuration":43,  
                           "travelMode":"Driving"  
                        },  
                        {  
                           "compassDirection":"southeast",  
                           "instruction":{  
                              "maneuverType":"RampThenHighwayLeft",  
                              "text":"Take ramp left for I-90 East \/ US-2 North \/ US-395 East toward Spokane"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.635141611099243,  
                                 -117.48395204544067  
                              ]  
                           },  
                           "travelDistance":5.777,  
                           "travelDuration":229,  
                           "travelMode":"Driving"  
                        },  
                        {  
                           "compassDirection":"east",  
                           "instruction":{  
                              "maneuverType":"TakeRampRight",  
                              "text":"At exit 281, take ramp right for Division St \/ US-2 East \/ US-395 North toward Newport \/ Colville"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.652651071548462,  
                                 -117.41769075393677  
                              ]  
                           },  
                           "travelDistance":0.457,  
                           "travelDuration":24,  
                           "travelMode":"Driving"  
                        },  
                        {  
                           "compassDirection":"north",  
                           "instruction":{  
                              "maneuverType":"TurnLeft",  
                              "text":"Turn left onto US-2 East \/ US-395 North \/ S Division St"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.652232646942139,  
                                 -117.41167724132538  
                              ]  
                           },  
                           "travelDistance":0.57600000000000007,  
                           "travelDuration":86,  
                           "travelMode":"Driving"  
                        },  
                        {  
                           "compassDirection":"west",  
                           "instruction":{  
                              "maneuverType":"TurnLeft",  
                              "text":"Turn left onto W Sprague Ave"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.657259106636047,  
                                 -117.41123735904694  
                              ]  
                           },  
                           "travelDistance":0.078,  
                           "travelDuration":22,  
                           "travelMode":"Driving"  
                        },  
                        {  
                           "compassDirection":"west",  
                           "hints":[  
                              {  
                                 "hintType":"PreviousIntersection",  
                                 "text":"The last intersection is US-2 North \/ US-395 East \/ N Division St"  
                              },  
                              {  
                                 "hintType":"NextIntersection",  
                                 "text":"If you reach US-2 South \/ US-395 West \/ N Browne St, you've gone too far"  
                              }  
                           ],  
                           "instruction":{  
                              "maneuverType":"ArriveFinish",  
                              "text":"Arrive at Spokane, WA"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.657259106636047,  
                                 -117.41227872669697  
                              ]  
                           },  
                           "travelDistance":0,  
                           "travelDuration":0,  
                           "travelMode":"Driving"  
                        }  
                     ],  
                     "startLocation":{  
                        "name":"the west (on US-2 E)",  
                        "point":{  
                           "type":"Point",  
                           "coordinates":[  
                              47.6409512758255,  
                              -117.49714851379395  
                           ]  
                        },  
                        "confidence":"High",  
                        "entityType":null  
                     },  
                     "travelDistance":8.071,  
                     "travelDuration":406  
                  }  
               ],  
               "travelDistance":8.071,  
               "travelDuration":406  
            },  
            {  
               "__type":"Route:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "bbox":[  
                  47.65221118927002,  
                  -117.41227872669697,  
                  47.657259106636047,  
                  -117.38137900829315  
               ],  
               "id":"v60,i0,a0,cen-US,dAAAAAAAAAAA=,y0,s1,m0,o0,t0,woGQ8BOjrkPU=~kmIi\/8mBtAAAAA4BAAAAAAA=~dGhlIGVhc3QgKG9uIEktOTAgVyk=~~~,wqXc8BOc3kPU=~kmIi\/8ntswAAAA4BkMT\/PgA=~U3Bva2FuZSwgV0E=~0~~,k1",  
               "distanceUnit":"Kilometer",  
               "durationUnit":"Second",  
               "routeLegs":[  
                  {  
                     "actualEnd":{  
                        "type":"Point",  
                        "coordinates":[  
                           47.657259106636047,  
                           -117.41227872669697  
                        ]  
                     },  
                     "actualStart":{  
                        "type":"Point",  
                        "coordinates":[  
                           47.653992176055908,  
                           -117.38137900829315  
                        ]  
                     },  
                     "endLocation":{  
                        "name":"Spokane, WA",  
                        "point":{  
                           "type":"Point",  
                           "coordinates":[  
                              47.65726,  
                              -117.412279  
                           ]  
                        },  
                        "confidence":"High",  
                        "entityType":null  
                     },  
                     "itineraryItems":[  
                        {  
                           "compassDirection":"west",  
                           "instruction":{  
                              "maneuverType":"DepartStart",  
                              "text":"Depart I-90 West"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.653992176055908,  
                                 -117.38137900829315  
                              ]  
                           },  
                           "travelDistance":1.866,  
                           "travelDuration":67,  
                           "travelMode":"Driving"  
                        },  
                        {  
                           "compassDirection":"west",  
                           "instruction":{  
                              "maneuverType":"TakeRampRight",  
                              "text":"At exit 281, take ramp right for US-395 North \/ US-2 North toward Newport \/ Colville"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.652361392974854,  
                                 -117.40572810173035  
                              ]  
                           },  
                           "travelDistance":0.482,  
                           "travelDuration":66,  
                           "travelMode":"Driving"  
                        },  
                        {  
                           "compassDirection":"north",  
                           "instruction":{  
                              "maneuverType":"BearRight",  
                              "text":"Bear right onto US-2 East \/ US-395 North \/ S Division St"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.653520107269287,  
                                 -117.41123735904694  
                              ]  
                           },  
                           "travelDistance":0.418,  
                           "travelDuration":57,  
                           "travelMode":"Driving"  
                        },  
                        {  
                           "compassDirection":"west",  
                           "instruction":{  
                              "maneuverType":"TurnLeft",  
                              "text":"Turn left onto W Sprague Ave"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.657259106636047,  
                                 -117.41123735904694  
                              ]  
                           },  
                           "travelDistance":0.078,  
                           "travelDuration":22,  
                           "travelMode":"Driving"  
                        },  
                        {  
                           "compassDirection":"west",  
                           "hints":[  
                              {  
                                 "hintType":"PreviousIntersection",  
                                 "text":"The last intersection is US-2 North \/ US-395 East \/ N Division St"  
                              },  
                              {  
                                 "hintType":"NextIntersection",  
                                 "text":"If you reach US-2 South \/ US-395 West \/ N Browne St, you've gone too far"  
                              }  
                           ],  
                           "instruction":{  
                              "maneuverType":"ArriveFinish",  
                              "text":"Arrive at Spokane, WA"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.657259106636047,  
                                 -117.41227872669697  
                              ]  
                           },  
                           "travelDistance":0,  
                           "travelDuration":0,  
                           "travelMode":"Driving"  
                        }  
                     ],  
                     "startLocation":{  
                        "name":"the east (on I-90 W)",  
                        "point":{  
                           "type":"Point",  
                           "coordinates":[  
                              47.653992176055908,  
                              -117.38137900829315  
                           ]  
                        },  
                        "confidence":"High",  
                        "entityType":null  
                     },  
                     "travelDistance":2.844,  
                     "travelDuration":214  
                  }  
               ],  
               "travelDistance":2.844,  
               "travelDuration":214  
            }  
         ]  
      }  
   ],  
   "statusCode":200,  
   "statusDescription":"OK",  
   "traceId":"84c3d8e2626340e99a02f6e1c0c06543"  
}  
```  
  
## HTTP Status Codes  
  
[!INCLUDE [get-status-code-note](../../includes/get-status-code-note.md)]
  
 When the request is successful, the following HTTP status code is returned.  
  
* 200

When the request is not successful, the response returns one of the following errors.

* 400
* 401
* 404
* 429
* 500
* 503
  
## See Also  
 [Using the REST Services with .NET](../using-the-rest-services-with-net.md)
 [JSON Data Contracts](../json-data-contracts.md)
