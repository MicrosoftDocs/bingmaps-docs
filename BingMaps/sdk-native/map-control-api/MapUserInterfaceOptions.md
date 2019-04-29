
# MapUserInterfaceOptions class

A container class for various properties that can be used to configure interactivity for the control.

**Android**

>```java
> public class MapUserInterfaceOptions
>```

**iOS**

> ```objectivec
> @interface MSMapUserInterfaceOptions : NSObject
>```

## Properties

### isZoomButtonsVisible

Whether the zoom in and zoom out buttons are displayed.

**Android**

>```java
> boolean isZoomButtonsVisible()
> void setZoomButtonsVisible(final boolean visible)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL isZoomButtonsVisible
>```

### isCompassButtonVisible

Whether the compass is displayed.

**Android**

>```java
> boolean isCompassButtonVisible()
> void setCompassButtonVisible(boolean visible)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL isCompassButtonVisible
>```

### isTiltButtonVisible

Whether the tilt button is displayed.

**Android**

>```java
> boolean isTiltButtonVisible()
> void setTiltButtonVisible(boolean visible)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL isTiltButtonVisible
>```

### isMyLocationButtonVisible

Whether my location button is displayed.

**Android**

>```java
> boolean isMyLocationButtonVisible()
> void setMyLocationButtonVisible(boolean visible)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL isMyLocationButtonVisible
>```

### isRotateGesturesEnabled

Whether a user can use a twisting rotate finger gesture to rotate out of north-up

**Android**

>```java
> boolean isRotateGesturesEnabled()
> void setRotateGesturesEnabled(boolean enabled)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL isRotateEnabled
>```

### isTiltGesturesEnabled

Whether a user can use a two-finger gesture to tilt in and out of nadir views.

**Android**

>```java
> boolean isTiltGesturesEnabled()
> void setTiltGesturesEnabled(boolean enabled)
>```

**iOS**

> ```objectivec
> @property (nonatomic) BOOL isTiltEnabled
>```

### isPanGesturesEnabled

Whether a user can pan (scroll) the map around using gestures

**Android**

>```java
> boolean isPanGesturesEnabled()
> void setPanGesturesEnabled(boolean enabled)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL isPanEnabled
>```

### isZoomGesturesEnabled

Whether a user can use a two-finger gesture to zoom in and out of the map.

**Android**

>```java
> boolean isZoomGesturesEnabled()
> void setZoomGesturesEnabled(boolean enabled)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL isZoomEnabled
>```

### CopyrightDisplay

Controls whether copyright is displayed on mobile form factor sized MapViews. This is only available to internal Microsoft customers.

**Android**

>```java
> CopyrightDisplay getCopyrightDisplay()
> void setCopyrightDisplay(CopyrightDisplay copyrightDisplay)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL isCopyrightVisible
>```
