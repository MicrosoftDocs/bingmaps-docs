---
title: "MapCameraChangingEventArgs Class | Microsoft Docs"
author: "pablocan"
---

# MapCameraChangingEventArgs Class (Android only)

Event arguments passed to MapView.CameraChanging callback.

## Properties

### ChangeReason

Indicates the reason the CameraChanging event was triggered.

>```java
> final MapCameraChangeReason changeReason
>```

### Camera

Gets the current position of the map's camera.

>```java
> final MapCamera camera
>```

### IsFirstFrameSinceLastCameraChanged

Gets whether this is the first frame change since cameraChanging event occurs.

>```java
>  final boolean isFirstFrameSinceLastCameraChanged
>```

## See Also

* [OnMapCameraChangingListener](OnMapCameraChangingListener-interface.md)
* [MapView](../MapView-class.md)
