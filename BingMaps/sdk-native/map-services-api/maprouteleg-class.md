---
title: "MapRouteLeg Class | Microsoft Docs"
author: "kezhang"
---

# MapRouteLeg Class

Contains the set of actions (maneuvers) required to travel between two waypoints along a route.

## Properties

### BoundingBox

The bounding box that contains the route leg.

_See also:_ [GeoboundingBox](../map-control-api/geoboundingbox-class.md)

**Android**

>```java
>GeoboundingBox getBoundingBox()
>```

**iOS**

>```objectivec
>@property(nonatomic) MSGeoboundingBox* boundingBox;
>```

### EstimatedDurationInSeconds

The estimated time required to traverse the route leg.

**Android**

>```java
>long getEstimatedDurationInSeconds()
>```

**iOS**

>```objectivec
>@property(nonatomic) NSTimeInterval duration;
>```

### DurationWithoutTraffic

The estimated time required to traverse the route leg without traffic.

**Android**

>```java
>long getDurationWithoutTrafficInSeconds()
>```

**iOS**

>```objectivec
>@property(nonatomic) NSTimeInterval durationWithoutTraffic;
>```

### LengthInMeters  

The length of the route leg in meters.

**Android**

>```java
>double getLengthInMeters()
>```

**iOS**

>```objectivec
>@property(nonatomic) double lengthInMeters
>```

### Maneuvers  

The list of maneuvers associated with the route leg.

_See also:_ [MapRouteManeuver](maproutemaneuver-class.md)

**Android**

>```java
>List<MapRouteManeuver> getManeuvers()
>```

**iOS**

>```objectivec
>@property(nonatomic) NSArray<MSMapRouteManeuver*>* maneuvers;
>```

### Path  

The path of the route leg.

_See also:_ [Geopath](../map-control-api/geopath-class.md)

**Android**

>```java
>Geopath getPath()
>```

**iOS**

>```objectivec
>@property(nonatomic) MSGeopath* path
>```

### TrafficCongestion  

The level of traffic congestion along a map route leg.

_See also:_ [TrafficCongestion](TrafficCongestion-enumeration.md)

**Android**

>```java
>TrafficCongestion getTrafficCongestion()
>```

**iOS**

>```objectivec
>@property(nonatomic) MSMapTrafficCongestion trafficCongestion
>```

## See Also

* [MapRoute](maproute-class.md)
* [MapRouteManeuver](maproutemaneuver-class.md)