---
title: "Load Data Source Dataflow | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 59ee8299-9181-46ce-8243-a7f89bb0e885
caps.latest.revision: 47
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Load Data Source Dataflow
Load Data Source Dataflow API to create a data source that contains entity data for a user-specified entity type. For example, a data source could contain location and hours of operation information for a set of restaurants. With the Load Data Source Dataflow API you can:  
  
-   Create a data source.  
  
-   Update, add and delete data source entities.  
  
-   Overwrite an existing data source.  
  
-   Make your data source public.  
  
 You can also use the [Bing Maps Account Center](http://www.bingmapsportal.com) to create or update a data source. The Bing Maps Account Center also offers the option to geocode address data on upload. For more information, see [Creating and Managing Data Sources](http://msdn.microsoft.com/en-us/library/hh698204.aspx).  
  
 **Before using this API, review the [Geocode and Data Source Limits](../../geocode-and-data-source-limits.md).**  
  
 The Load Data Source Dataflow API creates and updates data sources by creating load data source jobs. The [Create a Load Data Source Job](../../data-source-management-api/load-data-source-dataflow/create-a-load-data-source-job-and-input-entity-data.md) URL is used to create the load data source job and requires a data schema and a set of entity data. The data schema and entity data can be provided in XML format or as values separated by commas, tabs or pipe (&#124;) values. KML, KMZ and shapefile formats are also supported. Shapefile data must be uploaded as a zipped set of .shp, .shx, and .dbf files. For more information about the data schema and input data, see [Data Schema and Sample Input](../../data-source-management-api/load-data-source-dataflow/load-data-source-data-schema-and-sample-input.md).  
  
 After you have created a job, you can use the [Get Load Data Source Status](../../data-source-management-api/load-data-source-dataflow/get-load-data-source-status.md) URL to get job status. A job can have one of three statuses: “Pending”, “Completed” or “Aborted”. A job has a “Pending” status when it is created and keeps that status until the job is “Completed” or Aborted”. When a job completes, the response returns a unique base URL that you can use to query the data source with the [Query API](../../query-api/index.md).  
  
 You can delete a data source by using the [Delete a Data Source](../../data-source-management-api/delete-data-source.md) API.  
  
## In this Section  
  
|||  
|-|-|  
|[Create a Load Data Source Job](../../data-source-management-api/load-data-source-dataflow/create-a-load-data-source-job-and-input-entity-data.md)|Describes how to create a data source and upload entity data by using a load data source job. You can also use this API to stage or update a data source.|  
|[Get Load Data Source Status](../../data-source-management-api/load-data-source-dataflow/get-load-data-source-status.md)|Describes how to request status for a load data source job.|  
|[Publish a Staged Data Source](../../data-source-management-api/load-data-source-dataflow/publish-staged-data-source.md)|Describes how to publish a staged data source.|  
|[Response Data](../../data-source-management-api/load-data-source-dataflow/load-data-source-dataflow-response-description.md)|Describes the responses returned when you create and get status for a load data source job.|  
|[Data Schema and Sample Input](../../data-source-management-api/load-data-source-dataflow/load-data-source-data-schema-and-sample-input.md)|Describes how to define a data schema and input data for an entity type. Examples are provided for XML format and for input data that is provided by using sets of values separated by pipe (&#124;), comma, or tab characters.|  
|[Geography Types](../../data-source-management-api/load-data-source-dataflow/geography-types.md)|Describes the variety of geography types available that represent a geographic area. These types can be used as an entity property and to query for entities in a custom geographical area.|  
|[Helpful Tips for Entity Data](../../data-source-management-api/load-data-source-dataflow/helpful-tips-for-entity-data.md)|Provides helpful tips to guide you when you create a data schema and entity data to upload to a data source.|  
|[C# Sample Code](../../data-source-management-api/load-data-source-dataflow/load-data-source-dataflow-sample-code-csharp.md)|Provides C# code that shows how to upload entity data to a data source by using the Load Data Source Dataflow API.|  
|[VB Sample Code](../../data-source-management-api/load-data-source-dataflow/load-data-source-dataflow-sample-code-vb.md)|Provides VB code that shows how to upload entity data to a data source by using the Load Data Source Dataflow API.|