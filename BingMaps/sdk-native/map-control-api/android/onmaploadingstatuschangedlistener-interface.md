---
title: "OnMapLoadingStatusChangedListener Interface | Microsoft Docs"
author: "pablocan"
---

# OnMapLoadingStatusChangedListener Interface (Android only)

Listener used with MapView.MapLoadingStatusChanged event.

>```java
> public interface OnMapLoadingStatusChangedListener
> {
>    /** Called when the map loading status changes **/
>    public boolean onMapLoadingStatusChanging(MapLoadingStatus status);
> }
>```

## See also

* [MapLoadingStatus](../maploadingstatus-enumeration.md)
* [MapView](../MapView-class.md)