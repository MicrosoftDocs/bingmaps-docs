---
title: "DirectionsRequestOptions Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: b6a1007e-6349-480d-b7c1-f0172e7f79ac
caps.latest.revision: 6
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# DirectionsRequestOptions Object
You can set options for how to calculate the route by passing an object containing direction request options to the `setRequestOptions` method of the [DirectionsManager](../v8-web-control/directionsmanager-class.md). 

## Properties

| Name                | Type               | Description                          |
|---------------------|--------------------|--------------------------------------|
| `distanceUnit`      | [DistanceUnit](../v8-web-control/distanceunit-enumeration.md)  | The unit to use when displaying direction distances. The default value is based on the specified culture.            |
| `maxRoutes`         | number             | The number of routes to calculate. If the *routeMode* is; <br/><br/>&nbsp; •	Driving, up to 3 routes<br/>&nbsp; •	Walking, only 1 route is supported<br/>&nbsp; •	Transit, up to 6 routes <br/><br/>Default: **3**  |
| `routeAvoidance`    | [RouteAvoidance](../v8-web-control/routeavoidance-enumeration.md)\[\] | The features to avoid when calculating the route. Default: **none**                |
| `routeDraggable`    | boolean            | A boolean indicating whether the route line on the map can be dragged with the mouse cursor. Default: **true**<br/><br/>Truck based routes currently do not support being dragged.     |
| `routeIndex`        | number             | If multiple routes are returned, the index of the route and directions to display. |
| `routeMode`         | [RouteMode](../v8-web-control/routemode-enumeration.md) | The type of directions to calculate. Default: **driving**                          |
| `routeOptimization` | [RouteOptimization](../v8-web-control/routeoptimization-enumeration.md)  | The optimization setting for the route calculation. Default: **shortestTime**      |
| `time`              | Date               | The time to use when calculating the route. If this property is set to null, the current time is used. This option only affects driving and transit routes. |
| `timeType`          | [TimeTypes](../v8-web-control/timetypes-enumeration.md) | The type of the time specified. Default: **departure**<br/><br/>This option only affects transit routes, driving routes are always based on departure time.                    |
| `vehicleSpec` | [VehicleSpec](../v8-web-control/vehiclespec-object.md) | Specifies the vehicle attributes to use when calculating a truck route. |