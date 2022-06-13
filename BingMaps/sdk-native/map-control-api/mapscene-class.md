---
title: MapScene Class | Microsoft Docs
description: Describes the MapScene class for Android and iOS and provide the class's static methods and additional references.
ms.author: pablocan
---

# MapScene Class

MapScene is the parent class of all MapScenes. A MapScene captures developer intent of what to display in the map.
MapScenes can be created via static factory methods on MapScene or descendants can be instantiated directly. To display a MapScene use `MapView.beginSetScene` and `MapView.setScene`.

**Android**

>```java
> public class MapScene
>```

**iOS**

>```objectivec
> @interface MSMapScene : NSObject
>```

## Static Methods

MapScene contains static methods for creating specific versions of MapScene.  Note that under the covers this will instantiate MapScenes with different state depending on the method (e.g., multiple locations vs. a single location).

### CreateFromLocation

Creates a map scene that displays a given location. The MapView determines how much around the point to display. For finer grained control of how close to the location to place the camera use `ofLocationAndRadius`.

_See also:_ [Geopoint](Geopoint-class.md)

**Android**

>```java
> static MapScene createFromLocation(Geopoint location)
> static MapScene createFromLocation(Geopoint location, @Nullable Double headingInDegrees, @Nullable Double pitchInDegrees)>
>```

**iOS**

>```objectivec
> + (instancetype)sceneWithLocation:(MSGeopoint *)location
> + (instancetype)sceneWithLocation:(MSGeopoint *)location heading:(CLLocationDirection)heading pitch:(double)pitch
>```

### CreateFromLocationAndRadius

Creates a map scene that displays the specified location and an amount of space around it.

_See also:_ [Geopoint](Geopoint-class.md)

**Android**

>```java
> static MapScene createFromLocationAndRadius(Geopoint location, double radiusInMeters) 
> static MapScene createFromLocationAndRadius(Geopoint location, double radiusInMeters, @Nullable Double headingInDegrees, @Nullable Double pitchInDegrees)
>```

**iOS**

>```objectivec
> + (instancetype)sceneWithLocation:(MSGeopoint *)location radius:(CLLocationDistance)radius
> + (instancetype)sceneWithLocation:(MSGeopoint *)location radius:(CLLocationDistance)radius heading:(CLLocationDirection)heading pitch:(double)pitch
>```

### CreateFromLocationAndZoomLevel

Creates a map scene that displays the specified location from the given zoom level.

_See also:_ [Geopoint](Geopoint-class.md)

**Android**

>```java
> static MapScene createFromLocationAndZoomLevel(Geopoint location, double zoomLevel) 
> static MapScene createFromLocationAndZoomLevel(Geopoint location, double zoomLevel, @Nullable Double headingInDegrees, @Nullable Double pitchInDegrees)
>```

**iOS**

>```objectivec
> + (instancetype)sceneWithLocation:(MSGeopoint *)location zoomLevel:(double)zoomLevel
> + (instancetype)sceneWithLocation:(MSGeopoint *)location zoomLevel:(double)zoomLevel heading:(CLLocationDirection)heading pitch:(double)pitch
>```

### CreateFromLocations

Creates a map scene that displays all of the locations, if possible.

_See also:_ [Geopoint](Geopoint-class.md)

**Android**

>```java
> static MapScene createFromLocations(java.lang.Iterable<Geopoint> locations)
> static MapScene createFromLocations(java.lang.Iterable<Geopoint> locations, @Nullable Double headingInDegrees, @Nullable Double pitchInDegrees)
>```

**iOS**

>```objectivec
> + (instancetype)sceneWithLocations:(NSArray<MSGeopoint *> *)locations
> + (instancetype)sceneWithLocations:(NSArray<MSGeopoint *> *)locations heading:(CLLocationDirection)heading pitch:(double)pitch
>```

### CreateFromLocationsAndMargin

Creates a map scene that displays all of the locations with specified additional margin in density-independent pixels, if possible.

_See also:_ [Geopoint](Geopoint-class.md)

**Android**

>```java
> static MapScene createFromLocationsAndMargin(java.lang.Iterable<Geopoint> locations, double marginInDeviceIndependentPixels)
> static MapScene createFromLocationsAndMargin(java.lang.Iterable<Geopoint> locations, double marginInDeviceIndependentPixels, @Nullable Double headingInDegrees, @Nullable Double pitchInDegrees)
>```

**iOS**

>```objectivec
> + (instancetype)sceneWithLocations:(NSArray<MSGeopoint *> *)locations margin:(double)margin
> + (instancetype)sceneWithLocations:(NSArray<MSGeopoint *> *)locations margin:(double)margin heading:(CLLocationDirection)heading pitch:(double)pitch
>```

### CreateFromLocationsAndMaxZoomLevel

Creates a map scene that displays all of the locations without zooming in further than a desired maximum zoom level, if possible.

_See also:_ [Geopoint](Geopoint-class.md)

**Android**

>```java
> static MapScene createFromLocationsAndMargin(java.lang.Iterable<Geopoint> locations, double maxZoomLevel)
> static MapScene createFromLocationsAndMargin(java.lang.Iterable<Geopoint> locations, double maxZoomLevel, @Nullable Double headingInDegrees, @Nullable Double pitchInDegrees)
>```

**iOS**

>```objectivec
> + (instancetype)sceneWithLocations:(NSArray<MSGeopoint *> *)locations maxZoomLevel:(double)maxZoomLevel
> + (instancetype)sceneWithLocations:(NSArray<MSGeopoint *> *)locations maxZoomLevel:(double)maxZoomLevel heading:(CLLocationDirection)heading pitch:(double)pitch
>```

### CreateFromLocationsAndMinRadius

Creates a map scene that displays all of the locations without zooming in further than a minimum amount of space around the center, if possible.

_See also:_ [Geopoint](Geopoint-class.md)

**Android**

>```java
> static MapScene createFromLocationsAndMargin(java.lang.Iterable<Geopoint> locations, double minRadiusInMeters)
> static MapScene createFromLocationsAndMargin(java.lang.Iterable<Geopoint> locations, double minRadiusInMeters, @Nullable Double headingInDegrees, @Nullable Double pitchInDegrees)
>```

**iOS**

>```objectivec
> + (instancetype)sceneWithLocations:(NSArray<MSGeopoint *> *)locations minRadius:(double)minRadius
> + (instancetype)sceneWithLocations:(NSArray<MSGeopoint *> *)locations minRadius:(double)minRadius heading:(CLLocationDirection)heading pitch:(double)pitch
>```

### CreateFromBoundingBox

Creates a map scene to display a particular bounding box. Equivalent to createFromLocations with each of the corners of the bounding box as points.

_See also:_ [GeoboundingBox](GeoboundingBox-class.md)

**Android**

>```java
> static MapScene createFromBoundingBox(GeoboundingBox boundingBox)
> static MapScene createFromBoundingBox(GeoboundingBox boundingbox, @Nullable Double headingInDegrees, @Nullable Double pitchInDegrees)
>```

**iOS**

>```objectivec
> + (instancetype)sceneWithBoundingBox:(MSGeoboundingBox *)boundingBox
> + (instancetype)sceneWithBoundingBox:(MSGeoboundingBox *)boundingBox heading:(CLLocationDirection)heading pitch:(double)pitch;
>```

### CreateFromBoundingBoxAndMargin

Creates a map scene to display a particular bounding box with specified margin in device-independent pixels from each side.

_See also:_ [GeoboundingBox](GeoboundingBox-class.md)

**Android**

>```java
> static MapScene createFromBoundingBoxAndMargin(GeoboundingBox boundingBox, double leftMarginInDeviceIndependentPixels, double topMarginInDeviceIndependentPixels, double rightMarginInDeviceIndependentPixels, double bottomMarginInDeviceIndependentPixels)
> static MapScene createFromBoundingBoxAndMargin(GeoboundingBox boundingbox, double leftMarginInDeviceIndependentPixels, double topMarginInDeviceIndependentPixels, double rightMarginInDeviceIndependentPixels, double bottomMarginInDeviceIndependentPixels, @Nullable Double headingInDegrees, @Nullable Double pitchInDegrees)
>```

**iOS**

>```objectivec
> + (instancetype)sceneWithBoundingBox:(MSGeoboundingBox *)boundingBox leftMargin:(double)leftMargin topMargin:(double)topMargin rightMargin:(double)rightMargin bottomMargin:(double)bottomMargin
> + (instancetype)sceneWithBoundingBox:(MSGeoboundingBox *)boundingBox leftMargin:(double)leftMargin topMargin:(double)topMargin rightMargin:(double)rightMargin bottomMargin:(double)bottomMargin heading:(CLLocationDirection)heading pitch:(double)pitch
>```

### CreateFromCamera

Creates a MapScene that displays from a specified viewpoint instead of displaying a target.

_See also:_ [MapCamera](MapCamera-class.md)

**Android**

>```java
> static MapScene createFromCamera(MapCamera camera)
>```

**iOS**

>```objectivec
> + (instancetype)sceneWithCamera:(MSMapCamera *)camera
>```

## See Also

* [Map Scenes, and Cameras](../map-control-concepts/map-scenes-and-cameras.md)
