
# Geopoint class

Represents a geographic point.

**Android**

>```java
> public class Geopoint extends Geoshape
>```

**iOS**

>```objectivec
> @interface MSGeopoint : MSGeoshape
>```

## Constructor

**Android**

>```java
> // Create Geopoint with the specified Geoposition and altitude reference system.
> Geopoint(Geoposition position)
>
> // Create Geopoint with the specified Geoposition.
> Geopoint(Geoposition position, AltitudeReferenceSystem altitudeReference)
>
> // Creates a Geopoint with the specified latitude and longitude in degrees, with the default altitude of 0 and altitude reference of surface.
> Geopoint(double latitude, double longitude)
>
> // Creates a Geopoint with the specified latitude and longitude in degrees and altitude in meters, with the default altitude reference of surface.
> Geopoint(double latitude, double longitude, double altitude)
>
> // Creates a Geopoint with the specified latitude and longitude in degrees, altitude in meters, and altitude reference system.
> Geopoint(double latitude, double longitude, double altitude, AltitudeReferenceSystem altitudeReference)
>
> // Creates a Geopoint from Android's Location object.
> Geopoint(android.location.Location location)
>```

_See also:_ [android.location.Location](https://developer.android.com/reference/android/location/Location.html)

**iOS**

>```objectivec
> + (instancetype)geopointWithLocation:(CLLocation *)location
>
> + (instancetype)geopointWithPosition:(MSGeoposition *)position
>
> + (instancetype)geopointWithPosition:(MSGeoposition *)position
>              altitudeReferenceSystem:(MSMapAltitudeReferenceSystem)altitudeReferenceSystem
>
> + (instancetype)geopointWithLatitude:(CLLocationDegrees)latitude
>                            longitude:(CLLocationDegrees)longitude
>
> + (instancetype)geopointWithLatitude:(CLLocationDegrees)latitude
>                            longitude:(CLLocationDegrees)longitude
>                             altitude:(CLLocationDistance)altitude
>
> + (instancetype)geopointWithLatitude:(CLLocationDegrees)latitude
>                            longitude:(CLLocationDegrees)longitude
>                             altitude:(CLLocationDistance)altitude
>              altitudeReferenceSystem:(MSMapAltitudeReferenceSystem)altitudeReferenceSystem
>```

## Static Methods

### InitWithLatitude (iOS Only)

Creates MSGeopoint object with a specific latitude, longitude, altitude, and altitude reference system.

>```objectivec
> - (instancetype)initWithLatitude:(CLLocationDegrees)latitude
>                        longitude:(CLLocationDegrees)longitude
>                         altitude:(CLLocationDistance)altitude
>          altitudeReferenceSystem:(MSMapAltitudeReferenceSystem)altitudeReferenceSystem
>```

### InitWithPostition (iOS Only)

Creates MSGeopoint object with a position and altitude reference system.

>```objectivec
> - (instancetype)initWithPosition:(MSGeoposition *)position
>          altitudeReferenceSystem:(MSMapAltitudeReferenceSystem)altitudeReferenceSystem
>```

### ToAltitudeReferenceSystem

Returns a location in a new altitude reference system. This method leverages a passed-in MapView for retrieving data for conversions.

**Android**

>```java
> Geopoint toAltitudeReferenceSystem(AltitudeReferenceSystem newAltitudeReferenceSystem, MapView mapView)
>``` 

**iOS**

>```objectivec
> - (MSGeopoint *)toAltitudeReferenceSystem:(MSMapAltitudeReferenceSystem)newAltitudeReferenceSystem
>                                       map:(MSMapView *)map
>```

## Properties

### Position

Gets the position of the geographic location.

**Android**

>```java
> double getPosition()
>```

**iOS**
>```objectivec 
> @property (nonatomic) MSGeoposition *position
>```

### AltitudeReferenceSystem

Gets the altitude reference system used to describe this location.

**Android**

>```java
> AltitudeReferenceSystem getAltitudeReferenceSystem()  
>```

**iOS**

>```objectivec 
> @property (nonatomic, readonly) MSMapAltitudeReferenceSystem altitudeReferenceSystem
>```

_See also:_ [AltitudeReferenceSystem](AltitudeReferenceSystem-enumeration.md)

## See Also

* [Geoshape](Geoshape-class.md)
* [Geoposition](Geoposition-class.md)
