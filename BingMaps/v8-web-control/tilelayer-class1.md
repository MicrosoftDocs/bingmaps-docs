---
title: "TileLayer Class1 | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: a1f906d0-cbb1-44b6-91d9-7e91731b89a5
caps.latest.revision: 10
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# TileLayer Class
Represents a tile layer that can be overlaid on top of the map. 

## Constructor

> TileLayer(options: [TileLayerOptions](TileLayerOptions%20Object.md))

## Properties

Name               | Type             | Description
------------------ | ---------------- | -------------------------------
`metadata`         | object           | Optional property to store any additional metadata for this layer.

## Methods

The TileLayer class has the following methods.  

Name                        | Return Type      | Description
--------------------------- | ---------------- | ----------------------------
`getOpacity()`                | number           | Returns the opacity of the tile layer, defined as a double between 0 (not visible) and 1.
`getTileSource()`             | [TileSource](TileSource%20Class.md)       | Returns the tile source of the tile layer.
`getVisible()`                | boolean          | Gets a boolean that indicates if the tile layer is visible or not.
`getZIndex()`                 | number           | Gets the zIndex of the tile layer.
`setOpacity(opacity: number)`  |                  | Sets the opacity of the tile layer. Value must be a number between 0 and 1.
setOptions(opt: [TileLayerOptions](TileLayerOptions%20Object.md)) |            | Sets options for the tile layer. Note that the TileSource can only be set when the tile layer is created and cannot be updated.
`setVisible(show: boolean)`    |                  | Sets the visibility of the tile layer.
`setZIndex(idx: number)`       |                  | Sets the zIndex of the tile layer.

## Examples

  * [Basic Tile Layer Example](../v8-web-control/basic-tile-layer-example.md)
  * [X, Y, Zoom Tile Layer](../v8-web-control/x-y-zoom-tilelayer.md)
  * [WMS Tile Layer Example](../v8-web-control/wms-tile-layer-example.md)
  * [Base Map Tile Layer Example](../v8-web-control/base-map-tile-layer-example.md)

## See Also
  * [TileLayerOptions Object](TileLayerOptions%20Object.md) 
