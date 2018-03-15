---
title: "Snap to Road Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: b50c506f-11cd-4256-be4d-fdd46c05e322
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Snap to Road Example
The following example shows how to snap points to the road.

In this case, consider a trucking company that wants to do periodic safety reviews of the routes that their truck drivers take. The trucks have built-in GPS devices that collect GPS points as the truck drives along its route. The company wants to snap the GPS points to the likely road taken for accuracy because often times collected GPS points can deviate from the actual road the driver was on due to occasional GPS signal interference (i.e.: trees, buildings, etc.). The company also wants to get the posted truck speed limit of the road that the truck was on to compare to the actual speed the driver was travelling.

Notice that both standard and truck speed limits are requested in this query. The reason for this is few roads have posted truck speed limits, when there is no posted truck speed limit the value returned will be 0. When this occurs, the standard posted speed limit is assumed to also apply to trucks as well.

Responses are shown for both XML and JSON formats.

**HTTP GET Request URL**

```
https://dev.virtualearth.net/REST/v1/Routes/SnapToRoad?points=47.590868,-122.336729;47.601604,-122.336042;47.60849,-122.34241;47.610568,-122.345064&includeTruckSpeedLimit=true&IncludeSpeedLimit=true&speedUnit=MPH&travelMode=driving&key=BingMapsKey 
```

**HTTP POST Request URL**

```
https://dev.virtualearth.net/REST/v1/Routes/SnapToRoad?key=BingMapsKey
```

**HTTP POST Header**

```
Content-Length: 402
Content-Type: application/json
```

**HTTP POST Body**

```
{
    "points":  [
        { "latitude": 47.590868, "longitude": -122.336729 },
        { "latitude": 47.601604, "longitude": -122.336042 },
        { "latitude": 47.608490, "longitude": -122.342410 },
        { "latitude": 47.610568, "longitude": -122.345064 }    
    ],
    "includeSpeedLimit": true,
    "includeTruckSpeedLimit": true,
    "speedUnit": "MPH",
    "travelMode": "driving"
}
```

**JSON Response**

```
{
    "authenticationResultCode": "ValidCredentials",
    "brandLogoUri": "http:\/\/veplatppe.maps.live-int.com\/Branding\/logo_powered_by.png",
    "copyright": "Copyright © 2017 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",
    "resourceSets": [{
        "estimatedTotal": 1,
        "resources": [{
            "__type": "SnapToRoadResponse:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",
            "snappedPoints": [{
                "coordinate": {
                    "latitude": 47.590862,
                    "longitude": -122.336719
                },
                "index": 0,
                "name": "WA-99 N \/ Alaskan Way Viaduct",
                "speedLimit": 40,
                "speedUnit": "MPH",
                "truckSpeedLimit": 0
            }, {
                "coordinate": {
                    "latitude": 47.601575,
                    "longitude": -122.336077
                },
                "index": 1,
                "name": "WA-99 N \/ Alaskan Way Viaduct",
                "speedLimit": 40,
                "speedUnit": "MPH",
                "truckSpeedLimit": 0
            }, {
                "coordinate": {
                    "latitude": 47.60849,
                    "longitude": -122.34241
                },
                "index": 2,
                "name": "WA-99 N \/ Alaskan Way Viaduct",
                "speedLimit": 50,
                "speedUnit": "MPH",
                "truckSpeedLimit": 40
            }, {
                "coordinate": {
                    "latitude": 47.610576,
                    "longitude": -122.345058
                },
                "index": 3,
                "name": "",
                "speedLimit": 40,
                "speedUnit": "MPH",
                "truckSpeedLimit": 0
            }]
        }]
    }],
    "statusCode": 200,
    "statusDescription": "OK",
    "traceId": "79124acfd5a349aaac3100d079102543|EAP1048229|7.7.0.0|"
}
```

**XML Response**

Add *&output=xml* to the URL above to get the XML response.

```
<?xml version="1.0" encoding="utf-8"?>
<Response xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">
  <Copyright>Copyright © 2017 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>
  <BrandLogoUri>http://veplatppe.maps.live-int.com/Branding/logo_powered_by.png</BrandLogoUri>
  <StatusCode>200</StatusCode>
  <StatusDescription>OK</StatusDescription>
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>
  <TraceId>0e68673f787c4e2bb496f58556d736ff|EAP1048229|7.7.0.0|</TraceId>
  <ResourceSets>
    <ResourceSet>
      <EstimatedTotal>1</EstimatedTotal>
      <Resources>
        <Resource xsi:type="SnapToRoadResponse">
          <SnappedPoints>
            <SnappedPoint>
              <Name>WA-99 N / Alaskan Way Viaduct</Name>
              <Coordinate>
                <Latitude>47.590862</Latitude>
                <Longitude>-122.336719</Longitude>
              </Coordinate>
              <Index>0</Index>
              <SpeedLimit>40</SpeedLimit>
              <TruckSpeedLimit>0</TruckSpeedLimit>
              <SpeedUnit>MPH</SpeedUnit>
            </SnappedPoint>
            <SnappedPoint>
              <Name>WA-99 N / Alaskan Way Viaduct</Name>
              <Coordinate>
                <Latitude>47.601575</Latitude>
                <Longitude>-122.336077</Longitude>
              </Coordinate>
              <Index>1</Index>
              <SpeedLimit>40</SpeedLimit>
              <TruckSpeedLimit>0</TruckSpeedLimit>
              <SpeedUnit>MPH</SpeedUnit>
            </SnappedPoint>
            <SnappedPoint>
              <Name>WA-99 N / Alaskan Way Viaduct</Name>
              <Coordinate>
                <Latitude>47.60849</Latitude>
                <Longitude>-122.34241</Longitude>
              </Coordinate>
              <Index>2</Index>
              <SpeedLimit>50</SpeedLimit>
              <TruckSpeedLimit>40</TruckSpeedLimit>
              <SpeedUnit>MPH</SpeedUnit>
            </SnappedPoint>
            <SnappedPoint>
              <Name />
              <Coordinate>
                <Latitude>47.610576</Latitude>
                <Longitude>-122.345058</Longitude>
              </Coordinate>
              <Index>3</Index>
              <SpeedLimit>40</SpeedLimit>
              <TruckSpeedLimit>0</TruckSpeedLimit>
              <SpeedUnit>MPH</SpeedUnit>
            </SnappedPoint>
          </SnappedPoints>
        </Resource>
      </Resources>
    </ResourceSet>
  </ResourceSets>
</Response>
```

## See Also

* [Using the REST Services with .NET](../rest-services/using-the-rest-services-with-net.md)
