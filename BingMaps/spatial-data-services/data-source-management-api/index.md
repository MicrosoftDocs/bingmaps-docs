---
title: "Data Source Management API | Microsoft Docs"
description: The overview page for the Data Source Management API section contains a description of the Data Source Management API which is used to create and manage data sources that store spatial entity data for a user-defined entity type, and provides links to and descriptions of each article in this section as well as a table listing each data source and links with information on how to use each with both Bing Spatial Data Services and Bing Maps Account Center.
ms.custom: ""
ms.date: "05/21/2024"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 90747d5f-7d32-4200-b58d-7fea793d97f0
caps.latest.revision: 35
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Data Source Management API

> [!NOTE]
> **Bing Maps Data Source Management API retirement**
>
> Bing Maps Data Source Management API is deprecated and has been retired for all free (Basic) account customers. Enterprise account customers can continue to use Bing Maps Data Source Management API until June 30th, 2028. To avoid service disruptions, all enterprise account customers using Bing Maps Spatial Data Service Data Source Management API will need to be updated to use an alternative, such as an Azure-based solution, by June 30th, 2028. For detailed migration guidance, see [Migrate Bing Maps Data Source Management and Query API](/azure/azure-maps/migrate-sds-data-source-management).
>
> Azure Maps is Microsoft's next-generation maps and geospatial services for developers. Azure Maps has many of the same features as Bing Maps for Enterprise, and more. To get started with Azure Maps, create a free [Azure subscription](https://azure.microsoft.com/free) and an [Azure Maps account](/azure/azure-maps/how-to-manage-account-keys#create-a-new-account). For more information about azure Maps, see [Azure Maps Documentation](/azure/azure-maps/). For migration guidance, see [Bing Maps Migration Overview](/azure/azure-maps/migrate-bing-maps-overview).

Use the Data Source Management API to create and manage data sources that store spatial entity data for a user-defined entity type. You can also create and manage your data sources using the [Bing Maps Account Center](https://www.bingmapsportal.com). The table below provides links to the documentation for both methods.

 **Before using this API, review the [Geocode and Data Source Limits](../geocode-and-data-source-limits.md).**  
  
 To get a list of all data source and geocode jobs submitted in the last 15 days, see [Get Job List](../get-job-list.md).  
  
|Data Source Action|Using Bing Spatial Data Services|Using Bing Maps Account Center|  
|------------------------|--------------------------------------|------------------------------------|  
|**Create**|[Load Data Source Dataflow](../data-source-management-api/load-data-source-dataflow/index.md)|[Uploading and Publishing Entity Data to a Data Source](https://msdn.microsoft.com/library/gg650600)|  
|**Update**|[Load Data Source Dataflow](../data-source-management-api/load-data-source-dataflow/index.md)|[Uploading and Publishing Entity Data to a Data Source](https://msdn.microsoft.com/library/gg650600)|  
|**Make Public**|[Make a Data Source Public](../data-source-management-api/make-public-data-source.md)|[Available only with the Bing Spatial Data Services.](https://msdn.microsoft.com/library/dn151784.aspx)|  
|**Query**|[Query API](../query-api/index.md)|Use Spatial Data Services [Query API](../query-api/index.md)|  
|**Download**|[Download a Data Source Dataflow](../data-source-management-api/download-data-source-dataflow/index.md)|[Downloading a Data Source](https://msdn.microsoft.com/library/hh698203)|  
|**Stage**|[Load Data Source Dataflow](../data-source-management-api/load-data-source-dataflow/index.md)|[Uploading and Publishing Entity Data to a Data Source](https://msdn.microsoft.com/library/gg650600)|  
|**Rollback**|[Rollback a Data Source Dataflow](../data-source-management-api/rollback-data-source-dataflow.md)|[Rollback a Data Source](https://msdn.microsoft.com/library/dn167663.aspx)|  
|**Delete**|[Delete a Data Source](../data-source-management-api/delete-data-source.md)|[Deleting a Data Source](https://msdn.microsoft.com/library/hh290820)|  
|**Get Info**|[Get Data Source Information](../data-source-management-api/get-data-source-information.md)|[Getting Data Source Information](https://msdn.microsoft.com/library/hh127034)|  
  
## In this Section  

|Topic|Description|
|-|-|  
|[Load Data Source Dataflow](../data-source-management-api/load-data-source-dataflow/index.md)|Create a data source and upload entity data.|  
|[Get Data Source Information](../data-source-management-api/get-data-source-information.md)|Get information about one or more data sources.|  
|[Download a Data Source Dataflow](../data-source-management-api/download-data-source-dataflow/index.md)|Download entity data for a published data source.|  
|[Make a Data Source Public](../data-source-management-api/make-public-data-source.md)|Make a data source publicly available or private.|  
|[Get All Public Data Sources](../data-source-management-api/get-all-public-data-sources.md)|Get all publicly available data sources.|  
|[Rollback a Data Source Dataflow](../data-source-management-api/rollback-data-source-dataflow.md)|Rollback a data source to a previous version.|  
|[Delete a Data Source](../data-source-management-api/delete-data-source.md)|Delete a data source.|