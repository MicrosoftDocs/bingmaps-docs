
# MSMapLoadingStatusDidChangeHandler interface (iOS only)

Handler used with MapView.MapLoadingStatusChanged event. Return true from this event to indicate whether it has been handled, or false otherwise.

>```objectivec 
> typedef BOOL (^MSMapLoadingStatusDidChangeHandler)(MSMapLoadingStatus)
>```

## See also

* [MapLoadingStatus](../MapLoadingStatus-enumeration.md)
* [MapView](../MapView-class.md)