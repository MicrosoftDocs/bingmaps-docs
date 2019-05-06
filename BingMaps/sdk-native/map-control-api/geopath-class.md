
# MSGeopath class

Represents a collection of Locations that form a path.

**Android**

>```java
> public class Geopath implements Iterable<Geolocation>
>```

**iOS**

>```objectivec
> @interface MSGeopath : NSObject<NSFastEnumeration>
>```

## Methods

### Add
Adds a new location to the set of locations in the Geopath.

**Android**

>```java
> `void add(Geolocation location)
>```

**iOS**

>```objectivec
> - (void)addLocation:(MSGeolocation *)loc
>```

### Insert (iOS Only)
Inserts a new location at a specific index in the path.

>```objectivec
> - (void)insertLocation:(MSGeolocation *)loc atIndex:(NSUInteger)index
>```


### Remove
Removes a specfic location from the Geopath. Return true if found.

**Android**

>```java
> boolean remove(Geolocation location)
> ```

**iOS**

>```objectivec 
> - (BOOL)removeLocation:(MSGeolocation *)loc
>```  

### RemoveAtIndex (iOS Only)
Removes a location at a specific index.

>```objectivec
> - (void)removeLocationAtIndex:(NSUInteger)index
>```

## Properties

### Size
The number of locations in the Geopath.

**Android** 

>```java
> int size()
>```

**iOS**

>```objectivec
> @property (readonly) NSUInteger count
>```

_See also:_ [Geolocation](Geolocation-class.md)
