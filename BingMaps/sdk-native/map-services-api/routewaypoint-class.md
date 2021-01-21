---
title: "RouteWaypoint Class | Microsoft Docs"
author: "kezhang"
---

# RouteWaypoint Class

Represents a stop, start, or intermediate waypoint that a route must pass through.

## Constructors

**Android**

>```java
>RouteWaypoint(double latitude, double longitude, double altitude, AltitudeReferenceSystem altitudeReference, RouteWaypointType type)
>RouteWaypoint(double latitude, double longitude, double altitude, RouteWaypointType type)
>RouteWaypoint(double latitude, double longitude)
>RouteWaypoint(double latitude, double longitude, RouteWaypointType type)
>```

**iOS**

>```objectivec
>- (instancetype)initWithLatitude:(CLLocationDegrees)latitude longitude:(CLLocationDegrees)longitude  altitude:(CLLocationDistance)altitude type:(MSMapRouteWaypointType)type;
>- (instancetype)initWithLatitude:(CLLocationDegrees)latitude longitude:(CLLocationDegrees)longitude altitude:(CLLocationDistance)altitude altitudeReferenceSystem:(MSMapAltitudeReferenceSystem)altitudeReferenceSystem  type:(MSMapRouteWaypointType)type;
>- (instancetype)initWithGeopoint:(MSGeopoint*)location type:(MSMapRouteWaypointType)type;
>```

### Point

The geopoint of the waypoint.

_See also:_ [Geopoint](../map-control-api/geopoint-class.md)

**Android**

>```java
>Geopoint getPoint()
>```

**iOS**

>```objectivec
>@property(nonatomic, readonly) MSGeopoint* location;
>```

### Type

The type of waypoint.

_See also:_ [RouteWaypointType](routewaypointtype-enumeration.md)

**Android**

>```java
>RouteWaypointType getType()
>```

**iOS**

>```objectivec
>@property(nonatomic, readonly) MSMapRouteWaypointType type;
>```

## See Also

* [Geopoint](../map-control-api/geopoint-class.md)
* [RouteWaypointType](routewaypointtype-enumeration.md)
