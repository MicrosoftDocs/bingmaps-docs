
# MSMapCameraWillChangeHandler interface (iOS only)

Handler used with MapView.CameraChanging event. Return true from this event to indicate whether it has been handled, or false otherwise.

>```objectivec
> typedef BOOL (^MSMapCameraWillChangeHandler)(MSMapCameraChangeReason, MSMapCamera*, BOOL) 
>```

## See also

* [MapCameraChangeReason](../MapCameraChangeReason-enumeration.md)
* [MapView](../MapView-class.md)