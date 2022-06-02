---
title: "Local Search | Microsoft Docs"
description: "This article provides API templates, parameters, and examples for Bing Maps Local Search API, which returns a list of business entities centered around a location or a geographic region."
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
https://dev.virtualearth.net/REST/v1/LocalSearch/?query={query}&userLocation={point}&key={BingMapsKey}
```

### Search by Query Restricted to a Bounding Box

Make a Local Search API request based on a string query within the specified bounding box using the `userMapView` parameter.

```url
https://dev.virtualearth.net/REST/v1/LocalSearch/?query={query}&userMapView={lat,lon,lat,lon}&key={BingMapsKey}
```

### Search by Query Restricted to a Circular Region

Make a Local Search API request based on a string query within the specified circular region using the `userCircularMapView` parameter.

```url
https://dev.virtualearth.net/REST/v1/LocalSearch/?query={query}&userCircularMapView={lat,lon,radius}&key={BingMapsKey}
```

### Search by Entity Type

Search for businesses by specifying a comma-separated list of type string IDs at a given location using the `type` parameter. The `userMapView` and `userCircularMapView` parameters can also be used when searching by categories.

```url
https://dev.virtualearth.net/REST/v1/LocalSearch/?type={type_string_id_list}&userLocation={point}&key={BingMapsKey}
```

## API Parameters

|Parameter | Alias | Description | Values |
|----------|:-----:|-------------|--------|
|`query`   | `q`   | **Required, if searching by query**. The query used to search for local entities. | A string that contains information about a location, such as an address or landmark name.<br /><br />*Example:* `query = 1%20Microsoft%20Way` | 
|`type`|  | **Required, if searching by type**. The specified types used to filter the local entities returned by the Local Search API.| A comma-separated list of string type identifiers. See the [list of available Type IDs](../common-parameters-and-types/type-identifiers/index.md)|
|`maxResults`| `maxRes` | **Optional.** Specifies the maximum number of locations to return in the response.  | An integer between 1 and 25. The default value is 5.<br /><br /> *Example*: `maxResults=10`|
|`userCircularMapView` |`ucmv` | **Optional.** A circular geographic region.| A circular region specified by a comma separated list of the latitude and longitude of the center of the circle, and the radius of the circle, in meters. *Example*: `48.604311,-122.981998,5000` |
|`userLocation` | `ul` |**Required if neither `userCircularMapView` nor `userMapView` are provided.** Coordinates for the user's location on Earth. | A comma separated list of the user's location (latitude, longitude) and radius, in meters, representing the confidence in the accuracy of the user's location.<br /><br />*Example*: `48.604311,-122.981998,5000`|
|`userMapView` | `umv`  | **Optional.** A rectangular region (a bounding box). | Specified by a comma separated list of the latitudes and longitudes of two corners of the rectangle, in the following order:<br /><br />- Latitude of the Southwest corner<br />- Longitude of the Southwest corner<br />- Latitude of the Northeast corner<br />- Longitude of the Northeast corner<br /><br /><br /> *Example*: `29.8171041,-122.981995,48.604311,-95.5413725`|

## Response

The Local Search API supports both JSON and XML responses.

### LocalSearch Resource

Successful Local Search API requests return a list of `LocalSearch` resources.

|JSON|XML|Description|
|----|----|----------|
|`entityType`|`EntityType`| The type of local entity, e.g. `Restaurant`.|
|`name`|`Name`|The name of the local entity, e.g. `Yea's Wok`.|
|`Website`|`Website`| If available, the URL for the local entity.|
|`geocodePoints`|`GeoCodePoints`| A container with the latitude and longitude for the local entity; typically the rooftop of the entity.|
|`point` | `Point` | A container with a latitude and longitude suitable for providing directions to the local entity. |
|`address`|`Address`| A container including the `formattedAddress`, `streetAddress`, `locality`, `adminDistrict`, `postalCode`, `countryRegion`, and `neighborhood` fields for the local entity.|
|`PhoneNumber`|`PhoneNumber`| If available, the telephone number for the local entity.|


## Examples

### Search by Query for local coffee shops in Downtown Seattle

Pioneer Square, in downtown Seattle, is located at: `47.602038, -122.333964`. Setting the parameter `query` to `coffee` gives us the following Local Search API URL:

```url
https://dev.virtualearth.net/REST/v1/LocalSearch/?query=coffee&userLocation=47.602038,-122.333964&key={BingMapsKey}
```

The JSON response:

```json
{
    "authenticationResultCode": "ValidCredentials",
    "brandLogoUri": "http://dev.virtualearth.net/Branding/logo_powered_by.png",
    "copyright": "Copyright © 2021 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",
    "resourceSets": [
        {
            "estimatedTotal": 10,
            "resources": [
                {
                    "__type": "SearchResult:http://schemas.microsoft.com/search/local/ws/rest/v1",
                    "name": "Starbucks",
                    "point": {
                        "type": "Point",
                        "coordinates": [
                            47.603889465332031,
                            -122.33554077148437
                        ]
                    },
                    "Address": {
                        "addressLine": "823 1st Ave",
                        "adminDistrict": "WA",
                        "countryRegion": "US",
                        "formattedAddress": "823 1st Ave, Seattle, WA, 98104",
                        "locality": "Seattle",
                        "postalCode": "98104"
                    },
                    "PhoneNumber": "(206) 340-9184",
                    "Website": "http://www.starbucks.com/store/16645/",
                    "entityType": "Restaurant",
                    "geocodePoints": [
                        {
                            "type": "Point",
                            "coordinates": [
                                47.603809356689453,
                                -122.33565521240234
                            ],
                            "calculationMethod": "Rooftop",
                            "usageTypes": [
                                "Display"
                            ]
                        }
                    ]
                },
                {
                    "__type": "SearchResult:http://schemas.microsoft.com/search/local/ws/rest/v1",
                    "name": "Starbucks",
                    "point": {
                        "type": "Point",
                        "coordinates": [
                            47.599094390869141,
                            -122.33290863037109
                        ]
                    },
                    "Address": {
                        "addressLine": "400 Occidental Ave S",
                        "adminDistrict": "WA",
                        "countryRegion": "US",
                        "formattedAddress": "400 Occidental Ave S, Seattle, WA, 98104",
                        "locality": "Seattle",
                        "postalCode": "98104"
                    },
                    "PhoneNumber": "(206) 624-2561",
                    "Website": "http://www.starbucks.com/",
                    "entityType": "Restaurant",
                    "geocodePoints": [
                        {
                            "type": "Point",
                            "coordinates": [
                                47.599094390869141,
                                -122.33263397216797
                            ],
                            "calculationMethod": "Rooftop",
                            "usageTypes": [
                                "Display"
                            ]
                        }
                    ]
                },
                {
                    "__type": "SearchResult:http://schemas.microsoft.com/search/local/ws/rest/v1",
                    "name": "Starbucks",
                    "point": {
                        "type": "Point",
                        "coordinates": [
                            47.605205535888672,
                            -122.33363342285156
                        ]
                    },
                    "Address": {
                        "addressLine": "999 3rd Ave",
                        "adminDistrict": "WA",
                        "countryRegion": "US",
                        "formattedAddress": "999 3rd Ave, Seattle, WA, 98104",
                        "locality": "Seattle",
                        "postalCode": "98104"
                    },
                    "PhoneNumber": "(206) 748-0058",
                    "Website": "http://www.starbucks.com/",
                    "entityType": "Restaurant",
                    "geocodePoints": [
                        {
                            "type": "Point",
                            "coordinates": [
                                47.605247497558594,
                                -122.33421325683594
                            ],
                            "calculationMethod": "Rooftop",
                            "usageTypes": [
                                "Display"
                            ]
                        }
                    ]
                },
                {
                    "__type": "SearchResult:http://schemas.microsoft.com/search/local/ws/rest/v1",
                    "name": "Starbucks",
                    "point": {
                        "type": "Point",
                        "coordinates": [
                            47.605587005615234,
                            -122.33090972900391
                        ]
                    },
                    "Address": {
                        "addressLine": "800 5th Ave",
                        "adminDistrict": "WA",
                        "countryRegion": "US",
                        "formattedAddress": "800 5th Ave, Seattle, WA, 98104",
                        "locality": "Seattle",
                        "postalCode": "98104"
                    },
                    "PhoneNumber": "(206) 623-3425",
                    "Website": "https://www.starbucks.com/store-locator/store/89253/",
                    "entityType": "Restaurant",
                    "geocodePoints": [
                        {
                            "type": "Point",
                            "coordinates": [
                                47.605548858642578,
                                -122.33027648925781
                            ],
                            "calculationMethod": "Rooftop",
                            "usageTypes": [
                                "Display"
                            ]
                        }
                    ]
                },
                {
                    "__type": "SearchResult:http://schemas.microsoft.com/search/local/ws/rest/v1",
                    "name": "Elm Coffee Roasters",
                    "point": {
                        "type": "Point",
                        "coordinates": [
                            47.600246429443359,
                            -122.33158874511719
                        ]
                    },
                    "Address": {
                        "addressLine": "240 2nd Ave S Ste 103",
                        "adminDistrict": "WA",
                        "countryRegion": "US",
                        "formattedAddress": "240 2nd Ave S Ste 103, Seattle, WA, 98104",
                        "locality": "Seattle",
                        "postalCode": "98104"
                    },
                    "PhoneNumber": "(206) 445-7808",
                    "Website": "https://elmcoffeeroasters.com/",
                    "entityType": "Restaurant",
                    "geocodePoints": [
                        {
                            "type": "Point",
                            "coordinates": [
                                47.600181579589844,
                                -122.33110046386719
                            ],
                            "calculationMethod": "Rooftop",
                            "usageTypes": [
                                "Display"
                            ]
                        }
                    ]
                },
                {
                    "__type": "SearchResult:http://schemas.microsoft.com/search/local/ws/rest/v1",
                    "name": "Starbucks",
                    "point": {
                        "type": "Point",
                        "coordinates": [
                            47.606231689453125,
                            -122.33615875244141
                        ]
                    },
                    "Address": {
                        "addressLine": "1191 2nd Ave",
                        "adminDistrict": "WA",
                        "countryRegion": "US",
                        "formattedAddress": "1191 2nd Ave, Seattle, WA, 98101",
                        "locality": "Seattle",
                        "postalCode": "98101"
                    },
                    "PhoneNumber": "(206) 652-8924",
                    "Website": "http://www.starbucks.com/",
                    "entityType": "Restaurant",
                    "geocodePoints": [
                        {
                            "type": "Point",
                            "coordinates": [
                                47.606266021728516,
                                -122.33662414550781
                            ],
                            "calculationMethod": "Rooftop",
                            "usageTypes": [
                                "Display"
                            ]
                        }
                    ]
                },
                {
                    "__type": "SearchResult:http://schemas.microsoft.com/search/local/ws/rest/v1",
                    "name": "Starbucks",
                    "point": {
                        "type": "Point",
                        "coordinates": [
                            47.604999542236328,
                            -122.33952331542969
                        ]
                    },
                    "Address": {
                        "addressLine": "1101 Alaskan Way",
                        "adminDistrict": "WA",
                        "countryRegion": "US",
                        "formattedAddress": "1101 Alaskan Way, Seattle, WA, 98101",
                        "locality": "Seattle",
                        "postalCode": "98101"
                    },
                    "PhoneNumber": "(206) 554-7060",
                    "Website": "https://www.starbucks.com/store-locator/store/16417/",
                    "entityType": "Restaurant",
                    "geocodePoints": [
                        {
                            "type": "Point",
                            "coordinates": [
                                47.6048583984375,
                                -122.33982849121094
                            ],
                            "calculationMethod": "Rooftop",
                            "usageTypes": [
                                "Display"
                            ]
                        }
                    ]
                },
                {
                    "__type": "SearchResult:http://schemas.microsoft.com/search/local/ws/rest/v1",
                    "name": "Starbucks",
                    "point": {
                        "type": "Point",
                        "coordinates": [
                            47.6070671081543,
                            -122.335693359375
                        ]
                    },
                    "Address": {
                        "addressLine": "1201 3rd Ave",
                        "adminDistrict": "WA",
                        "countryRegion": "US",
                        "formattedAddress": "1201 3rd Ave, Seattle, WA, 98101",
                        "locality": "Seattle",
                        "postalCode": "98101"
                    },
                    "PhoneNumber": "(206) 467-3079",
                    "Website": "https://www.starbucks.com/store-locator/store/89252/",
                    "entityType": "Restaurant",
                    "geocodePoints": [
                        {
                            "type": "Point",
                            "coordinates": [
                                47.6070671081543,
                                -122.335693359375
                            ],
                            "calculationMethod": "Rooftop",
                            "usageTypes": [
                                "Display"
                            ]
                        }
                    ]
                },
                {
                    "__type": "SearchResult:http://schemas.microsoft.com/search/local/ws/rest/v1",
                    "name": "Cherry Street Coffee House",
                    "point": {
                        "type": "Point",
                        "coordinates": [
                            47.602653503417969,
                            -122.33394622802734
                        ]
                    },
                    "Address": {
                        "addressLine": "103 Cherry St",
                        "adminDistrict": "WA",
                        "countryRegion": "US",
                        "formattedAddress": "103 Cherry St, Seattle, WA, 98104",
                        "locality": "Seattle",
                        "postalCode": "98104"
                    },
                    "PhoneNumber": "(206) 621-9372",
                    "Website": "http://www.cherryst.com/",
                    "entityType": "Restaurant",
                    "geocodePoints": [
                        {
                            "type": "Point",
                            "coordinates": [
                                47.602653503417969,
                                -122.33394622802734
                            ],
                            "calculationMethod": "Rooftop",
                            "usageTypes": [
                                "Display"
                            ]
                        }
                    ]
                },
                {
                    "__type": "SearchResult:http://schemas.microsoft.com/search/local/ws/rest/v1",
                    "name": "Slate Coffee Roasters",
                    "point": {
                        "type": "Point",
                        "coordinates": [
                            47.602470397949219,
                            -122.33266448974609
                        ]
                    },
                    "Address": {
                        "addressLine": "602 2nd Ave",
                        "adminDistrict": "WA",
                        "countryRegion": "US",
                        "formattedAddress": "602 2nd Ave, Seattle, WA, 98104",
                        "locality": "Seattle",
                        "postalCode": "98104"
                    },
                    "PhoneNumber": "(206) 235-6565",
                    "Website": "http://www.slatecoffee.com/",
                    "entityType": "Restaurant",
                    "geocodePoints": [
                        {
                            "type": "Point",
                            "coordinates": [
                                47.602497100830078,
                                -122.33243560791016
                            ],
                            "calculationMethod": "Rooftop",
                            "usageTypes": [
                                "Display"
                            ]
                        }
                    ]
                }
            ]
        }
    ],
    "statusCode": 200,
    "statusDescription": "OK",
    "traceId": "801b6e061d3e4c838ed631c941280692|CO0000112B|0.0.0.0"
}
```

### Search for coffee in Downtown Seattle by Type

Instead of searching by a query, the Local Search API allows us to search at a location for local entities what match a comma-separated list of string type identifiers. For example, looking at the available [Type Identifiers](../common-parameters-and-types/type-identifiers/index.md), we find that the best match for "coffee" is the string ID `CoffeeAndTea`. So we set the parameter `type` to `CoffeeAndTea`.

Here is the URL, using the same location the previous example:

```url
https://dev.virtualearth.net/REST/v1/LocalSearch/?type=CoffeeAndTea&userLocation=47.602038,-122.333964&o=xml&key={BingMapsKey}
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

Searching the string [Type Identifiers](../common-parameters-and-types/type-identifiers/index.md), we find two matches for our type strings: `MovieTheaters` and `KoreanRestaurants`. So we set the parameter `type` to `MovieTheaters,KoreanRestaurants`, and we specify the `userCircularMapView`  instead of the `userLocation` parameter.

The resulting URL is:

```url
https://dev.virtualearth.net/REST/v1/LocalSearch/?type=MovieTheaters,KoreanRestaurants&userCircularMapView=47.668979,-122.387562,300&key={BingMapsKey}
```   

And the JSON response:

```json
{
    "authenticationResultCode": "ValidCredentials",
    "brandLogoUri": "http://dev.virtualearth.net/Branding/logo_powered_by.png",
    "copyright": "Copyright © 2021 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",
    "resourceSets": [
        {
            "estimatedTotal": 4,
            "resources": [
                {
                    "__type": "SearchResult:http://schemas.microsoft.com/search/local/ws/rest/v1",
                    "name": "Majestic Bay Theatres",
                    "point": {
                        "type": "Point",
                        "coordinates": [
                            47.668788909912109,
                            -122.38408660888672
                        ]
                    },
                    "Address": {
                        "addressLine": "2044 NW Market St",
                        "adminDistrict": "WA",
                        "countryRegion": "US",
                        "formattedAddress": "2044 NW Market St, Seattle, WA, 98107",
                        "locality": "Seattle",
                        "postalCode": "98107"
                    },
                    "PhoneNumber": "(206) 781-2229",
                    "Website": "https://majesticbay.com/",
                    "entityType": "LocalBusiness",
                    "geocodePoints": [
                        {
                            "type": "Point",
                            "coordinates": [
                                47.668788909912109,
                                -122.38408660888672
                            ],
                            "calculationMethod": "Rooftop",
                            "usageTypes": [
                                "Display"
                            ]
                        }
                    ]
                },
                {
                    "__type": "SearchResult:http://schemas.microsoft.com/search/local/ws/rest/v1",
                    "name": "Kimchi House",
                    "point": {
                        "type": "Point",
                        "coordinates": [
                            47.671367645263672,
                            -122.38759613037109
                        ]
                    },
                    "Address": {
                        "addressLine": "5809 24th Ave NW",
                        "adminDistrict": "WA",
                        "countryRegion": "US",
                        "formattedAddress": "5809 24th Ave NW, Seattle, WA, 98107",
                        "locality": "Seattle",
                        "postalCode": "98107"
                    },
                    "PhoneNumber": "(206) 784-5322",
                    "Website": "http://kimchihouseseattle.com/",
                    "entityType": "Restaurant",
                    "geocodePoints": [
                        {
                            "type": "Point",
                            "coordinates": [
                                47.671379089355469,
                                -122.38784790039062
                            ],
                            "calculationMethod": "Rooftop",
                            "usageTypes": [
                                "Display"
                            ]
                        }
                    ]
                },
                {
                    "__type": "SearchResult:http://schemas.microsoft.com/search/local/ws/rest/v1",
                    "name": "Ann’s Teriyaki",
                    "point": {
                        "type": "Point",
                        "coordinates": [
                            47.668701171875,
                            -122.38677215576172
                        ]
                    },
                    "Address": {
                        "addressLine": "2246 NW Market St",
                        "adminDistrict": "WA",
                        "countryRegion": "US",
                        "formattedAddress": "2246 NW Market St, Seattle, WA, 98107",
                        "locality": "Seattle",
                        "postalCode": "98107"
                    },
                    "PhoneNumber": "(206) 789-5838",
                    "Website": null,
                    "entityType": "Restaurant",
                    "geocodePoints": [
                        {
                            "type": "Point",
                            "coordinates": [
                                47.668891906738281,
                                -122.38676452636719
                            ],
                            "calculationMethod": "Rooftop",
                            "usageTypes": [
                                "Display"
                            ]
                        }
                    ]
                },
                {
                    "__type": "SearchResult:http://schemas.microsoft.com/search/local/ws/rest/v1",
                    "name": "Careys Cinema and More",
                    "point": {
                        "type": "Point",
                        "coordinates": [
                            47.668243408203125,
                            -122.38571929931641
                        ]
                    },
                    "Address": {
                        "addressLine": "5425 Ballard Ave NW",
                        "adminDistrict": "WA",
                        "countryRegion": "US",
                        "formattedAddress": "5425 Ballard Ave NW, Seattle, WA, 98107",
                        "locality": "Seattle",
                        "postalCode": "98107"
                    },
                    "PhoneNumber": "(206) 353-8222",
                    "Website": null,
                    "entityType": "LocalBusiness",
                    "geocodePoints": [
                        {
                            "type": "Point",
                            "coordinates": [
                                47.668281555175781,
                                -122.38566589355469
                            ],
                            "calculationMethod": "Rooftop",
                            "usageTypes": [
                                "Display"
                            ]
                        }
                    ]
                }
            ]
        }
    ],
    "statusCode": 200,
    "statusDescription": "OK",
    "traceId": "aac0c5ac12214da99286da79724c34ec|CO0000112C|0.0.0.0"
}
```

## HTTP Status Codes

[!INCLUDE [get-status-code-note](../../includes/get-status-code-note.md)]


When the request is successful, the following HTTP status code is returned:
- 200

When the request is not successful, the response returns one of the following errors:
- 204
- 400
