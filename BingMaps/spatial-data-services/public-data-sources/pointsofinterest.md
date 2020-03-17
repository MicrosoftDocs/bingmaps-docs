---
title: "PointsOfInterest | Microsoft Docs"
ms.custom: ""
ms.date: "03/05/2020"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ?
caps.latest.revision: 24
author: "eriklind"
ms.author: "eriklind"
manager: "dirabel"
ms.service: "bing-maps"
---
# PointsOfInterest

The PointsOfInterest data source contains information about points of interest (POIs) in many countries of the world (see list of countries below). You can query this data source by using the Bing Spatial Data Services [Query API](../query-api/index.md) and any Bing Maps Key.  

> [!NOTE]
>  For migrating from the deprecated NAVTEQNA and NAVTEQEU data sources to the superceding PointsOfInterest data source, simply update the base query URL in your application from 'f22876ec257b474b82fe2ffcb8393150/NavteqNA/NavteqPOIs' (for NAVTEQNA data source) and 'f22876ec257b474b82fe2ffcb8393150/NavteqEU/NavteqPOIs' (for NAVTEQEU data source) to 'Microsoft/PointsOfInterest/Locations'.
  
> [!IMPORTANT]
>  When you query this data source for specific property values, you must include a geographical area to search. This does not apply if you are querying for specific entities using entity ID. See [Query by Area](../query-api/query-by-area.md) and [Query by ID](../query-api/query-by-id.md) for details. POI entities may not be available for every location.                                              
**Note:**  The PointsOfInterest data sources do not support the intersects and nearRoute filters.  
  
## POI Entity Properties  
 The following table describes the properties that you can query to get information about worldwide points of interest. These properties make up the Microsoft entity type that is used by the PointsOfInterest data source.  
  
|Property|Data Type|Example Value|  
|--------------|---------------|-------------------|  
|EntityID (Primary Key)|Edm.String|111|  
|Name|Edm.String|Coho Vineyard & Winery|  
|DisplayName|Edm.String|Coho Vineyard & Winery|  
|Latitude|Edm.Double|50.792458|  
|Longitude|Edm.Double|-1.146712|  
|AddressLine|Edm.String|1234 Main Street|  
|Locality|Edm.String|Helena|  
|AdminDistrict|Edm.String|Montana|  
|AdminDistrict2|Edm.String|Lewis and Clark|  
|PostalCode|Edm.String|98146|  
|CountryRegion|Edm.String|USA|  
|Phone|Edm.String|800-5550111|  
|EntityTypeID|Edm.String|2084|  
  
## Entity Types  
 For a complete list of the entity type IDs that you can query, see [POI Entity Types](../public-data-sources/poi-entity-types.md).  
  
## How to query the PointsOfInterest data source  
 You can query PointsOfInterest data source by using the following base URL and adding additional parameters such a geographical area to search and the properties you want to return. For a complete description of query options and more examples, see [Query API](../query-api/index.md).  
  
> [!IMPORTANT]
>  When you query this data source for specify property values, you must include a geographical area to search. This does not apply if you are querying for specific entities using entity ID. See [Query by Area](../query-api/query-by-area.md) and [Query by ID](../query-api/query-by-id.md) for details.  
  
 **Base Query URL**  
  
```url 
http://spatial.virtualearth.net/REST/v1/data/Microsoft/PointsOfInterest/Locations  
```  
  
 **Query Example**  
  
 The following query example queries for banks within 5 kilometers of the specified latitude and longitude. The query key you use can be any Bing Maps Key. For complete information about querying a data source, see [Query API](../query-api/index.md).  
  
```url
http://spatial.virtualearth.net/REST/v1/data/Microsoft/PointsOfInterest/Locations?spatialFilter=nearby(40.83274904439099,-74.3163299560546935,5)&$filter=EntityTypeID%20eq%20'6000'&$select=EntityID,DisplayName,Latitude,Longitude,__Distance&$top=3&key=anyBingMapsKey  
```
