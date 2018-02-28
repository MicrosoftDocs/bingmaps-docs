---
title: "NAVTEQNA | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: b51a571e-45e8-49d2-a25d-0756ebe3d847
caps.latest.revision: 24
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# NAVTEQNA
The NAVTEQNA data source contains information about points of interest (POIs) in North America. You can query this data source by using the [!INCLUDE[bm_spatialapi_product_name](../articles/includes/bm-spatialapi-product-name-md.md)][Query API](../spatial-data-services/query-api2.md) and any [!INCLUDE[maps_ticket](../articles/includes/maps-ticket-md.md)].  
  
> [!IMPORTANT]
>  When you query this data source for specific property values, you must include a geographical area to search. This does not apply if you are querying for specific entities using entity ID. See [Query by Area](../spatial-data-services/query-by-area.md) and [Query by ID](../spatial-data-services/query-by-id.md) for details. POI entities may not be available for every location.                                              **Note:**  NAVTEQNA and NAVTEQEU data sources do not support the intersects and nearRoute filters.  
  
## POI Entity Properties  
 The following table describes the properties that you can query to get information about a point of interest in North America. These properties make up the NAVTEQPOIs entity type that is used by the NAVTEQNA data source.  
  
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
 For a complete list of the entity type IDs that you can query, see [POI Entity Types](../spatial-data-services/poi-entity-types.md).  
  
## How to query the NAVTEQNA data source  
 You can query NAVTEQNA data source by using the following base URL and adding additional parameters such a geographical area to search and the properties you want to return. For a complete description of query options and more examples, see [Query API](../spatial-data-services/query-api2.md).  
  
> [!IMPORTANT]
>  When you query this data source for specify property values, you must include a geographical area to search. This does not apply if you are querying for specific entities using entity ID. See [Query by Area](../spatial-data-services/query-by-area.md) and [Query by ID](../spatial-data-services/query-by-id.md) for details.  
  
 **Base Query URL**  
  
```  
http://spatial.virtualearth.net/REST/v1/data/f22876ec257b474b82fe2ffcb8393150/NavteqNA/NavteqPOIs  
```  
  
 **Query Example**  
  
 The following query example queries for banks within 5 kilometers of the specified latitude and longitude. The query key you use can be any [!INCLUDE[maps_ticket](../articles/includes/maps-ticket-md.md)]. For complete information about querying a data source, see [Query API](../spatial-data-services/query-api2.md).  
  
```  
http://spatial.virtualearth.net/REST/v1/data/f22876ec257b474b82fe2ffcb8393150/NavteqNA/NavteqPOIs?spatialFilter=nearby(40.83274904439099,-74.3163299560546935,5)&$filter=EntityTypeID%20eq%20'6000'&$select=EntityID,DisplayName,Latitude,Longitude,__Distance&$top=3&key=anyBingMapsKey  
```