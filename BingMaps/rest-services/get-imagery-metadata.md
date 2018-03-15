---
title: "Get Imagery Metadata | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 8e9208d3-d54e-4321-9bbb-554c7fadcb08
caps.latest.revision: 96
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Get Imagery Metadata
Use the following URL templates to get metadata for imagery that is hosted by Bing™ Maps. The imagery metadata returned includes URLs and dimensions for imagery tiles, ranges of zoom levels, and imagery vintage information.  
  
 Uses of this metadata include the following:  
  
-   Determine the vintage of the imagery at a location.    
-   Determine the availability of imagery at a location at a specified zoom level.    
-   Determine the availability of different types of imagery at a location.    
-   Build custom maps by stitching together imagery tiles.  
  
## URL Templates  
  
> [!Note]
> These templates support both HTTP and HTTPS protocols. To use this API, you must have a [Bing Maps key](../getting-started/getting-a-bing-maps-key.md). 
  
There are two types of imagery metadata URLs:  
  
-   **Complete Metadata URLs**: Get imagery information that includes a map tile.    
-   **Basic Metadata URL**: Get imagery information that does not include a map tile.  
  
### Complete Metadata URLs  
 **Get the metadata for an imagery set.**  
  
> [!NOTE]
>  This template is not applicable for Birdseye imagery because Birdseye imagery requires a location.  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Metadata/{imagerySet}?key={BingMapsKey}  
```  
  
 **Get the metadata for an imagery set at a specific location.**  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Metadata/{imagerySet}/{centerPoint}?orientation={orientation}&zoomLevel={zoomLevel}&include={ImageryProviders}&key={BingMapsKey}  
```  
  
### Basic Metadata URL  
  
> [!NOTE]
>  This URL returns all imagery metadata except for the map tile URL.  
  
 **Get only the basic metadata for an imagery set at a specific location. This URL does not return a map tile URL.**  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/BasicMetadata/{imagerySet}/{centerPoint}?orientation={orientation}&zoomLevel={zoomLevel}&include={ImageryProviders}&key={BingMapsKey}  
```  
  
### Template Parameters  
  
> [!NOTE]
>  See the [Common Parameters and Types](../rest-services/common-parameters-and-types.md) section for additional common parameters to use with these URLs.  
>   
>  Common parameters include:  
>   
>  -   [Output Parameters](../rest-services/output-parameters.md): Includes response output types and the JSON callback parameters.  
> -   [Culture Parameter](../rest-services/culture-parameter.md): Includes a list of the supported cultures.  
>   
>  When an alias is provided, you can use the alias to shorten the length of the query parameter. For example, zoomLevel=10 can be shortened to zl=10.  
>   
>  Parameter values are not case-sensitive.  
  
|Parameters|Alias|Description|Values|  
|----------------|-----------|-----------------|------------|  
|imagerySet||**Required.** The type of imagery for which you are requesting metadata.|Aerial - Aerial imagery.<br /><br /> AerialWithLabels - Aerial imagery with a road overlay.<br /><br /> AerialWithLabelsOnDemand - Aerial imagery with on-demand road overlay.<br /><br /> Birdseye - Bird’s eye (oblique-angle) imagery.<br /><br /> BirdseyeWithLabels - Bird’s eye imagery with a road overlay.<br /><br /> BirdseyeV2 - The second generation Bird’s eye (oblique-angle) imagery.<br /><br /> BirdseyeV2WithLabels - The second generation Bird’s eye (oblique-angle) imagerywith a road overlay.<br /><br /> CanvasDark - A dark version of the road maps.<br /><br /> CanvasLight - A lighter version of the road maps which also has some of the details such as hill shading disabled.<br /><br /> CanvasGray - A grayscale version of the road maps.<br /><br /> Road - Roads without additional imagery. Uses the legacy static tile service.<br /><br /> RoadOnDemand - Roads without additional imagery. Uses the dynamic tile service.<br /><br /> OrdnanceSurvey - Ordnance Survey imagery. This imagery is visible only for the London area.<br /><br /> **Example**: imagerySet=Aerial|  
|centerPoint||**Required when imagerySet is Birdseye or BirdseyeWithLabels. Optional for other imagery sets.** The center point to use for the imagery metadata.|A point on the earth specified by latitude and longitude coordinates. For more information about point values, see [Location and Area Types](../rest-services/location-and-area-types.md).<br /><br /> **Example**: 47.610,-122.107|  
|include|incl|**Optional.** Specifies to provide additional information about the imagery as part of the response.|The only option for this parameter is ImageryProviders. When this parameter value is specified, information about the imagery providers is returned in the response.<br /><br /> **Example**: include=ImageryProviders|  
|orientation|dir|**Optional.** The orientation of the viewport to use for the imagery metadata. This option only applies to Birdseye imagery.|A double value between 0 to 360, where 0 = North [**default**], 90 = East, 180 = South, 270 = West.<br /><br /> **Example**: orientation=253.21|  
|uriScheme||**Optional.** Specifies the scheme that image URL in the response should use.|Two values can be specified; http (default), https.<br /><br /> **Example**: uriScheme=https|  
|zoomLevel|zl|**Required if a centerPoint is specified and imagerySet is set to Road, Aerial or AerialWithLabels** The level of zoom to use for the imagery metadata.|An integer between 1 and 21. **Note:**  Some imagery may not be available at all zoom levels for all locations. If imagery is not available at a location, a message is returned in the `ErrorDetails` collection of the response. For more information about this collection, see [Common Response Description](../rest-services/common-response-description.md). <br /><br /> **Example**: zoomLevel=10|  
  
## Response  
 When metadata for Birdseye or BirdseyeWithLabels imagery is requested, a BirdseyeMetadata resource is returned in the response. For other imagery types, an ImageryMetadata resource is returned. The ImageryMetadata resource may contain a map tile URL. For more information about the map tile URL and other metadata returned, see [Imagery Metadata](../rest-services/imagery-metadata.md). For more information about the common response syntax for the Bing Maps REST Services, see [Common Response Description](../rest-services/common-response-description.md). JSON and XML responses are provided for the URL examples in the following section.  
  
 These URLs support JSON (application/json) and XML (application/xml) response formats. A JSON response is provided by default unless you request XML output by setting the output (o) parameter. For more information, see [Output Parameters](../rest-services/output-parameters.md).  
  
## Examples  
 **Get Aerial imagery metadata at street level.**  
  
 This example returns metadata for aerial imagery metadata at street level in New York City. Note that a center point and a zoom level are both specified. If only one of these values were specified, this URL would return an error. The response is requested in XML format.  
  
```  
https://dev.virtualearth.net/REST/V1/Imagery/Metadata/Aerial/40.714550167322159,-74.007124900817871?zl=15&o=xml&key=BingMapsKey  
```  
  
 **BasicMetadata option:** If you requested basic metadata only instead of the complete metadata by using the corresponding basic metadata URL template, the `ImageUrl` field would not be included. The rest of the response is the same.  
  
 **XML Response**  
  
 This example returns the following XML response. For more information about the response fields including the image URL (map tile URL), see [Common Response Description](../rest-services/common-response-description.md) and [Imagery Metadata](../rest-services/imagery-metadata.md).  
  
```  
<Response xmlns:xsi="http://www.w3.org/2001/XMLSchema instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>Copyright © 2010 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>  
  <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>1a0d6dd60ea94171b8444a9e6e4555ca</TraceId>  
    <ResourceSets>  
      <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
        <Resources>  
          <ImageryMetadata>  
          <ImageUrl>http://ecn.t3.tiles.virtualearth.net/tiles/a032010110123333.jpeg?g=471&mkt={culture}}</ImageUrl>  
          <ImageWidth>256</ImageWidth>  
          <ImageHeight>256</ImageHeight>  
          <ZoomMin>15</ZoomMin>  
          <ZoomMax>15</ZoomMax>  
          <VintageStart>2006-09-01</VintageStart>  
          <VintageEnd>2006-12-31</VintageEnd>  
        </ImageryMetadata>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
```  
  
 **JSON Response**  
  
 The following JSON response contains the same information as the XML response and is provided when the output (o) parameter is not set.  
  
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
               "__type":"ImageryMetadata:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "imageHeight":256,  
               "imageUrl":"http:\/\/ecn.t3.tiles.virtualearth.net/tiles/a032010110123333.jpeg?g=471&mkt={culture}}",  
               "imageUrlSubdomains":null,  
               "imageWidth":256,  
               "imageryProviders":null,  
               "vintageEnd":"31 Jan 2006 GMT",  
               "vintageStart":"01 Jan 2006 GMT",  
               "zoomMax":15,  
               "zoomMin":15  
            }  
         ]  
      }  
   ],  
   "statusCode":200,  
   "statusDescription":"OK",  
   "traceId":"dfd1a6a2c33f414abf9f41d84ed02404"  
}  
```  
  
 **Get Road imagery metadata.**  
  
 This example gets metadata for road imagery. The response is requested in XML format.  
  
```  
https://dev.virtualearth.net/REST/V1/Imagery/Metadata/Road?output=xml&key=BingMapsKey  
```  
  
 **BasicMetadata option:** If you requested basic metadata only instead of the complete metadata by using the corresponding basic metadata URL template, the `ImageUrl` field would not be included. The rest of the response is the same.  
  
 **XML Response**  
  
 This example returns the following XML response. For more information about the response and resource fields including the image URL (map tile URL), see [Common Response Description](../rest-services/common-response-description.md) and [Imagery Metadata](../rest-services/imagery-metadata.md).  
  
```  
<Response xmlns:xsi="http://www.w3.org/2001/XMLSchema instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>Copyright © 2010 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>  
  <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>648b2fb028574e159a999015b3a83b87</TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <ImageryMetadata>  
          <ImageUrl>http://ecn.{subdomain}.tiles.virtualearth.net/tiles/r{quadkey}.jpeg?g=129&mkt={culture}&shading=hill&stl=H</ImageUrl>  
          <ImageUrlSubdomains>  
            <string>t0</string>  
            <string>t1</string>  
            <string>t2</string>  
            <string>t3</string>  
          </ImageUrlSubdomains>  
          <ImageWidth>256</ImageWidth>  
          <ImageHeight>256</ImageHeight>  
          <ZoomMin>1</ZoomMin>  
          <ZoomMax>21</ZoomMax>  
        </ImageryMetadata>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
```  
  
 **JSON Response**  
  
 The following JSON response contains the same information as the XML response and is provided when the output (o) parameter is not set.  
  
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
               "__type":"ImageryMetadata:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "imageHeight":256,  
               "imageUrl":"http:\/\/ecn.{subdomain}.tiles.virtualearth.net/tiles/r{quadkey}.jpeg?g=129&mkt={culture}&shading=hill&stl=H"  
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
               "zoomMax":19,  
               "zoomMin":1  
            }  
         ]  
      }  
   ],  
   "statusCode":200,  
   "statusDescription":"OK",  
   "traceId":"d709a168fde44fe496dcbfafd829185d"  
}  
```  
  
 **Get Birdseye imagery metadata.**  
  
 This example gets metadata for Birdseye imagery of San Francisco. The response is requested in XML format.  
  
```  
https://dev.virtualearth.net/REST/V1/Imagery/Metadata/Birdseye/37.779160067439079,-122.42004945874214?o=xml&key=BingMapsKey  
```  
  
 **BasicMetadata option:** If you requested basic metadata only instead of the complete metadata by using the corresponding basic metadata URL template, the `ImageUrl` field would not be included. The rest of the response is the same.  
  
 **XML Response**  
  
 This example returns the following XML response. For more information about the response fields including the image URL (map tile URL), see [Common Response Description](../rest-services/common-response-description.md) and [Imagery Metadata](../rest-services/imagery-metadata.md).  
  
```  
<Response xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
    <Copyright>Copyright © 2017 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>  
    <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
    <StatusCode>200</StatusCode>  
    <StatusDescription>OK</StatusDescription>  
    <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
    <TraceId>776700d9a33e4712b308697da7619c9f|CO30276302|7.7.0.0|</TraceId>  
    <ResourceSets>  
        <ResourceSet>  
            <EstimatedTotal>1</EstimatedTotal>  
            <Resources>  
                <BirdseyeMetadata>  
                    <ImageUrl>http://ak.{subdomain}.tiles.virtualearth.net/tiles/be000122033113001-9-14-{zoom}-{tileId}.jpeg?g=5777&key=BingMapsKey</ImageUrl>  
                    <ImageUrlSubdomains>  
                        <string>t0</string>  
                        <string>t1</string>  
                        <string>t2</string>  
                        <string>t3</string>  
                    </ImageUrlSubdomains>  
                    <ImageWidth>512</ImageWidth>  
                    <ImageHeight>512</ImageHeight>  
                    <ZoomMin>18</ZoomMin>  
                    <ZoomMax>21</ZoomMax>  
                    <VintageStart>2013-10-17</VintageStart>  
                    <VintageEnd>2013-10-17</VintageEnd>  
                    <Orientation>0</Orientation>  
                    <TilesX>9</TilesX>  
                    <TilesY>14</TilesY>  
                </BirdseyeMetadata>  
            </Resources>  
        </ResourceSet>  
    </ResourceSets>  
</Response>  
  
```  
  
 **JSON Response**  
  
 The following JSON response contains the same information as the XML response and is provided when the output (o) parameter is not set.  
  
```  
{  
    "authenticationResultCode": "ValidCredentials",  
    "brandLogoUri": "http:\/\/dev.virtualearth.net\/Branding\/logo_powered_by.png",  
    "copyright": "Copyright © 2017 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
    "resourceSets": [{  
        "estimatedTotal": 1,  
        "resources": [{  
            "__type": "BirdseyeMetadata:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
            "imageHeight": 512,  
            "imageUrl": "http:\/\/ak.{subdomain}.tiles.virtualearth.net\/tiles\/be000122033113001-9-14-{zoom}-{tileId}.jpeg?g=5777&key=BingMapsKey",  
            "imageUrlSubdomains": ["t0", "t1", "t2", "t3"],  
            "imageWidth": 512,  
            "imageryProviders": null,  
            "vintageEnd": "17 Oct 2013 GMT",  
            "vintageStart": "17 Oct 2013 GMT",  
            "zoomMax": 21,  
            "zoomMin": 18,  
            "orientation": 0,  
            "tilesX": 9,  
            "tilesY": 14  
        }]  
    }],  
    "statusCode": 200,  
    "statusDescription": "OK",  
    "traceId": "1ddf6f4da2f34ee480cf5c1958776a24|CO30275838|7.7.0.0|"  
}  
```  
  
 **Get Road imagery metadata and imagery provider information.**  
  
 This example returns road imagery metadata and requests information about the imagery providers. The response is returned in JSON format. You can specify to return the response in XML format by setting the output parameter to xml.  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Metadata/Road?incl=ImageryProviders&key=BingMapKey  
```  
  
 **Get Birdseye imagery metadata centered at a point.**  
  
 This example returns Birdseye imagery metadata for imagery that is centered at the specified point. The response is returned in JSON format. You can specify to return the response in XML format by setting the output parameter to xml.  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Metadata/Birdseye/47.23,-122.3?key=BingMapsKey  
```  
  
 **Get BirdseyeWithLabels imagery metadata centered at a point and from a viewport angle of 90 degrees.**  
  
 The example gets Birdseye imagery metadata for imagery that includes labels and that has an orientation angle of 90 degrees. The imagery is centered at the specified point. The response is returned in JSON format. You can specify to return the response in XML format by setting the output parameter to xml.  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Metadata/BirdseyeWithLabels/47.23,-122.3?dir=90&key=BingMapsKey  
```  
  
 **Get Road imagery metadata centered at a point and for a specified zoom level.**  
  
 This example returns road imagery metadata that is centered at the specified point with a zoom level of 10. . The response is returned in JSON format. You can specify to return the response in XML format by setting the output parameter to xml.  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Metadata/Road/47.23,-122.3?zl=10?key=BingMapsKey  
```  
  
 **Get Aerial imagery metadata centered at a point and for a specified zoom level.**  
  
 This example returns metadata for aerial imagery that is centered at the specified point with a zoom level of 10. The response is returned in JSON format. You can specify to return the response in XML format by setting the output parameter to xml.  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Metadata/Aerial/47.23,-122.3?zl=10&key=BingMapsKey  
```  
  
 **Get AerialWithLabels metadata centered at a point and for a specified zoom level.**  
  
 This example returns metadata for aerial imagery with labels and that is centered at the specified point with a zoom level of 10. The response is returned in JSON format. You can specify to return the response in XML format by setting the output parameter to xml.  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Metadata/AerialWithLabels/47.23,-122.3?zl=10&key=BingMapsKey  
```  
  
## HTTP Status Codes  
  
> [!NOTE]
>  For more details about these HTTP status codes, see [Status Codes and Error Handling](../rest-services/status-codes-and-error-handling.md).  
  
 When the request is successful, the following HTTP status code is returned.  
  
* 200

When the request is not successful, the response returns one of the following errors.

* 400
* 401
* 404
* 429
* 500
* 503
  
## See Also  
 [Bing Maps Tile System](http://msdn.microsoft.com/en-us/library/bb259689.aspx)   
 [Building Your Own Tile Server](http://msdn.microsoft.com/en-us/library/bb545006.aspx)   
 [Understanding Scale and Resolution](http://msdn.microsoft.com/en-us/library/aa940990.aspx)   
 [Using the REST Services with .NET](../rest-services/using-the-rest-services-with-net.md)   
 [JSON Data Contracts](../rest-services/json-data-contracts.md)