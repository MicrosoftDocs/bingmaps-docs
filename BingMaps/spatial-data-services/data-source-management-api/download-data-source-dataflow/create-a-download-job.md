---
title: "Create a Download Job | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: e630d52c-f5dc-452e-8bb4-aa1ca115362c
caps.latest.revision: 14
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Create a Download Job
Use the following URL to download entity data from a published data source.  
  
 You can also use the [Bing Maps Account Center](http://www.bingmapsportal.com) to download a data source. For more information, see [Creating and Managing Data Sources](http://msdn.microsoft.com/en-us/library/hh698204.aspx) in the Bing Maps Account Center Help.  
  
## Supported HTTP Methods  
 GET  
  
## URL template  
  
> [!IMPORTANT]
>  This template supports both HTTP and HTTPS protocols. URLs in the response use HTTPS protocol.  
  
 **Download data source entity data.**  
  
 This URL creates a DataSourceDownload job that downloads entity data and the data schema for a data source. You can download the published data source or up to two (2) prior versions or a staged version by specifying a data source job ID.  
  
```url
http://spatial.virtualearth.net/REST/v1/Dataflows/DataSourceDownload/accessId/dataSourceName?output=output&jobId=jobId&key=DataSourceMasterKey  
```  
  
 After you create a download job, use the status URL provided in the response to check status. For more information about the status URL, see the **Examples** section and [Get Download Data Source Job Status](../../data-source-management-api/download-data-source-dataflow/get-download-data-source-job-status.md).  
  
 For a step-by-step description of how use the DataSourceDownload Dataflow to download entity data, see [Walkthrough](../../data-source-management-api/download-data-source-dataflow/download-data-source-walkthrough.md).  
  
## Template Parameters  
  
> [!NOTE]
>  Parameter names and values are not case sensitive except for the key parameter value.  
  
|Parameter|Alias|Description|Values|  
|---------------|-----------|-----------------|------------|  
|accessId||**Required**. A unique ID for the data source.|A string containing and ID that is part of the URL structure that identifies the data source.<br /><br /> You can retrieve the accessId and dataSourceName values when you get information about all datasources. For more information, see [Get Data Source Information](../../data-source-management-api/get-data-source-information.md).<br /><br /> **Example**: a92dcfac8a0894bc4921ad5c74022623.|  
|dataSourceName||**Required** The name of the data source that you want to search.|A string that identifies the data source. The name is part of the URL structure that identifies the data source.<br /><br /> You can retrieve the accessId and dataSourceName values when you get information about all datasources. For more information, see [Get Data Source Information](../../data-source-management-api/get-data-source-information.md).<br /><br /> **Example**: MyDataSourceName|  
|jobId||**Optional** The job ID that specifies the data source version to download.|A GUID that identifies the version of the data source to download. The published version is downloaded by default. Up to two (2) previous versions and one (1) staged version of a data source may be available for download. To see the job IDs of all versions of a data source, query for information about that data source with `showAllVersions` set to `true`. For more information, see [Get Data Source Information](../../data-source-management-api/get-data-source-information.md).|  
|output|o|**Optional**. The output format for the response.|One of the following values:<br /><br /> -   json **[default]**<br />-   xml<br /><br /> **Example**: o=xml|  
|key||**Required**. The master key for the data source.|The Bing Maps Key that was specified as the master key when the data source was created.<br /><br /> **Example**: key=abc123def456ghi789abc123def456ghi789|  
  
## Response  
 This URL supports the following response formats.  
  
-   JSON: **application/json**  
  
-   XML: **application/xml**  
  
 For information about the response, see [Response Data](../../data-source-management-api/download-data-source-dataflow/download-data-source-dataflow-response-description.md).  
  
## Examples  
 **EXAMPLE: Create a job to download entity data from a data source.**  
  
 The following request example shows how to request a data source download job. The key parameter must be set to the data source master key.  
  
 The response specifies a status URL that you can use to monitor the download job status. This status URL is highlighted in the response examples below. See [Get Download Data Source Job Status](../../data-source-management-api/download-data-source-dataflow/get-download-data-source-job-status.md) to learn how to use the status URL to determine when the download job is complete.  
  
```url
http://spatial.virtualearth.net/REST/v1/data/DataSourceDownload/12ccc26d9e9412345f94922212345/DataSourceName?o=xml&key=DataSourceMasterKey  
```  
  
 **XML Response**  
  
 This URL will return a response similar to the following example.  
  
```xml
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
          <Link role="self">https://spatial.virtualearth.net/REST/v1/dataflows/DataSourceDownload/DataSourceName</Link>  
          <Status>Pending</Status>  
          <CreatedDate>2011-11-17T12:38:16.8179772-08:00</CreatedDate>  
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
  
 **JSON Response**  
  
 If o=xml was not specified in the response, a JSON response similar to the following example is returned.  
  
```json
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
                     "url":"https:\/\/spatial.virtualearth.net\/REST\/v1\/dataflows\/DataSourceDownload\/DataSourceName"  
                  }  
               ],  
               "createdDate":"Thu, 17 Nov 2011 20:38:31 GMT",  
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
   "traceId":"9bc6dede6e79468ba1cc3728aa7f1cb4"  
}  
```  
  
## HTTP Status Codes  
  
> [!NOTE]
>  For more details about these HTTP status codes, see [Status Codes and Error Handling](../../status-codes-and-error-handling.md).  
  
 When the request is successful, the following HTTP status code is returned.  
  
-   202  
  
 When the request is not successful, the response returns one of the following errors.  
  
-   400  
  
-   401  
  
     This error code can occur in any of the following conditions:  
  
    -   The key parameter is not specified.  
  
    -   The specified key value is not a valid Bing Maps Key.  
  
    -   The specified key is not the master key for the data source.  
  
-   404  
  
    -   This error code can occur when the data source does not exist.  
  
-   500  
  
-   503