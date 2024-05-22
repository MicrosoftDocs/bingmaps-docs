---
title: MapCameraChangingEventArgs Class | Microsoft Docs
description: Describes the MapCameraChangingEventArgs class for Android and provides the class' ChangeReason, Camera, and IsFirstFrameSinceLastCameraChanged properties.
ms.author: pablocan
---

# MapCameraChangingEventArgs Class (Android only)

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

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
