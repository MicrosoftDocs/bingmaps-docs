---
title: "Point Class | Microsoft Docs"
description: "Describes the point class and provides the class's constructor, properties, and a table that gives the return type and description for various methods."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d196d952-cd2b-401a-9d00-7b6694004329
caps.latest.revision: 5
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Point Class
This class is used to represent a pixel coordinate or offset. This is often used by pushpin anchors, and map location to pixel conversion calculations. 

## Constructor

> `Point(x: number, y: number)`

## Properties

Name       | Type      | Description
---------- | --------- | ---------------------------
`x`        | number    | The x value of the point.
`y`        | number    | The y value of the point.

## Methods

The following is a list of methods that are part of the Point class.

Name                                         | Return Type         | Description
-------------------------------------------- | ------------------- | ------------------------------------------------------------
`add(point: Point)`                          | [Point](point-class.md)               | Adds the x and y values of two points and returns a new Point.
`clone()`                                    | [Point](point-class.md)               | Returns a copy of the Point object.
`equals(point: Point, tolerance?: number)`   | boolean             | Compares the x and y values of two points to see if they are equal. If a tolerance value is specified, it checks to see if the linear distance between the points is less than or equal to the tolerance value.
`subtract(point: Point)`                     | [Point](point-class.md)               | Subtracts the x and y values of a points and returns a new Point.
`toString()`                                 | string              | Converts the Point object into a string.
