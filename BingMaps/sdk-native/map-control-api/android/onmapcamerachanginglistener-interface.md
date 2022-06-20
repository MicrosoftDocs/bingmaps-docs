---
title: OnMapCameraChangingListener Interface | Microsoft Docs
description: Describes the OnMapCameraChangingListener interface for Android and provides the MapCameraChangingEventArgs and MapView references.
ms.author: pablocan
---

# OnMapCameraChangingListener Interface (Android only)

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
