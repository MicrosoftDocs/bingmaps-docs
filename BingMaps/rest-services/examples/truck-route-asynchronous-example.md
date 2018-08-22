---
title: "Truck Route Asynchronous Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 13aa406b-2ff7-4b25-9015-06d4228a17ba
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Truck Route Asynchronous Example
This example makes an asynchronous truck routing request for a truck that is transporting a flammable material between Pittsburgh Brashear High School (590 Crane Ave, Pittsburgh, PA) and Duquesne University (600 Forbes Ave, Pittsburgh, PA). Vehicles carrying flammable material must avoid the Liberty Tunnel which most other vehicles would take when travelling between these two locations. Both a GET and its equivalent POST request are shown. Responses are shown for both XML and JSON formats.

**HTTP GET Request URL**

```
https://dev.virtualearth.net/REST/v1/Routes/TruckAsync?wp.0=590%20Crane%20Ave%2C%20Pittsburgh%2C%20PA&wp.1=600%20Forbes%20Ave%2C%20Pittsburgh%2C%20PA&vehicleHazardousMaterials=Flammable&key=BingMapsKey
```

**HTTP POST Request URL**

```
https://dev.virtualearth.net/REST/v1/Routes/TruckAsync?key=BingMapsKey
```

*HTTP POST Header*

```
Content-Length: 227            
 Content-Type: application/json
```

*HTTP POST Body*

```
{
    "waypoints": [{
        "address": "590 Crane Ave, Pittsburgh, PA"
    },{
        "address": "600 Forbes Ave, Pittsburgh, PA"
    }],
    "vehicleSpec": {
        "vehicleHazardousMaterials": "Flammable"
    }
}
```

**JSON Response**

```JSON
{
    "authenticationResultCode": "ValidCredentials",
    "brandLogoUri": "http:\/\/dev.virtualearth.net\/Branding\/logo_powered_by.png",
    "copyright": "Copyright © 2018 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",
    "resourceSets": [{
        "estimatedTotal": 1,
        "resources": [{
            "__type": "RouteProxyAsyncResult:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",
            "callbackInSeconds": 3,
            "callbackUrl": "https:\/\/dev.virtualearth.net\/REST\/v1\/Routes\/TruckAsyncCallback?key=xxxxxxxxxxxxxxxxxxx&requestId=9d721ef1-8ae1-4aef-a9b3-9badf01b4b1d",
            "errorMessage": "Request accepted",
            "isAccepted": true,
            "requestId": "9d721ef1-8ae1-4aef-a9b3-9badf01b4b1d"
        }]
    }],
    "statusCode": 200,
    "statusDescription": "OK",
    "traceId": "00aae20507b84317a0b68ddebb7bce3c|CO30276242|7.7.0.0|"
}
```

**XML Response**

Add &output=xml to the original request URL to get the XML response.

```XML
<?xml version="1.0" encoding="utf-8"?>
<Response xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">
    <Copyright>Copyright © 2018 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>
    <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>
    <StatusCode>200</StatusCode>
    <StatusDescription>OK</StatusDescription>
    <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>
    <TraceId>d3035a15199144b7b2724ef262711d72|CO30324209|7.7.0.0|</TraceId>
    <ResourceSets>
        <ResourceSet>
            <EstimatedTotal>1</EstimatedTotal>
            <Resources>
                <Resource xsi:type="RouteProxyAsyncResult">
                    <IsAccepted>true</IsAccepted>
                    <IsCompleted>false</IsCompleted>
                    <CallbackInSeconds>3</CallbackInSeconds>
                    <CallbackUrl>https://dev.virtualearth.net/REST/v1/Routes/TruckAsyncCallback?key=xxxxxxxxxxxxxxxxxx&amp;requestId=9d721ef1-8ae1-4aef-a9b3-9badf01b4b1d&amp;o=xml</CallbackUrl>
                    <ErrorMessage>Request accepted</ErrorMessage>
                    <RequestId>9d721ef1-8ae1-4aef-a9b3-9badf01b4b1d</RequestId>
                </Resource>
            </Resources>
        </ResourceSet>
    </ResourceSets>
</Response>
```

## Status Request

When making an asynchronous request to the truck routing service the initial response includes a *RouteProxyAsyncResult* which includes a unique *requestId*. This *requestId* can be used to check the status of the asynchronous truck routing request by using the following HTTP GET URL. The response from the initial request and all responses using the following status request URL will include a field which indicates an estimated amount of time remaining until the requested truck routing has been generated. The responses shown below in both XML and JSON formats are example of the status returned when the truck routing request has been completed.
HTTP GET Request URL

```
https://dev.virtualearth.net/REST/v1/Routes/TruckAsyncCallback?requestId=9d721ef1-8ae1-4aef-a9b3-9badf01b4b1d&key=BingMapsKey
```

**JSON Response**

```JSON
{
    "authenticationResultCode": "ValidCredentials",
    "brandLogoUri": "http:\/\/dev.virtualearth.net\/Branding\/logo_powered_by.png",
    "copyright": "Copyright © 2018 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",
    "resourceSets": [{
        "estimatedTotal": 1,
        "resources": [{
            "__type": "RouteProxyAsyncResult:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",
            "callbackInSeconds": -1,
            "callbackUrl": "https:\/\/dev.virtualearth.net\/REST\/v1\/Routes\/TruckAsyncCallback?key=xxxxxxxxxxxxxxxxx&requestId=9d721ef1-8ae1-4aef-a9b3-9badf01b4b1d",
            "isAccepted": true,
            "isCompleted": true,
            "requestId": "cd22cff0-cd65-4e5b-b781-e086219eb10a",
            "resultUrl": "https:\/\/dev.virtualearth.net\/REST\/v1\/Routes\/TruckAsyncCallback?key=xxxxxxxxxxxxxxx&requestId=9d721ef1-8ae1-4aef-a9b3-9badf01b4b1d&DownloadResult=true"
        }]
    }],
    "statusCode": 200,
    "statusDescription": "OK",
    "traceId": "5b04ceb5f48b4fb1834b69771d01aa85|CO30276339|7.7.0.0|"
}
```

**XML Response**

Add &output=xml to the original request URL to get the XML response.

```XML
<?xml version="1.0" encoding="utf-8"?>
<Response xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">
    <Copyright>Copyright © 2018 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>
    <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>
    <StatusCode>200</StatusCode>
    <StatusDescription>OK</StatusDescription>
    <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>
    <TraceId>d90319671fe9415ea354c319a8080773|CO30263812|7.7.0.0|</TraceId>
    <ResourceSets>
        <ResourceSet>
            <EstimatedTotal>1</EstimatedTotal>
            <Resources>
                <Resource xsi:type="RouteProxyAsyncResult">
                    <IsAccepted>true</IsAccepted>
                    <IsCompleted>true</IsCompleted>
                    <CallbackInSeconds>-1</CallbackInSeconds>
                    <CallbackUrl>https://dev.virtualearth.net/REST/v1/Routes/TruckAsyncCallback?key=xxxxxxxxxxxxxxxxxx&amp;requestId=9d721ef1-8ae1-4aef-a9b3-9badf01b4b1d&amp;o=xml</CallbackUrl>
                    <RequestId>9d721ef1-8ae1-4aef-a9b3-9badf01b4b1d</RequestId>
                    <ResultUrl>https://dev.virtualearth.net/REST/v1/Routes/TruckAsyncCallback?key=xxxxxxxxxxxxxxx&amp;requestId=9d721ef1-8ae1-4aef-a9b3-9badf01b4b1d&amp;o=xml&amp;DownloadResult=true</ResultUrl>
                </Resource>
            </Resources>
        </ResourceSet>
    </ResourceSets>
</Response>
```


## Downloaded Results

When an asynchronous truck routing request has completed, the status response will include a *resultUrl* field which can be used to download the requested truck routing result. The following is truck routing result that would be downloaded when using the *resultUrl*. The downloaded truck routing results are in the same format as the original request (JSON or XML).

**JSON Response**

```JSON
{
    "authenticationResultCode": "ValidCredentials",
    "brandLogoUri": "http:\/\/veplat2.maps.live-int.com\/Branding\/logo_powered_by.png",
    "copyright": "Copyright © 2017 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",
    "resourceSets": [{
        "estimatedTotal": 1,
        "resources": [{
            "__type": "Route:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",
            "bbox": [40.41682, -80.01989, 40.43807, -79.99351],
            "distanceUnit": "Mile",
            "durationUnit": "Second",
            "routeLegs": [{
                "actualEnd": {
                    "type": "Point",
                    "coordinates": [40.438033, -79.99351]
                },
                "actualStart": {
                    "type": "Point",
                    "coordinates": [40.416981, -80.018574]
                },
                "alternateVias": [],
                "cost": 0,
                "description": "US-19 TRUCK, PJ McArdle Roadway",
                "endLocation": {
                    "bbox": [40.433687, -80.000376, 40.441413, -79.986844],
                    "name": "600 Forbes Ave, Pittsburgh, PA 15219",
                    "point": {
                        "type": "Point",
                        "coordinates": [40.43755, -79.99361]
                    },
                    "address": {
                        "addressLine": "600 Forbes Ave",
                        "adminDistrict": "PA",
                        "adminDistrict2": "Allegheny",
                        "countryRegion": "United States",
                        "formattedAddress": "600 Forbes Ave, Pittsburgh, PA 15219",
                        "locality": "Pittsburgh",
                        "postalCode": "15219"
                    },
                    "confidence": "High",
                    "entityType": "Address",
                    "geocodePoints": [{
                        "type": "Point",
                        "coordinates": [40.43755, -79.99361],
                        "calculationMethod": "Rooftop",
                        "usageTypes": ["Display"]
                    }, {
                        "type": "Point",
                        "coordinates": [40.438033, -79.99351],
                        "calculationMethod": "Rooftop",
                        "usageTypes": ["Route"]
                    }],
                    "matchCodes": ["Good"]
                },
                "itineraryItems": [{
                    "compassDirection": "east",
                    "details": [{
                        "compassDegrees": 96,
                        "endPathIndices": [2],
                        "maneuverType": "DepartStart",
                        "mode": "Driving",
                        "names": ["Crane Ave"],
                        "roadType": "Arterial",
                        "startPathIndices": [0]
                    }],
                    "iconType": "Auto",
                    "instruction": {
                        "formattedText": null,
                        "maneuverType": "DepartStart",
                        "text": "Depart Crane Ave toward US-19 TRUCK \/ PA-51 \/ Saw Mill Run Blvd"
                    },
                    "maneuverPoint": {
                        "type": "Point",
                        "coordinates": [40.416981, -80.018574]
                    },
                    "sideOfStreet": "Unknown",
                    "towardsRoadName": "US-19 TRUCK \/ PA-51 \/ Saw Mill Run Blvd",
                    "travelDistance": 0.214373,
                    "travelDuration": 38,
                    "travelMode": "Driving"
                }, {
                    "compassDirection": "north",
                    "details": [{
                        "compassDegrees": 341,
                        "endPathIndices": [8],
                        "locationCodes": ["104-04700"],
                        "maneuverType": "TurnLeft",
                        "mode": "Driving",
                        "names": ["Saw Mill Run Blvd"],
                        "roadShieldRequestParameters": {
                            "bucket": 656023,
                            "shields": [{
                                "labels": ["19"],
                                "roadShieldType": 2
                            }]
                        },
                        "roadType": "MajorRoad",
                        "startPathIndices": [2]
                    }],
                    "iconType": "Auto",
                    "instruction": {
                        "formattedText": null,
                        "maneuverType": "TurnLeft",
                        "text": "Turn left onto US-19 TRUCK \/ PA-51 \/ Saw Mill Run Blvd"
                    },
                    "maneuverPoint": {
                        "type": "Point",
                        "coordinates": [40.41703, -80.01453]
                    },
                    "sideOfStreet": "Unknown",
                    "travelDistance": 0.691586,
                    "travelDuration": 86,
                    "travelMode": "Driving"
                }, {
                    "compassDirection": "east",
                    "details": [{
                        "compassDegrees": 77,
                        "endPathIndices": [13],
                        "maneuverType": "TurnRight",
                        "mode": "Driving",
                        "names": ["Woodruff St"],
                        "roadType": "Arterial",
                        "startPathIndices": [8]
                    }],
                    "iconType": "Auto",
                    "instruction": {
                        "formattedText": null,
                        "maneuverType": "TurnRight",
                        "text": "Turn right onto Woodruff St"
                    },
                    "maneuverPoint": {
                        "type": "Point",
                        "coordinates": [40.42583, -80.01989]
                    },
                    "sideOfStreet": "Unknown",
                    "travelDistance": 0.455465,
                    "travelDuration": 76,
                    "travelMode": "Driving"
                }, {
                    "compassDirection": "north",
                    "details": [{
                        "endPathIndices": [17],
                        "maneuverType": "TurnLeft",
                        "mode": "Driving",
                        "names": ["Merrimac St"],
                        "roadType": "Arterial",
                        "startPathIndices": [13]
                    }],
                    "iconType": "Auto",
                    "instruction": {
                        "formattedText": null,
                        "maneuverType": "TurnLeft",
                        "text": "Turn left onto Merrimac St"
                    },
                    "maneuverPoint": {
                        "type": "Point",
                        "coordinates": [40.4302, -80.01371]
                    },
                    "sideOfStreet": "Unknown",
                    "travelDistance": 0.359774,
                    "travelDuration": 99,
                    "travelMode": "Driving"
                }, {
                    "compassDirection": "northeast",
                    "details": [{
                        "compassDegrees": 41,
                        "endPathIndices": [24],
                        "maneuverType": "RoadNameChange",
                        "mode": "Driving",
                        "names": ["PJ McArdle Roadway"],
                        "roadType": "Arterial",
                        "startPathIndices": [17]
                    }],
                    "iconType": "Auto",
                    "instruction": {
                        "formattedText": null,
                        "maneuverType": "RoadNameChange",
                        "text": "Road name changes to PJ McArdle Roadway"
                    },
                    "maneuverPoint": {
                        "type": "Point",
                        "coordinates": [40.43536, -80.0129]
                    },
                    "sideOfStreet": "Unknown",
                    "travelDistance": 0.853764,
                    "travelDuration": 95,
                    "travelMode": "Driving"
                }, {
                    "compassDirection": "northeast",
                    "details": [{
                        "compassDegrees": 37,
                        "endPathIndices": [26],
                        "locationCodes": ["104N04720", "104-04720"],
                        "maneuverType": "TurnLeft",
                        "mode": "Driving",
                        "names": ["Liberty Bridge"],
                        "roadType": "MajorRoad",
                        "startPathIndices": [24]
                    }],
                    "iconType": "Auto",
                    "instruction": {
                        "formattedText": null,
                        "maneuverType": "TurnLeft",
                        "text": "Turn left onto Liberty Bridge"
                    },
                    "maneuverPoint": {
                        "type": "Point",
                        "coordinates": [40.4292, -79.9993]
                    },
                    "sideOfStreet": "Unknown",
                    "travelDistance": 0.397056,
                    "travelDuration": 82,
                    "travelMode": "Driving"
                }, {
                    "compassDirection": "northeast",
                    "details": [{
                        "compassDegrees": 34,
                        "endPathIndices": [28],
                        "locationCodes": ["104N04721"],
                        "maneuverType": "KeepStraight",
                        "mode": "Driving",
                        "names": ["Crosstown Blvd"],
                        "roadType": "MajorRoad",
                        "startPathIndices": [26]
                    }],
                    "iconType": "Auto",
                    "instruction": {
                        "formattedText": null,
                        "maneuverType": "KeepStraight",
                        "text": "Keep straight onto Crosstown Blvd"
                    },
                    "maneuverPoint": {
                        "type": "Point",
                        "coordinates": [40.43427, -79.99574]
                    },
                    "sideOfStreet": "Unknown",
                    "signs": ["6th Ave", "Forbes Ave", "I-579 North"],
                    "travelDistance": 0.14043,
                    "travelDuration": 15,
                    "travelMode": "Driving"
                }, {
                    "compassDirection": "north",
                    "details": [{
                        "compassDegrees": 7,
                        "endPathIndices": [30],
                        "maneuverType": "TakeRampLeft",
                        "mode": "Driving",
                        "names": [],
                        "roadType": "Ramp",
                        "startPathIndices": [28]
                    }],
                    "iconType": "Auto",
                    "instruction": {
                        "formattedText": null,
                        "maneuverType": "TakeRampLeft",
                        "text": "Take ramp left toward 6th Ave \/ Forbes Ave"
                    },
                    "maneuverPoint": {
                        "type": "Point",
                        "coordinates": [40.43607, -79.99451]
                    },
                    "sideOfStreet": "Unknown",
                    "signs": ["6th Ave", "Forbes Ave"],
                    "travelDistance": 0.138566,
                    "travelDuration": 30,
                    "travelMode": "Driving"
                }, {
                    "compassDirection": "east",
                    "details": [{
                        "compassDegrees": 85,
                        "endPathIndices": [34],
                        "locationCodes": ["104-09110"],
                        "maneuverType": "TurnRight",
                        "mode": "Driving",
                        "names": ["Forbes Ave"],
                        "roadType": "Arterial",
                        "startPathIndices": [30]
                    }],
                    "iconType": "Auto",
                    "instruction": {
                        "formattedText": null,
                        "maneuverType": "TurnRight",
                        "text": "Turn right onto Forbes Ave"
                    },
                    "maneuverPoint": {
                        "type": "Point",
                        "coordinates": [40.43805, -79.99415]
                    },
                    "sideOfStreet": "Unknown",
                    "travelDistance": 0.033554,
                    "travelDuration": 12,
                    "travelMode": "Driving"
                }, {
                    "compassDirection": "east",
                    "details": [{
                        "compassDegrees": 96,
                        "endPathIndices": [34],
                        "locationCodes": ["104-09110"],
                        "maneuverType": "ArriveFinish",
                        "mode": "Driving",
                        "names": ["Forbes Ave"],
                        "roadType": "Arterial",
                        "startPathIndices": [34]
                    }],
                    "hints": [{
                        "hintType": "PreviousIntersection",
                        "text": "The last intersection is Shingiss St"
                    }, {
                        "hintType": "NextIntersection",
                        "text": "If you reach Boyd St, you've gone too far"
                    }],
                    "iconType": "Auto",
                    "instruction": {
                        "formattedText": null,
                        "maneuverType": "ArriveFinish",
                        "text": "Arrive at Stop: Y, X = 40.438033, -79.99351"
                    },
                    "maneuverPoint": {
                        "type": "Point",
                        "coordinates": [40.438033, -79.99351]
                    },
                    "sideOfStreet": "Unknown",
                    "travelDistance": 0,
                    "travelDuration": 0,
                    "travelMode": "Driving"
                }],
                "routeSubLegs": [{
                    "endWaypoint": {
                        "type": "Point",
                        "coordinates": [40.438033, -79.99351],
                        "description": "Stop: Y, X = 40.438033, -79.99351",
                        "isVia": false,
                        "locationIdentifier": "",
                        "routePathIndex": 34
                    },
                    "startWaypoint": {
                        "type": "Point",
                        "coordinates": [40.416981, -80.018574],
                        "description": "Stop: Y, X = 40.416981, -80.018574",
                        "isVia": false,
                        "locationIdentifier": "",
                        "routePathIndex": 0
                    },
                    "travelDistance": 3.284568,
                    "travelDuration": 536
                }],
                "startLocation": {
                    "bbox": [40.415365, -80.024903, 40.423091, -80.011373],
                    "name": "590 Crane Ave, Pittsburgh, PA 15216",
                    "point": {
                        "type": "Point",
                        "coordinates": [40.419228, -80.018138]
                    },
                    "address": {
                        "addressLine": "590 Crane Ave",
                        "adminDistrict": "PA",
                        "adminDistrict2": "Allegheny",
                        "countryRegion": "United States",
                        "formattedAddress": "590 Crane Ave, Pittsburgh, PA 15216",
                        "locality": "Pittsburgh",
                        "postalCode": "15216"
                    },
                    "confidence": "High",
                    "entityType": "Address",
                    "geocodePoints": [{
                        "type": "Point",
                        "coordinates": [40.419228, -80.018138],
                        "calculationMethod": "Rooftop",
                        "usageTypes": ["Display"]
                    }, {
                        "type": "Point",
                        "coordinates": [40.416981, -80.018574],
                        "calculationMethod": "Rooftop",
                        "usageTypes": ["Route"]
                    }],
                    "matchCodes": ["Good"]
                },
                "travelDistance": 3.284568,
                "travelDuration": 536
            }],
            "trafficCongestion": "Unknown",
            "trafficDataUsed": "None",
            "travelDistance": 3.284568,
            "travelDuration": 536,
            "travelDurationTraffic": 765
        }]
    }],
    "statusCode": 200,
    "statusDescription": "OK",
    "traceId": "29597209e24e4135b256baebd8488617|EAP8083228|7.7.0.0|"
}
```

**XML Response**

Add `&output=xml` to the URL above to get the XML response.

```XML
<?xml version="1.0" encoding="utf-8"?>
<Response xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">
  <Copyright>Copyright © 2017 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>
  <BrandLogoUri>http://veplat2.maps.live-int.com/Branding/logo_powered_by.png</BrandLogoUri>
  <StatusCode>200</StatusCode>
  <StatusDescription>OK</StatusDescription>
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>
  <TraceId>ee29f23fe70148e09351ab0d4b72b238|EAP8083229|7.7.0.0|</TraceId>
  <ResourceSets>
    <ResourceSet>
      <EstimatedTotal>1</EstimatedTotal>
      <Resources>
        <Route>
          <BoundingBox>
            <SouthLatitude>40.41682</SouthLatitude>
            <WestLongitude>-80.01989</WestLongitude>
            <NorthLatitude>40.43807</NorthLatitude>
            <EastLongitude>-79.99351</EastLongitude>
          </BoundingBox>
          <DistanceUnit>Mile</DistanceUnit>
          <DurationUnit>Second</DurationUnit>
          <TravelDistance>3.284568</TravelDistance>
          <TravelDuration>536</TravelDuration>
          <TravelDurationTraffic>765</TravelDurationTraffic>
          <RouteLeg>
            <TravelDistance>3.284568</TravelDistance>
            <TravelDuration>536</TravelDuration>
            <Cost>0</Cost>
            <ActualStart>
              <Latitude>40.416981</Latitude>
              <Longitude>-80.018574</Longitude>
            </ActualStart>
            <ActualEnd>
              <Latitude>40.438033</Latitude>
              <Longitude>-79.99351</Longitude>
            </ActualEnd>
            <StartLocation>
              <Name>590 Crane Ave, Pittsburgh, PA 15216</Name>
              <Point>
                <Latitude>40.419228</Latitude>
                <Longitude>-80.018138</Longitude>
              </Point>
              <BoundingBox>
                <SouthLatitude>40.415365</SouthLatitude>
                <WestLongitude>-80.024903</WestLongitude>
                <NorthLatitude>40.423091</NorthLatitude>
                <EastLongitude>-80.011373</EastLongitude>
              </BoundingBox>
              <EntityType>Address</EntityType>
              <Address>
                <AddressLine>590 Crane Ave</AddressLine>
                <AdminDistrict>PA</AdminDistrict>
                <AdminDistrict2>Allegheny</AdminDistrict2>
                <CountryRegion>United States</CountryRegion>
                <FormattedAddress>590 Crane Ave, Pittsburgh, PA 15216</FormattedAddress>
                <Locality>Pittsburgh</Locality>
                <PostalCode>15216</PostalCode>
              </Address>
              <Confidence>High</Confidence>
              <MatchCode>Good</MatchCode>
              <GeocodePoint>
                <Latitude>40.419228</Latitude>
                <Longitude>-80.018138</Longitude>
                <CalculationMethod>Rooftop</CalculationMethod>
                <UsageType>Display</UsageType>
              </GeocodePoint>
              <GeocodePoint>
                <Latitude>40.416981</Latitude>
                <Longitude>-80.018574</Longitude>
                <CalculationMethod>Rooftop</CalculationMethod>
                <UsageType>Route</UsageType>
              </GeocodePoint>
            </StartLocation>
            <EndLocation>
              <Name>600 Forbes Ave, Pittsburgh, PA 15219</Name>
              <Point>
                <Latitude>40.43755</Latitude>
                <Longitude>-79.99361</Longitude>
              </Point>
              <BoundingBox>
                <SouthLatitude>40.433687</SouthLatitude>
                <WestLongitude>-80.000376</WestLongitude>
                <NorthLatitude>40.441413</NorthLatitude>
                <EastLongitude>-79.986844</EastLongitude>
              </BoundingBox>
              <EntityType>Address</EntityType>
              <Address>
                <AddressLine>600 Forbes Ave</AddressLine>
                <AdminDistrict>PA</AdminDistrict>
                <AdminDistrict2>Allegheny</AdminDistrict2>
                <CountryRegion>United States</CountryRegion>
                <FormattedAddress>600 Forbes Ave, Pittsburgh, PA 15219</FormattedAddress>
                <Locality>Pittsburgh</Locality>
                <PostalCode>15219</PostalCode>
              </Address>
              <Confidence>High</Confidence>
              <MatchCode>Good</MatchCode>
              <GeocodePoint>
                <Latitude>40.43755</Latitude>
                <Longitude>-79.99361</Longitude>
                <CalculationMethod>Rooftop</CalculationMethod>
                <UsageType>Display</UsageType>
              </GeocodePoint>
              <GeocodePoint>
                <Latitude>40.438033</Latitude>
                <Longitude>-79.99351</Longitude>
                <CalculationMethod>Rooftop</CalculationMethod>
                <UsageType>Route</UsageType>
              </GeocodePoint>
            </EndLocation>
            <ItineraryItem>
              <TravelMode>Driving</TravelMode>
              <TravelDistance>0.214373</TravelDistance>
              <TravelDuration>38</TravelDuration>
              <ManeuverPoint>
                <Latitude>40.416981</Latitude>
                <Longitude>-80.018574</Longitude>
              </ManeuverPoint>
              <Instruction maneuverType="DepartStart">Depart Crane Ave toward US-19 TRUCK / PA-51 / Saw Mill Run Blvd</Instruction>
              <CompassDirection>east</CompassDirection>
              <Detail>
                <ManeuverType>DepartStart</ManeuverType>
                <StartPathIndex>0</StartPathIndex>
                <EndPathIndex>2</EndPathIndex>
                <Name>Crane Ave</Name>
                <CompassDegrees>96</CompassDegrees>
                <Mode>Driving</Mode>
                <RoadType>Arterial</RoadType>
              </Detail>
              <IconType>Auto</IconType>
              <TowardsRoadName>US-19 TRUCK / PA-51 / Saw Mill Run Blvd</TowardsRoadName>
              <SideOfStreet>Unknown</SideOfStreet>
            </ItineraryItem>
            <ItineraryItem>
              <TravelMode>Driving</TravelMode>
              <TravelDistance>0.691586</TravelDistance>
              <TravelDuration>86</TravelDuration>
              <ManeuverPoint>
                <Latitude>40.41703</Latitude>
                <Longitude>-80.01453</Longitude>
              </ManeuverPoint>
              <Instruction maneuverType="TurnLeft">Turn left onto US-19 TRUCK / PA-51 / Saw Mill Run Blvd</Instruction>
              <CompassDirection>north</CompassDirection>
              <Detail>
                <ManeuverType>TurnLeft</ManeuverType>
                <StartPathIndex>2</StartPathIndex>
                <EndPathIndex>8</EndPathIndex>
                <Name>Saw Mill Run Blvd</Name>
                <CompassDegrees>341</CompassDegrees>
                <Mode>Driving</Mode>
                <RoadType>MajorRoad</RoadType>
                <RoadShieldRequestParameters>
                  <Bucket>656023</Bucket>
                  <Shield>
                    <RoadShieldType>2</RoadShieldType>
                    <Label>19</Label>
                  </Shield>
                </RoadShieldRequestParameters>
                <LocationCode>104-04700</LocationCode>
              </Detail>
              <IconType>Auto</IconType>
              <SideOfStreet>Unknown</SideOfStreet>
            </ItineraryItem>
            <ItineraryItem>
              <TravelMode>Driving</TravelMode>
              <TravelDistance>0.455465</TravelDistance>
              <TravelDuration>76</TravelDuration>
              <ManeuverPoint>
                <Latitude>40.42583</Latitude>
                <Longitude>-80.01989</Longitude>
              </ManeuverPoint>
              <Instruction maneuverType="TurnRight">Turn right onto Woodruff St</Instruction>
              <CompassDirection>east</CompassDirection>
              <Detail>
                <ManeuverType>TurnRight</ManeuverType>
                <StartPathIndex>8</StartPathIndex>
                <EndPathIndex>13</EndPathIndex>
                <Name>Woodruff St</Name>
                <CompassDegrees>77</CompassDegrees>
                <Mode>Driving</Mode>
                <RoadType>Arterial</RoadType>
              </Detail>
              <IconType>Auto</IconType>
              <SideOfStreet>Unknown</SideOfStreet>
            </ItineraryItem>
            <ItineraryItem>
              <TravelMode>Driving</TravelMode>
              <TravelDistance>0.359774</TravelDistance>
              <TravelDuration>99</TravelDuration>
              <ManeuverPoint>
                <Latitude>40.4302</Latitude>
                <Longitude>-80.01371</Longitude>
              </ManeuverPoint>
              <Instruction maneuverType="TurnLeft">Turn left onto Merrimac St</Instruction>
              <CompassDirection>north</CompassDirection>
              <Detail>
                <ManeuverType>TurnLeft</ManeuverType>
                <StartPathIndex>13</StartPathIndex>
                <EndPathIndex>17</EndPathIndex>
                <Name>Merrimac St</Name>
                <CompassDegrees>0</CompassDegrees>
                <Mode>Driving</Mode>
                <RoadType>Arterial</RoadType>
              </Detail>
              <IconType>Auto</IconType>
              <SideOfStreet>Unknown</SideOfStreet>
            </ItineraryItem>
            <ItineraryItem>
              <TravelMode>Driving</TravelMode>
              <TravelDistance>0.853764</TravelDistance>
              <TravelDuration>95</TravelDuration>
              <ManeuverPoint>
                <Latitude>40.43536</Latitude>
                <Longitude>-80.0129</Longitude>
              </ManeuverPoint>
              <Instruction maneuverType="RoadNameChange">Road name changes to PJ McArdle Roadway</Instruction>
              <CompassDirection>northeast</CompassDirection>
              <Detail>
                <ManeuverType>RoadNameChange</ManeuverType>
                <StartPathIndex>17</StartPathIndex>
                <EndPathIndex>24</EndPathIndex>
                <Name>PJ McArdle Roadway</Name>
                <CompassDegrees>41</CompassDegrees>
                <Mode>Driving</Mode>
                <RoadType>Arterial</RoadType>
              </Detail>
              <IconType>Auto</IconType>
              <SideOfStreet>Unknown</SideOfStreet>
            </ItineraryItem>
            <ItineraryItem>
              <TravelMode>Driving</TravelMode>
              <TravelDistance>0.397056</TravelDistance>
              <TravelDuration>82</TravelDuration>
              <ManeuverPoint>
                <Latitude>40.4292</Latitude>
                <Longitude>-79.9993</Longitude>
              </ManeuverPoint>
              <Instruction maneuverType="TurnLeft">Turn left onto Liberty Bridge</Instruction>
              <CompassDirection>northeast</CompassDirection>
              <Detail>
                <ManeuverType>TurnLeft</ManeuverType>
                <StartPathIndex>24</StartPathIndex>
                <EndPathIndex>26</EndPathIndex>
                <Name>Liberty Bridge</Name>
                <CompassDegrees>37</CompassDegrees>
                <Mode>Driving</Mode>
                <RoadType>MajorRoad</RoadType>
                <LocationCode>104N04720</LocationCode>
                <LocationCode>104-04720</LocationCode>
              </Detail>
              <IconType>Auto</IconType>
              <SideOfStreet>Unknown</SideOfStreet>
            </ItineraryItem>
            <ItineraryItem>
              <TravelMode>Driving</TravelMode>
              <TravelDistance>0.14043</TravelDistance>
              <TravelDuration>15</TravelDuration>
              <ManeuverPoint>
                <Latitude>40.43427</Latitude>
                <Longitude>-79.99574</Longitude>
              </ManeuverPoint>
              <Instruction maneuverType="KeepStraight">Keep straight onto Crosstown Blvd</Instruction>
              <CompassDirection>northeast</CompassDirection>
              <Detail>
                <ManeuverType>KeepStraight</ManeuverType>
                <StartPathIndex>26</StartPathIndex>
                <EndPathIndex>28</EndPathIndex>
                <Name>Crosstown Blvd</Name>
                <CompassDegrees>34</CompassDegrees>
                <Mode>Driving</Mode>
                <RoadType>MajorRoad</RoadType>
                <LocationCode>104N04721</LocationCode>
              </Detail>
              <Sign>6th Ave</Sign>
              <Sign>Forbes Ave</Sign>
              <Sign>I-579 North</Sign>
              <IconType>Auto</IconType>
              <SideOfStreet>Unknown</SideOfStreet>
            </ItineraryItem>
            <ItineraryItem>
              <TravelMode>Driving</TravelMode>
              <TravelDistance>0.138566</TravelDistance>
              <TravelDuration>30</TravelDuration>
              <ManeuverPoint>
                <Latitude>40.43607</Latitude>
                <Longitude>-79.99451</Longitude>
              </ManeuverPoint>
              <Instruction maneuverType="TakeRampLeft">Take ramp left toward 6th Ave / Forbes Ave</Instruction>
              <CompassDirection>north</CompassDirection>
              <Detail>
                <ManeuverType>TakeRampLeft</ManeuverType>
                <StartPathIndex>28</StartPathIndex>
                <EndPathIndex>30</EndPathIndex>
                <CompassDegrees>7</CompassDegrees>
                <Mode>Driving</Mode>
                <RoadType>Ramp</RoadType>
              </Detail>
              <Sign>6th Ave</Sign>
              <Sign>Forbes Ave</Sign>
              <IconType>Auto</IconType>
              <SideOfStreet>Unknown</SideOfStreet>
            </ItineraryItem>
            <ItineraryItem>
              <TravelMode>Driving</TravelMode>
              <TravelDistance>0.033554</TravelDistance>
              <TravelDuration>12</TravelDuration>
              <ManeuverPoint>
                <Latitude>40.43805</Latitude>
                <Longitude>-79.99415</Longitude>
              </ManeuverPoint>
              <Instruction maneuverType="TurnRight">Turn right onto Forbes Ave</Instruction>
              <CompassDirection>east</CompassDirection>
              <Detail>
                <ManeuverType>TurnRight</ManeuverType>
                <StartPathIndex>30</StartPathIndex>
                <EndPathIndex>34</EndPathIndex>
                <Name>Forbes Ave</Name>
                <CompassDegrees>85</CompassDegrees>
                <Mode>Driving</Mode>
                <RoadType>Arterial</RoadType>
                <LocationCode>104-09110</LocationCode>
              </Detail>
              <IconType>Auto</IconType>
              <SideOfStreet>Unknown</SideOfStreet>
            </ItineraryItem>
            <ItineraryItem>
              <TravelMode>Driving</TravelMode>
              <TravelDistance>0</TravelDistance>
              <TravelDuration>0</TravelDuration>
              <ManeuverPoint>
                <Latitude>40.438033</Latitude>
                <Longitude>-79.99351</Longitude>
              </ManeuverPoint>
              <Instruction maneuverType="ArriveFinish">Arrive at Stop: Y, X = 40.438033, -79.99351</Instruction>
              <CompassDirection>east</CompassDirection>
              <Hint hintType="PreviousIntersection">The last intersection is Shingiss St</Hint>
              <Hint hintType="NextIntersection">If you reach Boyd St, you've gone too far</Hint>
              <Detail>
                <ManeuverType>ArriveFinish</ManeuverType>
                <StartPathIndex>34</StartPathIndex>
                <EndPathIndex>34</EndPathIndex>
                <Name>Forbes Ave</Name>
                <CompassDegrees>96</CompassDegrees>
                <Mode>Driving</Mode>
                <RoadType>Arterial</RoadType>
                <LocationCode>104-09110</LocationCode>
              </Detail>
              <IconType>Auto</IconType>
              <SideOfStreet>Unknown</SideOfStreet>
            </ItineraryItem>
            <RouteSubLeg>
              <TravelDistance>3.284568</TravelDistance>
              <TravelDuration>536</TravelDuration>
              <StartWaypoint>
                <Latitude>40.416981</Latitude>
                <Longitude>-80.018574</Longitude>
                <Description>Stop: Y, X = 40.416981, -80.018574</Description>
                <IsVia>false</IsVia>
                <LocationIdentifier />
                <RoutePathIndex>0</RoutePathIndex>
              </StartWaypoint>
              <EndWaypoint>
                <Latitude>40.438033</Latitude>
                <Longitude>-79.99351</Longitude>
                <Description>Stop: Y, X = 40.438033, -79.99351</Description>
                <IsVia>false</IsVia>
                <LocationIdentifier />
                <RoutePathIndex>34</RoutePathIndex>
              </EndWaypoint>
            </RouteSubLeg>
            <Description>US-19 TRUCK, PJ McArdle Roadway</Description>
          </RouteLeg>
        </Route>
      </Resources>
    </ResourceSet>
  </ResourceSets>
</Response>
```

## See Also

* [Using the REST Services with .NET](../rest-services/using-the-rest-services-with-net.md)
