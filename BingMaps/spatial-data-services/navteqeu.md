---
title: "NAVTEQEU | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: e69be280-a5a9-4183-9a04-0cb57da37474
caps.latest.revision: 18
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# NAVTEQEU
The NAVTEQEU data source contains information about points of interest (POIs) in Europe. You can query this data source by using the Bing Spatial Data Services[Query API](../spatial-data-services/query-api.md) and any Bing Maps Key.  
  
> [!IMPORTANT]
>  When you query this data source for specific property values, you must include a geographical area to search. This does not apply if you are querying for specific entities using entity ID. See [Query by Area](../spatial-data-services/query-by-area.md) and [Query by ID](../spatial-data-services/query-by-id.md) for details. POI entities may not be available for every location. **Note:**  NAVTEQNA and NAVTEQEU data sources do not support the intersects and nearRoute filters.  
  
## POI Entity Properties  
 The following table describes the properties that you can query to get information about a point of interest. These properties make up the NAVTEQPOIs entity type that is used by the NAVTEQEU data source.  
  
|Property|Data Type|Example Value|  
|--------------|---------------|-------------------|  
|EntityID (Primary Key)|Edm.String|111|  
|LanguageCode|Edm.String|GER|  
|Name|Edm.String|Contoso, Ltd|  
|DisplayName|Edm.String|Contoso, Ltd|  
|Latitude|Edm.Double|36.7222|  
|Longitude|Edm.Double|-4.4450|  
|AddressLine|Edm.String|Calle Rodriguez, 1234|  
|Locality|Edm.String|Malaga|  
|AdminDistrict|Edm.String|Andalucia|  
|AdminDistrict2|Edm.String|MA|  
|PostalCode|Edm.String|28146|  
|CountryRegion|Edm.String|España|  
|Phone|Edm.String|+34 xx xxx xxxx|  
|EntityTypeID|Edm.String|3000|  
  
## Entity Types  
 For a complete list of the entity type IDs that you can query, see [POI Entity Types](../spatial-data-services/poi-entity-types.md).  
  
## How to query the NAVTEQEU data source  
 You can query the NAVTEQEU data source by using the following base URL and adding additional parameters such a geographical area to search and the properties you want to return. For a complete description of query options and more examples, see [Query API](../spatial-data-services/query-api.md).  
  
 **Base Query URL**  
  
```  
http://spatial.virtualearth.net/REST/v1/data/c2ae584bbccc4916a0acf75d1e6947b4/NavteqEU/NavteqPOIs  
```  
  
 **Query Example**  
  
 The following query example queries for banks within 5 kilometers of the specified latitude and longitude. The query key you use can be any Bing Maps Key.  
  
```  
http://spatial.virtualearth.net/REST/v1/data/c2ae584bbccc4916a0acf75d1e6947b4/NavteqEU/NavteqPOIs?spatialFilter=nearby(50.1120796203613,8.68340969085693,100)&$select=EntityID,Latitude,Longitude,DisplayName,__Distance,LanguageCode&$top=3&key=anyBingMapsKey  
```