---
title: "Geospatial Endpoint Service | Microsoft Docs"
description: "Describes the Geospatial Endpoint services and provides parameters, responses, supported services, and examples."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 81846570-94e7-43a1-943a-57191c132ecf
caps.latest.revision: 21
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Geospatial Endpoint Service

The Geospatial Endpoint Service is a REST service that provides information about Geospatial Platform services for the language and geographical region you specify. The service information includes available service endpoints and language support for these endpoints. Disputed geographical areas and embargoed countries or regions that do not have any service support are also identified.  
  
 This documentation does not explain how to use the service endpoints returned in the response.  
  
## Request URLs  
 Use the following URLs to make a Geospatial Endpoint Service request. Options are provided for requests with and without specific geographical coordinates.  
  
 **Get the service information for the language and region specified.**  
  
```url
http://dev.virtualearth.net/REST/V1/GeospatialEndpoint/language/userRegion?key={BingMapsKey}  
```  
  
 **Get the service information for the language, region and location coordinates specified.**  
  
 The latitude and longitude coordinates are reverse-geocoded to determine the location. If this location corresponds to a non-disputed country or region, then this location overrides the userRegion value in the request. However, if the coordinates are in a disputed country or region, then the userRegion in the request is used. For example, if the coordinates represent a disputed area along the border of India and China, and userRegion is set to IN (India) in the request and the language is set to hi-in (Hindi), then IN services for Hindi are returned. In the same example, if the userRegion is set to CN (China) and the language is set to zh-hans (Simplified Chinese), then CN services for Simplified Chinese are returned in the response.  
  
```url
http://dev.virtualearth.net/REST/V1/GeospatialEndpoint/language/userRegion/latitude,longitude?key={BingMapsKey}  
```  
  
## Parameters  
  
|Parameter|Alias|Description|Values|  
|---------------|-----------|-----------------|------------|  
|language||The preferred language.|An IETF language code, that includes the language and region code subtags, such as en-us or zh-hans.<br /><br /> **Example**: en-us<br /><br /> This code represents English as it is spoken in the United States.<br /><br /> **Example**: zh-hans<br /><br /> This code represents Simplified Chinese.|  
|userRegion||A country or region.|An ISO 3166-1 alpha-2 region code, such as US, IN, and CN.<br /><br /> **Example**: US<br /><br /> This code represents the United States.|  
|latitude, longitude||A location on the Earth.<br /><br /> These coordinates are reverse-geocoded to determine the country or region. If this location is in a disputed area, then the userRegion parameter value is used to determine the corresponding region.|The latitude and longitude of the user’s location in degrees.<br /><br /> **Example**: 33.977531,75.726013|  
|output|o|**Optional**. The output format for the response.|One of the following values:<br /><br /> -   json **[default]**<br />-   xml<br /><br /> **Example**: o=xml|  
|key||Your [Bing Maps Key](https://msdn.microsoft.com/library/ff428642).|The GUID value that represents a Bing Maps Key.|  
  
## Response

 The response returns the following information:  
  
- Whether this is a politically disputed area, such as an area claimed by more than one country.  
  
- Whether services are available in the user’s region.  
  
- A list of available geospatial services including endpoints and language support for each service.  
  
### Using the Endpoints with Parameters  

 It is important to note that the endpoints returned in the response are not typically URLs that you can execute. They give the base URL to which you can add parameters, such as a quad key for an image, route waypoints or an address to geocode. This documentation does not cover the parameters specific to each service.  
  
 For example, a common endpoint for geocoding is `dev.virtualearth.net\REST\v1\Locations`. However, this URL does not return any results without adding parameters. The following example shows how to geocode an address by providing address information and a Bing Maps Key.  
  
```url
http://dev.virtualearth.net/REST/v1/Locations?q=1%20Microsoft%20Way%20Redmond%20WA%2098052&o=xml&key=YourBingMapsKey  
```  
  
### Response Fields

 The following example shows the general structure for the JSON response. You can also request an XML response. Example requests and JSON and XML responses are provided in the [Examples](../articles/geospatial-endpoint-service.md#examples) section.  
  
```json
{  
   "authenticationResultCode":"ValidCredentials",  
   "brandLogoUri":"http:\/\/dev.virtualearth.net\/Branding\/logo_powered_by.png",  
   "copyright":"Copyright © 2013 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
   "resourceSets":[  
      {  
         "estimatedTotal":1,  
         "resources":[  
            {  
               "__type":"GeospatialEndpoint:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "isDisputedArea":false,  
               "isSupported":true,  
               "ur":"FR",  
               "services":[  
                  {  
                     "endpoint":"ecn.dynamic.t{0-3}.tiles.virtualearth.net\/comp\/ch\/{quadkey}?mkt={market}&it=G,VE,BX,L,LA&shading=hill&n=z&ur={userregion}",  
                     "fallbackLanguage":null,  
                     "languageSupported":true,  
                     "serviceName":"MapTiles"  
                  },  
                  {  
                     "endpoint":"dev.virtualearth.net\/REST\/v1\/Locations",  
                     "fallbackLanguage":null,  
                     "languageSupported":true,  
                     "serviceName":"Geocode"  
                  },  
                  {  
                     "endpoint":"dev.virtualearth.net\/REST\/v1\/Routes",  
                     "fallbackLanguage":null,  
                     "languageSupported":true,  
                     "serviceName":"Route"  
                  }  
               ]  
            }  
         ]  
      }  
   ],  
   "statusCode":200,  
   "statusDescription":null,  
   "traceId":"961e9c1e63e64bd4aa7d140ee4e05697"  
}  
```  
  
#### General Fields
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|isDisputedArea|IsDisputedArea|Boolean|Specifies if this area in the request is claimed by more than one country. For example, many areas along the border of India and China are disputed areas. Even though an area is disputed area, it may still be supported by Geospatial Platform services.|  
|isSupported|IsSupported|Boolean|Specifies if Geospatial Platform services are available in the country or region. Microsoft does not support services in embargoed areas. For example, if you request Geospatial Platform Service information for Cuba (CU), isSupported is set to true, and no service information is returned.|  
|ur (user region)|UR (user region)|string|The country or region that was used to determine service support. If you specified a latitude and longitude in the request that is in a non-disputed country or region, this country or region is returned in the response.<br /><br /> Please see the section [Region Localities](#region-localities) below for more details on the `User Region Codes` and `Culture Codes`.|  
|services|Services|array|Information for each geospatial service that is available in the country or region and language specified in the request.<br /><br /> See the **Service Fields** table for the information provided for each service.<br /><br /> For a list of available services, see [Supported Services](../articles/geospatial-endpoint-service.md#supportedServices).|  
  
#### Region Localities
  
 In order to get this label to appear, the user region of the map has to be set to one of following `User Region Codes`.  
  
|User Region Code|Official Short Form|Culture Code|  
|----------------------|-------------------------|------------------|  
|IL|Israel|He-il|  
|KR|Korea|Ko-kr|  
|PK|Pakistan|pa-pk|  
|IN|India|En-in|  
|CN|China|zh-cn|  
|AR|Argentina|es-AR|  
|BH|Bahrain|ar-BH|  
|EG|Egypt|ar-EG|  
|JO|Jordon|ar-JO|  
|SA|Saudi Arabia|ar-SA|  
|KW|Kuwait|ar-KW|  
|OM|Oman|ar-OM|  
|QA|Qatar|ar-QA|  
|MA|Morocco|ar-MA|  
|AE|UAE|ar-AE|  
  
#### Service Fields
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|endpoint|Endpoint|URL|The URL service endpoint to use in this region. Note that to use the service, you must typically add parameters specific to the service. These parameters are not described in this documentation.|  
|languageSupported|LanguageSupported|Boolean|Set to true if the service supports the language in the request for the region. If the language is supported, then the service endpoint will return responses using this language. If it is not supported, then the service will use the fallback language.|  
|fallbackLanguage|FallbackLanguage|string|Specifies the secondary or fallback language in this region or country. If the requested language is not supported and a fallback language is not available, United States English (en-us) is used.|  
|serviceName|ServiceName|string|An abbreviated name for the service. See [Supported Services](../articles/geospatial-endpoint-service.md#supportedServices) for a list of available services.|  
  
#### Response Container Fields
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|statusCode|StatusCode|integer|The HTTP Status code for the request.|  
|statusDescription|StatusDescription|string|A description of the HTTP status code.|  
|authenticationResultCode|AuthenticationResultCode|One of the following values:<br /><br /> ValidCredentials<br /><br /> InvalidCredentials<br /><br /> CredentialsExpired<br /><br /> NotAuthorized<br /><br /> NoCredentials<br /><br /> None|A status code that offers additional information about authentication success or failure.|  
|traceId|TraceId|string|A unique identifier for the request.|  
|copyright|Copyright|string|A copyright notice.|  
|brandLogoUri|BrandLogoUri|string|A URL that references a brand image to support contractual branding requirements.|  
|resourceSets|ResourceSets|collection|A collection of ResourceSet objects. A ResourceSet is a container of Resources returned by the request. For more information, see the ResourceSet section below.|  
|estimatedTotal|EstimatedTotal|long|An estimate of the total number of resources in the ResourceSet.|  
|resources|Resources|collection|A collection of one or more resources. The resources that are returned depend on the request. Information about resources is provided in the API reference for each Bing Maps REST Services API.|  
|errorDetails|ErrorDetails|string[]|A collection of error descriptions. For example, ErrorDetails can identify parameter values that are not valid or missing.|  
  
<a name="supportedServices"></a>   
## Supported Services  
 The following table describes the services that are supported by the Geospatial Endpoint Service. Information about one or more of these services may be returned in the response.  
  
|Service Type|Response Service Name|Description|  
|------------------|---------------------------|-----------------|  
|Map Imagery|MapTiles|Returns tiles from one of the following map tile services depending on the user region and language specified in the request.<br /><br /> -   On Demand Tile Service: Returns map tiles that are created on the server. This service endpoint will be provided when the user is in a geopolitically sensitive area, such as a disputed area or a country associated with such an area.<br />-   Pre-rendered Tile Service: Returns map tiles that have been pre-rendered during offline processing. This service endpoint will be provided when the user is not in a geopolitically sensitive area.|  
|Map Imagery|TrafficTiles|Returns map tiles that show traffic flow overlays.|  
|Map Imagery|StaticMapsB2B|Static Map API (Bing Maps REST Services): Returns static maps for the parameters that you specify. For parameter descriptions, see the [documentation](https://msdn.microsoft.com/library/ff701724).<br /><br /> **Note**: You must replace the *dev.virtualearth.net* endpoint in the documentation with the endpoint provided in the response.|  
|Map Metadata|MetadataB2B|Map Imagery Metadata API (Bing Maps REST Services): Returns map metadata for the parameters that you specify. For parameter descriptions, see the [documentation](https://msdn.microsoft.com/library/ff701712).<br /><br /> **Note**: You must use the endpoint provided in the response to replace the public dev.virtualearth.net endpoint in the documentation.|  
|Geocode|Geocode|Locations API (Bing Maps REST Services): Returns geocoded or reverse-geocoded location information for the parameters you specify. For parameter descriptions, see the [documentation](https://msdn.microsoft.com/library/ff701715).<br /><br /> **Note**: You must replace the *dev.virtualearth.net* endpoint in the documentation with the endpoint provided in the response.|  
|Route|Route|Routes API (Bing Maps REST Services): Returns route information for the parameters you specify. For parameter descriptions, see the [documentation](https://msdn.microsoft.com/library/ff701705).<br /><br /> **Note**: You must use the endpoint provided in the response to replace the public dev.virtualearth.net endpoint in the documentation.|  
|Image URL|BingLogo|Returns the attribution logo to display with Bing Maps tiles that do not include Nokia data.|  
|Image URL|CombinedLogo|Returns the attribution logo to display with Bing Maps tiles that include Nokia data.|  
  
<a name="examples"></a>

## Examples

### Typical Service support example
  
 Language: **fr-fr (French)**, userRegion: **FR (France)**  
  
```url
http://dev.virtualearth.net/REST/V1/GeospatialEndpoint/fr-fr/FR?key={BingMapsKey}  
```  
  
```json
{  
   "authenticationResultCode":"ValidCredentials",  
   "brandLogoUri":"http:\/\/dev.virtualearth.net\/Branding\/logo_powered_by.png",  
   "copyright":"Copyright © 2013 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
   "resourceSets":[  
      {  
         "estimatedTotal":1,  
         "resources":[  
            {  
               "__type":"GeospatialEndpointResponse:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "isDisputedArea":false,  
               "isSupported":true,  
               "services":[  
                  {  
                     "endpoint":"ecn.dynamic.t{0-3}.tiles.virtualearth.net\/comp\/ch\/{quadkey}?mkt={market}&it=G,VE,BX,L,LA&shading=hill&n=z&ur={userregion}",  
                     "fallbackLanguage":"fr",  
                     "languageSupported":false,  
                     "serviceName":"MapTiles"  
                  },  
                  {  
                     "endpoint":"ecn.t{0-7}.tiles.virtualearth.net\/tiles\/dp\/content?mkt={market}&p=tf&a={quadkey}&n=z",  
                     "fallbackLanguage":"fr",  
                     "languageSupported":false,  
                     "serviceName":"TrafficTiles"  
                  },  
                  {  
                     "endpoint":"dev.virtualearth.net\/REST\/V1\/Imagery\/Map",  
                     "fallbackLanguage":"fr",  
                     "languageSupported":false,  
                     "serviceName":"StaticMapsB2B"  
                  },  
                  {  
                     "endpoint":"dev.virtualearth.net\/REST\/V1\/Imagery\/Metadata",  
                     "fallbackLanguage":"fr",  
                     "languageSupported":false,  
                     "serviceName":"MetadataB2B"  
                  },  
                  {  
                     "endpoint":"dev.virtualearth.net\/REST\/v1\/Locations",  
                     "fallbackLanguage":"fr",  
                     "languageSupported":false,  
                     "serviceName":"Geocode"  
                  },  
                  {  
                     "endpoint":"dev.virtualearth.net\/REST\/v1\/Routes",  
                     "fallbackLanguage":"fr",  
                     "languageSupported":false,  
                     "serviceName":"Route"  
                  },  
                  {  
                     "endpoint":"ecn.dev.virtualearth.net\/Branding\/logo_powered_by.png",  
                     "fallbackLanguage":"fr",  
                     "languageSupported":false,  
                     "serviceName":"BingLogo"  
                  },  
                  {  
                     "endpoint":"ecn.dev.virtualearth.net\/Branding\/logo_powered_by.png",  
                     "fallbackLanguage":"fr",  
                     "languageSupported":false,  
                     "serviceName":"CombinedLogo"  
                  }  
               ],  
               "ur":"FR"  
            }  
         ]  
      }  
   ],  
   "statusCode":200,  
   "statusDescription":"OK",  
   "traceId":"4bcd1b7077e84c049cfbbcda3632c22a"  
}  
```  
  
You would receive the following JSON response if the output=xml parameter was set in this example.  
  
```xml
<?xml version="1.0" encoding="utf-8"?>  
<Response xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>Copyright © 2013 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>  
  <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>00e37177aa52425083eae9fc4874fceb</TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <Resource xsi:type="GeospatialEndpointResponse">  
          <UR>FR</UR>  
          <IsDisputedArea>false</IsDisputedArea>  
          <IsSupported>true</IsSupported>  
          <Services>  
            <ServiceInfo>  
              <ServiceName>MapTiles</ServiceName>  
              <Endpoint>ecn.dynamic.t{0-3}.tiles.virtualearth.net/comp/ch/{quadkey}?mkt={market}&amp;it=G,VE,BX,L,LA&amp;shading=hill&amp;n=z&amp;ur={userregion}</Endpoint>  
              <LanguageSupported>false</LanguageSupported>  
              <FallbackLanguageId>fr</FallbackLanguageId>  
            </ServiceInfo>  
            <ServiceInfo>  
              <ServiceName>TrafficTiles</ServiceName>  
              <Endpoint>ecn.t{0-7}.tiles.virtualearth.net/tiles/dp/content?mkt={market}&amp;p=tf&amp;a={quadkey}&amp;n=z</Endpoint>  
              <LanguageSupported>false</LanguageSupported>  
              <FallbackLanguageId>fr</FallbackLanguageId>  
            </ServiceInfo>  
            <ServiceInfo>  
              <ServiceName>StaticMapsB2B</ServiceName>  
              <Endpoint>dev.virtualearth.net/REST/V1/Imagery/Map</Endpoint>  
              <LanguageSupported>false</LanguageSupported>  
              <FallbackLanguageId>fr</FallbackLanguageId>  
            </ServiceInfo>  
            <ServiceInfo>  
              <ServiceName>MetadataB2B</ServiceName>  
              <Endpoint>dev.virtualearth.net/REST/V1/Imagery/Metadata</Endpoint>  
              <LanguageSupported>false</LanguageSupported>  
              <FallbackLanguageId>fr</FallbackLanguageId>  
            </ServiceInfo>  
            <ServiceInfo>  
              <ServiceName>Geocode</ServiceName>  
              <Endpoint>dev.virtualearth.net/REST/v1/Locations</Endpoint>  
              <LanguageSupported>false</LanguageSupported>  
              <FallbackLanguageId>fr</FallbackLanguageId>  
            </ServiceInfo>  
            <ServiceInfo>  
              <ServiceName>Route</ServiceName>  
              <Endpoint>dev.virtualearth.net/REST/v1/Routes</Endpoint>  
              <LanguageSupported>false</LanguageSupported>  
              <FallbackLanguageId>fr</FallbackLanguageId>  
            </ServiceInfo>  
            <ServiceInfo>  
              <ServiceName>BingLogo</ServiceName>  
              <Endpoint>ecn.dev.virtualearth.net/Branding/logo_powered_by.png</Endpoint>  
              <LanguageSupported>false</LanguageSupported>  
              <FallbackLanguageId>fr</FallbackLanguageId>  
            </ServiceInfo>  
            <ServiceInfo>  
              <ServiceName>CombinedLogo</ServiceName>  
              <Endpoint>ecn.dev.virtualearth.net/Branding/logo_powered_by.png</Endpoint>  
              <LanguageSupported>false</LanguageSupported>  
              <FallbackLanguageId>fr</FallbackLanguageId>  
            </ServiceInfo>  
          </Services>  
        </Resource>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
```  
  
### No Service support example
  
 Language: **en-us (English)**, userRegion: **CU (Cuba)**  
  
```url
http://dev.virtualearth.net/REST/V1/GeospatialEndpoint/en-us/cu?key={BingMapsKey}  
```  
  
```json
{  
   "authenticationResultCode":"ValidCredentials",  
   "brandLogoUri":"http:\/\/dev.virtualearth.net\/Branding\/logo_powered_by.png",  
   "copyright":"Copyright © 2013 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
   "resourceSets":[  
      {  
         "estimatedTotal":1,  
         "resources":[  
            {  
               "__type":"GeospatialEndpointResponse:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "isDisputedArea":false,  
               "isSupported":false,  
               "services":null,  
               "ur":"CU"  
            }  
         ]  
      }  
   ],  
   "statusCode":200,  
   "statusDescription":"OK",  
   "traceId":"eaaa2cd43ebb48a597baa601eb2437df  
}  
```  
  
 You would receive the following JSON response if the output=xml parameter was set in this example. Note that the **Services** array does not appear.  
  
```xml
<?xml version="1.0" encoding="utf-8"?>  
<Response xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>Copyright © 2013 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>  
  <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>2559b704c7e34392b95bfb99437060adTraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <Resource xsi:type="GeospatialEndpointResponse">  
          <UR>CU</UR>  
          <IsDisputedArea>false</IsDisputedArea>  
          <IsSupported>false</IsSupported>  
        </Resource>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
```  
  
### Disputed area example
  
 Language: **zh-hans (Simplified Chinese)**, userRegion: **CN (China)**, Coordinates: **Disputed Area between India and China**  
  
> [!NOTE]
> The response shows `CN` as the region because the latitude and longitude are in a disputed area.  
  
```url
http://dev.virtualearth.net/REST/V1/GeospatialEndpoint/zh-hans/cn/32.750323,79.376221?key={BingMapsKey}  
```  
  
```json
{  
   "authenticationResultCode":"ValidCredentials",  
   "brandLogoUri":"http:\/\/dev.virtualearth.net\/Branding\/logo_powered_by.png",  
   "copyright":"Copyright © 2013 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
   "resourceSets":[  
      {  
         "estimatedTotal":1,  
         "resources":[  
            {  
               "__type":"GeospatialEndpointResponse:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "isDisputedArea":true,  
               "isSupported":true,  
               "services":[  
                  {  
                     "endpoint":"r{0-3}.tiles.ditu.live.com\/tiles\/r{quadkey}.png?g={generation}",  
                     "fallbackLanguage":null,  
                     "languageSupported":true,  
                     "serviceName":"RoadWithLabels"  
                  },  
                  {  
                     "endpoint":"r{0-3}.tiles.ditu.live.com\/tiles\/r{quadkey}.png?g={generation}",  
                     "fallbackLanguage":null,  
                     "languageSupported":true,  
                     "serviceName":"MapTiles"  
                  },  
                  {  
                     "endpoint":"traftile.mapabc.com\/trafficengine\/traffictile?Key={quadkey}",  
                     "fallbackLanguage":null,  
                     "languageSupported":true,  
                     "serviceName":"TrafficTiles"  
                  },  
                  {  
                     "endpoint":"dev.ditu.live.com\/REST\/V1\/Imagery\/Map",  
                     "fallbackLanguage":null,  
                     "languageSupported":true,  
                     "serviceName":"StaticMapsB2B"  
                  },  
                  {  
                     "endpoint":"dev.ditu.live.com\/REST\/V1\/Locations",  
                     "fallbackLanguage":null,  
                     "languageSupported":true,  
                     "serviceName":"Geocode"  
                  },  
                  {  
                     "endpoint":"dev.ditu.live.com\/REST\/V1\/Routes",  
                     "fallbackLanguage":null,  
                     "languageSupported":true,  
                     "serviceName":"Route"  
                  }  
               ],  
               "ur":"CN"  
            }  
         ]  
      }  
   ],  
   "statusCode":200,  
   "statusDescription":"OK",  
   "traceId":"711c2b03cb1744f2849eddfd7a7650a3"  
}  
```  
  
You would receive the following JSON response if the output=xml parameter was set in this example.  
  
```xml
<?xml version="1.0" encoding="utf-8"?>  
<Response xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>Copyright © 2013 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>  
  <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>94994c4c84da4c40a32e55c0c2a76b06</TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <Resource xsi:type="GeospatialEndpointResponse">  
          <UR>CN</UR>  
          <IsDisputedArea>true</IsDisputedArea>  
          <IsSupported>true</IsSupported>  
          <Services>  
            <ServiceInfo>  
              <ServiceName>RoadWithLabels</ServiceName>  
              <Endpoint>r{0-3}.tiles.ditu.live.com/tiles/r{quadkey}.png?g={generation}</Endpoint>  
              <LanguageSupported>true</LanguageSupported>  
            </ServiceInfo>  
            <ServiceInfo>  
              <ServiceName>MapTiles</ServiceName>  
              <Endpoint>r{0-3}.tiles.ditu.live.com/tiles/r{quadkey}.png?g={generation}</Endpoint>  
              <LanguageSupported>true</LanguageSupported>  
            </ServiceInfo>  
            <ServiceInfo>  
              <ServiceName>TrafficTiles</ServiceName>  
              <Endpoint>traftile.mapabc.com/trafficengine/traffictile?Key={quadkey}</Endpoint>  
              <LanguageSupported>true</LanguageSupported>  
            </ServiceInfo>  
            <ServiceInfo>  
              <ServiceName>StaticMapsB2B</ServiceName>  
              <Endpoint>dev.ditu.live.com/REST/V1/Imagery/Map</Endpoint>  
              <LanguageSupported>true</LanguageSupported>  
            </ServiceInfo>  
            <ServiceInfo>  
              <ServiceName>Geocode</ServiceName>  
              <Endpoint>dev.ditu.live.com/REST/V1/Locations</Endpoint>  
              <LanguageSupported>true</LanguageSupported>  
            </ServiceInfo>  
            <ServiceInfo>  
              <ServiceName>Route</ServiceName>  
              <Endpoint>dev.ditu.live.com/REST/V1/Routes</Endpoint>  
              <LanguageSupported>true</LanguageSupported>  
            </ServiceInfo>  
          </Services>  
        </Resource>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
```  
  
Language: **hi-in (Hindi)**, userRegion: **IN (India)**, Coordinates: **Disputed Area between India and China**  
  
> [!NOTE]
> The response shows `IN` as the region because the latitude and longitude coordinates are in a disputed area.  
  
```url
http://dev.virtualearth.net/REST/V1/GeospatialEndpoint/hi-in/in/32.750323,79.376221?key={BingMapsKey}  
```  
  
```json
{  
   "authenticationResultCode":"ValidCredentials",  
   "brandLogoUri":"http:\/\/dev.virtualearth.net\/Branding\/logo_powered_by.png",  
   "copyright":"Copyright © 2013 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
   "resourceSets":[  
      {  
         "estimatedTotal":1,  
         "resources":[  
            {  
               "__type":"GeospatialEndpointResponse:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "isDisputedArea":true,  
               "isSupported":true,  
               "services":[  
                  {  
                     "endpoint":"ecn.dynamic.t{0-3}.tiles.virtualearth.net\/comp\/ch\/{quadkey}?mkt=en-us&it=G,L&shading=hil&n=z",  
                     "fallbackLanguage":"en-US",  
                     "languageSupported":false,  
                     "serviceName":"RoadWithLabels"  
                  },  
                  {  
                     "endpoint":"ecn.dynamic.t{0-3}.tiles.virtualearth.net\/comp\/ch\/{quadkey}?mkt=en-us&it=A,G,L&n=z",  
                     "fallbackLanguage":"en-US",  
                     "languageSupported":false,  
                     "serviceName":"AerialWithLabels"  
                  },  
                  {  
                     "endpoint":"ecn.dynamic.t{0-3}.tiles.virtualearth.net\/comp\/ch\/{quadkey}?mkt=en-us&it=G&shading=hill&n=z",  
                     "fallbackLanguage":"en-US",  
                     "languageSupported":false,  
                     "serviceName":"RoadWithoutLabels"  
                  },  
                  {  
                     "endpoint":"ecn.dynamic.t{0-3}.tiles.virtualearth.net\/comp\/ch\/{quadkey}?mkt=en-us&it=A,G&n=z",  
                     "fallbackLanguage":"en-US",  
                     "languageSupported":false,  
                     "serviceName":"AerialWithoutLabels"  
                  },  
                  {  
                     "endpoint":"ecn.dynamic.t{0-3}.tiles.virtualearth.net\/comp\/ch\/{quadkey}?mkt={market}&it=G,VE,BX,L,LA&shading=hill&n=z&ur={userregion}",  
                     "fallbackLanguage":"en-US",  
                     "languageSupported":false,  
                     "serviceName":"MapTiles"  
                  },  
                  {  
                     "endpoint":"ecn.t{0-7}.tiles.virtualearth.net\/tiles\/dp\/content?mkt={market}&p=tf&a={quadkey}&n=z",  
                     "fallbackLanguage":"en-US",  
                     "languageSupported":false,  
                     "serviceName":"TrafficTiles"  
                  },  
                  {  
                     "endpoint":"dev.virtualearth.net\/REST\/V1\/Imagery\/Map",  
                     "fallbackLanguage":"en-US",  
                     "languageSupported":false,  
                     "serviceName":"StaticMapsB2B"  
                  },  
                  {  
                     "endpoint":"dev.virtualearth.net\/REST\/V1\/Imagery\/Metadata",  
                     "fallbackLanguage":"en-US",  
                     "languageSupported":false,  
                     "serviceName":"MetadataB2B"  
                  },  
                  {  
                     "endpoint":"dev.virtualearth.net\/REST\/v1\/Locations",  
                     "fallbackLanguage":"en-US",  
                     "languageSupported":false,  
                     "serviceName":"Geocode"  
                  },  
                  {  
                     "endpoint":"dev.virtualearth.net\/REST\/v1\/Routes",  
                     "fallbackLanguage":"en-US",  
                     "languageSupported":false,  
                     "serviceName":"Route"  
                  }  
               ],  
               "ur":"IN"  
            }  
         ]  
      }  
   ],  
   "statusCode":200,  
   "statusDescription":"OK",  
   "traceId":"c3d472f7ba6b4c8bbcb4a41c1ce82e8b  
}  
```  
  
You would receive the following JSON response if the output=xml parameter was set in this example.  
  
```xml
<?xml version="1.0" encoding="utf-8"?>  
<Response xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>Copyright © 2013 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>  
  <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>105c3b6e5e6a4577a4bb405b72a2b413|CPKM001262|02.00.117.100|</TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <Resource xsi:type="GeospatialEndpointResponse">  
          <UR>IN</UR>  
          <IsDisputedArea>true</IsDisputedArea>  
          <IsSupported>true</IsSupported>  
          <Services>  
            <ServiceInfo>  
              <ServiceName>RoadWithLabels</ServiceName>  
              <Endpoint>ecn.dynamic.t{0-3}.tiles.virtualearth.net/comp/ch/{quadkey}?mkt=en-us&amp;it=G,L&amp;shading=hil&amp;n=z</Endpoint>  
              <LanguageSupported>false</LanguageSupported>  
              <FallbackLanguageId>en-US</FallbackLanguageId>  
            </ServiceInfo>  
            <ServiceInfo>  
              <ServiceName>AerialWithLabels</ServiceName>  
              <Endpoint>ecn.dynamic.t{0-3}.tiles.virtualearth.net/comp/ch/{quadkey}?mkt=en-us&amp;it=A,G,L&amp;n=z</Endpoint>  
              <LanguageSupported>false</LanguageSupported>  
              <FallbackLanguageId>en-US</FallbackLanguageId>  
            </ServiceInfo>  
            <ServiceInfo>  
              <ServiceName>RoadWithoutLabels</ServiceName>  
              <Endpoint>ecn.dynamic.t{0-3}.tiles.virtualearth.net/comp/ch/{quadkey}?mkt=en-us&amp;it=G&amp;shading=hill&amp;n=z</Endpoint>  
              <LanguageSupported>false</LanguageSupported>  
              <FallbackLanguageId>en-US</FallbackLanguageId>  
            </ServiceInfo>  
            <ServiceInfo>  
              <ServiceName>AerialWithoutLabels</ServiceName>  
              <Endpoint>ecn.dynamic.t{0-3}.tiles.virtualearth.net/comp/ch/{quadkey}?mkt=en-us&amp;it=A,G&amp;n=z</Endpoint>  
              <LanguageSupported>false</LanguageSupported>  
              <FallbackLanguageId>en-US</FallbackLanguageId>  
            </ServiceInfo>  
            <ServiceInfo>  
              <ServiceName>MapTiles</ServiceName>  
              <Endpoint>ecn.dynamic.t{0-3}.tiles.virtualearth.net/comp/ch/{quadkey}?mkt={market}&amp;it=G,VE,BX,L,LA&amp;shading=hill&amp;n=z&amp;ur={userregion}</Endpoint>  
              <LanguageSupported>false</LanguageSupported>  
              <FallbackLanguageId>en-US</FallbackLanguageId>  
            </ServiceInfo>  
            <ServiceInfo>  
              <ServiceName>TrafficTiles</ServiceName>  
              <Endpoint>ecn.t{0-7}.tiles.virtualearth.net/tiles/dp/content?mkt={market}&amp;p=tf&amp;a={quadkey}&amp;n=z</Endpoint>  
              <LanguageSupported>false</LanguageSupported>  
              <FallbackLanguageId>en-US</FallbackLanguageId>  
            </ServiceInfo>  
            <ServiceInfo>  
              <ServiceName>StaticMapsB2B</ServiceName>  
              <Endpoint>dev.virtualearth.net/REST/V1/Imagery/Map</Endpoint>  
              <LanguageSupported>false</LanguageSupported>  
              <FallbackLanguageId>en-US</FallbackLanguageId>  
            </ServiceInfo>  
            <ServiceInfo>  
              <ServiceName>MetadataB2B</ServiceName>  
              <Endpoint>dev.virtualearth.net/REST/V1/Imagery/Metadata</Endpoint>  
              <LanguageSupported>false</LanguageSupported>  
              <FallbackLanguageId>en-US</FallbackLanguageId>  
            </ServiceInfo>  
            <ServiceInfo>  
              <ServiceName>Geocode</ServiceName>  
              <Endpoint>dev.virtualearth.net/REST/v1/Locations</Endpoint>  
              <LanguageSupported>false</LanguageSupported>  
              <FallbackLanguageId>en-US</FallbackLanguageId>  
            </ServiceInfo>  
            <ServiceInfo>  
              <ServiceName>Route</ServiceName>  
              <Endpoint>dev.virtualearth.net/REST/v1/Routes</Endpoint>  
              <LanguageSupported>false</LanguageSupported>  
              <FallbackLanguageId>en-US</FallbackLanguageId>  
            </ServiceInfo>  
          </Services>  
        </Resource>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
```
