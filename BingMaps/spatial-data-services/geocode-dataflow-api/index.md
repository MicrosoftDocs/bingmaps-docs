---
title: "Geocode Dataflow API | Microsoft Docs"
description: "The overview page for the Geocode Dataflow API, which uses REST URLs to geocode and reverse-geocode large sets of spatial data, with information on what you need to do in order to use these API along with links to articles that describe the data schema, how to create and check on jobs, download results, sample input/output files, sample code and a walkthrough."
ms.custom: ""
ms.date: "05/21/2024"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 917538d4-90ef-4108-b51c-a84066b5b2f9
caps.latest.revision: 49
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Geocode Dataflow API

> [!NOTE]
> **Bing Maps Spatial Data Service Geocode Dataflow API retirement**
>
> Bing Maps Spatial Data Service Geocode Dataflow API is deprecated and has been retired for all free (Basic) account customers. Enterprise account customers can continue to use Bing Maps Spatial Data Service Geocode Dataflow API until June 30th, 2028. To avoid service disruptions, all enterprise account customers using Bing Maps Spatial Data Service Geocode Dataflow API will need to be updated to use Azure Maps [Get Geocoding Batch](/rest/api/maps/search/get-geocoding-batch) or Azure Maps [Get Reverse Geocoding Batch](/rest/api/maps/search/get-reverse-geocoding-batch) API by June 30th, 2028. Azure Maps Geocoding Batch API and Azure Maps Reverse Geocode Batch API will be updated to support a larger number of locations per batch soon. For detailed migration guidance, see [Migrate Bing Maps Geocode Dataflow API](/azure/azure-maps/migrate-geocode-dataflow).
>
> Azure Maps is Microsoft's next-generation maps and geospatial services for developers. Azure Maps has many of the same features as Bing Maps for Enterprise, and more. To get started with Azure Maps, create a free [Azure subscription](https://azure.microsoft.com/free) and an [Azure Maps account](/azure/azure-maps/how-to-manage-account-keys#create-a-new-account). For more information about azure Maps, see [Azure Maps Documentation](/azure/azure-maps/). For migration guidance, see [Bing Maps Migration Overview](/azure/azure-maps/migrate-bing-maps-overview).

**Before using this API, make sure you are aware of the [Geocode and Data Source Limits](../geocode-and-data-source-limits.md).**  
  
 **About data schema versions**: There are two versions of the input and output data schema for this API. The latest data schema (version 2.0) provides additional geocoding information in the response, such as different points for routing and display and a rectangular area that bounds the location. If you are a new user, version 2.0 is recommended because it provides the greatest flexibility. Version 1.0 users can upgrade to version 2.0, but must be aware of the changes in the data schema including some name changes that were made to match the REST Services [Locations API](https://msdn.microsoft.com/library/ff701715.aspx).  
  
 The Geocode Dataflow API uses REST URLS to geocode and reverse-geocode large sets of spatial data. To use this API, you must:  
  
1.  Format your location data using the [Data Schema  v2.0](../geocode-dataflow-api/geocode-dataflow-data-schema-version-2-0.md) or [Data Schema v1.0](../geocode-dataflow-api/geocode-dataflow-data-schema-version-1-0.md) (for existing users). The spatial data you upload can be in XML format, or it can be provided as sets of values that use commas, tabs, or pipe (&#124;) characters to separate the values.  
  
2.  [Create Job](../geocode-dataflow-api/create-a-geocode-job-and-upload-data.md)  
  
3.  [Get Job Status](../geocode-dataflow-api/get-status-of-a-geocode-job.md) and watch for the job to complete.  
  
4.  [Download Results](../geocode-dataflow-api/download-geocode-job-results.md)  
  
 For an overview of this process, see [Walkthrough](../geocode-dataflow-api/geocode-dataflow-walkthrough.md).  
  
 To get a list of all geocode dataflow jobs and data source jobs submitted in the last 15 days, see [Get Job List](../get-job-list.md).  
  
## In this Section  
  
|Resource|Description|  
|-|-|  
|[Create Job](../geocode-dataflow-api/create-a-geocode-job-and-upload-data.md)|Describes how to create a job to geocode and reverse-geocode the data.|  
|[Get Job Status](../geocode-dataflow-api/get-status-of-a-geocode-job.md)|Describes how to get the status of a geocode job.|  
|[Download Results](../geocode-dataflow-api/download-geocode-job-results.md)|Describes how to download geocoded results.|  
|[Response Data](../geocode-dataflow-api/geocode-dataflow-response-description.md)|Describes the information returned in the HTTP responses.|  
|[Walkthrough](../geocode-dataflow-api/geocode-dataflow-walkthrough.md)|Provides a detailed overview of how to use the Geocode Dataflow using version 2.0 of the data schema.|  
|[Sample Code](../geocode-dataflow-api/geocode-dataflow-sample-code.md)|Provides complete sample code that uses the Geocode Dataflow and version 1.0 of the data schema to geocode data.|  
|[Data Schema v1.0](../geocode-dataflow-api/geocode-dataflow-data-schema-version-1-0.md)|Describes the original (version 1.0) data schema for the input data and the geocoded results.|  
|[Data Schema  v2.0](../geocode-dataflow-api/geocode-dataflow-data-schema-version-2-0.md)|Describes version 2.0 of the data schema for the input data and the geocoded results.|  
|[Sample Input and Output v1.0](../geocode-dataflow-api/geocode-dataflow-sample-input-and-output-data-version-1-0.md)|Shows examples of all types of accepted input formats for the original (version 1.0) of the data schema. This includes XML examples and examples of sets of values separated by pipe (&#124;), comma, or tab characters|  
|[Sample Input and Output v2.0](../geocode-dataflow-api/geocode-dataflow-sample-input-and-output-data-version-2-0.md)|Shows examples of all types of accepted input formats for version 2.0 of the data schema. This includes XML examples and examples of sets of values separated by pipe (&#124;), comma, or tab characters|