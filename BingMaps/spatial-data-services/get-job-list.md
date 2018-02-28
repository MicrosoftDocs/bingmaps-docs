---
title: "Get Job List | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 22d545f5-551e-4cd3-bd61-c31cd9311358
caps.latest.revision: 8
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Get Job List
Use the following URL to get a list of all dataflow and data source jobs that were submitted in the last 15 days for the account associated with the Bing Maps Key specified in the request. Jobs are created when you geocode entities and create or modify a data source. Both pending and completed jobs are returned with pending jobs listed first. Note that download jobs are not included in this list.  
  
 Some data source processes may include more than one jobs. For example, if you stage a data source and then publish it, you will have run both a DataSourceIncrementalStaging joband a DataSourcePublishFromStaged job. This is important because there are limits to the number of jobs you can run in a given time period. For more information about job limits and other API requirements, see [Geocode and Data Source Limits](../spatial-data-services/geocode-and-data-source-limits.md).  
  
## URL Template  
  
```  
http://spatial.virtualearth.net/REST/v1/dataflows/listjobs?key=AccountBingMapsKey&output=output  
```  
  
### Template Parameters  
  
|Parameter|Alias|Description|Values|  
|---------------|-----------|-----------------|------------|  
|key||**Required**. A Bing Maps Key associated with the Bing Maps Account that you want to query.|A Bing Maps Key obtained from the Bing Maps Account Center that is associated with the account you want to query. For information about how to get a Bing Maps Key, see [Getting a Bing Maps Key](../getting-started/getting-a-bing-maps-key.md).<br /><br /> Example: key=abc123def456ghi789abc123def456ghi789|  
|output|o|**Optional**. The output format for the response.|One of the following values:<br /><br /> -   json **[default]**<br />-   xml<br /><br /> **Example**: output=xml|  
  
## Response  
 The response to a get job list request returns information about the following jobs. Job creation and job completed times are provided as well as the status (Pending or Completed). Note that Data Source Download Dataflow jobs are not returned by the API.  
  
 Jobs marked with an asterisk (*) are also created when you use the [!INCLUDE[maps_devportal_name](../getting-started/includes/maps-devportal-name-md.md)] to manage your data sources.  
  
|Job Type|Description|  
|--------------|-----------------|  
|Geocode*|Geocode Dataflow Job|  
|DataSourceComplete*|Load Data Source Dataflow Job to create or to completely overwrite a data source.|  
|DataSourceIncremental*|Load Data Source Dataflow Job to incrementally update selected entities in a data source.|  
|DataSourceCompleteStaging|Load Data Source Dataflow Job that stages an update to a data source that creates or overwrites the data source.|  
|DataSourceIncrementalStaging|Load Data Source Dataflow Job that stages an incremental update to a data source.|  
|DataSourcePublishFromStaged|Data Source Publish Job that publishes a staged data source.|  
|DataSourceRollback|Data Source Rollback Dataflow job that restores a previous version of the data source.|  
|DataSourceDelete*|Data Source Delete Job that deletes a data source.|  
|DataSourceAccess*|Make a Data Source Public or Private Job to specify whether the data source can be accessed with any Bing Maps Key (public).|  
  
## Example  
 **Get a list of all dataflow and data source jobs that were submitted in the last 15 days.**  
  
```  
http://spatial.virtualearth.net/REST/v1/Dataflows/ListJobs?key=BingMapsKey  
```  
  
 **JSON Response**  
  
 This example returns the following response that lists all the pending and completed jobs from the last 15 days.  
  
```  
{  
   "authenticationResultCode":"ValidCredentials",  
   "brandLogoUri":"http:\/\/spatial.virtualearth.net\/Branding\/logo_powered_by.png",  
   "copyright":"Copyright © 2013 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
   "resourceSets":[  
      {  
         "estimatedTotal":110,  
         "resources":[  
            {  
               "__type":"DataServiceJob:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "id":"0deea07139a742e7a03a74bb4784a738",  
               "name":"DeleteADataSource  
               "createdDate":"Fri, 04 Jan 2013 01:06:23 GMT",  
               "description":"DataSourceDelete",  
               "status":"Pending"  
            },  
            {  
               "__type":"DataflowJob:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "id":"28217d5f12744c33be7d09f6bce76eb3",  
               "name":"CreateOrUpdateADataSource",  
               "completedDate":"Thu, 03 Jan 2013 23:22:15 GMT",  
               "createdDate":"Thu, 03 Jan 2013 23:21:58 GMT",  
               "description":"DataSourceComplete",  
               "failedEntityCount":0,  
               "processedEntityCount":3,  
               "status":"Completed",  
               "totalEntityCount":3  
            },  
            {  
               "__type":"DataflowJob:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "id":"47e6703c22d34df98d48674b803f17cb",  
               "links":[  
                  {  
                     "role":"self",  
                     "url":"https:\/\/spatial.virtualearth.net\/REST\/v1\/dataflows\/Geocode\/47e6703c22d34df98d48674b803f22cb"  
                  },  
                  {  
                     "name":"succeeded",  
                     "role":"output",  
                     "url":"https:\/\/spatial.virtualearth.net\/REST\/v1\/dataflows\/ListJobs\/47e6703c22d34df98d48674b803f22cb\/output\/succeeded"  
                  }  
               ],  
               "completedDate":"Wed, 02 Jan 2013 23:32:27 GMT",  
               "createdDate":"Wed, 02 Jan 2013 23:32:24 GMT",  
               "description":"Geocode",  
               "failedEntityCount":0,  
               "processedEntityCount":3,  
               "status":"Completed",  
               "totalEntityCount":3  
            },  
            {  
               "__type":"DataflowJob:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "id":"82876e0717114bc1ad2b94e9111e4206",  
               "name":"IncrementalUpdateOfDataSource",  
               "completedDate":"Thu, 20 Dec 2012 19:23:19 GMT",  
               "createdDate":"Thu, 20 Dec 2012 19:23:08 GMT",  
               "description":"DataSourceIncremental",  
               "failedEntityCount":0,  
               "processedEntityCount":4,  
               "status":"Completed",  
               "totalEntityCount":4  
            },  
            {  
               "__type":"DataServiceJob:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "id":"9a25a8b26e9c4d569ebfee76ea940160",  
               "links":[  
                  {  
                     "name":"service",  
                     "role":"dataSource",  
                     "url":"https:\/\/spatial.virtualearth.net\/REST\/v1\/data\/c589f4fb424048428d602ff6cd0a49eb\/SetDataSourcePublicOrPrivate"  
                  }  
               ],  
               "name":"SetDataSourcePublicOrPrivate ",  
               "completedDate":"Thu, 20 Dec 2012 19:15:36 GMT",  
               "createdDate":"Thu, 20 Dec 2012 19:14:33 GMT",  
               "description":"DataSourceAccess",  
               "status":"Completed"  
            }  
         ]  
      }  
   ],  
   "statusCode":200,  
   "statusDescription":"OK",  
   "traceId":"3f3b4619b0b7485a97feb883eb871f70"  
}  
```  
  
 **XML Response**  
  
 This XML response is returned when output=xml is added to the URL.  
  
```  
<Response xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>Copyright © 2013 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>  
  <BrandLogoUri>http://spatial.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>f8e999a06f3b449894c175aded847e12</TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>110</EstimatedTotal>  
      <Resources>  
        <DataServiceJob>  
          <Name>DeleteADataSource</Name>  
          <Id>0deea07139a742e7a03a74bb4784a738</Id>  
          <Description>DataSourceDelete</Description>  
          <Status>Pending</Status>  
          <CreatedDate>2013-01-03T17:06:23.546903-08:00</CreatedDate>  
          <CompletedDate xsi:nil="true"/>  
        </DataServiceJob>  
        <DataflowJob>  
          <Name>CreateOrUpdateADataSource</Name>  
          <Id>28217d5f12744c33be7d09f6bce76eb3</Id>  
          <Description>DataSourceComplete</Description>  
          <Status>Completed</Status>  
          <CreatedDate>2013-01-03T15:21:58.2262338-08:00</CreatedDate>  
          <CompletedDate>2013-01-03T15:22:15.7979398-08:00</CompletedDate>  
          <TotalEntityCount>3</TotalEntityCount>  
          <ProcessedEntityCount>3</ProcessedEntityCount>  
          <FailedEntityCount>0</FailedEntityCount>  
        </DataflowJob>  
        <DataflowJob>  
          <Id>47e6703c22d34df98d48674b803f17cb</Id>  
          <Link role="self">https://spatial.virtualearth.net/REST/v1/dataflows/Geocode/47e6703c22d34df98d48674b803f22cb</Link>  
          <Link role="output" name="succeeded">https://spatial.virtualearth.net/REST/v1/dataflows/ListJobs/47e6703c22d34df98d48674b803f22cb/output/succeeded</Link>  
          <Description>Geocode</Description>  
          <Status>Completed</Status>  
          <CreatedDate>2013-01-02T15:32:24.1743172-08:00</CreatedDate>  
          <CompletedDate>2013-01-02T15:32:27.1934569-08:00</CompletedDate>  
          <TotalEntityCount>1234</TotalEntityCount>  
          <ProcessedEntityCount>1234</ProcessedEntityCount>  
          <FailedEntityCount>0</FailedEntityCount>  
        </DataflowJob>  
        <DataflowJob>  
          <Name>IncrementalUpdateOfDataSource</Name>  
          <Id>82876e0717114bc1ad2b94e9111e4206</Id>  
          <Description>DataSourceIncremental</Description>  
          <Status>Completed</Status>  
          <CreatedDate>2012-12-20T11:23:08.6682264-08:00</CreatedDate>  
          <CompletedDate>2012-12-20T11:23:19.7245133-08:00</CompletedDate>  
          <TotalEntityCount>4321</TotalEntityCount>  
          <ProcessedEntityCount>4321</ProcessedEntityCount>  
          <FailedEntityCount>0</FailedEntityCount>  
        </DataflowJob>  
        <DataServiceJob>  
          <Name>SetDataSourcePublicOrPrivate</Name>  
          <Id>9a25a8b26e9c4d569ebfee76ea940160</Id>  
          <Link role="dataSource" name="service">https://spatial.virtualearth.net/REST/v1/data/c589f4fb424048428d602ff6cd0a22eb/ SetDataSourcePublicOrPrivate </Link>  
          <Description>DataSourceAccess</Description>  
          <Status>Completed</Status>  
          <CreatedDate>2012-12-20T11:14:33.2400466-08:00</CreatedDate>  
          <CompletedDate>2012-12-20T11:15:36.5972052-08:00</CompletedDate>  
        </DataServiceJob>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
  
```