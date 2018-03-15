---
title: "GeoDataPrimitive Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 446a2621-cf5c-4df4-9e75-138ad91a54e4
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# GeoDataPrimitive Object
Represents the primitive object for a boundary returned by the [GeoData API](../spatial-data-services/geodata-api.md). 

## Properties

Name                | Type           | Description
------------------- | -------------- | -----------------------------
`PrimitiveID`       | string         | A unique ID associated with this polygon primitive. 
`Shape`             | string         | A comma-delimited sequence starting with the version number of the polygon set followed by a list of compressed polygon "rings" (closed paths represented by sequences of latitude and-longitude points).
`NumPoints`         | string         | The number of vertex points used to define the polygon.
`SourceID`          | string         | An ID identifying the data provider that supplied the data. This ID number will reference one of the sources listed in the array of `CopyrightSources` in the `Copyright` property of the [GeoDataResultSet](../v8-web-control/geodataresultset-object.md) object.

