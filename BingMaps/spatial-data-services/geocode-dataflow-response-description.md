---
title: "Geocode Dataflow Response Description | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 5e2b1201-e119-4cc2-9251-d252ceff5d4e
caps.latest.revision: 19
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Geocode Dataflow Response Description
The following tables describe the response syntax for a Geocode Dataflow request in a set of hierarchical tables. Examples in JSON and XML formats are also provided.  
  
## Response  
 The following fields are the top-level fields in the Geocode Dataflow response. Additional tables describe the fields in each of the collections.  
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|`copyright`|`Copyright`|*string*|A copyright notice.|  
|`brandLogoUri`|`BrandLogoUri`|*string*|A URL that references a brand image to support contractual branding requirements.|  
|`statusCode`|`StatusCode`|*integer*|The HTTP Status code for the request.|  
|`statusDescription`|`StatusDescription`|*string*|A description of the HTTP status code.|  
|`authenticationResultCode`|`AuthenticationResultCode`|One of the following values:<br /><br /> `ValidCredentials`<br /><br /> `InvalidCredentials`<br /><br /> `CredentialsExpired`<br /><br /> `NotAuthorized`<br /><br /> `NoCredentials`<br /><br /> `None`|A status code that offers additional information about authentication success or failure.|  
|`traceId`|`TraceId`|*string*|A unique identifier for the request.|  
|`resourceSets`|`ResourceSets`|*collection*|A collection of ResourceSet objects. A ResourceSet is a container of Resources returned by the request. For more information, see the ResourceSet section below.|  
|`errorDetails`|`ErrorDetails`|*string[]*|A collection of error descriptions. For example, ErrorDetails can identify parameter values that are not valid or are missing.|  
  
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
|`links`|`Link`|*URL*|A URL that is defined by its role and name attributes.<br /><br /> `“role”:”self”`: Use to check the status of your job.<br /><br /> `“role”:”output”` and `“name”:“succeeded”`: Use to download data that was processed successfully.<br /><br /> `“role”:”output”` and `“name”:“failed”`: Use to download data that was not processed successfully.|  
|`description`|`Description`|*string*|A user-defined description of the dataflow job. If a description is not specified when the workflow is created, this field is not included or the value is null.|  
|`status`|`Status`|One of the following values:<br /><br /> `Pending`: The dataflow job is processing.<br /><br /> `Completed`: The dataflow job has completed. A status of completed does not indicate success.<br /><br /> `Aborted`: The workflow stopped because of an error.|The status of the dataflow job.|  
|`createdDate`|`CreatedDate`|*DateTime*|The date and time that the dataflow job was created.|  
|`completedDate`|`CompletedDate`|*DateTime*|The date and time that the dataflow job is completed. If the `Status` field is set to `Pending`, the `CompletedDate` field is not shown or is empty.|  
|`totalEntityCount`|`TotalEntityCount`|*integer*|The total number of entities that were uploaded.|  
|`processedEntityCount`|`ProcessedEntityCount`|*integer*|The number of entities that were processed. This number included entities that were processed successfully and those that failed. If the field is set to 0, the number of processed entries is not known.|  
|`failedEntityCount`|`FailedEntityCount`|*integer*|The number of entities that did not process successfully because of an error.|  
|`errorMessage`|`ErrorMessage`|*string*|Additional error information that is provided when the `Status` is set to `Aborted`.|  
  
## DataflowJob Response Examples  
 The following examples show DataflowJob resource content in JSON and XML formats.  
  
### JSON Example  
  
```  
{  
   "authenticationResultCode":"ValidCredentials",  
   "brandLogoUri":"http:\/\/spatial.virtualearth.net\/Branding\/logo_powered_by.png",  
   "copyright":"© 2010 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
   "resourceSets":[  
      {  
         "estimatedTotal":1,  
         "resources":[  
            {  
               "__type":"DataflowJob:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "id":"5bf10c37df944083b1879fbb0556e67e",  
               "links":[  
                  {  
                     "role":"self",  
                     "url":"https:\/\/spatial.virtualearth.net\/REST\/v1\/dataflows\/Geocode\/5bf10c37df944083b1879fbb0556e67e"  
                  },  
                  {  
                     "name":"succeeded",  
                     "role":"output",  
                     "url":"https:\/\/spatial.virtualearth.net\/REST\/v1\/dataflows\/Geocode\/5bf10c37df944083b1879fbb0556e67e\/output\/succeeded"  
                  },  
                  {  
                     "name":"failed",  
                     "role":"output",  
                     "url":"https:\/\/spatial.virtualearth.net\/REST\/v1\/dataflows\/Geocode\/5bf10c37df944083b1879fbb0556e67e\/output\/failed"  
                  }  
               ],  
               "completedDate":"Mon, 10 May 2010 20:23:49 GMT",  
               "createdDate":"Mon, 10 May 2010 20:22:35 GMT",  
               "description":"Xml",  
               "failedEntityCount":2,  
               "processedEntityCount":12,  
               "status":"Completed",  
               "totalEntityCount":12  
            }  
         ]  
      }  
   ],  
   "statusCode":200,  
   "statusDescription":"OK",  
   "traceId":"e8bfe25fdc4f4bc5824cda4e568e1c19"  
}  
```  
  
### XML Example  
  
```  
<Response xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>© 2010 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>  
  <BrandLogoUri>http://spatial.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>f65bd9af90e241b3a7d52316314eb352|BL12080319|02.00.103.1000|</TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <DataflowJob>  
          <Id>5bf10c37df944083b1879fbb0556e67e</Id>  
          <Link role="self">https://spatial.virtualearth.net /REST/v1/dataflows/Geocode/5bf10c37df944083b1879fbb0556e67e</Link>  
          <Link role="output" name="succeeded">https://spatial.virtualearth.net/REST/v1/dataflows/Geocode/5bf10c37df944083b1879fbb0556e67e/output/succeeded</Link>  
          <Link role="output" name="failed">https://spatial.virtualearth.net/REST/v1/dataflows/Geocode/5bf10c37df944083b1879fbb0556e67e/output/failed</Link>  
          <Description>Xml</Description>  
          <Status>Completed</Status>  
          <CreatedDate>2010-05-10T13:22:35.0553408-07:00</CreatedDate>  
          <CompletedDate>2010-05-10T13:23:49.1959658-07:00</CompletedDate>  
          <TotalEntityCount>12</TotalEntityCount>  
          <ProcessedEntityCount>12</ProcessedEntityCount>  
          <FailedEntityCount>2</FailedEntityCount>  
        </DataflowJob>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
```