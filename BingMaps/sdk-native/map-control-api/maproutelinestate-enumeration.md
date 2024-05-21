---
title: MapRouteLineState Enumeration | Microsoft Docs
description: Describes the MapRouteLineState enumeration for Android and iOS and provides the enumeration's values.
ms.author: khass
---

# MapRouteLineState Enumeration

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Specifies the name of the state of MapRouteLine, which determine appearance of route line.

**Android**

>```java
> public enum MapRouteLineState
> {
>     UNSPECIFIED(0),
>     ACTIVE(1),
>     ALTERNATIVE(2)
> }
>```

**iOS**

>```objectivec
> typedef NS_ENUM(NSInteger, MSMapRouteLineState)
> {
>     MSMapRouteLineStateUnspecified = 0,
>     MSMapRouteLineStateActive = 1,
>     MSMapRouteLineStateAlternative = 2
> };
>```

## Values

### Unspecified

The MapRouteLine will be displayed with default route line state.

### Active

The MapRouteLine will be displayed with active route line state.

### Alternative

The MapRouteLine will be displayed with alternative route line state.

## See Also

* [MapRouteLine](MapRouteLine-class.md)