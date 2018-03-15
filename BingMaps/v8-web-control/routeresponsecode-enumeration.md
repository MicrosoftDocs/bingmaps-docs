---
title: "RouteResponseCode Enumeration | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 58203d9e-ad7d-44e4-af43-2262598d07b4
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# RouteResponseCode Enumeration
Contains response codes for a route calculation request.

| Response Code | Name                           | Description                                                                                                                                                                     |
|---------------|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0             | **success**                    | The route was successfully calculated.                                                                                                                                          |
| 1             | **unknownError**               | An unknown error has occurred.                                                                                                                                                  |
| 2             | **cannotFindNearbyRoad**       | A nearby road cannot be found for one or more of the route waypoints.                                                                                                           |
| 3             | **tooFar**                     | The distance between two route waypoints, or the total length of the route exceeds the limit of the route mode. Modify the waypoint locations so that they are closer together. |
| 4             | **noSolution**                 | A route cannot be calculated for the specified waypoints. For example, this code is returned when a route between “Seattle, WA” and “Honolulu, HI” is requested.                |
| 5             | **dataSourceNotFound**         | There is no route data for the specified waypoints.                                                                                                                             |
| 7             | **noAvailableTransitTrip**     | There are no transit options available for the specified time.                                                                                                                  |
| 8             | **transitStopsTooClose**       | The transit stops are so close that walking is *always* a better option.                                                                                                        |
| 9             | **walkingBestAlternative**     | The transit stops are so close that walking is a better option.                                                                                                                 |
| 10            | **outOfTransitBounds**         | There is no transit data available for the route or for one or more of the specified waypoints, or the waypoints are in different transit areas that do not overlap.            |
| 11            | **timeout**                    | The directions calculation request has timed out.                                                                                                                               |
| 12            | **waypointDisambiguation**     | One or more waypoints need to be disambiguated. This error does not occur if the `autoDisplayDisambiguation` directions render option is set to **true**.                     |
| 13            | **hasEmptyWaypoint**           | One or more waypoints do not have an address or location specified.                                                                                                             |
| 14            | **exceedMaxWaypointLimit**     | The maximum number of waypoints, which is 25, has been exceeded.                                                                                                                |
| 15            | **atleastTwoWaypointRequired** | At least two waypoints are required to calculate a route.                                                                                                                       |
| 16            | **firstOrLastStoppointIsVia**  | The first or last waypoint is a via point, which is not allowed.                                                                                                                |
| 17            | **searchServiceFailed**        | The search service failed to return results.                                                                                                                                    |
| 18            | **invalidCredentials**         | The credentials passed to the Directions module are invalid.                                                                                                                    |
