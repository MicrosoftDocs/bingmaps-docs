---
title: OnMapCameraChangedListener Interface | Microsoft Docs
description: Describes the OnMapCameraChangedListener interface for Android and provides the MapCameraChangedEventArgs and MapView references.
ms.author: pablocan
---

# OnMapCameraChangedListener Interface (Android only)

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Listener used with MapView.CameraChanged event.

>```java
> public interface OnMapCameraChangedListener
> {
>     /** Called when camera stops moving. */
>     boolean onMapCameraChanged(MapCameraChangedEventArgs e);
> }
>```

## See Also

* [MapCameraChangedEventArgs](MapCameraChangedEventArgs-class.md)
* [MapView](../MapView-class.md)
