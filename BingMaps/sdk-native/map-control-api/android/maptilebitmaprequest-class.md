---
title: MapTileBitmapRequest Class | Microsoft Docs
description: Describes the mapTileBitmapRequest class for Android and outlines the PixelData property and provides additional references.
ms.author: pablocan
---

# MapTileBitmapRequest Class (Android only)

Contains data that a custom tile map layer developer can set to represent the requested tile.

## Properties

### PixelData

The pixel data used for the request.

>```java
> @Nullable byte[] getPixelData()
> void setPixelData(byte[] pixelData)
>```

## See Also

* [MapTileBitmapRequestedEventArgs](MapTileBitmapRequestedEventArgs-class.md)
* [CustomTileMapLayer](../CustomTileMapLayer-class.md)
