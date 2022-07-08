---
title: "Getting Started with the Bing Maps REST Services | Microsoft Docs"
description: "This article describes the Bing Maps REST Services Application Programming Interface (API) and provides a table that lists the Bing Maps REST Services and the common tasks they perform."
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
ms.service: "bing-maps"
---

# Getting Started with the Bing Maps REST Services

The Bing™ Maps REST Services Application Programming Interface (API) is a Representational State Transfer (REST) API that you can use to do common tasks, such as finding an address, retrieving a map with a pushpin and a label, or getting driving directions. You perform these tasks by constructing a URL.
  
 **To use the Bing Maps REST Services, you must have a [Bing Maps Key](../getting-started/bing-maps-dev-center-help/getting-a-bing-maps-key.md).**  
  
## Bing Maps REST Services  

 The following table lists the Bing Maps REST Services and the common tasks they perform. Click the links for API details.  
  
|REST API|Features|  
|--------------|--------------|  
|[Locations](../rest-services/locations/index.md)|-   Find a location based on an address, point, or query.|  
|[Elevations](../rest-services/elevations/index.md)|-   Get the elevations for a set of locations, a path, or an area on the Earth.|  
|[Imagery](../rest-services/imagery/index.md)|-   Get a static map.<br />-   Get a static map that displays a route.<br />-   Get imagery metadata.|
|[Routes](../rest-services/routes/index.md)|-   Find a walking, driving or transit route.<br />-   Find routes from major routes to a location.<br />-   Get traffic information along a route.|  
|[Traffic](../rest-services/traffic/index.md)|-   Get traffic information for a geographical area.| 
|[Autosuggest](../rest-services/autosuggest.md)| - Get a list of autosuggested entities from a user's query.|  
|[Time Zone](../rest-services/timezone/index.md)| - Get a Time Zone by point or query.<br />- Convert UTC datetime to a time zone.<br />- Get information about Windows and IANA time zone standards.|
  
### Additional Topics  

> [!NOTE]
>  Bing Maps API works ONLY from requests using the standard HTTP ports: 80 (http) or 443 (https).

 The following topics show examples of how to use the Bing Maps REST Services with other Bing Maps APIs or provide related information.  
  
|Topic|Description|  
|-|-|  
|[Accessing the Bing Maps REST Services using PHP](../articles/accessing-the-bing-maps-rest-services-using-php.md)|This article shows how to write a PHP application that can interact with the Bing Maps REST Services APIs.|  
|[Bing Maps Transit Coverage](../coverage/index.md)|Provides a list of transit agencies that are used by Bing Maps REST Services to provide transit routes.|  
  
## Transaction Accounting

 Transactions are counted for each Bing Maps REST Services request sent with a valid Bing Maps Key. For information about billable and non-billable transactions for the Bing Maps REST Services, see [Understanding Bing Maps Transactions](../getting-started/bing-maps-dev-center-help/understanding-bing-maps-transactions.md).
