---
title: "What&#39;s New in Bing Spatial Data Services | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 48b55f8e-a43d-4ad6-8d4f-69445eac736c
caps.latest.revision: 53
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# What&#39;s New in Bing Spatial Data Services
The [Bing Spatial Data Services](../spatial-data-services/index.md) contains the following new features.  
  
 **September 2016**  
  
 **The maximum number of points a geography object can have has increased from 2,000 to 100,000.**  
  
 **March 2016**  
  
 **KML and ESRI Shapefiles can now be uploaded as a data source. ESRI Shapefiles are also automatically reprojected to the WGS84 spherical mercator projection for correct placement on Bing Maps.**  
  
 **November 2013**  
  
 **May 2014**  
  
 **The maximum number of jobs that you can run in a 24 hour period is increased from 5 to 50 for non-enterprise accounts.** See [Geocode and Data Source Limits](../spatial-data-services/geocode-and-data-source-limits.md).  
  
 **November 2013**  
  
 **Use geographical shapes, such as polygons and line strings, to represent entity locations in your data source data schema**  
  
 You can now define location as either a geographical area, such as polygon or line string or a single point (latitude and longitude). For more information, see [Data Schema and Sample Input](data-source-management-api/load-data-source-dataflow/load-data-source-data-schema-and-sample-input.md) and [Geography Types](data-source-management-api/load-data-source-dataflow/geography-types.md).  
  
 Note that geographical shapes are only supported when you upload your data source using the [Bing Spatial Data Services](../spatial-data-services/index.md). You cannot use the Bing Maps Dev Center to upload data sources with a geographical shape type.  
  
 **Use geographical shapes to query data sources.**  
  
 You can use the [Geography Types](data-source-management-api/load-data-source-dataflow/geography-types.md) to query for data source entities within a custom area defined by geographical shapes using the “intersects” spatial filter function.  For more information, see [Query by Area](query-api/query-by-area.md). If you want to return the intersection of an entity’s geographical shape with another geographical shape you specify, use the “intersection” function with the $select query option.  
  
 **Get a list of all public data sources.** You can request a list of all publicly available data sources. This includes the [Public Data Sources](public-data-sources/index.md) owned and managed by Microsoft as well as any data source that is made public using the [Make a Data Source Public](data-source-management-api/make-public-data-source.md) API.  
  
 **Search up to 1000 kilometers when you [Query by Area](query-api/query-by-area.md) or [Query by Property](query-api/query-by-property.md). The previous limit was 400 kilometers.** .  
  
 **June 2013**  
  
 **GeoData API (Preview) gets geographical boundaries.** With the [Geodata API](../spatial-data-services/geodata-api.md), you can get boundary data for a variety of geographical entities from a country or region to postal codes by specifying an address or point (latitude and longitude) inside the entity.  
  
 **May, 2013**  
  
 **Batch geocoding and data source APIs are now available to all users.** Previously only available to enterprise users, the [Geocode Dataflow API](geocode-dataflow-api/index.md) and [Data Source Management API](data-source-management-api/index.md) are now accessible to any user with a Bing Maps Account. Usage is subject to the [Geocode and Data Source Limits](../spatial-data-services/geocode-and-data-source-limits.md).  
  
 For earlier releases, see [Release History](../spatial-data-services/release-history.md) [starting with January, 2013].