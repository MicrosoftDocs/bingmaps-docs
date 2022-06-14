---
title: "Download Data Source Dataflow Response Description | Microsoft Docs"
description: "Describes process of downloading data source dataflow responses and provides a table that outlines a description, type, and fields forJSON and XML."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: c0553260-3516-4979-a9ff-3d1338ae8c3a
caps.latest.revision: 5
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Download Data Source Dataflow Response Description
The following tables describe the response syntax for a Data Source Download Dataflow request in a set of hierarchical tables.  
  
## Response  
 The following fields are the top-level fields in the Download Data Source Dataflow response. Additional tables describe the fields in each of the collections.  
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|`copyright`|`Copyright`|*string*|A copyright notice.|  
|`brandLogoUri`|`BrandLogoUri`|*string*|A URL that references a brand image to support contractual branding requirements.|  
|`statusCode`|`StatusCode`|*integer*|The HTTP Status code for the request.|  
|`statusDescription`|`StatusDescription`|*string*|A description of the HTTP status code.|  
|`authenticationResultCode`|`AuthenticationResultCode`|One of the following values:<br /><br /> `ValidCredentials`<br /><br /> `InvalidCredentials`<br /><br /> `CredentialsExpired`<br /><br /> `NotAuthorized`<br /><br /> `NoCredentials`<br /><br /> `None`|A status code that offers additional information about authentication success or failure.|  
|`traceId`|`TraceId`|*string*|A unique identifier for the request.|  
|`resourceSets`|`ResourceSets`|*collection*|A collection of `ResourceSet` objects. A `ResourceSet` is a container of Resources returned by the request. For more information, see the ResourceSet section below.|  
|`errorDetails`|`ErrorDetails`|*string[]*|A collection of error descriptions. For example, `ErrorDetails` can identify parameter values that are not valid or are missing. An error log URL is also provided as part of `links` or `Link` fields.|  
  
## ResourceSet  
 The ResourceSet container provides the following information.  
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|`estimatedTotal`|`EstimatedTotal`|*long*|An estimate of the total number of resources in the ResourceSet.|  
|`resources`|`Resources`|*collection*|A collection of one or more DataflowJob resources. Information about the DataflowJob resource is found in the DataflowJob section.|  
  
## DataflowJob  
 The DataflowJob resource container provides the following information.  
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|`id`|`Id`|*string*|A unique string that identifies the dataflow job. There are no requirements for the string format.|  
|`links`|`Link`|*URL*|URLs that is defined by its role and name attributes.<br /><br /> `“role”:”self”`: Use to check the status of your job. This URL is provided in the response when you create a load data source job.<br /><br /> `“role”:”output”` and `“name”:”succeeded”`: Use to access the downloaded entity data. This URL appears in the response only when the job status is set to Completed.<br /><br /> `“role”:”output”` and `“name”:”failed”`: Use to access the error log for the job. This URL appears in the response only when the job status is set to Aborted.|  
|`status`|`Status`|One of the following values:<br /><br /> `Pending`: The dataflow job is processing.<br /><br /> `Completed`: The dataflow job has completed.<br /><br /> `Aborted`: The workflow stopped because of an error.|The status of the dataflow job.|  
|`createdDate`|`CreatedDate`|*DateTime*|The date and time that the dataflow job was created.|  
|`completedDate`|`CompletedDate`|*DateTime*|The date and time that the dataflow job is completed. If the `Status` field is set to `Pending`, the `CompletedDate` field is not shown or is empty.|  
|`totalEntityCount`|`TotalEntityCount`|*integer*|The total number of entities that were uploaded.|  
|`processedEntityCount`|`ProcessedEntityCount`|*integer*|This field is not used.|  
|`failedEntityCount`|`FailedEntityCount`|*integer*|This field is not used.|  
|`errorMessage`|`ErrorMessage`|*string*|Additional error information that is provided when the `Status` is set to `Aborted`. A link to an error log is also provided in the `links` or `Link` field.|  
  
## Data Source Download Response Examples  
 The following examples show DataflowJob resource content in JSON and XML formats.  
  
### JSON Example  
  
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
  
### XML Example  
  
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
          <Link role="self">https://spatial.virtualearth.net/REST/v1/dataflows/DataSourceDownload/MyDataSourceName</Link>  
          <Status>Completed</Status>  
          <Link role="output" name="succeeded">https://spatial.virtualearth.net/REST/v1/dataflows/DataSourceDownload/MyDataSourceName/output/succeeded</Link>  
          <CreatedDate>2011-11-17T12:50:08.8179772-08:00</CreatedDate>  
          <CompletedDate xsi:nil="true" />  
          <TotalEntityCount>300</TotalEntityCount>  
          <ProcessedEntityCount>0</ProcessedEntityCount>  
          <FailedEntityCount>0</FailedEntityCount>  
        </DataflowJob>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
  
```