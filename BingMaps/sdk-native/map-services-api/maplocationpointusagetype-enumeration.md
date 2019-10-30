---
title: "MapLocationPointUsageType Enumeration | Microsoft Docs"
author: "pablocan"
---

# MapLocationPointUsageType Enumeration

The best use for the geocode point. Each geocode point is defined as a `Route` point, a `Display` point or `RouteAndDisplay`.

Use `Route` points if you are creating a route to the location. Use `Display` points if you are showing the location on a map. For example, if the location is a park, a `Route` point may specify an entrance to the park where you can enter with a car, and a `Display` point may be a point that specifies the center of the park.

**Android**

>```java
>public enum MapLocationPointUsageType
>{
>    UNKNOWN(0),
>    ROUTE(1),
>    DISPLAY(2),
>    ROUTE_AND_DISPLAY(3);
>}
>```

**iOS**

>```objectivec
>typedef NS_ENUM(NSInteger, MSMapLocationPointUsageType)
>{
>    MSMapLocationPointUsageTypeUnknown = 0,
>    MSMapLocationPointUsageTypeRoute = 1,
>    MSMapLocationPointUsageTypeDisplay = 2,
>    MSMapLocationPointUsageTypeRouteAndDisplay = 3
>};
>```

## Values

### Unknown

Bing Maps SDK was unable to parse the value in the response.

### Route

Map location point is best used for routing.

### Display

Map location point is best used for displaying the corresponding location on the map.

### RouteAndDisplay

Map location point can be used for both routing and displaying the location on the map.

## See also

* [MapLocationPoint](MapLocationPoint-class.md)
