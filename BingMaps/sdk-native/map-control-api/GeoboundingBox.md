
# GeoboundingBox class

Represents a bounded geographic area.

**Android**

>```java
> public class GeoboundingBox
>```

**iOS**

>```objectivec
> @interface MSGeoboundingBox : NSObject
>```

## Constructors

_See also:_ [MSGeolocation](Geolocation.md)

**Android**

>```java
> // Creates a  bounding box based on 2 opposite corners of a bounding box. 
> GeoboundingBox(Geolocation northwest, Geolocation southeast)
> //Creates a bounding box to contain the specified locations. locations must contain at least 1 element.
> GeoboundingBox(List<Geolocation> locations)
>```

**iOS**
>```objectivec
>+ (instancetype)geoBoundingBoxWithNorthwest:(MSGeolocation *)northwest southeast:(MSGeolocation *)southeast
>+ (instancetype)geoBoundingBoxWithLocations:(NSArray<MSGeolocation *> *)locations
>```


## Properties

### North

The latitude of the northern border of the bounding box.

**Android**

>```java
> final double north
> ```

**iOS**

>```objectivec
> @property (nonatomic, readonly) double north
>```


### East

The longitude of the eastern border of the bounding box.

**Android**

>```java
> final double east
> ```

**iOS**

>```objectivec
> @property (nonatomic, readonly) double east
>```

### South

The latitude of the southern border of the bounding box.

**Android**

>```java
> final double south
> ```

**iOS**

>```objectivec
> @property (nonatomic, readonly) double south
>```

### West

The longitude of the western border of the bounding box.

**Android**

>```java
> final double west
> ```

**iOS**

>```objectivec
> @property (nonatomic, readonly) double west
>```

### MinimumAltitude

The minimum altitude of all the points within the bounding box.

**Android**

>```java
> final double minimumAltitude
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) double minimumAltitude
>```

### MaximumAltitude

Gets the maximum altitude of all the points within the bounding box.

**Android**

>```java
> final double maximumAltitude
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) double maximumAltitude
>```

### NorthwestCorner (Android Only)

The north west corner of the bounding box.
_See also:_ [Geolocation](Geolocation.md)

>```java
> Geolocation getNorthwestCorner()
> ```

### SoutheastCorner (Android Only)

The south east corner of the bounding box.
_See also:_ [Geolocation](Geolocation.md)

>```java
> Geolocation getSoutheastCorner()
> ```
