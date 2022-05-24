---
title: MapPermissionsRequestReason Enumeration | Microsoft Docs
description: Describes the MapPermissionsRequestReason enumeration for Android and outlines the UserInteraction and Programmatic values.
ms.author: rkot
---

# MapPermissionsRequestReason Enumeration (Android only)

Specifies the reason for a permissions request.

>```java
> enum MapPermissionsRequestReason
> {
>     USER_INTERACTION,
>     PROGRAMMATIC
> }
>```

## Values

### UserInteraction

Permissions required for a scenario originating from the UI.

### Programmatic

Permissions required for a scenario originating from the API.

## See Also

* [MapPermissionsCallback](mappermissionscallback-interface.md)
* [MapPermissionsDelegate](mappermissionsdelegate-interface.md)
* [MapPermissionsRequestArgs](mappermissionsrequestargs-class.md)
