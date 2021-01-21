---
title: "MapLocationMatchCode Enumeration | Microsoft Docs"
author: "pablocan"
---

# MapLocationMatchCode Enumeration

The geocoding level for each geopoint for a location returned from a geocoding request.

For example, a geocoded location with match codes of `Good` and `Ambiguous` means that more than one geocode location was found for the location information and that the geocode service did not have search up-hierarchy to find a match.

Similarly, a geocoded location with match codes of `Ambiguous` and `UpHierarchy` implies that a geocode location could not be found that matched all the provided location information, so the geocode service had to search up-hierarchy and found multiple matches at that level. An example of up an `Ambiguous` and `UpHierarchy` result is when you provide complete address information, but the geocode service cannot locate a match for the street address and instead returns information for more than one `RoadBlock` entity type value.

**Android**

>```java
>public enum MapLocationMatchCode
>{
>    UNKNOWN(0),
>    GOOD(1),
>    AMBIGUOUS(2),
>    UP_HIERARCHY(4);
>}
>```

**iOS**

>```objectivec
>typedef NS_ENUM(NSInteger, MSMapLocationMatchCodes)
>{
>    MSMapLocationMatchCodeUnknown = 0,
>    MSMapLocationMatchCodeGood = 1,
>    MSMapLocationMatchCodeAmbiguous = 2,
>    MSMapLocationMatchCodeUpHierarchy = 4
>};
>```

## Values

### Unknown

Bing Maps SDK was unable to parse the value in the response.

### Good

The location has only one match or all returned matches are considered strong matches. For example, a query for New York returns several Good matches.

### Ambiguous

The location is one of a set of possible matches. For example, when you query for the street address 128 Main St., the response may return two locations for 128 North Main St. and 128 South Main St. because there is not enough information to determine which option to choose.

### UpHierarchy

The location represents a move up the geographic hierarchy. This occurs when a match for the location request was not found, so a less precise result is returned.

## See Also

* [MapLocation](MapLocation-class.md)
