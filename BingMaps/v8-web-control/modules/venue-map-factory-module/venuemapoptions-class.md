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



## Properties
Name                               | Type           | Description
---------------------------------- | --------------------- | -----------------------------------
`error` | Function() => `void` | The error callback function after venue map creation fails
`metadataLoader` | test | [VenueMapMetadataLoader Object](venuemapmetadataloader-object.md)