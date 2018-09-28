---
title: "Polygon Class | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: f571bbcb-e9db-4592-96cf-68b7bb22a27b
caps.latest.revision: 10
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Polygon Class
A polygon is an area defined by a closed ring of locations. A simple polygon consists of an array of [Location](../v8-web-control/location-class.md) objects that form a boundary. This is useful for showing an area of interest on a map. In some applications there may be a need to for more complex polygons, such as polygons that have a hole in them. Take for instance the country of South Africa, which has a land locked country, Lesotho, within its main border. To represent South Africa on a map we need to be able to cut a hole in the polygon that represents its boundary to exclude the area of Lesotho. The first array of locations in a polygon represent the main border and is often called the exterior ring. All additional arrays of locations in a polygon are used to represent holes in the main polygon and are often called interior rings. Here is what the borders of South Africa look like.

![BMV8_SouthAfricaBorders](../v8-web-control/media/bmv8-southafricaborders.png)
 
The Polygon class derives from the `IPrimitive` interface. When creating a polygon at least one array of Location objects must be passed as an argument to the constructor. An array of Location arrays can be passed in when creating complex polygons. Optionally, polygon options can also be passed as an argument.

## Constructor

> Polygon(rings: [Location](../v8-web-control/location-class.md)[] | [Location](../v8-web-control/location-class.md)[][], options?: [PolygonOptions](../v8-web-control/polygonoptions-object.md))

## Methods

The Polygon class has the following methods.

Name                                                | Return Type           | Description
--------------------------------------------------- | --------------------- | -------------------------------------------------------
`getCursor()`	| string | Gets the css cursor value when the polygon has mouse events on it.
`getGeneralizable()` | boolean | Returns whether the polygon is generalizable based on zoom level or not.
`getFillColor()`                                    | string _or_ [Color](../v8-web-control/color-class.md)     | Returns the color of the inside of the polygon.
`getLocations()`                                    | [Location](../v8-web-control/location-class.md)[]            | Returns the first ring of locations that define the polygon. If multiple rings were used to create the polygon, this method will return the first ring in the array.
`getRings()`                                        |                       | Returns an array of location arrays, where each location array defines a ring of the polygon.
`getStrokeColor()`                                  | string _or_ [Color](../v8-web-control/color-class.md)     | Returns the color of the outline of the polygon.
`getStrokeDashArray()`                              | string _or_ number[]  | Returns the string that represents the stroke/gap sequence used to draw the outline of the polygon.
`getStrokeThickness()`                              | number                | Returns the thickness of the outline of the polygon.
`getVisible()`                                      | boolean               | Returns whether the polygon is visible. A value of false indicates that the polygon is hidden, although it is still an entity on the map.
setLocations([Location](../v8-web-control/location-class.md)[])                          |                       | Sets the locations that define the polygon. Overwrites the rings value.
setOptions(opt: [PolygonOptions](../v8-web-control/polygonoptions-object.md))                  |                       | Sets options for the polygon.
setRings(rings: [Location](../v8-web-control/location-class.md)[] _or_ [Location](../v8-web-control/location-class.md)[][])     |                       | Sets an array of location arrays, where each location array defines a ring of the polygon.


## Properties

Name                | Type               | Description
------------------- | ------------------ | ------------------------------------------
`metadata`            | object             | Information that is linked to the polygon. Some modules such as the GeoJSON and Spatial Data Service modules will also often add information to this property.

## Events

| Name      | Arguments      | Description                                                                        |
|-----------|----------------|------------------------------------------------------------------------------------|
| `changed` | [IPrimitiveChangedEventArgs](../v8-web-control/iprimitivechangedeventargs-object.md) | Occurs when the locations/rings or options of the polygon has changed. |
| `click`     | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the mouse is used to click the polygon.                       |
`dblclick` | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the mouse is used to double click the polygon.
| `mousedown` | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the left mouse button is pressed when the mouse is over the polygon.   |
| `mouseout`  | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the mouse cursor moves out of the area covered by the polygon.|
| `mouseover` | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the mouse is over the polygon.                                |
| `mouseup`   | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the left mouse button is lifted up when the mouse is over the polygon. |