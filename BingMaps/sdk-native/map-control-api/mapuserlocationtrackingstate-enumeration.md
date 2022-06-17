---
title: MapUserLocationTrackingState Enumeration | Microsoft Docs
description: Describes the MapUserLocationTrackingState enumeration for Android and iOS and provides the enumeration's values and additional references.
ms.author: adl
---

# MapUserLocationTrackingState Enumeration

Specifies the tracking state of user location.

**Android**

>```java
> public enum MapUserLocationTrackingState {
>   PERMISSION_DENIED,
>   READY,
>   DISABLED
> }
>```

**iOS**

>```objectivec
> typedef NS_ENUM(NSInteger, MSMapUserLocationTrackingState) {
>   MSMapUserLocationTrackingStatePermissionDenied,
>   MSMapUserLocationTrackingStateReady,
>   MSMapUserLocationTrackingStateDisabled
> };
>```

## Values

### PermissionDenied

Tracking was unable to start due to missing location permissions.

### Ready

Tracking has started sucessfully.

### Disabled

Tracking was unable to start due to providers being disabled.

## See Also

* [MapUserLocation](mapuserlocation-class.md)