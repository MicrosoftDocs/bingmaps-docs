---
title: "MSMapUserDidSelectStyleEventArgs Class | Microsoft Docs"
author: "pablocan"
---

# MSMapUserDidSelectStyleEventArgs Class (iOS only)

Event arguments passed to UserInterfaceOptions.MapUserDidSelectStyle callback.

>```objectivec
> @interface MSMapUserDidSelectStyleEventArgs : NSObject
>```

## Properties

### SelectedStyle

Gets the selected style from within the map style picker.

>```objectivec
> @property(nonatomic, readonly) MSMapStylePickerStyle selectedStyle
>```

### StyleSheet

Gets the base map style sheet for the selected style.

>```objectivec
> @property(nonatomic) MSMapStyleSheet* styleSheet
>```

## See Also

* [MSMapUserDidSelectStyleHandler](MSMapUserDidSelectStyleHandler-interface.md)
* [MapUserInterfaceOptions](../MapUserInterfaceOptions-class.md)
* [MSMapStylePickerStyle](../MapStylePickerStyle-enumeration.md)
* [MSMapStyleSheet](../MapStyleSheet-class.md)
