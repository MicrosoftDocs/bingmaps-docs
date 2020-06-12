---
title: "Venue Maps Factory Class | Microsoft Docs"
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

# VenueMapFactoryClass
The **VenueMapFactory** class can create instances of the [VenueMap](venuemap-class.md) class and [VenueMapFootprintsLayer](venuemapfootprintslayer-class.md) class.

## Constructor

> VenueMapFactory(map: [Map](../../map-control-api/map-class.md))

When creating a **VenueMapFactory**, the map instance associated with venue map factory must be passed.


## Methods

Below are the list of methods for **VenueMapFactory**.

Name                               | Return Type           | Description
---------------------------------- | ------------ | -----------------------------------
`create(options:` [VenueMapOptions](venuemapoptions-object.md) `)` || Creates a [VenueMap](venuemap-class.md) with specifications defined in `options`.
`createFootprintsLayer(options: ` [VenueMapFootprintsLayerOptions](venuemapfootprintslayeroptions-object.md) `)`| | Creates a [VenueMapFootprintsLayer](venuemapfootprintslayer-class.md) with specifications defined in `options`.