---
title: OnMapCameraChangingListener Interface | Microsoft Docs
description: Describes the OnMapCameraChangingListener interface for Android and provides the MapCameraChangingEventArgs and MapView references.
ms.author: pablocan
---

# OnMapCameraChangingListener Interface (Android only)

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Listener used with MapView.CameraChanging event.

>```java
> public interface OnMapCameraChangingListener
> {
>     /** Called when camera stops moving. */
>     boolean onMapCameraChanging(MapCameraChangingEventArgs e);
> }
>```

## See Also

* [MapCameraChangingEventArgs](MapCameraChangingEventArgs-class.md)
* [MapView](../MapView-class.md)
