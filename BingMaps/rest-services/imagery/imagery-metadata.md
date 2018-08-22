---
title: "Imagery Metadata | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 8481908c-ac69-43ef-b737-a089b02972d3
caps.latest.revision: 28
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Imagery Metadata
The response returned by an Imagery Metadata URL request contains a resource that provides imagery metadata information. If the metadata requested is for Birdseye imagery, a Birdseye Metadata resource is returned. For other types of imagery, an Imagery Metadata resource is returned. This topic contains descriptions of the information elements in these resources, followed by JSON and XML examples.  
  
 For more information about the common response syntax for the Bing Maps REST Services, see [Common Response Description](../rest-services/common-response-description.md).  
  
## Common Imagery Resource Fields  
 The following fields are used in both the Imagery Metadata and the Birdseye Metadata resources.  
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|imageUrl|ImageUrl|URI|One of the following:<br /><br /> A URL template for an image tile if a specific point is specified.<br /><br /> A general URL template for the specified imagery set. **Note:**  For more information about the URI placeholder fields that may appear in the image tile, see **Understanding the Image URL Placeholders** section below.|  
|imageUrlSubdomains|ImageUrlSubdomains|string|One or more URL subdomains that may be used when constructing an image tile URL.|  
|imageWidth|ImageWidth|integer|The width of the image tile.|  
|imageHeight|ImageHeight|integer|The height of the image tile.|  
|vintageStart|VintageStart|DateTime|The earliest date found in an imagery set or for a specific imagery tile.|  
|vintageEnd|VintageEnd|DateTime|The latest date found in an imagery set or for a specific imagery tile.|  
|zoomMin|ZoomMin|integer|The minimum zoom level available for this imagery set.|  
|zoomMax|ZoomMax|integer|The maximum zoom level available for this imagery set.|  
  
## Birdseye Metadata Resource Fields  
 These fields are only used only by the Birdseye Metadata resource.  
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|orientation|Orientation|double|The orientation of the viewport for the imagery metadata in degrees where 0 = North [default], 90 = East, 180 = South, 270 = West.|  
|tilesX|TilesX|integer|The horizontal dimension of the imagery in number of tiles.|  
|tilesY|TilesY|integer|The vertical dimension of the imagery in number of tiles.|  
  
## Understanding the Image URL Placeholders  
 When you request imagery metadata, the image URL field returned in the response specifies a map tile. This map tile can contain one or more of the following placeholders.  
  
|URI placeholder|Description|  
|---------------------|-----------------|  
|{culture}|The culture of the map. The culture value determines the language that is used to display text. For a list of cultures that are supported by the Imagery API, see [Culture Parameter](../rest-services/culture-parameter.md).|  
|{quadkey}|The quadkey of the tile. For information about quadkeys, see [Bing Maps Tile System](http://msdn.microsoft.com/en-us/library/bb259689.aspx)|  
|{subdomain}|The sub-domain to use to retrieve tiles to allow maximum performance for network calls. The value values are t0, t1, t2, or t3.|  
|{tileId}|TileId is an index from 0 to (tilesX * tilesY) - 1 indicating a specific tile in the scene. 0 is top left corner and tiles are numbered in row order. So increasing values go left to right and then top to bottom.|  
|{zoom}|The zoom level of the map.|  
  
## Examples  
 The following examples show the resources returned by the Imagery Metadata API.  
  
### Imagery Metadata Resource Example  
 **JSON Example**  
  
```  
{  
  "imageHeight":256,  
  "imageUrl":"http:\/\/ecn.t2.tiles.virtualearth.net\/tiles\/a0212300322.jpeg?g=414&mkt={culture}",  
  "imageUrlSubdomains":null,  
  "imageWidth":256,  
  "vintageEnd":"01 Mar 2001 GMT",  
  "vintageStart":"01 Mar 2001 GMT",  
  "zoomMax":10,  
  "zoomMin":10  
}  
```  
  
 **XML Example**  
  
```  
<ImageryMetadata>  
  <ImageUrl>http://ecn.t2.tiles.virtualearth.net/tiles/a0212300322.jpeg?g=414&mkt={culture}</ImageUrl>  
  <ImageWidth>256</ImageWidth>  
  <ImageHeight>256</ImageHeight>  
  <ZoomMin>10</ZoomMin>  
  <ZoomMax>10</ZoomMax>  
  <VintageStart>2001-03-01</VintageStart>  
  <VintageEnd>2001-03-01</VintageEnd>  
</ImageryMetadata>  
```  
  
### Birdseye Imagery Resource Example  
 **XML Example**  
  
```  
<BirdseyeMetadata>  
  <ImageUrl>http://ecn.{subdomain}.tiles.virtualearth.net/tiles/o02301020333-37448-{zoom}-{tileId}.jpeg?g=461</ImageUrl>  
  <ImageUrlSubdomains>  
    <string>t0</string>  
    <string>t1</string>  
    <string>t2</string>  
    <string>t3</string>  
  </ImageUrlSubdomains>  
  <ImageWidth>256</ImageWidth>  
  <ImageHeight>256</ImageHeight>  
  <ZoomMin>19</ZoomMin>  
  <ZoomMax>20</ZoomMax>  
  <Orientation>0</Orientation>  
  <TilesX>16</TilesX>  
  <TilesY>12</TilesY>  
</BirdseyeMetadata>  
```  
  
 **JSON Example**  
  
```  
{  
   "authenticationResultCode":"ValidCredentials",  
   "brandLogoUri":"http:\/\/dev.virtualearth.net\/Branding\/logo_powered_by.png",  
   "copyright":"Copyright © 2010 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
   "resourceSets":[  
      {  
         "estimatedTotal":1,  
         "resources":[  
            {  
               "__type":"BirdseyeMetadata:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "imageHeight":256,  
               "imageUrl":"http:\/\/ecn.{subdomain}.tiles.virtualearth.net\/tiles\/o02301020333-37448-{zoom}-{tileId}.jpeg?g=461  
               "imageUrlSubdomains":[  
                  "t0",  
                  "t1",  
                  "t2",  
                  "t3"  
               ],  
               "imageWidth":256,  
               "imageryProviders":null,  
               "vintageEnd":null,  
               "vintageStart":null,  
               "zoomMax":20,  
               "zoomMin":19,  
               "orientation":0,  
               "tilesX":16,  
               "tilesY":12  
            }  
         ]  
      }  
   ],  
   "statusCode":200,  
   "statusDescription":"OK",  
   "traceId":"79cdbd530cdc4bbfaee4c8f8d780d1e3"  
}  
```