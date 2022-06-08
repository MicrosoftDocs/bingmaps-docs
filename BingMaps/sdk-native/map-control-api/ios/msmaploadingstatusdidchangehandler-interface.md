---
title: MSMapLoadingStatusDidChangeHandler Interface | Microsoft Docs
description: Describes the MSMapLoadingStatusDidChangeHandler interface for iOS and provides the interface's syntax and additional references.
ms.author: pablocan
---

# MSMapLoadingStatusDidChangeHandler Interface (iOS only)

Handler used with MapView.MapLoadingStatusChanged event. Return true from this event to indicate whether it has been handled, or false otherwise.

>```objectivec
> typedef BOOL (^MSMapLoadingStatusDidChangeHandler)(MSMapLoadingStatus)
>```

## See Also

* [MapLoadingStatus](../MapLoadingStatus-enumeration.md)
* [MapView](../MapView-class.md)