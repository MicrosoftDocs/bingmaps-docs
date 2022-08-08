---
title: OnMapStylePickerTrafficSwitchToggledListener Interface | Microsoft Docs
description: Describes the OnMapStylePickerTrafficSwitchToggledListener interface for Android and provides syntax and additional references.
ms.author: pablocan
---

# OnMapStylePickerTrafficSwitchToggledListener Interface (Android only)

Listener used with UserInterfaceOptions.MapStylePickerTrafficSwitchToggled event.

>```java
> public interface OnMapStylePickerTrafficSwitchToggledListener
>{
>    /** Called when the traffic switch is toggled. */
>    boolean onTrafficSwitchToggled(MapStylePickerTrafficSwitchToggledEventArgs e);
>}
>```

## See Also

* [MapStylePickerTrafficSwitchToggledEventArgs](MapStylePickerTrafficSwitchToggledEventArgs-class.md)
* [MapUserInterfaceOptions](../MapUserInterfaceOptions-class.md)