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
Options used to customize how a vector tile layer for displaying venue map footprints is read and loaded via the [VenueMapFactory](venuemapfactory-class.md).


## Properties
Name                               | Type           | Description
---------------------------------- | --------------------- | -----------------------------------
`error` | function() | The callback function invoked after venue map creation fails.
`metadataLoader` | **VenueMapMetadataLoader** | Method called to invoke loading of [VMJSON](../../venues/index.md) metadata. If not specified, `Network.downloadJsonp` is invoked.
`metadataUrl` | string OR function() => string | The custom url endpoint that returns a string or a function that returns a string. If the [VMJSON](../../venues/index.md) file is hosted on a different domain, and [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) is not enabled, but does support [JSONP](https://en.wikipedia.org/wiki/JSONP), the name of JSONP URL parameter that can be used to download the file across different domains needs to be specified. 
`success`| function(VenueMap: [VenueMap](venuemap-class.md) ) | The callback function invoked after a venue map is succesfully created.
`venueMapId` | string | The id of the venue map.
<br/>
<br/>
<br/>
<br/>

## VenueMapMetdataLoader Method
Parameter                               | Req? | Description
----------------------------------  | :---------------------: | -----------------------------------
`error` | |The callback function invoked invoked when there's an error loading the data
`market` | |Country+language code for the current market
`success` | ✔ |The callback function invoked when the data for the venue is to be loaded
`venueMapId` | ✔ | The ID of the venue to load