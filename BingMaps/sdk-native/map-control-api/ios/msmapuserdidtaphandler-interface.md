---
title: MSMapUserDidTapHandler Interface | Microsoft Docs
description: Describes the MSMapUserDidTapHandler interface for iOS and provides the interface's syntax and additional references.
ms.author: pablocan
---

# MSMapUserDidTapHandler Interface (iOS only)

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Handler used with MapView.Tapped event. Return true from this event to prevent other OnMapTappedListeners from receiving this event or false to allow other listeners to receive his notification as well. Events are processed in the order they were attached to the MapView.

>```objectivec
> typedef BOOL (^MSMapUserDidTapHandler)(CGPoint, MSGeopoint*)
>```

## See Also

* [Geopoint](../Geopoint-class.md)
* [MapView](../MapView-class.md)