---
title: OnMapTappedListener Interface | Microsoft Docs
description: Describes the OnMapTappedListener interface for Android and provides syntax and additional references.
ms.author: pablocan
---

# OnMapTappedListener Interface (Android only)

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Listener used with MapView.Tapped event. Return true from this event to prevent other OnMapTappedListeners from receiving this event or false to allow other listeners to receive his notification as well. Events are processed in the order they were attached to the MapView.

>```java
> public interface OnMapTappedListener
>{
>    /** Called when map is tapped. */
>    boolean onMapTapped(MapTappedEventArgs e);
>}
>```

## See Also

* [MapTappedEventArgs](MapTappedEventArgs-class.md)
* [MapView](../MapView-class.md)
