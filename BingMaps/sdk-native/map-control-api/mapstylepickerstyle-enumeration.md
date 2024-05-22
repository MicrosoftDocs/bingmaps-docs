---
title: MapStylePickerStyle Enumeration | Microsoft Docs
description: Describes the MapStylePickerStyle enumeration for Android and iOS and provides the enumeration's values and additional references.
ms.author: pablocan
---

# MapStylePickerStyle Enumeration

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Defines the tapped style within the style picker.

**Android**

>```java
> public enum MapStylePickerStyle
> {
>     DEFAULT,
>     DARK,
>     AERIAL
> }
>```

**iOS**

>```objectivec
> typedef NS_ENUM(NSInteger, MSMapStylePickerStyle)
> {
>     MapStylePickerStyleDefault,
>     MapStylePickerStyleDark,
>     MapStylePickerStyleAerial
> }
>```

## Values

### Default

The default style.

### Dark

The dark style.

### Aerial

The aerial style.

## See Also

* [MapUserInterfaceOptions](MapUserInterfaceOptions-class.md)
