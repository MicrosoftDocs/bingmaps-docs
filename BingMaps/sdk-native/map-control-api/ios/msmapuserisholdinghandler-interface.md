---
title: MSMapUserIsHoldingHandler Interface | Microsoft Docs
description: Describes the MSMapUserIsHoldingHandler interface for iOS and provides the interface's syntax and additional references.
ms.author: pablocan
---

# MSMapUserIsHoldingHandler Interface (iOS only)

Handler used with MapView.Holding event. Return true from this event to prevent other OnMapHoldingListeners from receiving this event or false to allow other listeners to receive his notification as well. Events are processed in the order they were attached to the MapView.

>```objectivec
> typedef BOOL (^MSMapUserIsHoldingHandler)(CGPoint, MSGeopoint*)
>```

## See Also

* [Geopoint](../Geopoint-class.md)
* [MapView](../MapView-class.md)