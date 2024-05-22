---
title: "Output Parameters | Microsoft Docs"
description: "Describes output parameters and provides a table that outlines the alias, description, and values for various parameters with examples."
ms.date: "02/28/2018"
ms.topic: "reference"
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Output 

[!INCLUDE [bing-maps-enterprise-service-retirement](../../includes/bing-maps-enterprise-service-retirement.md)]

Use output parameters to specify the output of the request.  
  
 When an alias is provided, you can use the alias to shorten the length of the query parameter. For example, `output=xml` can be shortened to `o=xml`.  
  
|Parameter|Alias|Description|Values|  
|---------------|-----------|-----------------|------------|  
|`output`|`o`|**Optional**. The output format for the response.|One of the following values:<br /><br /> - `json` **[default]**<br />- `xml`<br /><br />Example: `output=xml`|  
|`suppressStatus`|`ss`|**Optional**. When set to `true` the HTTP Status returned is **200 OK** for all responses, including when there are errors. The content of the response always contains the actual HTTP Status.|- `true`<br />- `false` **[default]**<br /><br />Example: `suppressStatus=true`|  
|`jsonp`||**Optional.** Name of JSON callback function that is called when the response to the request is received. The JSON object provided in the response is passed to the callback function.|A string that contains the name of the callback function.<br /><br />Example: `jsonp=MyCallbackFunction`|  
|`jsonso`||**Optional.** The state object to pass to the JSON callback function. You can use a state object to match a response with a specific call. This value is provided as the second parameter to the callback function provided in the JSONP parameter.|Any valid JavaScript string.<br /><br />Example: `jsonso=abc3144sd`|  
  
## Examples
 
This example returns the template that you can use to build a map that shows roads. The output is requested in XML format.  
  
```url
http://dev.virtualearth.net/REST/v1/Imagery/Metadata/Road?output=xml&key={BingMapsKey}  
```
  
This example returns the following response. The URL template is provided by the ImageURL element.  
  
```xml
<Response xmlns:xsi="http://www.w3.org/2001/XMLSchema instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>Copyright © 2010 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>  
  <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>55da9336cd984609b45a91fc9fc26905</TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <ImageryMetadata>  
          <ImageUrl>http://ecn.{subdomain}.m3.tiles.live int.com/tiles/r{quadkey}.jpeg?g=58&mkt={culture}&shading=hill&stl=H</ImageUrl>  
          <ImageUrlSubdomains>  
            <string>t0</string>  
            <string>t1</string>  
            <string>t2</string>  
            <string>t3</string>  
          </ImageUrlSubdomains>  
          <ImageWidth>256</ImageWidth>  
          <ImageHeight>256</ImageHeight>  
          <ZoomMin>1</ZoomMin>  
          <ZoomMax>19</ZoomMax>  
        </ImageryMetadata>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
```  
  
This example gets a JSON object and specifies a callback function and a state parameter value.  
  
```url
http://dev.virtualearth.net/REST/v1/Imagery/Metadata/Road?output=json&jsonp=MyCallbackFunction&jsonso=abc3144sd&key={BingMapsKey}  
```
  
For this example, the body of the response contains the following function call.  
  
```javascript
MyCallbackFunction({"authenticationResultCode":"ValidCredentials",  
  "brandLogoUri":"http:\/\/dev.virtualearth.net\/Branding\/logo_powered_by.png",  
  "copyright":"Copyright © 2010 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
  "resourceSets":[{"estimatedTotal":1,"resources":[{"__type":"ImageryMetadata:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
  "imageHeight":256,  
  "imageUrl":"http:\/\/ecn.{subdomain}.tiles.virtualearth.net\/tiles\/r{quadkey}.jpeg?g=470&mkt={culture}&shading=hill&stl=H",  
  "imageUrlSubdomains":["t0","t1","t2","t3"],  
  "imageWidth":256,  
  "imageryProviders":null,  
  "vintageEnd":null,"vintageStart":null,  
  "zoomMax":19,"zoomMin":1}]}],  
  "statusCode":200,  
  "statusDescription":"OK",  
  "traceId":"d172cd085d624f2cab9b2c0a07ae06f1"},  
  "abc3144sd")  
```