---
title: "LocationRect Class2 | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: a3eecc38-4be9-4a7a-affc-ddfdc249d816
caps.latest.revision: 10
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# LocationRect Class
The LocationRect class, also known as a bounding box, consists of a set of coordinates that are used to represent rectangular area on the map. These are often used for setting the map view but are also useful for doing calculations. A LocationRect object has three properties; center, width and height. The center property is a [Location](../v8-web-control/location-class.md) object marking the center of the LocationRect area. The width and height properties are angles in degrees from the center of the LocationRect to the edges. An instance of the LocationRect class can be created using the following code. 

## Constructor

> `LocationRect(center: Location, width: number, height: number)`

## Properties

Name          | Type         | Description
------------- | ------------ | --------------------
`center`      | [Location](../v8-web-control/location-class.md)     | The location that defines the center of the rectangle.
`height`      | number       | The height, in degrees, of the rectangle.
`width`       | number       | The width, in degrees, of the rectangle.

## Static Methods

In addition to creating a LocationRect object using center, width and height values the following static methods can be used to create a LocationRect as well:

Method                                                              | Description
------------------------------------------------------------------- | ----------------------
fromCorners(northwest: [Location](../v8-web-control/location-class.md), southeast: [Location](../v8-web-control/location-class.md))             | Returns a LocationRect using the specified locations for the northwest and southeast corners.
`fromEdges(north:number, west:number, south:number, east:number)`   | Returns a LocationRect using the specified northern and southern latitudes and western and eastern longitudes for the rectangle boundaries.
fromLocations([Location](../v8-web-control/location-class.md)[])                                         | Returns a LocationRect using a list of locations or an array of locations.
`fromString("north,west,south,east")`                               | Creates a LocationRect from a string with the following format: "north,west,south,east". North, west, south and east specify the coordinate number values.

## Methods

The following is a list of methods that are part of the LocationRect class.

Name                                 | Return Type          | Description
------------------------------------ | -------------------- | ----------------------------
`buffer(percentage: number)`         |                      | Scales the size of a LocationRect by multiplying the width and height properties by a percentage.
`clone()`                            | LocationRect         | Returns a copy of the LocationRect object.
contains(location: [Location](../v8-web-control/location-class.md))                         | boolean              | Determines if a Location is within the LocationRect.
`crossesInternationalDateLine()`     | boolean              | Determines if the LocationRect crosses the 180th meridian.
`getEast()`                          | number               | Returns the longitude that defines the eastern edge of the LocationRect.
`getNorth()`                         | number               | Returns the latitude that defines the northern edge of the LocationRect.
`getNorthwest()`                     | [Location](../v8-web-control/location-class.md)             | Returns the Location that defines the northwest corner of the LocationRect.
`getSouth()`                         | number               | Returns the latitude that defines the southern edge of the LocationRect.
`getSoutheast()`                     | [Location](../v8-web-control/location-class.md)             | Returns the Location that defines the southeast corner of the LocationRect.
`getWest()`                          | number               | Returns the latitude that defines the western edge of the LocationRect.
intersects(locationRect: LocationRect)                       | boolean              | Determines if one LocationRect intersects with this LocationRect.
`splitByInternationalDateLine()`     | LocationRect[]       | If a LocationRect crosses the international date line, this method splits it into two LocationRect objects and returns them as an array.
`toString()`                         | string               | Converts the LocationRect object to a string. The output will be in the format "North,West,South,East".
