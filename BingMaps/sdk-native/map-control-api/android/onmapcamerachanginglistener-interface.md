---
title: "OnMapCameraChangingListener Interface | Microsoft Docs"
author: "pablocan"
---

# OnMapCameraChangingListener Interface (Android only)

Listener used with MapView.CameraChanging event.

>```java
> public interface OnMapCameraChangingListener
> {
>     /** Called when camera stops moving. */
>     public boolean onMapCameraChanging(MapCameraChangingEventArgs e);
> }
>```

## See also

* [MapCameraChangingEventArgs](MapCameraChangingEventArgs-class.md)
* [MapView](../MapView-class.md)