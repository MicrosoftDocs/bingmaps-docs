---
title: "MSMapLocationProvider Class | Microsoft Docs"
author: "adl"
---

# MSMapLocationProvider Class (iOS only)

A location provider to be used to retrieve user location on iOS. 

See [MapUserLocation](../mapuserlocation-class.md) for more details on how to start tracking user location with a location provider.

>```objectivec
> @interface MSMapLocationProvider : NSObject<CLLocationManagerDelegate>
>```

## Constructors

### Default constructor

Initializes location provider with the default properties from MSMapLocationProviderBuilder.
See [MSMapLocationProviderBuilder](msmaplocationproviderbuilder-class.md) for more details on what the default properties are.

>```objectivec
> - (instancetype)init
>```

### Customizable Constructor

Initializes location provider with the properties set on the builder inside the passed in block. See [MSMapLocationProviderBuilder](msmaplocationproviderbuilder-class.md) for more details what properties can be set.

>```objectivec
> - (instancetype)initWithBuilderBlock:(void (^)(MSMapLocationProviderBuilder*))builderBlock
>```

Example:

>```objectivec
> [[MSMapLocationProvider alloc] initWithBuilderBlock:^(MSMapLocationProviderBuilder* builder) {
>           builder.headingFilter = 3;
>           [builder useLastKnownLocationOnLaunch];
> }];
>```

## Properties

### DesiredAccuracy

Refer to [MSMapLocationProviderBuilder](msmaplocationproviderbuilder-class.md) for information on what desiredAccuracy represents.

If set is called before location retrieval started, setting will be saved for when location retrieval starts. If set is called after location retrieval started, it will restart with the new setting.

>```objectivec
> @property(nonatomic) CLLocationAccuracy desiredAccuracy
>```

### HeadingFilter

Refer to [MSMapLocationProviderBuilder](msmaplocationproviderbuilder-class.md) for information on what headingFilter represents.

If set is called before location retrieval started, setting will be saved for when location retrieval starts. If set is called after location retrieval started, it will restart with the new setting.

>```objectivec
> @property(nonatomic) CLLocationDegrees headingFilter
>```

### LastLocation

Returns the last location emitted by this location provider, if any. Returns [`CLLocation`](https://developer.apple.com/documentation/corelocation/cllocation).

>```objectivec
> @property(nonatomic, readonly, nullable) CLLocation* lastLocation
>```

## Methods

### startTracking

Starts tracking the location on the device. This method may be called multiple times and stopTracking should be called once for each call to startTracking that returns MapUserLocationTrackingStateReady.

>```objectivec
> - (MSMapUserLocationTrackingState)startTracking
>```

### stopTracking

Stops a previous call to start tracking. Must be called once for each call to startTracking that returns MapUserLocationTrackingState.READY.

>```objectivec
> - (void)stopTracking
>```

## Events

### LocationChanged

Fired when a location event is received while tracking is active.  
removeLocationDidChangeHandler returns false if the listener has not been previously added or has been already removed.

>```objectivec
> - (MSMapHandlerId)addLocationDidChangeHandler:(MSMapLocationChangedHandler)handler
> - (BOOL)removeLocationDidChangeHandler:(MSMapHandlerId)handlerId
>```

_See also:_ [MSMapLocationChangedHandler](msmaplocationchangedhandler-interface.md)