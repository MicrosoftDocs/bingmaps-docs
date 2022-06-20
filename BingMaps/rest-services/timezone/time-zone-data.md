---
title: Time Zone Data | Microsoft Docs
description: The Bing Maps Time Zone API returns responses in either XML or JSON. All responses include at least one TimeZone resource.
ms.custom: 
ms.date: 12/11/2018
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
ms.topic: article
ms.assetid: fa146e18-716a-49b7-88b3-17f78e617245
caps.latest.revision: 6
author: eriklindeman
ms.author: eriklind
manager: stevelom
ms.service: bing-maps
---

# Time Zone Data

The Bing Maps Time Zone API returns responses in either XML or JSON. All responses include at least one `TimeZone` resource. Optionally, either a `convertedTime` resource or a `DstRule` resource, or both, will be included in each response. 

These resources are described below.

## __TimeZone__ Resource

|Field Description  |`JSON` Fields | `XML` Fields |
|---------|---------|---------|     
|Standard name of the time zone, e.g. `Pacific standard time`	|`genericName` |	`GenericName` |
|Abbreviation for the time zone, e.g. `PST` | `abbreviation` | `Abbreviation`|
|Time zone name per the IANA standard<sup>1</sup>|	`ianaTimeZoneId`|`IANATimeZoneID`|
|Time zone name as per the Microsoft Windows standard| `windowsTimeZoneID`|	`WindowsTimeZoneID`|
|Offset of time zone from UTC, in `(+/-)hh:mm` format | `utcOffset`| `UTCOffset`|
| `ConvertedTime` Resource | `convertedTime` | `ConvertedTime` |
| `DstRule` Resource<sup>2</sup> | `dstRule` | `DSTRule` | 

<sup>1</sup> If either `desttz` is set to a valid Windows Time Zone ID or `standardtimezoneid` is `WINDOWS`, then the IANA Time Zone ID field will *not* be present in the response.
 
<sup>2</sup> Present in the response only if both `includeDstRules` is `true` and Dst Rules are available for the requested IANA or Windows Time Zone ID.

## __ConvertedTime__ Resource

|Field Description  |`JSON` Fields | `XML` Fields|
|---------|---------|---------|
|Local time for designated time zone, in UTC format |	`localTime`|	`LocalTime`|
| UTC offset with DST, `(+/-)hh:mm` format | `utcOffsetWithDst`| `UTCOffsetWithDst`|
| Display name of time zone, e.g. `Pacific Daylight Time` | `timeZoneDisplayName` | `TimeZoneDisplayName` |
| Display Time zone abbreviation, e.g. `PDT` | `timeZoneDisplayAbbr` | `TimeZoneDisplayAbbr`|

## __DstRule__ Resource

|Field Description  |`JSON` Fields | `XML` Fields|
|---------|---------|---------|
|The month (three-letter abbreviation) when DST starts, e.g. `Mar` | `dstStartMonth` | `DSTStartMonth` |
|DST starting date rule<sup>3</sup> | `dstStartDateRule` | `DSTStartDateRule` |
|The local time when DST starts, `hh:mm` format | `dstStartTime` | `DSTStartTime` |
|The offset to apply *during* DST, `(+/-)h:mm` format<sup>4</sup> | `dstAdjust1` | `DSTAdjust1` |
|The month (three-letter abbreviation) when DST ends, e.g. `Oct` | `dstEndMonth` | `DSTEndMonth` |
|DST ending date rule<sup>3</sup> | `dstEndDateRule` | `DSTEndDateRule` |
|The local time when DST ends, `hh:mm` format | `dstEndTime` | `DSTEndTime` |
|The offset to apply *outside* of DST, `(+/-)h:mm` format<sup>4</sup>  | `dstAdjust2` | `DSTAdjust2`|

<sup>3</sup> The syntax for DST Rules consists of four types of expressions. The first is an integer denoting a day in a month, e.g. `10`. The second is the prefix `last-` which denotes the last day of the month, e.g. `lastSun`. Lastly, there are two relational operators: `>=` and `=<`. For example `Mon>=5` denotes the first Monday of the month on or *after* the fifth day, while `Mon<=5` denotes the first Monday of the month on or *before* the fifth day. For more details, see the [IANA documentation on time zone syntax]( https://data.iana.org/time-zones/tz-how-to.html).

<sup>4</sup> The values for the fields `dstAdjust1` and `dstAdjust2` will never both return valid time offsets. If one field returns a valid time offset in the format `h:mm`, the other field will always return `0`.  
