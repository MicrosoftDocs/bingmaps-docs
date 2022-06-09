---
title: "Venue Maps Factory Class | Microsoft Docs"
description: Describes the Venue Maps factory class, which creates instances of the VenueMap class, and details its constructor and create method.
ms.custom: ""
ms.date: "06/12/2020"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ""
caps.latest.revision: 0
author: "SimonShapiroMsft"
ms.author: "simshap"
manager: "cordellj"
ms.service: "bing-maps"
---

# VenueMapFactoryClass
The **VenueMapFactory** class can create instances of the [VenueMap](venuemap-class.md) class.

## Constructor

> VenueMapFactory(map: [Map](../../map-control-api/map-class.md))

When creating a **VenueMapFactory**, instaces created by the factory will be shown on the map associated with the factory.


## Methods

Below are the list of methods for **VenueMapFactory**.

Name                               | Return Type           | Description
---------------------------------- | ------------ | -----------------------------------
`create(options:` [VenueMapOptions](venuemapoptions-object.md) `)` || Creates a [VenueMap](venuemap-class.md) with specifications defined in `options`.
