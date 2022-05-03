---
title: "Venue Maps Options Object | Microsoft Docs"
ms.custom: ""
ms.date: "06/12/2020"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ""
caps.latest.revision: 0
author: "SimonShapiroMsft"
ms.author: v-munksteve
manager: "cordellj"
ms.service: "bing-maps"
---

# VenueMapOptions
Options used to customize how a [Venue](../../../venues/venue.md) file is read and loaded via the [VenueMapFactory](venuemapfactory-class.md).

When hosting a venue map at a custom endpoint, the venue map can be loader either using `metadataLoader` or `metadataUrl`. Therefore, only one of `metadataLoader` and `metdataUrl` should be included in **VenueMapOptions**. 



Specifically, one should pay attention to the case where their data is hosted on a different domain where CORS is not enabled. In this case, the hosting site should create a templated webpage for hosting the data that is triggered by an additional parameter which allows for the file to be downloaded across domains. The parameter name is defined by the hosting website. The value for that parameter should be set to `{callback}`. See [Load Venue Map Using Metadata Url with JSONP](https://www.bing.com/api/maps/mapcontrol/isdk/) for an example of this.

## Properties
Name                               | Type           | Description
---------------------------------- | --------------------- | -----------------------------------
`error` | function() | The callback function invoked after venue map creation fails.
`metadataLoader` | **VenueMapMetadataLoader** | Method called to invoke loading of [Venue](../../../venues/venue.md) metadata. If not specified, the data will be feteched from the value of `metadataUrl`.
`metadataUrl` | string | The custom url endpoint that returns a string or a function that returns a string. If the url contains the `{callback}` placeholder, it will be fetched as [JSONP](https://en.wikipedia.org/wiki/JSONP). Otherwise, it will be fetched as JSON using [XHR](https://en.wikipedia.org/wiki/XMLHttpRequest). 
`showFloorSwitcher` | boolean | If `true`, the floor switcher control is shown when this venue is visible. This property is `false` by default. 
`success`| function(venueMap: [VenueMap](venuemap-class.md) ) | The callback function invoked after a venue map is successfully created.
`venueMapId` | string | The id of the venue map.

> [!WARNING]
> The floor switcher is only shown if the [navbar](../../map-control-api/navigationbarmode-enumeration.md) is using the `square` style
<br/>

<br/>

## VenueMapMetadataLoader Method
Parameter                               | Req? | Description
----------------------------------  | :---------------------: | -----------------------------------
`venueMapId` | ✔ | The ID of the venue to load
`success` | ✔ |The callback function invoked when the data for the venue is to be loaded
`error` | |The callback function invoked invoked when there's an error loading the data
`market` | |Country+language code for the current market