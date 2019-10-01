
# MSMapCameraDidChangeHandler interface (iOS only)

Handler used with MapView.CameraChanged event. Return true from this event to indicate whether it has been handled, or false otherwise.

>```objectivec
> typedef BOOL (^MSMapCameraDidChangeHandler)(MSMapCameraChangeReason, MSMapCamera*) 
>```

## See also

* [MapCameraChangeReason](../MapCameraChangeReason-enumeration.md)
* [MapView](../MapView-class.md)