
# Geolocation class

Represents a collection of Locations that form a path.

**Android**

>```java
> public class Geolocation
>```

**iOS**

>```objectivec
> @interface MSGeolocation : NSObject
>```

## Constructor

**Android**

>```java
> //Creates a location at 0,0 with an altitude of 0 and altitude reference of surface.  
> Geolocation()
> //Creates a location with the specified latitude and longitude in degrees. The default altitude of 0 and altitude reference of surface.  
> Geolocation(double latitude, double longitude)
> //Creates a location with the specified latitude and longitude in degrees and altitude in meters with default altitude reference of surface.  
> Geolocation(double latitude, double longitude, double altitude)
> // Creates a location with the specified latitude and longitude in degrees and altitude in meters.  
> Geolocation(double latitude, double longitude, double altitude, AltitudeReferenceSystem altitudeReference)
>```

**iOS**

>```objectivec
> + (instancetype)geolocationWithLatitude:(double)latitude
>                            longitude:(double)longitude
> + (instancetype)geolocationWithLatitude:(double)latitude
>                            longitude:(double)longitude
>                             altitude:(double)altitude
> + (instancetype)geolocationWithLatitude:(double)latitude
>                            longitude:(double)longitude
>                             altitude:(double)altitude
>              altitudeReferenceSystem:(MSMapAltitudeReferenceSystem)altitudeReferenceSystem
>```

## Static Methods

### InitWithLatitude (iOS Only)

Creates MSGeolocation object with a specific latitude, longitude, altitude, and altitude reference system.

>```objectivec
> - (instancetype)initWithLatitude:(double)latitude
>                        longitude:(double)longitude
>                         altitude:(double)altitude
>          altitudeReferenceSystem:(MSMapAltitudeReferenceSystem)altitudeReferenceSystem
>```

### ToAltitudeReferenceSystem

Returns a location in a new altitude reference system. This method leverages a passed-in MapView for retrieving data for conversions.

**Android**

>```java
> Geolocation toAltitudeReferenceSystem(AltitudeReferenceSystem newAltitudeReferenceSystem, MapView mapView)
>``` 

**iOS**

>```objectivec
> - (MSGeolocation *)toAltitudeReferenceSystem:(MSMapAltitudeReferenceSystem)newAltitudeReferenceSystem
>                                          map:(MSMapView *)map
>```

## Properties

### Latitude

Gets the latitude of the location in degrees.

**Android**

>```java
> double getLatitude()
> void setLatitude(double latitude)
>```  

**iOS**

>```objectivec
> - @property (nonatomic, readonly) double longitude
>```


### Longitude

Gets the longitude .of the location in degrees.

**Android**

>```java
> double getLongitude()  
> void setLongitude(double longitude)
>```  

**iOS**

>```objectivec
> @property (nonatomic, readonly) double longitude
>```


### Altitude

Gets the altitude of the location in meters.

**Android**

>```java
> double getAltitude()  
> void setAltitude(double altitude)
>```

**iOS**
>```objectivec 
> @property (nonatomic, readonly) double altitude
>```  

### AltitudeReferenceSystem

Gets the type of altitude used to describe this location.

**Android**

>```java
> AltitudeReferenceSystem getAltitudeReferenceSystem()  
> void setAltitudeReferenceSystem(AltitudeReferenceSystem altitudeReferenceSystem)
>```

>##### iOS

**iOS**

>```objectivec 
> @property (nonatomic, readonly) MSMapAltitudeReferenceSystem altitudeReferenceSystem
>```

## See Also

[AltitudeReferenceSystem](AltitudeReferenceSystem-enumeration.md)
