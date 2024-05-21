---
title: MapStylePickerSelectedStyleChangedEventArgs Class | Microsoft Docs
description: Describes the MapStylePickerSelectedStyleChangedEventArgs class for Android and outlines the SelectStyle and StyleSheet properties.
ms.author: pablocan
---

# MapStylePickerSelectedStyleChangedEventArgs Class (Android only)

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Event arguments passed to UserInterfaceOptions.MapStylePickerSelectedStyleChanged callback. Update the `selectedStyle` event argument if working with a customized basemap style and return true to have it applied to the the map.

## Properties

### SelectedStyle

Gets the selected style from within the map style picker.

>```java
> MapStylePickerStyle getSelectedStyle()
>```

### StyleSheet

Gets the base map style sheet for the selected style.

>```java
> MapStyleSheet getStyleSheet()
> void setStyleSheet(MapStyleSheet mapStyleSheet)
>```

## See Also

* [OnMapStylePickerSelectedStyleChangedListener](OnMapStylePickerSelectedStyleChangedListener-interface.md)
* [MapStylePickerStyle](../MapStylePickerStyle-enumeration.md)
* [MapStyleSheet](../MapStyleSheet-class.md)
