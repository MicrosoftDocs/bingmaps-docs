
# Geoshape class

Represents a geographic shape.

**Android**

>```java
> public abstract class Geoshape
>```

**iOS**

>```objectivec
> @interface MSGeoshape : NSObject
>```

## Properties

### AltitudeReferenceSystem

Altitude reference system used for geographic region.

**Android**

>```java
> AltitudeReferenceSystem getAltitudeReferenceSystem()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) MSMapAltitudeReferenceSystem altitudeReferenceSystem
>```

_See also:_ [AltitudeReferenceSystem](AltitudeReferenceSystem-enumeration.md)

### GeoshapeType

Indicates the shape of a geographic region.

**Android**

>```java
> GeoshapeType getGeoshapeType()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) MSGeoshapeType geoshapeType
>```

_See also:_ [GeoshapeType](GeoshapeType-enumeration.md)

## See Also

* [GeoboundingBox](Geoboundingbox-class.md)
* [Geopath](Geopath-class.md)
* [Geopoint](Geopoint-class.md)
