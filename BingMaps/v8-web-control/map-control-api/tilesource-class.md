---
title: "TileSource Class | Microsoft Docs"
description: "Describes the TileSource class and provides the class's constructor and a table that outlines the return type and description for various methods."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: cca04203-532a-4842-ac8e-2a838f3909dc
caps.latest.revision: 6
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# TileSource Class

Defines the data source for a tile layer.

## Constructor

> ` TileSource(options:TileSourceOptions)`

The `mercator` property of the TileLayer class takes in a TileSource object. The TileSource class contains all the information needed to define the source of the data for a tile layer. 

##  Methods

The TileSource class has the following methods.  

Name                      | Return Type    | Description
------------------------- | -------------- | -----------------------------------------
`getBounds()`             | [LocationRect](locationrect-class.md)   | Gets the specified bounding box of the of the tile source.
`getHeight()`             | number         | Returns the pixel height of each tile in the tile source.
`getMaxZoom()`            | number         | Gets the maximum zoom level specified for the tile source.
`getMinZoom()`            | number         | Gets the minimum zoom level specified for the tile source.
`getUriConstructor()`     | string _or_  function([PyramidTileId](pyramidtileid-class.md)): string       | Returns a string or callback function that constructs tile URLs used to retrieve tiles for the tile layer.
`getWidth()`              | number         | Returns the pixel width of each tile in the tile source.


## See Also
  * [TileSourceOptions Object](tilesourceoptions-object.md)
