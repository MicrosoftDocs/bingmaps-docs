# MapLocationFinder Class

Forms and sends geocoding requests.

## Static Methods

### FindLocations

Forms and sends a geocoding request by string query.

_See also:_

* [MapLocationOptions](MapLocationOptions-class.md)
* (Android) [MapLocationCallback](Android/MapLocationCallback-interface.md) | (iOS) [MapLocationFinderResultHandler](iOS/MapLocationFinderResultHandler-interface.md)

**Android**

>```java
>// Default overload: takes string query, options (nullable), and callback.
>void findLocations(String query, MapLocationOptions options, MapLocationCallback callback)
>
>// Overload that takes a reference geolocation in addition to the default set of parameters. When you specify this parameter, the location is taken into account and the results returned may be more relevant to the user.
>void findLocations(String query, Geolocation referencePoint, MapLocationOptions options, MapLocationCallback callback)
>
>// Overload that takes a reference geobounding box in addition to the default set of parameters. When you specify this parameter, the geographical area is taken into account when computing the results of a location query.
>void findLocations(String query, GeoboundingBox referenceBoundingBox, MapLocationOptions options, MapLocationCallback callback)
>
>// Overload that takes both geolocation and geobounding box as reference in addition to the default set of parameters.
>void findLocations(String query, Geolocation referencePoint, GeoboundingBox referenceBoundingBox, MapLocationOptions options, MapLocationCallback callback)
>```

**iOS**

>```objectivec
>// Default overload: takes string query, options (nullable), and callback handler.
>+ (void)findLocations:(NSString*)query withOptions:(MSMapLocationOptions* _Nullable)options handleResultWith:(MSMapLocationFinderResultHandler)handler
>
>// Overload that takes a reference geolocation in addition to the default set of parameters. When you specify this parameter, the location is taken into account and the results returned may be more relevant to the user.
>+ (void)findLocations:(NSString*)query withReferencePoint:(MSGeolocation* _Nullable)referencePoint withOptions:(MSMapLocationOptions* _Nullable)options handleResultWith:(MSMapLocationFinderResultHandler)handler
>
>// Overload that takes a reference geobounding box in addition to the default set of parameters. When you specify this parameter, the geographical area is taken into account when computing the results of a location query.
>+ (void)findLocations:(NSString*)query withReferenceBoundingBox:(MSGeoboundingBox* _Nullable)referenceBoundingBox withOptions:(MSMapLocationOptions* _Nullable)options handleResultWith:(MSMapLocationFinderResultHandler)handler
>
>// Overload that takes both geolocation and geobounding box as reference in addition to the default set of parameters.
>+ (void)findLocations:(NSString*)query withReferencePoint:(MSGeolocation* _Nullable)referencePoint withReferenceBoundingBox:(MSGeoboundingBox* _Nullable)referenceBoundingBox withOptions:(MSMapLocationOptions* _Nullable)options handleResultWith:(MSMapLocationFinderResultHandler)handler
>```

### FindLocationsAt

Forms and sends a reverse geocoding request by geolocation.

_See also:_
* [MapLocationOptions](MapLocationOptions-class.md)
* (Android) [MapLocationCallback](Android/MapLocationCallback-interface.md) | (iOS) [MapLocationFinderResultHandler](iOS/MapLocationFinderResultHandler-interface.md)
* [Geolocation](../map-control-api/Geolocation-class.md)

**Android**

>```java
>// Takes geolocation query, options (nullable), and callback.
>void findLocationsAt(Geolocation location, MapLocationOptions options, MapLocationCallback callback)
>```

**iOS**

>```objectivec
>// Takes geolocation query, options (nullable), and callback handler.
>+ (void)findLocationsAt:(MSGeolocation*)location withOptions:(MSMapLocationOptions* _Nullable)options handleResultWith:(MSMapLocationFinderResultHandler)handler
>```

## Examples

### Android

```java
MapServices.SetCredentialsKey("...");

MapLocationOptions options = new MapLocationOptions()
    .setCulture("de")
    .setRegion("DE")
    .setMaxResults(20);

MapLocationFinder.findLocations("space needle", options, new MapLocationCallback() {
    @Override
    void onResult(MapLocationFinderResult result)
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
