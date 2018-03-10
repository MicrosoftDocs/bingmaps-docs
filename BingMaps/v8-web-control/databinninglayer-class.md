---
title: "DataBinningLayer Class | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 042436f7-607e-4ffe-8e0c-fbbec37f4509
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# DataBinningLayer Class
The DataBinningLayer class which makes it easy to create data bins from arrays of pushpins. The generated data bins extend from the polygon class and support all polygon options and events.

## Constructor

> DataBinningLayer(pushpins?: [Pushpin](../v8-web-control/pushpin-class.md)\[\], options?: [DataBinningOptions](../v8-web-control/databinningoptions-object.md))

## Methods

| Name                                     | Return Type         | Description                                                                   |
|------------------------------------------|---------------------|-------------------------------------------------------------------------------|
| `clear()`                                  |                     | Removes all the data in the layer.                                            |
| `dispose()`                                |                     | Cleans up any resources this object is consuming.                             |
| `getOptions()`                             | [DataBinningOptions](../v8-web-control/databinningoptions-object.md) | Retrieves the options used by the data binning layer.                         |
| `getPushpins()`                            | [Pushpin](../v8-web-control/pushpin-class.md)\[\]         | Retrieves all the pushpins that have been passed into the data binning layer. |
| `getPrimitives()`                          | [DataBinPolygon](../v8-web-control/databinpolygon-class.md)\[\]  | Returns an array containing all the data bin polygons.                        |
| `getVisible()`                             | boolean             | Gets a value indicating whether the layer is visible or not.                  |
| `getZIndex()`                              | number              | Gets the zIndex of the layer.                                                 |
| setOptions(options: [DataBinningOptions](../v8-web-control/databinningoptions-object.md)) |                     | Sets the options used for calculating and rendering the data bins.            |
| setPushpins(pushpins: [Pushpin](../v8-web-control/pushpin-class.md)\[\])       |                     | Sets the array of pushpins that are used to generate the data bins.           |
| `setVisible(value: boolean)`               |                     | Sets whether the layer is visible or not.                                     |
| `setZIndex(zIndex: number)`                |                     | Sets the zIndex of the layer. See also: [zIndexing in Bing Maps V8](../v8-web-control/zindexing-in-bing-maps-v8.md)                                                 |

## Events

The DataBinningLayer extends from the Layer class and allows supports all the same events.

| Name       | Arguments           | Description                                                                                                               |
|------------|---------------------|---------------------------------------------------------------------------------------------------------------------------|
| `click`      | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the mouse is used to click the map or when a touch end event occurs on a data bin in the layer.               |
| `dblclick`   | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the mouse is used to double click the map or when a touch end event occurs on a data bin in the layer.        |
| `mousedown`  | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the left mouse button is pressed or a touch start event occurs on a data bin in the layer.                    |
| `mouseover`  | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the mouse cursor moves over top of the area covered by a data bin in the layer.                               |
| `mouseout`   | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the mouse cursor moves out of the area covered by a data bin in the layer.                                    |
| `mouseup`    | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the left mouse button is lifted up or when the touch end event occurs on a data bin in the layer.             |
| `rightclick` | [MouseEventArgs](../v8-web-control/mouseeventargs-object.md) | Occurs when the right mouse button is used to click the map or when a long touch press occurs on a data bin in the layer. |