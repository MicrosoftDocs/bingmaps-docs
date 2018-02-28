---
title: "Getting Started with the Bing Maps REST Services | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 1e99826c-df76-490f-aaea-f5f5ee9376ce
caps.latest.revision: 46
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Getting Started with the Bing Maps REST Services
The Bing™ Maps REST Services Application Programming Interface (API) is a Representational State Transfer (REST) API that you can use to do common tasks, such as finding an address, retrieving a map with a pushpin and a label, or getting driving directions. You perform these tasks by constructing a URL..  
  
 **To use the [!INCLUDE[bm_rest_product_name](../articles/includes/bm-rest-product-name-md.md)], you must have a [Bing Maps Key](http://msdn.microsoft.com/en-us/library/ff428642.aspx).**  
  
## Bing Maps REST Services  
 The following table lists the [!INCLUDE[bm_rest_product_name](../articles/includes/bm-rest-product-name-md.md)] and the common tasks they perform. Click the links for API details.  
  
|REST API|Features|  
|--------------|--------------|  
|[Locations](../rest-services/locations-api.md)|-   Find a location based on an address, point, or query.|  
|[Elevations](../rest-services/elevations-api.md)|-   Get the elevations for a set of locations, a path, or an area on the Earth.|  
|[Imagery](../rest-services/imagery-api.md)|-   Get a static map.<br />-   Get a static map that displays a route.<br />-   Get imagery metadata.|  
|[Routes](../rest-services/routes-api.md)|-   Find a walking, driving or transit route.<br />-   Find routes from major routes to a location.<br />-   Get traffic information along a route.|  
|[Traffic](../rest-services/traffic-api.md)|-   Get traffic information for a geographical area.|  
  
### Additional Topics  
 The following topics show examples of how to use the [!INCLUDE[bm_rest_product_name](../articles/includes/bm-rest-product-name-md.md)] with other Bing Maps APIs or provide related information.  
  
|||  
|-|-|  
|[Accessing the Bing Maps REST Services using PHP](http://msdn.microsoft.com/en-us/library/ff817004.aspx)|This article shows how to write a PHP application that can interact with the Bing Maps REST Services APIs.|  
|[Bing Maps Transit Coverage](http://msdn.microsoft.com/en-us/library/hh441739.aspx)|Provides a list of transit agencies that are used by [!INCLUDE[bm_rest_product_name](../articles/includes/bm-rest-product-name-md.md)] to provide transit routes.|  
  
## Transaction Accounting  
 Transactions are counted for each [!INCLUDE[bm_rest_product_name](../articles/includes/bm-rest-product-name-md.md)] request sent with a valid Bing Maps Key. For information about billable and non-billable transactions for the [!INCLUDE[bm_rest_product_name](../articles/includes/bm-rest-product-name-md.md)], see [Viewing Bing Maps Usage Reports](http://msdn.microsoft.com/en-us/library/ff859477.aspx).