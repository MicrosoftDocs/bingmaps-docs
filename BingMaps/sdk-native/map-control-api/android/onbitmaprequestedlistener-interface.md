---
title: "OnBitmapRequestedListener Interface | Microsoft Docs"
ms.author: "pablocan"
---

# OnBitmapRequestedListener Interface (Android only)

Used by CustomTileMapLayer to call out to developer code when a tile image is required for the MapView.

>```java
> public interface OnBitmapRequestedListener
> {
>     /** Called when a bitmap is requested. */
>     void OnBitmapRequested(MapTileBitmapRequestedEventArgs e);
> }
>```

## See Also

* [MapTileBitmapRequestedEventArgs](MapTileBitmapRequestedEventArgs-class.md)
* [CustomTileMapLayer](../CustomTileMapLayer-class.md)
