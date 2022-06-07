---
title: "GeoXmlLayer Class | Microsoft Docs"
description: Describes the GeoXmlLayer class, a layer that loads and renders geospatial XML data on the map, including descriptions of its constructor, properties, methods, and events.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 56ad7026-f18e-4cf3-913e-f8395b92c4ab
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# GeoXmlLayer Class

A layer that loads and renders geospatial XML data on the map.

## Constructor

> GeoXmlLayer(dataSource?: string *or* ArrayBuffer, isUrl?: boolean, options?: [GeoXmlLayerOptions](geoxmllayeroptions-object.md))

## Properties

| Name       | Type   | Description                                                        |
|------------|--------|--------------------------------------------------------------------|
| `metadata` | object | Optional property to store any additional metadata for this layer. |

## Methods

| Name                                                                 | Return Type             | Description                                                                |
|----------------------------------------------------------------------|-------------------------|----------------------------------------------------------------------------|
| `clear()`                                                            |                         | Removes all the data in the layer.                                         |
| `dispose()`                                                          |                         | Cleans up any resources this object is consuming.                          |
| `getDataSource()`                                                    | string *or* ArrayBuffer | Returns the data source used by the layer.                                 |
| `getDataSet()`                                                       | [GeoXmlDataSet](geoxmldataset-object.md)           | Returns the data set that ws extracted from the data source.               |
| `getOptions()`                                                       | [GeoXmlLayerOptions](geoxmllayeroptions-object.md)      | Returns the options used by the GeoXmlLayer.                               |
| `getVisible()`                                                       | boolean                 | Gets a value indicating whether the layer is visible or not.               |
| `setDataSource(dataSource: string *or* ArrayBuffer, isUrl: boolean)` |                         | Sets the data source to render in the GeoXmlLayer.                         |
| `setOptions(options: GeoXmlLayerOptions)`                            |                         | Sets the options used for loading and rendering data into the GeoXmlLayer. |
| `setVisible(value: boolean)`                                         |                         | Sets whether the layer is visible or not.                                  |

## Events

The GeoXmlLayer class allows you to add events which are triggered when interacting with the `IPimitive` shapes that are in the layer. The benefit of this is that you only need to add the event on the layer and not on each individual shape. This results in less memory being used by the application and slightly faster response times by the events. Events are not added to Ground or Screen Overlays.

| Name   | Arguments    | Description   |
|--------|--------------|---------------|
| `click`      | [MouseEventArgs](../../map-control-api/mouseeventargs-object.md) | Occurs when the mouse is used to click the map or when a touch end event occurs on an IPrimitive shape in the layer.               |
| `dblclick` | [MouseEventArgs](../../map-control-api/mouseeventargs-object.md)| Occurs when the mouse is used to double click the map or when a touch end event occurs on an IPrimitive shape in the layer. |
| `mousedown`  | [MouseEventArgs](../../map-control-api/mouseeventargs-object.md) | Occurs when the left mouse button is pressed or a touch start event occurs on an IPrimitive shape in the layer.                    |
| `mouseover`  | [MouseEventArgs](../../map-control-api/mouseeventargs-object.md) | Occurs when the mouse cursor moves over top of the area covered by an IPrimitive shape in the layer.                               |
| `mouseout`   | [MouseEventArgs](../../map-control-api/mouseeventargs-object.md) | Occurs when the mouse cursor moves out of the area covered by an IPrimitive shape in the layer.                                    |
| `mouseup`    | [MouseEventArgs](../../map-control-api/mouseeventargs-object.md) | Occurs when the left mouse button is lifted up or when the touch end event occurs on an IPrimitive shape in the layer.             |
| `rightclick` | [MouseEventArgs](../../map-control-api/mouseeventargs-object.md) | Occurs when the right mouse button is used to click the map or when a long touch press occurs on an IPrimitive shape in the layer. |
