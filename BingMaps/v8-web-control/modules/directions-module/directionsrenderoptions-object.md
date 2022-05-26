---
title: "DirectionsRenderOptions Object | Microsoft Docs"
description: Describes the DirectionsRenderOptions object, which contains direction render options, and provides a list of properties.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: e17a413b-0c32-4997-a3b6-e93e862c19b1
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# DirectionsRenderOptions Object

You can set options for how to the route is rendered by passing an object containing direction render options to the `setRenderOptions` method of the [DirectionsManager](directionsmanager-class.md). The following is a list of properties that are available in the DirectionsRenderOptions object.

| Name                          | Type       | Description                                                        |
|-------------------------------|------------|--------------------------------------------------------------------|
| `autoUpdateMapView`             | boolean    | A boolean indicating whether to automatically set the map view to the best map view of the calculated route. Default: **true**                       |
| `displayDisclaimer`             | boolean    | A boolean indicating whether to display the disclaimer about the accuracy of the directions. Default: **true**                                       |
| `displayManeuverIcons`          | boolean    | A boolean indicating whether to display the icons for each direction maneuver. Default: **true**                                                     |
| `displayPostItineraryItemHints` | boolean    | A boolean indicating whether to display direction hints that describe when a direction step was missed. Default: **true**                            |
| `displayPreItineraryItemHints`  | boolean    | A boolean indicating whether to display direction hints that describe what to look for before you come to the next direction step. The default value is true. |
| `displayRouteSelector`          | boolean    | A boolean indicating whether to display the route selector control. Default: **true**                                                                |
| `displayStepWarnings`           | boolean    | A boolean indicating whether to display direction warnings. Default: **true**                                                                        |
| `displayWalkingWarning`         | boolean    | A boolean indicating whether to display a warning about walking directions. Default: **true**                                                        |
| `drivingPolylineOptions` | [PolylineOptions](../../map-control-api/polylineoptions-object.md) | The polyline options that define how to draw the route line on the map, if the **RouteMode** is driving. |
| `firstWaypointPushpinOptions` | [PushpinOptions](../../map-control-api/pushpinoptions-object.md) | The pushpin options that define how the first waypoint should be rendered. | 
| `itineraryContainer`            | DOMElement | The DOM element inside which the directions itinerary will be rendered.                                                                                           |
| `lastWaypointPushpinOptions` | [PushpinOptions](../../map-control-api/pushpinoptions-object.md) | The pushpin options that define how the last waypoint should be rendered. | 
| `showInputPanel`                | boolean    | A boolean indicating whether to show the input panel. Default: **false**                                                                             |
| `transitPolylineOptions` | [PolylineOptions](../../map-control-api/polylineoptions-object.md) | The options that define how to draw the route line on the map, if the **RouteMode** is transit. | 
| `walkingPolylineOptions` | [PolylineOptions](../../map-control-api/polylineoptions-object.md) | The options that define how to draw the route line on the map, if the **RouteMode** is walking. |
| `waypointPushpinOptions` | [PushpinOptions](../../map-control-api/pushpinoptions-object.md) | The options that define the pushpin to use for all route waypoints by default. The first and last waypoints in the route will be overridden by firstWaypointPushpinOptions and lastWaypointPushpinOptions if set. |
