---
title: "Metadata Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: f13b5a2f-5ed7-4cf0-a2d4-80936bf2d787
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# Metadata Object
Represents the metadata object for a boundary returned by the [GeoData API](../spatial-data-services/geodata-api.md). 

## Properties

Name                  | Type             | Description
--------------------- | ---------------- | ---------------------------
`AreaSqKm`            | string           | The approximate total surface area (in square kilometers) covered by all the polygons that comprise this entity.
`BestMapViewBox`      | string           | An area on the Earth that provides the best map view for this entity. This area is defined as a bounding box in the format of a “MULTIPOINT ((WestLongitude SouthLatitude), (EastLongitude NorthLatitude))”.
`OfficialCulture`     | string           | The culture associated with this entity. <br/><br/>**Example**: en
`PopulationClass`     | string           | The approximate population within this entity. <br/><br/>**Example**: PopClass20000to99999
`RegionalCulture`     | string           | The regional culture associated with this entity.

> [!NOTE]
> Not all properties will be returned for all results.