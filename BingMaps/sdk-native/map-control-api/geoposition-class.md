---
title: Geoposition Class | Microsoft Docs
description: Describes the Geoposition class and Android and iOS and provides the class' constructor, static methods, and properties.
ms.author: pablocan
---

# Geoposition Class

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Represents a geographic position.

**Android**

>```java
> public class Geoposition
>```

**iOS**

>```objectivec
> @interface MSGeoposition : NSObject
>```

## Constructor

**Android**

>```java
> // Creates a Geoposition with the specified latitude and longitude in degrees, with the default altitude of 0.
> Geoposition(double latitude, double longitude)
>
> // Creates a Geoposition with the specified latitude and longitude in degrees and altitude in meters.
> Geoposition(double latitude, double longitude, double altitude)
>```

_See also:_ [android.location.Location](https://developer.android.com/reference/android/location/Location.html)

**iOS**

>```objectivec
> + (instancetype)geopositionWithCoordinates:(CLLocationCoordinate2D)coordinates
>
> + (instancetype)geopositionWithLatitude:(CLLocationDegrees)latitude
>                               longitude:(CLLocationDegrees)longitude
>
> + (instancetype)geopositionWithLatitude:(CLLocationDegrees)latitude
>                               longitude:(CLLocationDegrees)longitude
>                                altitude:(CLLocationDistance)altitude
>```

## Static Methods

### InitWithLatitude (iOS Only)

Creates MSGeoposition object with a specific latitude, longitude, altitude.

>```objectivec
> - (instancetype)initWithLatitude:(CLLocationDegrees)latitude
>                        longitude:(CLLocationDegrees)longitude
>                         altitude:(CLLocationDistance)altitude
>```

## Properties

### Latitude

Gets the latitude of geographic position in degrees.

**Android**

>```java
> double getLatitude()
> void setLatitude(double latitude)
>```

**iOS**

>```objectivec
> - @property (nonatomic) CLLocationDegrees latitude
>```


### Longitude

Gets the longitude of geographic position in degrees.

**Android**

>```java
> double getLongitude()  
> void setLongitude(double longitude)
>```

**iOS**

>```objectivec
> @property (nonatomic) CLLocationDegrees longitude
>```


### Altitude

Gets the altitude of geographic position in meters.

**Android**

>```java
> double getAltitude()
> void setAltitude(double altitude)
>```

**iOS**
>```objectivec 
> @property (nonatomic) CLLocationDistance altitude
>```
