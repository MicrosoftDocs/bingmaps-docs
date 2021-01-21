---
title: "MapRouteDrivingOptions Class | Microsoft Docs"
author: "kezhang"
---

# MapRouteDrivingOptions Class

Forms optional options for a routing request.

## Constructors

Constructor takes no arguments, initializing all fields by default to empty optional value (parameter will not be included in the request)

**Android**

>```java
>MapRouteDrivingOptions()
>```

**iOS**

>```objectivec
>- (instancetype)init
>```

## Properties

### InitialHeading

Gets or Sets the preferred start direction of the route from the current location in degrees, where 0 or 360 = North, 90 = East, 180 = South, and 270 = West.  

*If value is not between 0 and 360, 'InvalidArgumentException' will be thrown out.*

**Android**

>```java
>@Nullable Double getInitialHeading()
>MapRouteDrivingOptions setInitialHeading(@Nullable Double value)
>```

**iOS**

>```objectivec
>@property(nonatomic) NSInteger initialHeading;
>- (void)setInitialHeading:(NSInteger)initialHeading
>```

### DepartureTime

Gets or Sets the date and time of the departure on a route.

*If not specified, devices's system local time is used by default.*

**Android**

>```java
>@Nullable Date getDepartureTime()
>MapRouteDrivingOptions setDepartureTime(@Nullable Date localDateTime)
>```

**iOS**

>```objectivec
>@property(nonatomic, nullable) NSDate* departureTime;
>- (void)setDepartureTime:(NSDate* _Nullable)departureTime
>```

### MaxAlternateRouteCount

Get or Sets a value that indicates the maximum number of alternative routes that are to be provided, if available

*If not specified, 0 is used by default.*

**Android**

>```java
>int getMaxAlternateRouteCount()
>MapRouteDrivingOptions setMaxAlternateRouteCount(@Nullable Integer value)
>```

**iOS**

>```objectivec
>@property(nonatomic) NSInteger maxAlternateRouteCount;
>- (void)setMaxAlternateRouteCount:(NSInteger)maxAlternateRouteCount
>```

### RouteOptimization

Get or Sets a value that specifies to which MapRouteOptimization applied to the route(s).

*If not specified, TIME_WITH_TRAFFIC is used by default.*

_See also:_ [MapRouteOptimization](maprouteoptimization-enumeration.md)

**Android**

>```java
>MapRouteOptimization getRouteOptimization()
>MapRouteDrivingOptions setRouteOptimization(MapRouteOptimization routeOptimization)
>```

**iOS**

>```objectivec
>@property(nonatomic) MSMapRouteOptimization routeOptimization;
>```

### RouteRestrictions

Get or Sets a value that specifies to which MapRouteRestrictions applied to the route(s).

_See also:_ [MapRouteRestrictions](maprouterestrictions-enumeration.md)

**Android**

>```java
>@MapRouteRestrictions int getMapRouteRestrictions()
>MapRouteDrivingOptions setRouteRestrictions(@MapRouteRestrictions int routeRestrictions)
>```

**iOS**

>```objectivec
>@property(nonatomic) MSMapRouteRestrictions routeRestrictions;
>```

## See Also

* [MapRouteFinder](maproutefinder-class.md)