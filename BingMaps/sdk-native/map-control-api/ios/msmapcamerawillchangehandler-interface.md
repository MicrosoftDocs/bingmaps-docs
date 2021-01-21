---
title: "MSMapCameraWillChangeHandler Interface | Microsoft Docs"
author: "pablocan"
---

# MSMapCameraWillChangeHandler Interface (iOS only)

Handler used with MapView.CameraChanging event. Return true from this event to indicate whether it has been handled, or false otherwise.

>```objectivec
> typedef BOOL (^MSMapCameraWillChangeHandler)(MSMapCameraChangeReason, MSMapCamera*, BOOL)
>```

## See Also

* [MapCameraChangeReason](../MapCameraChangeReason-enumeration.md)
* [MapView](../MapView-class.md)