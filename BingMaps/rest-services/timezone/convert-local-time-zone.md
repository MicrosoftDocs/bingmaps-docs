---
title: "Convert Local Time Zone| Microsoft Docs"
ms.custom: ""
ms.date: "12/11/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: fa146e18-716a-49b7-88b3-17f78e617245
caps.latest.revision: 6
ms.author: "v-chrfr"
manager: "stevelom"
ms.service: "bing-maps"
---

# Convert Time Zone

The Bing Maps Time Zone API performs time zone conversions. Given any datetime value in UTC format and the desired time zone, the API will return a response with that datetime converted to the specified time zone. If a date is provided in the UTC time stamp, the API will return the specified time zone with the proper DST values.

## API Template

> [!NOTE]
>
> This template supports both HTTP and HTTPS.

### Convert UTC Datetime to a Different Time Zone

Converts a datetime value in UTC format to local time in the specified time zone. The date component is used to determine the correct day light saving settings. 

```url
https://dev.virtualearth.net/REST/v1/TimeZone/Convert/?datetime={datetime_utc}&desttz={timezoneid}&key={BingMapsAPIKey}
```

## API Parameters

|Parameters |Alias  |Descriptions  |Values |
|:------|:----:|---------|---------|
|`dateTime` |`dt`| **Required.** The UTC date time string for the specified location. The date must be specified to apply the correct DST.| The date time string must be in UTC format. If the date is not included, the returned time zone information may be incorrect.<br /><br />*Example*: `2018-05-15T13:14:15Z` |
|`desttz` | |  **Required**. The ID of the destination time zone.<br /><br />The value of `datetime` will be converted to the local time of this time zone. | Any valid [IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) or [Windows](https://support.microsoft.com/help/973627/microsoft-time-zone-index-values) time zone name.<br /><br />*Examples*:<br /><br />- `Americas/LosAngeles`<br />- `Cape Verde Standard Time`|
|`includeDstRules`| | **Optional.** If set to `true` then DST rule information will be returned in the response.<br /><br />**Note**: For information about DST rules, see the [DSTRule Resource](time-zone-data.md). | Either `true` or `false`.<br /><br />Default: `false` |
|`output`|`o`|**Optional.** Output format of the response.|Format of the response:<br/><br/>- `JSON`<br />- `XML`<br /><br />Default: `JSON`|


> [!NOTE]
>
> The Time Zone API does not maintain historical record of any time zone or day light settings. If a location had a different time zone in the past, it is not considered. The Bing Maps Time Zone API results are based only on current policies and standards.

## Response

Detailed information about Time Zone API responses can be found at [Time Zone Data](time-zone-data.md).

All successful requests return a [TimeZone Resource](time-zone-data.md). 

If applicable, daylight savings information is included separately in the [ConvertedTime Resource](time-zone-data.md) and [DSTRule Resource](time-zone-data.md) fields of the response.

Time Zone API responses are available in JSON and XML formats.

## Examples

### Convert an UTC Date Time Stamp to a Different Time Zone

This example sends a request with a datetime stamp (e.g. `2018-05-15T13:14:15Z`) and the desired time zone for Los Angeles (`timezone = America/Los_Angeles`) and returns an XML response. 

Notice that there are two separate XML fields containing the DST information. The `ConvertedTime` field contains information about the local time zone at that location, including the UTC offset. The field `DSTRule` includes information about the DST start and ending times for that location.

The URL request:

```url
https://dev.virtualearth.net/REST/v1/timezone/convert/?datetime=2018-05-15T13:14:15Z&desttz=america/Los_Angeles&o=xml&includeDstRules=true&key={BingMapsAPIKey}

```

XML response:

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<Response xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <Copyright>Copyright © 2018 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>
    <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>
    <StatusCode>200</StatusCode>
    <StatusDescription>OK</StatusDescription>
    <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>
    <TraceId>aa6dd02248ec48ed86fa981bd797ebae|TW-CWU-178|7.7.0.0</TraceId>
    <ResourceSets>
        <ResourceSet>
            <EstimatedTotal>1</EstimatedTotal>
            <Resources>
                <Resource xsi:type="RESTTimeZone">
                    <TimeZone>
                        <GenericName>Pacific Standard Time</GenericName>
                        <Abbreviation>PST</Abbreviation>
                        <IANATimeZoneId>America/Los_Angeles</IANATimeZoneId>
                        <WindowsTimeZoneId>Pacific Standard Time</WindowsTimeZoneId>
                        <UTCOffset>-8:00</UTCOffset>
                        <ConvertedTime>
                            <LocalTime>2018-05-15T06:14:15</LocalTime>
                            <UTCOffsetWithDst>-7:00</UTCOffsetWithDst>
                            <TimeZoneDisplayName>Pacific Daylight Time</TimeZoneDisplayName>
                            <TimeZoneDisplayAbbr>PDT</TimeZoneDisplayAbbr>
                        </ConvertedTime>
                        <DSTRule>
                            <DSTStartMonth>Mar</DSTStartMonth>
                            <DSTStartDateRule>Sun>=8</DSTStartDateRule>
                            <DSTStartTime>2:00</DSTStartTime>
                            <DSTAdjust1>1:00</DstAdjust1>
                            <DSTEndMonth>Nov</DSTEndMonth>
                            <DSTEndDateRule>Sun>=1</DSTEndDateRule>
                            <DSTEndTime>2:00</DSTEndTime>
                            <DSTAdjust2>0</DSTAdjust2>
                        </DSTRule>
                    </TimeZone>
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