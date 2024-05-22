---
title: MSMapUserLocationTrackingInterruptedHandler Interface | Microsoft Docs
description: Describes the MSMapUserLocationTrackingInterruptedHandler interface for iOS and provides the interface's syntax and additional references.
ms.author: adl
---

# MSMapUserLocationTrackingInterruptedHandler Interface (iOS only)

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Handler used with UserLocation's tracking interrupted event. Return true from this event to prevent other listeners from receiving this event or false to allow other listeners to receive this notification as well.

>```objectivec
> typedef BOOL (^MSMapUserLocationTrackingInterruptedHandler)(MSMapUserLocationTrackingInterruptedEventArgs* _Nonnull)
>```

## See Also

* [MSMapUserLocationTrackingInterruptedEventArgs](msmapuserlocationtrackinginterruptedeventargs-class.md)
* [MapUserLocation](../mapuserlocation-class.md)