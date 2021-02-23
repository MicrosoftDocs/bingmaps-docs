---
title: "MSMapLocationProviderBuilder Class | Microsoft Docs"
ms.author: "adl"
---

# MSMapLocationProviderBuilder Class (iOS only)

A builder object which contains properties that can be optionally set by the hosting app to create a MSMapLocationProvider.

See [MSMapLocationProvider](msmaplocationprovider-class.md) for more details on how to use the builder with the location provider's constructor.

>```objectivec
> @interface MSMapLocationProviderBuilder : NSObject
>```

## Properties

### DesiredAccuracy

Represents desired accuracy level for location tracking. Desired accuracy must be one of CLLocationManager's accuracy constants. If the user only authorized an accuracyAuthorization of CLAccuracyAuthorization.reducedAccuracy, desiredAccuracy will always be kCLLocationAccuracyReduced regardless of what it is set as. Otherwise, the location service will do its best to achieve the requested accuracy, but it is not guaranteed. 

Default value is kCLLocationAccuracyNearestTenMeters.

>```objectivec
> @property(nonatomic) CLLocationAccuracy desiredAccuracy
>```

### HeadingFilter

Represents the minimum angular change in degrees required to generate new heading events.

Default value is 5 degrees.

>```objectivec
> @property(nonatomic) CLLocationDegrees headingFilter
>```

## Methods

### SetNavigationSettings
Sets properties to be suitable for navigation. Sets desired accuracy as kCLLocationAccuracyBestForNavigation, heading filter as kCLHeadingFilterNone, and useLastKnownLocationOnLaunch as NO.

>```objectivec
> - (void)setNavigationSettings
>```

### UseLastKnownLocationOnLaunch

Call this to use the last known location as the default location on launch if it exists. Default will not use the last known location on launch.

>```objectivec
> - (void)useLastKnownLocationOnLaunch
>```