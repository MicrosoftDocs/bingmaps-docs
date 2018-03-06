---
title: "AnimatedTileLayerOptions Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 5a6738a8-b15e-4660-8671-9af583fa131c
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# AnimatedTileLayerOptions Object
An object that defines the options for an [AnimatedTileLayer](../v8-web-control/animatedtilelayer-class.md).

| Name             | Type           | Description                                                                                                            |
|------------------|----------------|------------------------------------------------------------------------------------------------------------------------|
| `autoPlay`         | boolean        | A boolean that specifies whether the animation should auto-start when it is added to the map or not. Default: **true** |
| `frameRate`        | number         | The number of miliseconds between two layer frames. Default: **1000**                                                      |
| `loadingScreen`    | [CustomOverlay](../v8-web-control/customoverlay-class.md)  | A custom loading screen to show on the map when the map tiles are being fetched.                                       |
| `maxTotalLoadTime` | number         | The max amount of total loading time of all tiles in a viewport in milliseconds. Default: **15000**                        |
| `mercator`         | [TileSource](../v8-web-control/tilesource-class.md)\[\] | The array of tile layer sources to animate through.                                                                    |
| `visible`          | boolean        | A boolean specifying if the animated tile layer is visible or not. Default: **true** |
