---
title: "MapHoldingEventArgs Class | Microsoft Docs"
author: "pablocan"
---

# MapHoldingEventArgs Class (Android only)

Event arguments passed to MapView.Holding callback.

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

* [OnMapHoldingListener](OnMapHoldingListener-interface.md)
* [MapView](../MapView-class.md)
