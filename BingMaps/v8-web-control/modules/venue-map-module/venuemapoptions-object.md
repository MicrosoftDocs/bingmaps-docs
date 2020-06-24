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
Options used to customize how a [Venue](../../venues/venue.md) file is read and loaded via the [VenueMapFactory](venuemapfactory-class.md).

When hosting a venue map at a custom endpoint, one needs to ensure that the data hosted at `metadataUrl` can be loaded using the method defined in `metadataLoader`. Specifically, one should pay attention to the case where their data is hosted on a different domain where CORS is not enabled. In this case, the hosting site should create another webpage triggered by an additional parameter (referred to below as the JSONP URL parameter) which allows for the file to be downloaded across domains.

## Properties
Name                               | Type           | Description
---------------------------------- | --------------------- | -----------------------------------
`error` | function() | The callback function invoked after venue map creation fails.
`metadataLoader` | **VenueMapMetadataLoader** | Method called to invoke loading of [Venue](../../venues/venue.md) metadata. If not specified, `Network.downloadJsonp` is invoked.
`metadataUrl` | string OR function() => string | The custom url endpoint that returns a string or a function that returns a string. If the [Venue](../../venues/venue.md) file is hosted on a different domain, and [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) is not enabled, but does support [JSONP](https://en.wikipedia.org/wiki/JSONP), the name of JSONP URL parameter that can be used to download the file across different domains needs to be specified. 
`showFloorSwitcher` | boolean | If `true`, the floor switcher control is shown when this venue is visible. This property is `false` by default.
`success`| function(VenueMap: [VenueMap](venuemap-class.md) ) | The callback function invoked after a venue map is successfully created.
`venueMapId` | string | The id of the venue map.

<br/>
<br/>

## VenueMapMetdataLoader Method
Parameter                               | Req? | Description
----------------------------------  | :---------------------: | -----------------------------------
`success` | ✔ |The callback function invoked when the data for the venue is to be loaded
`venueMapId` | ✔ | The ID of the venue to load
`error` | |The callback function invoked invoked when there's an error loading the data
`market` | |Country+language code for the current market