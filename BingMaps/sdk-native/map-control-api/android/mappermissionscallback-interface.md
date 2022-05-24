---
title: MapPermissionsCallback Interface | Microsoft Docs
description: Describes the MapPermissionsCallback interface for Android and provides the MapPermissionsDelegate, RequestArgs, and RequestReason references.
ms.author: sasakthi
---

# MapPermissionsCallback Interface (Android only)

Provides a callback for the client to call upon receiving permissions result.

>```java
> public interface MapPermissionsCallback
> {
>     void onPermissionsResult(String[] permissions, int[] grantResults);
> }
>```

## See Also

* [MapPermissionsDelegate](mappermissionsdelegate-interface.md)
* [MapPermissionsRequestArgs](mappermissionsrequestargs-class.md)
* [MapPermissionsRequestReason](mappermissionsrequestreason-enumeration.md)
