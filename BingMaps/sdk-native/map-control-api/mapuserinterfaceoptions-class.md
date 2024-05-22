---
title: MapUserInterfaceOptions Class | Microsoft Docs
description: Describes the MapUserInterfaceOptions class for Android and iOS and provides the class's properties, methods, and events.
ms.author: pablocan
---

# MapUserInterfaceOptions Class

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

A container class for various properties that can be used to configure interactivity for the control.

**Android**

>```java
> public class MapUserInterfaceOptions
>```

**iOS**

>```objectivec
> @interface MSMapUserInterfaceOptions : NSObject
>```

## Properties

### CompassButtonAlignment

The horizontal and vertical alignment of the compass button within the map.

**Android**

>```java
> setCompassButtonAlignment(
>   MapToolbarHorizontalAlignment horizontalAlignment,
>   MapToolbarVerticalAlignment verticalAlignment)
>```

**iOS**

>```objectivec
> - (void)setCompassButtonHorizontalAlignment:(MSMapToolbarHorizontalAlignment)horizontalAlignment verticalAlignment:(MSMapToolbarVerticalAlignment)verticalAlignment
>```

_See also:_ [MapToolbarHorizontalAlignment enumeration](MapToolbarHorizontalAlignment-enumeration.md)
_See also:_ [MapToolbarVerticalAlignment enumeration](MapToolbarVerticalAlignment-enumeration.md)

### CompassButtonVisible

Whether the compass is displayed.

**Android**

>```java
> boolean isCompassButtonVisible()
> void setCompassButtonVisible(boolean visible)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL compassButtonVisible
>```

### StylePickerButtonAlignment

The horizontal and vertical alignment of the style picker button within the map.

**Android**

>```java
> setStylePickerButtonAlignment(
>   MapToolbarHorizontalAlignment horizontalAlignment,
>   MapToolbarVerticalAlignment verticalAlignment)
>```

**iOS**

>```objectivec
> - (void)setStylePickerButtonHorizontalAlignment:(MSMapToolbarHorizontalAlignment)horizontalAlignment verticalAlignment:(MSMapToolbarVerticalAlignment)verticalAlignment
>```

_See also:_ [MapToolbarHorizontalAlignment enumeration](MapToolbarHorizontalAlignment-enumeration.md)
_See also:_ [MapToolbarVerticalAlignment enumeration](MapToolbarVerticalAlignment-enumeration.md)

### StylePickerButtonVisible

Whether the style picker button is displayed.

**Android**

>```java
> boolean isStylePickerButtonVisible()
> void setStylePickerButtonVisible(boolean visible)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL stylePickerButtonVisible
>```

### TiltButtonAlignment

The horizontal and vertical alignment of the tilt button within the map.

**Android**

>```java
> setTiltButtonAlignment(
>   MapToolbarHorizontalAlignment horizontalAlignment,
>   MapToolbarVerticalAlignment verticalAlignment)
>```

**iOS**

>```objectivec
> - (void)setTiltButtonHorizontalAlignment:(MSMapToolbarHorizontalAlignment)horizontalAlignment verticalAlignment:(MSMapToolbarVerticalAlignment)verticalAlignment
>```

_See also:_ [MapToolbarHorizontalAlignment enumeration](MapToolbarHorizontalAlignment-enumeration.md)
_See also:_ [MapToolbarVerticalAlignment enumeration](MapToolbarVerticalAlignment-enumeration.md)

### TiltButtonVisible

Whether the tilt button is displayed.

**Android**

>```java
> boolean isTiltButtonVisible()
> void setTiltButtonVisible(boolean visible)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL tiltButtonVisible
>```

### UserLocationButtonAlignment

The horizontal and vertical alignment of the user location button within the map.

**Android**

>```java
> setUserLocationButtonAlignment(
>   MapToolbarHorizontalAlignment horizontalAlignment,
>   MapToolbarVerticalAlignment verticalAlignment)
>```

**iOS**

>```objectivec
> - (void)setUserLocationButtonHorizontalAlignment:(MSMapToolbarHorizontalAlignment)horizontalAlignment verticalAlignment:(MSMapToolbarVerticalAlignment)verticalAlignment
>```

_See also:_ [MapToolbarHorizontalAlignment enumeration](MapToolbarHorizontalAlignment-enumeration.md)
_See also:_ [MapToolbarVerticalAlignment enumeration](MapToolbarVerticalAlignment-enumeration.md)

### UserLocationButtonVisible

Whether the user location button is displayed.

**Android**

>```java
> boolean isUserLocationButtonVisible()
> void setUserLocationButtonVisible(boolean visible)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL userLocationButtonVisible
>```

### ZoomButtonsAlignment

The horizontal and vertical alignment of the zoom buttons within the map.

**Android**

>```java
> setZoomButtonsAlignment(
>   MapToolbarHorizontalAlignment horizontalAlignment,
>   MapToolbarVerticalAlignment verticalAlignment)
>```

**iOS**

>```objectivec
> - (void)setZoomButtonsHorizontalAlignment:(MSMapToolbarHorizontalAlignment)horizontalAlignment verticalAlignment:(MSMapToolbarVerticalAlignment)verticalAlignment
>```

_See also:_ [MapToolbarHorizontalAlignment enumeration](MapToolbarHorizontalAlignment-enumeration.md)
_See also:_ [MapToolbarVerticalAlignment enumeration](MapToolbarVerticalAlignment-enumeration.md)

### ZoomButtonsVisible

Whether the zoom in and zoom out buttons are displayed.

**Android**

>```java
> boolean isZoomButtonsVisible()
> void setZoomButtonsVisible(final boolean visible)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL zoomButtonsVisible
>```


### PanGestureEnabled

Whether a user can pan (scroll) the map around using gestures

**Android**

>```java
> boolean isPanGestureEnabled()
> void setPanGestureEnabled(boolean enabled)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL panGestureEnabled
>```


### RotateGestureEnabled

Whether a user can use a twisting rotate finger gesture to rotate out of north-up

**Android**

>```java
> boolean isRotateGestureEnabled()
> void setRotateGestureEnabled(boolean enabled)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL rotateGestureEnabled
>```


### TiltGestureEnabled

Whether a user can use a two-finger gesture to tilt in and out of nadir views.

**Android**

>```java
> boolean isTiltGestureEnabled()
> void setTiltGestureEnabled(boolean enabled)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL tiltGestureEnabled
>```


### ZoomGestureEnabled

Whether a user can use a two-finger gesture to zoom in and out of the map.

**Android**

>```java
> boolean isZoomGestureEnabled()
> void setZoomGestureEnabled(boolean enabled)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL zoomGestureEnabled
>```


### CopyrightDisplay

Controls whether copyright is displayed on mobile form factor sized map views.

**Android**

>```java
> CopyrightDisplay getCopyrightDisplay()
> void setCopyrightDisplay(CopyrightDisplay copyrightDisplay)
>```

**iOS**

>```objectivec
> @property (nonatomic) MSCopyrightDisplay copyrightDisplay
>```

_See also:_ [CopyrightDisplay enumeration](copyrightdisplay-enumeration.md)

### SaveMapUserPreferences

Controls whether style and traffic preferences selected through the style picker are saved. If enabled, the user's style preferences should be persisted and restored on subsequent sessions.

**Android**

>```java
> boolean isSaveMapUserPreferencesEnabled()
> void setSaveMapUserPreferencesEnabled(boolean enabled)
>```

**iOS**

>```objectivec
> @property(nonatomic) BOOL saveMapUserPreferencesEnabled
>```

## Methods

### ClearMapUserPreferences

Clears the user's preferences from memory.

**Android**

>```java
> void clearMapUserPreferences()
>```

**iOS**

>```objectivec
> - (void)clearMapUserPreferences;
>```

## Events

### MapStylePickerSelectedStyleChanged

Fired when a style is selected in the map style picker, or a previous selection is being restored.

**Android**

>```java
> void setOnMapStylePickerSelectedStyleChangedListener(OnMapStylePickerSelectedStyleChangedListener listener)
>```

_See also:_ [OnMapStylePickerSelectedStyleChangedListener](Android/OnMapStylePickerSelectedStyleChangedListener-interface.md)

**iOS**

>```objectivec
> - (void)setUserDidSelectStyleHandler:(MSMapUserDidSelectStyleHandler)handler
>```

_See also:_ [MSMapUserDidSelectStyleHandler](iOS/MSMapUserDidSelectStyleHandler-interface.md)

### MapStylePickerTrafficSwitchToggled

Fired when the switch is toggled in the map style picker, or a previous toggle is being restored.

**Android**

>```java
> void setOnMapStylePickerTrafficSwitchToggledListener(OnMapStylePickerTrafficSwitchToggledListener listener)
>```

_See also:_ [OnMapStylePickerTrafficSwitchToggledListener](Android/OnMapStylePickerTrafficSwitchToggledListener-interface.md)

**iOS**

>```objectivec
> - (void)setUserDidToggleTrafficSwitch:(MSMapUserDidToggleTrafficSwitchHandler)handler
>```

_See also:_ [MSMapUserDidToggleTrafficSwitchHandler](iOS/MSMapUserDidToggleTrafficSwitchHandler-interface.md)