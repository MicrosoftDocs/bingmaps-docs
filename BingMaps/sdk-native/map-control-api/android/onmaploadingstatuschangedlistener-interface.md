---
title: OnMapLoadingStatusChangedListener Interface | Microsoft Docs
description: Describes the OnMapLoadingStatusChangedListener interface for Android and provides the MapLoadingStatus and MapView references.
ms.author: pablocan
---

# OnMapLoadingStatusChangedListener Interface (Android only)

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
