
# MapTileBitmapRequestedEventArgs class (Android only)

Passed to developer code when MapView needs a map tile for a [CustomTileMapLayer](../CustomTileMapLayer.md). As the map moves around the world, each tile it needs will be passed to the custom tile map layer which in turn uses this class to call out to developer code and ask for the image.

## Properties

### X

Returns the X position of the requested tile.

>```java
> int getX()
>```

### Y

Returns the Y position of the requested tile.

>```java
> int getY()
>```

### ZoomLevel

Returns the zoom level value of the requested tile.

>```java
> int getZoomLevel()
>```

### Request

Returns a MapTileBitmapRequest where pixel data can be applied to the map.

```MapTileBitmapRequest getRequest()```  
_See also:_ [MapTileBitmapRequest](MapTileBitmapRequest.md)