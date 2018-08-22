---
title: "Find a Location by Point | Microsoft Docs"
ms.date: "02/28/2018"
ms.topic: "article"
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Find a Location by Point

Use the following URL template to get the location information associated with latitude and longitude coordinates.  
  
 When you make a request by using the following URL template, the response returns one or more Location resources that contain location information associated with the latitude and longitude coordinate values that you specify. Location information can be as specific as an address or more general such as the country or region. You can specify the type of location information you want to receive by setting the `includeEntityTypes` parameter in the URL. For example, you can specify to only receive information about the neighborhood that corresponds to the coordinates. For more information about the Location resource, see [Location Data](../services/location-data.md). You can also view the example URL and response values in the Examples section.  
  
## URL Template  
  
[!INCLUDE [get-bing-map-key-note](../../includes/get-bing-map-key-note.md)]
  
 **Get an address for a specified point (latitude and longitude).**  
  
```url
http://dev.virtualearth.net/REST/v1/Locations/{point}?includeEntityTypes={entityTypes}&includeNeighborhood={includeNeighborhood}&include={includeValue}&key={BingMapsKey}  
```  
  
### Template Parameters  
  
> [!NOTE]
>  See the [Common Parameters and Types](../common-parameters-and-types/index.md) section for additional common parameters to use with these URLs.  
>   
>  Common parameters include:  
>   
>  -   [Output Parameters](../common-parameters-and-types/output-parameters.md): Includes response output types and the JSON callback parameters.  
> -   [Culture Parameter](../common-parameters-and-types/culture-parameter.md): Includes a list of the supported cultures.  
>   
>  Parameter values are not case-sensitive.  
  
|Parameters|Alias|Description|Values|  
|----------------|-----------|-----------------|------------|  
|includeEntityTypes||**Optional**. Specifies the entity types that you want to return in the response. Only the types you specify will be returned. If the point cannot be mapped to the entity types you specify, no location information is returned in the response.|A comma separated list of entity types selected from the following options.<br /><br /> -   Address<br />-   Neighborhood<br />-   PopulatedPlace<br />-   Postcode1<br />-   AdminDivision1<br />-   AdminDivision2<br />-   CountryRegion<br /><br /> These entity types are ordered from the most specific entity to the least specific entity. When entities of more than one entity type are found, only the most specific entity is returned. For example, if you specify Address and AdminDistrict1 as entity types and entities were found for both types, only the Address entity information is returned in the response. One exception to this rule is when both PopulatedPlace and Neighborhood entity types are specified and information is found for both. In this case, the information for both entity types is returned. Also, more than one Neighborhood may be returned because the area covered by two different neighborhoods can overlap.|  
|point||**Required.** The coordinates of the location that you want to reverse geocode. A point is specified by a latitude and a longitude. For more information, see the definition of Point in [Location and Area Types](../common-parameters-and-types/location-and-area-types.md).|A point on the Earth specified by a latitude and longitude. For more information, see the definition of Point in [Location and Area Types](../common-parameters-and-types/location-and-area-types.md).<br /><br /> Example: `47.64054,-122.12934`|  
|includeNeighborhood|inclnb|**Optional.** Specifies to include the neighborhood in the response when it is available.|One of the following values:<br /><br /> -   1: Include neighborhood information when available.<br />-   0 **[default]**: Do not include neighborhood information.<br />     Example:<br /> `inclnb=1`|  
|include|incl|**Optional.** Specifies additional values to include.|The only value for this parameter is ciso2. When you specify include=ciso2, the [two-letter ISO country code](http://www.iso.org/iso/country_codes.htm) is included for addresses in the response.<br /><br />Example:<br /><br /> `incl=ciso2`|  
  
## Response

One or more Location resources are returned in the response when you make a request using this URL template. For more information about the Location resource, see [Location Data](location-data.md). For more information about the common response syntax for the Bing Maps REST Services, see [Common Response Description](../common-parameters-and-types/common-response-description.md). JSON and XML responses are provided for the URL example in the following section.  
  
 This URL supports JSON (`application/json`) and XML (`application/xml`) response formats. A JSON response is provided by default unless you request XML output by setting the output (`o`) parameter. For more information, see [Output Parameters](../common-parameters-and-types/output-parameters.md).  
  
## Examples  
 **Find location information for a specified point on the Earth.**  
  
 This example gets address information for a specified latitude and longitude and requests the results in XML format.  
  
```url
http://dev.virtualearth.net/REST/v1/Locations/47.64054,-122.12934?o=xml&key=BingMapsKey  
```  
  
 **XML Response**  
  
 This example returns the following XML response.  
  
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
    dd31ffaf098f4406b7ecdd0da36680ff  
  </TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <Location>  
          <Name>1 Microsoft Way, Redmond, WA 98052</Name>  
          <Point>  
            <Latitude>47.640568390488625</Latitude>  
            <Longitude>-122.1293731033802</Longitude>  
          </Point>  
          <BoundingBox>  
            <SouthLatitude>47.636705672917948</SouthLatitude>  
            <WestLongitude>-122.137016420622</WestLongitude>  
            <NorthLatitude>47.6444311080593</NorthLatitude>  
            <EastLongitude>-122.1217297861384</EastLongitude>  
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
          <Confidence>Medium</Confidence>  
          <MatchCode>Good</MatchCode>  
          <GeocodePoint>  
            <Latitude>47.640568390488625</Latitude>  
            <Longitude>-122.1293731033802</Longitude>  
            <CalculationMethod>Interpolation</CalculationMethod>  
            <UsageType>Display</UsageType>  
            <UsageType>Route</UsageType>  
          </GeocodePoint>  
        </Location>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
  
```  
  
 **JSON Response**  
  
 The following JSON response contains the same information as the XML response and is provided when the output (`o`) parameter is not set.  
  
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
                  47.636705672917948,  
                  -122.137016420622,  
                  47.6444311080593,  
                  -122.1217297861384  
               ],  
               "name":"1 Microsoft Way, Redmond, WA 98052",  
               "point":{  
                  "type":"Point",  
                  "coordinates":[  
                     47.640568390488625,  
                     -122.1293731033802  
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
               "confidence":"Medium",  
               "entityType":"Address",  
               "geocodePoints":[  
                  {  
                     "type":"Point",  
                     "coordinates":[  
                        47.640568390488625,  
                        -122.1293731033802  
                     ],  
                     "calculationMethod":"Interpolation",  
                     "usageTypes":[  
                        "Display",  
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
   "traceId":"99b1256e09044490bce82bbbba1dab7a"  
}  
```
  
 **Find location information for a specified point and request that only CountryRegion entity types be returned.**  
  
 This example requests only country or region information for the same latitude and longitude as the previous example.  
  
```url 
http://dev.virtualearth.net/REST/v1/Locations/47.64054,-122.12934?includeEntityTypes=countryRegion&o=xml&key=BingMapsKey  
```  
  
 **XML Response**  
  
 This example returns the following XML response.  
  
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
    ca4cc0ce946e4564a20a44db811ee954  
  </TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <Location>  
          <Name>United States</Name>  
          <Point>  
            <Latitude>39.450000762939453</Latitude>  
            <Longitude>-98.907997131347656</Longitude>  
          </Point>  
          <BoundingBox>  
            <SouthLatitude>26.677207946777344</SouthLatitude>  
            <WestLongitude>177.3487548828125</WestLongitude>  
            <NorthLatitude>75.7627944946289</NorthLatitude>  
            <EastLongitude>-55.848747253417969</EastLongitude>  
          </BoundingBox>  
          <EntityType>Sovereign</EntityType>  
          <Address>  
            <CountryRegion>United States</CountryRegion>  
            <FormattedAddress>United States</FormattedAddress>  
          </Address>  
          <Confidence>High</Confidence>  
          <MatchCode>Good</MatchCode>  
          <GeocodePoint>  
            <Latitude>39.450000762939453</Latitude>  
            <Longitude>-98.907997131347656</Longitude>  
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
                  26.677207946777344,  
                  177.3487548828125,  
                  75.7627944946289,  
                  -55.848747253417969  
               ],  
               "name":"United States",  
               "point":{  
                  "type":"Point",  
                  "coordinates":[  
                     39.450000762939453,  
                     -98.907997131347656  
                  ]  
               },  
               "address":{  
                  "countryRegion":"United States",  
                  "formattedAddress":"United States"  
               },  
               "confidence":"High",  
               "entityType":"Sovereign",  
               "geocodePoints":[  
                  {  
                     "type":"Point",  
                     "coordinates":[  
                        39.450000762939453,  
                        -98.907997131347656  
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
   "traceId":"df80a942ddb3440188d7f97a31979d1a"  
}  
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