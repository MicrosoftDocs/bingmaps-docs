---
title: "Spatial Data Services Module Examples | Microsoft Docs"
description: Provides a list of examples for the Spatial Data Services module, which allows developers to upload data and expose it as a spatial REST service.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 84745a30-baa1-4215-93aa-71c80cf56c07
caps.latest.revision: 7
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Spatial Data Services Module Examples

The Bing Spatial Data Services allow you to upload data and have it exposed as a spatial REST service for use in your application. These data sources are initially only accessible through the [Query REST API](../../../spatial-data-services/query-api/index.md) of the service using only your Bing Maps key, however you can make them publicly available which allows any Bing Maps key to access the data. There ar several data sources public data sources available in the Bing Maps, so of these are documented here. In addition to its hosting and spatial REST service capabilities, the Bing Spatial Data services also provides access to administrative boundary data such as state and country boundaries through the [GeoData REST API](geodata-api/index.md). 

This module wraps the [Query](../../../spatial-data-services/query-api/index.md) and [GeoData](../../../spatial-data-services/geodata-api.md) REST API’s in the Bing Spatial Data Services and exposes them as an easy to use JavaScript library. It handles all data conversions to and from shapes in Bing Maps to the format required by these services (Well Known Text or Encoded Strings). 


## Examples

   * [Filter Example](filter-example.md) 

**Query API**
  * [Find By Property](query-api/find-by-property-example.md)
  * [Find Nearby](query-api/find-nearby-example.md)
  * [Basic Intersection Search](query-api/basic-intersection-search-example.md)
  * [Along a Route Search](query-api/along-a-route-search.md)
  * [Choropleth Map](query-api/choropleth-map-example.md)
  * [Paged Search Results](query-api/paged-search-results-example.md)
  
**GeoData API**
  * [Load a Single Boundary from the GeoData Service](geodata-api/load-single-boundary-geodata-example.md)
  * [Load Multiple Boundaries from the GeoData Service](geodata-api/load-multiple-boundaries-geodata-example.md)
  * [Search Boundary](geodata-api/search-boundary-example.md)

## Related Topics

  * [QueryAPIManager Class](../../modules/spatial-data-service-module/queryapimanager-class.md)
  * [QueryAPIOptions Object](../../modules/spatial-data-service-module/queryapioptions-object.md)
  * [SpatialFilterOptions Object](../../modules/spatial-data-service-module/spatialfilteroptions-object.md)
  * [GeoDataApiManager Class](../../modules/spatial-data-service-module/geodataapimanager-class.md)
  * [GetBoundaryRequestOptions Object](../../modules/spatial-data-service-module/getboundaryrequestoptions-object.md) 
  * [Filter Class](../../modules/spatial-data-service-module/filter-class.md)
  * [FilterGroup Class](../../modules/spatial-data-service-module/filtergroup-class.md)
   