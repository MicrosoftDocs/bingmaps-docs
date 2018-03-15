---
title: "Distance Matrix Histogram Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: b580ba7b-4b3b-4f7d-b27f-b856771ab2cc
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Distance Matrix Histogram Example
This example returns a distance matrix histogram between a set of origins and destinations between June 15<sup>th</sup>, 2017 at 1PM PST and June 15<sup>th</sup>, 2017 at 5PM PST with a resolution of 2 (30-minute intervals). This request will automatically use predictive traffic data to provide accurate estimates. This example shows the complete asynchronous request process from the initial request, as well as checking the status until completed. Both a GET and its equivalent POST request are shown. Responses are shown for both XML and JSON formats.

**HTTP GET Request URL**

```
https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrixAsync?origins=47.6044,-122.3345;47.6731,-122.1185;47.6149,-122.1936&destinations=45.5347,-122.6231;47.4747,-122.2057&travelMode=driving&startTime=2017-06-15T13:00:00-07:00&endTime=2017-06-15T17:00:00-7:00&resolution=2&key=BingMapsKey
```

**HTTP POST Request URL**

```
https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrixAsync?key=BingMapsKey
```

HTTP POST Header

```
Content-Length: 564
Content-Type: application/json
```

HTTP POST Body

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
    "travelMode": "driving",
    "startTime": "2017-06-15T13:00:00-07:00",
    "endTime": "2017-06-15T17:00:00-07:00",
    "resolution": 2
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
                    "__type": "DistanceMatrixAsyncStatus:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",
                    "callbackInSeconds": 80,
                    "callbackUrl": "https:\/\/dev.virtualearth.net\/REST\/v1\/Routes\/DistanceMatrixAsyncCallback?key=Ah_C8OJJu8wnNX50rGHf8_OYKonuhZ-CfLQ-kXS-4tI-QsTN9pkLPPfgZgKigwa8&requestId=df07c5b2-179c-4eb2-a392-bee2bd804ae8",
                    "isAccepted": true,
                    "requestId": "df07c5b2-179c-4eb2-a392-bee2bd804ae8"
                }
            ]
        }
    ],
    "statusCode": 200,
    "statusDescription": "OK",
    "traceId": "4fde4fc448f444acb96be305c2175347|BN20130721|7.7.0.0|"
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
  <TraceId>e45dcfa2744745a3a98f63d51fd1f6a0|BN20290118|7.7.0.0|</TraceId>
  <ResourceSets>
    <ResourceSet>
      <EstimatedTotal>1</EstimatedTotal>
      <Resources>
        <Resource xsi:type="DistanceMatrixAsyncStatus">
          <IsAccepted>true</IsAccepted>
          <CallbackInSeconds>80</CallbackInSeconds>
          <CallbackUrl>https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrixAsyncCallback?key=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&amp;requestId=df07c5b2-179c-4eb2-a392-bee2bd804ae8</CallbackUrl>
          <RequestId>df07c5b2-179c-4eb2-a392-bee2bd804ae8</RequestId>
          <ResultUrl />
        </Resource>
      </Resources>
    </ResourceSet>
  </ResourceSets>
</Response>
```

## Status Request

When making an asynchronous request to the distance matrix service the initial response includes a `DistanceMatrixAsyncStatus` which includes a unique `requestId`. This `requestId` can be used to check the status of the asynchronous distance matrix request by using the following HTTP GET URL. The response from the initial request and all responses using the following status request URL will include a field which indicates an estimated amount of time remaining until the requested distance matrix has been generated. The responses shown below in both XML and JSON formats are example of the status returned when the distance matrix request has been completed.

**HTTP GET Request URL**

```
https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrixAsyncCallback?requestId=df07c5b2-179c-4eb2-a392-bee2bd804ae8&key=BingMapsKey
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
                    "__type": "DistanceMatrixAsyncStatus:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",
                    "callbackInSeconds": -1,
                    "callbackUrl": "https:\/\/dev.virtualearth.net\/REST\/v1\/Routes\/DistanceMatrixAsyncCallback?key=Ah_C8OJJu8wnNX50rGHf8_OYKonuhZ-CfLQ-kXS-4tI-QsTN9pkLPPfgZgKigwa8&requestId=df07c5b2-179c-4eb2-a392-bee2bd804ae8",
                    "errorMessage": "Request accepted.",
                    "isAccepted": true,
                    "isCompleted": true,
                    "requestId": "df07c5b2-179c-4eb2-a392-bee2bd804ae8",
                    "resultUrl": "https:\/\/routematrix.blob.core.windows.net\/finalresults\/df07c5b2-179c-4eb2-a392-bee2bd804ae8"
                }
            ]
        }
    ],
    "statusCode": 200,
    "statusDescription": "OK",
    "traceId": "9b0da90d29444da7b166fe175a74af9d|BN20130721|7.7.0.0|"
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
  <TraceId>e45dcfa2744745a3a98f63d51fd1f6a0|BN20290118|7.7.0.0|</TraceId>
  <ResourceSets>
    <ResourceSet>
      <EstimatedTotal>1</EstimatedTotal>
      <Resources>
        <Resource xsi:type="DistanceMatrixAsyncStatus">
          <IsAccepted>true</IsAccepted>
          <IsCompleted>true</IsCompleted>
          <CallbackInSeconds>-1</CallbackInSeconds>
          <CallbackUrl>https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrixAsyncCallback?key=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&amp;requestId=df07c5b2-179c-4eb2-a392-bee2bd804ae8</CallbackUrl>
          <RequestId>df07c5b2-179c-4eb2-a392-bee2bd804ae8</RequestId>
          <ResultUrl>https://routematrix.blob.core.windows.net/finalresults/df07c5b2-179c-4eb2-a392-bee2bd804ae8<ResultUrl>
        </Resource>
      </Resources>
    </ResourceSet>
  </ResourceSets>
</Response>
```

## Downloaded Results

When an asynchronous distance matrix request has completed, the status response will include a `resultUrl` field can be used to download the requested distance matrix result. The following is the distance matrix result that would be downloaded when using the `resultUrl`. The downloaded distance matrix results are only available in JSON format.

**JSON Response**

```json
{
    "isAccepted": true,
    "isCompleted": true,
    "callbackInSeconds": -1,
    "requestId": "df07c5b2-179c-4eb2-a392-bee2bd804ae8",
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
    "results": [
        {
            "originIndex": 0,
            "destinationIndex": 1,
            "travelDistance": 23.269,
            "travelDuration": 1283,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T22:30:00.0000000+00:00"
        },
        {
            "originIndex": 1,
            "destinationIndex": 1,
            "travelDistance": 28.43,
            "travelDuration": 1334,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T23:30:00.0000000+00:00"
        },
        {
            "originIndex": 0,
            "destinationIndex": 1,
            "travelDistance": 23.269,
            "travelDuration": 1569,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T21:30:00.0000000+00:00"
        },
        {
            "originIndex": 1,
            "destinationIndex": 0,
            "travelDistance": 296.035,
            "travelDuration": 11968,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T23:00:00.0000000+00:00"
        },
        {
            "originIndex": 1,
            "destinationIndex": 1,
            "travelDistance": 28.43,
            "travelDuration": 2198,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T20:30:00.0000000+00:00"
        },
        {
            "originIndex": 0,
            "destinationIndex": 0,
            "travelDistance": 281.244,
            "travelDuration": 11218,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T22:30:00.0000000+00:00"
        },
        {
            "originIndex": 0,
            "destinationIndex": 1,
            "travelDistance": 23.269,
            "travelDuration": 1553,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T20:00:00.0000000+00:00"
        },
        {
            "originIndex": 2,
            "destinationIndex": 1,
            "travelDistance": 18.064,
            "travelDuration": 1705,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T21:00:00.0000000+00:00"
        },
        {
            "originIndex": 2,
            "destinationIndex": 0,
            "travelDistance": 285.669,
            "travelDuration": 12440,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T22:00:00.0000000+00:00"
        },
        {
            "originIndex": 1,
            "destinationIndex": 1,
            "travelDistance": 28.43,
            "travelDuration": 2144,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T20:00:00.0000000+00:00"
        },
        {
            "originIndex": 2,
            "destinationIndex": 1,
            "travelDistance": 18.064,
            "travelDuration": 1690,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T21:30:00.0000000+00:00"
        },
        {
            "originIndex": 0,
            "destinationIndex": 1,
            "travelDistance": 23.269,
            "travelDuration": 1607,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T20:30:00.0000000+00:00"
        },
        {
            "originIndex": 1,
            "destinationIndex": 1,
            "travelDistance": 28.43,
            "travelDuration": 1614,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T23:00:00.0000000+00:00"
        },
        {
            "originIndex": 0,
            "destinationIndex": 0,
            "travelDistance": 281.244,
            "travelDuration": 12946,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T20:30:00.0000000+00:00"
        },
        {
            "originIndex": 1,
            "destinationIndex": 0,
            "travelDistance": 296.035,
            "travelDuration": 12905,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T22:00:00.0000000+00:00"
        },
        {
            "originIndex": 0,
            "destinationIndex": 0,
            "travelDistance": 281.244,
            "travelDuration": 13083,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T20:00:00.0000000+00:00"
        },
        {
            "originIndex": 2,
            "destinationIndex": 1,
            "travelDistance": 18.064,
            "travelDuration": 1152,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T23:00:00.0000000+00:00"
        },
        {
            "originIndex": 1,
            "destinationIndex": 0,
            "travelDistance": 296.035,
            "travelDuration": 12392,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T22:30:00.0000000+00:00"
        },
        {
            "originIndex": 1,
            "destinationIndex": 0,
            "travelDistance": 296.035,
            "travelDuration": 11667,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T23:30:00.0000000+00:00"
        },
        {
            "originIndex": 0,
            "destinationIndex": 0,
            "travelDistance": 281.244,
            "travelDuration": 12696,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T21:00:00.0000000+00:00"
        },
        {
            "originIndex": 2,
            "destinationIndex": 1,
            "travelDistance": 18.064,
            "travelDuration": 1633,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T20:00:00.0000000+00:00"
        },
        {
            "originIndex": 2,
            "destinationIndex": 1,
            "travelDistance": 18.064,
            "travelDuration": 881,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T23:30:00.0000000+00:00"
        },
        {
            "originIndex": 0,
            "destinationIndex": 0,
            "travelDistance": 281.244,
            "travelDuration": 10967,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T23:00:00.0000000+00:00"
        },
        {
            "originIndex": 2,
            "destinationIndex": 0,
            "travelDistance": 285.669,
            "travelDuration": 13637,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T20:30:00.0000000+00:00"
        },
        {
            "originIndex": 1,
            "destinationIndex": 1,
            "travelDistance": 28.43,
            "travelDuration": 2243,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T21:30:00.0000000+00:00"
        },
        {
            "originIndex": 2,
            "destinationIndex": 0,
            "travelDistance": 285.669,
            "travelDuration": 11218,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T23:30:00.0000000+00:00"
        },
        {
            "originIndex": 1,
            "destinationIndex": 0,
            "travelDistance": 296.035,
            "travelDuration": 14219,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T20:00:00.0000000+00:00"
        },
        {
            "originIndex": 2,
            "destinationIndex": 0,
            "travelDistance": 285.669,
            "travelDuration": 12952,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T21:30:00.0000000+00:00"
        },
        {
            "originIndex": 0,
            "destinationIndex": 0,
            "travelDistance": 281.244,
            "travelDuration": 12318,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T21:30:00.0000000+00:00"
        },
        {
            "originIndex": 2,
            "destinationIndex": 0,
            "travelDistance": 285.669,
            "travelDuration": 13343,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T21:00:00.0000000+00:00"
        },
        {
            "originIndex": 2,
            "destinationIndex": 1,
            "travelDistance": 18.064,
            "travelDuration": 1504,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T22:30:00.0000000+00:00"
        },
        {
            "originIndex": 1,
            "destinationIndex": 1,
            "travelDistance": 28.43,
            "travelDuration": 1980,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T22:30:00.0000000+00:00"
        },
        {
            "originIndex": 0,
            "destinationIndex": 0,
            "travelDistance": 281.244,
            "travelDuration": 11730,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T22:00:00.0000000+00:00"
        },
        {
            "originIndex": 1,
            "destinationIndex": 0,
            "travelDistance": 296.035,
            "travelDuration": 13781,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T21:00:00.0000000+00:00"
        },
        {
            "originIndex": 0,
            "destinationIndex": 1,
            "travelDistance": 23.269,
            "travelDuration": 1230,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T23:00:00.0000000+00:00"
        },
        {
            "originIndex": 2,
            "destinationIndex": 1,
            "travelDistance": 18.064,
            "travelDuration": 1660,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T20:30:00.0000000+00:00"
        },
        {
            "originIndex": 2,
            "destinationIndex": 0,
            "travelDistance": 285.669,
            "travelDuration": 11511,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T23:00:00.0000000+00:00"
        },
        {
            "originIndex": 1,
            "destinationIndex": 0,
            "travelDistance": 296.035,
            "travelDuration": 14010,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T20:30:00.0000000+00:00"
        },
        {
            "originIndex": 0,
            "destinationIndex": 1,
            "travelDistance": 23.269,
            "travelDuration": 1600,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T21:00:00.0000000+00:00"
        },
        {
            "originIndex": 2,
            "destinationIndex": 1,
            "travelDistance": 18.064,
            "travelDuration": 1577,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T22:00:00.0000000+00:00"
        },
        {
            "originIndex": 2,
            "destinationIndex": 0,
            "travelDistance": 285.669,
            "travelDuration": 13782,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T20:00:00.0000000+00:00"
        },
        {
            "originIndex": 2,
            "destinationIndex": 0,
            "travelDistance": 285.669,
            "travelDuration": 11946,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T22:30:00.0000000+00:00"
        },
        {
            "originIndex": 1,
            "destinationIndex": 0,
            "travelDistance": 296.035,
            "travelDuration": 13281,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T21:30:00.0000000+00:00"
        },
        {
            "originIndex": 1,
            "destinationIndex": 1,
            "travelDistance": 28.43,
            "travelDuration": 2093,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T22:00:00.0000000+00:00"
        },
        {
            "originIndex": 0,
            "destinationIndex": 1,
            "travelDistance": 23.269,
            "travelDuration": 1203,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T23:30:00.0000000+00:00"
        },
        {
            "originIndex": 1,
            "destinationIndex": 1,
            "travelDistance": 28.43,
            "travelDuration": 2249,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T21:00:00.0000000+00:00"
        },
        {
            "originIndex": 0,
            "destinationIndex": 0,
            "travelDistance": 281.244,
            "travelDuration": 10926,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T23:30:00.0000000+00:00"
        },
        {
            "originIndex": 0,
            "destinationIndex": 1,
            "travelDistance": 23.269,
            "travelDuration": 1392,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T22:00:00.0000000+00:00"
        }
    ]
}
```

## See Also

-   [Using the REST Services with .NET](../rest-services/using-the-rest-services-with-net.md)
