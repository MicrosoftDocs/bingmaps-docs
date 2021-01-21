---
title: "MapUserLocationSignalLostAlertAction Enumeration | Microsoft Docs"
ms.author: "adl"
---

# MapUserLocationSignalLostAlertAction Enumeration

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