---
title: "TileSourceOptions Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: c5c52169-d860-4a41-ab86-6a46d4eef26c
caps.latest.revision: 8
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# TileSourceOptions Object
The following is a list of option properties that can be used with a TileSource.

Name              | Type                    | Description
----------------- | ----------------------- | ---------------------------
`bounds`          | [LocationRect](../v8-web-control/locationrect-class.md) | A bounding box that specifies where tiles are available. <br/><br/>Note: This will not crop tiles to the specific bounding box, it limits the tiles it loads to those that intersect this bounding box.
`maxZoom`         | number                  | The maximum zoom level tiles that tiles should be rendered at.
`minZoom`         | number                  | The minimum zoom level tiles that tiles should be rendered at.
`uriConstructor`  | string _or_ function([PyramidTileId](../v8-web-control/pyramidtileid-class.md)): string    | **Required**. This can be a string or a callback function that constructs the URLs used to retrieve tiles from the tile source. When using a string, the uriConstructor will allow you to specify placeholders that will be replaced with the tiles value (i.e. {quadkey}). See the Tile URL Parameters section for a list of supported parameters. <br/><br/>Besides using formatted tile URLs, you can also specify a callback function as the uriConstructor. This is useful if you need to be able to build custom tile URL’s that may require some additional calculations for a tile.<br/><br/>**Note**: When rendered on a high DPI screen such as a mobile device, the map may request tiles from a higher zoom level and scale them down to increase the DPI of your tile layer and create a crisper image.

**_Tip_**: Setting the `bounds`, `minZoom` and `maxZoom` of a tile source is useful if you only have tiles available in a specific area, as this will prevent tiles for outside of that area from being requested. This will result in less requests being made to your tile server for tiles that don't exist or are not needed.

## Tile URL Parameters

The following is a list of all the possible tile URL parameters that are supported by the [TileSource](../v8-web-control/tilesource-class.md) class and can be in the `uriConstructor` URL.

URL           | Parameter Description
------------- | -------------------------
`{x}`	          | X position of tile. Tile URL usually also needs {y} and {zoom}.
`{y}`	          | Y position of tile. Tile URL usually also needs {x} and {zoom}.
`{zoom}`        | Zoom level of tile. Tile URL usually also needs {x} and {y}.
`{quadkey}`     | Tile quadkey id.
`{subdomain}`   | Used to specify a subdomain. Provides a number between 0 and 3.
`{mkt}`         | The culture of the map.
`{ur}`          | The user region setting of the map.
`{bbox}`        | A bounding box string with the format "{west},{south},{east},{north}". This is useful when working with WMS imagery services.