---
title: MapToolbarVerticalAlignment Enumeration | Microsoft Docs
description: Describes the MapToolbarVerticalAlignment enumeration for Android and iOS and provides the enumeration's Top, Center, and Bottom values.
ms.author: pablocan
---

# MapToolbarVerticalAlignment Enumeration

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Controls the vertical alignment of the toolbar buttons within the map.

**Android**

>```java
> enum MapToolbarVerticalAlignment
> {
>     TOP,
>     CENTER,
>     BOTTOM
> }
>```

**iOS**

>```objectivec
> typedef NS_ENUM(NSInteger, MSMapToolbarVerticalAlignment)
> {
>     MSMapToolbarVerticalAlignmentTop,
>     MSMapToolbarVerticalAlignmentCenter,
>     MSMapToolbarVerticalAlignmentBottom
> }
>```

## Values

### Top

Aligned to the top of the map.

### Center

Aligned to the center of the map.

### Bottom

Aligned to the bottom of the map.