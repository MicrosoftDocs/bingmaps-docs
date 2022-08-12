---
title: MapCameraChangeReason Enumeration | Microsoft Docs
description: Describes the MapCameraChangeReason enumeration for Android and iOS and provides the enumeration's syntax and System, UserInteraction, and Programmatic values.
ms.author: pablocan
---

# MapCameraChangeReason Enumeration

Specifies the reason the position of the map's camera has changed.

**Android**

>```java 
> public enum MapCameraChangeReason 
> {
>     SYSTEM,
>     USER_INTERACTION,
>     PROGRAMMATIC,
> }
>```

**iOS**

>```objectivec 
> typedef NS_ENUM(NSInteger, MSMapCameraChangeReason)
> {
>      MSMapCameraChangeReasonSystem = 0,
>      MSMapCameraChangeReasonUserInteraction,
>      MSMapCameraChangeReasonProgrammatic
> }
>```

### System
The system changed the position of the map's camera.

### UserInteraction
The user manually changed the position of the map's camera.

### Programmatic
The position of the map's camera changed programmatically.
