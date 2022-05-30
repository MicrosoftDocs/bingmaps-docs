---
title: "TileLayerOptions Object | Microsoft Docs"
description: "Describes the TileLayerOptions object and provides a table that outline the type and description for various objects."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 0493d1b0-1380-42a9-9f2a-8ad49d622853
caps.latest.revision: 8
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# TileLayerOptions Object

The following is a list of option properties that can be used with a TileLayer.

Name                | Type          | Description
------------------- | ------------- | ----------------------------------------
`downloadTimeout`   | number        | The number of milliseconds allowed for the tile layer image download. If the timeout occurs before the image is fully downloaded, the map control considers the download a failure. The default value is 10000. 
`enableCors` | boolean | Allow retrieving data from CORS supported server.
`mercator`          | [TileSource](tilesource-class.md)    | The tile source for the tile layer. Can only be set when TileLayer is initially created.
`opacity`           | number        | The opacity of the tile layer, defined by a number between 0 (not visible) and 1.
`useCredentialsForCORS` | boolean | Specifies that CORS should be made with the "use-credentials" flag instead of "anonymous".
`visible`           | boolean       | A boolean indicating whether to show or hide the tile layer. The default value is true. A value of false indicates that the tile layer is hidden, although it is still an entity on the map.
`zIndex`            | number        | The z-index of the tile layer. See also: [zIndexing in Bing Maps V8](../articles/zindexing-in-bing-maps-v8.md) 	
