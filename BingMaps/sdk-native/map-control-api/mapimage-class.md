
# MapImage class

An image that can be used with [MapIcon](MapIcon-class.md).

**Android**

>```java
> public class MapImage
>```

**iOS**

>```objectivec
> @interface MSMapImage : NSObject
>```

## Constructor

**Android**

>```java
> MapImage(android.graphics.Bitmap bitmap)
>```

**iOS**

>```objectivec
> + (instancetype)imageFromSvg:(NSData *)svgData
> + (instancetype)imageWithUIImage:(UIImage *)image
> + (instancetype)imageWithUIView:(UIView *)view
>```

## Properties

### Bitmap (Android only)

The bitmap associated with this MapImage.

>```java
> android.graphics.Bitmap getBitmap()
>```  


## See Also

[Icons](../map-control-concepts/map-icons.md)