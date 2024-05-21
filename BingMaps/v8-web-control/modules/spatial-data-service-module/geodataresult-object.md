---
title: "GeoDataResult Object | Microsoft Docs"
description: Describes the GeoDataResult object, which represents a single result GeoData API object, and includes descriptions for each of its properties.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: fcf705c1-ef17-4458-ba28-480e4c4ffb3a
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# GeoDataResult Object

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../../includes/bing-maps-web-control-sdk-retirement.md)]

Represents a single result object returned by the [GeoData API](../../../spatial-data-services/geodata-api.md). 

## Properties

Name               | Type                      | Description
------------------ | ------------------------- | --------------------------------
`Copyright`          | [Copyright](copyright-object.md)                | Copyright information for the returned boundary data.
`EntityID`           | string                    | A unique ID number associated with this entity. 
`EntityMetadata`     | [Metadata](metadata-object.md)                 | A collection of metadata information associated with the entity. The `getEntityMetadata` option of the request must be set to **true**.
`Name`               | [Name](name-object.md)                     | Information about the name of the boundary location.
`Polygons`           | [Polygon](../../map-control-api/polygon-class.md)[]                 | A Polygon object that has been generated from the data in the Primitives property.
`Primitives`         | [GeoDataPrimitive](geodataprimitive-object.md)[]       | An array of objects that contain the polygon information for the boundary.

> [!NOTE]
> The `Name` and `EntityMetadata` properties are not available for all boundary data. 