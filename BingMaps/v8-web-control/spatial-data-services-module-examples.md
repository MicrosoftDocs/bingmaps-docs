---
title: "Spatial Data Services Module Examples | Microsoft Docs"
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
ms:service: "bing-maps"
---
# Spatial Data Services Module Examples
The Bing Spatial Data Services allow you to upload data and have it exposed as a spatial REST service for use in your application. These data sources are initially only accessible through the [Query REST API](../spatial-data-services/query-api.md) of the service using only your Bing Maps key, however you can make them publicly available which allows any Bing Maps key to access the data. There ar several data sources public data sources available in the Bing Maps, so of these are documented here. In addition to its hositng and spatial REST service capabilities, the Bing Spatial Data services also provides access to administrative boundary data such as state and acountry boundaries through the [GeoData REST API](geodata-api.md). 

This module wraps the [Query](../spatial-data-services/query-api.md) and [GeoData](geodata-api.md) REST API’s in the Bing Spatial Data Services and exposes them as an easy to use JavaScript library. It handles all data conversions to and from shapes in Bing Maps to the format required by these services (Well Known Text or Encoded Strings). 


## Examples

   * [Filter Example](../v8-web-control/filter-example.md) 

**Query API**
  * [Find By Property](../v8-web-control/find-by-property-example.md)
  * [Find Nearby](../v8-web-control/find-nearby-example.md)
  * [Basic Intersection Search](../v8-web-control/basic-intersection-search-example.md)
  * [Along a Route Search](../v8-web-control/along-a-route-search.md)
  * [Choropleth Map](../v8-web-control/choropleth-map-example.md)
  * [Paged Search Results](../v8-web-control/paged-search-results-example.md)
  
**GeoData API**
  * [Load a Single Boundary from the GeoData Service](../v8-web-control/load-single-boundary-geodata-example.md)
  * [Load Multiple Boundaries from the GeoData Service](../v8-web-control/load-multiple-boundaries-geodata-example.md)
  * [Search Boundary](../v8-web-control/search-boundary-example.md)

## Related Topics

  * [QueryAPIManager Class](../v8-web-control/queryapimanager-class.md)
  * [QueryAPIOptions Object](../v8-web-control/queryapioptions-object.md)
  * [SpatialFilterOptions Object](../v8-web-control/spatialfilteroptions-object.md)
  * [GeoDataApiManager Class](../v8-web-control/geodataapimanager-class.md)
  * [GetBoundaryRequestOptions Object](../v8-web-control/getboundaryrequestoptions-object.md) 
  * [Filter Class](../v8-web-control/filter-class.md)
  * [FilterGroup Class](../v8-web-control/filtergroup-class.md)
   