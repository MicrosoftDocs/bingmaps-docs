---
title: "PointsOfInterest | Microsoft Docs"
ms.date: "03/25/2020"
ms.topic: "article"
description: "Bing Maps Spatial Data Services PointsOfInterest data source details"
author: "eriklindeman"
ms.author: "eriklind"
manager: "dirabel"
ms.service: "bing-maps"
---

# PointsOfInterest

[!INCLUDE [bing-maps-enterprise-service-retirement](../../includes/bing-maps-enterprise-service-retirement.md)]

The PointsOfInterest data source contains information about points of interest (POIs) for over 150 countries/regions worldwide. POI coverage varies by country/region. You can query this data source by using the Bing Spatial Data Services [Query API](../query-api/index.md) and any Bing Maps Key. The results are limited to 25 points of interest when using a Basic key. Enterprise keys do not have such limit.

> [!IMPORTANT]
>  When you query this data source for specific property values, you must include a geographical area to search. This does not apply if you are querying for specific entities using entity ID. See [Query by Area](../query-api/query-by-area.md) and [Query by ID](../query-api/query-by-id.md) for details. POI entities may not be available for every location.                                              
**Note:**  The PointsOfInterest data source does not support the intersects and nearRoute filters.  
  
## POI Entity Properties  
 The following table describes the properties that you can query to get information about worldwide points of interest. These properties make up the PointsOfInterest entity type that is used by the Microsoft data source.  
  
|Property|Data Type|Example Value|  
|--------------|---------------|-------------------|  
|EntityID (Primary Key)|Edm.String|987654321123456789|  
|Name|Edm.String|Contoso Cafe|  
|DisplayName|Edm.String|Contoso Cafe|  
|Latitude|Edm.Double|47.610005|  
|Longitude|Edm.Double|-122.185992|  
|AddressLine|Edm.String|1234 Main Street|  
|Locality|Edm.String|Bellevue|  
|AdminDistrict|Edm.String|Washington|  
|AdminDistrict2|Edm.String|King|  
|PostalCode|Edm.String|98004|  
|CountryRegion|Edm.String|USA|  
|Phone|Edm.String|+(1)-(425)1231234|  
|EntityTypeID|Edm.String|9996|  
  
## Entity Types  
 For a complete list of the entity type IDs that you can query, see [POI Entity Types](../public-data-sources/poi-entity-types.md).  
  
## How to query the PointsOfInterest data source  
 You can query PointsOfInterest data source by using the following base URL and adding additional parameters such a geographical area to search and the properties you want to return. For a complete description of query options and more examples, see [Query API](../query-api/index.md).  
  
> [!IMPORTANT]
>  When you query this data source for specify property values, you must include a geographical area to search. This does not apply if you are querying for specific entities using entity ID. See [Query by Area](../query-api/query-by-area.md) and [Query by ID](../query-api/query-by-id.md) for details.  
  
 **Base Query URL**  
  
```url 
http://spatial.virtualearth.net/REST/v1/data/Microsoft/PointsOfInterest
```  
  
 **Query Example**  
  
 The following query example queries for banks within 5 kilometers of the specified latitude and longitude. The query key you use can be any Bing Maps Key. For complete information about querying a data source, see [Query API](../query-api/index.md).  
  
```url
http://spatial.virtualearth.net/REST/v1/data/Microsoft/PointsOfInterest?spatialFilter=nearby(40.83274904439099,-74.3163299560546935,5)&$filter=EntityTypeID%20eq%20'6000'&$select=EntityID,DisplayName,Latitude,Longitude,__Distance&$top=3&key=anyBingMapsKey  
```
