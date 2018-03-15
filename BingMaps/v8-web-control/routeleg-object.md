---
title: "RouteLeg Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 46590a2f-9229-4f64-a008-9ab5bcba0658
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# RouteLeg Object
Represents a leg of a route. A route leg is the part of the route between two stop waypoints.

|   Name                |   Type             |   Description                                                              |
|-----------------------|--------------------|----------------------------------------------------------------------------|
| endTime               | Date           | The end time of the route leg. This property only applies when the routeMode of the DirectionsRequestOptions is set to **transit**.           |
| endWaypointLocation   | [Location](../v8-web-control/location-class.md) | The location of the last waypoint of this leg.                |
| itineraryItems        | [DirectionsStep](../v8-web-control/directionsstep-object.md)\[\] | The directions steps associated with this route leg.                                                                                          |
| originalRouteIndex    | number             | The index of the route to which this route leg belongs.                    |
| startTime             | Date           | The start time of the route leg. This property only applies when the routeMode of the DirectionsRequestOptions is set to **transit**.         |
| startWaypointLocation | [Location](../v8-web-control/location-class.md) | The location of the first waypoint of this route leg.         |
| subLegs               | [RouteSubLeg](../v8-web-control/routesubleg-object.md)\[\]    | The sub legs of this route leg. A sub leg of a route is the part of the route between a stop point and a via point or between two via points. |
| summary               | [RouteSummary](../v8-web-control/routesummary-object.md) | The summary which describes this route leg.          |
