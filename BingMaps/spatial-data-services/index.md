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
ms.service: "bing-maps"
---
# Bing Spatial Data Services
The Bing™ Spatial Data Services Application Programming Interface (API) provides a Representational State Transfer (REST) interface that can geocode, store and query spatial data. This simple REST interface accomplishes tasks by setting parameters in a URL and then submitting the URL as an HTTP request. The HTTP response returns the results of the request.  
  
 With the Bing Spatial Data Services, you can:  
  
-   Geocode and reverse-geocode large numbers of locations with the [Geocode Dataflow API](geocode-dataflow-api/index.md).  
  
-   Store and query entities with a location, such as set of retail stores or restaurants using our [Data Source Management API](data-source-management-api/index.md) and [Query API](query-api/index.md).  
  
 **Bing Maps Account Center (alternative)**:  You can also manage data sources and geocode using the [Bing Maps Account Center](https://www.bingmapsportal.com). For more information, see [Creating and Managing Data Sources](https://msdn.microsoft.com/en-us/library/hh698204.aspx).  
  
 **Download this documentation**: [CHM](https://www.microsoft.com/downloads/en/details.aspx?FamilyID=58f58f96-d9dc-4f23-a2e6-6b25d0d742c1&displaylang=en) &#124; [PDF](https://www.microsoft.com/downloads/en/details.aspx?FamilyID=b0c49ebe-c27a-4cfe-b6a9-c8d5406ce5dd&displaylang=en)  
  
 Transaction accounting is provided when you use the Bing Spatial Data Services. For more information about billable and non-billable transactions for the Bing Spatial Data Services, see [Usage Transactions](https://msdn.microsoft.com/en-us/library/ff859477.aspx). There are also some use limits for this API. For more information, see [Geocode and Data Source Limits](../spatial-data-services/geocode-and-data-source-limits.md)  
  
## In this Section  
  
|||  
|-|-|  
|[Getting Started](../spatial-data-services/getting-started-with-the-spatial-data-services.md)|Provides information to help you get started with the Bing Spatial Data Services.|  
|[What's New](../spatial-data-services/whats-new-in-bing-spatial-data-services.md)|Outlines the latest features added to the Bing Spatial Data Services.|  
|[Public Data Sources](public-data-sources/index.md)|Includes descriptions of public data sources that you can query.|  
|[Status Codes and Error Handling](../spatial-data-services/status-codes-and-error-handling.md)|Describes the HTTP errors that can occur when you use the Bing Spatial Data Services APIs.|  
|[Geocode and Data Source Limits](../spatial-data-services/geocode-and-data-source-limits.md)|Defines limits on the total number of dataflow and data source jobs, such as the number of jobs that can be in process at the same time.|  
|[Get Job List](../spatial-data-services/get-job-list.md)|Describes the API that returns a list of all dataflow and data source jobs submitted in the last 15 days.|  
|[Geocode Dataflow API](geocode-dataflow-api/index.md)|Describes the API that geocodes sets of spatial data.|  
|[Data Source Management API](data-source-management-api/index.md)|Describes the API that creates and manages data sources.|  
|[Query API](query-api/index.md)|Describes the API that queries a data source. You can query for entities in a given area, along a route, or search by entity property or ID.|  
|[Geodata API](../spatial-data-services/geodata-api.md)|[**This API is a preview and is subject to change.**] Describes the API that gets one or more polygons that represent a geographical entity such as a country/region, admin division, or postal code.|  
|[Release History](../spatial-data-services/release-history.md)|A history of Bing Spatial Data Services feature releases since November, 2013.|  
|[Developer Resources](../spatial-data-services/developer-resources.md)|Provides a set of helpful links and references for the developer.|  
  
## See Also  
 [Terms and Conditions](https://www.microsoft.com/maps/product/terms.html)