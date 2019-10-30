---
title: "CustomTileMapLayer Class | Microsoft Docs"
author: "pablocan"
---

# CustomTileMapLayer Class

Display tiles based on developer-supplied bytes returned in callbacks.

**Android** 

>```java
> public class CustomTileMapLayer extends MapLayer
>```

**iOS**

>```objectivec
> @interface MSMapCustomTileMapLayer : MSMapLayer
>```

## See Also [MapLayer](MapLayer-class.md)

## Methods

### clearTileCache

Clears the tile cache so that all tiles will be requested again from the provider.

**Android**

>```java
> void clearTileCache()
>```

**iOS**

>```objectivec
>- (void)clearTileCache
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
