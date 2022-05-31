---
title: "MouseEventArgs Object | Microsoft Docs"
description: "This article describes methods and properties of the MouseEventArg Object."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 71a003b5-6952-47de-b025-61cd1866eadb
caps.latest.revision: 9
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# MouseEventArgs Object

A MouseEventArgs object is returned by many the mouse event handlers.

## Methods

| Name     | Return Type     | Description                                                                |
|----------|-----------------|--------------------------------------------------------------------------------|
| `getX()`   | number          | Returns the x-value of the pixel coordinate, relative to the map, of the mouse |
| `getY()`   | number          | Returns the y-value of the pixel coordinate, relative to the map, of the mouse |

## Properties

| Name      | Type     | Description |
|-----------|----------|-------------|
| `eventName` | string   | The event that occurred.    |
| `isPrimary` | boolean | A boolean indicating if the primary button, such as the left mouse button or a tap on a touch screen, was used during a mouse down or up event.
| `isSecondary` | boolean | A boolean indicating if the secondary mouse button, such as the right mouse button, was used during a mouse down or up event.
| `layer`     | [Layer](layer-class.md) | If the target is a shape, this will be the layer that the shape is in. |
| `location`  | [Location](location-class.md) | The map location of where the event occurred. |
| `pageX`     | number   | The x-value of the pixel coordinate on the page of the mouse cursor. |
| `pageY`     | number   | The y-value of the pixel coordinate on the page of the mouse cursor. |
| `point`     | [Point](point-class.md) | The pixel coordinate of the mouse cursor relative to the top left corner of the map div. |
| `target`    | [Map](map-class.md) _or_ [IPrimitive](iprimitive-class.md) | The object that triggered the event.                                                           |
| `targetType` | string | The type of the object that the event is attached to. Valid values include the following: ‘map’, 'layer', ‘polygon’, ‘polyline’, or ‘pushpin’ |
| `wheelDelta` | number | The number of units that the mouse wheel has changed. |
