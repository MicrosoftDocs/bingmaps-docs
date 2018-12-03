---
title: "GeoDataResultSet Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 02fc4d88-08a6-45f6-aba5-cc3216bc7359
caps.latest.revision: 6
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# GeoDataResultSet Object

Represents the set of results returned by the [GeoData API](../../../spatial-data-services/geodata-api.md).

## Properties

Name            | Type                  | Description
--------------- | --------------------- | --------------------------------
`Copyright`       | string                | Copyright information for the [GeoData API](../../../spatial-data-services/geodata-api.md).
`location`        | string _or_ [Location](../../map-control-api/location-class.md)  | The location provided in the query that generated this result.
`results`         | [GeoDataResult](geodataresult-object.md)[]      | Results of the boundary data.
