---
title: MapProjection Enumeration | Microsoft Docs
description: Describes the MapProjection enumeration for Android and iOS and provides the enumeration's Web mercator and Globe values.
ms.author: pablocan
---

# MapProjection Enumeration

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Controls how the map projects the world onto the screen.

**Android**

>```java
> enum MapProjection
> {
>     WEB_MERCATOR,
>     GLOBE
> }
>```

**iOS**

>```objectivec
> typedef NS_ENUM(NSInteger, MSMapProjection)
> {
>     MSMapProjectionMercator,
>     MSMapProjectionGlobe,
> }
>```

## Values

### Web mercator

Uses the web mercator projection common to many map rendering engines. Because of limitations of the projection the poles cannot be rendered in this projection.

### Globe

The earth is displayed as a globe allowing the whole earth to be viewed. 