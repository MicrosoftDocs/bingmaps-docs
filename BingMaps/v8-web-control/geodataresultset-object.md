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
---
# GeoDataResultSet Object
Represents the set of results returned by the [GeoData API](Geodata%20API%20\(Preview\).xml).

## Properties

Name            | Type                  | Description
--------------- | --------------------- | --------------------------------
`Copyright`       | string                | Copyright information for the [GeoData API](Geodata%20API%20\(Preview\).xml).
`location`        | string _or_ [Location](../v8-web-control/location-class.md)  | The location provided in the query that generated this result.
`results`         | [GeoDataResult](../v8-web-control/geodataresult-object.md)[]      | Results of the boundary data.
