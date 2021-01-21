---
title: "MSMapElementLayerUserDidTapElementHandler Interface | Microsoft Docs"
ms.author: "pablocan"
---

# MSMapElementLayerUserDidTapElementHandler Interface (iOS only)

Handler used with MapElementLayer.MapElementTapped event. Return true from this event to indicate whether it has been handled, or false otherwise.

>```objectivec
> typedef BOOL (^MSMapElementLayerUserDidTapElementHandler)(CGPoint, MSGeopoint*_Nonnull, NSMutableSet<MSMapElement *> *_Nonnull)
>```

## See Also

* [Geopoint](../Geopoint-class.md)
* [MapElement](../MapElement-class.md)
* [MapView](../MapView-class.md)