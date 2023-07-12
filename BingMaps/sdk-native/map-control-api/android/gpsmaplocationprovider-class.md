---
title: GPSMapLocationProvider Class | Microsoft Docs
description: Describes the GPSMapLocationProvider class for Android and provides the class' constructor and properties.
ms.author: adl
---

# GPSMapLocationProvider Class (Android only)

A location provider which uses GPS location services. 

The benefit of using this location provider is that it works in all countries/regions as it comes with all Android phones. You also don't have to pull in an extra module to use this provider. The downside to using this provider is that it is not battery efficient. Also, you have to choose one provider to retrieve signals from (such as network or GPS) instead of having them all work together for one signal.

>```java
> class GPSMapLocationProvider extends MapLocationProvider
>```

## Constructor

In order to construct a GPSMapLocationProvider, use GPSMapLocationProvider.Builder to optionally set your own settings and then call build() to construct an instance. 

>```java
> public static class Builder {
>   Builder(Context context);
> 
>   Builder setMinTime(long minTime);
> 
>   Builder setDesiredProviders(ArrayList<String> desiredProviders);
> 
>   Builder setSensorSamplingPeriod(int sensorSamplingPeriod);
> 
>   /**
>    * Call this to show last location available on launch if it exists.
>    */
>   Builder useLastKnownLocationOnLaunch();
> 
>   /**
>    * Helps user set settings to be used in navigation mode.
>    * Sets minTime as 1 second and desiredProviders as GPS_PROVIDER,
>    * NETWORK_PROVIDER, and PASSIVE_PROVIDER in that order,
>    * and sensorSamplingPeriod as 20 ms.
>    */
>   Builder setNavigationSettings();
> 
>   GPSMapLocationProvider build();
> }
>```

Example:
>```java
>new GPSMapLocationProvider.Builder(getApplicationContext())
>       .setDesiredProviders(new ArrayList<>(Arrays.asList(LocationManager.NETWORK_PROVIDER, LocationManager.GPS_PROVIDER)))
>       .setMinTime(TimeUnit.SECONDS.toMillis(0))
>       .build();
>```

## Properties

### MinTime

Represents the minimum time interval between location updates in milliseconds. Default minTime is 5000.

If set is called before location retrieval started, setting will be saved for when location retrieval starts. If set is called after location retrieval started, it will restart with the new setting.

>```java
> void setMinTime(long minTime)
> long getMinTime()
>```

### DesiredProviders

Represents the desired providers to be used in the order you want them to be tried. If location tracking can not be started with the desiredProviders, the default providers will be used instead. Default desiredProviders is an array containing LocationManager.GPS_PROVIDER, LocationManager.NETWORK_PROVIDER and LocationManager.PASSIVE_PROVIDER in that order.

If set is called before location retrieval started, setting will be saved for when location retrieval starts. If set is called after location retrieval started, it will restart with the new setting.

>```java
> void setDesiredProviders(ArrayList<String> desiredProviders)
> ArrayList<String> getDesiredProviders()
>```

### SensorSamplingPeriod

See [MapLocationProvider](maplocationprovider-class.md)

## See Also
* [MapUserLocation](../mapuserlocation-class.md)
* [MapLocationProvider](maplocationprovider-class.md)
