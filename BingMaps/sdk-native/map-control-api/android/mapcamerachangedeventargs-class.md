---
title: "MapCameraChangedEventArgs Class | Microsoft Docs"
ms.author: "pablocan"
---

# MapCameraChangedEventArgs Class (Android only)

Event arguments passed to MapView.CameraChanged callback.

## Properties

### ChangeReason

Indicates the reason the CameraChanged event was triggered.

>```java
> final MapCameraChangeReason changeReason
>```

### Camera

Gets the current position of the map's camera.

>```java
> final MapCamera camera
>```

## See Also

* [OnMapCameraChangedListener](OnMapCameraChangedListener-interface.md)
* [MapView](../MapView-class.md)
