---
title: "MapManeuverNotices Enumeration | Microsoft Docs"
author: "kezhang"
---

# MapManeuverNotices Enumeration

Provides additional information about a maneuver. This enumeration provides values for the ManeuverNotices property of a MapRouteManeuver.

This enumeration allows a bitwise combination of its member values.

**Android**

>```java
>public @interface MapManeuverNotices {
>  int NONE = 0;
>  int TOLL = 1;
>  int UNPAVED = 1 << 1;
>}
>```

**iOS**

>```objectivec
>typedef NS_ENUM(NSInteger, MSMapManeuverNotices) { 
>    MSMapManeuverNoticesNone = 0, 
>    MSMapManeuverNoticesToll, 
>    MSMapManeuverNoticesUnpaved 
>}
>```

## Values

### None

There is no additional information.

### Toll

The maneuver includes a toll road.

### Unpaved

The maneuver includes an unpaved road.

## See Also

* [MapRouteManeuver](maproutemaneuver-class.md)