
# Enabling/Disabling User Interface Gestures and Controls

By default, our map shows a toolbar with controls that the user can use to navigate the map. These controls are zoom, compass, and location.

![User Interface Controls](media/User-interface-controls.png)

Our map also supports multiple gestures to navigate, such as pan, rotate, tilt, and zoom.

In some scenarios, it may be desirable to disable these controls and/or gestures.

## Examples

### Disable Zoom Controls and Gestures

**Android**

>``` Java
> MapUserInterfaceOptions uiOptions = mMap.getUserInterfaceOptions();
> // disable zoom control
> uiOptions.setZoomButtonsVisible(false);
> // disable zoom gesture
> uiOptions.setZoomGestureEnabled(false);
>```

**Swift**

>``` swift
> let uiOptions = self.mapView.userInterfaceOptions
> // disable zoom control
> uiOptions.zoomButtonsVisible  = false
> // disable zoom gesture
> uiOptions.zoomGestureEnabled = false
>```

**Objective-C**

>``` objectivec
> MSMapUserInterfaceOptions *uiOptions = [self.mapView userInterfaceOptions];
> // disable zoom control
> uiOptions.zoomButtonsVisible  = NO
> // disable zoom gesture
> uiOptions.zoomGestureEnabled  = NO
>```