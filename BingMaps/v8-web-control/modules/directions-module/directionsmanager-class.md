---
title: "DirectionsManager Class | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: da2358d8-e39f-4083-8bab-cd333d179c78
caps.latest.revision: 10
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# DirectionsManager Class
The DirectionsManager is the primary class in the Directions module. It contains methods for calculating directions and displaying a route on a map.

## Constructor
	
> `DirectionsManager(map:Map, waypoints?:Waypoint[])`

## Methods

| Name                                                 | Type                     | Description     |
|------------------------------------------------------|--------------------------|-----------------|
| addWaypoint(waypoint: [Waypoint](waypoint-class.md), index?: number)       | [Waypoint](waypoint-class.md) | Adds a waypoint to the route at the given index, if specified. If an index is not specified, the waypoint is added as the last waypoint in the route. The maximum number of walking or driving waypoints is 25. The maximum number of transit waypoints is 2. Up to 10 via points are allowed between two stop waypoints.<br/><br/>To recalculate the route, use `calculateDirections`.                                                                                     |
| `calculateDirections()`                              |                          | Calculates directions based on request and render options set (`setRequestOptions`, `setRenderOptions`) and the waypoints added (`addWaypoint`). The `directionsUpdated` event fires when the calculation is complete and the route is displayed on the map.<br/><br/>You must call this method after making any changes to the route options or waypoints for these changes to take effect. |
| `clearAll()`                                         |                          | Clears the directions results, request and render options and removes all waypoints.                                                           |
| `clearDisplay()`                                     |                          | Clears the directions displayed and removes the route line from the map. This method does not remove waypoints from the route and retains all calculated direction information and option settings. To clear the calculated directions and options, use `clearAll`. |
| `dispose()`                                          |                          | Deletes the DirectionsManager object and releases any associated resources.                                                                  |
| `getAllPushpins()` | [Pushpin](../../map-control-api/pushpin-class.md)[] | Returns all current pushpins for the rendered route. This includes pushpins created by addWaypoint and viaPoints created due to drag and drop. | 
| `getAllWaypoints()`                                  | [Waypoint](waypoint-class.md)\[\]             | Returns the waypoints for the route.                                                                                                              |
| `getCurrentRoute()`                                  | [Route](route-object.md) | Returns the currently displayed route information.                                                                                        |
| `getRenderOptions()`                                 | [DirectionsRenderOptions](directionsrenderoptions-object.md) | Returns the route render options.                                                                                                                 |
| `getRequestOptions()`                                | [DirectionsRequestOptions](directionsrenderoptions-object.md) | Returns the directions request options.                                                                                                           |
| `getRouteResult()`                                   | [Route](route-object.md)\[\]      | Returns the current calculated route(s). If the route was not successfully calculated, **null** is returned.                                        |
removeWaypoint(waypointOrIndex: [Waypoint](waypoint-class.md) _or_ number)    |                          | Sets the specified render options for the route. Use `calculateDirections` to update the route once a waypoint has been removed.                                                                                             |
| setRenderOptions(options: [DirectionsRenderOptions](directionsrenderoptions-object.md)) |         | Sets the specified render options for the route.  |
| setRequestOptions(options: [DirectionsRequestOptions](directionsrenderoptions-object.md) |    | Sets the specified route calculation options.
| `showInputPanel(inputContainerId: string)` | | Displays an input panel for calculating directions in the specified container. | 

## Events

| Name                | Arguments                | Description                                                               |
|---------------------|--------------------------|---------------------------------------------------------------------------|
| `directionsError`   | [DirectionsErrorEventArgs](../v8-web-control/directionserroreventargs-object.md) | Occurs when calculating the directions caused an error.                   |
| `directionsUpdated` | [DirectionsEventArgs](../v8-web-control/directionserroreventargs-object.md)      | Occurs when the directions calculation was successful and the itinerary and route on the map have been updated. |
