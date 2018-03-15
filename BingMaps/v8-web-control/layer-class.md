---
title: "Layer Class | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 513b79ac-9df6-4dee-bcdd-df0afc1147e9
caps.latest.revision: 14
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# Layer Class
The Layer class makes it easy to organize groups of data by storing them in separate layers on the map. Grouping your data into layers provides a number of benefits such as the ability to hide or attach events to all `IPrimitive` shapes in a layer with a single line of code, while also providing providing a performance benefit over manually looping through each shape and performing these tasks.

## Constructor

> `Layer(id?: string)`

## Properties

Name               | Type             | Description
------------------ | ---------------- | -------------------------------
`metadata`         | object           | Optional property to store any additional metadata for this layer.

## Methods

Name                                                     | Return Type       | Description
-------------------------------------------------------- | ----------------- | ---------------------------------
`add(data: IPrimitive or IPrimitive[], index?: number)`  |                   | Adds a shapes to the layer, at the specified index if specified.<br/><br/> • **data**: The shape(s) to be added to the layer.<br/> • **index**: The index at which to insert the shape into the layer.
`clear()`                                                |                   | Removes all the data in the layer. 
`dispose()`                                              |                   | Cleans up any resources this object is consuming.
`getId()`                                                | string            | Gets the id of the layer. 
`getPrimitives()`                                        | [IPrimitive](../v8-web-control/iprimitive-class.md)[]      | Gets an array of shapes that are in the layer. This can be used to iterate over the individual shapes.
`getVisible()`                                           | boolean           | Gets a value indicating whether the layer is visible or not.
`getZIndex()`                                            | number            | Gets the zIndex of the layer.
`remove(primitive: IPrimitive)`                          | [IPrimitive](../v8-web-control/iprimitive-class.md)        | Removes a shape from the layer and returns it.
`removeAt(index: number)`                                | [IPrimitive](../v8-web-control/iprimitive-class.md)        | Removes a shape from the layer at the specified index. 
`setPrimitives(primitives: IPrimitive[])`                |                   | Replaces all shapes in the layer with the new array of shapes that have been provided.
`setVisible(value: boolean)`                              |                   | Sets whether the layer is visible or not.
`setZIndex(zIndex: number)`                               |                   | Sets the zIndex of the layer. See also: [zIndexing in Bing Maps V8](../v8-web-control/zindexing-in-bing-maps-v8.md) 

## Events ##

The Layer class allows you to add events which are triggered when interacting with the `IPimitive` shapes that are in the layer. The benefit of this is that you only need to add the event on the layer and not on each individual shape. This results in less memory being used by the application and slightly faster response times by the events.

| Name   | Arguments    | Description   |
|--------|--------------|---------------|
| `click`      | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the mouse is used to click the map or when a touch end event occurs on an IPrimitive shape in the layer.               |
| `dblclick` | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md)| Occurs when the mouse is used to double click the map or when a touch end event occurs on an IPrimitive shape in the layer. |
| `mousedown`  | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the left mouse button is pressed or a touch start event occurs on an IPrimitive shape in the layer.                    |
| `mouseover`  | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the mouse cursor moves over top of the area covered by an IPrimitive shape in the layer.                               |
| `mouseout`   | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the mouse cursor moves out of the area covered by an IPrimitive shape in the layer.                                    |
| `mouseup`    | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the left mouse button is lifted up or when the touch end event occurs on an IPrimitive shape in the layer.             |
| `rightclick` | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the right mouse button is used to click the map or when a long touch press occurs on an IPrimitive shape in the layer. |


**_Note for Bing Maps V7 developers_**: In the Bing Maps V7 SDK, a class called `EntityCollection` was used to create data layers on the map. This class has been deprecated and replaced with the `Layer` class. However, to minimize migration efforts we have added an `EntityCollection` class for backwards compatibility which wraps the `Layer` class. This wrapper flattens all child entity collections of an `EntityCollection` into a single layer. This may result in some rendering differences when compared to V7. This `EntityCollection` class should only be used if migrating an app from V7 that requires minimal code changes.

## See Also

  * [Layer Examples](../v8-web-control/layers.md)
