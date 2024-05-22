---
title: MapUserLocationTrackingMode Enumeration | Microsoft Docs
description: Describes the MapUserLocationTrackingMode enumeration for Android and iOS and provides the enumeration's None and CenteredOnUser values.
ms.author: adl
---

# MapUserLocationTrackingMode Enumeration

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Specifies the tracking mode of user location.

**Android**

>```java
> public enum MapUserLocationTrackingMode {
>   NONE,
>   CENTERED_ON_USER
> }
>```

**iOS**

>```objectivec
> typedef NS_ENUM(NSInteger, MSMapUserLocationTrackingMode) {
>   MSMapUserLocationTrackingModeNone,
>   MSMapUserLocationTrackingModeCenteredOnUser
> };
>```

## Values

### None

The camera will not be tracking the user's location.

### CenteredOnUser

The camera will center on the user's location until the user interrupts tracking by interacting with the map.

## See Also

* [MapUserLocation](mapuserlocation-class.md)