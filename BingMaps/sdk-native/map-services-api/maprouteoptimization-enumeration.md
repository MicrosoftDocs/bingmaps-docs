---
title: "MapRouteOptimization Enumeration | Microsoft Docs"
author: "kezhang"
---

# MapRouteOptimization Enumeration

Specifies the optimization applied to a route. This enumeration provides values for certain parameters of some overloads of the GetDrivingRoute method.

**Android**

>```java
>public enum MapRouteOptimization {
>  TIME(0),,
>  DISTANCE(1),
>  TIME_WITH_TRAFFIC(2),
>  SCENIC(3);
>}
>```

**iOS**

>```objectivec
>typedef NS_ENUM(NSInteger, MSMapRouteOptimization) {
>    MSMapRouteOptimizationTime = 0,
>    MSMapRouteOptimizationDistance,
>    MSMapRouteOptimizationTimeWithTraffic,
>    MSMapRouteOptimizationScenic
>};
>```

## Values

### Time

The route is calculated to minimize the time. Traffic information is not used.

### Distance

The route is calculated to minimize the distance. Traffic information is not used.

### TimeWithTraffic

The route is calculated to minimize the time and uses current traffic information.

### Scenic

The route is calculated to include the most scenic roads.

## See Also

* [MapRouteFinder](maproutefinder-class.md)
* [MapRouteDrivingOptions](maproutedrivingoptions-class.md)