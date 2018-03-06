---
title: "PyramidTileId Class | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 6397f3a5-5bdc-47a4-9f28-9f5f6ce6b99f
caps.latest.revision: 5
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# PyramidTileId Class
Occasionally you may run into a situation where you need to perform additional calculations against the tile information to generate the required tile URL. This can be done by passing a callback function to the `uriConstructor` property. When this callback function is triggered, it receives a PyramidTileId object that contains additional information about the tile that is being requested. You can then use this information to create the required tile URL and return it from the callback function.

## Constructor

> 	`PyramidTileId(x: number, y: number, zoom: number, width?: number, height?: number)`

## Properties

The following is a list of the properties in the PyramidTileId class.

Name            | Type            | Description
--------------- | --------------- | ------------------------
`pixelHeight`   | number          | The height of the tile.
`pixelWidth`    | number          | The width of the tile.
`quadKey`       | string          | The quadkey ID of the tile. 
`x`             | number          | The x tile coordinate.
`y`             | number          | The y tile coordinate.
`zoom`          | number          | The zoom level of the tile.

## Static Methods

Name            | Type            | Description
--------------- | --------------- | ------------------------
`areEqual(tileId1: PyramidTileId, tileId2: PyramidTileId)` | boolean | Compares two PyramidTileId objects and returns a boolean indicating if the two PyramidTileId are equal.
`fromQuadKey(quadkey: string, width?: number, height?: number)` | PyramidTileId | Generates a PyramidTileId from a quadkey tile id string.

## See Also: 

* [Bing Maps Tile System](../articles/bing-maps-tile-system.md)