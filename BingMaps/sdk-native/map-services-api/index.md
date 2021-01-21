---
title: "MapServices API Reference | Microsoft Docs"
author: "pablocan"
---

# MapServices API Reference

## Classes 

Name                                                        | Details
----------------------------------------------------------- | ------------------------------------------------------
[Geopoint](../map-control-api/Geopoint-class.md)            | Describes a geographic point.
[MapLocation](MapLocation-class.md)                         | Contains data about a specific location returned from a geocoding request.
[MapLocationAddress](MapLocationAddress-class.md)           | Contains address data for a specific location returned from a geocoding request.
[MapLocationFinder](MapLocationFinder-class.md)             | Forms and sends geocoding requests.
[MapLocationOptions](MapLocationOptions-class.md)           | Forms optional parameters for a geocoding request.
[MapLocationPoint](MapLocationPoint-class.md)               | Contains geospatial data for a specific point associated with the location returned from a geocoding request.
[MapLocationFinderResult](MapLocationFinderResult-class.md) | Contains status code and result location data for a geocoding request.
[ManeuverWarning](ManeuverWarning-class.md)                 | A potential issue along a route leg.
[MapRoute](MapRoute-class.md)                               | Contains a path to be traveled between two or more waypoints.
[MapRouteDrivingOptions](MapRouteDrivingOptions-class.md)   | Forms optional options for a routing request.
[MapRouteFinder](MapRouteFinder-class.md)                   | Forms and sends a route request
[MapRouteFinderResult](MapLocationFinderResult-class.md)    | Contains status code and result route data.
[MapRouteLeg](MapRouteLeg-class.md)                         | Contains the set of actions (maneuvers) required to travel between two waypoints along a route.
[MapRouteManeuver](MapRouteManeuver-class.md)               | Contains actions to be taken along the path of a route leg.
[MapServices](MapServices-class.md)                         | Provides common methods for map services.
[RouteWaypoint](RouteWaypoint-class.md)                     | Represents a stop, start, or intermediate waypoint that a route must pass through.

## Enumerations

Name                                                                                  | Details
------------------------------------------------------------------------------------- | ------------------------------------------------------
[MapLocationEntityTypes](MapLocationEntityTypes-enumeration.md)                       | The entity types to be included in the response for a geocoding request.
[MapLocationMatchCode](MapLocationMatchCode-enumeration.md)                           | The geocoding level for a location returned from a geocoding request.
[MapLocationPointCalculationMethod](MapLocationPointCalculationMethod-enumeration.md) | The method that was used to compute the geopoint for a location returned from a geocoding request.
[MapLocationPointUsageType](MapLocationPointUsageType-enumeration.md)                 | The best use for the geopoint for a location returned from a geocoding request.
[MapLocationFinderStatus](MapLocationFinderStatus-enumeration.md)                     | Status code for a geocoding request.
[ManeuverWarningKind](ManeuverWarningKind-enumeration.md)                             | Specifies the type of potential issue along a route leg.
[ManeuverWarningSeverity](ManeuverWarningSeverity-enumeration.md)                     | Specifies the severity of a potential issue along a route leg.
[MapManeuverNotices](MapManeuverNotices-enumeration.md)                               | Provides additional information about a maneuver.
[MapRouteFinderStatus](MapRouteFinderStatus-enumeration.md)                           | Status code of a MapRouteFinder query.
[MapRouteManeuverKind](MapRouteManeuverKind-enumeration.md)                           | Describes the various types of maneuvers that can occur in a route.
[MapRouteOptimization](MapRouteOptimization-enumeration.md)                           | The optimization applied to a route.
[MapRouteRestrictions](MapRouteRestrictions-enumeration.md)                           | The restrictions applied to a route.
[RouteWaypointType](RouteWaypointType-enumeration.md)                                 | The type of waypoint.
[TrafficCongestion](TrafficCongestion-enumeration.md)                                 | The level of traffic congestion along a map route or route leg.

## Interfaces

Name                                                                                                  | Details
----------------------------------------------------------------------------------------------------- | ------------------------------------------------------
[OnMapLocationFinderResultListener](Android/OnMapLocationFinderResultListener-interface.md) (Android) | Represents an interface for handling the results of a geocoding request, on Android.
[MapLocationFinderResultHandler](iOS/MapLocationFinderResultHandler-interface.md) (iOS)               | Represents an interface for handling the results of a geocoding request, on iOS.
[OnMapRouteFinderResultListener](Android/OnMapRouteFinderResultListener-interface.md) (Android)       | Represents an interface for handling the results of a routing request, on Android.
[MSMapRoutingCompletionBlock](iOS/MapRoutingCompletionBlock-interface.md) (iOS)                       | Represents an interface for handling the results of a routing request, on iOS.
