---
title: OnMapHoldingListener Interface | Microsoft Docs
description: Describes the OnMapHoldingListener interface for Android and provides the MapHoldingEventArgs and MapView references.
ms.author: pablocan
---

# OnMapHoldingListener Interface (Android only)

Listener used with MapView.Holding event. Return true from this event to prevent other OnMapHoldingListeners from receiving this event or false to allow other listeners to receive his notification as well. Events are processed in the order they were attached to the MapView.

>```java
> public interface OnMapHoldingListener
> {
>     /** Called when pointer is held. */
>     boolean onMapHolding(MapHoldingEventArgs e);
> }
>```

## See Also

* [MapHoldingEventArgs](MapHoldingEventArgs-class.md)
* [MapView](../MapView-class.md)