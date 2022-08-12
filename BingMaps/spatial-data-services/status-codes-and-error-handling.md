---
title: "Status Codes and Error Handling1 | Microsoft Docs"
description: "Each response to a request provides an HTTP status code. This article lists the most common HTTP status codes that are provided from these requests." 
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d9cd4164-d7c5-475b-ac34-89130d4c1bf8
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Status Codes and Error Handling

Each response to a request provides an HTTP status code. This article describes these codes.  
  
## HTTP Status Codes  

The following table lists the most common HTTP status codes. Additional information may be provided with a specific request.  
  
|HTTP Status Code|Description|Details|  
|----------------------|-----------------|-------------|  
|200|OK|The request is successful.|  
|201|Created|A new resource is created.|  
|202|Accepted|The request has been accepted for processing.|  
|400|Bad Request|The request contained an error.|  
|401|Unauthorized|Access was denied. You may have entered your credentials incorrectly, or you might not have access to the requested resource or operation.|  
|403|Forbidden|The request is for something forbidden. Authorization will not help.|  
|404|Not Found|The requested resource was not found.|  
|500|Internal Server Error|Your request could not be completed because there was a problem with the service.|  
|503|Service Unavailable|There's a problem with the service right now. Please try again later.|