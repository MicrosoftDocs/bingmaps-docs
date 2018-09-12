---
title: "Get Download Data Source Job Status | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: b773d45c-ad44-4c88-8baa-de6fb8f09ca7
caps.latest.revision: 7
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Get Download Data Source Job Status
Use the following URL to get the status of a download data source job.  
  
## Supported HTTP Methods  
 GET  
  
## URL template  
  
> [!NOTE]
>  This template supports both HTTP and HTTPS protocols. URLs in the response use HTTPS protocol.  
  
 **Get status information for a data source download job.**  
  
 A status URL in the following format without the output parameter and master key is provided in the response to the URL request that you made to [Create a Download Job](../spatial-data-services/create-a-download-job.md). The status URL is specified in a `link` field with an attribute of `self`. This URL with the data source master key provides the status of the job.  
  
```  
http://spatial.virtualearth.net/REST/v1/Dataflows/DataSourceDownload/DataSourceName?output=output&key=DataSourceMasterKey  
```  
  
 When the download job status is set to Completed, a download URL is included in the response. For information about accessing downloaded entity data, see the **Examples** section below and  [Get Downloaded Data](../spatial-data-services/get-downloaded-data.md).  
  
 For a step-by-step description of how use the Download Data Source Dataflow, see [Walkthrough](../spatial-data-services/download-data-source-walkthrough.md).  
  
### Template Parameters  
  
> [!NOTE]
>  Parameter names and values are not case-sensitive except for the key parameter value.  
  
|Parameter|Alias|Description|Values|  
|---------------|-----------|-----------------|------------|  
|DataSourceName||**Required.** The name of the data source.|**Example**: MyDataSourceName|  
|key||**Required**. The data source master key.|A Bing Maps Key that is  the data source master key.<br /><br /> **Example**: key=abc123def456ghi789abc123def456ghi789|  
|output|o|**Optional**. The output format for the response.|One of the following values:<br /><br /> -   json **[default]**<br />-   xml<br /><br /> **Example**: o=xml|  
  
## Response  
 This URL supports the following response formats.  
  
-   JSON: **application/json**  
  
-   XML: **application/xml**  
  
 For information about the response, see [Response Data](../spatial-data-services/download-data-source-dataflow-response-description.md).  
  
## Examples  
 This example requests status information in XML format for a download job for MyDataSourceName data source. When the job status is complete, a download URL is included in the response that you can use to download data. See [Get Downloaded Data](../spatial-data-services/get-downloaded-data.md) for more information. The example responses are for a completed job and the download URL is highlighted.  
  
```  
http://spatial.virtualearth.net/REST/v1/Dataflows/DataSourceDownload/MyDataSourceName?o=xml&key=DataSourceMasterKey  
```  
  
 **XML Response**  
  
 This URL will return a response similar to the following example.  
  
```  
<?xml version="1.0" encoding="utf-8"?>  
<Response xmlns:xsi="https://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="https://www.w3.org/2001/XMLSchema" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>Copyright © 2011 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>  
  <BrandLogoUri>http://spatial.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>201</StatusCode>  
  <StatusDescription>Created</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>0ddc1a3bd3dc46e28c92bb01942b0812</TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <DataflowJob>  
          <Id>8ccf2a5b428d423c92759150dcddc338</Id>  
          <Link role="self">https://spatial.virtualearth.net/REST/v1/dataflows/DataSourceDownload/MyDataSourceName</Link>  
          <Status>Completed</Status>  
          <Link role="output" name="succeeded">https://spatial.virtualearth.net/REST/v1/dataflows/DataSourceDownload/MyDataSourceName/output/succeeded</Link>  
          <CreatedDate>2011-11-17T12:50:08.8179772-08:00</CreatedDate>  
          <CompletedDate xsi:nil="true" />  
          <TotalEntityCount>300</TotalEntityCount>  
          <ProcessedEntityCount></ProcessedEntityCount>  
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
   "copyright":"Copyright © 2011 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
   "resourceSets":[  
      {  
         "estimatedTotal":1,  
         "resources":[  
            {  
               "__type":"DataflowJob:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "id":"8ccf2a5b428d423c92759150dcddc338",  
               "links":[  
                  {  
                     "role":"self",  
                     "url":"https:\/\/spatial.virtualearth.net\/REST\/v1\/dataflows\/DataSourceDownload\/MyDataSourceName"  
                  },  
                  {  
                     "role":"output",  
                     "output":"succeeded",  
                     "url":"https:\/\/spatial.virtualearth.net\/REST\/v1\/dataflows\/DataSourceDownload\/MyDataSourceName\/ouput\/succeeded"  
                  }  
  
               ],  
               "createdDate":"Thu, 17 Nov 2011 20:38:31 GMT",  
               "failedEntityCount":0,  
               "processedEntityCount":0,  
               "status":"Completed",  
               "totalEntityCount":300  
            }  
         ]  
      }  
   ],  
   "statusCode":201,  
   "statusDescription":"Created",  
   "traceId":"9bc6dede6e79468ba1cc3728aa7f1cb4"  
}  
```  
  
## HTTP Status Codes  
  
> [!NOTE]
>  For more details about these HTTP status codes, see [Status Codes and Error Handling](../spatial-data-services/status-codes-and-error-handling.md).  
  
 When the request is successful, the following HTTP status code is returned.  
  
-   200  
  
 When the request is not successful, the response returns one of the following HTTP status codes.  
  
-   400  
  
-   500  
  
-   503