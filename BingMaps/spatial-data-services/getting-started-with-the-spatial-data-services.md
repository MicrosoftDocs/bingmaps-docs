---
title: "Getting Started with the Spatial Data Services | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 077b79a4-e9c4-46ef-996c-ca6ee64aa202
caps.latest.revision: 42
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Getting Started with the Spatial Data Services

Bing Spatial Data Services provides REST APIs that work with large sets of spatial data. With these APIs you can geocode spatial data and you can store data that has a spatial component in data sources that you can query.  
  
 See the links in the **How to:** sections below to find out more information.  
  
## Getting Started

To get started with the Bing Spatial Data Services, you must have a [Bing Maps Key](https://www.microsoft.com/maps/create-a-bing-maps-key.aspx).  
  
> [!NOTE]
>  Before using this API, review the [Geocode and Data Source Limits](../spatial-data-services/geocode-and-data-source-limits.md)  
  
 You can also use Bing Maps Dev Center to geocode entities and to create and manage your data sources. For more information, see [Creating and Managing Data Sources](https://msdn.microsoft.com/library/hh698204.aspx). The Bing Spatial Data Services and the Bing Maps Dev Center can be used interchangeably to manage data sources for a single Bing Maps Account.  
  
## How to: Geocode and reverse-geocode spatial data  
 Use the [Geocode Dataflow API](geocode-dataflow-api/index.md) to create dataflow jobs that geocode and reverse-geocode large sets of data. For more information, see [Geocode Dataflow API](geocode-dataflow-api/index.md). For an example of the complete process, see the [Walkthrough](geocode-dataflow-api/geocode-dataflow-walkthrough.md)  
  
## How to: Create a data source  
 Use the [Load Data Source Dataflow](data-source-management-api/load-data-source-dataflow/index.md) to create a new data source.  
  
## How to: Query a data source  
 Use the [Query API](query-api/index.md) to query for entities in a data source.  
  
## How to: Update a data source  
 Use the [Load Data Source Dataflow](data-source-management-api/load-data-source-dataflow/index.md) to update an existing data source.  
  
## How to: Download a data source  
 Use the [Download a Data Source Dataflow](data-source-management-api/download-data-source-dataflow/index.md) API to download a data source.  
  
## How to: Delete a data source  
 Use the [Delete a Data Source](data-source-management-api/delete-data-source.md) API to delete a data source.  
  
## How to: Stage a data source  
 Use the [Load Data Source Dataflow](data-source-management-api/load-data-source-dataflow/index.md) to stage an existing data source. After testing your data source, you can [Publish a Staged Data Source](data-source-management-api/load-data-source-dataflow/publish-staged-data-source.md).  
  
## How to: Rollback a data source  
 Use the [Rollback a Data Source Dataflow](data-source-management-api/rollback-data-source-dataflow.md) to rollback a data source to a previous version.  
  
## How to: Get information about data sources  
 Use the [Get Data Source Information](data-source-management-api/get-data-source-information.md) API to get information about a data source such as the entity type and properties that it stores. You can also request information about all of the data sources that belong to a Bing Maps Account.  
  
## How to: Use the Spatial Data Services with other Bing Maps APIs  
 Read the [Show Spatial Data Search Results on a Map](https://msdn.microsoft.com/library/hh305205.aspx) and [Searching for Traffic Incidents Along a Route](https://msdn.microsoft.com/library/hh779734.aspx) articles to learn how integrate Bing Spatial Data Services with [Bing Maps Rest Services](https://msdn.microsoft.com/library/ff701713.aspx) and the [Bing Maps AJAX Control, Version 7.0](https://msdn.microsoft.com/library/gg427610.aspx).  
  
## Public Data Sources  
 The following are public data sources that you can access with any Bing Maps Key.  
  
|Public Data Source|Description|  
|------------------|-----------|  
|[NAVTEQNA Data Source](public-data-sources/navteqna.md)|NavTechNA is a data source that contains points of interest in North America.|  
|[NAVTEQEU Data Source](public-data-sources/navteqeu.md)|NavTechEU is a data source that contains points of interest in Europe.|  
|[Traffic Incident Data Source](public-data-sources/traffic-incident-data-source.md)|TrafficIncident is a data source that contains traffic incidents data in the United States and Canada.|  
|[FourthCoffeeSample Data Source](public-data-sources/fourthcoffeesample.md)|FourthCoffeeSample is a data source with sample data.|  
  
## Transaction Accounting  
 Transactions are counted for each Bing Spatial Data Services request sent with a valid Bing Maps Key. For information about billable and non-billable transactions for the Bing Spatial Data Services and how to view them, see [Viewing Bing Maps Usage Reports](https://msdn.microsoft.com/library/ff859477.aspx).