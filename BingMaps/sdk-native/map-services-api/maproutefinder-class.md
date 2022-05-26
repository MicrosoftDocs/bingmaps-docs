---
title: MapRouteFinder Class | Microsoft Docs
description: Describes the MapRouteFinder class for Android and iOS and provides the class's static methods, examples, and additional references.
ms.author: kezhang
---

# MapRouteFinder Class

Forms and sends routing requests.

## Static Methods

### GetDrivingRoute

Forms and sends a routing request by the specified start and end coordinates.

_See also:_

* [Geopoint](../map-control-api/geopoint-class.md)
* [RouteWaypoint](routewaypoint-class.md)
* [MapRoute](maproute-class.md)
* [MapRouteDrivingOptions](maproutedrivingoptions-class.md)
* (Android) [OnMapRouteFinderResultListener](Android/onmaproutefinderresultlistener-interface.md) | (iOS) [MSMapRoutingCompletionBlock](iOS/maproutingcompletionblock-interface.md)

**Android**

>```java
>// Default overload: takes the specified start and end coordinates, and callback. returns the id of request which can be used to cancel ongoing request
>int getDrivingRoute(Geopoint startPoint, Geopoint endPoint, OnMapRouteFinderResultListener callback)
>
>// Overload that takes the specified start and end coordinates(using MapRouteDrivingOptions), and callback. returns the id of request which can be used to cancel ongoing request
>int getDrivingRoute(Geopoint startPoint, Geopoint endPoint, MapRouteDrivingOptions options, OnMapRouteFinderResultListener callback) 
>
>// Overload that takes a specified waypoints, and callback. returns the id of request which can be used to cancel ongoing request
>int getDrivingRoute(List<RouteWaypoint> waypoints, OnMapRouteFinderResultListener callback)
>
>// Overload that takes a specified waypoints(using MapRouteDrivingOptions), and callback. returns the id of request which can be used to cancel ongoing request
>int getDrivingRoute(List<RouteWaypoint> mapRouteWaypoints, MapRouteDrivingOptions options, OnMapRouteFinderResultListener callback)
>
>// Cancel ongoing route request by given id
>boolean cancelRouteRequest(int routeRequestId)
>```

**iOS**

>```objectivec
>// Default overload: takes the specified start and end coordinates, and callback.
>+ (void)getDrivingRoute:(MSGeopoint*)startLocation to:(MSGeopoint*)endLocation callBack:(MSMapRoutingCompletionBlock)callback
>
>// Overload that takes the specified start and end coordinates(using MapRouteDrivingOptions), and callback.
>+ (void)getDrivingRoute:(MSGeopoint*)startLocation to:(MSGeopoint*)endLocation routeDrivingOptions:(MSMapRouteDrivingOptions*)routeDrivingOptions callBack:(MSMapRoutingCompletionBlock)callback;
>
>// Overload that takes a specified waypoints, and callback.
>+ (void)getDrivingRouteWithWaypoints:(NSArray<MSMapRouteWaypoint*>*)waypoints callBack:(MSMapRoutingCompletionBlock)callback;
>
>// Overload that takes a specified waypoints(using MapRouteDrivingOptions), and callback.
>+ (void)getDrivingRouteWithWaypoints:(NSArray<MSMapRouteWaypoint*>*)waypoints routeDrivingOptions:(MSMapRouteDrivingOptions*)routeDrivingOptions callBack:(MSMapRoutingCompletionBlock)callback;
>```

## Examples

### Android

```java
MapServices.setCredentialsKey("...");
MapServices.setContext(getApplicationContext());

MapRouteDrivingOptions options = new MapRouteDrivingOptions()
    .setRouteOptimization(MapRouteOptimization.TIME_WITH_TRAFFIC)
    .setRouteRestrictions(MapRouteRestrictions.TOLLROADS)
    .setMaxAlternateRouteCount(2);

MapRouteFinder.getDrivingRoute(
    new Geopoint(47.620484, -122.349182), 
    new Geopoint(47.615490, -122.194931),
    options,
	new OnMapRouteFinderResultListener() {
        @Override
        public void onMapRouteFinderResult(MapRouteFinderResult result) {
            if (result.getStatus() == MapRouteFinderStatus.SUCCESS) {
                MapRoute route = result.getRoute();
                List<MapRoute> alternateRoutes = result.getAlternateRoutes();
                // ...
            }
        }
    }
);
```

### iOS

```objectivec
[MSMapServices setCredentialsKey:@"..."];

MSMapRouteDrivingOptions *options = [[MSMapRouteDrivingOptions alloc] init];
options.routeRestrictions = MSMapRouteRestrictionsTollRoads;
options.routeOptimization = MSMapRouteOptimizationTimeWithTraffic;
options.maxAlternateRouteCount = 2;

[MSMapRouteFinder getDrivingRoute:[MSGeopoint geopointWithLatitude:47.620484 longitude:-122.349182] [MSGeopoint geopointWithLatitude:47.615490 longitude:-122.194931] routeDrivingOptions:options callBack:^void(MSMapRoutingCompletionBlock *result) {
    if ([result status] == MSMapRouteFinderStatusSuccess) {
        MSMapRoute* route = [result mapRoute];
        NSArray<MSMapRoute*>* alternateRoutes = [result alternateRoutes];
        // ...
    }
}];
```

## See Also

* [MapServices](mapservices-class.md)