---
title: "MSMapLocationChangedEventArgs Class | Microsoft Docs"
ms.author: "adl"
---

# MSMapLocationChangedEventArgs Class (iOS only)

Event arguments passed to MSMapLocationProvider's location changed callback.

>```objectivec
> @interface MSMapLocationChangedEventArgs : NSObject
>```

## Properties

### Location

The location of the user that was just changed.

>```objectivec
> @property(nonatomic, readonly) CLLocation* location
>```

## See Also

* [MSMapLocationChangedHandler](msmaplocationchangedhandler-interface.md)
* [MSMapLocationProvider](msmaplocationprovider-class.md)
