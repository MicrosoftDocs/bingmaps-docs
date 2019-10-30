---
title: "OnMapCameraChangedListener Interface | Microsoft Docs"
author: "pablocan"
---

# OnMapCameraChangedListener Interface (Android only)

Listener used with MapView.CameraChanged event.

>```java
> public interface OnMapCameraChangedListener
> {
>     /** Called when camera stops moving. */
>     public boolean onMapCameraChanged(MapCameraChangedEventArgs e);
> }
>```

## See also

* [MapCameraChangedEventArgs](MapCameraChangedEventArgs-class.md)
* [MapView](../MapView-class.md)