---
title: OnMapLoadingStatusChangedListener Interface | Microsoft Docs
description: Describes the OnMapLoadingStatusChangedListener interface for Android and provides the MapLoadingStatus and MapView references.
ms.author: pablocan
---

# OnMapLoadingStatusChangedListener Interface (Android only)

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Listener used with MapView.MapLoadingStatusChanged event.

>```java
> public interface OnMapLoadingStatusChangedListener
> {
>    /** Called when the map loading status changes **/
>    boolean onMapLoadingStatusChanged(MapLoadingStatus status);
> }
>```

## See Also

* [MapLoadingStatus](../maploadingstatus-enumeration.md)
* [MapView](../MapView-class.md)
