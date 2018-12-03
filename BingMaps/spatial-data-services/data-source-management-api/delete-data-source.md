---
title: "Delete a Data Source | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 1b73707d-9a7f-4ae5-bc38-838080640db4
caps.latest.revision: 26
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Delete a Data Source
Use the following URL to delete a data source. To delete a data source, a delete data source job is created.  
  
 You can also use the [Bing Maps Account Center](http://www.bingmapsportal.com) to delete a data source. For more information, see [Creating and Managing Data Sources](http://msdn.microsoft.com/en-us/library/hh698204.aspx).  
  
 A job is created when you delete a data source.  Before using this API, review the job limits in [Geocode and Data Source Limits](../geocode-and-data-source-limits.md).  
  
 To get a list of all the data source and geocode jobs submitted in the last 15 days, see [Get Job List](../get-job-list.md).  
  
## Supported HTTP Methods  
 DELETE  
  
### URL Template  
 **Delete a data source.**  
  
 The key parameter in this URL must be set to the data source master key.  
  
 You can get the data source base component (http://spatial.virtualearth.net/REST/v1/data/*accessId*/*dataSourceName*), by using the [Get Data Source Information](../data-source-management-api/get-data-source-information.md) API and requesting information about all the data sources associated with the Bing Maps Account that manages the data source.  
  
 The URL uses the **HTTP DELETE** method so you cannot delete a datasource by typing the URL directly in the address bar of a browser. See the **Example** section for more information.  
  
```url
http://spatial.virtualearth.net/REST/v1/data/accessId/dataSourceName?key=masterKey  
```  
  
 After you initiate a job to delete a data source, you must wait until the delete job is completed before creating a new data source with the same name.  
  
## Template Parameters  
  
> [!NOTE]
>  Parameter names and values are not case sensitive except for the key parameter value.  
  
|Parameter|Description|Values|  
|---------------|-----------------|------------|  
|accessId|**Required**. A unique ID for the data source.|A string containing and ID that is part of the URL structure that identifies the data source.<br /><br /> You can retrieve the accessId and dataSourceName values when you get information about all datasources. For more information, see [Get Data Source Information](../data-source-management-api/get-data-source-information.md).<br /><br /> **Example**: a92dcfac8a0894bc4921ad5c74022623.|  
|dataSourceName|**Required** The name of the data source that you want to search.|A string that identifies the data source. The name is part of the URL structure that identifies the data source.<br /><br /> You can retrieve the accessId and dataSourceName values when you get information about all datasources. For more information, see [Get Data Source Information](../data-source-management-api/get-data-source-information.md).<br /><br /> **Example**: FourthCoffeeSample|  
|isStaging|**Optional**. Specifies to delete the staged version of the data source.|A Boolean value.<br /><br /> -   0 or false**[default]**<br />-   1 or true<br /><br /> **Example**: isStaging=1|  
|key|**Required**. The master key for the data source.|The Bing Maps Key that was specified as the master key when the data source was created.<br /><br /> **Example**: key=abc123def456ghi789abc123def456ghi789|  
  
## Response  
 If the data source is successfully deleted, the HTTP 202 status code is returned. The response does not contain any content.  
  
## Example  
 **EXAMPLE: Delete a data source.**  
  
 The following request deletes a data source. The key parameter must be set to the data source master key. You cannot submit this URL directly from the Address bar in a browser because the URL uses the HTTP DELETE method. You may want to use a tool such as [Fiddler](https://www.fiddler2.com/fiddler2/) or [cURL](https://curl.haxx.se/) to submit this URL request.  
  
```url
DELETE http://spatial.virtualearth.net/REST/v1/data/12ccc26d9e9412345f94922212345/ADataSourceName?key=masterKey HTTP/1.1  
```  
  
## HTTP Status Codes  
  
> [!NOTE]
>  For more details about these HTTP status codes, see [Status Codes and Error Handling](../status-codes-and-error-handling.md).  
  
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