---
title: "Status Codes and Error Handling2 | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 22fc6fbd-889f-4fd7-ab08-98e69c27f92a
caps.latest.revision: 11
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Status Codes and Error Handling
## Handling empty responses  
 Occasionally, the servers processing service requests can be overloaded, and you may receive some responses that contain no results for queries that you would normally receive a result. To identify this situation, check the HTTP headers of the response. If the HTTP header X-MS-BM-WS-INFO is set to 1, it is best to wait a few seconds and try again.  
  
 This may happen occasionally for Basic or Trial Bing Maps Keys, and rarely for Enterprise Bing Maps Keys. If you are experiencing this behavior continually with an Enterprise Bing Maps Key, contact [Bing Maps Enterprise Support](https://support.microsoft.com/oas/default.aspx?prid=13766&st=1).  
  
## HTTP Status Codes  
 Each response to a request provides an HTTP status code. The following table lists the most common HTTP status codes. Additional information may be provided with a specific request.  
  
|HTTP Status Code|Short Description|Details|  
|----------------------|-----------------------|-------------|  
|200|OK|The request is successful.|  
|201|Created|A new resource is created.|  
|202|Accepted|The request has been accepted for processing.|  
|400|Bad Request|The request contained an error.|  
|401|Unauthorized|Access was denied. You may have entered your credentials incorrectly, or you might not have access to the requested resource or operation.|  
|403|Forbidden|The request is for something forbidden. Authorization will not help.|  
|404|Not Found|The requested resource was not found.|  
|429|Too Many Requests|The user has sent too many requests in a given amount of time. The account is being rate limited.|  
|500|Internal Server Error|Your request could not be completed because there was a problem with the service.|  
|503|Service Unavailable|There's a problem with the service right now. Please try again later.|