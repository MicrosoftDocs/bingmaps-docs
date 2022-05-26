---
title: RouteWaypointType Enumeration | Microsoft Docs
description: Describes the RouteWaypointType enumeration for android and iOS and provides the enumeration's values and additional references.
ms.author: kezhang
---

# RouteWaypointType Enumeration

Specifies the type of waypoint

**Android**

>```java
>public enum RouteWaypointType {
>  STOP(0),
>  VIA(1);
>}
>```

**iOS**

>```objectivec
>typedef NS_ENUM(NSInteger, MSMapRouteWaypointType) { 
>    MSMapRouteWaypointTypeStop = 0, 
>    MSMapRouteWaypointTypeVia 
>}
>```

## Values

### Stop

A start or stop waypoint of a route or route leg.

### Via

An intermediate waypoint that a route must pass through.

## See Also

* [RouteWaypoint](routewaypoint-class.md)