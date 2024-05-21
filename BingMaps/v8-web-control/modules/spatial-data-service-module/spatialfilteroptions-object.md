---
title: "SpatialFilterOptions Object | Microsoft Docs"
description: Describes the SpatialFilterOptions object, which represents spatial filter options for querying a data source hosted in the Bing Spatial Data Services and provides a list of the object's properties.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 37824105-392f-481e-8519-0dc9f513d55d
caps.latest.revision: 7
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# SpatialFilterOptions Object

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../../includes/bing-maps-web-control-sdk-retirement.md)]

Represents the spatial filter options for querying a data source that is hosted in the Bing Spatial Data Services.

## Properties

Name                    | Type                       | Description                              |
----------------------- | -------------------------- | ----------------------------------
spatialFilterType       | string                     | **Required**. One of the following values:<br/><br/>&nbsp; • **nearby** – Searches in a radius around a location.<br/>&nbsp; • **nearRoute** – Searches for results that are within 1 mile of a route.<br/>&nbsp; • **intersects** – Searches for results that intersect with the specified geometry.<br/><br/>**Note**: Note that the NavteqNA and NavteqEU data sources only support nearby queries. 
location                | string _or_ [Location](../../map-control-api/location-class.md)       | Location at which the filter should be applied (only for **nearby filter**).
radius                  | number                     | Radius to use when performing a nearby search.  The distance in kilometers and must be between 0.16 and 1000 kilometers. (only for **nearby filter**).
start                   | string _or_ [Location](../../map-control-api/location-class.md)       | Start location of the route (only for **nearRoute filter**)
end                     | string _or_ [Location](../../map-control-api/location-class.md)       | End location of the route (only for **nearRoute filter**).
intersects              | string _or_ [LocationRect](../../map-control-api/locationrect-class.md) _or_ [IPrimitive](../../map-control-api/iprimitive-class.md) | Intersection object. Can be a well known text string or a LocationRect object.  (only for **intersects filter**).

If performing a **nearRoute** query the following additional properties may optionally also be specified in in the **SpatialFilterOptions** object.

| Name                    | Type       | Description                                          |
|-------------------------|------------|------------------------------------------------------|
| avoid                   | string\[\] | A list of values that limit the use of highways and toll roads in the route. Supported values:<br/><br/>&nbsp; • **highways** - Avoids the use of highways in the route.<br/>&nbsp; • **tolls** - Avoids the use of toll roads in the route.<br/>&nbsp; • **minimizeHighways** - Minimizes (tries to avoid) the use of highways in the route.<br/>&nbsp; • **minimizeTolls** - Minimizes (tries to avoid) the use of toll roads in the route.  |
| distanceBeforeFirstTurn | number     | An integer distance specified in meters. Use this parameter to make sure that the moving vehicle has enough distance to make the first turn. |
| heading                 | number     | An integer value between 0 and 359 that represents degrees from north where north is 0 degrees and the heading is specified clockwise from north. For example, setting the heading of 270 degrees creates a route that initially heads west.   |
| optimize                | string     | The optimization setting for the route calculation. One of the following values:<br/><br/>&nbsp; • **distance** - The route is calculated to minimize the distance. Traffic information is not used.<br/>&nbsp; • **time** - The route is calculated to minimize the time. Traffic information is not used.<br/>&nbsp; • **timeWithTraffic** - The route is calculated to minimize the time and uses current traffic information.<br/><br/>Default: **time**. |
| travelMode              | string     | The type of directions to calculate. One of the following values:<br/><br/>&nbsp; • **Driving**<br/>&nbsp; • **Walking**<br/><br/>Default: **Driving**.  |


> [!TIP]
> The Bing Maps Spatial Data Services does all distance calculations in kilometers. You can use the Distance conversion functionality in the [Spatial Math module](../spatial-math-module/index.md) if you prefer to work a different distance unit such as miles, meters, yards or feet.
