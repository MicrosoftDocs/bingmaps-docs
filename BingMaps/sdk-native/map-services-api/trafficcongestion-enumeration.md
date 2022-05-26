---
title: TrafficCongestion Enumeration | Microsoft Docs
description: Describes the TrafficCongestion enumeration for Android and iOS and provides the enumeration's values and additional references.
ms.author: kezhang
---

# TrafficCongestion Enumeration

Specifies the level of traffic congestion along a map route or route leg.

**Android**

>```java
>public enum TrafficCongestion {
>  UNKNOWN(0),
>  NONE(1),
>  MILD(2),
>  MEDIUM(3),
>  HEAVY(4);
>}
>```

**iOS**

>```objectivec
>typedef NS_ENUM(NSInteger, MSMapTrafficCongestion) {
>    MSMapTrafficCongestionUnknown = 0,
>    MSMapTrafficCongestionNone = 1,
>    MSMapTrafficCongestionMild = 2,
>    MSMapTrafficCongestionMedium = 3,
>    MSMapTrafficCongestionHeavy = 4
>};
>```

## Values

### UNKNOWN

The level of traffic congestion is unknown.

### NONE

The level of traffic congestion is none.

### MILD

The level of traffic congestion is mild.

### MEDIUM

The level of traffic congestion is medium.

### HEAVY

The level of traffic congestion is heavy.

## See Also

* [MapRoute](maproute-class.md)
* [MapRouteLeg](maprouteleg-class.md)