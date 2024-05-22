---
title: CustomTileMapLayer Class | Microsoft Docs
description: Describes the CustomTileMapLayer class for Android and iOS and provides the class' properties, methods, and additional references.
ms.author: pablocan
---

# CustomTileMapLayer Class

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Display tiles based on developer-supplied bytes returned in callbacks.

**Android** 

>```java
> public class CustomTileMapLayer extends MapLayer
>```

**iOS**

>```objectivec
> @interface MSMapCustomTileMapLayer : MSMapLayer
>```

## Properties

### BitmapRequested

Callback that is invoked when a map requests a tile map. The callback is responsible for providing the data back to the map synchronously.

>```java 
> void addOnBitmapRequestedListener(OnBitmapRequestedListener listener)
> void removeBitmapRequestedListener()
>```

_See also:_
[OnBitmapRequestedListener](Android/OnBitmapRequestedListener-interface.md)

**iOS**

>```objectivec
> @property (nonatomic, weak) id<MSMapCustomTileMapLayerDelegate> delegate
>```

_See also:_
[MSMapCustomTileMapLayerDelegate](iOS/MSMapCustomTileMapLayerDelegate-protocol.md)

## Methods

### ClearTileCache

Clears the tile cache so that all tiles will be requested again from the provider.

**Android**

>```java
> void clearTileCache()
>```

**iOS**

>```objectivec
>- (void)clearTileCache
>```

## See Also

[MapLayer](MapLayer-class.md)