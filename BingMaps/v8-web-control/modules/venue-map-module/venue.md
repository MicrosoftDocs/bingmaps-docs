---
title: Venue JSON class
titleSuffix: Microsoft Bing Maps
description: Venue JSON class encapsulates a venue, consisting of one or more floors. Display data in the Bing Maps V8 Web Control by creating a VenueMap instance.
ms.custom: 
ms.date: 05/26/2020
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
ms.topic: article
ms.assetid: E917F6EC-F5EE-4F98-8C33-05868734390C
caps.latest.revision: 3
author: DavidBuerer
ms.author: dbuerer
manager: 
ms.service: bing-maps
---

# Venue JSON class

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../../includes/bing-maps-web-control-sdk-retirement.md)]

Encapsulates a venue, consisting of one or more floors.

Data that adheres to this JSON format can be displayed in the [Bing Maps V8 Web Control] by creating a [VenueMap] instance with [VenueMapFactory].create.

## Properties

| Property        | Type           | Req? | Description |
|-----------------|----------------|:------:|-------------|
| id              | string         |  ✔   | A unique identifier of the venue. |
| isGeoPositioned | boolean        |      | Whether this venue, once its coordinates are transformed, has geopositioned longitude, latitude values or engineering coordinates. |
| defaultCulture  | string         |      | The culture that is used when a string has an empty culture or if this value is not specified, en-us is used as the default. |
| name            | culture:string |      | Dictionary of culture-specific names for the venue where empty string for the key refers to the culture identified by the defaultCulture property. |
| xy              | number[]       |      | An X,Y coordinate that, once transform is applied, defines a central location for the venue. |
| address         | [address]      |      | |
| phone           | string         |      | The phone number for the venue. |
| defaultFloor    | integer        |      | The index of the floor to display as default, where the lowest floor is 1. |
| bbox            | number[]       |      | A set of coordinates (bottom, left, top, right) that, once transform is applied, define the geographical area of the venue. |
| floors          | [floor]        |  ✔   | A list of the floors that comprise the venue, starting with the **footprint floor** which is shown at every floor, and proceeding from the bottom of the venue upward. |
| transform       | number[]       |      | A 3x3 matrix that, if provided, will be applied to each of the coordinates in the venue.  This will typically take coordinates from engineering coordinates to geopositioned ones. |

### The Footprint Floor

The first (0) entry in the floors array is a special floor that is not part of floor selection, but instead contains geometry that is shown with every floor.  This primarily consists of the footprint geometry, but could contain other geometry like outdoor fountains.

### The Transform Field

The matrix contained in the transform field is expected to be applied to any coordinate (venue.xy, geometry.x and y, etc.) using a method like this one:

```csharp
public Point Transform(Point point)
{
    return new Vector2D(
        point.X * transform[0] + point.Y * transform[1] + transform[2],
        point.X * transform[3] + point.Y * transform[4] + transform[5]);
}
```

## Example

See the venue [sample].

[address]: address.md
[floor]: floor.md
[sample]: sample.md
[Bing Maps V8 Web Control]: ../index.md
[VenueMap]: venuemap-class.md
[VenueMapFactory]: venuemapoptions-object.md
