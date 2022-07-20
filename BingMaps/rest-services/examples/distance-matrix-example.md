---
title: "Distance Matrix Example | Microsoft Docs"
description: "This distance matrix example returns a simple distance matrix between a set of origins and destinations."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 3e525b3f-ea78-41c2-b1b3-2b483b1838c0
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Distance Matrix Example

This example returns a simple distance matrix between a set of origins and destinations. Both a GET and its equivalent POST request are shown. Responses are shown for both XML and JSON formats.

**HTTP GET Request URL**

```url
https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins=47.6044,-122.3345;47.6731,-122.1185;47.6149,-122.1936&destinations=45.5347,-122.6231;47.4747,-122.2057&travelMode=driving&key={BingMapsKey}
```

**HTTP POST Request URL**

```url
https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?key={BingMapsKey}
```

HTTP POST Header

```url
Content-Length: 450
Content-Type: application/json
```

*HTTP POST Body*

```json
{
    "origins": [{
        "latitude": 47.6044,
        "longitude": -122.3345
    },
    {
        "latitude": 47.6731,
        "longitude": -122.1185
    },
    {
        "latitude": 47.6149,
        "longitude": -122.1936
    }],
    "destinations": [{
        "latitude": 45.5347,
        "longitude": -122.6231
    }, 
    {
        "latitude": 47.4747,
        "longitude": -122.2057
    }],
    "travelMode": "driving"
}
```

**JSON Response**

```json
{
    "authenticationResultCode": "ValidCredentials",
    "brandLogoUri": "http:\/\/dev.virtualearth.net\/Branding\/logo_powered_by.png",
    "copyright": "Copyright © 2017 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",
    "resourceSets": [
        {
            "estimatedTotal": 1,
            "resources": [
                {
                    "__type": "DistanceMatrix:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",
                    "destinations": [
                        {
                            "latitude": 45.5347,
                            "longitude": -122.6231
                        },
                        {
                            "latitude": 47.4747,
                            "longitude": -122.2057
                        }
                    ],
                    "origins": [
                        {
                            "latitude": 47.6044,
                            "longitude": -122.3345
                        },
                        {
                            "latitude": 47.6731,
                            "longitude": -122.1185
                        },
                        {
                            "latitude": 47.6149,
                            "longitude": -122.1936
                        }
                    ],
                    "results": [
                        {
                            "destinationIndex": 0,
                            "originIndex": 0,
                            "travelDistance": 281.261777777778,
                            "travelDuration": 9560.7
                        },
                        {
                            "destinationIndex": 1,
                            "originIndex": 0,
                            "travelDistance": 23.284,
                            "travelDuration": 931.5
                        },
                        {
                            "destinationIndex": 0,
                            "originIndex": 1,
                            "travelDistance": 296.074722222222,
                            "travelDuration": 10203.1
                        },
                        {
                            "destinationIndex": 1,
                            "originIndex": 1,
                            "travelDistance": 28.4669444444444,
                            "travelDuration": 1155.6
                        },
                        {
                            "destinationIndex": 0,
                            "originIndex": 2,
                            "travelDistance": 285.752194444444,
                            "travelDuration": 9818.4
                        },
                        {
                            "destinationIndex": 1,
                            "originIndex": 2,
                            "travelDistance": 18.1444166666667,
                            "travelDuration": 770.9
                        }
                    ]
                }
            ]
        }
    ],
    "statusCode": 200,
    "statusDescription": "OK",
    "traceId": "cbe10c5972504e84abd9d9f921a604e2|BN20131519|7.7.0.0|"
}
```

**XML Response**

Add `&output=xml` to the URL above to get the XML response.

```xml
<?xml version="1.0" encoding="utf-8"?>
<Response xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">
  <Copyright>Copyright © 2017 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>
  <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>
  <StatusCode>200</StatusCode>
  <StatusDescription>OK</StatusDescription>
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>
  <TraceId>9eaa7048e9cc457c804c15bac083d8b7|BN20220145|7.7.0.0|</TraceId>
  <ResourceSets>
    <ResourceSet>
      <EstimatedTotal>1</EstimatedTotal>
      <Resources>
        <Resource xsi:type="DistanceMatrix">
          <Origins>
            <Coordinate>
              <Latitude>47.6044</Latitude>
              <Longitude>-122.3345</Longitude>
            </Coordinate>
            <Coordinate>
              <Latitude>47.6731</Latitude>
              <Longitude>-122.1185</Longitude>
            </Coordinate>
            <Coordinate>
              <Latitude>47.6149</Latitude>
              <Longitude>-122.1936</Longitude>
            </Coordinate>
          </Origins>
          <Destinations>
            <Coordinate>
              <Latitude>45.5347</Latitude>
              <Longitude>-122.6231</Longitude>
            </Coordinate>
            <Coordinate>
              <Latitude>47.4747</Latitude>
              <Longitude>-122.2057</Longitude>
            </Coordinate>
          </Destinations>
          <Results>
            <Distance>
              <DepartureTime xsi:nil="true" />
              <OriginIndex>0</OriginIndex>
              <DestinationIndex>0</DestinationIndex>
              <TravelDistance>281.261777777778</TravelDistance>
              <TravelDuration>9560.7</TravelDuration>
              <TotalWalkDuration>0</TotalWalkDuration>
            </Distance>
            <Distance>
              <DepartureTime xsi:nil="true" />
              <OriginIndex>0</OriginIndex>
              <DestinationIndex>1</DestinationIndex>
              <TravelDistance>23.284</TravelDistance>
              <TravelDuration>931.5</TravelDuration>
              <TotalWalkDuration>0</TotalWalkDuration>
            </Distance>
            <Distance>
              <DepartureTime xsi:nil="true" />
              <OriginIndex>1</OriginIndex>
              <DestinationIndex>0</DestinationIndex>
              <TravelDistance>296.074722222222</TravelDistance>
              <TravelDuration>10203.1</TravelDuration>
              <TotalWalkDuration>0</TotalWalkDuration>
            </Distance>
            <Distance>
              <DepartureTime xsi:nil="true" />
              <OriginIndex>1</OriginIndex>
              <DestinationIndex>1</DestinationIndex>
              <TravelDistance>28.4669444444444</TravelDistance>
              <TravelDuration>1155.6</TravelDuration>
              <TotalWalkDuration>0</TotalWalkDuration>
            </Distance>
            <Distance>
              <DepartureTime xsi:nil="true" />
              <OriginIndex>2</OriginIndex>
              <DestinationIndex>0</DestinationIndex>
              <TravelDistance>285.752194444444</TravelDistance>
              <TravelDuration>9818.4</TravelDuration>
              <TotalWalkDuration>0</TotalWalkDuration>
            </Distance>
            <Distance>
              <DepartureTime xsi:nil="true" />
              <OriginIndex>2</OriginIndex>
              <DestinationIndex>1</DestinationIndex>
              <TravelDistance>18.1444166666667</TravelDistance>
              <TravelDuration>770.9</TravelDuration>
              <TotalWalkDuration>0</TotalWalkDuration>
            </Distance>
          </Results>
        </Resource>
      </Resources>
    </ResourceSet>
  </ResourceSets>
</Response>
```

## See Also

* [Using the REST Services with .NET](../using-the-rest-services-with-net.md)
