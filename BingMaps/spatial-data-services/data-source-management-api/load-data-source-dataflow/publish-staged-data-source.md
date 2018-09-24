---
title: "Publish a Staged Data Source | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 5532a64f-657f-49c3-8104-bce1db6ba419
caps.latest.revision: 6
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Publish a Staged Data Source
Use the following URL to publish a staged data source.  
  
 A job is created when you publish a staged a data source.  Before using this API, review the job limits in [Geocode and Data Source Limits](../../geocode-and-data-source-limits.md).  
  
## Supported HTTP Methods  
 GET  
  
## URL Template  
  
> [!NOTE]
>  This template supports both HTTP and HTTPS protocols. URLs in the response use HTTPS protocol.  
  
 Make sure you review the job limits defined in [Geocode and Data Source Limits](../../geocode-and-data-source-limits.md).  
  
 **Publish a staged data source**  
  
 This URL will publish a staged data source that was created by setting loadOperation=completeStaged or incrementalStaging when you created a [Load Data Source Job](../../data-source-management-api/load-data-source-dataflow/create-a-load-data-source-job-and-input-entity-data.md).  
  
```  
http://spatial.virtualearth.net/REST/v1/data/accessId/dataSourceName/$commit?output=output&key=masterKey  
```  
  
 **Get status to determine when the publish is complete**  
  
 After you start the publishing process, you can check status using the URL provided in the response to the publish request. When the staged data source is published and available to query, the `Status` field in the $getstatus response is set to `Completed`. The status URL has the following structure.  
  
```  
http://spatial.virtualearth.net/REST/v1/data/jobs/publishJobId/$getstatus?output=output&key=masterKey  
```  
  
## Template Parameters  
  
> [!NOTE]
>  Parameter names and values are not case-sensitive except for the key parameter value.  
  
|Parameter|Alias|Description|Values|  
|---------------|-----------|-----------------|------------|  
|accessId||**Required**. A unique ID for the data source.|You can retrieve the query URL that contains the accessId and dataSourceName values when you [Get Data Source Information](../../data-source-management-api/get-data-source-information.md) for all data sources or from you [Get Load Data Source Status](../../data-source-management-api/load-data-source-dataflow/get-load-data-source-status.md) for the completed job that staged the data.<br /><br /> **Example**: a92dcfac8a0894bc4921ad5c74022623.|  
|dataSourceName||**Required** The name of the data source.|You can retrieve the query URL that contains the accessId and dataSourceName values when you [Get Data Source Information](../../data-source-management-api/get-data-source-information.md) for all data sources or from you [Get Load Data Source Status](../../data-source-management-api/load-data-source-dataflow/get-load-data-source-status.md) for the completed job that staged the data.<br /><br /> **Example**: MyDataSourceName|  
|key||**Required.** The master key for the data source.|The Bing Maps Key that was specified as the master key for the data source. For more information, see [Create a Load Data Source Job](../../data-source-management-api/load-data-source-dataflow/create-a-load-data-source-job-and-input-entity-data.md).|  
|output|o|**Optional**. The output format for the response.|One of the following values:<br /><br /> -   json **[default]**<br />-   xml<br /><br /> **Example**: o=xml|  
  
## Response  
 This URL supports the following response formats.  
  
-   JSON: **application/json**  
  
-   XML: **application/xml**  
  
## Examples  
 **EXAMPLE: Publish a staged data source.**  
  
```  
http://spatial.virtualearth.net/REST/v1/data/12ccc26d9e9412345f94922212345/MyDataSourceName/$commit?o=xml&key=MyDataSourceMasterKey  
```  
  
 **XML Response**  
  
 This URL will return a response similar to the following example.  
  
```  
<?xml version="1.0" encoding="UTF-8"?>  
<Response xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
  <Copyright>Copyright © 2013 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>  
  <BrandLogoUri>http://spatial.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>202</StatusCode>  
  <StatusDescription>Accepted</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>21db26ff791144738230a9cf2cc9ff6aTraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <DataServiceJob>  
          <Id>3627f4ab4882498074e79cda29f3a</Id>  
          <Link role="self">https://spatial.virtualearth.net/REST/v1/data/jobs/3627f4ab4882498074e79cda29f3a/$getstatus</Link>  
          <Description>DataSourcePublishFromStaged</Description>  
          <Status>Accepted</Status>  
          <CreatedDate>2013-02-25T11:26:32.2843589-08:00</CreatedDate>  
          <CompletedDate xsi:nil="true"/>  
        </DataServiceJob>  
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
               "__type":"DataServiceJob:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "id":"3627f4ab4882498074e79cda29f3a",  
               "links":[  
                  {  
                     "role":"self",  
                     "url":"https:\/\/spatial.virtualearth.net\/REST\/v1\/data\/jobs\/3627f4ab4882498074e79cda29f3a\/$getstatus"  
                  }  
               ],  
               "createdDate":"Mon, 25 Feb 2013 19:27:54 GMT",  
               "description":"DataSourcePublishFromStaged",  
               "status":"Accepted"  
            }  
         ]  
      }  
   ],  
   "statusCode":202,  
   "statusDescription":"Accepted",  
   "traceId":"e60b410fdbe845f3a1337f4f54f16e98"  
}  
```  
  
 **Example:** Get the status of the DataSourcePublishFromStaged data source job. When the `Status` is set to `Completed`, the staged data source is successfully published. Not that this URL is from the response in the previous example with the master key added.  
  
```  
https://spatial.virtualearth.net/REST/v1/data/jobs/3627f4ab4882498074e79cda29f3a/$getstatus?key=masterKey  
```  
  
 **XML Response**  
  
```  
<?xml version="1.0" encoding="utf-8"?>  
<Response xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
  <Copyright>Copyright © 2013 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>  
  <BrandLogoUri>http://spatial.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>dac74e31ecae4312b91dd1c65a367987|BR1M006105|02.00.106.2200|</TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <DataServiceJob>  
          <Name>StageDataSource</Name>  
          <Id>3627acab48964b3896074e79cda29f3a</Id>  
          <Description>DataSourcePublishFromStaged</Description>  
          <Status>Completed</Status>  
          <CreatedDate>2013-02-25T11:26:31.8781295-08:00</CreatedDate>  
          <CompletedDate>2013-02-25T11:26:38.3090478-08:00</CompletedDate>  
        </DataServiceJob>  
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
   "copyright":"Copyright © 2013 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
   "resourceSets":[  
      {  
         "estimatedTotal":1,  
         "resources":[  
            {  
               "__type":"DataServiceJob:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "name":"PulishStagedDataSource",  
               "id":"3627acab48964b3896074e79cda29f3a",  
               "createdDate":"Tue, 16 Oct 2012 22:47:15 GMT",  
               "completedDate":"Tue, 16 Oct 2012 22:50:15 GMT",  
               "description":"DataSourcePublishFromStaged",  
               "status":"Completed"  
            }  
         ]  
      }  
   ],  
   "statusCode":201,  
   "statusDescription":"Created",  
   "traceId":"4799eeda80e445b4a1f0de6591b296b1"  
}  
  
```