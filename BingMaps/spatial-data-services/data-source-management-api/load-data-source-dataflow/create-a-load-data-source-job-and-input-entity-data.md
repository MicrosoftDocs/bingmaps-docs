---
title: "Create a Load Data Source Job and Input Entity Data | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 7f460cef-d6c4-4b54-9b88-7aa4216ecf0c
caps.latest.revision: 82
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Create a Load Data Source Job and Input Entity Data
Use the following URL to create, stage and update a data source. This URL creates a load data source dataflow job.  
  
 You can also use the [Bing Maps Account Center](http://www.bingmapsportal.com) to create or update a data source. For more information, see [Creating and Managing Data Sources](http://msdn.microsoft.com/en-us/library/hh698204.aspx).  
  
 A job is created when you create, stage or update a data source. Before using this API, review the job limits in [Geocode and Data Source Limits](../../geocode-and-data-source-limits.md).  
  
## Supported HTTP Methods  
 POST  
  
## URL template  
  
> [!NOTE]
> This template supports both HTTP and HTTPS protocols. URLs in the response use HTTPS protocol.  
  
 **Create a load data source job to create or update a data source.**  
  
 This URL creates a load data source job to create, stage or update a data source.  
  
 The response to this HTTP request returns a URL that you can use to check the status of the load data source job.  
  
 Before using this API, make sure you know the [Geocode and Data Source Limits](../../geocode-and-data-source-limits.md) which include data and job limits.  
  
 The master key and the query key must be different Bing Maps Keys from the same .  
  
```  
http://spatial.virtualearth.net/REST/v1/Dataflows/LoadDataSource?dataSourceName=dataSourceName&loadOperation=loadOperation&dataLocation=dataLocation&setPublic=setPublic&input=input&output=output&key=masterKey&queryKey=queryKey  
```  
  
### Template Parameters  
  
> [!NOTE]
> Parameter names and values are not case-sensitive except for the key and queryKey parameter values.  
  
|Parameter|Alias|Description|Values|  
|---------------|-----------|-----------------|------------|  
|accessId||**Optional.** A unique ID for the data source. Provide it when performing an incremental upload to an existing data source.|A string containing an ID that is part of the URL structure that identifies the data source.<br /><br /> **Example**: a92dcfac8a0894bc4921ad5c74022623|  
|dataSourceName||**Required** The name of the data source.|A user-defined string that contains a name for the data source.<br /><br /> A data source name can have up to 50 characters and can contain alphanumeric characters and any of the following:<br /><br /> ~ ` ! $ ^ _ = { }<br /><br /> **Example**: dataSourceName=FourthCoffeeSample|  
|dataLocation||**Optional.** Specifies the location of the data that you want to load into the data source. The data must contain a data schema along with the data sets. The location must be hosted by the [Windows®F Azure™ Blob Service](http://msdn.microsoft.com/en-us/library/dd135733.aspx). **Note:**  You must set the dataLocation parameter to the location of the data or include the data to process in the HTTP request. If you do both, the URL returns an error.|A Windows Azure™ Blob Service location that contains the data to process. The Blob Service uses the following URL formats:<br /><br /> http://*account-name*.blob.core.windows.net/*myDataFile*<br /><br /> https://*account-name*.blob.core.windows.net/*myDataFile*<br /><br /> For more information, see [Addressing Blob Service Requests](http://msdn.microsoft.com/en-us/library/dd135731.aspx).<br /><br /> Before you make your request to start the dataflow job, make sure that the Blob Service URL is available publicly or shared with a signature key. If the URL is shared with a signature key, it must be encoded. For more information, see [Managing Access to Containers and Blobs](http://msdn.microsoft.com/en-us/library/ee393343.aspx).<br /><br /> The following content types are supported for data that is retrieved:<br /><br /> -   application/xml<br />-   text/xml<br />-   text/plain<br />-   application/octet-stream [for compressed data]<br /><br /> If you are specifying an Azure blob that is accessed by using a signature key, you must encode the URL.<br /><br /> **Example**: dataLocation=http://myAzureAccount.blob.core.windows.net/myEntityData<br /><br /> **Example for an Azure blob with a signature key**: dataLocation=http%3a%2f%2fmyAzureAccount.blob.core.windows.net%2fmyEntityData%3fse%3d2012-08-27T22%253A46%253A57Z%26sr%3db%26si%3d readonly%26sig%3dabcdef10389481|  
|input||**Required**. The format of the data schema and input data.|One of the following values:<br /><br /> -   kml<br />-   shp<br />-   xml<br />-   csv<br />-   tab<br />-   pipe<br /><br /> For more information about the data schema and input data formats including examples, see [Data Schema and Sample Input](../../data-source-management-api/load-data-source-dataflow/load-data-source-data-schema-and-sample-input.md).<br /><br /> **Example**:input=csv|  
|setPublic||**Optional** Specifies whether the data source is publicly-accessible.<br /><br /> You can change the public status after the data source is created. For more information see [Make a Data Source Public](../../data-source-management-api/make-public-data-source.md).|One of the following values:<br /><br /> -   1: Make the data source publicly accessible to anyone with a valid Bing Maps Key.<br />-   **0 [default]**: Do not make the data source public.<br /><br /> This option is not valid for staged data sources. A staged data source is one where the loadOperation parameter is set to completeStaging or incrementalStaging.<br /><br /> **Example**: setPublic=1|  
|loadOperation||**Required** The type of operation to perform with the data.|One of the following values:<br /><br /> -   complete: Publishes entity data to a new data source or overwrites an existing data source.<br />-   completeStaging: Performs the same operation as "complete" except that the data source data is staged and not published. Use the query URLs with the `isStaged` parameter set to `1` (true) to query the staged data source. See [Publish a Staged Data Source](../../data-source-management-api/load-data-source-dataflow/publish-staged-data-source.md) for the URL to use when you are ready to publish. Staged data sources that are not published are deleted after 30 days.<br />-   incremental: Edit, add and delete entities in an existing data source.<br />     If you want to delete entities, you must add a property named `__deleteEntity` to the schema and set it to `1` or `true` for each entity that you want to remove.<br />-   incrementalStaging: Performs the same operation as "incremental" except that the data source update is staged and not published. Use the query URLs with the `isStaged` parameter set to `1` or `true` to query the staged data source. See [Publish a Staged Data Source](../../data-source-management-api/load-data-source-dataflow/publish-staged-data-source.md) for the URL to use when you are ready to publish. Staged data sources that are not published are deleted after 30 days.<br /><br /> **Example**: loadOperation=complete|  
|output|o|**Optional**. The output format for the response.|One of the following values:<br /><br /> -   json **[default]**<br />-   xml<br /><br /> **Example**: output=xml|  
|key||**Required.** The Bing Maps Key to use to create or access the data source. If you are creating a new data source, this Bing Maps Key becomes the master key for the data source. If you are updating a data source, you must set the key parameter to the data source master key. **Note:**  The master key and the query key must be different Bing Maps Keys from the same Bing Maps Account.|A Bing Maps Key obtained from the [Bing Maps Account Center](https://www.bingmapsportal.com/). For information about how to get a Bing Maps Key, see [Getting a Bing Maps Key](http://msdn.microsoft.com/en-us/library/ff428642.aspx).<br /><br /> **Example**: key=abc123def456ghi789abc123def456ghi789|  
|queryKey||**Optional**. A Bing Maps Key that is used to query the data source. **Note:**  The master key and the query key must be different Bing Maps Keys from the same Bing Maps Account.|A Bing Maps Key obtained from the [Bing Maps Account Center](https://www.bingmapsportal.com/). For information about how to get a Bing Maps Key, see [Getting a Bing Maps Key](http://msdn.microsoft.com/en-us/library/ff428642.aspx).<br /><br /> All queries on the data source can use this key. You can also use the master key to query the data source. The master key is the Bing Maps Key that you used for the `key` parameter when you create the data source.<br /><br /> If you do not specify a query key, then you can query the data source with any Bing Maps Key that is associated with the same Bing Maps Account as the data source master key. **Important:**  It is best practice to use a Bing Maps Key that is different than the master key to query the data source because the master key is also used to update and delete the data source. When you use the master key for queries, you increase the chance for the master key to be compromised by an unauthorized user. <br /><br /> **Example**: queryKey=312456def132ghi789abc6473def456ghi321|  
  
## Input  
 When you create the HTTP request to upload data and create a load data source job, you must post the input data in the body of the request or set the dataLocation parameter to a URL where your data can be retrieved. You must also set the content type in the request to one of the following input format values.  
  
 Input data must use UTF-8 encoding. For input data examples, see [Data Schema and Sample Input](../../data-source-management-api/load-data-source-dataflow/load-data-source-data-schema-and-sample-input.md).  
  
 This URL supports the following input formats.  
  
-   KML (application/xml)  
  
-   SHP (application/octet-stream)  
  
-   XML (application/xml)  
  
-   XML (text/xml)  
  
-   Comma-delimited values (text/plain)  
  
-   Tab-delimited values (text/plain)  
  
-   Pipe-delimited values (text/plain)  
  
-   Binary (application/octet-stream) [for compressed data]  
  
## Response  
 The response to this URL contains a link that you can use to get the status of the load data source job.  
  
 This URL supports the following response formats.  
  
-   JSON (application/json)  
  
-   XML (application/xml)  
  
 For detailed information about the response, see [Response Data](../../data-source-management-api/load-data-source-dataflow/load-data-source-dataflow-response-description.md).  
  
## Examples  
 **EXAMPLE: Create a load data source job to create a new data source that includes the input data in the HTTP request.**  
  
 This example creates a new data source and provides a data schema with entity data to load into the data source. For more information about the data schema and input data, see [Data Schema and Sample Input](../../data-source-management-api/load-data-source-dataflow/load-data-source-data-schema-and-sample-input.md). Because the dataLocation parameter is not specified in this example, the input data must be included in the HTTP request. The specified query key must be used to perform any query operations against this data source. The query key is a Bing Maps Key that belongs to the same Bing Maps Account as the Bing Maps Key used for the key parameter.  
  
 **URL and XML response**  
  
```  
http://spatial.virtualearth.net/REST/v1/Dataflows/LoadDataSource?loadOperation=complete&input=xml&o=xml&key=masterKey&query=queryKey  
```  
  
```  
<Response xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"   
          xmlns:xsd="http://www.w3.org/2001/XMLSchema"   
          xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>© 2011 Microsoft and its suppliers. This API and any results cannot be used or accessed without Microsoft’s express written permission.</Copyright>  
  <BrandLogoUri>http://spatial.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>201</StatusCode>  
  <StatusDescription>Created</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>2bf0339473434af7b34336790b001f7</TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <DataflowJob>  
          <Id>f8293dc72ac04942b7cb003c9608c547</Id>  
          <Link role="self">https://spatial.virtualearth.net/REST/v1/dataflows/LoadDataSource/f8293dc72ac04942b7cb003c9608c547</Link>  
          <Status>Pending</Status>  
          <CreatedDate>2010-11-12T20:03:56.3157889-08:00</CreatedDate>  
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
  
 **URL and JSON response**  
  
 The response returns a URL that you can use to get status of the dataflow job that was created. The URL is provided as the value of a `"url"` element under `links` with the attribute `"role"` set to `"self"`.  
  
```  
http://spatial.virtualearth.net/REST/v1/Dataflows/LoadDataSource?loadOperation=complete&input=xml&key=masterKey&queryKey=queryKey  
```  
  
```  
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
               "createdDate":"Fri, 12 Nov 2010 20:03:56 GMT",  
               "description":"FourthCoffeeSample Data Source",  
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
   "traceId":"3fa754b674cc431d8a72d86a5aea27be"  
}  
```  
  
 **EXAMPLE: Create a load data source job to update, add and delete specified entities.**  
  
 The input format for creating a data source and adding or updating entities is the same. If you are also deleting entries, you must add a schema property named __deleteEntity to your schema  
  
```  
http://spatial.virtualearth.net/REST/v1/Dataflows/LoadDataSource?loadOperation=incremental&input=xml&o=xml&key=masterKey  
```  
  
 **EXAMPLE: Create a load data source job to create a new data source and use the `dataLocation` parameter to specify the location of the input data.**  
  
```  
http://spatial.virtualearth.net/REST/v1/Dataflows/LoadDataSource?loadOperation=complete&dataLocation=http://myAzureAccount.blob.core.windows.net/myEntityData&input=x  
ml&o=xml&key=masterKey&queryKey=queryKey  
```  
  
## HTTP Status Codes  
 In addition to HTTP status codes, error information is provided in the response to this request. For more information, see the [Response Data](../../data-source-management-api/load-data-source-dataflow/load-data-source-dataflow-response-description.md).  
  
> [!NOTE]
>  For more details about these HTTP status codes, see [Status Codes and Error Handling](../../status-codes-and-error-handling.md).  
  
 When the request is successful, the following HTTP status code is returned.  
  
-   201  
  
 When the request is not successful, the response returns one of the following errors.  
  
-   400  
  
    -   A 400 HTTP status code can occur when you try to create a data source with the same name as a data source you just deleted, but the delete job has not completed.  
  
-   403  
  
    -   A 403 HTTP status code can occur when you try to create a data source for an account that already has the maximum of 25 published data sources.  
  
-   500  
  
-   503