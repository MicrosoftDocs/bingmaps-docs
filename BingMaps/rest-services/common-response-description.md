---
title: "Common Response Description | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 51a9e43b-ce57-45f8-a6d5-dca8b755b384
caps.latest.revision: 27
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Common Response Description
The response to a Bing Maps REST Services URL request includes the status of the request and one or more resources that contain location, imagery, or route information. The resource information that is returned depends on the Bing Maps REST Services URL that is used and the parameter values that are provided with it. For example, a [Locations](../rest-services/locations-api.md) URL returns one or more Location resources that provide location information based on the values in the URL request.  
  
 The following tables describe the common fields that are returned in the response to a Bing Maps REST Services URL request. For more information about specific resource content, see the API reference for the Locations, Imagery, and Routes APIs.  
  
## Response  
 The Response container for a request provides the following information.  
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|statusCode|StatusCode|integer|The HTTP Status code for the request.|  
|statusDescription|StatusDescription|string|A description of the HTTP status code.|  
|authenticationResultCode|AuthenticationResultCode|One of the following values:<br /><br /> ValidCredentials<br /><br /> InvalidCredentials<br /><br /> CredentialsExpired<br /><br /> NotAuthorized<br /><br /> NoCredentials<br /><br /> None|A status code that offers additional information about authentication success or failure.|  
|traceId|TraceId|string|A unique identifier for the request.|  
|copyright|Copyright|string|A copyright notice.|  
|brandLogoUri|BrandLogoUri|string|A URL that references a brand image to support contractual branding requirements.|  
|resourceSets|ResourceSets|collection|A collection of ResourceSet objects. A ResourceSet is a container of Resources returned by the request. For more information, see the ResourceSet section below.|  
|errorDetails|ErrorDetails|string[]|A collection of error descriptions. For example, ErrorDetails can identify parameter values that are not valid or missing.|  
  
## ResourceSet  
 The ResourceSet container provides the following information.  
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|estimatedTotal|EstimatedTotal|long|An estimate of the total number of resources in the ResourceSet.|  
|resources|Resources|collection|A collection of one or more resources. The resources that are returned depend on the request. Information about resources is provided in the API reference for each Bing Maps REST Services API.|  
  
## Examples  
 The following are examples JSON and XML responses.  
  
### JSON Response Example  
  
```  
{  
    "authenticationResultCode":"ValidCredentials",  
    "brandLogoUri":"http:\/\/dev.virtualearth.net\/Branding\/logo_powered_by.png",  
    "copyright":"Copyright © 2010 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
    "resourceSets":[  
        {  
            "estimatedTotal":1,  
            "resources":[  
                {  
                   Resource content specific to a REST service  
                }  
            ]  
        }  
    ],  
    "statusCode":200,  
    "statusDescription":null,  
    "traceId":"961e9c1e63e64bd4aa7d140ee4e05697"  
}  
```  
  
### XML Response Example  
  
```  
<Response xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>Copyright © 2010 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>  
  <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>25c368c85b964f4c978ff932b966a9d4</TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <Resource>  
          <!-- Resource content specific to a REST service -->  
        </Resource>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
  
```