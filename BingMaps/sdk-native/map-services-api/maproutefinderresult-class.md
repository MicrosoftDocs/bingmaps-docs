---
title: "MapRouteFinderResult Class | Microsoft Docs"
ms.author: "kezhang"
---

# MapRouteFinderResult Class

Contains status code and result route data for a MapRouteFinder request.

## Properties

### Status

The status code for the MapRouteFinder request.

_See also:_ [MapRouteFinderStatus](maproutefinderstatus-enumeration.md)

**Android**

>```java
>MapRouteFinderStatus getStatus()
>```

**iOS**

>```objectivec
>@property (nonatomic) MSMapRouteFinderResult status
>```

### MapRoute

Primary route found by a MapRouteFinder request.  
If `Status` is not `Success`, the mapRoute will be empty.

_See also:_ [MapRoute](maproute-class.md)

**Android**

>```java
>@Nullable MapRoute getRoute()
>```

**iOS**

>```objectivec
>@property(nonatomic, nullable) MSMapRoute* mapRoute;
>```

### AlternateRoutes

Alternate routes found by a MapRouteFinder request(if available).  
If `setMaxAlternateRouteCount()` in MapRouteDrivingOptions is set to 1 or greater, the alternateRoutes will be provided.<br />
If `Status` is not `Success`, the alternateRoutes will be empty.

_See also:_ 

* [MapRoute](maproute-class.md)
* [MapRouteDrivingOptions](maproutedrivingoptions-class.md)

**Android**

>```java
>@Nullable List<MapRoute> getAlternateRoutes()
>```

**iOS**

>```objectivec
>@property(nonatomic) NSArray<MSMapRoute*>* alternateRoutes
>```

## See Also

* [MapRouteFinder](maproutefinder-class.md)
* [MapRouteDrivingOptions](maproutedrivingoptions-class.md)
