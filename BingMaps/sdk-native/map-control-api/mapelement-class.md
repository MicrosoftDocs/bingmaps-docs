---
title: MapElement Class | Microsoft Docs
description: Describes the MapElement class for Android and iOS and provides the class' properties, accessibility elements, and additional references.
ms.author: pablocan
---

# MapElement Class

Represents an element displayed on a MapControl.

**Android**

>```java
> public abstract class MapElement
>```

**iOS**

>```objectivec
> @interface MSMapElement : UIAccessibilityElement
>```

## Properties

### MapStyleSheetEntry

Gets or sets the name of an entry in the map's style sheet that you'd like to apply to this MapElement. Set this property to a string or to any of the property values available in the [MapStyleSheetEntries](/uwp/api/windows.ui.xaml.controls.maps.mapstylesheetentries) class.

**Android**

>```java
> String getMapStyleSheetEntry()
> void setMapStyleSheetEntry(@Nullable String mapStyleSheetEntry)
>```

**iOS**

>```objectivec
> @property (nonatomic, nullable) NSString *mapStyleSheetEntry;
>```

_See also:_ 
* [MapStyleSheet](MapStyleSheet-class.md)
* [Map Style Sheet Reference](/bingmaps/styling/map-style-sheet-entries)  

### MapStyleSheetEntryState

Gets or sets the name of the state of this MapElement. If the style sheet defines a style for that state, that style is applied to this element. Values defined in the style sheet for the state override values defined in the MapStyleSheetEntry.

**Android**

>```java
> String getMapStyleSheetEntryState()
> void setMapStyleSheetEntryState(@Nullable String mapStyleSheetEntryState)
>```

**iOS**

>```objectivec
> @property (nonatomic, nullable) id mapStyleSheetEntryState;
>```

_See also:_ 
* [MapStyleSheet](MapStyleSheet-class.md)
* [Map Style Sheet Reference](/bingmaps/styling/map-style-sheet-entries)   

### Tag

Gets or sets an arbitrary object value that can be used to store custom information about this object.

**Android**

>```java
> @Nullable Object getTag()
> void setTag(@Nullable Object newTag)
>```

**iOS**

>```objectivec
> @property (nonatomic) id tag;
>```

### Visible

Whether the item is visible or not.

**Android**

>```java
> boolean isVisible()
> void setVisible(boolean visible)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL visible
>```

### ZIndex

The ZIndex of the map element. Elements with a higher ZIndex will render on top of elements with a lower ZIndex.

**Android**

>```java
> int getZIndex()
> void setZIndex(int zIndex)
>```

**iOS**

>```objectivec
> @property (nonatomic) int zIndex
>```


## Accessibility

Map elements are accessible via corresponding accessibility traits depending on the platform.  
***Note: It is recommended to provide accessibility descriptions for user elements. User elements with missing descriptions will not be accessible.***

### ContentDescription property (Android)

Describes the element for accessibility services.

>```java
> @Nullable CharSequence getContentDescription()
> void setContentDescription(@Nullable CharSequence description)
>```

### UIAccessibilityElement superclass (iOS)

`MSMapElement` inherits from `UIAccessibilityElement` where the information about the element can be provided. Please refer to
[official documentation](https://developer.apple.com/documentation/uikit/uiaccessibilityelement) for usage and details.


## See Also

* [MapIcon](MapIcon-class.md)
* [MapPolyline](MapPolyline-class.md)
* [MapPolygon](MapPolygon-class.md)
