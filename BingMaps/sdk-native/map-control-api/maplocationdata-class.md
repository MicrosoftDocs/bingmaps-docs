---
title: MapLocationData Class | Microsoft Docs
description: Describes the MapLocationData class for Android and iOS and provides the class' properties and additional references.
ms.author: adl
---

# MapLocationData Class

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Represents the last information retrieved from a location update. Latitude, longitude, and timestamp are guaranteed to have valid values for every location fix. 

## Properties

### Latitude

Latitude of position in degrees.

**Android**

>```java
> double getLatitude()
>```

**iOS**

>```objectivec
> @property(nonatomic, readonly) CLLocationDegrees latitude
>```


### Longitude

Longitude of position in degrees.

**Android**

>```java
> double getLongitude()
>```

**iOS**

>```objectivec
> @property(nonatomic, readonly) CLLocationDegrees longitude
>```

### PositionAccuracy

Accuracy of latitude and longitude in meters.

**Android**

Returns null if no value is available.

>```java
> @Nullable Double getPositionAccuracy()
>```

**iOS**

Returns -1 if no value is available.

>```objectivec
> @property(nonatomic, readonly) CLLocationAccuracy positionAccuracy
>```

### Altitude

Altitude of position in meters relative to AltitudeReference. 

**Android**

Returns null if no value is available.

>```java
> @Nullable Double getAltitude()
> ```

**iOS**

Returns nil if no value is available. Otherwise, returns double representated as a NSNumber.

>```objectivec
> @property(nonatomic, readonly, nullable) NSNumber* altitude
>```

### AltitudeAccuracy

Altitude accuracy of position in meters.

**Android**

Returns null if no value is available.

>```java
> @Nullable Double getAltitudeAccuracy()
> ```

**iOS**

Returns -1 if no value is available.

>```objectivec
> @property(nonatomic, readonly) CLLocationAccuracy altitudeAccuracy
>```

### AltitudeReference

Altitude reference of position. 

_See also:_ [AltitudeReferenceSystem](altitudereferencesystem-enumeration.md)

**Android**

>```java
> AltitudeReferenceSystem getAltitudeReference()
> ```

**iOS**

>```objectivec
> @property(nonatomic, readonly) MSMapAltitudeReferenceSystem altitudeReference
>```

### Bearing

Bearing of position in degrees where bearing is the direction the user is moving in. This value is relative to true North. North is 0 degrees, east is 90 degrees, south is 180 degrees, and west is 270 degrees.

**Android**

Returns null if no value is available.

>```java
> @Nullable Double getBearing()
> ```

**iOS**

Returns -1 if no value is available.

>```objectivec
> @property(nonatomic, readonly) CLLocationDirection bearing
>```

### Speed

Speed of position in meters per second. 

**Android**

Returns null if no value is available.

>```java
> @Nullable Double getSpeed()
> ```

**iOS**

Returns -1 if no value is available.

>```objectivec
> @property(nonatomic, readonly) CLLocationSpeed speed
>```

### Timestamp

Timestamp of position.

**Android**

Represents the date and time when the location data was retrieved, as UTC time in milliseconds since January 1, 1970.

>```java
> long getTimestamp()
> ```

**iOS**

>```objectivec
> @property(nonatomic, readonly) NSDate* timestamp
>```

## See Also

* [MapUserLocation](mapuserlocation-class.md)
