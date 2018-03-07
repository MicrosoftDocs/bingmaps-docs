---
title: "Snap Points to Roads | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 74971c59-f5de-41f0-a8b0-40746c83e332
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Snap Points to Roads
The Bing Maps Snap to Road API takes GPS point data, in the form of latitudes and longitudes, and returns a list of objects that form a route snapped to the roads on a map. The information returned on the road segments, include the names of the roads that the GPS points are associated with and their posted speed limits. You can also interpolate the GPS points, resulting in a route that smoothly follows the geometry of the road for map display purposes, which is a valuable feature when tracking assets and for data visualization.

When you make a request by using one of the following URL templates, the response returns a `SnapToRoadResponse` resource that contains the requested snapped coordinate information. For more information about the `SnapToRoadResponse` resource, see [Snap to Road Data](../rest-services/snap-to-road-data.md). You can also view the example URL and response values in the **Examples** section.

The algorithm that powers the Bing Maps Snap to Road API is based on [this great paper](https://www.microsoft.com/en-us/research/publication/hidden-markov-map-matching-noise-sparseness/) written by Microsoft Research.

> ![Note]
> The GPS points must be within 2.5 kilometer of each other. 

## Supported HTTP Methods

GET, POST

## URL Template

> ![Note]
> These templates support both HTTP and HTTPS protocols. To use this API, you must have a [Bing Maps key](https://msdn.microsoft.com/library/ff428642). 

**GET Requests**

When making a GET request the URL should look something like this:

```
http://dev.virtualearth.net/REST/v1/Routes/SnapToRoad?points=points&interpolate=interpolate&includeSpeedLimit=includeSpeedLimit&includeTruckSpeedLimit=includeTruckSpeedLimit&speedUnit=speedUnit&travelMode=travelMode&key=BingMapsKey
```

URI parameter alias’s will be supported only for GET requests.

**POST requests**

*HTTP POST Request URL*

```
https://dev.virtualearth.net/REST/v1/Routes/SnapToRoad?key=BingMapsKey
```

*POST Header*

```
Content-Length: insertLengthOfHTTPBody
Content-Type: application/json
```

*POST body*

```
{
	"points": [{
		"latitude": number,
                             "longitude": number
	}],
	"interpolate": bool,
	"includeSpeedLimit": bool,
	"includeTruckSpeedLimit": bool,
	"speedUnit": string,
	"travelMode": string
}
```

## Template Parameters

The following is a list of parameters that are supported by the Snap to Road API.

> ![Note]
> Additional parameters, such as output and JSON callback parameters, are found in [Output Parameters](../rest-services/output-parameters.md).<br/><br/>An alias can be used for a URL parameter when making a GET request to shorten the length of the query parameter. For example, points=47.610,-122.107; can be shortened to pts=47.610,-122.107;.  

| Parameter              | Alias | Description                                                                                                                                                                    |
|------------------------|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| points                 | pts   | **Required**. A set of points to snap to roads. If you have a large number of values, you can use the HTTP POST. Up to 500 points for synchronhous requests, and 100,000 points for asynchrnous requests.<br/><br/>For GET requests: lat0,lon0;lat1,lon1;...;latM,lonM<br/><br/>**Example**: points=37.77916,-122.42;32.71568,-117.16172;<br/><br/>For POST requests:<br/>\[{<br/>&nbsp;&nbsp;&nbsp;&nbsp;"latitude": lat0,<br/>&nbsp;&nbsp;&nbsp;&nbsp;"longitude": lon0<br/>},<br/>{<br/>&nbsp;&nbsp;&nbsp;&nbsp;"latitude": lat1,<br/>&nbsp;&nbsp;&nbsp;&nbsp;"longitude": lon1<br/>},<br/>.<br/>.<br/>.<br/>{<br/>&nbsp;&nbsp;&nbsp;&nbsp;"latitude": latN,<br/>&nbsp;&nbsp;&nbsp;&nbsp;"longitude": lonN<br/>}\]<br/><br/>**Example:**<br/><br/>"points": \[{<br/>&nbsp;&nbsp;&nbsp;&nbsp;"latitude": 37.77916,<br/>&nbsp;&nbsp;&nbsp;&nbsp;"longitude": -122.42<br/>},<br/>{<br/>&nbsp;&nbsp;&nbsp;&nbsp;"latitude": 32.71568,<br/>&nbsp;&nbsp;&nbsp;&nbsp;"longitude": -117.16172<br/>}\]                                                                                                                                                                              |
| interpolate            | intpl | **Optional**. Indicates if the space between the snapped points should be filled with additional points along the road, thus returning the full route path. Default: **false**<br/><br/>**Example**: interpolate=true                                                                                                                                                   |
| includeSpeedLimit      | spdl  | **Optional**. Indicates if speed limitation data should be returned for the snapped points. Default: **false**<br/><br/>**Example**: includeSpeedLimit=true                                                                                                                                             |
| includeTruckSpeedLimit | tspdl | **Optional.** Indicates if speed limitation data should be returned for the snapped points. Default: **false**<br/><br/>**Example**: includeTruckSpeedLimit=true                                                                                                                                        |
| speedUnit              | spu   | **Optional.** Indicates the units in which the returned speed limit data is in. Possible values:<br/><br/> • **MPH** – Miles per hour<br/> • **KPH** – Kilometers per hour \[default\]<br/><br/>**Example**: speedUnit=MPH |
| travelMode             | mode  | **Optional.** Indicates which routing profile to snap the points to. Possible values:<br/><br/> • **driving** \[default\]<br/> • **walking** (coming soon)<br/><br/>**Example:** travelMode=driving |

## Examples

**Snap points to road**

The following example shows how to snap points to the road.

In this case, consider a trucking company that wants to do periodic safety reviews of the routes that their truck drivers take. The trucks have built-in GPS devices that collect GPS points as the truck drives along its route. The company wants to snap the GPS points to the likely road taken for accuracy because often times collected GPS points can deviate from the actual road the driver was on due to occasional GPS signal interference (i.e.: trees, buildings, etc.). The company also wants to get the posted truck speed limit of the road that the truck was on to compare to the actual speed the driver was travelling.

*HTTP GET Request URL*

```
https://dev.virtualearth.net/REST/v1/Routes/SnapToRoad?points=47.590868,-122.336729;47.601604,-122.336042;47.60849,-122.34241;47.610568,-122.345064&includeTruckSpeedLimit=true&IncludeSpeedLimit=true&speedUnit=MPH&travelMode=driving&key=BingMapsKey
```

*HTTP POST Request URL*

```
https://dev.virtualearth.net/REST/v1/Routes/SnapToRoad?key=BingMapsKey
```

*HTTP POST Header*

```
Content-Length: 402
Content-Type: application/json
```

*HTTP POST Body*

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

Notice that both standard and truck speed limits are requested in this query. The reason for this is few roads have posted truck speed limits, when there is no posted truck speed limit the value returned will be 0. When this occurs, the standard posted speed limit is assumed to also apply to trucks as well.

To view the complete XML and JSON responses, see [Snap to Road Example](../rest-services/snap-to-road-example.md).

## HTTP Status Codes

> ![Note]
> For more details about these HTTP status codes, see [Status Codes and Error Handling](../rest-services/status-codes-and-error-handling.md). 

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

* [Using the REST Services with .NET](../rest-services/using-the-rest-services-with-net.md)
* [Snap to Road Example](../rest-services/snap-to-road-example.md)
