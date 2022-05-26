---
title: MapLocationFinderResult Class | Microsoft Docs
description: Describes the MapLocationFinderResult class for Android and iOS and provides the class's properties and additional references.
ms.author: pablocan
---

# MapLocationFinderResult Class

Contains status code and result location data for a geocoding request.

## Properties

### Status

The status code for the completed request.

_See also:_ [MapLocationFinderStatus](MapLocationFinderStatus-enumeration.md)

**Android**

>```java
>MapLocationFinderStatus getStatus()
>```

**iOS**

>```objectivec
>@property (nonatomic, readonly) MSMapLocationFinderStatus status
>```

### Locations

Location data returned in the response.  
If `Status` is not `Success`, the list will be empty.

_See also:_ [MapLocation](MapLocation-class.md)

**Android**

>```java
>List<MapLocation> getLocations()
>```

**iOS**

>```objectivec
>@property (nonatomic, readonly) NSArray<MSMapLocation*>* locations
>```

## See Also

* [MapLocationFinder](MapLocationFinder-class.md)
