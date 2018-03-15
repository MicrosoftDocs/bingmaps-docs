---
title: "Find a Location by Query | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 7918a94e-65c7-4526-82e5-7641f89518b1
caps.latest.revision: 64
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Find a Location by Query
Use the following URL templates to get latitude and longitude coordinates that correspond to location information provided as a query string. The strings `Space Needle` (a landmark) and `1 Microsoft Way Redmond WA` (an address) are examples of query strings with location information. These strings can be specified as a structured URL parameter or as a query parameter value. This URL template can be used to geocode information from any country. For more accurate results, use [User Context Parameters](../rest-services/user-context-parameters.md), such as the coordinates of a user’s current location.  
  
 When you make a request by using one of the following URL templates, the response returns one or more Location resources that contain location information associated with the URL parameter values. The location information for each resource includes latitude and longitude coordinates, the type of location, and the geographical area that contains the location. For more information about the Location resource, see [Location Data](../rest-services/location-data.md). You can also view the example URL and response values in the **Examples** section.  
  
## URL Template  
  
> [!Note]
> These templates support both HTTP and HTTPS protocols. To use this API, you must have a [Bing Maps key](../getting-started/getting-a-bing-maps-key.md). 
  
> [!TIP]
>  Be sure to review the [Bing Maps API Best Practices guide](../getting-started/bing-maps-api-best-practices.md) before using this service.  

 **Returns latitude and longitude coordinates for a location that is specified as query string.**  
  
  <!--
 **Structured URL**  
  
 A structured URL specifies the location data as part of the URL path.  
  
```  
http://dev.virtualearth.net/REST/v1/Locations/{locationQuery}?includeNeighborhood={includeNeighborhood}&maxResults={maxResults}&include={includeValue}&key={BingMapsKey}  
```  
 
 **Unstructured URL**  
 -->
 
 An URL appends the location data to the URL path. In the following template, the location data is specified by using a query parameter that is appended to the end of the URL path.  
  
```  
http://dev.virtualearth.net/REST/v1/Locations?query={locationQuery}&includeNeighborhood={includeNeighborhood}&include={includeValue}&maxResults={maxResults}&key={BingMapsKey}  
```  
  
### Template Parameters  
  
> [!NOTE]
>  See the [Common Parameters and Types](../rest-services/common-parameters-and-types.md) section for additional common parameters to use with these URLs.  
>   
>  Common parameters include:  
>   
>  -   [Output Parameters](../rest-services/output-parameters.md): Includes response output types and the JSON callback parameters.  
> -   [Culture Parameter](../rest-services/culture-parameter.md): Includes a list of the supported cultures.  
> -   [User Context Parameters](../rest-services/user-context-parameters.md): Includes parameters that set user location and viewport values to assist with determining locations. For example, you can prioritize the set of locations returned by a location query when you provide information about the user’s location.  
>   
>  When an alias is provided, you can use the alias to shorten the length of the query parameter. For example, query=1600 Pennsylvania Ave NW Washington, DC can be shortened to q=1600 Pennsylvania Ave NW Washington, DC.  
>   
>  Parameters are not case-sensitive.  
>   
>  For all location values, it is a best practice to encode the URI before making the request. Encoding replaces spaces with "%20" and replaces other special characters with similar encoded values. For more information, see [encodeURI](http://www.w3schools.com/jsref/jsref_encodeURI.asp) [JavaScript] and [Uri.EscapeDataString](http://msdn.microsoft.com/en-us/library/system.uri.aspx) [.NET].  
  
|Parameters|Alias|Description|Values|  
|----------------|-----------|-----------------|------------|  
|query|q|**Required.** Location information.|A string that contains information about a location, such as an address or landmark name.<br /><br /> **Structured URL examples**:<br /><br /> White%20House<br /><br /> 1600%20Pennsylvania%20Ave%20NW%20Washington,%20DC<br /><br /> **Unstructured URL examples**:<br /><br /> query=White%20House<br /><br /> q=1600%20Pennsylvania%20Ave%20NW%20Washington,%20DC|  
|includeNeighborhood|inclnb|**Optional.** Specifies to include the neighborhood with the address information the response when it is available.|One of the following values:<br /><br /> -   1: Include neighborhood information when available.<br />-   0 **[default]**: Do not include neighborhood information.<br /><br /> **Example:**<br /><br /> inclnb=1|  
|include|incl|**Optional.** Specifies to include additional information in the response.|One or more of the following options:<br /><br /> -   queryParse: Specifies that the response shows how the query string was parsed into address values, such as addressLine, locality, adminDistrict, and postalCode.<br />-   ciso2: Specifies to include the [two-letter ISO country code](http://www.iso.org/iso/country_codes.htm).<br /><br /> If you specify more than one include value, separate the values with a comma.<br /><br /> **Examples**:<br /><br /> incl=queryParse<br /><br /> incl=queryParse,ciso2|  
|maxResults|maxRes|**Optional.** Specifies the maximum number of locations to return in the response.|A string that contains an integer between 1 and 20. The default value is 5.<br /><br /> **Example:**<br /><br /> maxResults=10|  
  
## Response  
 One or more Location resources are returned in the response when you make a request by using these URL templates. For more information about the Location resource, see [Location Data](../rest-services/location-data.md). For more information about the common response syntax for the Bing Maps REST Services, see [Common Response Description](../rest-services/common-response-description.md). JSON and XML responses are provided for the URL examples in the following section.  
  
 These URLs support JSON (application/json) and XML (application/xml) response formats. A JSON response is provided by default unless you request XML output by setting the output (o) parameter. For more information, see [Output Parameters](../rest-services/output-parameters.md).  
  
## Examples  
 **Find location information for an address using a query string.**  
  
 The following examples request latitude and longitude information for an address specified by the query string `1 Microsoft way, Redmond WA 98052`. Both URLs return the same information. The results are requested in XML format.  
  
```  
http://dev.virtualearth.net/REST/v1/Locations/1%20Microsoft%20Way%20Redmond%20WA%2098052?o=xml&key=BingMapsKey  
```  
  
```  
http://dev.virtualearth.net/REST/v1/Locations?q=1%20Microsoft%20Way%20Redmond%20WA%2098052&o=xml&key=BingMapsKey  
```  
  
 **XML Response**  
  
 This example returns the following XML response.  
  
```  
<Response xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>  
    Copyright © 2014 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.  
  </Copyright>  
  <BrandLogoUri>  
    http://dev.virtualearth.net/Branding/logo_powered_by.png  
  </BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>  
    8bd85f8d93a142fe9bc409cd50b54120  
  </TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <Location>  
          <Name>Tower of London, United Kingdom</Name>  
          <Point>  
            <Latitude>51.509521484375</Latitude>  
            <Longitude>-0.0763700008392334</Longitude>  
          </Point>  
          <BoundingBox>  
            <SouthLatitude>51.507022857666016</SouthLatitude>  
            <WestLongitude>-0.078029103577137</WestLongitude>  
            <NorthLatitude>51.509269714355469</NorthLatitude>  
            <EastLongitude>-0.074420802295207977</EastLongitude>  
          </BoundingBox>  
          <EntityType>HistoricalSite</EntityType>  
          <Address>  
            <AdminDistrict>England</AdminDistrict>  
            <AdminDistrict2>London</AdminDistrict2>  
            <CountryRegion>United Kingdom</CountryRegion>  
            <FormattedAddress>Tower of London, United Kingdom</FormattedAddress>  
            <Locality>London</Locality>  
            <Neighborhood>EC3</Neighborhood>  
            <Landmark>Tower of London</Landmark>  
          </Address>  
          <Confidence>High</Confidence>  
          <MatchCode>Good</MatchCode>  
          <GeocodePoint>  
            <Latitude>51.509521484375</Latitude>  
            <Longitude>-0.0763700008392334</Longitude>  
            <CalculationMethod>Rooftop</CalculationMethod>  
            <UsageType>Display</UsageType>  
          </GeocodePoint>  
        </Location>  
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
   "copyright":"Copyright Â© 2014 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
   "resourceSets":[  
      {  
         "estimatedTotal":1,  
         "resources":[  
            {  
               "__type":"Location:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "bbox":[  
                  51.507022857666016,  
                  -0.078029103577137,  
                  51.509269714355469,  
                  -0.074420802295207977  
               ],  
               "name":"Tower of London, United Kingdom",  
               "point":{  
                  "type":"Point",  
                  "coordinates":[  
                     51.509521484375,  
                     -0.0763700008392334  
                  ]  
               },  
               "address":{  
                  "adminDistrict":"England",  
                  "adminDistrict2":"London",  
                  "countryRegion":"United Kingdom",  
                  "formattedAddress":"Tower of London, United Kingdom",  
                  "locality":"London",  
                  "neighborhood":"EC3",  
                  "landmark":"Tower of London"  
               },  
               "confidence":"High",  
               "entityType":"HistoricalSite",  
               "geocodePoints":[  
                  {  
                     "type":"Point",  
                     "coordinates":[  
                        51.509521484375,  
                        -0.0763700008392334  
                     ],  
                     "calculationMethod":"Rooftop",  
                     "usageTypes":[  
                        "Display"  
                     ]  
                  }  
               ],  
               "matchCodes":[  
                  "Good"  
               ]  
            }  
         ]  
      }  
   ],  
   "statusCode":200,  
   "statusDescription":"OK",  
   "traceId":"b0a6385e511b409aaeddd4be7c2ffaed"  
}  
```  
  
 **Find location information and request query parse information.**  
  
 The following URL performs the same query as the previous example, and also requests query parse information  
  
```  
http://dev.virtualearth.net/REST/v1/Locations/1%20Microsoft%20Way%20Redmond%20WA%2098052?include=queryParse&o=xml&key=BingMapsKey  
```  
  
 This query returns the same response as above with the additional query parse information.  
  
 **XML Query Parse Response**  
  
```  
<QueryParseValue Property="AddressLine" Value="1 Microsoft Way" />   
<QueryParseValue Property="Locality" Value="Redmond" />   
<QueryParseValue Property="PostalCode" Value="98052" />   
<QueryParseValue Property="AdminDistrict" Value="WA" />  
  
```  
  
 **JSON Query Parse Response**  
  
```  
"queryParseValues":[  
                     {  
                        "property":"AddressLine",  
                        "value":"1 Microsoft Way"  
                     },  
                     {  
                        "property":"Locality",  
                        "value":"Redmond"  
                     },  
                     {  
                        "property":"PostalCode",  
                        "value":"98052"  
                     },  
                     {  
                        "property":"AdminDistrict",  
                        "value":"WA"  
                     }  
                  ]  
  
```  
  
 **Find location information associated with a query string and relevant to the user’s location.**  
  
 The following example searches for locations associated with the search query "Kings Road". Because the userLocation parameter is specified, the results returned are relevant to the user’s location. For more information about the userLocation parameter and other user context parameters, see [User Context Parameters](../rest-services/user-context-parameters.md).  
  
```  
http://dev.virtualearth.net/REST/v1/Locations?culture=en-GB&query=Kings%20Road&o=xml&userLocation=51.504360719046616,-0.12600176611298197&o=xml&key=BingMapsKey  
```  
  
 **Find location information associated with a query string and request neighborhood information.**  
  
 The following example searches for locations associated with the search query "Brookyln New York". Because the includeNeighborhood (inclnb) parameter is set to 1, the Neighborhood field is returned in the response.  
  
```  
http://dev.virtualearth.net/REST/v1/Locations/tower%20of%20london?inclnb=1&o=xml&key=BingMapsKey  
```  
  
 **XML Response**  
  
```  
<Response xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>  
    Copyright © 2014 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.  
  </Copyright>  
  <BrandLogoUri>  
    http://dev.virtualearth.net/Branding/logo_powered_by.png  
  </BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>  
    8bd85f8d93a142fe9bc409cd50b54120  
  </TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <Location>  
          <Name>Tower of London, United Kingdom</Name>  
          <Point>  
            <Latitude>51.509521484375</Latitude>  
            <Longitude>-0.0763700008392334</Longitude>  
          </Point>  
          <BoundingBox>  
            <SouthLatitude>51.507022857666016</SouthLatitude>  
            <WestLongitude>-0.078029103577137</WestLongitude>  
            <NorthLatitude>51.509269714355469</NorthLatitude>  
            <EastLongitude>-0.074420802295207977</EastLongitude>  
          </BoundingBox>  
          <EntityType>HistoricalSite</EntityType>  
          <Address>  
            <AdminDistrict>England</AdminDistrict>  
            <AdminDistrict2>London</AdminDistrict2>  
            <CountryRegion>United Kingdom</CountryRegion>  
            <FormattedAddress>Tower of London, United Kingdom</FormattedAddress>  
            <Locality>London</Locality>  
            <Neighborhood>EC3</Neighborhood>  
            <Landmark>Tower of London</Landmark>  
          </Address>  
          <Confidence>High</Confidence>  
          <MatchCode>Good</MatchCode>  
          <GeocodePoint>  
            <Latitude>51.509521484375</Latitude>  
            <Longitude>-0.0763700008392334</Longitude>  
            <CalculationMethod>Rooftop</CalculationMethod>  
            <UsageType>Display</UsageType>  
          </GeocodePoint>  
        </Location>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response  
  
```  
  
 **JSON Response**  
  
 The following JSON response contains the same information as the XML response and is provided when the output (o) parameter is not set.  
  
```  
{  
   "authenticationResultCode":"ValidCredentials",  
   "brandLogoUri":"http:\/\/dev.virtualearth.net\/Branding\/logo_powered_by.png",  
   "copyright":"Copyright © 2014 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
   "resourceSets":[  
      {  
         "estimatedTotal":1,  
         "resources":[  
            {  
               "__type":"Location:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "bbox":[  
                  51.507022857666016,  
                  -0.078029103577137,  
                  51.509269714355469,  
                  -0.074420802295207977  
               ],  
               "name":"Tower of London, United Kingdom",  
               "point":{  
                  "type":"Point",  
                  "coordinates":[  
                     51.509521484375,  
                     -0.0763700008392334  
                  ]  
               },  
               "address":{  
                  "adminDistrict":"England",  
                  "adminDistrict2":"London",  
                  "countryRegion":"United Kingdom",  
                  "formattedAddress":"Tower of London, United Kingdom",  
                  "locality":"London",  
                  "neighborhood":"EC3",  
                  "landmark":"Tower of London"  
               },  
               "confidence":"High",  
               "entityType":"HistoricalSite",  
               "geocodePoints":[  
                  {  
                     "type":"Point",  
                     "coordinates":[  
                        51.509521484375,  
                        -0.0763700008392334  
                     ],  
                     "calculationMethod":"Rooftop",  
                     "usageTypes":[  
                        "Display"  
                     ]  
                  }  
               ],  
               "matchCodes":[  
                  "Good"  
               ]  
            }  
         ]  
      }  
   ],  
   "statusCode":200,  
   "statusDescription":"OK",  
   "traceId":"3c42ae05ba464bda8b915e765d3e86e9"  
}  
```  
  
 **Find location information for a landmark.**  
  
 The following example requests location information for the Eiffel Tower.  
  
```  
http://dev.virtualearth.net/REST/v1/Locations/Eiffel%20Tower?o=xml&key=BingMapsKey  
```  
  
 **XML Response**  
  
```  
<Response xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>  
    Copyright © 2011 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.  
  </Copyright>  
  <BrandLogoUri>  
    http://dev.virtualearth.net/Branding/logo_powered_by.png  
  </BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>  
    4095ee6d5c73457495db49dacf2abc56  
  </TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <Location>  
          <Name>Eiffel Tower, Paris, France</Name>  
          <Point>  
            <Latitude>48.857929229736328</Latitude>  
            <Longitude>2.295259952545166</Longitude>  
          </Point>  
          <BoundingBox>  
            <SouthLatitude>48.857460021972656</SouthLatitude>  
            <WestLongitude>2.2933001518249512</WestLongitude>  
            <NorthLatitude>48.859039306640625</NorthLatitude>  
            <EastLongitude>2.2956900596618652</EastLongitude>  
          </BoundingBox>  
          <EntityType>Monument</EntityType>  
          <Address>  
            <AdminDistrict>IdF</AdminDistrict>  
            <AdminDistrict2>Paris</AdminDistrict2>  
            <CountryRegion>France</CountryRegion>  
            <FormattedAddress>Eiffel Tower, Paris, France</FormattedAddress>  
            <Locality>Paris</Locality>  
            <Landmark>Eiffel Tower</Landmark>  
          </Address>  
          <Confidence>High</Confidence>  
          <MatchCode>Good</MatchCode>  
          <GeocodePoint>  
            <Latitude>48.857929229736328</Latitude>  
            <Longitude>2.295259952545166</Longitude>  
            <CalculationMethod>Rooftop</CalculationMethod>  
            <UsageType>Display</UsageType>  
          </GeocodePoint>  
        </Location>  
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
   "copyright":"Copyright © 2011 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
   "resourceSets":[  
      {  
         "estimatedTotal":1,  
         "resources":[  
            {  
               "__type":"Location:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "bbox":[  
                  48.857460021972656,  
                  2.2933001518249512,  
                  48.859039306640625,  
                  2.2956900596618652  
               ],  
               "name":"Eiffel Tower, Paris, France",  
               "point":{  
                  "type":"Point",  
                  "coordinates":[  
                     48.857929229736328,  
                     2.295259952545166  
                  ]  
               },  
               "address":{  
                  "adminDistrict":"IdF",  
                  "adminDistrict2":"Paris",  
                  "countryRegion":"France",  
                  "formattedAddress":"Eiffel Tower, Paris, France",  
                  "locality":"Paris",  
                  "landmark":"Eiffel Tower"  
               },  
               "confidence":"High",  
               "entityType":"Monument",  
               "geocodePoints":[  
                  {  
                     "type":"Point",  
                     "coordinates":[  
                        48.857929229736328,  
                        2.295259952545166  
                     ],  
                     "calculationMethod":"Rooftop",  
                     "usageTypes":[  
                        "Display"  
                     ]  
                  }  
               ],  
               "matchCodes":[  
                  "Good"  
               ]  
            }  
         ]  
      }  
   ],  
   "statusCode":200,  
   "statusDescription":"OK",  
   "traceId":"fb2339699bd24beab9766baf6382f926"  
}  
```  
  
 **Find location information and request up to 10 location results in the response.**  
  
 This example provides location information for the query string "New York" and requests up to 10 location results in the response. The default maximum number of locations returned is five (5) results.  
  
```  
http://dev.virtualearth.net/REST/v1/Locations?q=Greenville&maxResults=10&key=BingMapsKey  
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
 * [Using the REST Services with .NET](../rest-services/using-the-rest-services-with-net.md)   
 * [JSON Data Contracts](../rest-services/json-data-contracts.md)   