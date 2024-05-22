---
title: MapRouteLineTravelMode Enumeration | Microsoft Docs
description: Describes the MapRouteLineTravelMode enumeration for Android and iOS and provides the enumeration's values.
ms.author: khass
---

# MapRouteLineTravelMode Enumeration

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Specifies the name of the entry of MapRouteSegment, which determine appearance of line segment.

**Android**

>```java
> public enum MapRouteLineTravelMode
> {
>     DRIVING(0),
>     WALKING(1),
>     TRANSIT(2)
> }
>```

**iOS**

>```objectivec
> typedef NS_ENUM(NSInteger, MSMapRouteLineTravelMode)
> {
>     MSMapRouteLineTravelModeDriving = 0,
>     MSMapRouteLineTravelModeWalking = 1,
>     MSMapRouteLineTravelModeTransit = 2
> };
>```

## Values

### Driving

The MapRouteLine will be displayed with driving line entry.

### Walking

The MapRouteLine will be displayed in walking line entry.

### Transit

The MapRouteLine will be displayed in transit line entry.

## See Also

* [MapRouteSegment](MapRouteSegment-class.md)