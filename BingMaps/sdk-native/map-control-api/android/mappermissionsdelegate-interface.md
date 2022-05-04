---
title: "MapPermissionsDelegate Interface | Microsoft Docs"
description: Learn about the MapPermissionsDelegate interface.
ms.author: v-munksteve
---

# MapPermissionsDelegate Interface (Android only)

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
