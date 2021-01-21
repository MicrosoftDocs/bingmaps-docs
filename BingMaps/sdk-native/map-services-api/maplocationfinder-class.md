---
title: "MapLocationFinder Class | Microsoft Docs"
author: "pablocan"
---

# MapLocationFinder Class

Forms and sends geocoding requests.

## Static Methods

### FindLocations

Forms and sends a geocoding request by string query.

_See also:_

* [MapLocationOptions](MapLocationOptions-class.md)
* (Android) [OnMapLocationFinderResultListener](Android/OnMapLocationFinderResultListener-interface.md) | (iOS) [MapLocationFinderResultHandler](iOS/MapLocationFinderResultHandler-interface.md)

**Android**

These methods return a [Future](https://developer.android.com/reference/java/util/concurrent/Future) object that can be used to work with the asynchronous operation including canceling the operation.  
See also [MapLocationFinderResult](maplocationfinderresult-class.md).

>```java
>// Default overload: takes string query, options (nullable), and callback.
>Future<MapLocationFinderResult> findLocations(String query, @Nullable MapLocationOptions options, OnMapLocationFinderResultListener callback)
>
>// Overload that takes a reference geopoint in addition to the default set of parameters. When you specify this parameter, the location is taken into account and the results returned may be more relevant to the user.
>Future<MapLocationFinderResult> findLocations(String query, @Nullable Geopoint referencePoint, @Nullable MapLocationOptions options, OnMapLocationFinderResultListener callback)
>
>// Overload that takes a reference geobounding box in addition to the default set of parameters. When you specify this parameter, the geographical area is taken into account when computing the results of a location query.
>Future<MapLocationFinderResult> findLocations(String query, @Nullable GeoboundingBox referenceBoundingBox, @Nullable MapLocationOptions options, OnMapLocationFinderResultListener callback)
>
>// Overload that takes both geopoint and geobounding box as reference in addition to the default set of parameters.
>Future<MapLocationFinderResult> findLocations(String query, @Nullable Geopoint referencePoint, @Nullable GeoboundingBox referenceBoundingBox, @Nullable MapLocationOptions options, OnMapLocationFinderResultListener callback)
>```

**iOS**

>```objectivec
>// Default overload: takes string query, options (nullable), and callback handler.
>+ (void)findLocations:(NSString*)query withOptions:(MSMapLocationOptions* _Nullable)options handleResultWith:(MSMapLocationFinderResultHandler)handler
>
>// Overload that takes a reference geopoint in addition to the default set of parameters. When you specify this parameter, the location is taken into account and the results returned may be more relevant to the user.
>+ (void)findLocations:(NSString*)query withReferencePoint:(MSGeopoint* _Nullable)referencePoint withOptions:(MSMapLocationOptions* _Nullable)options handleResultWith:(MSMapLocationFinderResultHandler)handler
>
>// Overload that takes a reference geobounding box in addition to the default set of parameters. When you specify this parameter, the geographical area is taken into account when computing the results of a location query.
>+ (void)findLocations:(NSString*)query withReferenceBoundingBox:(MSGeoboundingBox* _Nullable)referenceBoundingBox withOptions:(MSMapLocationOptions* _Nullable)options handleResultWith:(MSMapLocationFinderResultHandler)handler
>
>// Overload that takes both geopoint and geobounding box as reference in addition to the default set of parameters.
>+ (void)findLocations:(NSString*)query withReferencePoint:(MSGeopoint* _Nullable)referencePoint withReferenceBoundingBox:(MSGeoboundingBox* _Nullable)referenceBoundingBox withOptions:(MSMapLocationOptions* _Nullable)options handleResultWith:(MSMapLocationFinderResultHandler)handler
>```

### FindLocationsAt

Forms and sends a reverse geocoding request by geopoint.

_See also:_
* [MapLocationOptions](MapLocationOptions-class.md)
* (Android) [OnMapLocationFinderResultListener](Android/OnMapLocationFinderResultListener-interface.md) | (iOS) [MapLocationFinderResultHandler](iOS/MapLocationFinderResultHandler-interface.md)
* [Geopoint](../map-control-api/Geopoint-class.md)

**Android**

>```java
>// Takes geopoint query, options (nullable), and callback.
>void findLocationsAt(Geopoint location, @Nullable MapLocationOptions options, OnMapLocationFinderResultListener callback)
>```

**iOS**

>```objectivec
>// Takes geopoint query, options (nullable), and callback handler.
>+ (void)findLocationsAt:(MSGeopoint*)location withOptions:(MSMapLocationOptions* _Nullable)options handleResultWith:(MSMapLocationFinderResultHandler)handler
>```

## Examples

### Android

```java
MapServices.SetCredentialsKey("...");

MapLocationOptions options = new MapLocationOptions()
    .setCulture("de")
    .setRegion("DE")
    .setMaxResults(20);

MapLocationFinder.findLocations("space needle", options, new OnMapLocationFinderResultListener() {
    @Override
    void onMapLocationFinderResult(MapLocationFinderResult result)
    {
        if (result.getStatus() == MapLocationFinderStatus.SUCCESS) {
            List<MapLocation> resultLocations = result.getLocations();
            // ...
        }
    }
});
```

### iOS

```objectivec
[MSMapServices setCredentialsKey:@"..."];

MSMapLocationOptions *options = [[MSMapLocationOptions alloc] init];
[options setCulture:@"de"];
[options setRegion:@"DE"];
[options setMaxResults:20];

[MSMapLocationFinder findLocations:@"space needle" withOptions:options handleResultWith:^void(MSMapLocationFinderResult *result) {
    if ([result status] == MSMapLocationFinderStatusSuccess) {
        NSArray<MSMapLocation*>* resultLocations = [result locations];
        // ...
    }
}];
```

## See Also

* [MapServices](MapServices-class.md)
