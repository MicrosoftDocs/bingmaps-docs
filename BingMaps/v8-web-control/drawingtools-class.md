---
title: "DrawingTools Class | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: c8d441b2-1436-448a-9e79-e4af5a973d65
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# DrawingTools Class
The DrawingTools class exposes a set of tools for drawing and editing shapes on the map.

## Constructor

> DrawingTools(map: [Map](../v8-web-control/map-class.md))

## Methods

The **DrawingTools** class has the following methods.

| Name                                                    | Return Type | Description                                                   |
|---------------------------------------------------------|-------------|---------------------------------------------------------------|
| create(shapeType: [ShapeType](../v8-web-control/shapetype-enumeration.md), created?: function(shape: [IPrimitive](../v8-web-control/iprimitive-class.md)))  |             | Initializes the drawing layer and instructs it to create a new shape of a given type. A callback function can be provided which is invoked when the new shape as be initially created. |
| `dispose()` |             | Disposes the instance of the DrawingTools class. |
| edit(shape: [IPrimitive](../v8-web-control/iprimitive-class.md))                               |             | Adds a shape to the drawing layer and puts it into edit mode. |
| finish(finished?: function(shape: [IPrimitive](../v8-web-control/iprimitive-class.md))) | | Finishes any shape create / edit operation currently in progress, and returns the shape that was created or editted. |
| showDrawingManager(function(manager?: [DrawingManager](../v8-web-control/drawingmanager-class.md))) |             | Creates a drawing manager which allows multi-shape editing and displays the toolbar.  |

## Events

The DrawingTools class provides the following events.

| Name               | Type                   | Description                                                                                                                            |
|--------------------|------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| `drawingChanged`     | [IPrimitive](../v8-web-control/iprimitive-class.md)             | Occurs after the shape has had a change. For example, finished dragging a vertex to a new location.                                    |
| `drawingChanging`    | [IPrimitive](../v8-web-control/iprimitive-class.md)             | Occurs when the shape is being actively manipulated. For example, this event will continuously fire when dragging a vertex of a shape. |
| `drawingEnded`       | [IPrimitive](../v8-web-control/iprimitive-class.md)             | Occurs when the user has finished drawing or editing a shape.                                                                          |
| `drawingModeChanged` | [DrawingModeChangedData](../v8-web-control/drawingmodechangeddata-object.md) | Occurs when the drawing mode has changed.                                                                                              |
| `drawingStarted`     | [IPrimitive](../v8-web-control/iprimitive-class.md)             | Occurs when the user has started drawing or editing a shape.     