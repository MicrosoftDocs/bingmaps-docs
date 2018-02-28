---
title: "Bing Spatial Data Services | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: b1372816-dbaa-4b78-a365-088998c72138
caps.latest.revision: 50
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Bing Spatial Data Services
The Bing™ Spatial Data Services Application Programming Interface (API) provides a Representational State Transfer (REST) interface that can geocode, store and query spatial data. This simple REST interface accomplishes tasks by setting parameters in a URL and then submitting the URL as an HTTP request. The HTTP response returns the results of the request.  
  
 With the [!INCLUDE[bm_spatialapi_product_name](../articles/includes/bm-spatialapi-product-name-md.md)], you can:  
  
-   Geocode and reverse-geocode large numbers of locations with the [Geocode Dataflow API](../spatial-data-services/geocode-dataflow-api.md).  
  
-   Store and query entities with a location, such as set of retail stores or restaurants using our [Data Source Management API](../spatial-data-services/data-source-management-api.md) and [Query API](../spatial-data-services/query-api2.md).  
  
 **Bing Maps Account Center (alternative)**:  You can also manage data sources and geocode using the [Bing Maps Account Center](http://www.bingmapsportal.com). For more information, see [Creating and Managing Data Sources](http://msdn.microsoft.com/en-us/library/hh698204.aspx).  
  
 **Download this documentation**: [CHM](http://www.microsoft.com/downloads/en/details.aspx?FamilyID=58f58f96-d9dc-4f23-a2e6-6b25d0d742c1&displaylang=en) &#124; [PDF](http://www.microsoft.com/downloads/en/details.aspx?FamilyID=b0c49ebe-c27a-4cfe-b6a9-c8d5406ce5dd&displaylang=en)  
  
 Transaction accounting is provided when you use the [!INCLUDE[bm_spatialapi_product_name](../articles/includes/bm-spatialapi-product-name-md.md)]. For more information about billable and non-billable transactions for the [!INCLUDE[bm_spatialapi_product_name](../articles/includes/bm-spatialapi-product-name-md.md)], see [Usage Transactions](http://msdn.microsoft.com/en-us/library/ff859477.aspx). There are also some use limits for this API. For more information, see [Geocode and Data Source Limits](../spatial-data-services/geocode-and-data-source-limits.md)  
  
## In this Section  
  
|||  
|-|-|  
|[Getting Started](../spatial-data-services/getting-started-with-the-spatial-data-services.md)|Provides information to help you get started with the [!INCLUDE[bm_spatialapi_product_name](../articles/includes/bm-spatialapi-product-name-md.md)].|  
|[What's New](../spatial-data-services/what-s-new-in-bing-spatial-data-services.md)|Outlines the latest features added to the [!INCLUDE[bm_spatialapi_product_name](../articles/includes/bm-spatialapi-product-name-md.md)].|  
|[Public Data Sources](../spatial-data-services/public-data-sources.md)|Includes descriptions of public data sources that you can query.|  
|[Status Codes and Error Handling](../spatial-data-services/status-codes-and-error-handling1.md)|Describes the HTTP errors that can occur when you use the [!INCLUDE[bm_spatialapi_product_name](../articles/includes/bm-spatialapi-product-name-md.md)] APIs.|  
|[Geocode and Data Source Limits](../spatial-data-services/geocode-and-data-source-limits.md)|Defines limits on the total number of dataflow and data source jobs, such as the number of jobs that can be in process at the same time.|  
|[Get Job List](../spatial-data-services/get-job-list.md)|Describes the API that returns a list of all dataflow and data source jobs submitted in the last 15 days.|  
|[Geocode Dataflow API](../spatial-data-services/geocode-dataflow-api.md)|Describes the API that geocodes sets of spatial data.|  
|[Data Source Management API](../spatial-data-services/data-source-management-api.md)|Describes the API that creates and manages data sources.|  
|[Query API](../spatial-data-services/query-api2.md)|Describes the API that queries a data source. You can query for entities in a given area, along a route, or search by entity property or ID.|  
|[Geodata API](../spatial-data-services/geodata-api1.md)|[**This API is a preview and is subject to change.**] Describes the API that gets one or more polygons that represent a geographical entity such as a country/region, admin division, or postal code.|  
|[Release History](../spatial-data-services/release-history2.md)|A history of [!INCLUDE[bm_spatialapi_product_name](../articles/includes/bm-spatialapi-product-name-md.md)] feature releases since November, 2013.|  
|[Developer Resources](../spatial-data-services/developer-resources1.md)|Provides a set of helpful links and references for the developer.|  
  
## See Also  
 [Terms and Conditions](http://www.microsoft.com/maps/product/terms.html)