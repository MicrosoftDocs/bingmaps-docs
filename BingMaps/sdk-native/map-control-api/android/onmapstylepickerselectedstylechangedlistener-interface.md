---
title: "OnMapStylePickerSelectedStyleChangedListener Interface | Microsoft Docs"
author: "pablocan"
---

# OnMapStylePickerSelectedStyleChangedListener Interface (Android only)

Listener used with UserInterfaceOptions.MapStylePickerSelectedStyleChanged event.

>```java
> public interface OnMapStylePickerSelectedStyleChangedListener
>{
>    /** Called when map style picker style is selected. */
>    public boolean onSelectedStyleChanged(MapStylePickerSelectedStyleChangedEventArgs e);
>}
>```

## See Also

* [MapStylePickerSelectedStyleChangedEventArgs](MapStylePickerSelectedStyleChangedEventArgs-class.md)
* [MapUserInterfaceOptions](../MapUserInterfaceOptions-class.md)