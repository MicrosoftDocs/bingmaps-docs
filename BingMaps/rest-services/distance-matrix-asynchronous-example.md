---
title: "Distance Matrix Asynchronous Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 3de6ca6f-257b-4577-9424-39058bc473c9
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Distance Matrix Asynchronous Example
This example returns a simple driving based distance matrix for the set of origins and destinations for a specified time, June 15<sup>th</sup>, 2017 at 1PM PST. This request will automatically use predictive traffic data to provide accurate estimates. This example shows the complete asynchronous request process from the initial request, and checking the status until completed. Both a GET and its equivalent POST request are shown. Responses are shown for both XML and JSON formats.

**HTTP GET Request URL**

```
https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrixAsync?origins=47.6044,-122.3345;47.6731,-122.1185;47.6149,-122.1936&destinations=45.5347,-122.6231;47.4747,-122.2057&travelMode=driving&startTime=2017-06-15T13:00:00-07:00&key=BingMapsKey
```

**HTTP POST Request URL**

```
https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrixAsync?key=BingMapsKey
```

HTTP POST Header

```
Content-Length: 497
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
    "startTime": "2017-06-15T13:00:00-07:00"
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
                    "callbackInSeconds": 10,
                    "callbackUrl": "https:\/\/dev.virtualearth.net\/REST\/v1\/Routes\/DistanceMatrixAsyncCallback?key= xxxxxxxxxxxxxxxxxx&requestId=9d721ef1-8ae1-4aef-a9b3-9badf01b4b1d",
                    "isAccepted": true,
                    "requestId": "9d721ef1-8ae1-4aef-a9b3-9badf01b4b1d"
                }
            ]
        }
    ],
    "statusCode": 200,
    "statusDescription": "OK",
    "traceId": "b0d0126ef8984228b21d37194fbf72a7|BN20121764|7.7.0.0|"
}
```

**XML Response**

Add `&output=xml` to the URL above to get the XML response.

```xml
<?xml version="1.0" encoding="utf-8"?><Response xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">
  <Copyright>Copyright © 2017 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>
  <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>
  <StatusCode>200</StatusCode>
  <StatusDescription>OK</StatusDescription>
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>
  <TraceId>cc062945da9d46a58717cffb4b5fb019|BN20190653|7.7.0.0|</TraceId>
  <ResourceSets>
    <ResourceSet>
      <EstimatedTotal>1</EstimatedTotal>
      <Resources>
        <Resource xsi:type="DistanceMatrixAsyncStatus">
          <IsAccepted>true</IsAccepted>
          <IsCompleted>false</IsCompleted>
          <CallbackInSeconds>10</CallbackInSeconds>
          <CallbackUrl>https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrixAsyncCallback?key=xxxxxxxxxxxxxxxxxxxxxxxxxxxx&amp;requestId=af2ee392-cb20-42f4-80e8-24c0e4e46529</CallbackUrl>
          <RequestId>9d721ef1-8ae1-4aef-a9b3-9badf01b4b1d</RequestId>
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
https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrixAsyncCallback?requestId=9d721ef1-8ae1-4aef-a9b3-9badf01b4b1d&key=BingMapsKey
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
                    "callbackUrl": "https:\/\/dev.virtualearth.net\/REST\/v1\/Routes\/DistanceMatrixAsyncCallback?key=xxxxxxxxxxxxxxxxxxxxxxxxxxxx&requestId=9d721ef1-8ae1-4aef-a9b3-9badf01b4b1d",
                    "isAccepted": true,
                    "isCompleted": true,
                    "requestId": "9d721ef1-8ae1-4aef-a9b3-9badf01b4b1d",
                    "resultUrl": "https:\/\/routematrix.blob.core.windows.net\/finalresults\/9d721ef1-8ae1-4aef-a9b3-9badf01b4b1d"
                }
            ]
        }
    ],
    "statusCode": 200,
    "statusDescription": "OK",
    "traceId": "165140fdda774fa9bded630f97cd96e5|BN20121764|7.7.0.0|"
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
  <TraceId>e08a8dc9cea749e1ac165a4a38a9fea8|BN20130621|7.7.0.0|</TraceId>
  <ResourceSets>
    <ResourceSet>
      <EstimatedTotal>1</EstimatedTotal>
      <Resources>
        <Resource xsi:type="DistanceMatrixAsyncStatus">
          <IsAccepted>true</IsAccepted>
          <IsCompleted>true</IsCompleted>
          <CallbackInSeconds>-1</CallbackInSeconds>
          <CallbackUrl>https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrixAsyncCallback?key=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&amp;requestId=9d721ef1-8ae1-4aef-a9b3-9badf01b4b1d</CallbackUrl>
          <RequestId>9d721ef1-8ae1-4aef-a9b3-9badf01b4b1d</RequestId>
          <ResultUrl>https://routematrix.blob.core.windows.net/finalresults/af2ee392-cb20-42f4-80e8-24c0e4e46529</ResultUrl>
        </Resource>
      </Resources>
    </ResourceSet>
  </ResourceSets>
</Response>
```

## Downloaded Results

When an asynchronous distance matrix request has completed, the status response will include a `resultUrl` field which can be used to download the requested distance matrix result. The following is the distance matrix result that would be downloaded when using the `resultUrl`. The downloaded distance matrix results are only available in JSON format.

**JSON Response**

```json
{
    "origins": [
        {
            "latitude": 47.6044,
            "longitude": -122.3345
        }, {
            "latitude": 47.6731,
            "longitude": -122.1185
        }, {
            "latitude": 47.6149,
            "longitude": -122.1936
        }
    ],
    "destinations": [
        {
            "latitude": 45.5347,
            "longitude": -122.6231
        }, {
            "latitude": 47.4747,
            "longitude": -122.2057
        }
    ],
    "results": [
        {
            "originIndex": 1,
            "destinationIndex": 1,
            "travelDistance": 28.43,
            "travelDuration": 1318,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T20:00:00.0000000+00:00"
        }, {
            "originIndex": 1,
            "destinationIndex": 0,
            "travelDistance": 296.035,
            "travelDuration": 11618,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T20:00:00.0000000+00:00"
        }, {
            "originIndex": 0,
            "destinationIndex": 1,
            "travelDistance": 23.269,
            "travelDuration": 1209,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T20:00:00.0000000+00:00"
        }, {
            "originIndex": 0,
            "destinationIndex": 0,
            "travelDistance": 281.244,
            "travelDuration": 10893,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T20:00:00.0000000+00:00"
        }, {
            "originIndex": 2,
            "destinationIndex": 1,
            "travelDistance": 18.064,
            "travelDuration": 854,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T20:00:00.0000000+00:00"
        }, {
            "originIndex": 2,
            "destinationIndex": 0,
            "travelDistance": 285.669,
            "travelDuration": 11153,
            "totalWalkDuration": 0,
            "hasError": false,
            "departureTime": "2017-06-15T20:00:00.0000000+00:00"
        }
    ]
}
```

## See Also

-   [Using the REST Services with .NET](../rest-services/using-the-rest-services-with-net.md)
