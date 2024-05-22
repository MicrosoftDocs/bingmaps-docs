---
title: OnMapDoubleTappedListener Interface | Microsoft Docs
description: Describes the OnMapDoubleTappedListener interface for Android and provides the MapDoubleTappedEventArgs and MapView references.
ms.author: pablocan
---

# OnMapDoubleTappedListener Interface (Android only)

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Listener used with MapView.DoubleTapped event. Return true from this event to prevent other OnMapDoubleTappedListeners from receiving this event or false to allow other listeners to receive his notification as well. Events are processed in the order they were attached to the MapView.

>```java
> public interface OnMapDoubleTappedListener
> {
>     /** Called when map is double tapped. */
>     boolean onMapDoubleTapped(MapDoubleTappedEventArgs e);
> }
>```

## See Also

* [MapDoubleTappedEventArgs](MapDoubleTappedEventArgs-class.md)
* [MapView](../MapView-class.md)
