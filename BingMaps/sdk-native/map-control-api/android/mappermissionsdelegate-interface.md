---
title: MapPermissionsDelegate Interface | Microsoft Docs
description: Describes the MapPermissionsDelegate interface for Android and provides the MapPermissionsCallback, RequestArgs, RequestReason, and MapView references.
ms.author: sasakthi
---

# MapPermissionsDelegate Interface (Android only)

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Delegates permission requests to the client in order to forward to the Android framework.

>```java
> public interface MapPermissionsDelegate
> {
>     void requestPermissions(MapPermissionsRequestArgs args);
> }
>```

## See Also

* [MapPermissionsCallback](mappermissionscallback-interface.md)
* [MapPermissionsRequestArgs](mappermissionsrequestargs-class.md)
* [MapPermissionsRequestReason](mappermissionsrequestreason-enumeration.md)
* [MapView](../mapview-class.md)
