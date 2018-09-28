---
title: "Spatial Data Service Module | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 20f6f190-17e2-4cb5-a82a-a46ae62fdb7e
caps.latest.revision: 6
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Spatial Data Service Module
**Module Name**: Microsoft.Maps.SpatialDataService

**Namespace**: Microsoft.Maps.SpatialDataService

The Bing Spatial Data Services allow you to upload data and have it exposed as a spatial REST service for use in your application. These data sources are initially only accessible through the [Query REST API](../spatial-data-services/query-api.md) of the service using only your Bing Maps key, however you can make them publicly available which allows any Bing Maps key to access the data. There ar several data sources public data sources available in the Bing Maps, so of these are documented here. In addition to its hositng and spatial REST service capabilities, the Bing Spatial Data services also provides access to administrative boundary data such as state and acountry boundaries through the [GeoData REST API](geodata-api.md). 

This module wraps the [Query](../spatial-data-services/query-api.md) and [GeoData](geodata-api.md) REST API’s in the Bing Spatial Data Services and exposes them as an easy to use JavaScript library. It handles all data conversions to and from shapes in Bing Maps to the format required by these services (Well Known Text or Encoded Strings). 

## Static Classes

The following static classes are exposed through the Microsoft.Maps.SpatialDataService namespace.

Name                                                | Description
--------------------------------------------------- | ------------------------
[QueryAPIManager](../v8-web-control/queryapimanager-class.md)	    | Provides that ability to query data sources that are hosted by the Bing Spatial Data Services using the Query API.
[GeoDataAPIManager](../v8-web-control/geodataapimanager-class.md)  | Provides the ability to request polygons that describe the boundaries of a geographic entities, such as an AdminDivision1 (such as a state or province) or a Postcode1 (such as a zip code) that contain a given point (latitude and longitude) or address. This uses the GeoData API in the Bing Spatial Data Services.

##  Classes

The following classes are available in the Microsoft.Maps.SpatialDataServices namespace.

Name                                       | Description
------------------------------------------ | --------------------------
[Filter](../v8-web-control/filter-class.md)            | A class that defines the logic for a filter that can generate a string version of the filter logic that is compatible with the Bing spatial Data Services and can also process the filter logic against a JSON object.
[FilterGroup](../v8-web-control/filtergroup-class.md)     | A class that defines the group of filters, and can generate a string version of the filter logic that is compatible with the Bing spatial Data Services and can also process the filter logic against a JSON object.
[GetBoundaryRequestOptions](../v8-web-control/getboundaryrequestoptions-object.md) | Contains options for boundary data. 
[GeoDataResultSet](../v8-web-control/geodataresultset-object.md)| A set of results returned by the GeoData API.
[GeoDataResult](../v8-web-control/geodataresult-object.md) | A specific result returned by the GeoData API.
[Metadata](../v8-web-control/metadata-object.md) | Contains metadata for a boundary returned by the GeoData API.   
[Name](../v8-web-control/name-object.md) | The name for a boundary returned by the GeoData API. 
[GeoDataPrimitive](../v8-web-control/geodataprimitive-object.md) | Describes a primitive for a boundary returned by the GeoData API.  
[Copyright](../v8-web-control/copyright-object.md) | Information on copyright for a boundary returned by the GeoData API.  
[CopyrightSource](../v8-web-control/copyrightsource-object.md) | Represents the copyright source for a boundary returned by the GeoData API.  

## Enumeration

The following enumerations are available in the Microsoft.Maps.SpatialDataServices namespace.

Name                                                                    | Description
----------------------------------------------------------------------- | ----------------------
[FilterCompareOperator](../v8-web-control/filtercompareoperator-enumeration.md)        | Specifies how to compare the filters value against the corresponding property value.
[FilterLogicalOperator](../v8-web-control/filterlogicaloperator-enumeration.md)         | Specifies how two or more filters are linked together.    

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
