---
title: "MapRoute Class | Microsoft Docs"
author: "kezhang"
---

# MapRoute Class

Represents a path to be traveled between two or more waypoints.

## Properties

### BoundingBox

The bounding box that contains the route.

_See also:_ [GeoboundingBox](../map-control-api/geoboundingbox-class.md)

**Android**

>```java
>GeoboundingBox getBoundingBox()
>```

**iOS**

>```objectivec
>@property(nonatomic) MSGeoboundingBox* boundingBox;
>```

### EstimatedDurationInSeconds()

The estimated time required to traverse the route.

**Android**

>```java
>long getEstimatedDurationInSeconds()
>```

**iOS**

>```objectivec
>@property(nonatomic) NSTimeInterval duration;
>```

### DurationWithoutTraffic

The estimated time required to traverse the route without traffic.

**Android**

>```java
>long getDurationWithoutTrafficInSeconds()
>```

**iOS**

>```objectivec
>@property(nonatomic) NSTimeInterval durationWithoutTraffic;
>```

### HasBlockedRoads

Indicates the route has been modified from the "best" route to avoid blocked roads.

**Android**

>```java
>boolean getHasBlockedRoads()
>```

**iOS**

>```objectivec
>@property(nonatomic) BOOL hasBlockedRoads;
>```

### IsScenic 

Indicates whether the MapRoute is based on scenic roads.

**Android**

>```java
>boolean getIsScenic()
>```

**iOS**

>```objectivec
>@property(nonatomic) BOOL isScenic;
>```

### IsTrafficBased  

Indicates whether the MapRoute is based on traffic.

**Android**

>```java
>boolean getIsTrafficBased ()
>```

**iOS**

>```objectivec
>@property(nonatomic) BOOL isTrafficBased;
>```

### Legs  

The list of legs associated with the route. This property returns MapRouteLeg a collection of  objects.

_See also:_ [MapRouteLeg](maprouteleg-class.md)

**Android**

>```java
>List<MapRouteLeg> getLegs()
>```

**iOS**

>```objectivec
>@property(nonatomic) NSArray<MSMapRouteLeg*>* legs;
>```

### LengthInMeters  

The length of the route in meters.

**Android**

>```java
>double getLengthInMeters()
>```

**iOS**

>```objectivec
>@property(nonatomic) double lengthInMeters
>```

### Path  

The path of the route.

**Android**

>```java
>Geopath getPath()
>```

**iOS**

>```objectivec
>@property(nonatomic) MSGeopath* path
>```

### TrafficCongestion  

The level of traffic congestion along a map route.

_See also:_ [TrafficCongestion](trafficcongestion-enumeration.md)

**Android**

>```java
>TrafficCongestion getTrafficCongestion()
>```

**iOS**

>```objectivec
>@property(nonatomic) MSMapTrafficCongestion trafficCongestion
>```

### ViolatedRestrictions   

The MapRouteRestrictions that have been violated by the route.

_See also:_ [MapRouteRestrictions](maprouterestrictions-enumeration.md)

**Android**

>```java
>@MapRouteRestrictions int getViolatedRestrictions()
>```

**iOS**

>```objectivec
>@property(nonatomic) MSMapRouteRestrictions violatedRestrictions
>```

## See Also

* [MapRouteFinder](maproutefinder-class.md)