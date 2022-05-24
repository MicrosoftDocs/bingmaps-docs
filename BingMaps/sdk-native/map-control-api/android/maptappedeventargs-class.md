---
title: MapTappedEventArgs Class | Microsoft Docs
description: Describes the MapTappedEventArgs class for Android and outlines the Position and Location properties.
ms.author: pablocan
---

# MapTappedEventArgs Class (Android only)

Event arguments passed to MapView.Tapped callback.

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

* [OnMapTappedListener](OnMapTappedListener-interface.md)
* [MapView](../MapView-class.md)
