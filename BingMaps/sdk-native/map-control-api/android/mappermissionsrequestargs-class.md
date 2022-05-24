---
title: MapPermissionsRequestArgs Class | Microsoft Docs
description: Describes the MapPermissionsRequestArgs class for Android and outlines the Permissions, Reason, and Callback properties.
ms.author: sasakthi
---

# MapPermissionsRequestArgs Class (Android only)

Contains arguments passed to MapPermissionsDelegate with a request for permissions.

## Properties

### Permissions

An array of permission identifiers.

>```java
> final String[] permissions
>```

### Reason

A MapPermissionsRequestReason value indicating the origin of the request.

>```java
> final MapPermissionsRequestReason reason
>```

### Callback

A callback for the client to call upon receiving permissions result.

>```java
> final WeakReference<MapPermissionsCallback> callback
>```

## See Also

* [MapPermissionsCallback](mappermissionscallback-interface.md)
* [MapPermissionsDelegate](mappermissionsdelegate-interface.md)
* [MapPermissionsRequestReason](mappermissionsrequestreason-enumeration.md)
