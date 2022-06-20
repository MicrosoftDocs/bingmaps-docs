---
title: "Core Calculations | Microsoft Docs"
description: Describes core calculations in the Spatial Math Module and provides a list of static methods.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 66970f16-fb87-4edd-8bcf-fbd9ea441767
caps.latest.revision: 6
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Core Calculations

The core calculations in the Spatial Math Module provide a set of commonly used spatial calculations, such as the ability to calculate distances between locations, or perform unit conversions. These calculations are exposed as static methods on the `Microsoft.Maps.SpatialMath` namespace.

## Static Methods

Name                                                                                                                 | Return Type               | Description
-------------------------------------------------------------------------------------------------------------------- | ------------------------- | ----------------------------
convertArea(area: number, fromUnits: [AreaUnits](areaunits-enumeration.md), toUnits: [AreaUnits](areaunits-enumeration.md))                                                | number                    | Converts an area from one area unit to another.
convertDistance(distance: number, fromUnits: [DistanceUnits](distanceunits-enumeration.md), toUnits: [DistanceUnits](distanceunits-enumeration.md))                                | number                    | Converts a distance from one distance unit to another.
getCardinalSpline(locations: [Location\[\]](../../map-control-api/location-class.md), tension ?: number, nodeSize ?: number, close ?: boolean) | [Location\[\]](../../map-control-api/location-class.md) | Calculates an array of locations that form a cardinal spline between the specified array of locations.<br/>&nbsp; • **tension** - A number that indicates the tightness of the curve. Can be any number, although a value between 0 and 1 is usually used. Default: **0.5**<br/>&nbsp; • **nodeSize** - Number of nodes to insert between each Location. Default: **15**<br/>&nbsp; • **close** - A boolean indicating if the spline should be a closed ring or not. Default: **false**
getDestination(origin: [Location](../../map-control-api/location-class.md), bearing: number, distance: number, units?: [DistanceUnits](distanceunits-enumeration.md))  | [Location](../../map-control-api/location-class.md)                  | Calculates a destination coordinate based on a starting coordinate, a heading, a distance, and an optional distance unit type.<br/><br/>The bearing angle is between 0 - 360 degrees, where 0 - North, 90 - East, 180 - South, 270 - West.
getDistanceTo(origin: [Location](../../map-control-api/location-class.md), destination: [Location](../../map-control-api/location-class.md), units?: [DistanceUnits](distanceunits-enumeration.md), highAccuracy?: boolean)              | number                    | Calculate the distance between two locations on the surface of the earth using the Haversine formula. If ***_highAccuracy_*** value is set to true, the slower but more accurate Vincenty formula is used instead. 
getEarthRadius(units?: [DistanceUnits](distanceunits-enumeration.md))                                                                              | number                    | Returns the approximate radius of the earth in the specified distance units for a WGS84 spheroid. 
getGeodesicPath(path: [Location](../../map-control-api/location-class.md)[], nodeSize?: number)                                                               | [Location](../../map-control-api/location-class.md)[]                | Takes an array of Locations and fills in the space between them with accurately positioned coordinates to form an approximated Geodesic path (appears as a curved line on map). The **_nodeSize_** parameter is the number of Location objects to insert between each location to approximate a geodesic path.
getHeading(origin: [Location](../../map-control-api/location-class.md), destination: [Location](../../map-control-api/location-class.md))                                                                | number                    | Calculates the heading from one Location to another.
getLengthOfPath(path: [Location](../../map-control-api/location-class.md)[], units?: [DistanceUnits](distanceunits-enumeration.md), highAccuracy?: boolean) | number | Calculates the distance between all Location objects in an array.
getLocationAlongPath(path: [Polyline](../../map-control-api/polyline-class.md) _or_ [Location](../../map-control-api/location-class.md)[], distance: number, units?: [DistanceUnits](distanceunits-enumeration.md))                      | [Location](../../map-control-api/location-class.md)                  | Calculates the Location on a path that is a specified distance away from the start of the path. If the specified distance is longer than the length of the path, the last coordinate of the path will be returned.
getRegularPolygon(origin: [Location](../../map-control-api/location-class.md), radius: number, numberOfPoints: number, units?: [DistanceUnits](distanceunits-enumeration.md), offset?: number)  | [Location](../../map-control-api/location-class.md)[]              | Calculates an array of locations that are an equal distance away from a central point to create a regular polygon.<br/><br/>&nbsp; • **origin** – center of the polygon.<br/>&nbsp; • **radius** – the distance from the origin to each point on the polygon.<br/>&nbsp; • **numberOfPoints** – the number of points the polygon should have.<br/>&nbsp; • **units** – The distance units of the radius.<br/>&nbsp; • **offset** – An angle between 0 and 360 to rotate the polygon clockwise. When 0 the first Location in the polygon will be North of the origin.<br/><br/>**Tip**: The larger the **_numberOfPoints_** property, the more the generated array of locations will look like a circle.
interpolate(origin: [Location](../../map-control-api/location-class.md), destination: [Location](../../map-control-api/location-class.md), fraction?: number)                                            | [Location](../../map-control-api/location-class.md)                  | Calculates a Location that is a fraction of the distance between two points, relative to the first Location object. Default fraction is 0.5, which is the midpoint between the coordinates.
locationRectToPolygon(bounds: [LocationRect](../../map-control-api/locationrect-class.md))                                                                        | [Polygon](../../map-control-api/polygon-class.md)                   | Takes a [LocationRect](../../map-control-api/locationrect-class.md) object and converts it to a [Polygon](../../map-control-api/polygon-class.md).
toDegMinSec(loc: [Location](../../map-control-api/location-class.md))                                                                                         | string                    | Takes a Location object and converts it into a Degree Minute Seconds string in the format. For example: 40° 26′ 46″ N 79° 58′ 56″ W
`tryParseDegMinSec(input: string)`                                                                                   | number _or_ [Location](../../map-control-api/location-class.md)      | Tries to parse the given string that is in Degree Minute Seconds format. For Example: 35° 26′ 31″ E or 40° 26′ 46″ N 79° 58′ 56″ W <br/><br/>Returns a decimal degree value if only a single angle is provided. If two angles provided in the string, then a Location object is returned. If string is in an i