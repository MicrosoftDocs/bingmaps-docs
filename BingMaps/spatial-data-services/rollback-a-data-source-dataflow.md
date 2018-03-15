---
title: "Rollback a Data Source Dataflow | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ea1f98a3-20b3-4eac-9633-2150a97df888
caps.latest.revision: 11
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bingmaps"
---
# Rollback a Data Source Dataflow
Use the following URLs to rollback a data source to a previous version. Up to two (3) previous versions of a data source are available.  
  
 A job is created when you rollback a data source.  Before using this API, review the job limits in [Geocode and Data Source Limits](../spatial-data-services/geocode-and-data-source-limits.md).  
  
 To get a list of all the data source and geocode jobs submitted in the last 15 days, see [Get Job List](../spatial-data-services/get-job-list.md).  
  
## Supported HTTP Methods  
 GET  
  
## URL Template  
  
> [!NOTE]
>  This template supports both HTTP and HTTPS protocols. URLs in the response use HTTPS protocol.  
  
 **Rollback to a previously published version of a data source**  
  
 To find the job ID for the data source version you want to restore, query for information about a data source using the `showAllVersions` parameter. For more information, see [Get Data Source Information](../spatial-data-services/get-data-source-information.md).  
  
```  
http://spatial.virtualearth.net/REST/v1/Dataflows/DataSourceRollback/previousVersionJobId/dataSourceName?output=output&key=masterKey  
```  
  
 **Get status to determine when the rollback is complete**  
  
 After you start the rollback process, you can check status using the URL provided in the response to the rollback request. When the data source rollback is completed, the status field in the response is set to `Completed`. The status URL has the following structure.  
  
```  
http://spatial.virtualearth.net/REST/v1/Dataflows/DataSourceRollback/rollbackJobId?output=output&key=masterKey  
```  
  
## Template Parameters  
  
> [!NOTE]
>  Parameter names and values are not case-sensitive except for the key parameter value.  
  
|Parameter|Alias|Description|Values|  
|---------------|-----------|-----------------|------------|  
|previousVersionJobId||**Required** The job ID of the data source you want to restore.|To find the job ID for the data source version you want to republish, query for information about a data source using the `showAllVersions` parameter. For more information, see [Get Data Source Information](../spatial-data-services/get-data-source-information.md).|  
|dataSourceName||**Required** The name of the data source.|**Example**: MyDataSourceName|  
|key||**Required.** The master key for the data source.|The Bing Maps Key that was specified as the master key for the data source. For more information, see [Create a Load Data Source Job](../spatial-data-services/create-a-load-data-source-job-and-input-entity-data.md).|  
|output|o|**Optional**. The output format for the response.|One of the following values:<br /><br /> -   json **[default]**<br />-   xml<br /><br /> **Example**: o=xml|  
  
## Response  
 This URL supports the following response formats.  
  
-   JSON: **application/json**  
  
-   XML: **application/xml**  
  
## Example  
 **EXAMPLE**: Make a request to roll back a data source to a previous version of the data and schema. This URL starts a rollback dataflow job.  
  
```  
http://dev.virtualearth.net/REST/v1/Dataflows/DataSourceRollback/e60b410fdbe845f3a1337f4f54f16e97/FourthCoffeeShop?o=xml&key=masterKey  
```  
  
 **XML Response**  
  
```  
<?xml version="1.0" encoding="UTF-8"?>  
<Response xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
  <Copyright>Copyright ©2013 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>  
  <BrandLogoUri>http://spatial.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>201</StatusCode>  
  <StatusDescription>Created</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>9fdc6e24dbca446daac390a98f7dc94f</TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <DataflowJob>  
          <Id>8a6229d493904715aedf3b2ef08611c0</Id>  
          <Link role="self">https://spatial.virtualearth.net/REST/v1/dataflows/DataSourceRollback/8a6229d493904715aedf3b2ef08611c0</Link>  
          <Description>DataSourceRollback</Description>  
          <Status>Created</Status>  
          <CreatedDate>2013-02-25T11:32:08.2160874-08:00</CreatedDate>  
          <CompletedDate xsi:nil="true"/>  
          <TotalEntityCount>0</TotalEntityCount>  
          <ProcessedEntityCount>0</ProcessedEntityCount>  
          <FailedEntityCount>0</FailedEntityCount>  
        </DataflowJob>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
  
```  
  
 **JSON Response**  
  
 If o=xml was not specified in the response, a JSON response similar to the following example is returned.  
  
```  
{  
   "authenticationResultCode":"ValidCredentials",  
   "brandLogoUri":"http:\/\/spatial.virtualearth.net\/Branding\/logo_powered_by.png",  
   "copyright":"Copyright 2013 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
   "resourceSets":[  
      {  
         "estimatedTotal":1,  
         "resources":[  
            {  
               "__type":"DataflowJob:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "id":"8a6229d493904715aedf3b2ef08611c0",  
               "links":[  
                  {  
                     "role":"self",  
                     "url":"https:\/\/spatial.virtualearth.net\/REST\/v1\/dataflows\/DataSourceRollback\/8a6229d493904715aedf3b2ef08611c0"  
                  }  
               ],  
               "name":"PreviousDataSource",  
               "createdDate":"Mon, 25 Feb 2013 19:17:04 GMT",  
               "description":"DataSourceRollback",  
               "failedEntityCount":0,  
               "processedEntityCount":0,  
               "status":"Pending",  
               "totalEntityCount":0  
            }  
         ]  
      }  
   ],  
   "statusCode":201,  
   "statusDescription":"Created",  
   "traceId":"416a72a10e664ec8a38425683f21bc48"  
}  
```  
  
 **Example:** Get the status of the DataSourceRollback dataflow job. When the `Status` is set to `Completed`, the rollback is complete.  
  
```  
https://spatial.virtualearth.net/REST/v1/dataflows/DataSourceRollback/e60b410fdbe845f3a1337f4f54f16e97?key=masterKey  
```  
  
 **XML Response**  
  
 The `dataSource` link provides the query URL for the restored data source.  
  
```  
<?xml version="1.0" encoding="utf-8" ?>  
<Response xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>Copyright © 2013 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>  
  <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>91331572df314911bc4b6ab4e2953ec1</TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <DataflowJob>  
          <Name>PreviousDataSource</Name>  
          <Id>741dedf051d14cbb8d84df9661bc27dd</Id>  
          <Link role="self">https://dev.virtualearth.net/REST/v1/dataflows/DataSourceRollback/741dedf051d14cbb8d84df9661bc27dd</Link>  
          <Link role="dataSource" name="service">https://dev.virtualearth.net/REST/v1/data/0edf86ad7e7042345323cb25af67916aa/FourthCoffeeSample</Link>  
          <Description>DataSourceRollback</Description>  
          <Status>Completed</Status>  
          <CreatedDate>2013-02-25T11:43:59.5194386-08:00</CreatedDate>  
          <CompletedDate>2013-02-25T11:44:10.1239816-08:00</CompletedDate>  
          <TotalEntityCount>0</TotalEntityCount>  
          <ProcessedEntityCount>0</ProcessedEntityCount>  
          <FailedEntityCount>0</FailedEntityCount>  
        </DataflowJob>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
  
```  
  
 **JSON Response**  
  
 If o=xml was not specified in the response, a JSON response similar to the following example is returned.  
  
```  
{  
   "authenticationResultCode":"ValidCredentials",  
   "brandLogoUri":"http:\/\/spatial.virtualearth.net\/Branding\/logo_powered_by.png",  
   "copyright":"© 2013 Microsoft and its suppliers. This API and any results cannot be used or accessed without Microsoft’s express written permission.",  
   "resourceSets":[  
      {  
         "estimatedTotal":1,  
         "resources":[  
            {  
               "__type":"DataflowJob:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "name":"PreviousDataSource",  
               "id":"741dedf051d14cbb8d84df9661bc27dd",  
               "links":[  
                  {  
                     "role":"self",  
                     "url":"https:\/\/spatial.virtualearth.net\/REST\/v1\/dataflows\/DataSourceRollback\/741dedf051d14cbb8d84df9661bc27dd"  
                  }  
                  {  
                     "name":"service",  
                     "role":"datasource",  
                     "url":"https:\/\/spatial.virtualearth.net\/REST\/v1\/data\/0edf86ad7e7042345323cb25af67916aa/\/FourthCoffeeSample"  
                  }  
               ],  
               "completedDate":" Mon, 25 Feb 2013 19:17:04 GMT",  
               "createdDate":" Mon, 25 Feb 2013 19:17:04 GMT",  
               "failedEntityCount":0,  
               "processedEntityCount":0,  
               "status":"Completed",  
               "totalEntityCount":0  
            }  
         ]  
      }  
   ],  
   "statusCode":200,  
   "statusDescription":"OK",  
   "traceId":"9401a5764214a3b87a4c982d2d98a64"  
}  
```