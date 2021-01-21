---
title: "MapLocationEntityTypes Enumeration | Microsoft Docs"
author: "pablocan"
---

# MapLocationEntityTypes Enumeration

Specifies the entity types that you want returned in the response for a geocoding request. Only the types you specify will be returned. If the point cannot be mapped to the entity types you specify, no location information is returned in the response.

These entity types are ordered from the most specific entity to the least specific entity. When entities of more than one entity type are found, only the most specific entity is returned. For example, if you specify `Address` and `AdminDivision` as entity types and entities were found for both types, only the `Address` entity information is returned in the response. One exception to this rule is when both `PopulatedPlace` and `Neighborhood` entity types are specified and information is found for both. In this case, the information for both entity types is returned. Also, more than one neighborhood may be returned because the area covered by two different neighborhoods can overlap.

The values can be combined using bitwise `OR`.

**Android**

>```java
>public class MapLocationEntityTypes
>{
>    public static final int NOT_SET = 0;
>    public static final int ADDRESS = 1;
>    public static final int NEIGHBORHOOD = 2;
>    public static final int POPULATED_PLACE = 4;
>    public static final int POSTCODE = 8;
>    public static final int ADMIN_DIVISION = 16;
>    public static final int ADMIN_DIVISION_2 = 32;
>    public static final int COUNTRY_REGION = 64;
>}
>```

**iOS**

>```objectivec
>typedef NS_OPTIONS(NSUInteger, MSMapLocationEntityTypes)
>{
>    MSMapLocationEntityTypeNotSet = 0,
>    MSMapLocationEntityTypeAddress = 1,
>    MSMapLocationEntityTypeNeighborhood = 2,
>    MSMapLocationEntityTypePopulatedPlace = 4,
>    MSMapLocationEntityTypePostcode = 8,
>    MSMapLocationEntityTypeAdminDivision = 16,
>    MSMapLocationEntityTypeAdminDivision2 = 32,
>    MSMapLocationEntityTypeCountryRegion = 64
>};
>```

## Values

### NotSet

Default value, does not set `EntityTypes` parameter in the request.

### Address

Include addresses in the response.

### Neighborhood

Include neighborhoods in the response.

### PopulatedPlace

Include populated areas in the response.

### Postcode

Include postcode areas in the response.

### AdminDivision

Include administrative divisions in the response.

### AdminDivision2

Include second level administrative divisions in the response.

### CountryRegion

Include countries in the response.

## See Also

* [MapLocationOptions](MapLocationOptions-class.md)
