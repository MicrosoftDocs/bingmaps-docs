---
title: "MSMapElementLayerUserDidTapFlyoutHandler Interface | Microsoft Docs"
ms.author: "pablocan"
---

# MSMapElementLayerUserDidTapFlyoutHandler Interface (iOS only)

Handler used with MapElementLayer.MapFlyoutTapped event. Return true from this event to indicate whether it has been handled, or false otherwise.

>```objectivec
> typedef BOOL (^MSMapElementLayerUserDidTapFlyoutHandler)(MSMapFlyout *_Nonnull, MSMapIcon *_Nonnull)
>```

## See Also

* [MapFlyout](../MapFlyout-class.md)
* [MapIcon](../MapIcon-class.md)