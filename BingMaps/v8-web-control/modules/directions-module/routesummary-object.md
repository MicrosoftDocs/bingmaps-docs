---
title: "RouteSummary Object | Microsoft Docs"
description: Describes the RouteSummary object, which represents a route summary, and provides a list of route summary properties.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ca328710-1554-4dc8-9baf-ed5cf48702d0
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# RouteSummary Object

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../../includes/bing-maps-web-control-sdk-retirement.md)]

Represents a route summary.

|   Name          |   Type   |   Description                                                                                                                                                                          |
|-----------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `distance`        | number   | The total travel distance of the route, specified in the units set in the `distanceUnit` property of the [DirectionsRequestOptions](directionsrequestoptions-object.md).                                         |
| `monetaryCost` | number | The cost of the route. This property is only returned if the **routeMode** of the [DirectionsRequestOptions](directionsrequestoptions-object.md) is set to **transit** and the map culture is set to *ja-jp*. |
| `northEast`       | [Location](../../map-control-api/location-class.md) | The location of the northeast corner of bounding box that defines the best map view of the route.                                                                                      |
| `southWest`       | [Location](../../map-control-api/location-class.md) | The location of the southwest corner of bounding box that defines the best map view of the route.                                                                                      |
| `time`            | number   | The total travel time, in seconds, for the route.                                                                                                                                      |
| `timeWithTraffic` | number   | The total travel time, in seconds, taking into account traffic delays, for the route. This property is 0 if the `avoidTraffic` property of the [DirectionsRequestOptions](directionsrequestoptions-object.md) is set to **false**. |
