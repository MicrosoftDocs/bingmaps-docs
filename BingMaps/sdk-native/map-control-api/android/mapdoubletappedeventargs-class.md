---
title: MapDoubleTappedEventArgs Class | Microsoft Docs
description: Describes the MapDoubleTappedEventArgs class for Android and provides the class' Position and Location properties.
ms.author: pablocan
---

# MapDoubleTappedEventArgs Class (Android only)

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Event arguments passed to MapView.DoubleTapped callback.

## Properties

### Position

Gets the position of the pointer input in screen pixels, relative to the map view.

>```java
> final android.graphics.Point position
>```

### Location

Gets the geographic location that corresponds to the position from the received user input.

>```java
> final Geopoint location
>```

## See Also

* [OnMapDoubleTappedListener](OnMapDoubleTappedListener-interface.md)
* [MapView](../MapView-class.md)
