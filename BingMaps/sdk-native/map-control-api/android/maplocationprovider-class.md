---
title: "MapLocationProvider Class | Microsoft Docs"
ms.author: "adl"
---

# MapLocationProvider Class (Android only)

An abstract class that contains common methods for all Android location providers. 

>```java
> abstract class MapLocationProvider implements SensorEventListener
>```

See [GPSMapLocationProvider](gpsmaplocationprovider-class.md) for a concrete class you can use.

See [MapUserLocation](../mapuserlocation-class.md) for more details on how to start tracking user location with a location provider.

## Methods

### startTracking

Starts tracking the location on the device. This method may be called multiple times and stopTracking should be called once for each call to startTracking that returns MapUserLocationTrackingState.READY.

>```java
> MapUserLocationTrackingState startTracking()
>```

### stopTracking

Stops a previous call to start tracking. Must be called once for each call to startTracking that returns MapUserLocationTrackingState.READY.

>```java
> void stopTracking()
>```

## Events

### LocationChanged

Fired when a location event is received while tracking is active.  
removeLocationChangedListener returns false if the listener has not been previously added or has been already removed.  
See [LocationChangedListener](locationchangedlistener-interface.md) for more details on the listener interface.

>```java
> void addLocationChangedListener(LocationChangedListener locationChangedListener)
> boolean removeLocationChangedListener(LocationChangedListener locationChangedListener)
>```

## Properties

### LastLocation

Returns the last location emitted by this location provider, if any. Returns [`android.location.Location`](https://developer.android.com/reference/android/location/Location).
>```java
> @Nullable android.location.Location getLastLocation()
>```

### SensorSamplingPeriod

Represents sensor sampling period in microseconds for retrieving heading. Note that this value is only a hint to the system and events may be received faster or slower than the specified rate. Usually, events are received faster than the specified rate. This value can not be less than 0. Default sensorSamplingPeriod is SensorManager.SENSOR_DELAY_NORMAL.

If set is called before location retrieval started, setting will be saved for when location retrieval starts. If set is called after location retrieval started, it will restart with the new setting.
>```java
> void setSensorSamplingPeriod(int sensorSamplingPeriod)
> int getSensorSamplingPeriod()
>```

