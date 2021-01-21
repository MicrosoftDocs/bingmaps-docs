---
title: "MSMapLocationChangedHandler Interface | Microsoft Docs"
author: "adl"
---

# MSMapLocationChangedHandler Interface (iOS only)

Handler used with MSMapLocationProvider's location changed event. Return true from this event to prevent other listeners from receiving this event or false to allow other listeners to receive this notification as well.

>```objectivec
> typedef BOOL (^MSMapLocationChangedHandler)(MSMapLocationChangedEventArgs* _Nonnull);
>```

## See Also

* [MSMapLocationChangedEventArgs](msmaplocationchangedeventargs-class.md)
* [MSMapLocationProvider](msmaplocationprovider-class.md)