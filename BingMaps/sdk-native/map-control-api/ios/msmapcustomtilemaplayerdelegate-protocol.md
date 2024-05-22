---
title: MSMapCustomTileMapLayerDelegate protocol | Microsoft Docs
description: Describes the MSMapCustomTileMapLaterDelegate protocol for iOS and provides the protocol's syntax and additional references.
ms.author: pablocan
---

# MSMapCustomTileMapLayerDelegate protocol (iOS only)

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

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