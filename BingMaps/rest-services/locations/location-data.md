---
title: "Location Data | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d16845e0-c89f-4523-a59f-c29a7e22f108
caps.latest.revision: 55
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Location Data

## Location Resource  

The response returned by a Locations URL contains one or more Location resources. Each Location resource contains location information that corresponds to the values provided in the request. This topic provides descriptions of the Locations resource fields, followed by JSON and XML examples.  
  
[!INCLUDE [get-common-response-note](../../includes/get-common-response-note.md)]
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|name|Name|string|The name of the resource.|  
|point|Point|Point. For more information about the Point type, see [Location and Area Types](../common-parameters-and-types/location-and-area-types.md).|The latitude and longitude coordinates of the location.|  
|bbox|BoundingBox|BoundingBox. For more information about the BoundingBox type, see [Location and Area Types](../common-parameters-and-types/location-and-area-types.md).|A geographic area that contains the location. A bounding box contains SouthLatitude, WestLongitude, NorthLatitude, and EastLongitude values in units of degrees.|  
|entityType|EntityType|string|The classification of the geographic entity returned, such as `Address`.|  
|address|Address|Address|The postal address for the location. An address can contain AddressLine, Neighborhood, Locality, AdminDistrict, AdminDistrict2, CountryRegion, CountryRegionIso2, PostalCode, FormattedAddress, and Landmark fields.<br /><br /> Notes:<br /><br /> -   If you specify include=ciso2 in the request, a CountryRegionIso2 field containing the [two-letter ISO country code](http://www.iso.org/iso/country_codes.htm) is returned.<br />-   If you specify include=neighborhood in the request, a Neighborhood field is returned when available.<br /><br /> For more information about these fields, see [Location and Area Types](../common-parameters-and-types/location-and-area-types.md).|  
|confidence|Confidence|One of the following values:<br /><br /> High, Medium, Low|The level of confidence that the geocoded location result is a match. Use this value with the match code to determine for more complete information about the match.<br /><br /> The confidence of a geocoded location is based on many factors including the relative importance of the geocoded location and the user’s location, if specified. The following description provides more information about how confidence scores are assigned and how results are ranked.<br /><br /> If the confidence is set to High, one or more strong matches were found. Multiple High confidence matches are sorted in ranked order by importance when applicable. For example, landmarks have importance but addresses do not.<br /><br /> If a request includes a user location or a map area (see [User Context Parameters](../common-parameters-and-types/user-context-parameters.md)), then the ranking may change appropriately. For example, a location query for "Paris" returns "Paris, France" and "Paris, TX" both with High confidence. "Paris, France" is always ranked first due to importance unless a user location indicates that the user is in or very close to Paris, TX or the map view indicates that the user is searching in that area.<br /><br /> In some situations, the returned match may not be at the same level as the information provided in the request. For example, a request may specify address information and the geocode service may only be able to match a postal code. In this case, if the geocode service has a confidence that the postal code matches the data, the confidence is set to Medium and the match code is set to UpHierarchy to specify that it could not match all of the information and had to search up-hierarchy.<br /><br /> If the location information in the query is ambiguous, and there is no additional information to rank the locations (such as user location or the relative importance of the location), the confidence is set to Medium. For example, a location query for "148th Ave, Bellevue" may return "148th Ave SE" and "148th Ave NE" both with Medium confidence.<br /><br /> If the location information in the query does not provide enough information to geocode a specific location, a less precise location value may be returned and the confidence is set to Medium. For example, if an address is provided, but a match is not found for the house number, the geocode result with a Roadblock entity type may be returned. You can check the entityType field value to determine what type of entity the geocode result represents. For a list of entity types, see [POI Entity Types](/bing-maps-docs/spatial-data-services/poi-entity-types.md).|  
|matchCodes|MatchCode|One or more of the following values: Good, Ambiguous, UpHierarchy|One or more match code values that represent the geocoding level for each location in the response.<br /><br /> For example, a geocoded location with match codes of Good and Ambiguous means that more than one geocode location was found for the location information and that the geocode service did not have search up-hierarchy to find a match.<br /><br /> Similarly, a geocoded location with match codes of Ambiguous and UpHierarchy means that a geocode location could not be found that matched all of the location information, so the geocode service had to search up-hierarchy and found multiple matches at that level. An example of up an Ambiguous and UpHierarchy result is when you provide complete address information, but the geocode service cannot locate a match for the street address and instead returns information for more than one RoadBlock value.<br /><br /> The possible values are:<br /><br /> **Good**: The location has only one match or all returned matches are considered strong matches. For example, a query for New York returns several Good matches.<br /><br /> **Ambiguous**: The location is one of a set of possible matches. For example, when you query for the street address 128 Main St., the response may return two locations for 128 North Main St. and 128 South Main St. because there is not enough information to determine which option to choose.<br /><br /> **UpHierarchy**: The location represents a move up the geographic hierarchy. This occurs when a match for the location request was not found, so a less precise result is returned. For example, if a match for the requested address cannot be found, then a match code of UpHierarchy with a RoadBlock entity type may be returned.|  
|queryParseValues|QueryParseValue|collection|A collection of parsed values that shows how a location query string was parsed into one or more of the following address values.<br /><br /> -   AddressLine<br />-   Locality<br />-   AdminDistrict<br />-   AdminDistrict2<br />-   PostalCode<br />-   CountryRegion<br />-   Landmark|  
|geocodePoints|GeocodePoint|collection|A collection of geocoded points that differ in how they were calculated and their suggested use. For a description of the points in this collection, see the **Geocode Point Fields** section below.|  
  
 **Geocode Point Fields**  
  
 The following fields are provided for each geocode point in the Geocode Points collection.  
  
|JSON|XML|Type|Description|  
|----------|---------|----------|-----------------|  
|point|Point|Point. For more information about the Point type, see [Location and Area Types](../common-parameters-and-types/location-and-area-types.md).|The latitude and longitude coordinates of the geocode point.|  
|calculationMethod|CalculationMethod|One of the following values:<br /><br /> -   Interpolation: The geocode point was matched to a point on a road using interpolation.<br />-   InterpolationOffset: The geocode point was matched to a point on a road using interpolation with an additional offset to shift the point to the side of the street.<br />-   Parcel: The geocode point was matched to the center of a parcel.<br />-   Rooftop: The geocode point was matched to the rooftop of a building.|The method that was used to compute the geocode point.|  
|usageTypes|usageType|One or more of the following values:<br /><br /> -   Display<br />-   Route|The best use for the geocode point.<br /><br /> Each geocode point is defined as a Route point, a Display point or both.<br /><br /> Use Route points if you are creating a route to the location. Use Display points if you are showing the location on a map. For example, if the location is a park, a Route point may specify an entrance to the park where you can enter with a car, and a Display point may be a point that specifies the center of the park.|  
  
## Examples  
  
### JSON Example  
  
```json
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
         "matchCodes":[  
           "Good"  
         ]  
      }  
   ]  
}  
```
  
### XML Example  
  
```xml
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
  <MatchCode>Good</<MatchCode>  
  <QueryParseValue Property="AddressLine" Value="1 Microsoft Way" />   
  <QueryParseValue Property="Locality" Value="Redmond" />   
  <QueryParseValue Property="PostalCode" Value="98052" />   
  <QueryParseValue Property="AdminDistrict" Value="WA" />   
  <GeocodePoint>  
    <Latitude>47.640568390488625</Latitude>  
    <Longitude>-122.1293731033802</Longitude>  
    <CalculationMethod>Interpolation</CalculationMethod>  
    <UsageType>Display</UsageType>  
    <UsageType>Route</UsageType>  
  </GeocodePoint>  
</Location>  
```