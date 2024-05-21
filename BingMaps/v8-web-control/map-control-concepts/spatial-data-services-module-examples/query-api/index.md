---
title: "Query API Examples | Microsoft Docs"
description: The overview page for the Query API Examples section contains a description and links to examples and related topics.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: c0fac600-3651-47f6-a63d-f09634936a2b
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Query API Examples

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../includes/bing-maps-web-control-sdk-retirement.md)]

The [Query API](../../../../spatial-data-services/query-api/index.md) is a component of the Bing Spatial Data Services. You can use the Query API to query a data source for information about entities in that data source. For example, if the data source contains restaurant entities, you can query for French restaurants nearby or you can get information about a specific restaurant. Each query response can return a maximum number of 250 results.

Below are some ways you could use the Query API to search a data source that contains information about a set of restaurants.

* Use Query by Area to search for all movie theaters within 20 kilometers. 
* Use Query Near a Route to search for all restaurants along a route.
* Use Query by Property to search for all restaurants within 20 miles that have more than 20 employees.

Bing Maps V8 exposes the Query API through the [QueryAPIManager class](../../../modules/spatial-data-service-module/queryapimanager-class.md) in the Spatial Data Services module.

## Examples

  * [Find By Property](find-by-property-example.md)
  * [Find Nearby](find-nearby-example.md)
  * [Basic Intersection Search](basic-intersection-search-example.md)
  * [Choropleth Map](choropleth-map-example.md)
  * [Paged Search Results](paged-search-results-example.md)

## Related Topics

  * [QueryAPIManager Class](../../../modules/spatial-data-service-module/queryapimanager-class.md)
  * [QueryAPIOptions Object](../../../modules/spatial-data-service-module/queryapioptions-object.md)
  * [SpatialFilterOptions Object](../../../modules/spatial-data-service-module/spatialfilteroptions-object.md)
  * [Filter Class](../../../modules/spatial-data-service-module/filter-class.md)
  * [FilterGroup Class](../../../modules/spatial-data-service-module/filtergroup-class.md)
   