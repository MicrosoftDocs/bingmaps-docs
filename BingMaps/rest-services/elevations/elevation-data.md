---
title: "Elevation Data | Microsoft Docs"
ms.date: "02/28/2018"
ms.topic: "article"
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Elevation Data

The response returned by an Elevations URL can contain elevation or sea level offset resource data.  
  
 These resources are provided within a common response container. For a description, see [Common Response Description](common-response-description.md).  
  
## Elevation and Sea Level Offset Resource Data  
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|elevations|Elevations|array of integers|A list of elevation values in meters.|  
|offsets|Offsets|array of integers|The difference between sea level models for a set of locations.|  
|zoomLevel|ZoomLevel|integer|The zoom level used to compute the elevation values. Zoom level values are from 1 to 21. A lower value typically means less accurate results because the resolution of the elevation data is less. At lower resolutions, interpolated elevation values use data points that are further apart.<br /><br /> The zoom level used depends on the amount of elevation data available in a region and can be lowered when the specified path covers a long distance.|  
  
## Examples  

 **Elevations Resource**  
  
 **JSON Response**  
  
```json
{  
   "authenticationResultCode":"ValidCredentials",  
   "brandLogoUri":"http:\/\/dev.virtualearth.net\/Branding\/logo_powered_by.png",  
   "copyright":"Copyright © 2012 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
   "resourceSets":[  
      {  
         "estimatedTotal":1,  
         "resources":[  
            {  
               "__type":"ElevationData:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "elevations":[1776,1775,1777,1776],  
               "zoomLevel":14  
            }  
         ]  
      }  
   ],  
   "statusCode":200,  
   "statusDescription":"OK",  
   "traceId":"8d57dbeb0bb94e7ca67fd25b4114f5c3"  
}  
```  
  
 **XML Response**  
  
```xml 
<Response xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>  
    Copyright © 2012 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.  
  </Copyright>  
  <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>  
    3e6771dbe66045a18f72a787dc8c8deb  
  </TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <ElevationData>  
          <ZoomLevel>14</ZoomLevel>  
          <Elevations>  
            <int>1776</int>  
            <int>1775</int>  
            <int>1777</int>  
            <int>1776</int>  
          </Elevations>  
        </ElevationData>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
  
```  
  
 **Sea Level Offset Resource**  
  
 **JSON Response**  
  
```json
{  
   "authenticationResultCode":"ValidCredentials",  
   "brandLogoUri":"http:\/\/dev.virtualearth.net\/Branding\/logo_powered_by.png",  
   "copyright":"Copyright © 2012 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
   "resourceSets":[  
      {  
         "estimatedTotal":1,  
         "resources":[  
            {  
               "__type":"SeaLevelData:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "offsets":[-23, -23, -23, -23],  
               "zoomLevel":14  
            }  
         ]  
      }  
   ],  
   "statusCode":200,  
   "statusDescription":"OK",  
   "traceId":"ec8ceb0a09754aa3b9e981cb13a4282a"  
}  
```  
  
 **XML Response**  
  
```xml
<Response xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>  
    Copyright © 2012 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.  
  </Copyright>  
  <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>  
    e55037868ba34371a859462f7a0c59f3  
  </TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <SeaLevelData>  
          <ZoomLevel>14</ZoomLevel>  
          <Offsets>  
            <int>-23</int>  
            <int>-23</int>  
            <int>-23</int>  
            <int>-23</int>  
          </Offsets>  
        </SeaLevelData>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
  
```