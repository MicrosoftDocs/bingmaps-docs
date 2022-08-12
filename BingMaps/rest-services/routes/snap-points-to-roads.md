---
title: "Snap Points to Roads | Microsoft Docs"
description: "This article describes the Bing Maps Snap to Road API and provides URL templates, API limits, template parameters, and examples."
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
ms.service: "bing-maps"
---

# Snap Points to Roads

The Bing Maps Snap to Road API takes GPS point data, in the form of latitudes and longitudes, and returns a list of objects that form a route snapped to the roads on a map. The information returned on the road segments, include the names of the roads that the GPS points are associated with and their posted speed limits. You can also interpolate the GPS points, resulting in a route that smoothly follows the geometry of the road for map display purposes, which is a valuable feature when tracking assets and for data visualization.

When you make a request by using one of the following URL templates, the response returns a `SnapToRoadResponse` resource that contains the requested snapped coordinate information. For more information about the `SnapToRoadResponse` resource, see [Snap to Road Data](snap-to-road-data.md). You can also view the example URL and response values in the **Examples** section.

The algorithm that powers the Bing Maps Snap to Road API is based on [this great paper](https://www.microsoft.com/research/publication/hidden-markov-map-matching-noise-sparseness/) written by Microsoft Research.

For Snap Points to Roads geographic availability, see the travelMode parameter below.

## API Limits

Requests to the Snap to Road API can be done in one of two ways:

* Synchronous requests can be made with up to 100 points.
* Asynchronous requests can be made with up to 1,000 points. It is recommended to make this request using POST when passing in more than 100 points. 

If you are not sure which one to use, it is recommended to use the asynchronous method as this will work for all scenarios.

> [!Note]
> The GPS points must be within 2.5 kilometer of each other.

**How asynchronous requests work**  

See [Asynchronous Requests documentation](../common-parameters-and-types/asynchronous-requests.md).

## Supported HTTP Methods

GET, POST

POST requests require all parameters to be passed into the body of the request as a JSON object. This API is [CORs enabled](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing).

**When to use HTTP GET vs POST**

Many developers prefer the simplicity of HTTP GET requests which simply require generating a URL. However, browsers and servers have limits on the maximum length that URLs can be. Typically, it is best to keep your URLs under 2083 characters in length. With this in mind, it is recommended to only use HTTP GET requests when your request has less than a hundred points.

## URL Template

[!INCLUDE [get-bing-map-key-note](../../includes/get-bing-map-key-note.md)]

**Synchronous GET Requests**

When making a GET request the URL should look something like this:

```url
http://dev.virtualearth.net/REST/v1/Routes/SnapToRoad?points={points}&interpolate={interpolate}&includeSpeedLimit={includeSpeedLimit}&includeTruckSpeedLimit={includeTruckSpeedLimit}&speedUnit={speedUnit}&travelMode={travelMode}&key={BingMapsKey}
```

URI parameter alias’s will be supported only for GET requests.

**Synchronous POST requests**

*HTTP POST Request URL*

```url
https://dev.virtualearth.net/REST/v1/Routes/SnapToRoad?key={BingMapsKey}
```

*POST Header*

```url
Content-Length: insertLengthOfHTTPBody
Content-Type: application/json
```

*POST body*

```json
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

**Asynchronous GET Request URL**

```url
https://dev.virtualearth.net/REST/v1/Routes/SnapToRoadAsync?points={points}&interpolate={interpolate}&includeSpeedLimit={includeSpeedLimit}&includeTruckSpeedLimit={includeTruckSpeedLimit}&speedUnit={speedUnit}&travelMode={travelMode}&key={BingMapsKey}
```

**Asynchronous POST Request URL**

*HTTP POST Request URL*

```url
https://dev.virtualearth.net/REST/v1/Routes/SnapToRoadAsync?key={BingMapsKey}
```

*POST Header*

```url
Content-Length: insertLengthOfHTTPBody
Content-Type: application/json
```

*POST body*

```json
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

**URL for checking Asynchronous request status (GET)**

The initial asynchronous response includes a *callbackUrl* property which contains the URL that can be used to check the status of the job. Alternatively, the callback URL can also be generated by appending the *requestId* that is returned in the initial asynchronous request along with the same Bing Maps key used, with the **SnapToRoadAsyncCallback** endpoint as shown below. The response from this request will indicate if the request is complete or not, if complete it will provide a *resultUrl* property which is a URL that can be used to download the results.

```url
https://dev.virtualearth.net/REST/v1/Routes/SnapToRoadAsyncCallback?requestId={requestId}&key={BingMapsKey}
```

## Template Parameters

The following is a list of parameters that are supported by the Snap to Road API.

> [!Note]
> Additional parameters, such as output and JSON callback parameters, are found in [Output Parameters](../common-parameters-and-types/output-parameters.md).<br/><br/>An alias can be used for a URL parameter when making a GET request to shorten the length of the query parameter. For example, points=47.610,-122.107; can be shortened to pts=47.610,-122.107;.  

| Parameter              | GET Alias | Description  |
|------------------------|-------|--------------|
| `points`                 | pts   | **Required**. A set of points to snap to roads. If you have a large number of values, you can use the HTTP POST. Up to 100 points for synchronhous requests, and 1,000 points for asynchrnous requests.<br/><br/>For GET requests: lat0,lon0;lat1,lon1;...;latM,lonM<br/><br/>**Example**: points=37.77916,-122.42;32.71568,-117.16172;<br/><br/>For POST requests:<br/>\[{<br/>&nbsp;&nbsp;&nbsp;&nbsp;"latitude": lat0,<br/>&nbsp;&nbsp;&nbsp;&nbsp;"longitude": lon0<br/>},<br/>{<br/>&nbsp;&nbsp;&nbsp;&nbsp;"latitude": lat1,<br/>&nbsp;&nbsp;&nbsp;&nbsp;"longitude": lon1<br/>},<br/>.<br/>.<br/>.<br/>{<br/>&nbsp;&nbsp;&nbsp;&nbsp;"latitude": latN,<br/>&nbsp;&nbsp;&nbsp;&nbsp;"longitude": lonN<br/>}\]<br/><br/>**Example:**<br/><br/>"points": \[{<br/>&nbsp;&nbsp;&nbsp;&nbsp;"latitude": 37.77916,<br/>&nbsp;&nbsp;&nbsp;&nbsp;"longitude": -122.42<br/>},<br/>{<br/>&nbsp;&nbsp;&nbsp;&nbsp;"latitude": 32.71568,<br/>&nbsp;&nbsp;&nbsp;&nbsp;"longitude": -117.16172<br/>}\]                                                                                                                                                                              |
| `interpolate`            | intpl | **Optional**. Indicates if the space between the snapped points should be filled with additional points along the road, thus returning the full route path. Default: **false**<br/><br/>**Example**: interpolate=true                                                                                                                                                   |
| `includeSpeedLimit`      | spdl  | **Optional**. Indicates if speed limitation data should be returned for the snapped points. Default: **false**<br/><br/>**Example**: includeSpeedLimit=true                                                                                                                                             |
| `includeTruckSpeedLimit` | tspdl | **Optional.** Indicates if speed limitation data should be returned for the snapped points. Default: **false**<br/><br/>**Example**: includeTruckSpeedLimit=true                                                                                                                                        |
| `speedUnit`              | spu   | **Optional.** Indicates the units in which the returned speed limit data is in. Possible values:<br/><br/> • **MPH** – Miles per hour<br/> • **KPH** – Kilometers per hour \[default\]<br/><br/>**Example**: speedUnit=MPH |
| `travelMode`             | mode  | **Optional.** Indicates which routing profile to snap the points to. Possible values:<br/><br/> • **driving** \[default\]<br/> • **walking** <br/><br/>**Example:** travelMode=driving <br/><br /> **Note**: <br/><br/> For trucks, the vehicle attributes can be defined in the POST body. Please see the template POST body with vehicle attributes below this table. <br /><br /> For more details about vehicle attributes, please check the Calculate a Truck Route API doc: /bingmaps/rest-services/routes/calculate-a-truck-route. <br /><br /> **Geographic Availability**: <br /> -  `Driving` and `Walking` available in routing markets seen in the [Geographic Coverage documentation](../../coverage/geographic-coverage.md) with the exception of China, Japan, and Korea. <br />-  `Truck` is available in markets seen in the [Geographic Coverage documentation](../../coverage/geographic-coverage.md).|

*Template POST body with vehicle attributes*
```json
{
    "points": [{
        "latitude": number,
        "longitude": number
    }],
    "interpolate": bool,
    "includeSpeedLimit": bool,
    "includeTruckSpeedLimit": bool,
    "speedUnit": string,
    "travelMode": string,
    "vehicleSpec": {
        "dimensionUnit": string,
        "weightUnit": string,
        "vehicleHeight": number,
        "vehicleWidth": number,
        "vehicleLength": number,
        "vehicleWeight": number,
        "vehicleAxles": number,
        "vehicleTrailers": number,
        "vehicleSemi": bool,
        "vehicleMaxGradient": number,
        "vehicleMinTurnRadius": number,
        "vehicleAvoidCrossWind": bool,
        "vehicleAvoidGroundingRisk": bool,
        "vehicleHazardousMaterials": string,
        "vehicleHazardousPermits": string
    }
}
```

## Examples

**Snap points to road**

The following example shows how to snap points to the road.

In this case, consider a trucking company that wants to do periodic safety reviews of the routes that their truck drivers take. The trucks have built-in GPS devices that collect GPS points as the truck drives along its route. The company wants to snap the GPS points to the likely road taken for accuracy because often times collected GPS points can deviate from the actual road the driver was on due to occasional GPS signal interference (i.e.: trees, buildings, etc.). The company also wants to get the posted truck speed limit of the road that the truck was on to compare to the actual speed the driver was travelling.

*HTTP GET Request URL*

```url
https://dev.virtualearth.net/REST/v1/Routes/SnapToRoad?points=47.590868,-122.336729;47.601604,-122.336042;47.60849,-122.34241;47.610568,-122.345064&includeTruckSpeedLimit=true&IncludeSpeedLimit=true&speedUnit=MPH&travelMode=driving&key={BingMapsKey}
```

*HTTP POST Request URL*

```url
https://dev.virtualearth.net/REST/v1/Routes/SnapToRoad?key={BingMapsKey}
```

*HTTP POST Header*

```url
Content-Length: 402
Content-Type: application/json
```

*HTTP POST Body*

```json
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

Below is an example of HTTP POST Body with vehicle spec:

```json
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
    "travelMode": "driving",
    "vehicleSpec": {
        "vehicleHeight": 10,
        "vehicleWidth": 12,
        "vehicleLength": 20,
        "vehicleWeight": 5000,
        "vehicleAxles": 2,
        "vehicleTrailers": 1
    }
}

```

Notice that both standard and truck speed limits are requested in this query. The reason for this is few roads have posted truck speed limits, when there is no posted truck speed limit the value returned will be 0. When this occurs, the standard posted speed limit is assumed to also apply to trucks as well.

To view the complete XML and JSON responses, see [Snap to Road Example](../examples/snap-to-road-example.md).

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

* [Using the REST Services with .NET](../using-the-rest-services-with-net.md)
* [Snap to Road Example](../examples/snap-to-road-example.md)
