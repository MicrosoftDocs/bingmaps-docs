---
title: "Spatial Data Service Module | Microsoft Docs"
ms.custom: ""
ms.date: "09/26/2018"
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

The Bing Spatial Data Services allow you to upload data and have it exposed as a spatial REST service for use in your application. These data sources are initially only accessible through the [Query REST API](../../../spatial-data-services/query-api/index.md) of the service using only your Bing Maps key, however you can make them publicly available which allows any Bing Maps key to access the data. There ar several data sources public data sources available in the Bing Maps, so of these are documented here. In addition to its hosting and spatial REST service capabilities, the Bing Spatial Data services also provides access to administrative boundary data such as state and country boundaries through the [GeoData REST API](../../../spatial-data-services/geodata-api.md).

This module wraps the [Query](../../../spatial-data-services/query-api/index.md) and [GeoData](../../../spatial-data-services/geodata-api.md) REST API’s in the Bing Spatial Data Services and exposes them as an easy to use JavaScript library. It handles all data conversions to and from shapes in Bing Maps to the format required by these services (Well Known Text or Encoded Strings).

## Static Classes

The following static classes are exposed through the Microsoft.Maps.SpatialDataService namespace.

Name                                                | Description
--------------------------------------------------- | ------------------------
[QueryAPIManager](queryapimanager-class.md)	    | Provides that ability to query data sources that are hosted by the Bing Spatial Data Services using the Query API.
[GeoDataAPIManager](geodataapimanager-class.md)  | Provides the ability to request polygons that describe the boundaries of a geographic entities, such as an AdminDivision1 (such as a state or province) or a Postcode1 (such as a zip code) that contain a given point (latitude and longitude) or address. This uses the GeoData API in the Bing Spatial Data Services.

##  Classes

The following classes are available in the Microsoft.Maps.SpatialDataServices namespace.

Name                                       | Description
------------------------------------------ | --------------------------
[Filter](filter-class.md)            | A class that defines the logic for a filter that can generate a string version of the filter logic that is compatible with the Bing spatial Data Services and can also process the filter logic against a JSON object.
[FilterGroup](filtergroup-class.md)     | A class that defines the group of filters, and can generate a string version of the filter logic that is compatible with the Bing spatial Data Services and can also process the filter logic against a JSON object.
[GetBoundaryRequestOptions](getboundaryrequestoptions-object.md) | Contains options for boundary data. 
[GeoDataResultSet](geodataresultset-object.md)| A set of results returned by the GeoData API.
[GeoDataResult](geodataresult-object.md) | A specific result returned by the GeoData API.
[Metadata](metadata-object.md) | Contains metadata for a boundary returned by the GeoData API.   
[Name](name-object.md) | The name for a boundary returned by the GeoData API. 
[GeoDataPrimitive](geodataprimitive-object.md) | Describes a primitive for a boundary returned by the GeoData API.  
[Copyright](copyright-object.md) | Information on copyright for a boundary returned by the GeoData API.  
[CopyrightSource](copyrightsource-object.md) | Represents the copyright source for a boundary returned by the GeoData API.  

## Enumeration

The following enumerations are available in the Microsoft.Maps.SpatialDataServices namespace.

Name                                                                    | Description
----------------------------------------------------------------------- | ----------------------
[FilterCompareOperator](filtercompareoperator-enumeration.md)        | Specifies how to compare the filters value against the corresponding property value.
[FilterLogicalOperator](filterlogicaloperator-enumeration.md)         | Specifies how two or more filters are linked together.    

## Examples
   * [Filter Example](../../map-control-concepts/spatial-data-services-module-examples/filter-example.md) 

**Query API**
  * [Find By Property](../../map-control-concepts/spatial-data-services-module-examples/query-api/find-by-property-example.md)
  * [Find Nearby](../../map-control-concepts/spatial-data-services-module-examples/query-api/find-nearby-example.md)
  * [Basic Intersection Search](../../map-control-concepts/spatial-data-services-module-examples/query-api/basic-intersection-search-example.md)
  * [Along a Route Search](../../map-control-concepts/spatial-data-services-module-examples/query-api/along-a-route-search.md)
  * [Choropleth Map](../../map-control-concepts/spatial-data-services-module-examples/query-api/choropleth-map-example.md)
  * [Paged Search Results](../../map-control-concepts/spatial-data-services-module-examples/query-api/paged-search-results-example.md)
  
**GeoData API**
  * [Load a Single Boundary from the GeoData Service](../../map-control-concepts/spatial-data-services-module-examples/geodata-api/load-single-boundary-geodata-example.md)
  * [Load Multiple Boundaries from the GeoData Service](../../map-control-concepts/spatial-data-services-module-examples/geodata-api/load-multiple-boundaries-geodata-example.md)
  * [Search Boundary](../../map-control-concepts/spatial-data-services-module-examples/geodata-api/search-boundary-example.md)
