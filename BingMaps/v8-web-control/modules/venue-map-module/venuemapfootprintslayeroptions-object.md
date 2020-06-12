---
title: "Venue Maps Options Object | Microsoft Docs"
ms.custom: ""
ms.date: "06/12/20"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ""
caps.latest.revision: 0
author: "simshap"
ms.author: "simshap"
manager: "cordellj"
ms.service: "bing-maps"
---

# VenueMapFootprintsLayerOptions
Options used to customize how a [venueTile](../../venues/venueTile.md) file is read and loaded via the [VenueMapFactory](venuemapfactory-class.md).

When hosting venue map footprints layer metadata at a custom endpoint, one needs to ensure that the data hosted at `tileUrl` can be loaded using the method defined in `tileLoader`. Specifically, one should pay attention to the case where their data is hosted on a different domain where CORS is not enabled. In this case, the hosting site should create another webpage triggered by an additional parameter (referred to below as the JSONP URL parameter) which allows for the file to be downloaded across domains.


## Properties
Name                               | Type           | Description
---------------------------------- | --------------------- | -----------------------------------
`error` | function() | The callback function invoked after venue map footprints layer creation fails.
`interactive` | boolean | When `true`, the footprints shown on this layer are interactive - meaning they respond to hover + tap events. This property is `true` by default.
`success`| function(layer: **VenueMapFootprintsLayer** ) | The callback function invoked after a venue map footprints layer is succesfully created.
`tileLoader` | **VenueMapTileLoader** | Method called to invoke loading of [venueTile](../../venues/venueTile.md) metadata. If not specified, `Network.downloadJsonp` is invoked.
`tileUrl` | string OR function() => string | The custom url endpoint that returns a string or a function that returns a string. If the [venueTile](../../venues/venueTile.md) metadata is hosted on a different domain, and [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) is not enabled, but does support [JSONP](https://en.wikipedia.org/wiki/JSONP), the name of JSONP URL parameter that can be used to download the file across different domains needs to be specified. 


<br/>
<br/>

## VenueMapTileLoader Method
Parameter                               | Req? | Description
----------------------------------  | :---------------------: | -----------------------------------
`error` | |The callback function invoked invoked when there's an error loading the data
`quadKey` |✔ |Identifies the tile to load
`success` | ✔ |The callback function invoked when the data for the venue tile is to be loaded