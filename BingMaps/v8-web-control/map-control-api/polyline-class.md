---
title: "Polyline Class | Microsoft Docs"
description: "Describes the polyline class and provides the class's constructor and tables that outline the class's methods, properties, and events."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 766b7eb1-b090-499f-8278-2a3a58f6f6f7
caps.latest.revision: 10
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Polyline Class

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../includes/bing-maps-web-control-sdk-retirement.md)]

Polylines allow you to draw connected lines on a map. In many spatial database systems, this is also known as a LineString. The Polyline class derives from the `IPrimitive` interface. When creating a polyline, an array of locations must be passed as an argument in the constructor. Optionally polyline options can also be passed in as an argument.

## Constructor

> Polyline(locations: [Location](location-class.md)[], options?: [PolylineOptions](polylineoptions-object.md))

## Methods

The Polyline class has the following methods.

| Name                               | Return Type       | Description                                                |
|------------------------------------|-------------------|------------------------------------------------------------|
| `getCursor()` | string | Gets the css cursor value when the polyline has mouse events on it. |
| `getGeneralizable()` | boolean | Returns whether the polyline is generalizable based on zoom level or not. |
| `getLocations()`                   | [Location](location-class.md)\[\]      | Returns the locations that define the polyline.    |
| `getStrokeColor()`                 | string _or_ [Color](color-class.md)    | Returns the color of the polyline.                 |
| `getStrokeDashArray()`             | string _or_ number\[\] | Returns the string that represents the stroke/gap sequence used to draw the polyline.  |
| `getStrokeThickness()`             | number            | Returns the thickness of the polyline.                                    |
| `getVisible()`                     | boolean           | Returns whether the polyline is visible. A value of false indicates that the polyline is hidden, although it is still an entity on the map. |
| setLocations(locs: [Location](location-class.md)\[\]) |                   | Sets the locations that define the polyline.                              |
| setOptions(opt: [PolylineOptions](polylineoptions-object.md)) |                   | Sets options for the polyline.                                            |

## Properties

| Name     | Type     | Description                        |
|----------|----------|------------------------------------|
| `metadata` | object   | Information that is linked to the polyline. Some modules such at the GeoJSON, and Spatial Data Service modules will also often add information to this property.          |

## Events

| Name  | Arguments  | Description                                                                                   |
|-----------|----------------|---------------------------------------------------------------------------------------|
| `changed` | [IPrimitiveChangedEventArgs](iprimitivechangedeventargs-object.md) | Occurs when the locations or options of the polyline has changed. |
| `click`     | [MouseEventArgs](mouseeventargs-object.md) | Occurs when the mouse is used to click the polyline.   
`dblclick` | [MouseEventArgs](mouseeventargs-object.md) | Occurs when the mouse is used to double click the polyline.                             |
| `mousedown` | [MouseEventArgs](mouseeventargs-object.md) | Occurs when the left mouse button is pressed when the mouse is over the polyline.   |
| `mouseout`  | [MouseEventArgs](mouseeventargs-object.md) | Occurs when the mouse cursor moves out of the area covered by the polyline.         |
| `mouseover` | [MouseEventArgs](mouseeventargs-object.md) | Occurs when the mouse is over the polyline.                                         |
| `mouseup`   | [MouseEventArgs](mouseeventargs-object.md) | Occurs when the left mouse button is lifted up when the mouse is over the polyline. |
