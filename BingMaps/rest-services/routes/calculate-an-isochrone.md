---
title: "Calculate an Isochrone | Microsoft Docs"
description: "This article describes the Bing Maps Isochrone API and outlines API limits, URL templates, template parameters with descriptions, an example that shows how to request an isochrone and HTTP status codes."
ms.custom: ""
ms.date: "05/21/2024"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 3aa37091-134f-4d16-8c1c-5085e52cd47b
caps.latest.revision: 7
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Calculate an Isochrone

> [!NOTE]
> **Bing Maps Calculate an Isochrone API retirement**
>
> Bing Maps Calculate an Isochrone API is deprecated and will be retired. Free (Basic) account customers can continue to use Bing Maps Calculate an Isochrone API until June 30th, 2025. Enterprise account customers can continue to use Bing Maps Calculate an Isochrone API until June 30th, 2028. To avoid service disruptions, all implementations using Bing Maps Calculate an Isochrone API will need to be updated to use Azure Maps [Route Range](/rest/api/maps/route/get-route-range) API by the retirement date that applies to your Bing Maps for Enterprise account type.
>
> Azure Maps is Microsoft's next-generation maps and geospatial services for developers. Azure Maps has many of the same features as Bing Maps for Enterprise, and more. To get started with Azure Maps, create a free [Azure subscription](https://azure.microsoft.com/free) and an [Azure Maps account](/azure/azure-maps/how-to-manage-account-keys#create-a-new-account). For more information about azure Maps, see [Azure Maps Documentation](/azure/azure-maps/). For migration guidance, see [Bing Maps Migration Overview](/azure/azure-maps/migrate-bing-maps-overview).

The Bing Maps Isochrone API provides time-specific, isoline polygons for the distance that is reachable from a given location and supports multiple modes of transportation (i.e. driving and public transit). Use this solution to plan the area that can be reached from a designated starting point within a set time period. The isoline polygon area, good for visualization, can be used to filter for spatial queries, which opens up a wide variety of applications for spatial filtering. Here are some additional examples of where you might use isochrones:

* **Store Locators** – Show me all locations that are within 10 minutes of a user.
* **Stolen Vehicle Recovery** – Where could a vehicle have travelled to since it was stolen.
* **Real Estate** – Limit search results such that only those that are within the users preferred commute preferences to work. For example, show me all homes that are within a 30-minute drive of work.
* **Job Search Sites** – Show all jobs that are within 45 minutes of my home when taking public transit.
* **Geofence Generation** – Generate a polygon that be used as a geofence that alerts users when they are within a certain travel time or distance of a location.
* **Field management** – Show me all workers who are within a 15-minute drive of a job.
* **Emergency Services Planning** – Where could an emergency vehicle travel too within 5, 10, and 15 minutes.

When you make a request by using one of the following URL templates, the response returns either a `IsochroneResponse` resource that contains the requested isochrone information or an `RouteProxyAsyncResult` resource which contains information on the asynchronous request that was made to calculate an isochrone. For more information about these resources, see [Isochrone Data](../routes/isochrone-data.md). You can also view the example URL and response values in the [Examples](calculate-an-isochrone.md#examples) section.

> [!NOTE]
> **Bing Maps Calculate an Isochrone Feature Changes**
>
> As of 9/30/2024, the Bing Maps `Calculate an Isochrone` service will no longer support the ability to use transit as a `travelMode`. To avoid service disruptions, modify your application by 9/30/2024.

For Calculate an Isochrone geographic availability, see the travelMode parameter below.

## API Limits

Requests to the Isochrone API can be done in one of two ways:

* Most requests can be made with a simple synchronous GET request. Recommended for shorter travel times less than 30 minutes and distances less than 15 miles (24 km).
* An asynchronous request can be made for lager isochrones. Larger isochrones take longer to be generated as the network of possible roads grows exponentially.

If you are not sure which one to use, it is recommended to use the asynchronous method as this will work for all scenarios.

**How asynchronous requests work**

See [Asynchronous Requests documentation](../common-parameters-and-types/asynchronous-requests.md).

## Supported HTTP Methods

GET, POST

## URL Template

[!INCLUDE [get-bing-map-key-note](../../includes/get-bing-map-key-note.md)]

**Synchronous GET Requests**

When making a GET request the URL should look something like this:

```url
https://dev.virtualearth.net/REST/v1/Routes/Isochrones?waypoint={waypoint}&maxtime={maxTime}&maxDistance={maxDistance}&timeUnit={timeUnit}&distanceUnit={distanceUnit}&dateTime={dateTime}&travelMode={travelMode}&key={BingMapsKey}
```

**Asynchronous GET Requests**

Creates a job to calculate an isochrone using an asynchronous GET request. This type of request is recommended when the `maxTime` parameter is more than 30 minutes or the `maxDistance` parameter is more than 15 miles (24 km). 

```url
http://dev.virtualearth.net/REST/v1/Routes/IsochronesAsync?waypoint={waypoint}&maxtime={maxTime}&maxDistance={maxDistance}&timeUnit={timeUnit}&distanceUnit={distanceUnit}&dateTime={dateTime}&travelMode={travelMode}&key={BingMapsKey}
````

**URL for checking Asynchronous request status (GET)**

The initial asynchronous response includes a `callbackUrl` property which contains the URL that can be used to check the status of the job. Alternatively, the callback URL can also be generated by appending the `requestId` that is returned in the initial asynchronous request along with the same Bing Maps key used, with the `IsochroneAsyncCallback` endpoint as shown below. The response from this request will indicate if the request is complete or not, if complete it will provide a *resultUrl* property which is a URL that can be used to download the results.

```url
https://dev.virtualearth.net/REST/v1/Routes/IsochronesAsyncCallback?requestId={requestId}&key={BingMapsKey}
```

**Synchronous POST Requests**

When making a POST request the URL should look something like this:

```url
https://dev.virtualearth.net/REST/v1/Routes/Isochrones?key={BingMapsKey}
```

**Asynchronous POST Requests**

Creates a job to calculate an isochrone using an asynchronous POST request. This type of request is recommended when the `maxTime` parameter is more than 30 minutes or the `maxDistance` parameter is more than 15 miles (24 km). 

```url
https://dev.virtualearth.net/REST/v1/Routes/IsochronesAsync?key={BingMapsKey}
````

## Template Parameters

The following is a list of parameters that are supported by the Isochrone API.

> [!NOTE]
> Additional parameters, such as output and JSON callback parameters, are found in [Output Parameters](../common-parameters-and-types/output-parameters.md).<br><br>An alias can be used for a URL parameter when making a GET request to shorten the length of the query parameter. For example, waypoint=47.610,-122.107 can be shortened to wp=47.610,-122.107.  

| Parameter   | GET Alias| Description  |
|-------------|--------|----------------|
| `waypoint`  | `wp`   | **Required**. The point around which the isochrone will be calculated. This can be specified as a Point or address. For more information about Point values, see [Location and Area Types](../common-parameters-and-types/location-and-area-types.md).<br/><br/>**Examples**:<br/><br/>waypoint=47.610,-122.107 \[Point\]<br/><br/>waypoint=1%20Microsoft%20Way%20Redmond%20WA \[address\] |
| `maxTime`   |        | **Required.** The maximum travel time in the specified time units in which the isochrone polygon is generated. Cannot be set when *maxDistance* is set. Maximum value is 60 minutes when using asynchronous requests.<br/><br/>**Example:** maxTime=10 |
| `timeUnit`  | `tu`   | **Optional.** The units in which the maxTime value is specified. One of the following values:<br/><br/> • **minute**<br/> • **second** \[default\]<br/><br/>**Example**: timeUnit=second  |
|`maxDistance`|`maxDis`| **Required for Driving and Walking.** The maximum travel distance in the specified distance units in which the isochrone polygon is generated. Cannot be set when *maxTime* is set. Distance based isochrones are not supported for transit.<br/><br/>**Example:** maxDistance=15 |
| `distanceUnit`| `du` | **Optional**. The units in which the maxDistance value is specified. One of the following values:<br/><br/> • **mile** or **mi**<br/> • **kilometer** or **km** \[default\]<br/><br/>**Example**: distanceUnit=mi |
| `dateTime`  | `dt`   | **Optional** **for time based Driving and Transit**. When a maxTime value is specified, predictive traffic data is used to calculate the best isochrone route for the specified date time. This is not supported for distanced based queries.<br/><br/>A string that contains the date and time formatted as a [DateTime](https://msdn.microsoft.com/library/03ybds8y.aspx) value. For information about the string representation options for DateTime values, see [DateTime.Parse Method (String)](https://msdn.microsoft.com/library/1k1skd40.aspx). <br/><br/>**Examples**:<br/><br/>dateTime=03/01/2011 05:42:00<br/><br/>dateTime=05:42:00 \[assumes the current day\]<br/><br/>dateTime=03/01/2011 \[assumes the current time\] |
| `optimize`  | `optmz`| **Optional.** Specifies what parameters to use to optimize the isochrone route. One of the following values:<br/><br/> • **distance**: The route is calculated to minimize the distance. Traffic information is not used. Use with maxDistance.<br/> • **time** [default]: The route is calculated to minimize the time. Traffic information is not used. Use with maxTime.<br/> • **timeWithTraffic**: The route is calculated to minimize the time and uses current or predictive traffic information depending on if a dateTime value is specified. Use with maxTime.<br/><br/>**Example:** optimize=distance |
| `travelMode`| `mode` | **Optional.** Indicates the which routing profile to snap the points to. Possible values:<br/><br/> • **driving** \[default\]<br/> • **walking**<br/> • **transit**<sup>1</sup><br/>• **truck** <br/><br/><br/>**Example:** travelMode=walking <br/><br /> **Note**: <br/><br/> For travelMode=truck, the vehicle attributes can be defined in the POST body. Please see the template POST body with vehicle attributes below this table. For more details about vehicle attributes, please check the [Calculate a Truck Route API doc](./calculate-a-truck-route.md). <br /><br /> **Geographic Availability**: <br /> -  `Driving` and `Walking` are available in routing markets seen in the [Geographic Coverage documentation](../../coverage/geographic-coverage.md) with the exception of China, Japan, and Korea. <br /> -  `Truck` is available in Truck Routing markets seen in the [Geographic Coverage documentation](../../coverage/geographic-coverage.md). <br /> -  `Transit` is available in markets seen in the [Transit Coverage documentation](../../coverage/transit-coverage/index.md). |

<sup>1</sup> `transit` will no longer be a valid `travelMode` as of 9/30/2024.

*Template POST body with vehicle attributes*

```json
{
    "waypoint":string,
    "distanceUnit": string,
    "travelMode": string,
    "optimize": string,
    "maxDistance" : number,
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

**Calculate an Isochrone (synchronous)**

The following example shows how to request an isochrone.

In this case, consider a delivery company that has some electric vehicles in their fleet that have a maximum range of 100 miles on a fully charged battery. The company would like to determine which customer delivery locations the electric vehicles can reach and return back to the shop without having to recharge the vehicle battery. The company can use the resulting isochrone to assign the electric vehicles to only customer deliveries that are within the isochrone polygon.

* maxDistance: 50 miles (100 miles roundtrip)
* distanceUnit: mile
* optimize: distance
* travelMode: driving
* waypoint: Delivery company's shop latitude/longitude

*HTTP GET Request URL*

```url
https://dev.virtualearth.net/REST/v1/Routes/Isochrones?waypoint=31.520759,-97.133597&maxDistance=50&distanceUnit=mile&optimize=distance&travelMode=driving&key={BingMapsKey}
```

For isochrones with specific vehicle attributes, below are the example POST request URLs.  

*URL Template for Synchronous POST  request*
```url
https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdev.virtualearth.net%2FREST%2Fv1%2FRoutes%2FIsochrones%3Fkey&amp;data=02%7C01%7Cyasong%40microsoft.com%7C08d8aa10e2be4c1c8a8e08d7825ab785%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637121198441257460&amp;sdata=Dz8aDorHqG7%2FgWFaaJmvEDamsVfP3lcuNAt%2Bf6SP7ug%3D&amp;reserved=0={BingMapsKey}
```

*Asynchronous POST request*

```url
https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdev.virtualearth.net%2FREST%2Fv1%2FRoutes%2FIsochronesAsync%3Fkey&amp;data=02%7C01%7Cyasong%40microsoft.com%7C08d8aa10e2be4c1c8a8e08d7825ab785%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637121198441257460&amp;sdata=8clzM%2Bk0HrDeBjlw2yhMMGQWFg%2FhL7fdmkYSRfge3Vc%3D&amp;reserved=0={BingMapsKey}
```

*Example POST Body with vehicle attributes*

```json
{
    "waypoint":"31.520759,-97.133597",
    "distanceUnit": "mile",
    "travelMode": "Truck",
    "optimize": "distance",
    "maxDistance" : 30,
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

To view the complete XML and JSON responses, see [Isochrone Example](../examples/isochrone-example.md).

**Calculate an Isochrone (asynchronous)**

The following example shows how to request an isochrone asynchronously.

In this case, consider a person that is looking to rent an apartment near their company's office and doesn’t want more than a 30 minute commute by car back home each evening. The resulting isochrone can be used to limit the apartment search to only apartment listings within that commute polygon.

* maxTime: 30 minutes
* TimeUnit: minute
* DateTime: 11/27/2017 (Monday) at 6 PM PST (UTC offset)
* TravelMode: Driving
* Waypoint:  Company's office address

*HTTP GET Request URL*

```url
http://dev.virtualearth.net/REST/v1/Routes/IsochronesAsync?waypoint=1%20Microsoft%20Way%20Redmond%20WA&maxTime=30&timeUnit=minute&dateTime=2017-11-27T18:00:00-08:00&travelMode=Driving&key={BingMapsKey}
```

Once the initial request is made a *requestId* will be returned. A *requestId* is a unique identifier for the asynchronous request. This can be used to monitor the status of the request until it is completed, at which point the response will include a *resultURl* property which the resulting isochrone can be downloaded from. The following URL checks that status of an asynchronous request that has a *requestId* of “90b07189-33d8-4cbf-866a-1bd5c5b4f474”.

```url
https://dev.virtualearth.net/REST/v1/Routes/IsochroneAsyncCallback?requestId=90b07189-33d8-4cbf-866a-1bd5c5b4f474&key={BingMapsKey}
```

The following image shows the resulting isochrone.

![BM_NewIsochrone30Minute](../media/newisochrone.png)

To view the complete XML and JSON responses, see [Isochrone Asynchronous Example](../examples/isochrone-asynchronous-example.md).

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

> [!TIP]
> When making an asynchronous request, if the *RouteProxyAsyncResult* *ErrorMessage* says "Timeout occurred", the likely cause is that the maximum time or distance values in the request are too large and is resulting in a timeout on the server when calculating the isochrone.

## See Also

* [Using the REST Services with .NET](../using-the-rest-services-with-net.md)
* [Isochrone Data](isochrone-data.md)
* [Isochrone Example](../examples/isochrone-example.md)
* [Isochrone Asynchronous Example](../examples/isochrone-asynchronous-example.md)
