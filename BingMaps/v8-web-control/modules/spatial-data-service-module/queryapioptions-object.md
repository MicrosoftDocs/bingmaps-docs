---
title: "QueryAPIOptions Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: c7766e59-59f5-4e44-b9fc-26d556b6cc4f
caps.latest.revision: 5
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# QueryAPIOptions Object

Represents the options for querying a data source that is hosted in the Bing Spatial Data Services.

## Properties

Name                 | Type                      | Description
-------------------- | ------------------------- | -------------------
`queryUrl`           | string                    | **Required**. A query URL containing the access id, data source name and the entity type name. 
`filter`             | string _or_ [Filter](filter-class.md) _or_ [FilterGroup](filtergroup-class.md)   | **Optional**. Specifies a conditional expression for a list of properties and values.
`inlineCount`        | boolean                   | **Optional**. Specifies whether or not to return a count of the results in the response. Default: **false**.
`isStaging`          | boolean                   | **Optional**. Specifies to query the staged version of the data source instead of the published version. Default: **false**.
`orderBy`            | string[]                  | **Optional**. Specifies one or more properties to use to sort the results of a query. You can specify up to three (3) properties. Results are sorted in ascending order. <br/><br/>**Note**: You cannot use the latitude and longitude properties to sort results. You can use the elevation property.
`select`             | string[]                  | **Optional**. Specifies the data source properties to return in the response. If the $select query option is not specified or if it is set to "*" ($select=*), all data source properties are returned. Default: "**\*,_distance**"
`skip`               | number                    | **Optional**. Specifies to not return a specified number of query results. For example, if this value is set to 50, then the first result that is returned is the 51st result. You can use the skip query option with the top query option to display a subset of the query results. For example, the following parameter combinations provide sets of 10 results at a time.<br/><br/>skip=0, top=10 - provides results 1 to 10<br/>skip=10, top=10 - provides results 11 to 20<br/><br/>Default: **0**
`spatialFilter`      | [SpatialFilterOptions](spatialfilteroptions-object.md)     | **Optional**. Spatial filter options to apply.
`top`                | number                    | **Optional**. Specifies the maximum number of results to return in the query response. Default: **25**