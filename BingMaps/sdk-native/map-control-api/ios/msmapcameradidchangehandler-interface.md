---
title: "MSMapCameraDidChangeHandler Interface | Microsoft Docs"
author: "pablocan"
---

# MSMapCameraDidChangeHandler Interface (iOS only)

Handler used with MapView.CameraChanged event. Return true from this event to indicate whether it has been handled, or false otherwise.

>```objectivec
> typedef BOOL (^MSMapCameraDidChangeHandler)(MSMapCameraChangeReason, MSMapCamera*, BOOL)
>```

## See Also

* [MapCameraChangeReason](../MapCameraChangeReason-enumeration.md)
* [MapView](../MapView-class.md)