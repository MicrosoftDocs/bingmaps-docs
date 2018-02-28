---
title: "Waypoint Class4 | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 45ab6a81-68ca-467c-bd60-a782e9ef42cc
caps.latest.revision: 5
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Waypoint Class
In order to calculate a route between locations you need to first add all the locations as Waypoints to the [DirectionsManager](https://msdn.microsoft.com/library/mt750375.aspx). When creating an instance of the Waypoint class you must pass in an object containing [WaypointOptions](https://msdn.microsoft.com/library/mt750368.aspx).

## Constructor

> `Waypoint(options: WaypointOptions)`

## Methods

| Name                                    | Type | Description                                                                  |
|-----------------------------------------|----------|--------------------------------------------------------------------------|
| `dispose()`                             |          | Releases any resources associated with the waypoint.                     |
| `getAddress()`                          | string   | Returns the address associated with the waypoint.                        |
| `getLocation()`                         | [Location](Location%20Class.md) | Returns the location of the waypoint.             |
| `isViapoint()`                          | boolean  | Returns a boolean value indicating whether the waypoint is a via point. A via point is a location that your route is guaranteed to pass through. There can be multiple via points between two stop points. |
| setOptions(options: [WaypointOptions](https://msdn.microsoft.com/library/mt750368.aspx) |          | Sets options for the waypoint. For these options to take effect, you must recalculate the route.    