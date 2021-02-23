---
title: "MapLoadingStatus Enumeration | Microsoft Docs"
ms.author: "pablocan"
---

# MapLoadingStatus Enumeration

Specifies the LoadingStatus of the MapControl.

**Android**

>```java
> public enum MapLoadingStatus
> {
>     UPDATING,
>     COMPLETE,
>     COMPLETE_WITH_MISSING_DATA
> }
>```

**iOS**

>```objectivec
> typedef NS_ENUM(NSInteger, MSMapLoadingStatus)
> {
>     MSMapLoadingStatusUpdating = 0,
>     MSMapLoadingStatusComplete,
>     MSMapLoadingStatusCompleteWithMissingData
> };
>```

## Values

### Updating

The MapView is still in the process of downloading additional data needed to render the current view.

### Complete

The MapView has downloaded all needed data to render the current view

### CompleteWithMissingData

The MapView has downloaded all it can to render the current view, but some resources were unable to be downloaded.

## See Also

* [MapView](MapView-class.md)