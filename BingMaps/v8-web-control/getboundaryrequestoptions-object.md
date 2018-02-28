---
title: "GetBoundaryRequestOptions Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 2f17663f-9ec7-4ca4-aa7f-6133d9ddcb99
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# GetBoundaryRequestOptions Object
Represents the options for requests boundary data from the [GeoData API](Geodata%20API%20\(Preview\).xml) in the Bing Spatial Data Services.

## Properties
Name                | Type               | Description
------------------- | ------------------ | --------------------------
`lod`               | number             | The level of detail for the boundary polygons returned. An integer between 0 and 3, where 0 specifies the coarsest level of boundary detail and 3 specifies the best. Default: **0**
`entityType`        | string             | The entity type to return. Default: **CountryRegion**<br/><br/>Supported entity types:<br/><br/>&nbsp; • **AdminDivision1**: First administrative level within the country/region level, such as a state or a province.<br/>&nbsp; • **AdminDivision2**: Second administrative level within the country/region level, such as a county.<br/>&nbsp; • **CountryRegion**: Country or region.<br/>&nbsp; • **Neighborhood**: A section of a populated place that is typically well-known, but often with indistinct boundaries. <br/>&nbsp; • **PopulatedPlace**: A concentrated area of human settlement, such as a city, town or village.<br/>&nbsp; • **Postcode1**: The smallest post code category, such as a zip code. <br/>&nbsp; • **Postcode2**: The next largest post code category after Postcode1 that is created by aggregating Postcode1 areas. <br/>&nbsp; • **Postcode3**: The next largest post code category after Postcode2 that is created by aggregating Postcode2 areas.<br/>&nbsp; • **Postcode4**: The next largest post code category after Postcode3 that is created by aggregating Postcode3 areas.<br/><br/>**Note**: Not all entity types are available in all areas.
`culture`           | string             | Specifies the preferred language to use for any metadata text about the entity or polygons. Defaults to the culture used by the map control, which usually automatically detected based on user's browser settings. Setting this property will override the default value.
`getAllPolygons`    | boolean            | Specifies whether the response should include all of the boundary polygons for the requested entity or just return a single polygon that represents the main outline of the entity. Default: **false**
`getEntityMetadata` | boolean            | Specifies whether the response should include metadata about the entity, such as AreaSqKm and others. Default: **false**
`userRegion`        | string             | Specifies the user’s home country or region. Defaults to the region setting of the user who loads the map. <br/><br/>**Warning**: Setting this property will override the default value, which is the region the user is actually in, and will allow the user to see boundaries which may not align with the views of their region. This could result in geopolitically sensitive borders being returned.

**Note**: Some boundaries consist of multiple polygons. By default, only the first polygon will be returned. Set the `getAllPolygons` property to **true** to have all the polygons that make up the boundary returned.