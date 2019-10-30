---
title: "MapCameraChangedEventArgs Class | Microsoft Docs"
author: "pablocan"
---

# MapCameraChangedEventArgs Class (Android only)

Event arguments passed to MapView.CameraChanged callback.

## Properties

### changeReason

Indicates the reason the CameraChanged event was triggered.

>```java
> public final MapCameraChangeReason changeReason
>```

### camera

Gets the current position of the map's camera.

>```java
> public final MapCamera camera
>```

## See also

* [OnMapCameraChangedListener](OnMapCameraChangedListener-interface.md)
* [MapView](../MapView-class.md)
