
# GroundOverlayMapLayer class

Displays an image in a geographic area.

**Android**

>```java
> public class GroundOverlayMapLayer extends MapLayer
>```

**iOS**

>```objectivec
> @interface MSMapGroundOverlayMapLayer : MSMapLayer
>```

_See also:_ [MapLayer](MapLayer.md)

## Constructors

**Android**

>```java
> GroundOverlayMapLayer(android.graphics.Bitmap bitmap, GeoboundingBox latLongBox)
> ```

**iOS**

>```objectivec
> - (id)initWithImage:(UIImage*)image geoBoundingBox:(MSGeoboundingBox *)box
>```

_See also:_ [Overlay tiled images on a map](../map-control-concepts/Tile_Layers.md)