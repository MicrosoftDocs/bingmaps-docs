---
title: MapRouteLine Class | Microsoft Docs
description: Describes the MapRouteLine class for Android and iOS and provides the class' methods, properties, and additional references.
ms.author: pablocan
---

# MapRouteLine Class

Displays a route line on the map.  Represents a path to be traveled between two or more waypoints displayed on the map.

**Android**

>```java
> class MapRouteLine extends MapElement
>```

**iOS**

>```objectivec
> @interface MSMapRouteLine : MSMapElement
>```

_See also:_ [MapElement](mapelement-class.md)

## Methods

### addMapSegment

Adds a MapRouteSegment to the MapRouteLine. Returns false if the MapRouteSegment is already in the MapRouteLine. 

**Android**

>```java
> boolean addSegment(MapRouteSegment mapRouteSegment)
>```

**iOS**

>```objectivec
> - (BOOL)addSegment:(MSMapRouteSegment*)mapSegment
>```

### removeMapSegment

Removes a MapRouteSegment to the MapRouteLine. Returns false if the MapRouteSegment is not in the MapRouteLine. 

**Android**

>```java
> boolean removeSegment(MapRouteSegment mapRouteSegment)
>```

**iOS**

>```objectivec
> - (BOOL)removeSegment:(MSMapRouteSegment*)mapSegment
>```

### clearSegments

Removes all segments from the MapRouteLine.

**Android**

>```java
> void clearSegments()
>```

**iOS**

>```objectivec
> - (void)clearSegments
>```

## Properties

### iterator (Android only)

Allows enumerating over the segments in the MapRouteLine.

>```java
> Iterator<MapRouteSegment> getSegments()
>```

### mapRouteSegments (iOS only)

Allows enumerating over the segments in the MapRouteLine.

>```objectivec
> - property(nonatomic, readonly) NSArray<MSMapRouteSegment*>* mapRouteSegments
>`

### RouteState

**Android**

Sets or gets route state which is used to set the name of an entry of this MapRouteLine. If MapStyleSheetEntry is also set, this value gets ignored.

>```java
> MapRouteLineState getRouteState()
> void setRouteState(MapRouteLineState lineState)
>```

**iOS**
>```objectivec
> @property(nonatomic) MSMapRouteLineState routeState
>`

## See Also

* [MapRouteSegment](maproutesegment-class.md)
* [MapElement](mapelement-class.md)
