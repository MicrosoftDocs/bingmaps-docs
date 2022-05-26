---
title: "Spatial Math Module Examples | Microsoft Docs"
description: Describes the Spatial Math module, which provides commonly required spatial calculations, and provides lists of examples and related topics.
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
ms.service: "bing-maps"
---

# Spatial Math Module Examples

The Spatial Math module provides several commonly required spatial calculations.   

The Spatial Math module has three core parts:

* **Common Spatial Calculations**: This part consists of a set of commonly used spatial calculations, such as the ability to calculate distances between locations, or perform unit conversions. These calculations are exposed as static methods on the `Microsoft.Maps.SpatialMath` namespace.
* **Geometry Calculations**: This part consists of a set of complex geometric functions which can be used to perform binary operations against shapes (union, intersect, differences...), generate convex and concave hulls, and create Voronio diagrams. these static methods are exposed through the `Microsoft.Maps.SpatialMath.Geometry` namespace.       
* **Tile Math**: This part provides a set of methods that perform spatial calculations based on the Tile pyramid used by Bing Maps as defined [here](../../../articles/bing-maps-tile-system.md). This is often useful when creating custom data visualizations. These static methods are exposed through the `Microsoft.Maps.SpatialMath.Tile` namespace.   

In most calculations the distance or area unit parameters are optional. The default distance units used is meters, and the default area units is square meters.

## Examples

  * [Basic Core Spatial Math](basic-core-spatial-math-example.md)
  * [Geolocation Accuracy Circle](geolocation-accuracy-circle-example.md)
  * [Geometry Binary Operations](geometry-binary-operations.md)
  * [Calculate Tile Bounds](calculate-tile-bounds.md) 

## Related Topics

  * [AreaUnits Enumeration](../../modules/spatial-math-module/areaunits-enumeration.md)
  * [Core Calculations](../../modules/spatial-math-module/core-calculations.md)
  * [DistanceUnits Enumeration](../../modules/spatial-math-module/distanceunits-enumeration.md)
  * [Geometry Calculations](../../modules/spatial-math-module/geometry-calculations.md)
  * [Tile Calculations](../../modules/spatial-math-module/tile-calculations.md)
  