---
title: "MSMapCustomTileMapLayerDelegate protocol | Microsoft Docs"
author: "bmnxplat"
---

# MSMapCustomTileMapLayerDelegate protocol (iOS only)

Used by CustomTileMapLayer to call out to developer code when a tile image is required for the MapView.

>```objectivec
> @protocol MSMapCustomTileMapLayerDelegate <NSObject>
>
> - (void)customTileMapLayerOnBitmapRequestedAtX:(int)x y:(int)y zoom:(int)zoom
> completionHandler:(void(^)(NSData *data))completionHandler;
>
> @end
>```

## See Also

[CustomTileMapLayer](../CustomTileMapLayer-class.md)