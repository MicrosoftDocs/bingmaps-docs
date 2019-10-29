---
title: "MapLocation Class | Microsoft Docs"
author: "bmnxplat"
---

# MapLocation Class

Contains data about a specific location returned from a geocoding request.

## Properties

### DisplayName

The name of the resource.

**Android**

>```java
>String getDisplayName()
>```

**iOS**

>```objectivec
>@property (nonatomic, readonly) NSString* displayName
>```

### Point

The geopoint for the resource.

_See also:_ [Geopoint](../map-control-api/Geopoint-class.md)

**Android**

>```java
>Geopoint getPoint()
>```

**iOS**

>```objectivec
>@property (nonatomic, readonly) MSGeopoint* point
>```

### Address

The address associated with the resource.

_See also:_ [MapLocationAddress](MapLocationAddress-class.md)

**Android**

>```java
>MapLocationAddress getAddress()
>```

**iOS**

>```objectivec
>@property (nonatomic, readonly) MSMapLocationAddress* address
>```

### EntityType

The entity type that the resource is identified as.

**Android**

>```java
>String getEntityType()
>```

**iOS**

>```objectivec
>@property (nonatomic, readonly) NSString* entityType
>```

### GeocodePoints

Geocode points associated with the resource.

_See also:_ [MapLocationPoint](MapLocationPoint-class.md)

**Android**

>```java
>List<MapLocationPoint> getGeocodePoints()
>```

**iOS**

>```objectivec
>@property (nonatomic, readonly) NSArray<MSMapLocationPoint*>* geocodePoints
>```

### BoundingBox

Geobounding box associated with the resource.

_See also:_ [GeoboundingBox](../map-control-api/GeoboundingBox-class.md)

**Android**

>```java
>GeoboundingBox getBoundingBox()
>```

**iOS**

>```objectivec
>@property (nonatomic, readonly) MSGeoboundingBox* boundingBox
>```

### MatchCodes

One or more match code values that represent the geocoding level for each location in the response.

*In iOS this property has `NS_OPTIONS` type: to work with the value, check against individual `MSMapLocationMatchCodes` values using bitwise `AND` operation.*

_See also:_ [MapLocationMatchCode](MapLocationMatchCode-enumeration.md)

**Android**

>```java
>List<MapLocation.MatchCode> getMatchCodes()
>```

**iOS**

>```objectivec
>@property (nonatomic, readonly) MSMapLocationMatchCodes matchCodes
>```

### QueryParseValues

***Only available for geocoding by query.***

Key-value pairs specifying how the query string was parsed into address values, such as `addressLine`, `locality`, `adminDistrict`, and `postalCode`.

**Android**

>```java
>Map<String, String> getQueryParseValues()
>```

**iOS**

>```objectivec
>@property (nonatomic, readonly) NSDictionary* queryParseValues
>```

## See also

* [MapLocationFinder](MapLocationFinder-class.md)
* [MapLocationFinderResult](MapLocationFinderResult-class.md)
* [MapLocationAddress](MapLocationAddress-class.md)
* [MapLocationPoint](MapLocationPoint-class.md)
* [MapLocationMatchCode](MapLocationMatchCode-enumeration.md)
