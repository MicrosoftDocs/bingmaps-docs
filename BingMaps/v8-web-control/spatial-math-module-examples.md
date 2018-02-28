---
title: "Spatial Math Module Examples | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: faf8e258-a80c-4e7f-af96-ceb63e8259c0
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Spatial Math Module Examples
The Spatial Math module provides several commonly required spatial calculations.   

The Spatial Math module has three core parts:

* **Common Spatial Calculations**: This part consists of a set of commonly used spatial calculations, such as the ability to calculate distances between locations, or perform unit conversions. These calculations are exposed as static methods on the `Microsoft.Maps.SpatialMath` namespace.
* **Geometry Calculations**: This part consists of a set of complex geometric functions which can be used to perform binary operations against shapes (union, intersect, differences...), generate convex and concave hulls, and create Voronio diagrams. these static methods are exposed through the `Microsoft.Maps.SpatialMath.Geometry` namespace.       
* **Tile Math**: This part provides a set of methods that perform spatial calculations based on the Tile pyramid used by Bing Maps as defined [here](../articles/bing-maps-tile-system.md). This is often useful when creating custom data visualizations. These static methods are exposed through the `Microsoft.Maps.SpatialMath.Tile` namespace.   

In most calculations the distance or area unit parameters are optional. The default distance units used is meters, and the default area units is square meters.

## Examples

  * [Basic Core Spatial Math](../v8-web-control/basic-core-spatial-math-example.md)
  * [Geolocation Accuracy Circle](../v8-web-control/geolocation-accuracy-circle-example.md)
  * [Geometry Binary Operations](../v8-web-control/geometry-binary-operations.md)
  * [Calculate Tile Bounds](../v8-web-control/calculate-tile-bounds.md) 

## Related Topics

  * [AreaUnits Enumeration](../v8-web-control/areaunits-enumeration.md)
  * [Core Calculations](../v8-web-control/core-calculations.md)
  * [DistanceUnits Enumeration](../v8-web-control/distanceunits-enumeration.md)
  * [Geometry Calculations](../v8-web-control/geometry-calculations.md)
  * [Tile Calculations](../v8-web-control/tile-calculations.md)
  