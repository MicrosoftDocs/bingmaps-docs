---
title: "Make a Data Source Public | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: a0462c29-ea78-440b-836a-24cfb81341ec
caps.latest.revision: 15
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Make a Data Source Public

Use the following URLs to make your data source publicly accessible or to make it private. A public data source can be queried by anyone with a Bing Maps Key. A private data source can only queried using the data source query key only.  
  
 You can also use the [Bing Maps Account Center](http://www.bingmapsportal.com) to change the public status of a data source. For more information, see [Making a Data Source Public or Private](../../getting-started/bing-maps-dev-center-help/geocoding-and-managing-data-sources/making-a-data-source-public-or-private.md).  
  
 A job is created when you change the public status of a data source.  Before using this API, review the job limits in [Geocode and Data Source Limits](../geocode-and-data-source-limits.md).  
  
 To get a list of all the data source and geocode jobs submitted in the last 15 days, see [Get Job List](../get-job-list.md).  
  
## Supported HTTP Methods  
 GET  
  
## URL templates  
 **Set a data source to publicly accessible by setting the setPublic parameter.**.  
  
```url
http://spatial.virtualearth.net/REST/v1/data/accessID/dataSourceName/$updateDataSource?setPublic=setPublic&key=masterKey  
```  
  
 The base part of the following URL with *accessID* and *dataSourceName* is returned when you create the data source. It is also returned when you request information for all data sources that belong to a Bing Maps Account.  
  
### Template Parameters  
  
> [!NOTE]
>  Parameter names and values are not case-sensitive except for the key parameter value.  
  
|Parameter|Description|Values|  
|---------------|-----------------|------------|  
|accessId|**Required**. A unique ID for the data source.|A string containing and ID that is part of the URL structure that identifies the data source.<br /><br /> **Example**: a92dcfac8a0894bc4921ad5c74022623.|  
|dataSourceName|**Required**. The name of the data source that you want to search.|A string that identifies the data source. The name is part of the URL structure that identifies the data source.<br /><br /> **Example**: FourthCoffeeSample|  
|setPublic|**Required**. Specifies whether the data source is publicly available or private.|One of the following values:<br /><br /> -   1: Make the data source publicly accessible to anyone with a valid Bing Maps Key.<br />-   **0 [default]**: Do not make the data source public.<br /><br /> **Example**: setPublic=1|  
  
## Response  
 This URL supports the following response formats.  
  
-   JSON: **application/json**  
  
-   XML: **application/xml**  
  
 For information about the response, see [Response Data](download-data-source-dataflow/download-data-source-dataflow-response-description.md).  
  
## Examples  
 **EXAMPLE: Make a data source publicly available.** .  
  
 The following request makes the specified data source public.  
  
```url
http://spatial.virtualearth.net/REST/v1/data/d2accd5bf52e486f8261c4889d5940d6/FourthCoffeeSample/$updatedatasource?setPublic=1&o=xml&key=MasterKey  
```  
  
 The status of `Created` in the response indicates that the job to make the data source public has been created. This operation is expected to take only a few minutes. You can confirm that the data source is public by requesting data source information with the [Get Data Source Information](get-data-source-information.md) API. Depending on the request and response format, one of the following parameters should be set to true: bsi:isPublic="true","IsPublic":"true", or IsPublic="true".  
  
 **URL with XML Response**  
  
```xml  
<Response xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"   
          xmlns:xsd="http://www.w3.org/2001/XMLSchema"   
          xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>  
    Copyright © 2012 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.  
  </Copyright>  
  <BrandLogoUri>  
    http://spatial.virtualearth.net/Branding/logo_powered_by.png  
  </BrandLogoUri>  
  <StatusCode>201</StatusCode>  
  <StatusDescription>Created</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>  
    47fbdfa7eb2d4bc8ba06fb9f37aeb2fd  
  </TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <Resource xsi:type="DataServiceJob">  
          <Id>a7edd54c39704e638603a62ff42d4d39</Id>  
          <Description>Data source "FourthCoffeeSample" set public</Description>  
          <Status>Created</Status>  
          <CreatedDate>2012-10-16T15:45:24.7616166-07:00</CreatedDate>  
          <CompletedDate xsi:nil="true"/>  
        </Resource>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
  
```  
  
 **URL with JSON Response**  
  
 If o=xml was not specified in the response, a JSON response similar to the following example is returned.  
  
```json
{  
   "authenticationResultCode":"ValidCredentials",  
   "brandLogoUri":"http:\/\/spatial.virtualearth.net\/Branding\/logo_powered_by.png",  
   "copyright":"Copyright © 2012 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
   "resourceSets":[  
      {  
         "estimatedTotal":1,  
         "resources":[  
            {  
               "__type":"DataServiceJob:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "id":"38545e58f0204310afb9a39998ffe13b",  
               "createdDate":"Tue, 16 Oct 2012 22:47:15 GMT",  
               "description":"Data source \"FourthCoffeeSample\" set public",  
               "status":"Created"  
            }  
         ]  
      }  
   ],  
   "statusCode":201,  
   "statusDescription":"Created",  
   "traceId":"4799eeda80e445b4a1f0de6591b296b1"  
}  
```  
  
## HTTP Status Codes  
  
> [!NOTE]
>  For more details about these HTTP status codes, see [Status Codes and Error Handling](../status-codes-and-error-handling.md).  
  
 When the request is successful, the following HTTP status code is returned.  
  
-   202  
  
 When the request is not successful, the response returns one of the following errors.  
  
-   400  
  
-   401  
  
-   500  
  
-   503