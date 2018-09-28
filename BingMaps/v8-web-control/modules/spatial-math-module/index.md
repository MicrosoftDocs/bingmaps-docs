---
title: "Spatial Math Module | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 403eb765-1558-4c4b-a5dd-044e20789aba
caps.latest.revision: 10
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Spatial Math Module
**Module Name**: Microsoft.Maps.SpatialMath

In some applications it may be necessary to perform complex spatial calculations, such as the distance between two locations, or intersection area of two polygons. The Spatial Math module provides several commonly required spatial calculations.   

The Spatial Math module has three core parts:

* **Common Spatial Calculations**: This part consists of a set of commonly used spatial calculations, such as the ability to calculate distances between locations, or perform unit conversions. These calculations are exposed as static methods on the `Microsoft.Maps.SpatialMath` namespace.
* **Geometry Calculations**: This part consists of a set of complex geometric functions which can be used to perform binary operations against shapes (union, intersect, differences...), generate convex and concave hulls, and create Voronoi diagrams. These static methods are exposed through the `Microsoft.Maps.SpatialMath.Geometry` namespace.       
* **Tile Math**: This part provides a set of methods that perform spatial calculations based on the Tile pyramid used by Bing Maps as defined [here](../articles/bing-maps-tile-system.md). This is often useful when creating custom data visualizations. These static methods are exposed through the `Microsoft.Maps.SpatialMath.Tile` namespace.   

In most calculations the distance or area unit parameters are optional. The default distance units used is meters, and the default area units is square meters. 

## API Reference

  * [AreaUnits Enumeration](../v8-web-control/areaunits-enumeration.md)
  * [BufferEndCap Enumeration](../v8-web-control/bufferendcap-enumeration.md)
  * [Core Calculations](../v8-web-control/core-calculations.md)
  * [DistanceUnits Enumeration](../v8-web-control/distanceunits-enumeration.md)
  * [Geometry Calculations](../v8-web-control/geometry-calculations.md)
  * [Tile Calculations](../v8-web-control/tile-calculations.md)
  
## Examples

  * [Basic Core Spatial Math](../v8-web-control/basic-core-spatial-math-example.md)
  * [Geolocation Accuracy Circle](../v8-web-control/geolocation-accuracy-circle-example.md)
  * [Geometry Binary Operations](../v8-web-control/geometry-binary-operations.md)
  * [Calculate Tile Bounds](../v8-web-control/calculate-tile-bounds.md) 
