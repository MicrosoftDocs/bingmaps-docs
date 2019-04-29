
# MapScene Class

MapScene is the parent class of all MapScenes. A MapScene captures developer intent of what to display in the map.
MapScenes can be created via static factory methods on MapScene or descendants can be instantiated directly. To display a MapScene use `MapView.beginSetScene` and `MapView.setScene`.

**Android**

>```java
> public class MapScene
>```

**iOS**

>``` objectivec
> @interface MSMapScene : NSObject
>```

## Static Methods

MapScene contains static methods for creating specific versions of MapScene.  Note that under the covers this will instantiate MapScenes with different state depending on the method (e.g., multiple locations vs. a single location).

### createFromLocation

Creates a map scene that displays a given location. The MapView determines how much around the point to display. For finer grained control of how close to the location to place the camera use `ofLocationAndRadius`.

_See also:_ [Geolocation](Geolocation.md)

**Android**

>```java
> MapSceneOfLocation createFromLocation(Geolocation location)  
> MapSceneOfLocation createFromLocation(Geolocation location, double headingInDegrees, double pitchInDegrees)>
>```

**iOS**

>```objectivec
> + (instancetype)sceneWithLocation:(MSGeolocation *)location
> + (instancetype)sceneWithLocation:(MSGeolocation *)location heading:(double)heading pitch:(double)pitch
>```  

### createFromLocationAndRadius

Creates a map scene that displays the specified location and an amount of space around it.

_See also:_ [Geolocation](Geolocation.md)

**Android**

>```java
> MapSceneOfLocationAndRadius createFromLocationAndRadius(Geolocation location, double radiusInMeters) 
> MapSceneOfLocationAndRadius createFromLocationAndRadius(Geolocation location, double radiusInMeters, double headingInDegrees, double pitchInDegrees)
>```

**iOS**

>```objectivec
> + (instancetype)sceneWithLocation:(MSGeolocation *)location radius:(double)radius
> + (instancetype)sceneWithLocation:(MSGeolocation *)location radius:(double)radius heading:(double)heading pitch:(double)pitch
>```  

### createFromLocationAndZoomLevel

Creates a map scene that displays the specified location from the given zoom level.

_See also:_ [Geolocation](Geolocation.md)

**Android**

>```java
> MapSceneOfLocationWithZoomLevel createFromLocationAndZoomLevel(Geolocation location, double zoomLevel) 
> MapSceneOfLocationWithZoomLevel createFromLocationAndZoomLevel(Geolocation location, double zoomLevel, double headingInDegrees, double pitchInDegrees)
>```

**iOS**

>```objectivec
> + (instancetype)sceneWithLocation:(MSGeolocation *)location zoomLevel:(double)zoomLevel
> + (instancetype)sceneWithLocation:(MSGeolocation *)location zoomLevel:(double)zoomLevel heading:(double)heading pitch:(double)pitch
>```  

### createFromLocations

Creates a map scene that displays all of the locations, if possible.

_See also:_ [Geolocation](Geolocation.md)

**Android**

>```java
> MapSceneOfLocations createFromLocations(java.lang.Iterable<Geolocation> locations)
> MapSceneOfLocations createFromLocations(java.lang.Iterable<Geolocation> locations, double headingInDegrees, double pitchInDegrees)
>```

**iOS**

>```objectivec
> + (instancetype)sceneWithLocations:(NSArray<MSGeolocation *> *)locations
>```+ (instancetype)sceneWithLocations:(NSArray<MSGeolocation *> *)locations heading:(double)heading pitch:(double)pitch
>```  

### createFromLocationsAndMargin

Creates a map scene that displays all of the locations with specified additional margin in density-independent pixels, if possible.

_See also:_ [Geolocation](Geolocation.md)

**Android**

>```java
> MapSceneOfLocationsWithMargin createFromLocationsAndMargin(java.lang.Iterable<Geolocation> locations, double marginInDeviceIndependentPixels)
> MapSceneOfLocationsWithMargin createFromLocationsAndMargin(java.lang.Iterable<Geolocation> locations, double marginInDeviceIndependentPixels, double headingInDegrees, double pitchInDegrees)
>```

**iOS**

>```objectivec
> + (instancetype)sceneWithLocations:(NSArray<MSGeolocation *> *)locations margin:(double)margin
> + (instancetype)sceneWithLocations:(NSArray<MSGeolocation *> *)locations margin:(double)margin heading:(double)heading pitch:(double)pitch
> ```  

### createFromBoundingBox

Creates a map scene to display a particular bounding box. Equivalent to createFromLocations with each of the corners of the bounding box as points.

_See also:_ [GeoboundingBox](GeoboundingBox.md)

**Android**

>```java
> MapSceneOfBoundingBox createFromBoundingBox(GeoboundingBox boundingBox)
>```

**iOS**

>```objectivec
> + (instancetype)sceneWithBoundingBox:(MSGeoboundingBox *)geoBoundingBox
>```  

### createFromBoundingBoxAndMargin

Creates a map scene to display a particular bounding box with specified margin in device-independent pixels from each side.

_See also:_ [GeoboundingBox](GeoboundingBox.md)

**Android**

>```java
> MapSceneOfBoundingBoxWithMargin createFromBoundingBoxAndMargin(GeoboundingBox boundingBox, double leftMarginInDeviceIndependentPixels, double topMarginInDeviceIndependentPixels, double rightMarginInDeviceIndependentPixels, double bottomMarginInDeviceIndependentPixels)
>```

**iOS**

>```objectivec
> + (instancetype)sceneWithBoundingBox:(MSGeoboundingBox *)geoBoundingBox leftMargin:(double)leftMargin topMargin:(double)topMargin rightMargin:(double)rightMargin bottomMargin:(double)bottomMargin
> + (instancetype)sceneWithBoundingBox:(MSGeoboundingBox *)geoBoundingBox leftMargin:(double)leftMargin topMargin:(double)topMargin rightMargin:(double)rightMargin bottomMargin:(double)bottomMargin heading:(double)heading pitch:(double)pitch
>```

### createFromCamera

Creates a MapScene that displays from a specified viewpoint instead of displaying a target.

_See also:_ [MapCamera](MapCamera.md)

*Android**

>```java
> MapSceneFromCamera createFromCamera(MapCamera camera)
>```

**iOS**

>```objectivec
> + (instancetype)sceneWithCamera:(MSMapCamera *)camera
>```  

## See Also

* [Map Scenes, and Cameras](../map-control-concepts/Map_Scenes_and_Cameras.md)
