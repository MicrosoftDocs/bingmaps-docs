---
title: "MapDoubleTappedEventArgs Class | Microsoft Docs"
author: "pablocan"
---

# MapDoubleTappedEventArgs Class (Android only)

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

## See also

* [OnMapDoubleTappedListener](OnMapDoubleTappedListener-interface.md)
* [MapView](../MapView-class.md)
