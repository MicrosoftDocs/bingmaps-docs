---
title: "Get Load Data Source Status | Microsoft Docs"
description: "Describes how to get the status of a load data source job and provides supported HTTP methods, the URL template, template parameters, and HTTP status codes."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: a6fd1bab-f8c9-47e7-9691-232e9727e230
caps.latest.revision: 24
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Get Load Data Source Status

[!INCLUDE [bing-maps-spatial-data-service-data-source-management-api-retirement](../../includes/bing-maps-spatial-data-service-data-source-management-api-retirement.md)]

Use the following URL to get the status of a load data source job.  
  
## Supported HTTP Methods  
 GET  
  
## URL template  
  
> [!NOTE]
>  This template supports both HTTP and HTTPS protocols. URLs in the response use HTTPS protocol.  
  
 **Get status information for a load data source job.**  
  
 When you request status information for a load data source job, you must specify the master key for the data source. You request job status by using the URL returned in the response when you [Create a Load Data Source Job](../../data-source-management-api/load-data-source-dataflow/create-a-load-data-source-job-and-input-entity-data.md). The URL is specified in a `link` field of the response and has a `role` attribute set to `self`. To use this status URL, you must add the key parameter and set it to the data source master key. You can optionally add the output parameter to specify the how the response is returned. The URL template below shows the format of this status URL.  
  
 When the load data source job is complete, the response to this status URL contains another `link` field with the `role` attribute set to `datasource`. This link field contains a unique URL that you can use to query the data source. For more information, see [Response Data](../../data-source-management-api/load-data-source-dataflow/load-data-source-dataflow-response-description.md).  
  
```url
http://spatial.virtualearth.net/REST/v1/Dataflows/LoadDatasource/DataFlowJobID?output=output&key=masterKey  
```  
  
### Template Parameters  
  
> [!NOTE]
>  Parameter names and values are not case-sensitive except for the key parameter value.  
  
|Parameter|Alias|Description|Values|  
|---------------|-----------|-----------------|------------|  
|DataFlowJobID||**Required.** The job ID for the Load Data Source Dataflow job. This ID is returned in the response when you create a data source job and is also included in the "self" status link.|**Example**: f8293dc72ac04942b7cb003c9608c547|  
|key||**Required.** The master key for the data source.|The Bing Maps Key that was specified as the master key for the data source. For more information, see [Create a Load Data Source Job](../../data-source-management-api/load-data-source-dataflow/create-a-load-data-source-job-and-input-entity-data.md).|  
|output|o|**Optional**. The output format for the response.|One of the following values:<br /><br /> -   json **[default]**<br />-   xml<br /><br /> **Example**: o=xml|  
  
## Response  
 This URL supports the following response formats.  
  
-   JSON: **application/json**  
  
-   XML: **application/xml**  
  
 For information about the response, see [Response Data](../../data-source-management-api/load-data-source-dataflow/load-data-source-dataflow-response-description.md).  
  
## Examples  
 **EXAMPLE: Request job status for a load data source job.**  
  
 This example requests status information for the load data source job named FourthCoffeeSample that was created by specifying the master key b1c323ea23d99d267d99d267bbb814. This URL without the key and output parameters is returned in the response when you use the URL to [Create a Load Data Source Job](../../data-source-management-api/load-data-source-dataflow/create-a-load-data-source-job-and-input-entity-data.md).  
  
 **Responses returned while the job is in process**  
  
 While the job is in process, the `Status` in the response is set to `Pending`.  
  
 When the job completes, the `Status` field in the response is set to `Completed` and a URL that is unique to the data source is returned. This unique URL is contained as a link field that has a `role` attribute set to `self` and a `name` attribute set to `service`.  
  
 **URL with XML Response**  
  
```url
http://spatial.virtualearth.net/REST/v1/Dataflows/LoadDatasource/f8293dc72ac04942b7cb003c9608c547?o=xml&key=b1c323ea23d99d267d99d267bbb814  
```  
  
 **XML Response when the job is in process**  
  
 In this response, the `Status` field is set to `Pending` because the load data source job is in process.  
  
```xml
<Response xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"   
               xmlns:xsd="http://www.w3.org/2001/XMLSchema"    
               xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>© 2011 Microsoft and its suppliers. This API and any results cannot be used or accessed without Microsoft’s express written permission.</Copyright>  
  <BrandLogoUri>http://spatial.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>9401a5764214a3b87a4c982d2d98a64<TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <DataflowJob>  
          <Id>f8293dc72ac04942b7cb003c9608c547</Id>  
          <Link role="self">https://spatial.virtualearth.net/REST/v1/dataflows/LoadDataSource/f8293dc72ac04942b7cb003c9608c547</Link>  
          <Status>Pending</Status>  
          <CreatedDate>2010-11-13T12:58:39.3157889-08:00</CreatedDate>  
          <CompletedDate xsi:nil="true" />  
          <TotalEntityCount>0</TotalEntityCount>  
          <ProcessedEntityCount>0</ProcessedEntityCount>  
          <FailedEntityCount>0</FailedEntityCount>  
        </DataflowJob>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
  
```  
  
 **XML Response returned when the job has completed.**  
  
 In this response, the `Status` field is set to `Completed` and a new `link` field that has the role `attribute` set to `datasource` and the name attribute set to `service` is also returned.  
  
```xml
<Response xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"   
               xmlns:xsd="http://www.w3.org/2001/XMLSchema"   
               xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>© 2011 Microsoft and its suppliers. This API and any results cannot be used or accessed without Microsoft’s express written permission.</Copyright>  
  <BrandLogoUri>http://spatial.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>9401a5764214a3b87a4c982d2d98a64<TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <DataflowJob>  
          <Id>f8293dc72ac04942b7cb003c9608c547</Id>  
          <Link role="self">https://spatial.virtualearth.net/REST/v1/dataflows/LoadDataSource/f8293dc72ac04942b7cb003c9608c547</Link>  
          <Link role="datasource" name="service">https://spatial.virtualearth.net/REST/v1/data/20181f26d9e94c81acdf9496133d4f23/FourthCoffeeSample</Link>  
          <Status>Completed</Status>  
          <CreatedDate>2010-11-13T12:58:39.3157889-08:00</CreatedDate>  
          <CompletedDate>2010-11-13T12:59:45.4724897-08:00</CompletedDate>  
          <TotalEntityCount>0</TotalEntityCount>  
          <ProcessedEntityCount>0</ProcessedEntityCount>  
          <FailedEntityCount>0</FailedEntityCount>  
        </DataflowJob>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
  
```  
  
 **URL with JSON Responses**  
  
```url
http://spatial.virtualearth.net/REST/v1/Dataflows/LoadDatasource/f8293dc72ac04942b7cb003c9608c547?key=b1c323ea23d99d267d99d267bbb814  
```  
  
 **JSON Response returned when the job is in process.**  
  
 In this response, the `status` field is set to `Pending` because the load data source job is in process.  
  
```json
{  
   "authenticationResultCode":"ValidCredentials",  
   "brandLogoUri":"http:\/\/spatial.virtualearth.net\/Branding\/logo_powered_by.png",  
   "copyright":"© 2011 Microsoft and its suppliers. This API and any results cannot be used or accessed without Microsoft’s express written permission.",  
   "resourceSets":[  
      {  
         "estimatedTotal":1,  
         "resources":[  
            {  
               "__type":"DataflowJob:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "id":"f8293dc72ac04942b7cb003c9608c547",  
               "links":[  
                  {  
                     "role":"self",  
                     "url":"https:\/\/spatial.virtualearth.net\/REST\/v1\/dataflows\/LoadDataSource\/f8293dc72ac04942b7cb003c9608c547"  
                  }  
               ],  
               "createdDate":"Mon, 13 Nov 2010 20:58:39 GMT",  
               "failedEntityCount":0,  
               "processedEntityCount":0,  
               "status":"Pending",  
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
  
 **JSON Response returned when the job has completed.**  
  
 In this response, the `Status` field is set to `Completed` and a new `links` value that has the role `attribute` set to `"datasource"` and the name attribute set to `"service"` is also returned.  
  
```json
{  
   "authenticationResultCode":"ValidCredentials",  
   "brandLogoUri":"http:\/\/spatial.virtualearth.net\/Branding\/logo_powered_by.png",  
   "copyright":"© 2011 Microsoft and its suppliers. This API and any results cannot be used or accessed without Microsoft’s express written permission.",  
   "resourceSets":[  
      {  
         "estimatedTotal":1,  
         "resources":[  
            {  
               "__type":"DataflowJob:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "id":"f8293dc72ac04942b7cb003c9608c547",  
               "links":[  
                  {  
                     "role":"self",  
                     "url":"https:\/\/spatial.virtualearth.net\/REST\/v1\/dataflows\/LoadDataSource\/f8293dc72ac04942b7cb003c9608c547"  
                  }  
                  {  
                     "name":"service",  
                     "role":"datasource",  
                     "url":"https:\/\/spatial.virtualearth.net\/REST\/v1\/data\/20181f26d9e94c81acdf9496133d4f23\/FourthCoffeeSample"  
                  }  
               ],  
               "completedDate":"Mon, 13 Nov 2010 20:59:45 GMT",  
               "createdDate":"Mon, 13 Nov 2010 20:58:39 GMT",  
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
  
## HTTP Status Codes  
  
> [!NOTE]
>  For more details about these HTTP status codes, see [Status Codes and Error Handling](../../status-codes-and-error-handling.md).  
  
 When the request is successful, the following HTTP status code is returned.  
  
-   200  
  
 When the request is not successful, the response returns one of the following HTTP status codes.  
  
-   400  
  
-   401  
  
-   500  
  
-   503