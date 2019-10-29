---
title: "MSMapElementLayerUserDidTapHandler Interface | Microsoft Docs"
author: "bmnxplat"
---

# MSMapElementLayerUserDidTapHandler Interface (iOS only)

Handler used with MapElementLayer.MapElementTapped event. Return true from this event to indicate whether it has been handled, or false otherwise.

>```objectivec
> typedef BOOL (^MSMapElementLayerUserDidTapHandler)(CGPoint, MSGeopoint*_Nonnull, NSMutableSet<MSMapElement *> *_Nonnull)
>```

## See also

* [Geopoint](../Geopoint-class.md)
* [MapElement](../MapElement-class.md)
* [MapView](../MapView-class.md)