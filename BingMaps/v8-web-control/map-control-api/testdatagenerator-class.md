---
title: "TestDataGenerator Class | Microsoft Docs"
description: "Describes the TestDataGenerator class and provides a table that outlines the return value and description for various static method definitions."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 1ab540e8-71d6-4cae-8e49-3a650a8e1f83
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# TestDataGenerator Class

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../includes/bing-maps-web-control-sdk-retirement.md)]

Often when creating a demo or trying to test a new application you need to create some test/mock data.  Generating a random Location object isn’t particularly difficult, but what if you want to create a random Polygon that actually looks like a polygon, and maybe has a hole as well? 

This can be difficult to achieve and require a fair amount of code. In some cases, the code needed to generate random shape data can end up being longer than the code you are trying to test. To help with testing scenarios, the Bing Maps V8 control features a test data generator. This test data generator consists of a set of static methods which are exposed through the `Microsoft.Maps.TestDataGenerator` namespace.

## Static Methods

Definition                                                                      | Return Value                 | Description
------------------------------------------------------------------------------- | ---------------------------- | -----------------------------------
`getColor(withAlpha?: boolean)`                                                   | string                       | Generates a random hex color string. If the **withAlpha** value is to true, a RGBA value will be returned with an alpha value of 0.5.
`getLocations(num?: number, bounds?: LocationRect)`                               | Location _or_ Location[]     | Generates random Location objects.<br/>**num**: The number of locations to generate. If set to one a single Location will be returned. If greater than one and array will be returned.<br/>**bounds**: The bounding box in which all the locations should fall within.
`getPushpins(num?: number, bounds?: LocationRect, options?: IPushpinOptions)`     | Pushpin _or_ Pushpin[]       | Generates random pushpins.<br/>**num**: The number of pushpins to generate. If set to one a single Pushpin will be returned. If greater than one and array will be returned.<br/>**bounds**: The bounding box in which all the pushpins should fall within.<br/>**options**: The options to use for rendering the pushpins. Default is random.
`getPolylines(num?: number, bounds?: LocationRect, size?: number, scaleFactor?: number, options?: IPolylineOptions)`            | Polyline _or_ Polyline[]   | Generates random polylines.<br/>**num**: The number of polylines to generate. If set to one a single Polyline will be returned. If greater than one and array will be returned.<br/>**bounds**: The bounding box in which all the locations of the polylines should fall within.<br/>**size**: The number of locations each polylines should have. Default: random between 3 and 10.<br/>**scaleFactor**: A number that scales the size of the polylines based on size of the bounding box. A value of 0.1 would generate polylines that are no larger than 10% of the width/height of the map. Default: **0.1**<br/>**options**: The options to use for rendering the polylines. Default is random.
`getPolygons(num?: number, bounds?: LocationRect, size?: number, scaleFactor?: number, options?: IPolygonOptions, addHole?:boolean)` | Polygon _or_ Polygon[]  | Generates random simple polygons.<br/>**num**: The number of polygons to generate. If set to one a single Polygon will be returned. If greater than one and array will be returned.<br/>**bounds**: The bounding box in which all the locations of the polygon should fall within.<br/>**size**: The number of locations each polygon should have. Default: random between 3 and 10.<br/>**scaleFactor**: A number that scales the size of the polygons based on the size of the bounding box. A value of 0.1 would generate polygons that are no larger than 10% of the width/height of the map. Default: **0.1**<br/>**options**: The options to use for rendering the polygons. Default is random.<br/>**addHole**: A boolean indicating if the generated polygon should have a hole or not. Note that this will double the number of Location objects that are in the Polygon. Default: **false**

## See Also

* [Test Data Generator Example](../map-control-concepts/test-data-generator-example.md) 