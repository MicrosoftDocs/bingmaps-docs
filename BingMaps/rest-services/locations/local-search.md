---
title: "Local Search | Microsoft Docs"
ms.custom: ""
ms.date: "12/10/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d16845e0-c89f-4523-a59f-c29a7e22f108
caps.latest.revision: 55
author: "v-chrfr"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Local Search

The Bing Maps Local Search API returns a list of business entities centered around a location or a geographic region. Local Search requests are made by either specifying a list of type string IDs (e.g. "EatDrink") or a query (e.g. "Deep Dish Pizza"), and by specifying either the user's location or a geographical region. Aside from a point, two geographic regions are supported: a bounding box of coordinates or a circular region specified by a radius and a center point.

> [!NOTE]
>
> Presently, the Local Search API supports business entities only in the US.

## API Templates

### Search by Query

Make a Local Search API request based on a string query by specifying a user location.

```url
https://dev.virtualearth.net/REST/v1/LocalSearch/?query={query}&userLocation={point}&key={BingMapsAPIKey}
```

### Search by Query Restricted to a Bounding Box

Make a Local Search API request based on a string query within the specified bounding box using the `userMapView` parameter.

```url
https://dev.virtualearth.net/REST/v1/LocalSearch/?query={query}&userMapView={lat,lon,lat,lon}&key={BingMapsAPIKey}
```

### Search by Query Restricted to a Circular Region

Make a Local Search API request based on a string query within the specified circular region using the `userCircularMapView` parameter.

```url
https://dev.virtualearth.net/REST/v1/LocalSearch/?query={query}&userCircularMapView={lat,lon,radius}&key={BingMapsAPIKey}
```

### Search by Entity Type

Search for businesses by specifying a comma-separated list of type string IDs at a given location using the `type` parameter. The `userMapView` and `userCircularMapView` parameters can also be used when searching by categories.

```url
https://dev.virtualearth.net/REST/v1/LocalSearch/?type={type_string_id_list}&userLocation={point}&key={BingMapsAPIKey}
```

## API Parameters

|Parameter | Alias | Description | Values |
|----------|:-----:|-------------|--------|
|`query`   | `q`   | **Required, if searching by query**. The query used to search for local entities. | A string that contains information about a location, such as an address or landmark name.<br /><br />*Example:* `query = 1%20Microsoft%20Way` | 
|`type`|  | **Required, if searching by type**. The specified types used to filter the local entities returned by the Local Search API.| A comma-separated list of string type identifiers. See the [list of available Type IDs](../common-parameters-and-types/type-identifiers/index.md)|
|`maxResults`| `maxRes` | **Optional.** Specifies the maximum number of locations to return in the response.  | An integer between 1 and 25. The default value is 5.<br /><br /> *Example*: `maxResults=10`|
|`userCircularMapView` |`ucmv` | **Optional.** A circular geographic region.| A circular region specified by a comma separated list of the latitude and longitude of the center of the circle, and the radius of the circle, in meters. *Example*: `48.604311,-122.981998,5000` |
|`userLocation` | `ul` |**Required if neither `userCircularMapView` nor `userMapView` are provided.** Coordinates for the user's location on Earth. | A comma separated list of the user's location (latitude, longitude) and radius, in meters, representing the confidence in the accuracy of the user's location.<br /><br />*Example*: `48.604311,-122.981998,5000`|
|`userMapView` | `umv`  | **Optional.** A rectangular region (a bounding box). | Specified by a comma separated list of the latitudes and longitudes of two corners of the rectangle, in the following order:<br /><br />- Latitude of the Northwest corner<br />- Longitude of the Northwest corner<br />- Latitude of the Southeast corner<br />- Longitude of the Southeast corner<br /><br /><br /> *Example*: `29.8171041,-122.981995,48.604311,-95.5413725`|

## Response

The Local Search API supports both JSON and XML responses.

### LocalSearch Resource

Successful Local Search API requests return a list of `LocalSearch` resources.

|JSON|XML|Description|
|----|----|----------|
|`type`|`Type`| The type of local entity, e.g. `Restaurant`.|
|`id`| `ID`|Local entity identifier.| 
|`name`|`Name`|The name of the local entity, e.g. `Yea's Wok`.|
|`url`|`URL`| If available, the URL for the local entity.|
|`geocodePoints`|`GeoCodePoints`| A container with the latitude and longitude for the local entity; typically the rooftop of the entity.|
|`point` | `Point` | A container with a latitude and longitude suitable for providing directions to the local entity. |
|`address`|`Address`| A container including the `formattedAddress`, `streetAddress`, `locality`, `adminDistrict`, `postalCode`, `countryRegion`, and `neighborhood` fields for the local entity.|
|`telephone`|`Telephone`| If available, the telephone number for the local entity.|


## Examples

### Search by Query for local coffee shops in Downtown Seattle

Pioneer Square, in downtown Seattle, is located at: `47.602038, -122.333964`. Setting the parameter `query` to `coffee` gives us the following Local Search API URL:

```url
https://dev.virtualearth.net/REST/v1/LocalSearch/?query=coffee&userLocation=47.602038,-122.333964&key={BingMapsAPIKey}
```

The JSON response:

```json
{
  "authenticationResultCode": "ValidCredentials",
  "brandLogoUri": "http://dev.virtualearth.net/Branding/logo_powered_by.png",
  "copyright": "Copyright © 2018 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",
  "resourceSets": [
    {
      "estimatedTotal": 1,
      "resources": [
        {
          "__type": "SearchResult:http://schemas.microsoft.com/search/local/ws/rest/v1/LocalSearch",
          "entities": [
            {
              "type": "LocalBusiness",
              "id": "https://www.bingapis.com/api/v7/#Places.0",
              "name": "Starbucks",
              "url": "http://www.starbucks.com/store/15229/",
              "address": {
                "formattedAddress": "102 1st Ave S, Seattle, WA, 98104",
                "streetAddress": "102 1st Ave S",
                "locality": "Seattle",
                "adminDistrict": "WA",
                "postalCode": "98104",
                "countryRegion": "US",
                "neighborhood": "Pioneer Square"
              },
              "telephone": "(206) 382-2656"
            },
            {
              "type": "LocalBusiness",
              "id": "https://www.bingapis.com/api/v7/#Places.1",
              "name": "Starbucks",
              "url": "http://www.starbucks.com/store/16645/",
              "geocodePoints": {
                "latitude": 47.603588104248,
                "longitude": -122.335548400879
              },
              "point": {
                "latitude": 47.6036911010742,
                "longitude": -122.335311889648
              },
              "address": {
                "formattedAddress": "823 1st Ave, Seattle, WA, 98104",
                "streetAddress": "823 1st Ave",
                "locality": "Seattle",
                "adminDistrict": "WA",
                "postalCode": "98104",
                "countryRegion": "US",
                "neighborhood": "Downtown"
              },
              "telephone": "(206) 340-9184"
            },
            {
              "type": "LocalBusiness",
              "id": "https://www.bingapis.com/api/v7/#Places.2",
              "name": "Elm Coffee Roasters",
              "url": "http://elmcoffeeroasters.com/",
              "geocodePoints": {
                "latitude": 47.6002197265625,
                "longitude": -122.33130645752
              },
              "point": {
                "latitude": 47.6002197265625,
                "longitude": -122.331581115723
              },
              "address": {
                "formattedAddress": "240 2nd Ave S Ste 103, Seattle, WA, 98104",
                "streetAddress": "240 2nd Ave S Ste 103",
                "locality": "Seattle",
                "adminDistrict": "WA",
                "postalCode": "98104",
                "countryRegion": "US",
                "neighborhood": "Downtown"
              },
              "telephone": "(206) 445-7808"
            },
            {
              "type": "LocalBusiness",
              "id": "https://www.bingapis.com/api/v7/#Places.3",
              "name": "Starbucks",
              "url": "http://www.starbucks.com/store/11311/",
              "geocodePoints": {
                "latitude": 47.6045303344727,
                "longitude": -122.330612182617
              },
              "point": {
                "latitude": 47.604736328125,
                "longitude": -122.330101013184
              },
              "address": {
                "formattedAddress": "701 5th Ave, Seattle, WA, 98104",
                "streetAddress": "701 5th Ave",
                "locality": "Seattle",
                "adminDistrict": "WA",
                "postalCode": "98104",
                "countryRegion": "US",
                "neighborhood": "Downtown"
              },
              "telephone": "(206) 264-0152"
            },
            {
              "type": "LocalBusiness",
              "id": "https://www.bingapis.com/api/v7/#Places.4",
              "name": "Starbucks",
              "url": "http://www.starbucks.com/store/16138/",
              "geocodePoints": {
                "latitude": 47.599048614502,
                "longitude": -122.33268737793
              },
              "point": {
                "latitude": 47.5990524291992,
                "longitude": -122.332885742188
              },
              "address": {
                "formattedAddress": "400 Occidental Ave S, Seattle, WA, 98104",
                "streetAddress": "400 Occidental Ave S",
                "locality": "Seattle",
                "adminDistrict": "WA",
                "postalCode": "98104",
                "countryRegion": "US",
                "neighborhood": "Downtown"
              },
              "telephone": "(206) 624-2561"
            },
            {
              "type": "LocalBusiness",
              "id": "https://www.bingapis.com/api/v7/#Places.5",
              "name": "Starbucks",
              "url": "http://www.starbucks.com/store/11917/",
              "geocodePoints": {
                "latitude": 47.6050415039062,
                "longitude": -122.334266662598
              },
              "point": {
                "latitude": 47.6052856445312,
                "longitude": -122.333709716797
              },
              "address": {
                "formattedAddress": "999 3rd Ave, Seattle, WA, 98104",
                "streetAddress": "999 3rd Ave",
                "locality": "Seattle",
                "adminDistrict": "WA",
                "postalCode": "98104",
                "countryRegion": "US",
                "neighborhood": "Downtown"
              },
              "telephone": "(206) 748-0058"
            },
            {
              "type": "LocalBusiness",
              "id": "https://www.bingapis.com/api/v7/#Places.6",
              "name": "Starbucks",
              "url": "http://www.starbucks.com/store/89253/",
              "geocodePoints": {
                "latitude": 47.6057090759277,
                "longitude": -122.330268859863
              },
              "point": {
                "latitude": 47.6054878234863,
                "longitude": -122.330787658691
              },
              "address": {
                "formattedAddress": "800 5th Ave, Seattle, WA, 98104",
                "streetAddress": "800 5th Ave",
                "locality": "Seattle",
                "adminDistrict": "WA",
                "postalCode": "98104",
                "countryRegion": "US",
                "neighborhood": "Downtown"
              },
              "telephone": "(206) 623-3425"
            },
            {
              "type": "LocalBusiness",
              "id": "https://www.bingapis.com/api/v7/#Places.7",
              "name": "Cherry Street Coffee House",
              "url": "http://www.cherryst.com/locations",
              "geocodePoints": {
                "latitude": 47.6025314331055,
                "longitude": -122.333778381348
              },
              "point": {
                "latitude": 47.6027069091797,
                "longitude": -122.333953857422
              },
              "address": {
                "formattedAddress": "103 Cherry St, Seattle, WA, 98104",
                "streetAddress": "103 Cherry St",
                "locality": "Seattle",
                "adminDistrict": "WA",
                "postalCode": "98104",
                "countryRegion": "US",
                "neighborhood": "Downtown"
              },
              "telephone": "(206) 621-9372"
            },
            {
              "type": "LocalBusiness",
              "id": "https://www.bingapis.com/api/v7/#Places.8",
              "name": "Slate Coffee Roasters",
              "url": "http://www.slatecoffee.com/",
              "geocodePoints": {
                "latitude": 47.6025581359863,
                "longitude": -122.332389831543
              },
              "point": {
                "latitude": 47.6024436950684,
                "longitude": -122.332672119141
              },
              "address": {
                "formattedAddress": "602 2nd Ave, Seattle, WA, 98104",
                "streetAddress": "602 2nd Ave",
                "locality": "Seattle",
                "adminDistrict": "WA",
                "postalCode": "98104",
                "countryRegion": "US",
                "neighborhood": "Downtown"
              }
            },
            {
              "type": "LocalBusiness",
              "id": "https://www.bingapis.com/api/v7/#Places.9",
              "name": "Starbucks",
              "url": "http://www.starbucks.com/store/8749/",
              "geocodePoints": {
                "latitude": 47.5963554382324,
                "longitude": -122.327346801758
              },
              "point": {
                "latitude": 47.6017303466797,
                "longitude": -122.327651977539
              },
              "address": {
                "formattedAddress": "700 5th Ave, Seattle, WA, 98104",
                "streetAddress": "700 5th Ave",
                "locality": "Seattle",
                "adminDistrict": "WA",
                "postalCode": "98104",
                "countryRegion": "US",
                "neighborhood": "Downtown"
              },
              "telephone": "(206) 622-5789"
            }
          ],
          "searchAction": {},
          "total": 10
        }
      ]
    }
  ],
  "statusCode": 200,
  "statusDescription": "OK",
  "traceId": "9f8b3a0cf3ea4c35adf3a3dd6c1b13bd|CO39C69F01|7.7.0.0"
}
```

### Search for coffee in Downtown Seattle by Type

Instead of searching by a query, the Local Search API allows us to search at a location for local entities what match a comma-separated list of string type identifiers. For example, looking at the available [Type IDs](Type%20Identifiers.md), we find that the best match for "coffee" is the string ID `CoffeeAndTea`. So we set the parameter `type` to `CoffeeAndTea`.

Here is the URL, using the same location the previous example:

```url
https://dev.virtualearth.net/REST/v1/LocalSearch/?type=CoffeeAndTea&userLocation=47.602038,-122.333964&o=xml&key={BingMapsAPIKey}
```

And here is the XML response:

```xml
 <Response>
    <Copyright>Copyright © 2018 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>
     <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>
    <StatusCode>200</StatusCode>
    <StatusDescription>OK</StatusDescription>
    <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>
    <TraceId>3245c04c0a694c309549c6ca6217facc|MW10000A85|7.7.0.0</TraceId>
    <ResourceSets>
        <ResourceSet>
            <EstimatedTotal>5</EstimatedTotal>
            <Resources>
                <Resource xsi:type="SearchResult">
                    <Name>Pizza Hut</Name>
                    <Point>
                        <Latitude>47.5445327758789</Latitude>
                        <Longitude>-122.376449584961</Longitude>
                    </Point>
                    <EntityType>Restaurant</EntityType>
                    <Address>
                        <AddressLine>6501 35th Ave SW</AddressLine>
                        <AdminDistrict>WA</AdminDistrict>
                        <CountryRegion>US</CountryRegion>
                        <FormattedAddress>6501 35th Ave SW, Seattle, WA, 98126</FormattedAddress>
                        <Locality>Seattle</Locality>
                        <PostalCode>98126</PostalCode>
                    </Address>
                    <PhoneNumber>(206) 935-9300</PhoneNumber>
                    <Website>https://locations.pizzahut.com/wa/seattle/6501-35th-ave-sw</Website>
                    <GeocodePoint>
                        <Latitude>47.5445404052734</Latitude>
                        <Longitude>-122.376747131348</Longitude>
                        <CalculationMethod>Rooftop</CalculationMethod>
                        <UsageType>Display</UsageType>
                    </GeocodePoint>
                </Resource>
                <Resource xsi:type="SearchResult">
                    <Name>Pizza Hut</Name>
                    <Point>
                        <Latitude>47.5704307556152</Latitude>
                        <Longitude>-122.291015625</Longitude>
                    </Point>
                    <EntityType>Restaurant</EntityType>
                    <Address>
                        <AddressLine>3642 33rd Ave S Ste C-6</AddressLine>
                        <AdminDistrict>WA</AdminDistrict>
                        <CountryRegion>US</CountryRegion>
                        <FormattedAddress>3642 33rd Ave S Ste C-6, Seattle, WA, 98144</FormattedAddress>
                        <Locality>Seattle</Locality>
                        <PostalCode>98144</PostalCode>
                    </Address>
                    <PhoneNumber>(206) 725-7000</PhoneNumber>
                    <Website>https://locations.pizzahut.com/wa/seattle/3642-33rd-avenue-s</Website>
                    <GeocodePoint>
                        <Latitude>47.5704307556152</Latitude>
                        <Longitude>-122.290733337402</Longitude>
                        <CalculationMethod>Rooftop</CalculationMethod>
                        <UsageType>Display</UsageType>
                    </GeocodePoint>
                </Resource>
                <Resource xsi:type="SearchResult">
                    <Name>Domino's Pizza</Name>
                    <Point>
                        <Latitude>47.599250793457</Latitude>
                        <Longitude>-122.308433532715</Longitude>
                    </Point>
                    <EntityType>Restaurant</EntityType>
                    <Address>
                        <AddressLine>1800 S Jackson St, Ste D</AddressLine>
                        <AdminDistrict>WA</AdminDistrict>
                        <CountryRegion>US</CountryRegion>
                        <FormattedAddress>1800 S Jackson St Ste D, Seattle, WA, 98144</FormattedAddress>
                        <Locality>Seattle</Locality>
                        <PostalCode>98144</PostalCode>
                    </Address>
                    <PhoneNumber>(206) 325-3230</PhoneNumber>
                    <Website>https://www.dominos.com/en/?redirect=homepage&utm_source=locallistings&utm_medium=loclist&utm_campaign=localmaps</Website>
                    <GeocodePoint>
                        <Latitude>47.5996704101562</Latitude>
                        <Longitude>-122.308433532715</Longitude>
                        <CalculationMethod>Rooftop</CalculationMethod>
                        <UsageType>Display</UsageType>
                    </GeocodePoint>
                </Resource>
                <Resource xsi:type="SearchResult">
                    <Name>Domino's Pizza</Name>
                    <Point>
                        <Latitude>47.6012992858887</Latitude>
                        <Longitude>-122.334167480469</Longitude>
                    </Point>
                    <EntityType>Restaurant</EntityType>
                    <Address>
                        <AddressLine>112 1st Ave S, Ste 100</AddressLine>
                        <AdminDistrict>WA</AdminDistrict>
                        <CountryRegion>US</CountryRegion>
                        <FormattedAddress>112 1st Ave S Ste 100, Seattle, WA, 98104</FormattedAddress>
                        <Locality>Seattle</Locality>
                        <PostalCode>98104</PostalCode>
                    </Address>
                    <PhoneNumber>(206) 445-0999</PhoneNumber>
                    <Website>https://www.dominos.com/en/?redirect=homepage&utm_source=locallistings&utm_medium=loclist&utm_campaign=localmaps</Website>
                    <GeocodePoint>
                        <Latitude>47.6012992858887</Latitude>
                        <Longitude>-122.333839416504</Longitude>
                        <CalculationMethod>Rooftop</CalculationMethod>
                        <UsageType>Display</UsageType>
                    </GeocodePoint>
                </Resource>
                <Resource xsi:type="SearchResult">
                    <Name>Pizza Hut</Name>
                    <Point>
                        <Latitude>47.5100479125977</Latitude>
                        <Longitude>-122.354515075684</Longitude>
                    </Point>
                    <EntityType>Restaurant</EntityType>
                    <Address>
                        <AddressLine>1517 SW 104th St</AddressLine>
                        <AdminDistrict>WA</AdminDistrict>
                        <CountryRegion>US</CountryRegion>
                        <FormattedAddress>1517 SW 104th St, Seattle, WA, 98146</FormattedAddress>
                        <Locality>Seattle</Locality>
                        <PostalCode>98146</PostalCode>
                    </Address>
                    <PhoneNumber>(206) 764-6000</PhoneNumber>
                    <Website>https://locations.pizzahut.com/wa/seattle/1517-sw-104th-st</Website>
                    <GeocodePoint>
                        <Latitude>47.5098915100098</Latitude>
                        <Longitude>-122.354507446289</Longitude>
                        <CalculationMethod>Rooftop</CalculationMethod>
                        <UsageType>Display</UsageType>
                    </GeocodePoint>
                </Resource>
            </Resources>
        </ResourceSet>
    </ResourceSets>
```

### Search for a Cafe or Korean Restaurant within a Circular Radius

Suppose we want to find either movie theaters or Korean restaurants within a 300 meter radius right in the middle of Ballard, Seattle.

Searching the string [Type IDs](Type%20Identifiers.md), we find two matches for our type strings: `MovieTheaters` and `KoreanRestaurants`. So we set the parameter `type` to `MovieTheaters,KoreanRestaurants`, and we specify the `userCircularMapView`  instead of the `userLocation` parameter.

The resulting URL is:

```url
https://dev.virtualearth.net/REST/v1/LocalSearch/?type=MovieTheaters,KoreanRestaurants&userCircularMapView=47.668979,-122.387562,300&key={BingMapsAPIKey}
```   

And the JSON response:

```json
{
  "authenticationResultCode": "ValidCredentials",
  "brandLogoUri": "http://dev.virtualearth.net/Branding/logo_powered_by.png",
  "copyright": "Copyright © 2018 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",
  "resourceSets": [
    {
      "estimatedTotal": 1,
      "resources": [
        {
          "__type": "SearchResult:http://schemas.microsoft.com/search/local/ws/rest/v1/LocalSearch",
          "entities": [
            {
              "type": "LocalBusiness",
              "id": "https://www.bingapis.com/api/v7/#Places.0",
              "name": "Majestic Bay Theatres",
              "url": "http://majesticbay.com/",
              "point": {
                "latitude": 47.6689414978027,
                "longitude": -122.384101867676
              },
              "point": {
                "latitude": 47.6686706542969,
                "longitude": -122.384101867676
              },
              "address": {
                "formattedAddress": "2044 NW Market St, Seattle, WA, 98107",
                "streetAddress": "2044 NW Market St",
                "locality": "Seattle",
                "adminDistrict": "WA",
                "postalCode": "98107",
                "countryRegion": "US",
                "neighborhood": "Ballard"
              },
              "telephone": "(206) 781-2229"
            },
            {
              "type": "LocalBusiness",
              "id": "https://www.bingapis.com/api/v7/#Places.1",
              "name": "Kimchi House",
              "url": "http://kimchihouseseattle.com/",
              "point": {
                "latitude": 47.6714096069336,
                "longitude": -122.387870788574
              },
              "point": {
                "latitude": 47.6714096069336,
                "longitude": -122.387580871582
              },
              "address": {
                "formattedAddress": "5809 24th Ave NW, Seattle, WA, 98107",
                "streetAddress": "5809 24th Ave NW",
                "locality": "Seattle",
                "adminDistrict": "WA",
                "postalCode": "98107",
                "countryRegion": "US",
                "neighborhood": "Ballard"
              },
              "telephone": "(206) 784-5322"
            },
            {
              "type": "LocalBusiness",
              "id": "https://www.bingapis.com/api/v7/#Places.2",
              "name": "Ghost Light Theatricals",
              "url": "http://ghostlighttheatricals.org/",
              "point": {
                "latitude": 47.6690902709961,
                "longitude": -122.385787963867
              },
              "point": {
                "latitude": 47.6686706542969,
                "longitude": -122.385787963867
              },
              "address": {
                "formattedAddress": "2220 NW Market St Ste 1, Seattle, WA, 98107",
                "streetAddress": "2220 NW Market St Ste 1",
                "locality": "Seattle",
                "adminDistrict": "WA",
                "postalCode": "98107",
                "countryRegion": "US",
                "neighborhood": "Ballard"
              },
              "telephone": "(206) 395-5458"
            },
            {
              "type": "LocalBusiness",
              "id": "https://www.bingapis.com/api/v7/#Places.3",
              "name": "Careys Cinema and More",
              "point": {
                "latitude": 47.6679191589355,
                "longitude": -122.385711669922
              },
              "point": {
                "latitude": 47.668083190918,
                "longitude": -122.385475158691
              },
              "address": {
                "formattedAddress": "5425 Ballard Ave NW, Seattle, WA, 98107",
                "streetAddress": "5425 Ballard Ave NW",
                "locality": "Seattle",
                "adminDistrict": "WA",
                "postalCode": "98107",
                "countryRegion": "US",
                "neighborhood": "Ballard"
              },
              "telephone": "(206) 353-8222"
            }
          ],
          "searchAction": {},
          "total": 4
        }
      ]
    }
  ],
  "statusCode": 200,
  "statusDescription": "OK",
  "traceId": "f7d297ceebba48459010e6203418875a|CO389F482F|7.7.0.0"
}
```

## HTTP Status Codes
> [!NOTE]
> For more details about these HTTP status codes, see [Status Codes and Error Handling](Status%20Codes%20and%20Error%20Handling2.md).

When the request is successful, the following HTTP status code is returned:
- 200

When the request is not successful, the response returns one of the following errors:
- 204
- 400