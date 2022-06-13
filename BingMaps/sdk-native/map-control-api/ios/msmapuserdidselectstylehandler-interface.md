---
title: MSMapUserDidSelectStyleHandler Interface | Microsoft Docs
description: Describes the MSMapUserDidSelectStyleHandler interface for iOS and provides the interface's syntax and additional references.
ms.author: pablocan
---

# MSMapUserDidSelectStyleHandler Interface (iOS only)

Listener used with UserInterfaceOptions.MapUserDidSelectStyle event. Update the `selectedStyle` event argument if working with a customized basemap style and return true to have it applied to the the map.

>```objectivec
> typedef BOOL (^MSMapUserDidSelectStyleHandler)(MSMapUserDidSelectStyleEventArgs* _Nonnull);
>```

## See Also

* [MSMapUserDidSelectStyleEventArgs](MSMapUserDidSelectStyleEventArgs-class.md)