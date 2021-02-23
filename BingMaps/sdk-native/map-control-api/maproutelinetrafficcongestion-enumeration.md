---
title: "MapRouteLineTrafficCongestion Enumeration | Microsoft Docs"
ms.author: "khass"
---

# MapRouteLineTrafficCongestion Enumeration

Specifies the name of the state of MapRouteSegment, which determine appearance of route segment.

**Android**

>```java
> public enum MapRouteLineTrafficCongestion
> {
>     UNSPECIFIED(0),
>     NONE(1),
>     MILD(2)
>     MEDIUM(3)
>     HEAVY(4)
>     CLOSED(5)
> }
>```

**iOS**

>```objectivec
> typedef NS_ENUM(NSInteger, MSMapRouteLineTrafficCongestion)
> {
>     MSMapRouteLineTrafficCongestionUnspecified = 0,
>     MSMapRouteLineTrafficCongestionNone = 1,
>     MSMapRouteLineTrafficCongestionMild = 2
>     MSMapRouteLineTrafficCongestionMedium = 3,
>     MSMapRouteLineTrafficCongestionHeavy = 4,
>     MSMapRouteLineTrafficCongestionClosed = 5
> };
>```

## Values

### Unspecified

The MapRouteSegment will be displayed in default line state.

### None

The MapRouteSegment will be displayed with no traffic line state.

### Mild

The MapRouteSegment will be displayed with mild traffic line state.

### Medium

The MapRouteSegment will be displayed with medium traffic line state.

### Heavy

The MapRouteSegment will be displayed with heavy traffic line state.

### Closed

The MapRouteSegment will be displayed with closed road traffic line state.

## See Also

* [MapRouteSegment](MapRouteSegment-class.md)