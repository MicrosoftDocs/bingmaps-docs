---
title: "Tile Calculations | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 40bd4e04-d26d-4540-b093-4c0617d63d2f
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Tile Calculations

A set of methods that perform spatial calculations based on the Tile pyramid used by Bing Maps as defined [here](../../../articles/bing-maps-tile-system.md). These static methods are exposed through the `Microsoft.Maps.SpatialMath.Tiles` namespace.

Name                                                                                  | Return Type           | Description
------------------------------------------------------------------------------------- | --------------------- | ----------------------------
`mapSize(zoom: number)`                                                               | number                | Calculates the full width of the map in pixels at a specific zoom level from -180 degrees to 180 degrees.
groundResolution(latitude: number, zoom: number, units?: [DistanceUnits](distanceunits-enumeration.md))             | number                | Calculates the ground resolution at a specific degree of latitude in the specified units per pixel.
globalPixelToLocation(point: [Point](../../map-control-api/point-class.md), zoom: number)                                   | [Location](../../map-control-api/location-class.md)              | Converts a pixel coordinate into a geospatial coordinate at a specified zoom level. Global Pixel coordinates are relative to the top left corner of the map (90, -180).
locationToGlobalPixel(loc: [Location](../../map-control-api/location-class.md), zoom: number)                                  | [Point](../../map-control-api/point-class.md)                 | Converts a point from latitude/longitude WGS-84 coordinates (in degrees) into pixel XY coordinates at a specified level of detail.
globalPixelToTile(pixel: [Point](../../map-control-api/point-class.md), zoom: number)                                       | [PyramidTileId](../../map-control-api/pyramidtileid-class.md)         | Calculates the PyramidTileId that a global pixel intersects with at a specific zoom level.
tileToGlobalPixel(tile: [PyramidTileId](../../map-control-api/pyramidtileid-class.md))                               | [Point](../../map-control-api/point-class.md)                 | Converts the upper-left corner of a PyramidTileId into a global pixel coordinate.
locationToTile(loc: [Location](../../map-control-api/location-class.md), zoom: number)                                         | [PyramidTileId](../../map-control-api/pyramidtileid-class.md)         | Calculates the PyramidTileId that a Location object intersects with at a specific zoom level.
getTilesInBounds(bounds: [LocationRect](../../map-control-api/locationrect-class.md), zoom: number)                                | [PyramidTileId](../../map-control-api/pyramidtileid-class.md)[]       | Calculates all the PyramidTileId's that are within a LocationRect at a specific zoom level.
tileToLocationRect(tile: [PyramidTileId](../../map-control-api/pyramidtileid-class.md))                                             | [LocationRect](../../map-control-api/locationrect-class.md)          | Calculates the LocationRect of a PyramidTileId.
