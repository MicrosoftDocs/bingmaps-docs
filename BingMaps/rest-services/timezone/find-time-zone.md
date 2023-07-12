---
title: Find Time Zone | Microsoft Docs
description: Given a pair of coordinates or a place name query, the Bing Maps Time Zone API will return local time zone and DST information.
ms.custom: 
ms.date: 12/11/2018
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
ms.topic: article
ms.assetid: fa146e18-716a-49b7-88b3-17f78e617245
caps.latest.revision: 6
ms.author: v-munksteve
manager: stevelom
ms.service: bing-maps
---

# Find Time Zone

The Bing Maps Time Zone API makes it easy to retrieve time zone information for any point on Earth. Given a pair of coordinates or a place name query, the Time Zone API will return local time zone and daylight savings (DST) information for that location. Note that time zone data for bodies of water, like oceans or seas, is not supported.


## API Templates

There are two Time Zone API operations to retrieve time zone information for a location.

> [!NOTE]
>
> These templates support both HTTP and HTTPS.

### Time Zone from Location Point

Given a specified point of latitude and longitude coordinates, like `point = 47,-122`, the Time Zone API returns information about the time zone for that location.

```url
https://dev.virtualearth.net/REST/v1/TimeZone/{point}?datetime={datetime_utc}&key={BingMapsKey}
``` 

### Time Zone from Location Name

Given a query for a location, like `query = Bellevue, WA`, the Time Zone API finds that location and then returns information about the time zone for that location.

To avoid ambiguity when processing location names, make sure to fully qualify the location name with state (administrative region) and country/region names.

```url
https://dev.virtualearth.net/REST/v1/TimeZone/?query={query}&datetime={datetime_utc}&key={BingMapsKey}
```

## Template Parameters

|Parameters |Alias  |Descriptions  |Values |
|:------|:----:|---------|---------|
|`point` | | **Required for getting Time Zone by Location Point.** The coordinates of the location for which you want the entities situated.<br /><br />**Note:** The `point` and `query` parameters are mutually exclusive. Only one of these parameters can be specified in the same call. | A point on the Earth specified by a latitude and longitude. For more information, see the definition of Point in [Location and Area Types](../common-parameters-and-types/location-and-area-types.md). <br /><br />Use the following ranges of values:<br /><br />- `Latitude` (degrees): `[-90, +90]`<br />- `Longitude` (degrees): `[-180, +180]`<br /><br />*Example*: `47.610679194331169,-122.10788659751415`| 
|`query` |`q` | **Required for getting Time Zone by Query.** A string containing information about the location, including address, locality, and postal code.<br /><br />**Note:** The `point` and `query` parameters are mutually exclusive. Only one of these parameters can be specified in the same call. | To properly identify the given location, provide a fully qualified location e.g. place name, administrative region and country/region name.<br /><br />**Note:**	To avoid ambiguous results specify a qualified location name. For example, there are two Vancouvers, one in British Columbia, Canada and the other in Washington state, USA, so instead of the query "Vancouver" use either "Vancouver, BC" or "Vancouver, WA" (alternatively: "Vancouver, Canada" or "Vancouver, USA"). If no such qualification is present and multiple locations of the given name are detected, then more likely than not the most popular location is returned. <br /><br />**Note:** Please use full country/region names or [official ISO country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) in queries, e.g., use either `Capetown, ZA` or `Captetown, South Africa` instead of `Capetown, SA`. <br /><br />*Examples*:<br /><br />- `query = bellevue,wa,us`<br />- `q = 98052,wa`|
|`dateTime` |`dt`| **Optional.** The UTC date time string for the specified location. The date must be specified to apply the correct DST. |  The date time string must be in UTC format. If the date is not included, the returned time zone information may be incorrect.<br /><br />*Example*: `2018-05-15T13:14:15Z`|  
|`includeDstRules`| | **Optional.** If set to `true` then DST rule information will be returned in the response.<br /><br />**Note**: For information about DST rules, see the [DSTRule Resource](time-zone-data.md). | Either `true` or `false`.<br /><br />Default: `false` |
|`output`|`o`|**Optional.** Output format of the response.|Format of the response:<br/><br/>- `JSON`<br />- `XML`<br /><br />Default: `JSON`|

> [!NOTE]
>
> The Time Zone API does not maintain historical record of any time zone or day light settings. If a location had a different time zone in the past, it is not considered. The Bing Maps Time Zone API results are based only on current policies and standards.

## Response

Detailed information about Time Zone API responses can be found at [Time Zone Data](time-zone-data.md).

All successful requests return a [TimeZone Resource](time-zone-data.md). Time Zone API calls by query wrap this `TimeZone` resource in a `timeZoneAtLocation` -- see the note below for details.

If applicable, daylight savings information is included separately in the [ConvertedTime Resource](time-zone-data.md) and [DSTRule Resource](time-zone-data.md) fields of the response. 

Time Zone API responses are available in JSON and XML formats.


> [!NOTE] 
> 
> **Response for Time Zone API by Query**.
> 
> If the Time Zone API is called successfully with the query parameter specified, then the response will consist of the field `timeZoneAtLocation` with two sub-fields: `placeName` and `timeZone` for JSON and `PlaceName` and `TimeZone` for XML.
> 
> For example, in JSON:
> ```json
>"__type": "RESTTimeZone:http://schemas.microsoft.com/search/local/ws/rest/v1",
>                    "timeZoneAtLocation": [
>                        {
>                            "placeName": "Vancouver, BC",
>                            "timeZone": [
>                                {
>                                    "genericName": "Pacific Standard Time",
>                                    "abbreviation": "PST",
>                                    "ianaTimeZoneId": "America/Vancouver",
>                                    "windowsTimeZoneId": "Pacific Standard Time",
>                                    "utcOffset": "-8:00",
>                                    "convertedTime": {
>                                        "localTime": "2018-08-06T12:54:46",
>                                        "utcOffsetWithDst": "-7:00",
>                                        "timeZoneDisplayName": "Pacific Daylight Time",
>                                        "timeZoneDisplayAbbr": "PDT"
>                                    }
>                                }
>                            ]
>                        }
>                    ]
> ```
>
> And in XML:
>
> ```xml
><Resource xsi:type="RESTTimeZone">
>    <TimeZoneAtLocation>
>        <TimeZoneInfo>
>            <PlaceName>Vancouver, BC</PlaceName>
>            <TimeZone>
>                <TimeZone>
>                    <GenericName>Pacific Standard Time</GenericName>
>                    <Abbreviation>PST</Abbreviation>
>                    <IANATimeZoneId>America/Vancouver</IANATimeZoneId>
>                    <WindowsTimeZoneId>Pacific Standard Time</WindowsTimeZoneId>
>                    <UTCOffset>-8:00</UTCOffset>
>                    <ConvertedTime>
>                        <LocalTime>2018-08-06T14:19:31</LocalTime>
>                        <UTCOffsetWithDst>-7:00</UTCOffsetWithDst>
>                        <TimeZoneDisplayName>Pacific Daylight Time</TimeZoneDisplayName>
>                        <TimeZoneDisplayAbbr>PDT</TimeZoneDisplayAbbr>
>                    </ConvertedTime>
>                </TimeZone>
>            </TimeZone>
>        </TimeZoneInfo>
>    </TimeZoneAtLocation>
></Resource>
>```

## Examples

Below are several example URL requests and responses.

### Return Time Zone Information in JSON for a Location Point

This example sends a request with a point in Alaska to the Time Zone API. It returns a JSON response with the local time for that point in Alaskan Standard Time.

The URL request: 

```url
https://dev.virtualearth.net/REST/v1/timezone/61.768335,-158.808765?key={BingMapsKey}
```

JSON response:

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
                    "__type": "RESTTimeZone:http://schemas.microsoft.com/search/local/ws/rest/v1",
                    "timeZone": {
                        "genericName": "Alaskan Standard Time",
                        "abbreviation": "AKST",
                        "ianaTimeZoneId": "America/Anchorage",
                        "windowsTimeZoneId": "Alaskan Standard Time",
                        "utcOffset": "-9:00",
                        "convertedTime": {
                            "localTime": "2018-08-06T12:12:41",
                            "utcOffsetWithDst": "-8:00",
                            "timeZoneDisplayName": "Alaskan Daylight Time",
                            "timeZoneDisplayAbbr": "AKDT"
                        }
                    }
                }
            ]
        }
    ],
    "statusCode": 200,
    "statusDescription": "OK",
    "traceId": "b4f9374415454a24afcfe11438997869|CO37D54CC8|7.7.0.0"
}
```

### Return the Time Zone Information in XML for a Location Query

This example sends a request with the query “Bellevue, WA” and returns an XML response with the local time for that location in Pacific Standard Time.

> [!TIP]
>
> Use full country/region names or [official ISO country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) in queries. For example, use “Capetown, ZA” or “Captetown, South Africa” instead of “Capetown, SA”.

The request URL:

```url
https://dev.virtualearth.net/REST/v1/timezone/?query=bellevue,%20wa&output=xml&key={BingMapsKey}
```

XML Response:

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<Response xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <Copyright>Copyright © 2018 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>
    <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>
    <StatusCode>200</StatusCode>
    <StatusDescription>OK</StatusDescription>
    <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>
    <TraceId>4cf95fb83a8847faa890d9851abf7006|CO356342F5|7.7.0.0|Ref A: B55A920F9B734A27B4EEACB2D2B75DBA Ref B: CO1EDGE0922 Ref C: 2018-08-06T20:16:54Z</TraceId>
    <ResourceSets>
        <ResourceSet>
            <EstimatedTotal>1</EstimatedTotal>
            <Resources>
                <Resource xsi:type="RESTTimeZone">
                    <TimeZoneAtLocation>
                        <TimeZoneInfo>
                            <PlaceName>Bellevue, WA</PlaceName>
                            <TimeZone>
                                <TimeZone>
                                    <GenericName>Pacific Standard Time</GenericName>
                                    <Abbreviation>PST</Abbreviation>
                                    <IANATimeZoneId>America/Los_Angeles</IANATimeZoneId>
                                    <WindowsTimeZoneId>Pacific Standard Time</WindowsTimeZoneId>
                                    <UTCOffset>-8:00</UTCOffset>
                                    <ConvertedTime>
                                        <LocalTime>2018-08-06T13:16:54</LocalTime>
                                        <UTCOffsetWithDst>-7:00</UTCOffsetWithDst>
                                        <TimeZoneDisplayName>Pacific Daylight Time</TimeZoneDisplayName>
                                        <TimeZoneDisplayAbbr>PDT</TimeZoneDisplayAbbr>
                                    </ConvertedTime>
                                </TimeZone>
                            </TimeZone>
                        </TimeZoneInfo>
                    </TimeZoneAtLocation>
                </Resource>
            </Resources>
        </ResourceSet>
    </ResourceSets>
</Response>
```

## HTTP Status Codes

> [!NOTE]
> For more about these HTTP codes, see [Status Codes and Error Handling](https://msdn.microsoft.com/library/ff701703.aspx).

When the request is successful, the following HTTP status code is returned.
- `200`

When the request is not successful, the response returns one of the following errors.
- `400`
- `500`