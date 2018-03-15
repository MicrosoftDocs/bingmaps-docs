---
title: "Distance Matrix Data | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 4cefabbb-cb16-42b0-8016-8c97b9e5c44d
caps.latest.revision: 6
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Distance Matrix Data
The response returned when making an asynchronous request to the Distance Matrix API contains a `DistanceMatrixAsyncStatus` resource which provides information on the status of the request.

The response returned when making a synchronous request to the Distance Matrix API contains a `DistanceMatrix` resource. The information provided in the `DistanceMatrix` resource includes an array of results which correspond to each origin and destination pair in the request. If the request was made asynchronously, the response would provide a request id which can be used to query the status of the asynchronous request.

The following tables provide the descriptions of the `DistanceMatrix` and `DistanceMatrixAsyncStatus` resource fields.

For more information about the common response container for the Bing Maps REST Services, see [Common Response Description](../rest-services/common-response-description.md).

## DistanceMatrixAsyncStatus Resource

A `DistanceMatrixAsyncStatus` resource is returned as a response when making a `DistanceMatrixAsync` request. This resource provides the status of an asynchronous distance matrix request which includes an estimated amount of time left to process the request, the unique `requestId` to use when checking the status, as well as information on if the request was had any errors or not.

| JSON              | XML               | Type    | Description   |
|-------------------|-------------------|---------|---------------|
| callbackInSeconds | CallbackInSeconds | integer | An estimated number of seconds remaining to complete the request. Wait this long before checking the status again. |
| callbackUrl       | CallbackUrl       | string  | The callback URL to use to check the status of the request. |
| isAccepted        | IsAccepted        | boolean | Specifies if the request is accepted. A request will not be accepted if it is not valid, or is not within the coordinate pair limits. |
| isCompleted       | IsCompleted       | boolean | Specifies is the request has completed. |
| requestId         | RequestId         | string  | A unique identifier for an asynchronous request. This can be used to retrieve the results of an asynchronous request when it has completed. |
| resultUrl         | ResultUrl         | string  | When completed, this field will be populated with a URL which can be used to download the results. The downloaded results will be a `DistanceMatrix` resource in JSON format. XML support will be coming soon. |

## DistanceMatrix Resource

The following tables describe the fields in the `DistanceMatrix` resource in a hierarchical manner.

A distance matrix has the following basic structure:

* DistanceMatrix \[one\]
    * DistanceMatrixCell \[For each origin-destination pair and time interval\]

### Top-level Distance Matrix Resource Fields

The following fields are the top-level fields in the `DistanceMatrix` resource. Additional tables describe the fields in each cell of array of results.

| JSON         | XML          | Type                   | Description                                                                                              |
|--------------|--------------|------------------------|----------------------------------------------------------------------------------------------------------|
| destinations | Destinations | Coordinate\[\]         | The array of destinations that were used to calculate the distance matrix.                               |
| origins      | Origins      | Coordinate\[\]         | The array of destinations that were used to calculate the distance matrix.                               |
| result       | Result       | DistanceMatrixCell\[\] | Array of distance matrix cell results containing information for each coordinate pair and time interval. |

### Distance Matrix Cell Fields

These fields are specific to the array of `DistanceMatrixCells` in the `DistanceMatrix` resource.

| JSON             | XML              | Type    | Description   |
|------------------|------------------|---------|---------------|
| departureTime    | DepartureTime    | string  | The departure time in which this cell was calculated for. Only returned when a `startTime` is specified. When an `endTime` is specified in the request several cells will be returned for the same origin and destination pairs, each having a different departure time for each time interval in the generated histogram request. This string is in [ISO 8601 date format](https://en.wikipedia.org/wiki/ISO_8601).<br/><br/>**Example**: 2017-09-22T19:27:03.0000000+00:00 |
| destinationIndex | DestinationIndex | int     | The index of the destination in the provided destinations array used to calculate this cell. |
| hasError         | HasError         | boolean | A boolean indicating if an error occurred when calculating this cell. |
| originIndex      | OriginIndex      | int     | The index of the origin in the provided origins array used to calculate this cell. |
| travelDistance   | TravelDistance   | double  | The physical distance covered to complete a route between the origin and destination. Currently all distances returned are in kilometers. When travel mode is set to transit or a path between the origin and destination can't be calculated, this value is set to -1. |
| travelDuration   | TravelDuration   | double  | The time that it takes, in the specified time units, to travel a corresponding `TravelDistance`. If a path a path between the origin and destination can't be calculated, this value will be a negative number. |
| totalWalkDuration | TotalWalkDuration | double | The portion of the total route duration which requires walking. This may occur when the travel mode is set to transit. |

## Coordinate Field

These fields are used to represent a location coordinate.

| JSON      | XML       | Type   | Description                                  |
|-----------|-----------|--------|----------------------------------------------|
| latitude  | Latitude  | double | The latitude information of the coordinate.  |
| longitude | Longitude | double | The longitude information of the coordinate. |

## See Also

* [Using the REST Services with .NET](../rest-services/using-the-rest-services-with-net.md)
* [Distance Matrix Example](../rest-services/distance-matrix-example.md)
* [Distance Matrix Asynchronous Example](../rest-services/distance-matrix-asynchronous-example.md)
* [Distance Matrix Histogram Example](../rest-services/distance-matrix-histogram-example.md)
