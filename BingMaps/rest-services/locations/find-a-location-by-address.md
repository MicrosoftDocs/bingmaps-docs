---
title: "Find a Location by Address | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 8c01604f-8861-4c96-9013-75848b354837
caps.latest.revision: 100
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Find a Location by Address

Use the following URL templates to get latitude and longitude coordinates for a location by specifying values such as a locality, postal code, and street address.  
  
When you make a request by using one of the following URL templates, the response returns one or more Location resources that contain location information associated with the URL parameter values. The location information for each resource includes latitude and longitude coordinates, the type of location, and the geographical area that contains the location. For more information about the Location resource, see [Location Data](location-data.md). You can also view the example URL and response values in the Examples section.  
  
## URL Templates  
  
[!INCLUDE [get-bing-map-key-note](../../includes/get-bing-map-key-note.md)]
  
[!INCLUDE [get-bing-maps-best-practices-note](../../includes/get-bing-maps-best-practices-note.md)]
    
**Unstructured URL: Get the latitude and longitude coordinates based on a set of address values for any country**  
  
 You can get information for a location in any country by setting one or more of the parameters in the following URL.  
  
 An unstructured URL appends the location data to the URL path. In the URL below, address information is specified by using URL address parameters such as addressLine, adminDistrict. and postalCode. These parameters are appended to the URL path.  
  
```url
http://dev.virtualearth.net/REST/v1/Locations?countryRegion={countryRegion}&adminDistrict={adminDistrict}&locality={locality}&postalCode={postalCode}&addressLine={addressLine}&userLocation={userLocation}&userIp={userIp}&usermapView={usermapView}&includeNeighborhood={includeNeighborhood}&maxResults={maxResults}&key={BingMapsKey}  
```  

<!--  
 **Structured URLs: Get the latitude and longitude coordinates based on a set of address values for specific countries**  
  
> [!NOTE]
>  You can substitute a hyphen (-) for any structured URL parameter when there is no value.  
>   
>  For countries that do not have a structured URL template, use the Unstructured URL described below or use the [Find a Location by Query](../services/find-a-location-by-query.md) API which takes location well as encode other special characters information as a single query string.  
>   
>  For all location values, it is a best practice to encode the URI before making the request. Encoding replaces spaces with "%20" and replaces other special characters with similar encoded values. For more information, see [encodeURI](http://www.w3schools.com/jsref/jsref_encodeURI.asp) [JavaScript] and [Uri.EscapeDataString](http://msdn.microsoft.com/en-us/library/system.uri.aspx) [.NET].  
  
 A structured URL specifies the location data for the country as part of the URL path.  
  
 **Canada**  
  
```  
http://dev.virtualearth.net/REST/v1/Locations/CA/adminDistrict/postalCode/locality/addressLine?includeNeighborhood=includeNeighborhood&include=includeValue&maxResults=maxResults&key=BingMapsKey  
```  
  
 **France**  
  
```  
http://dev.virtualearth.net/REST/v1/Locations/FR/postalCode/locality/addressLine?includeNeighborhood=includeNeighborhood&include=includeValue&maxResults=maxResults&key=BingMapsKey  
```  
  
 **Germany**  
  
```  
http://dev.virtualearth.net/REST/v1/Locations/DE/postalCode/locality/addressLine?includeNeighborhood=includeNeighborhood&include=includeValue&maxResults=maxResults&key=BingMapsKey  
```  
  
 **United Kingdom**  
  
```  
http://dev.virtualearth.net/REST/v1/Locations/UK/postalCode?includeNeighborhood=includeNeighborhood&include=includeValue&maxResults=maxResults&key=BingMapsKey  
```  
  
 **United States**  
  
```  
http://dev.virtualearth.net/REST/v1/Locations/US/adminDistrict/postalCode/locality/addressLine?includeNeighborhood=includeNeighborhood&include=includeValue&maxResults=maxResults&key=BingMapsKey  
```  
  
```  
http://dev.virtualearth.net/REST/v1/Locations/US/adminDistrict/locality/addressLine?includeNeighborhood=includeNeighborhood&include=includeValue&maxResults=maxResults&key=BingMapsKey  
```  
-->

> [!IMPORTANT]
>  **About Special Characters**  
>   
>  When you specify location information using one of the structured URLs, do not use values that contain special characters such as a period (.), a comma (,), a colon (:) or a plus sign (+). A hyphen is acceptable as a placeholder, but should not be used as part of a parameter value in a structured URL. If the location information contains any special characters, use the Unstructured URL template or the [Find a Location by Query](find-a-location-by-query.md) API.  
>   
>  For example, if you want to get latitude and longitude values for the address "100 Main St. Somewhere, WA 98001" that contains a period (.), use one of the following query formats.  
>   
>  **Unstructured query:** `http://dev.virtualearth.net/REST/v1/Locations?CountryRegion=US&adminDistrict=WA&locality=Somewhere&postalCode=98001&addressLine=100%20Main%20St.&key=BingMapsKey`  
>   
>  **[Find a Location by Query](../services/find-a-location-by-query.md) query**: `http://dev.virtualearth.net/REST/v1/Locations?q=100%20Main%20St.%20Somewhere,%20WA%2098001&key=BingMapsKey`  

  
### Template Parameters  
  
> [!NOTE]
>  See the [Common Parameters and Types](../common-parameters-and-types/index.md) section for additional common parameters to use with these URLs.  
>   
>  Common parameters include:  
>   
>  -   [Output Parameters](../common-parameters-and-types/output-parameters.md): Includes response output types and the JSON callback parameters.  
> -   [Culture Parameter](../common-parameters-and-types/culture-parameter.md): Includes a list of the supported cultures.  
> -   [User Context Parameters](../common-parameters-and-types/user-context-parameters.md): Includes parameters that set user location and viewport values to help with determining locations. For example, you can specify the user’s location to prioritize the set of locations returned when you query with incomplete address information.  
>   
>  Parameter values are not case-sensitive.  
  
|Parameters|Alias|Description|Values|  
|----------------|-----------|-----------------|------------|  
|adminDistrict||**Optional for unstructured URL.** The subdivision name in the country or region for an address. This element is typically treated as the first order administrative subdivision, but in some cases it is the second, third, or fourth order subdivision in a country, dependency, or region.|A string that contains a subdivision, such as the abbreviation of a US state.<br /><br /> **Example**: WA|  
|locality||**Optional for unstructured URL.** The locality, such as the city or neighborhood, that corresponds to an address.|A string that contains the locality, such as a US city.<br /><br /> **Example**: Seattle|  
|postalCode||**Optional for unstructured URL.** The post code, postal code, or ZIP Code of an address.|A string that contains the postal code, such as a US ZIP Code.<br /><br /> **Example**: 98178|  
|addressLine||**Optional for unstructured URL.** The official street line of an address relative to the area, as specified by the Locality, or PostalCode, properties. Typical use of this element would be to provide a street address or any official address.|A string specifying the street line of an address.<br /><br /> **Example**: 1 Microsoft Way|  
|countryRegion||**Optional for unstructured URL.** The [ISO country code](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) for the country.|A string specifying the ISO country code.<br /><br /> **Example**: AU|  
|includeNeighborhood|inclnb|**Optional.** Specifies to include the neighborhood in the response when it is available. **Note:**  When you create your URL request, you can set the Locality parameter to a neighborhood. In this case, the neighborhood you provide may be returned in the neighborhood field of the response and a greater locality may be returned in the locality field. For example, you can create a request that specifies to include neighborhood information (inclnb=1) and that sets the Locality to Ballard and the AdminDistrict to WA (Washington State). In this case, the neighborhood field in the response is set to Ballard and the locality field is set to Seattle. You can find this example in the **Examples** section.|One of the following values:<br /><br /> -   1: Include neighborhood information when available.<br />-   0 **[default]**: Do not include neighborhood information.<br />     **Example:**<br />     inclnb=1|  
|include|incl|**Optional.** Specifies additional values to include.|The only value for this parameter is ciso2. When you specify include=ciso2, the [two-letter ISO country code](http://www.iso.org/iso/country_codes.htm) is included for addresses in the response.<br /><br /> **Example:**<br /><br /> incl=ciso2|  
|maxResults|maxRes|**Optional.** Specifies the maximum number of locations to return in the response.|A string that contains an integer between 1 and 20. The default value is 5.<br /><br /> **Example:**<br /><br /> maxResults=10|  
  
## Response  
 One or more Location resources are returned in the response when you make a request by using these URL templates. For more information about the Location resource, see [Location Data](location-data.md). For more information about the common response syntax for the Bing Maps REST Services, see [Common Response Description](../common-parameters-and-types/common-response-description.md). Responses are provided for some URL examples in the following section.  
  
 These URLs support JSON (`application/json`) and XML (`application/xml`) response formats. A JSON response is provided by default unless you request XML output by setting the output (`o`) parameter. For more information, see [Output Parameters](../common-parameters-and-types/output-parameters.md).  
  
## Examples  
  
 **Find location information for a United States street address including the ZIP Code.**  
  
 This example provides location information for a street address in the United States and requests the results in XML format.  
  
```url
http://dev.virtualearth.net/REST/v1/Locations/US/WA/98052/Redmond/1%20Microsoft%20Way?o=xml&key=BingMapsKey  
```  
  
 **XML Response**  
  
 The Locations resource returned for this example provides the latitude and longitude of the location and defines a geographical area (bounding box) that includes the location. The location entity type is defined as an Address and the address information that was used as input parameters is included and enhanced by adding the county (`AdminDistrict2`) and ZIP Code.  
  
```xml
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
    558732d648204c958546678579cbc5cb  
  </TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <Location>  
          <Name>1 Microsoft Way, Redmond, WA 98052</Name>  
          <Point>  
            <Latitude>47.640120461583138</Latitude>  
            <Longitude>-122.12971039116383</Longitude>  
          </Point>  
          <BoundingBox>  
            <SouthLatitude>47.636257744012461</SouthLatitude>  
            <WestLongitude>-122.13735364288299</WestLongitude>  
            <NorthLatitude>47.643983179153814</NorthLatitude>  
            <EastLongitude>-122.12206713944467</EastLongitude>  
          </BoundingBox>  
          <EntityType>Address</EntityType>  
          <Address>  
            <AddressLine>1 Microsoft Way</AddressLine>  
            <AdminDistrict>WA</AdminDistrict>  
            <AdminDistrict2>King Co.</AdminDistrict2>  
            <CountryRegion>United States</CountryRegion>  
            <FormattedAddress>1 Microsoft Way, Redmond, WA 98052</FormattedAddress>  
            <Locality>Redmond</Locality>  
            <PostalCode>98052</PostalCode>  
          </Address>  
          <Confidence>High</Confidence>  
          <MatchCode>Good</MatchCode>  
          <GeocodePoint>  
            <Latitude>47.640120461583138</Latitude>  
            <Longitude>-122.12971039116383</Longitude>  
            <CalculationMethod>InterpolationOffset</CalculationMethod>  
            <UsageType>Display</UsageType>  
          </GeocodePoint>  
          <GeocodePoint>  
            <Latitude>47.640144601464272</Latitude>  
            <Longitude>-122.12976671755314</Longitude>  
            <CalculationMethod>Interpolation</CalculationMethod>  
            <UsageType>Route</UsageType>  
          </GeocodePoint>  
        </Location>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
  
```
  
 **JSON Response**  
  
 The following JSON response contains the same information as the previous XML response and is provided when the output (`o`) parameter is not set.  
  
```json
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
                  47.636257744012461,  
                  -122.13735364288299,  
                  47.643983179153814,  
                  -122.12206713944467  
               ],  
               "name":"1 Microsoft Way, Redmond, WA 98052",  
               "point":{  
                  "type":"Point",  
                  "coordinates":[  
                     47.640120461583138,  
                     -122.12971039116383  
                  ]  
               },  
               "address":{  
                  "addressLine":"1 Microsoft Way",  
                  "adminDistrict":"WA",  
                  "adminDistrict2":"King Co.",  
                  "countryRegion":"United States",  
                  "formattedAddress":"1 Microsoft Way, Redmond, WA 98052",  
                  "locality":"Redmond",  
                  "postalCode":"98052"  
               },  
               "confidence":"High",  
               "entityType":"Address",  
               "geocodePoints":[  
                  {  
                     "type":"Point",  
                     "coordinates":[  
                        47.640120461583138,  
                        -122.12971039116383  
                     ],  
                     "calculationMethod":"InterpolationOffset",  
                     "usageTypes":[  
                        "Display"  
                     ]  
                  },  
                  {  
                     "type":"Point",  
                     "coordinates":[  
                        47.640144601464272,  
                        -122.12976671755314  
                     ],  
                     "calculationMethod":"Interpolation",  
                     "usageTypes":[  
                        "Route"  
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
   "traceId":"b0b1286504404eafa7e7dad3e749d570"  
}  
```  
  
 **Find location information for a United States street address without a postal code.**  
  
 This example provides location information for the same street address as the previous example, but does not specify the ZIP Code.  
  
```url
http://dev.virtualearth.net/REST/v1/Locations/US/WA/Redmond/1%20Microsoft%20Way?output=xml&key=BingMapsKey  
```  
  
 **Find location information and request up to 10 location results in the response.**  
  
 This example provides location information for the locality "Greenville" and requests up to 10 location results in the response. The default maximum number of locations returned is five (5) results.  
  
```url
http://dev.virtualearth.net/REST/v1/Locations?locality=Greenville&maxResults=10&key=BingMapsKey  
```  
  
 **Find location information by using a structured URL where some parameters have no value.**  
  
 This example provides location information for the United States and uses hyphens (-) for address values that are not specified.  
  
```url
http://dev.virtualearth.net/REST/v1/Locations/US/-/-/-?key=BingMapsKey  
```  
  
 **Find location information by using an unstructured URL and setting the userLocation parameter.**  
  
 This example provides location information for an unstructured query for Kings Road in the United Kingdom and uses the userLocation value to prioritize the response. If you remove the userLocation parameter in this example, the results change because the userLocation position prioritizes results that are closer to this location. For more information about the userLocation parameter and other user context parameters, see [User Context Parameters](../common-parameters-and-types/user-context-parameters.md).  
  
```url
http://dev.virtualearth.net/REST/v1/Locations?culture=en-GB&addressLine=Kings%20Road&o=xml&userLocation=51.504360719046616,-0.12600176611298197&key=BingMapsKey  
```  
  
 **Find location information and request neighborhood information in the response.**  
  
 This example provides location information for Ballard in Washington state (WA) and also returns neighborhood information. Ballard is a neighborhood, but is specified as a locality in the request. Note that in the response, Ballard is defined as the neighborhood and Seattle is defined as the locality.  
  
```url
http://dev.virtualearth.net/REST/v1/Locations/US/WA/-/Ballard/-?o=xml&inclnb=1&key=BingMapsKey  
```  
  
 **XML Response**  
  
```xml
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
    ce2998ccf7dc4985b689b091fb64b3e5  
  </TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <Location>  
          <Name>Ballard, WA</Name>  
          <Point>  
            <Latitude>47.675968170166016</Latitude>  
            <Longitude>-122.38591003417969</Longitude>  
          </Point>  
          <BoundingBox>  
            <SouthLatitude>47.6561164855957</SouthLatitude>  
            <WestLongitude>-122.41252899169922</WestLongitude>  
            <NorthLatitude>47.697746276855469</NorthLatitude>  
            <EastLongitude>-122.36044311523438</EastLongitude>  
          </BoundingBox>  
          <EntityType>Neighborhood</EntityType>  
          <Address>  
            <AdminDistrict>WA</AdminDistrict>  
            <AdminDistrict2>King Co.</AdminDistrict2>  
            <CountryRegion>United States</CountryRegion>  
            <FormattedAddress>Ballard, WA</FormattedAddress>  
            <Locality>Seattle</Locality>  
            <Neighborhood>Ballard</Neighborhood>  
          </Address>  
          <Confidence>High</Confidence>  
          <MatchCode>Good</MatchCode>  
          <GeocodePoint>  
            <Latitude>47.675968170166016</Latitude>  
            <Longitude>-122.38591003417969</Longitude>  
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
  
 The following JSON response contains the same information as the previous XML response and is provided when the output (o) parameter is not set.  
  
```json
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
                  47.6561164855957,  
                  -122.41252899169922,  
                  47.697746276855469,  
                  -122.36044311523438  
               ],  
               "name":"Ballard, WA",  
               "point":{  
                  "type":"Point",  
                  "coordinates":[  
                     47.675968170166016,  
                     -122.38591003417969  
                  ]  
               },  
               "address":{  
                  "adminDistrict":"WA",  
                  "adminDistrict2":"King Co.",  
                  "countryRegion":"United States",  
                  "formattedAddress":"Ballard, WA",  
                  "locality":"Seattle",  
                  "neighborhood":"Ballard"  
               },  
               "confidence":"High",  
               "entityType":"Neighborhood",  
               "geocodePoints":[  
                  {  
                     "type":"Point",  
                     "coordinates":[  
                        47.675968170166016,  
                        -122.38591003417969  
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
   "traceId":"0fa6626c9aae482e968c45e465862f93"  
}  
```  
  
 **Find location information for Canada.**  
  
 This example provides location information for a street in Vancouver, Canada.  
  
```url
http://dev.virtualearth.net/REST/v1/Locations/CA/BC/V6G/Vancouver/Stanley%20Park%20Causeway?key=BingMapsKey  
```  
  
 **Find location information for France.**  
  
 This example provides location information for a street in Paris, France.  
  
```url
http://dev.virtualearth.net/REST/v1/Locations/FR/75007/Paris/Avenue%20Gustave%20Eiffel?key=BingMapsKey  
```  
  
 **Find location information for Germany.**  
  
 This example provides location information for an address in Berlin, Germany. 
  
```url
http://dev.virtualearth.net/REST/v1/Locations/DE/12010/Berlin/Platz%20Der%20Luftbrücke%205?key=BingMapsKey  
```  
  
 **Find location information for the United Kingdom.**  
  
 These examples provide location information for a postal code in the United Kingdom.  
  
```url
http://dev.virtualearth.net/REST/v1/Locations/GB/SW1A?key=BingMapsKey  
```  
  
```url
http://dev.virtualearth.net/REST/v1/Locations/GB/SW1A%202AA?key=BingMapsKey  
```  
  
 **Find location information by using an unstructured URL.**  
  
 These examples provide location information based on the specified parameter values.  
  
```url
http://dev.virtualearth.net/REST/v1/Locations?postalCode=98052&key=BingMapsKey  
```  
  
```url
http://dev.virtualearth.net/REST/v1/Locations?locality=Redmond&adminDistrict=WA&key=BingMapsKey  
```  
  
```url
http://dev.virtualearth.net/REST/v1/Locations?countryRegion=AU&adminDistrict=WA&key=BingMapsKey  
```  
  
```url
http://dev.virtualearth.net/REST/v1/Locations?locality=London&postalCode=SW1A&key=BingMapsKey  
```  
  
## HTTP Status Codes  
  
[!INCLUDE [get-status-code-note](../../includes/get-status-code-note.md)]
  
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
 [Using the REST Services with .NET](../using-the-rest-services-with-net.md)   
 [JSON Data Contracts](../json-data-contracts.md)   
 [Geocoding a Location](https://msdn.microsoft.com/en-us/library/gg427601.aspx)
 [Getting Route Directions](https://msdn.microsoft.com/en-us/library/gg427607.aspx)   
 [Find a location by query](https://www.bingmapsportal.com/ISDK/AjaxV7#RESTServices1)