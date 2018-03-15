---
title: "DrawingManager Class | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 5f86a42d-89eb-4125-9565-4aa60f84f24b
caps.latest.revision: 7
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# DrawingManager Class
The **DrawingManager** class manages the ability to draw and edit multiple shapes on the map. Shapes managed by this class are rendered on a separate drawing layer. User can use a mouse or a touch screen to draw on the map. When they are done, double clicking the map, pressing the escape button or any button on the toolbar will exit the current drawing mode. This class does not have a publicly accessible constructor and can only be accessed using the `showDrawingManager` of the [DrawingTools](../v8-web-control/drawingtools-class.md) class.

## Methods

The **DrawingManager** class has the following methods.

| Name                                                 | Return Type    | Description                                              |
|------------------------------------------------------|----------------|----------------------------------------------------------|
| add(data: [IPrimitive](../v8-web-control/iprimitive-class.md) _or_ [IPrimitive](../v8-web-control/iprimitive-class.md)\[\], index?: number) |                | Adds a shapes to the layer, at the specified index if specified.<br/><br/>&nbsp; • **data** – The shape(s) to be added to the layer.<br/>&nbsp; • **index** – The index at which to insert the shape into the layer. |
| `dispose()`                                            |                | Disposes the drawing manager instance.                 |
| `clear()`                                              |                | Resets the drawing manager and clears all shapes in the drawing layer. |
| `getDrawingMode()`                                     | [DrawingMode](../v8-web-control/drawingmode-enumeration.md)    | Gets the current drawing mode of the drawing manager.  |
| `getPrimitives()`                                      | [IPrimitive](../v8-web-control/iprimitive-class.md)\[\] | Gets an array of shapes that are in the layer. This can be used to iterate over the individual shapes.  |
| indexOf(primitive: [IPrimitive](../v8-web-control/iprimitive-class.md), fromIndex?: number)       | number         | Returns the index of the shape in the drawing layer. Returns -1 if shape is not found. |
| remove(primitive: [IPrimitive](../v8-web-control/iprimitive-class.md))                        | [IPrimitive](../v8-web-control/iprimitive-class.md)     | Removes a shape from the layer and returns it.           |
| `removeAt(index: number)`                              | [IPrimitive](../v8-web-control/iprimitive-class.md)     | Removes a shape from the layer at the specified index. |
| setDrawingMode(mode: [DrawingMode](../v8-web-control/drawingmode-enumeration.md))                    |                | Sets the drawing mode of the drawing manager.            |
| setOptions(options: [DrawingManagerOptions](../v8-web-control/drawingmanageroptions-object.md)) | | Sets the drawing tool options. |
| setPrimitives(primitives: [IPrimitive](../v8-web-control/iprimitive-class.md)\[\])            |                | Replaces all shapes in the layer with the new array of shapes that have been provided. |

## Events

The DrawingManager class provides the following events.

| Name                 | Type        | Description                                        |
|----------------------|-------------|----------------------------------------------------|
| `disposed`           |             | Occurs when the drawing manager has been disposed.                                                 
| `drawingChanged`     | [IPrimitive](../v8-web-control/iprimitive-class.md)  | Occurs after the shape has had a change. For example, finished dragging a vertex to a new location. |
| `drawingChanging`    | [IPrimitive](../v8-web-control/iprimitive-class.md)  | Occurs when the shape is being actively manipulated. For example, this event will continuously fire when dragging a vertex of a shape. |
| `drawingEnded`       | [IPrimitive](../v8-web-control/iprimitive-class.md)  | Occurs when the user has finished drawing or editing a shape. |
| `drawingErased`      | [IPrimitive](../v8-web-control/iprimitive-class.md)  | Occurs when a shape is erased.    |
| `drawingModeChanged` | [DrawingMode](../v8-web-control/drawingmode-enumeration.md) | Occurs when the drawing mode has changed.    |
| `drawingStarted`     | [IPrimitive](../v8-web-control/iprimitive-class.md)  | Occurs when the user has started drawing or editing a shape.    |

