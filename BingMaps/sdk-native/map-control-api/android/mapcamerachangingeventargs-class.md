---
title: "MapCameraChangingEventArgs Class | Microsoft Docs"
author: "bmnxplat"
---

# MapCameraChangingEventArgs Class (Android only)

Event arguments passed to MapView.CameraChanging callback.

## Properties

### changeReason

Indicates the reason the CameraChanging event was triggered.

>```java
> public final MapCameraChangeReason changeReason
>```

### camera

Gets the current position of the map's camera.

>```java
> public final MapCamera camera
>```

### isFirstFrameSinceLastCameraChanged

Gets whether this is the first frame change since cameraChanging event occurs.

>```java
>  public final boolean isFirstFrameSinceLastCameraChanged
>```

## See also

* [OnMapCameraChangingListener](OnMapCameraChangingListener-interface.md)
* [MapView](../MapView-class.md)
