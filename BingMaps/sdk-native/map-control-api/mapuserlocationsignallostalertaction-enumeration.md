---
title: MapUserLocationSignalLostAlertAction Enumeration | Microsoft Docs
description: Describes the MapUserLocationSignalLostAlertAction enumeration for Android and iOS and provides the enumeration's Ignore and Show values.
ms.author: adl
---

# MapUserLocationSignalLostAlertAction Enumeration

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Specifies the action that should be taken for signal lost alerts.

**Android**

>```java
> public enum MapUserLocationSignalLostAlertAction {
>   IGNORE,
>   SHOW
> }
>```

**iOS**

>```objectivec
> typedef NS_ENUM(NSInteger, MSMapUserLocationSignalLostAlertAction) {
>   MSMapUserLocationSignalLostAlertActionIgnore,
>   MSMapUserLocationSignalLostAlertActionShow
> };
>```

## Values

### Ignore

Ignore and don't show the signal lost alert.

### Show

Show the signal lost alert.

## See Also

* [MapUserLocation](mapuserlocation-class.md)