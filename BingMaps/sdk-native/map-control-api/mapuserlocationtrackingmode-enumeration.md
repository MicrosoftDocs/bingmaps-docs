---
title: "MapUserLocationTrackingMode Enumeration | Microsoft Docs"
ms.author: "adl"
---

# MapUserLocationTrackingMode Enumeration

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