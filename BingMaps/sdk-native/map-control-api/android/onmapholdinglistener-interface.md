---
title: "OnMapHoldingListener Interface | Microsoft Docs"
author: "bmnxplat"
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

## See also

* [MapHoldingEventArgs](MapHoldingEventArgs-class.md)
* [MapView](../MapView-class.md)