---
title: "Bing Maps REST URL Structure | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "reference"
ms.assetid: a4b2979b-5634-4eac-a25e-95e11530fd04
caps.latest.revision: 28
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Base URL Structure

The Bing Maps REST Services are all called by using the following base formats.  
  
## HTTP protocol

```url
http://dev.virtualearth.net/REST/version/restApi/resourcePath?queryParameters&key=BingMapsKey  
```

## HTTPS protocol  

```url
https://dev.virtualearth.net/REST/version/restApi/resourcePath?queryParameters&key=BingMapsKey  
```

## Template Parameters  
  
> [!NOTE]
> All parameters in the Bing Maps REST Services are not case-sensitive.
  
|URL parameter|Alias|Description|Values|  
|------|-----------------|------------|---|  
|`version` |`v` + API version number)|**Required**. The version of the Bing Maps REST Services that you want to use.|A string containing `v` and an integer that specifies the version of the Bing Maps REST Services.<br /><br /> **Example**: v1.|
|`restApi`||**Required.** The REST API that you want to use.|A part of the URL path that identifies the REST API.<br /><br /> **Example**: Imagery/Map|
|`resourcePath`||**Optional.** Additional parameters that define a resource|A part of the URL path that specifies a resource, such as an address or landmark.<br /><br /> **Example**: BirdsEye/51.5063249319792,-0.127144753932953|
|`key`||**Required.** The Bing Maps Key to use for the request.|A Bing Maps Key obtained from the [Bing Maps Account Center](https://www.bingmapsportal.com/)<br /><br /> **Example**: key=A3sbe47EeFWsSlklbe **Note:**  Although it is described separately in this table because of its importance, the Bing Maps Key is a query parameter.|  
|`queryParameters`||**Optional with exceptions.** One or more parameters and values that define the request.|Depending on the request, query parameters may be optional or required. Query parameters consist of global parameters and parameters that are specific to each REST API. The Bing Maps Key is a required query parameter.<br /><br /> **Example**: userLocation=49.1231,-98.231|  
|`errorDetail`|`ed`|**Optional**. Specifies whether the response should include error-codes along with the error text.|Use with one of the following values.<br /><br /> -   `true`<br />-   `false` [default]<br /><br /> When this property is provided, response includes an error code along with a description for failed requests:<br /><br /> -   **errorCode**: "NoSolution"<br />-   **errorDetails**: "No route was found for the waypoints provided."|  
  
## Example

 The following example request specifies to use version one (`v1`) of the Bing Maps REST Services to find location information for the city of Seattle. The information will be returned in an XML format.  

```url
http://dev.virtualearth.net/REST/v1/Locations?q=seattle&output=xml&key=BingMapsKey  
```