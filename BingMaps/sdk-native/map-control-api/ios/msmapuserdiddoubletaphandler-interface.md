---
title: "MSMapUserDidDoubleTapHandler Interface | Microsoft Docs"
author: "pablocan"
---

# MSMapUserDidDoubleTapHandler Interface (iOS only)

Handler used with MapView.DoubleTapped event. Return true from this event to prevent other OnMapDoubleTappedListeners from receiving this event or false to allow other listeners to receive his notification as well. Events are processed in the order they were attached to the MapView.

>```objectivec
> typedef BOOL (^MSMapUserDidDoubleTapHandler)(CGPoint, MSGeopoint*)
>```

## See also

* [Geopoint](../Geopoint-class.md)
* [MapView](../MapView-class.md)