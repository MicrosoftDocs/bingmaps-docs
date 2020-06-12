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

# VenueMapOptions
Options used to customize how a [VMJSON](../../venues/index.md) file is read and loaded via the [VenueMapFactory](venuemapfactory-class.md).

When hosting a venue map at a custom endpoint, one needs to ensure that the data hosted at `metadataUrl` can be loaded using the method specified by `metadataLoader`. Specifically, one should pay attention to the case where their data is hosted on a different domain where CORS is not enabled. In this case, the hosting site should create another webpage triggered by an additional parameter (referred to below as the JSONP URL parameter) which allows for the file to be downloaded across domains.

## Properties
Name                               | Type           | Description
---------------------------------- | --------------------- | -----------------------------------
`error` | function() | The callback function invoked after venue map creation fails.
`metadataLoader` | [VenueMapMetadataLoader](venuemapmetadataloader-object.md) | Method called to invoke loading of [VMJSON](../../venues/index.md) metadata. If not specified, `Network.downloadJsonp` is invoked.
`metadataUrl` | string OR function() => string | The custom url endpoint that returns a string or a function that returns a string. If the [VMJSON](../../venues/index.md) file is hosted on a different domain, and [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) is not enabled, but does support [JSONP](https://en.wikipedia.org/wiki/JSONP), the name of JSONP URL parameter that can be used to download the file across different domains needs to be specified. 
`success`| function(VenueMap: [VenueMap](venuemap-class.md) ) | The callback function invoked after a venue map is succesfully created.
`venueMapId` | string | The id of the venue map.