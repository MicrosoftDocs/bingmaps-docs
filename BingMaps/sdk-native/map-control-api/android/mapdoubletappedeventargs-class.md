---
title: "MapDoubleTappedEventArgs Class | Microsoft Docs"
author: "bmnxplat"
---

# MapDoubleTappedEventArgs Class (Android only)

Event arguments passed to MapView.DoubleTapped callback.

## Properties

### Position

Gets the location of the pointer input in client coordinate.

>```java
> final android.graphics.Point position
>```

### Location

Gets the geographic location that corresponds to where the MapControl received user input.

>```java
> final Geopoint location
>```

## See also

* [OnMapDoubleTappedListener](OnMapDoubleTappedListener-interface.md)
* [MapView](../MapView-class.md)