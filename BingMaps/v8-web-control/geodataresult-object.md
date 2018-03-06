---
title: "GeoDataResult Object | Microsoft Docs"
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
---
# GeoDataResult Object
Represents a single result object returned by the [GeoData API](../spatial-data-services/geodata-api.md). 

## Properties

Name               | Type                      | Description
------------------ | ------------------------- | --------------------------------
`Copyright`          | [Copyright](../v8-web-control/copyright-object.md)                | Copyright information for the returned boundary data.
`EntityID`           | string                    | A unique ID number associated with this entity. 
`EntityMetadata`     | [Metadata](../v8-web-control/metadata-object.md)                 | A collection of metadata information associated with the entity. The `getEntityMetadata` option of the request must be set to **true**.
`Name`               | [Name](../v8-web-control/name-object.md)                     | Information about the name of the boundary location.
`Polygons`           | [Polygon](../v8-web-control/polygon-class.md)[]                 | A Polygon object that has been generated from the data in the Primitives property.
`Primitives`         | [GeoDataPrimitive](../v8-web-control/geodataprimitive-object.md)[]       | An array of objects that contain the polygon information for the boundary.

> [!NOTE]
> The `Name` and `EntityMetadata` properties are not available for all boundary data. 