# User Interface Gestures and Controls

By default, the map shows a toolbar with controls that the user can use to navigate the map. These controls are compass, zoom and tilt.

![User Interface Controls](media/User-interface-controls.png)

Our map engine also supports multiple gestures to navigate, such as pan, rotate, tilt, and zoom.

In some scenarios, it may be desirable to enable / disable these controls and/or gestures.

## Examples

### Disable Zoom Controls and Gestures

**Android**

>```java
> MapUserInterfaceOptions uiOptions = mMap.getUserInterfaceOptions();
> uiOptions.setZoomButtonsVisible(false);
> uiOptions.setZoomGestureEnabled(false);
>```

**Swift**

>```swift
> let uiOptions = self.mapView.userInterfaceOptions
> uiOptions.zoomButtonsVisible = false
> uiOptions.zoomGestureEnabled = false
>```

**Objective-C**

>```objectivec
> MSMapUserInterfaceOptions *uiOptions = self.mapView.userInterfaceOptions;
> uiOptions.zoomButtonsVisible = NO;
> uiOptions.zoomGestureEnabled = NO;
>```
