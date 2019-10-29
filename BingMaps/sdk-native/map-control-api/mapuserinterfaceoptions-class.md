---
title: "MapUserInterfaceOptions Class | Microsoft Docs"
author: "bmnxplat"
---

# MapUserInterfaceOptions Class

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
