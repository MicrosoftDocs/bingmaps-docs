---
title: "FourthCoffeeSample | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 6e6d7dc1-18d2-4576-9fb0-fb97c271828d
caps.latest.revision: 7
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# FourthCoffeeSample
The FourthCoffeeSample data source is a sample data source that you can use to learn how to query and get data source information by using the  Bing Spatial Data Services.  
  
> [!NOTE]
>  All Query API transactions are billable transactions including queries to the FourthCoffeeSample data source. Therefore, you may want to create an evaluation account to use with this data source. For more information about how to create an evaluation account, see [Getting a Bing Maps Key](http://msdn.microsoft.com/en-us/library/ff428642.aspx).  
  
## Entity Properties  
 The following table describes the properties that you can query. These properties make up the FourthCoffeeShops entity type that is used by the FourthCoffeeSample data source.  
  
|Property|Data Type|Example Value|  
|--------------|---------------|-------------------|  
|EntityID (Primary Key)|Edm.String|-18147|  
|Latitude|Edm.Double|50.792458|  
|Longitude|Edm.Double|-1.146712|  
|AddressLine|Edm.String|Bury Road|  
|PrimaryCity|Edm.String|Alverstoke|  
|SecondaryCity|Edm.String|Gosport|  
|Subdivision|Edm.String|Hampshire|  
|CountryRegion|Edm.String|United Kingdom|  
|PostalCode|Edm.String|PO123|  
|Phone|Edm.String|800-555-0111|  
|Manager|Edm.String|Aaron Con|  
|StoreOpen|Edm.String|Y|  
|StoreType|Edm.String|Kiosk|  
|Name|Edm.String|Fourth Coffee Store #18147|  
|DisplayName|Edm.String|Fourth Coffee Store #18147, Alverstoke, Hampshire, United Kingdom|  
|IsWiFiHotSpot|Edm.Boolean|0 [false]|  
|SeatingCapacity|Edm.Int64|50|  
|IsWheelChairAccessible|Edm.Boolean|1 [true]|  
|AcceptsOnlineOrders|Edm.Boolean|0 [false]|  
|AcceptsCoffeeCards|Edm.Boolean|1 [true]|  
|Open|Edm.Int64|800|  
|Close|Edm.Int64|2200|  
|CreatedDate|Edm.DateTime|2010-11-10T17:19:36|  
|LastUpdatedDate|Edm.DateTime|2010-11-15T17:19:36|  
  
## How to query the FourthCoffeeSample data source  
 You can query FourthCoffeeShops entities in the FourthCoffeeSample data source by using the following base URL and adding additional parameters such a geographical area to search and the properties you want to return.  
  
 **Base Query URL**  
  
```  
http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops  
```  
  
 **Query Example**  
  
 The following query example queries for FourthCoffeeShops entities within 5 kilometers of a location that is specified as a latitude and longitude pair. Because this is a sample data source, the query key you use can be any Bing Maps Key. For more information, see [Query API](../spatial-data-services/query-api.md).  
  
```  
http://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample/FourthCoffeeShops?spatialFilter=nearby(40.83274904439099,-74.3163299560546935,5)&$select=EntityID,Latitude,Longitude,__Distance&$top=3&key=anyBingMapsKey  
```