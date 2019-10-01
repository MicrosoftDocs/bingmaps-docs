# GeoshapeType enumeration

Indicates the shape of the geographic region.

**Android**

>```java
> public enum GeoshapeType
> {
>      GEOPOINT,
>      GEOPATH,
>      GEOBOUNDINGBOX
> }
>```

**iOS**

>``` objectivec
> typedef NS_ENUM(NSInteger, MSGeoshapeType)
> {
>      MSGeoshapeTypeGeopoint,
>      MSGeoshapeTypeGeopath,
>      MSGeoshapeTypeGeoboundingBox
> }
> ```

## Values

### Geopoint

The geographic region is a point.

### Geopath

The geographic region is an ordered series of points.

### GeoboundingBox

The geographic region is a rectangular region.