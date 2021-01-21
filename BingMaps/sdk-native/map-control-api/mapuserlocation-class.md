---
title: "MapUserLocation Class | Microsoft Docs"
author: "adl"
---

# MapUserLocation Class

Allows to track the user's location and display it on the map with an accuracy radius and a directionality cone.

Look [here](../map-control-concepts/user-location.md) for more information on how this class can be used with examples.

**Android**

>```java
> public class MapUserLocation
>```

**iOS**

>```objectivec
> @interface MSMapUserLocation : NSObject
>```

## Overview

There is no direct way to construct a UserLocation class. Instead, MapView holds a UserLocation instance which should be accessed in order to use user location features.

_See also:_ [MapView](mapview-class.md)

**Android**

>```java
> public class Mapview {
>   MapUserLocation getUserLocation()
> }
> ```

**iOS**

>```objectivec
> @interface MSMapView : UIView
> @property(nonatomic, readonly) MSMapUserLocation* userLocation
> @end
>```

## Properties

### Visible

Sets user location icon's visibility while tracking continues. If called before tracking was started, setting will be saved but nothing will show until tracking is started. The default value is true.

**Android**

>```java
> boolean getVisible()
> void setVisible(boolean visible)
>```

**iOS**

>```objectivec
> @property(nonatomic) BOOL visible
>```


### Tracking Mode

Sets user tracking mode to None or centeredOnUser. Default value is none. If tracking mode is set to centeredOnUser, once the user interrupts the map, it will change back to none. Add tracking interrupted event listeners to be notified once the user interrupts the map. See events section below for more information.

_See also:_ [MapUserLocationTrackingMode](mapuserlocationtrackingmode-enumeration.md)

**Android**

>```java
> MapUserLocationTrackingMode getTrackingMode()
> void setTrackingMode(MapUserLocationTrackingMode mode)
>```

**iOS**

>```objectivec
> @property(nonatomic) MSMapUserLocationTrackingMode trackingMode
>```

### Orientation
Sets user location orientation to be used by the directionality cone. Default value is heading. If called before tracking is started, the setting will take effect next time tracking is started. If called after tracking is started, the orientation will be switched immediately.

_See also:_ [MapUserLocationOrientation](mapuserlocationorientation-enumeration.md)

**Android**

>```java
> MapUserLocationOrientation getOrientation()
> void setOrientation(MapUserLocationOrientation orientation)
>```

**iOS**

>```objectivec
> @property(nonatomic) MSMapUserLocationOrientation orientation
>```

### Signal Lost Alert Action

Sets the action that should be taken for future signal lost alerts. Default value is ignore. If the alert is currently being shown, setting this action will not affect the current alert.

_See also:_ [MapUserLocationSignalLostAlertAction](mapuserlocationsignallostalertaction-enumeration.md)

**Android**

>```java
> MapUserLocationSignalLostAlertAction getSignalLostAlertAction()
> void setSignalLostAlertAction(MapUserLocationSignalLostAlertAction action)
>```

**iOS**

>```objectivec
> @property(nonatomic) MSMapUserLocationSignalLostAlertAction signalLostAlertAction
>```


### Last Location Data

Gets last location retrieved or null(Android) / nil(iOS) if no locations were ever recorded.

_See also:_ [MapLocationData](maplocationdata-class.md)

**Android**

>```java
> @Nullable MapLocationData getLastLocationData()
>```

**iOS**

>```objectivec
> @property(nonatomic, readonly, nullable) MSMapLocationData* lastLocationData
>```

### Last Heading

Gets last heading retrieved where heading is the direction the phone is pointing at. This value is relative to true North. The value 0 means the device is pointed toward true North, 90 means it is pointed east, 180 means it is pointed south, and 270 means it is pointed west.

**Android**

Returns null if no headings were ever recorded.

>```java
> @Nullable Double getLastHeading()
> ```

**iOS**

Returns -1 if no headings were ever recorded.

>```objectivec
> @property(nonatomic, readonly) CLLocationDirection lastHeading
>```

## Methods

### Start Tracking

Starts tracking and returns ready state if location permission were granted. Returns permissionDenied state if no location permissions were granted and tracking will not start. Returns disabled state if all providers were disabled. If permissionDenied was returned, developer should request for location permissions and then call this method again. If called multiple times, tracking will restart with the new locationProvider.

_See also:_ [MapUserLocationTrackingState](mapuserlocationtrackingstate-enumeration.md)

**Android**

>```java
> MapUserLocationTrackingState startTracking(MapLocationProvider mapLocationProvider)
> ```

_See also:_ [MapLocationProvider](android/maplocationprovider-class.md), and [GPSMapLocationProvider](android/gpsmaplocationprovider-class.md) 

**iOS**

>```objectivec
> - (MSMapUserLocationTrackingState)startTrackingWithLocationProvider:(MSMapLocationProvider*)locationProvider
>```

_See also:_ [MSMapLocationProvider](ios/msmaplocationprovider-class.md)

### Stop Tracking

Will stop tracking and hide the user location if it was already active. If called when user location was not active, nothing happens.

**Android**

>```java
> void stopTracking()
> ```

**iOS**

>```objectivec
> - (void)stopTracking
>```

## Events

### Tracking Interrupted

Fired when tracking mode was in CenteredOnUser state and the user interrupts the map and changes it back to tracking mode None. 

**Android**

>```java
> void addOnMapUserLocationTrackingInterruptedListener(OnMapUserLocationTrackingInterruptedListener listener)
> void removeOnMapUserLocationTrackingInterruptedListener(OnMapUserLocationTrackingInterruptedListener listener)
> ```

_See also:_ [OnMapUserLocationTrackingInterruptedListener](android/onmapuserlocationtrackinginterruptedlistener-interface.md)

**iOS**

>```objectivec
> - (MSMapHandlerId)addUserDidInterruptTrackingHandler:(MSMapUserLocationTrackingInterruptedHandler)handler
> - (BOOL)removeUserDidInterruptTrackingHandler:(MSMapHandlerId)handlerId
>```

_See also:_ [MSMapUserLocationTrackingInterruptedHandler](ios/msmapuserlocationtrackinginterrupted-interface.md)
