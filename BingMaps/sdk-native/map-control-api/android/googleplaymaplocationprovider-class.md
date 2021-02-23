---
title: "GooglePlayMapLocationProvider Class | Microsoft Docs"
ms.author: "adl"
---

# GooglePlayMapLocationProvider Class (Android only)

A location provider which uses Google Play location services.

The benefit of using this location provider is that it is not as battery draining as using pure GPS. It also intelligently combines different signals such as WiFi and GPS to provide a fused location provider. However, the downside to using this location provider is that it does not work in China, and you have to pull in an extra module to use this. Take a look at [GPSMapLocationProvider](gpsmaplocationprovider-class.md) as another option.

This class is in a separate module called googleplaymaplocationprovider. Note that by using this module, clients have to take a dependency on [Google Play](https://developer.android.com/google/play/developer-api). In order to use this location provider, you must include the module in your build.gradle like this:
```implementation project(path: ':googleplaymaplocationprovider')```


>```java
> class GooglePlayMapLocationProvider extends MapLocationProvider
>```

## Constructor

In order to construct a GooglePlayMapLocationProvider, use GooglePlayMapLocationProvider.Builder to optionally set your own settings and then call build() to construct an instance. 

>```java
> public static class Builder {
>   Builder(Context context);
> 
>   Builder setPriority(int priority);
> 
>   Builder setInterval(long interval);
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
>    * Sets priority as PRIORITY_HIGH_ACCURACY, interval as 1 second,
>    * and sensorSamplingPeriod as 20 ms.
>    */
>   Builder setNavigationSettings();
> 
>   GooglePlayMapLocationProvider build();
> }
>```

Example:
>```java
>new GooglePlayMapLocationProvider.Builder(getApplicationContext())
>       .setInterval(TimeUnit.SECONDS.toMillis(5))
>       .setSensorSamplingPeriod(SensorManager.SENSOR_DELAY_FASTEST)
>       .build();
>```

## Properties

### Priority

Represents the priority for location tracking which is used as a strong hint for which location sources to use. Priority must be one of LocationRequest's priority constants. Default priority is PRIORITY_BALANCED_POWER_ACCURACY.

If set is called before location retrieval started, setting will be saved for when location retrieval starts. If set is called after location retrieval started, it will restart with the new setting.

>```java
> void setPriority(int priority)
> int getPriority()
>```

### Interval

Represents the preferred rate in milliseconds to receive location updates. Note that location updates may be somewhat faster or slower than this rate. This value can not be less than 0. Default interval is 5000.

If set is called before location retrieval started, setting will be saved for when location retrieval starts. If set is called after location retrieval started, it will restart with the new setting.

>```java
> void setInterval(long interval)
> long getInterval()
>```

### SensorSamplingPeriod

See [MapLocationProvider](maplocationprovider-class.md)

## See Also
* [MapUserLocation](../mapuserlocation-class.md)
* [MapLocationProvider](maplocationprovider-class.md)
* [Google Play Documentation](https://developer.android.com/google/play/developer-api)
