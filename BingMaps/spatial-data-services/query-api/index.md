---
title: "Query API | Microsoft Docs"
description: "The overview page for the Query API section, with links to each of the articles in this section and a description for each."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 369ac9ed-4b54-424c-8369-32d48266035a
caps.latest.revision: 14
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Query API

The Query API is a component of the Bing Spatial Data Services. You can use the Query API to query a data source for information about entities in that data source. For example, if the data source contains restaurant entities, you can query for French restaurants nearby or you can get information about a specific restaurant. Each query response can return a maximum number of 250 results.  
  
 Below are some ways you could use the Query API to search a data source that contains information about a set of restaurants.  
  
-   Use Query by Area to search for all movie theaters within 20 kilometers.    
-   Use Query Near a Route to search for all restaurants along a route.    
-   Use Query by Property to search for all restaurants within 20 miles that have more than 20 employees.    
-   Use Query by ID to search for the restaurant entity that has an entity ID of "410".  
  
 For information about creating and updating data sources, see the [Load Data Source Dataflow](../data-source-management-api/load-data-source-dataflow/index.md).  
  
## In this Section  

|Resource|Description|  
|-|-|  
|[Query by Area](../query-api/query-by-area.md)|Describes how to query a data source for entities that are in a specified geographical area.|  
|[Query by Property](../query-api/query-by-property.md)|Describes how to query a data source for entities that satisfy a set of property value conditions.|  
|[Query Near a Route](../query-api/query-near-route.md)|Describes how to query a data source for entities near a route.|  
|[Query by ID](../query-api/query-by-id.md)|Describes how to query a data source for one or more entities by specifying entity IDs.|  
|[Query Options](../query-api/query-options.md)|Describes query options, such as the options to filter and order results and to user wildcard searches.|  
|[Response Data](../query-api/query-response-description.md)|Describes the response returned for queries.|  
|[C# Sample Code](../query-api/query-api-sample-code-csharp.md)|Provides sample C# code that uses the [Query API](../query-api/index.md).|  
|[VB Sample Code](../query-api/query-api-sample-code-vb.md)|Provides sample Visual Basic code that uses the [Query API](../query-api/index.md).|