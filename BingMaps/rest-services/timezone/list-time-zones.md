---
title: List Time Zones | Microsoft Docs
description: The list operation retrieves all available time zone data for either the IANA or Windows time zone standard.
ms.custom: 
ms.date: "05/21/2024"
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

# List Time Zones

> [!NOTE]
> **Bing Maps List Time Zone API retirement**
>
> Bing Maps List Time Zone API is deprecated and will be retired. Free (Basic) account customers can continue to use Bing Maps List Time Zone API until June 30th, 2025. Enterprise account customers can continue to use Bing Maps List Time Zone API until June 30th, 2028. To avoid service disruptions, all implementations using Bing Maps List Time Zone API will need to be updated to use Azure Maps [Timezone](/rest/api/maps/timezone) API by the retirement date that applies to your Bing Maps for Enterprise account type.
>
> Azure Maps is Microsoft's next-generation maps and geospatial services for developers. Azure Maps has many of the same features as Bing Maps for Enterprise, and more. To get started with Azure Maps, create a free [Azure subscription](https://azure.microsoft.com/free) and an [Azure Maps account](/azure/azure-maps/how-to-manage-account-keys#create-a-new-account). For more information about azure Maps, see [Azure Maps Documentation](/azure/azure-maps/). For migration guidance, see [Bing Maps Migration Overview](/azure/azure-maps/migrate-bing-maps-overview).

The list operation retrieves all available time zone data for either the [IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) or [Windows](https://support.microsoft.com/help/973627/microsoft-time-zone-index-values) time zone standard. Additionally, information about any particular time zone can be retrieved using the ID for that time zone formatted in either the IANA or Windows time zone standard.

## API Templates

> [!NOTE]
>
> These templates support both HTTP and HTTPS.

### Get a Full List of Time zones for a Given Standard (Windows or IANA)

The Time Zone API list operation returns a complete list of time zone information for either the [Microsoft Windows](https://support.microsoft.com/help/973627/microsoft-time-zone-index-values) or [IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) Time Zone standard. In the request URL specify `timezonestandard = WINDOWS` or `timezonestandard = IANA` to retrieve a list of Windows or IANA Time Zone information, respectively.

```url
https://dev.virtualearth.net/REST/v1/TimeZone/List/?timezonestandard={IANA_or_Windows}&key={BingMapsKey}
```

### Time Zone from Time Zone ID (Windows or IANA)

Given a specified Time Zone ID in either the [Microsoft Windows](https://support.microsoft.com/help/973627/microsoft-time-zone-index-values) or [IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) Time Zone format, e.g. `desttz = America/los_angeles`, the Time Zone API returns information about that time zone.

```url
https://dev.virtualearth.net/REST/v1/TimeZone/?desttz={time_zone_id}&key={BingMapsKey}
```


## API Parameters

|Parameters |Alias  |Descriptions  |Values |
|:------|:----:|---------|---------|
|`desttz` | |  **Required for getting Time Zone by Local Time Zone ID**. The ID of the destination time zone.| Any valid [IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) or [Windows time zone ID](https://support.microsoft.com/help/973627/microsoft-time-zone-index-values).<br /><br />*Examples*:<br /><br />- `Americas/LosAngeles`<br />- `Cape Verde Standard Time`|
|`includeDstRules`| | **Optional.** If set to `true` then DST rule information will be returned in the response.<br /><br />**Note**: For information about DST rules, see the [DSTRule Resource](time-zone-data.md). | Either `true` or `false`.<br /><br />Default: `false` |
|`timezonestandard` | `tzstd` | **Required for using the List operation.** Name of the time zone standard. |  One of the following values must be specified:<br /><br />- `IANA`<br />- `Windows`<br /><br />|
|`output`|`o`|**Optional.** Output format of the response.|Format of the response:<br/><br/>- `JSON`<br />- `XML`<br /><br />Default: `JSON`|


> [!NOTE]
>
> The Time Zone API does not maintain historical record of any time zone or day light settings. If a location had a different time zone in the past, it is not considered. The Bing Maps Time Zone API results are based only on current policies and standards.

## Response

Detailed information about Time Zone API responses can be found at [Time Zone Data](time-zone-data.md).

Successful calls to Time Zone API with the ist operation return a list of [TimeZone Resources](time-zone-data.md) with complete information about either the [IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) or [Microsoft Windows](https://support.microsoft.com/help/973627/microsoft-time-zone-index-values) Time Zone standard.

If applicable, daylight savings information is included separately in the [ConvertedTime Resource](time-zone-data.md) and [DSTRule Resource](time-zone-data.md) fields of the response. 

Time Zone API responses are available in JSON and XML formats.

## Examples

### Return a List of Timezones for a Given Standard

The List operation for the Time Zone API returns the complete list of either IANA or Windows Time Zone IDs by setting the `timezonestandard` parameter to either `iana` or `windows`, respectively.

The following URL request returns a list of the Windows Time Zone IDs:

```url
https://dev.virtualearth.net/REST/V1/TimeZone/List/?timezonestandard=windows&key={BingMapsKey}
```

The (truncated) JSON response:

```json
{
    "authenticationResultCode": "ValidCredentials",
    "brandLogoUri": "http://dev.virtualearth.net/Branding/logo_powered_by.png",
    "copyright": "Copyright © 2018 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",
    "resourceSets": [
        {
            "estimatedTotal": 128,
            "resources": [
                {
                    "__type": "RESTTimeZone:http://schemas.microsoft.com/search/local/ws/rest/v1",
                    "timeZone": {
                        "genericName": "UTC-11",
                        "ianaTimeZoneId": "Pacific/Niue",
                        "windowsTimeZoneId": "UTC-11",
                        "utcOffset": "-11:00"
                    }
                },
                
                /*  The other 127 resources removed for brevity  */
         }
    ],
    "statusCode": 200,
    "statusDescription": "OK",
    "traceId": "fa78920f38d24d0490a8b05300c6aab6|TW-CWU-178|7.7.0.0"
}
```

### Return Details about a Particular Timezone

The Time Zone API can be used to retrieve information about any timezone by specifying either its IANA or Windows Time Zone ID.

In this example, to get information about the time zone in L.A., we set `desttz` to the IANA code `America/Los_Angeles`.

```url
https://dev.virtualearth.net/REST/V1/TimeZone/?desttz=America/Los_Angeles&includeDstRules=true&key={BingMapsKey}
```

The JSON response for the Los Angeles time zone:

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
                        "genericName": "Pacific Standard Time",
                        "abbreviation": "PST",
                        "ianaTimeZoneId": "America/Los_Angeles",
                        "windowsTimeZoneId": "Pacific Standard Time",
                        "utcOffset": "-8:00",
                        "convertedTime": {
                            "localTime": "2018-08-06T14:46:55",
                            "utcOffsetWithDst": "-7:00",
                            "timeZoneDisplayName": "Pacific Daylight Time",
                            "timeZoneDisplayAbbr": "PDT"
                        },
                        "dstRule": {
                            "dstStartMonth": "Mar",
                            "dstStartDateRule": "Sun>=8",
                            "dstStartTime": "2:00",
                            "dstAdjust1": "1:00",
                            "dstEndMonth": "Nov",
                            "dstEndDateRule": "Sun>=1",
                            "dstEndTime ": "2:00",
                            "dstAdjust2": "0"
                        }
                    }
                }
            ]
        }
    ],
    "statusCode": 200,
    "statusDescription": "OK",
    "traceId": "7d925d7df36f4b3383ebc63ddba8e91d|TW-CWU-178|7.7.0.0"
}
```

## HTTP Status Codes

> [!NOTE]
> For more about these HTTP codes, see [Status Codes and Error Handling](https://msdn.microsoft.com/library/ff701703.aspx).

When the request is successful, the following HTTP status code is returned.
- `200`

When the request is not successful, the response returns one of the following errors.
- `400`
- `500`

