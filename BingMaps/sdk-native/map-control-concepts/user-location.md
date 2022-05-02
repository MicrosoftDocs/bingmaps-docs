---
title: UserLocation API
ms.author: "adl"
---

# UserLocation API

The ability to show the user's location and track the user's location is an important tool in a map. By using our UserLocation API, you can show the user's location on your map with some customizable features.

There are two main mechanisms this SDK supports to show the user's location:

1. Using the user location toolbar button
    * This requires minimal integration. A listener can be set to listen for the user location toolbar button tapped event.
    * Once the user clicks on this toolbar button, it will notify the listener and the tracking mode will be set to CenteredOnUser.
    * The developer can now request for the user's location permissions and start tracking after receiving those permissions
2. Using the User Location API to have more control over the user location features.
    * This option provides more flexibility for configuration. However, the developer will have to create their own mechanism to determine when to start tracking

See [MapUserLocation API](../map-control-api/mapuserlocation-class.md) for more information on the API.

## Features

### Me Poi Visibility
* A location provider needs to be passed in to call start tracking.
  
  For Android, you can use [GPSMapLocationProvider](../map-control-api/android/gpsmaplocationprovider-class.md). 
 
  For iOS, you can use [MSMapLocationProvider](../map-control-api/ios/msmaplocationprovider-class.md). 
  
  Read more about their differences in their respective documentations.
* To start tracking, it requires the developer to have requested for and obtained the user's location permissions
* Once tracking is started, the default functionality will show the user's location on the map
* The user location icon can be configured to be visible or not visible during tracking

### Retrieve Last Location Data And Last Heading
* Ability to ask for the location data of the last retrieved location
* Ability to ask for the value of the last retrieved heading
* If user location was active in the past but is now stopped, it will still return the last available location data and heading that was retrieved before user location was stopped


### Camera Tracking Mode

* Ability to set camera tracking mode to none or centeredOnUser
* Ability to add and remove listeners to be notified when the user interrupts the map and changes the tracking mode from centeredOnUser back to none

### Directionality Cone Orientation
* Ability to set the directionality cone's orientation to be using heading (direction phone is pointing in) or bearing (direction user is moving in).

### Signal Lost Alert Action
* Ability to set whether or not the signal lost alert should be shown when signal lost is detected.

## Examples

### Show the user's location on the map with default settings using MSMapLocationProvider(iOS) and GPSMapLocationProvider(Android)

**iOS**

```objectivec
// Assuming developer added the map and has the map in a variable called mapView like below
@property(weak, nonatomic) IBOutlet MSMapView* mapView;

MSMapLocationProvider* locationProvider = [[MSMapLocationProvider alloc] init]
MSMapUserLocationTrackingState trackingState = [mapView.userLocation startTrackingWithLocationProvider:locationProvider]
if (trackingState == MSMapUserLocationTrackingStatePermissionDenied) {
	// request for user location permissions and then call startTracking again
} else if (trackingState == MSMapUserLocationTrackingStateReady) {
	// handle the case where location tracking was successfully started
}
```

**Android**

```java
// Assuming developer added the map and has the map in a variable called map like below
MapView map = (MapView)findViewById(R.id.map);
MapUserLocation userLocation = map.getUserLocation();

MapUserLocationTrackingState userLocationTrackingState = userLocation.startTracking(new GPSMapLocationProvider.Builder(getApplicationContext()).build());
if (userLocationTrackingState == MapUserLocationTrackingState.PERMISSION_DENIED)
{
    // request for user location permissions and then call startTracking again
} else if (userLocationTrackingState == MapUserLocationTrackingState.READY)
{
    // handle the case where location tracking was successfully started
} else if (userLocationTrackingState == MapUserLocationTrackingState.DISABLED)
{
	// handle the case where all location providers were disabled
}
```

### Set the camera to track the user location and be notified once the user interrupts the map

**iOS**

```objectivec
// Assuming developer added the map and has the map in a variable called mapView like below
@property(weak, nonatomic) IBOutlet MSMapView* mapView;

MSMapUserLocation* userLocation = mapView.userLocation;
userLocation.trackingMode = MSMapUserLocationTrackingModeCenteredOnUser;
[userLocation addUserDidInterruptTrackingHandler:^BOOL(MSMapUserLocationTrackingInterruptedEventArgs* e){
	// Add your code here to handle the case where tracking mode is changed back to MSMapUserLocationTrackingModeNone

	// Return YES instead if you have consumed the event and don't want other handlers to be notified
	return NO;
}];
```

**Android**

```java
// Assuming developer added the map and has the map in a variable called map like below
MapView map = (MapView)findViewById(R.id.map);
MapUserLocation userLocation = map.getUserLocation();

userLocation.setTrackingMode(MapUserLocationTrackingMode.CENTERED_ON_USER);
userLocation.addOnMapUserLocationTrackingInterruptedListener(new OnMapUserLocationTrackingInterruptedListener() {
    @Override
    public boolean onMapUserLocationTrackingInterrupted(MapUserLocationTrackingInterruptedEventArgs e)
    {
        // Add your code here to handle the case where tracking mode is changed back to MapUserLocationTrackingMode.NONE

        // Return true instead if you have consumed the event and don't want other listeners to be notified
        return false;
    }
});
```



## See Also:

* [MapUserLocation](../map-control-api/mapuserlocation-class.md)
* [MapLocationProvider](../map-control-api/android/maplocationprovider-class.md)
* [GPSMapLocationProvider](../map-control-api/android/gpsmaplocationprovider-class.md)
* [MSMapLocationProvider](../map-control-api/ios/msmaplocationprovider-class.md)
* [MapView](../map-control-api/mapview-class.md)
