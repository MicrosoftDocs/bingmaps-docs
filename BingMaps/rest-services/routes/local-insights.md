---
title: "Local Insights | Microsoft Docs"
ms.custom: ""
ms.date: "12/12/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 64c43775-3911-4c76-a0b4-32dc5824a258
caps.latest.revision: 4
author: "v-chrfr"
ms.author: "v-chrfr"
manager: "stevelom"
ms.service: "bing-maps"
---

# Local Insights

The Bing Maps Local Insights API returns a list of local entities within the specified maximum driving time or distance traveled from a specified point on Earth. The API returns different types of entities as specified by the string type IDs; these types can be found on the [Type Identifiers](../common-parameters-and-types/type-identifiers/index.md) page. In each response, a maximum of 200 total entities is returned. Presently, the Local Insights API is only available in the US.

## API Templates

> [!NOTE]
> The Local Insights API supports both synchronous and asynchronous requests. If using Local Insights with traffic information, we strongly recommended that asynchronous requests are used.


### Synchronous Requests

Successful synchronous Local Insights API calls return a `LocalInsights` Response in either JSON or XML format.

#### Get Local Insights By Travel Time

Get a list of local insights at a waypoint – specified either as a coordinate or an address query – with a maximal traveling time radius specified by the `maxTime` parameter. Specify the kind of entities returned with a comma separated list of type IDs with the `type` parameter. The time unit is specified with `timeUnit` as either `minute` or `second` and the only permitted value of `optimize` is `time`.

```url
http://dev.virtualearth.net/REST/v1/Routes/LocalInsights?waypoint={coordinate_or_query}&maxTime={MaxTime}&timeUnit={second_or_minute}&type={type_string_ids}&key={BingMapsKey}
```

#### Get Local Insights By Travel Distance

Get a list of local insights at a waypoint – specified either as a coordinate pair or an address query – with a maximal traveling distance radius specified by the `maxDistance` parameter. Specify the kind of entities returned with a comma separated list of type IDs with the `type` parameter. The distance unit is specified with `distanceUnit` as either `mile` or `kilometer` and the only permitted value of `optimize` is `distance`. 

```url
http://dev.virtualearth.net/REST/v1/Routes/LocalInsights?waypoint={coordinate_or_query}& maxDistance={MaxDistance}&distanceUnit={mile_or_kilometer}&type={type_string_ids}&key={BingMapsKey}
```

> [!NOTE]
> 
> Traffic information is currently not used to optimize distance traveled.

### Asynchronous Requests

The URL templates for asynchronous requests are almost identical to the respective synchronous URL requests. Unlike with the synchronous URL requests, asynchronous URL requests return a `RouteProxyAsyncResult` response.

If successful, this response contains a field called `requestID` which is a unique ID for the asynchronous request and a field called `callbackURL` which contains a URL to check if the response is finished. The `callbackURL` can also be created from the `requestID` value, as shown below in the __Get Status of Asynchronous Request by RequestID__ template below.

The response of the callback URL is a `RouteProxyAsyncResult` response. If the asynchronous request if finished, then the field `isCompleted` in the response will be `true` and the response will contain the field `resultURL`. The result URL will return a LocalInsights Response with a list of local insights.

See the [Asynchronous Requests](../common-parameters-and-types/asynchronous-requests.md) documentation for more information about how to make asynchronous requests.

#### Asynchronous Get Local Insights by Time

Asynchronous GET Local Insights call by time.

```url
http://dev.virtualearth.net/REST/v1/Routes/LocalInsightsAsync?waypoint={coordinate_or_query}& maxTime={MaxTime}&timeUnit={second_or_minute}&type={type_string_ids}&key={BingMapsKey}
```

#### Asynchronous Get Local Insights by Distance

Asynchronous GET Local Insights call by distance.

```url
http://dev.virtualearth.net/REST/v1/Routes/LocalInsightsAsync?waypoint={coordinate_or_query}& maxDistance={MaxDistance}&distanceUnit={mile_or_kilometer}&type={type_string_ids}&key={BingMapsKey}
```

#### Get Status of Asynchronous Request by RequestID

Get a RouteProxyAsyncResult response containing the status of an asynchronous URL request by specifying the `requestID`.

```url
http://dev.virtualearth.net/REST/v1/Routes/LocalInsightsAsyncCallback?requestId={request_id}&key={BingMapsKey}
```

> [!NOTE]
>
> Use the Distance Matrix API to calculate distances between returned entities.

## API Parameters


|Parameter  |Alias  |Description  |Values  |
|:-----:|:---:|---------|---------|
|`waypoint` |`wp`| **Required**. The query or coordinates for a location around which the isochrone is created. |Either a point or an address query.<br /><br />*Examples*: <br /><br />- `waypoint = 47.5,-122`<br />- `waypoint = 1%20Microsoft%20Way%20Redmond%20WA` |
|`maxTime`||**Required, if `optimize` is `Time` or `TimeWithTraffic`**. The longest possible travel time used to generate the isochrone.<br />**Note**: Cannot be used when `maxDistance` is specified.|Any positive integer less than or equal to the maximum time, which is 60 minutes.<br />Note: The unit of time is specified with the `timeUnit` parameter.<br /><br />*Example*: `maxTime = 30`|
|`timeUnit` |`tu` |**Optional**. The unit of time for the parameter `maxTime`. |A string: either `second` or `minute`.<br /><br />Default: `second`|
|`maxDistance`  |`maxDist` | **Required, if `travelMode` is Driving or Walking.** The longest possible distance used define the geographic region in which to search for local entities.<br /><br />**Note**: Distance-based Local Insight API calls are unavailable for transit.<br /><br />**Note**: Cannot be used when `maxTime` is specified.|Any positive integer less than or equal to 50 miles.<br /><br />*Example*: `maxDistance = 40` |
|`distanceUnit` |`du` | **Optional**. The unit of distance for the `maxDistance` parameter. |Possible values:<br /><br />-	`mile` or `mi`<br />-	`kilometer` or `km`<br /><br />Default: `kilometer`|
|`type`||**Required**. A comma separated list of type IDs. | A comma separated list of string type IDs. See the [Type IDs](../common-parameters-and-types/type-identifiers/index.md) for the complete list of possible type ID values.<br />*Example*: `type = MovieTheaters,Parks` |
|`dateTime` |`dt` | **Optional, available only if `travelModel` is Driving**. The `datetime` parameter identifies the desired departure time used to return the list of local entities within the specified maximum driving time as specified using the `maxTime` parameter.|A string that contains the date and time formatted as a [DateTime](https://msdn.microsoft.com/library/03ybds8y.aspx) value. For information about the string representation options for [DateTime values, see DateTime.Parse Method (String)](https://msdn.microsoft.com/library/1k1skd40.aspx).<br />*Examples*:<br />- `dateTime = 03/01/2011 05:42:00`<br />- `dateTime = 05:42:00` [assumes the current day]<br />- `dateTime=03/01/2011` [assumes the current time]         |
|`optimize` |`optmz` |**Optional**. Specifies what parameters to use to optimize the isochrone route.| One of the following values:<br />- `distance`: The route is calculated to minimize the distance. Traffic information is not used. Use with maxDistance.<br />- `time`: The route is calculated to minimize the time. Traffic information is not used. Use with maxTime.<br /><br />Default: `time`<br /><br />*Example*: `optimize = time`.|
|`travelMode` |`mode`|**Optional**. Indicates the which routing profile to snap the points to.| Possible values:<br /><br />- `driving`<br />- `walking`<br />- `transit`<br /><br />Default: `driving`<br />*Example*: `travelMode = walking`.|
<!--|`startTime`| | __Optional for Driving, but required if making asynchronous Driving request__. Specifies the start or departure time of the matrix to calculate and uses predictive traffic data. | A date string in a format that can be parsed by [DateTimeOffset.Parse](https://msdn.microsoft.com/library/bb351654.aspx). This option is only supported when the travel mode is set to driving.<br /><br />*Example*: `startTime = 2017-06-15T8:00:00-07:00`| -->
## Response

See [Local Insights Data](local-insights-data.md).

## Examples

### Get Local Insights by Driving Time by Query

This example gets a list of local insights that are either Movie Theaters or Department Stores within a thirty minute drive of the Redmond Microsoft Campus. Two string types are used: `DepartmentStores` and `MovieTheaters`.

```url
http://dev.virtualearth.net/REST/V1/Routes/LocalInsights?Waypoint=1%20Microsoft%20Way,Redmond,WA&TravelMode=Driving&Optimize=time&MaxTime=30&TimeUnit=Minute&type=DepartmentStores,MovieTheaters&key={BingMapsKey}
```

Here is the successful JSON response.

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
          "__type": "LocalInsightsResponse:http://schemas.microsoft.com/search/local/ws/rest/v1",
          "typeResults": [
            {
              "typeName": "Department Stores",
              "typeSummary": "20 Department Stores in 30 Minutes by Driving",
              "entities": [
                {
                  "entityName": "Sears Stores",
                  "latitude": 47.630211,
                  "longitude": -122.141318
                },
                {
                  "entityName": "Fred Meyer",
                  "latitude": 47.62886852137511,
                  "longitude": -122.14475288604169
                },
                {
                  "entityName": "Daiso Japan",
                  "latitude": 47.620109,
                  "longitude": -122.130684
                },
                {
                  "entityName": "Ben Franklin Crafts",
                  "latitude": 47.6745642853546,
                  "longitude": -122.129096602237
                },
                {
                  "entityName": "HomeGoods",
                  "latitude": 47.61322,
                  "longitude": -122.18475
                },
                {
                  "entityName": "Costco Wholesale",
                  "latitude": 47.68118,
                  "longitude": -122.1815
                },
                {
                  "entityName": "Costco Wholesale Kirkland Warehouse",
                  "latitude": 47.68073998682604,
                  "longitude": -122.18175410738384
                },
                {
                  "entityName": "Revolve Consignment",
                  "latitude": 47.53507,
                  "longitude": -122.03667
                },
                {
                  "entityName": "Shoprite",
                  "latitude": 47.6224741119901,
                  "longitude": -122.312563286076
                },
                {
                  "entityName": "Daiso",
                  "latitude": 47.59634,
                  "longitude": -122.32614
                },
                {
                  "entityName": "Zara",
                  "latitude": 47.61188,
                  "longitude": -122.33729
                },
                {
                  "entityName": "Bargain Plaza",
                  "latitude": 47.50071935713182,
                  "longitude": -122.17796977901406
                },
                {
                  "entityName": "Fjallraven",
                  "latitude": 47.628875696097,
                  "longitude": -122.358053052728
                },
                {
                  "entityName": "Rama Deli and Market",
                  "latitude": 47.61655,
                  "longitude": -122.35243
                },
                {
                  "entityName": "USA Laptops Sreens Inc",
                  "latitude": 47.72458,
                  "longitude": -122.34086
                },
                {
                  "entityName": "Westfield Southcenter Mall",
                  "latitude": 47.458834,
                  "longitude": -122.258126
                },
                {
                  "entityName": "Westfield Southcenter",
                  "latitude": 47.45813,
                  "longitude": -122.25599
                },
                {
                  "entityName": "Quilts Etc",
                  "latitude": 47.45813,
                  "longitude": -122.25599
                },
                {
                  "entityName": "India Plaza",
                  "latitude": 47.46574,
                  "longitude": -122.28955
                },
                {
                  "entityName": "Eddie Bauer",
                  "latitude": 47.490105,
                  "longitude": -121.796338
                }
              ]
            },
            {
              "typeName": "Movie Theaters",
              "typeSummary": "2 Movie Theaters in 30 Minutes by Driving",
              "entities": [
                {
                  "entityName": "SecondStory Repertory",
                  "latitude": 47.66998,
                  "longitude": -122.11959
                },
                {
                  "entityName": "AMC Kent Station 14",
                  "latitude": 47.384842653844814,
                  "longitude": -122.23544404894568
                }
              ]
            }
          ],
          "origin": {
            "latitude": 47.640068,
            "longitude": -122.129858
          }
        }
      ]
    }
  ],
  "statusCode": 200,
  "statusDescription": "OK",
  "traceId": "40b9d0d37c344ce99e75a80d62e5112a|DAPZHU-DEV|7.7.0.0|Ref A: 814E90439D604CA5A5995AA54709F5EC Ref B: CO1EDGE0420 Ref C: 2018-10-15T21:44:55Z"
}
```

### Get Local Insights by Driving Time by Point

This example returns local entities at a point in Edmonds, Washington State, `47.811091,-122.369512`, within twenty minutes driving time. In this example, the local entities are parks and parking lots, using the Type IDs `Parks` and `Parking`.

```url
https://dev.virtualearth.net/REST/V1/Routes/LocalInsights?key={BingMapsKey}&waypoint=47.811091,-122.369512&travelMode=Driving&optimize=time&MaxTime=20&TimeUnit=Minute&type=parks,parking&o=xml
```

And the XML response:

```xml
<Response>
    <Copyright>Copyright © 2018 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>
    <BrandLogoUri>https://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>
    <StatusCode>200</StatusCode>
    <StatusDescription>OK</StatusDescription>
    <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>
    <TraceId>f003e095ab82470e88e3cbc5983b0d5e|MW10000A84|7.7.0.0</TraceId>
    <ResourceSets>
        <ResourceSet>
            <EstimatedTotal>1</EstimatedTotal>
            <Resources>
                <Resource xsi:type="LocalInsightsResponse">
                    <Origin>
                        <Latitude>47.811091</Latitude>
                        <Longitude>-122.369512</Longitude>
                    </Origin>
                    <CategoryTypeResults>
                        <CategoryTypeResult>
                            <CategoryName>Parks</CategoryName>
                            <CategorySummary>5 Parks in 20 Minutes by Driving</CategorySummary>
                            <Entities>
                                <LocalInsightsEntity>
                                    <EntityName>Richmond Beach Center Park</EntityName>
                                    <Latitude>47.77205339744016</Latitude>
                                    <Longitude>-122.38522949061662</Longitude>
                                </LocalInsightsEntity>
                                <LocalInsightsEntity>
                                    <EntityName>Meadowdale Playfields</EntityName>
                                    <Latitude>47.847783158175339</Latitude>
                                    <Longitude>-122.32521969622377</Longitude>
                                </LocalInsightsEntity>
                                <LocalInsightsEntity>
                                    <EntityName>Drug Rehab Lake Forest Park</EntityName>
                                    <Latitude>47.7546081542969</Latitude>
                                    <Longitude>-122.277923583984</Longitude>
                                </LocalInsightsEntity>
                                <LocalInsightsEntity>
                                    <EntityName>Lake Forest Park City Hall</EntityName>
                                    <Latitude>47.753910811869261</Latitude>
                                    <Longitude>-122.27754771953607</Longitude>
                                </LocalInsightsEntity>
                                <LocalInsightsEntity>
                                    <EntityName>Dogwood Play Park</EntityName>
                                    <Latitude>47.72104</Latitude>
                                    <Longitude>-122.29211</Longitude>
                                </LocalInsightsEntity>
                            </Entities>
                        </CategoryTypeResult>
                        <CategoryTypeResult>
                            <CategoryName>Parking</CategoryName>
                            <CategorySummary>0 Parking in 20 Minutes by Driving</CategorySummary>
                            <Entities/>
                        </CategoryTypeResult>
                    </CategoryTypeResults>
                </Resource>
            </Resources>
        </ResourceSet>
    </ResourceSets>
</Response>
```

### Get Local Insights by Driving Distance by Point

This example uses the same point in Edmonds as in the last example, but instead search for parks and parking entities by driving distance. In this example, the response returns entities within 10 miles of the specified point. 

```url
https://dev.virtualearth.net/REST/V1/Routes/LocalInsights?key={BingMapsKey}&waypoint=47.811091,-122.369512&travelMode=Driving&optimize=time&MaxTime=20&TimeUnit=Minute&type=parks,parking
```

Here is the JSON response:

```json
{
  "authenticationResultCode": "ValidCredentials",
  "brandLogoUri": "https://dev.virtualearth.net/Branding/logo_powered_by.png",
  "copyright": "Copyright © 2018 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",
  "resourceSets": [
    {
      "estimatedTotal": 1,
      "resources": [
        {
          "__type": "LocalInsightsResponse:http://schemas.microsoft.com/search/local/ws/rest/v1",
          "categoryTypeResults": [
            {
              "categoryTypeName": "Parks",
              "categoryTypeSummary": "5 Parks in 10 Miles by Driving",
              "entities": [
                {
                  "entityName": "Richmond Beach Center Park",
                  "latitude": 47.77205339744016,
                  "longitude": -122.38522949061662
                },
                {
                  "entityName": "Meadowdale Playfields",
                  "latitude": 47.84778315817534,
                  "longitude": -122.32521969622377
                },
                {
                  "entityName": "Drug Rehab Lake Forest Park",
                  "latitude": 47.7546081542969,
                  "longitude": -122.277923583984
                },
                {
                  "entityName": "Lake Forest Park City Hall",
                  "latitude": 47.75391081186926,
                  "longitude": -122.27754771953607
                },
                {
                  "entityName": "Dogwood Play Park",
                  "latitude": 47.72104,
                  "longitude": -122.29211
                }
              ]
            },
            {
              "categoryTypeName": "Parking",
              "categoryTypeSummary": "0 Parking in 10 Miles by Driving",
              "entities": []
            }
          ],
          "origin": {
            "latitude": 47.811091,
            "longitude": -122.369512
          }
        }
      ]
    }
  ],
  "statusCode": 200,
  "statusDescription": "OK",
  "traceId": "7125b438817b4a7bb68470a1fb06a1a1|MW10000A85|7.7.0.0"
}
```
