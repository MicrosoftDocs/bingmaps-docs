---
title: MapView Class | Microsoft Docs
description: Describes the MapView class for Android and iOS and provides the class's constructors, properties, methods, events, and accessibility features.
ms.author: pablocan
---

# MapView Class

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

This is the master class for using the Map functionality within maps.

**Android**

>```java
> class MapView extends FrameLayout
>```

**iOS**

>```objectivec
> @interface MSMapView : UIView
>```

_See also:_ [UIView](https://developer.apple.com/documentation/uikit/uiview)

## Constructors

**Android**

>```java
> MapView(android.content.Context context, MapRenderMode rasterRenderMode)
> MapView(android.content.Context context, android.util.AttributeSet attributeSet, MapRenderMode rasterRenderMode)
>```

## Properties

### Bounds

Returns the current geo-bounding box bounds of the current view.

_See also:_ [GeoboundingBox](GeoboundingBox-class.md)

**Android**

>```java
> GeoboundingBox getBounds()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) MSGeoboundingBox *mapBounds
>```

### BuildingsVisible

Determines whether 3D buildings are rendered on the map.

**Android**

>```java
> boolean isBuildingsVisible()
> void setBuildingsVisible(boolean visible)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL buildingsVisible
>```

### BusinessLandmarksVisible

Determines whether business landmarks (e.g., restaurants, hotels) are rendered on the map.

**Android**

>```java
> boolean isBusinessLandmarksVisible()
> void setBusinessLandmarksVisible(boolean visible)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL businessLandmarksVisible
>```

### Camera

Returns the current perspective of the current view of the map. The map's camera settings are updated whenever
the view of the map is changed. For example, when updating the Center property or calling the SetScene method.

_See also:_ [MapCamera](MapCamera-class.md)

**Android**

>```java
> MapCamera getMapCamera()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) MSMapCamera *camera
>```

### Center

Returns the center of the current view. Keep in mind that in oblique views (where some horizon is shown),
the "center" that is returned may not be at the physical center of the control's viewable rectangle.

_See also:_ [Geopoint](Geopoint-class.md)

**Android**

>```java
> Geopoint getCenter()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) MSGeopoint *mapCenter
>```

### FullVisibleRegion

Returns the current geopath that is the right-hand traverse of the currently visible area.

_See also:_ [Geopath](geopath-class.md)

**Android**

>```java
> Geopath getFullVisibleRegion()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) MSGeopath *fullVisibleRegion
>```

### NearVisibleRegion

Returns the current geopath  is the right-hand traverse of the approximate area of interest in the current map view.

_See also:_ [Geopath](geopath-class.md)

**Android**

>```java
> Geopath getNearVisibleRegion()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) MSGeopath *nearVisibleRegion
>```

### Heading

Specifies the heading of the view in degrees where `0` is north, `90` is east, `180` is south, and `270` is west.  
Valid values are between `0` and `360`.

**Android**

>```java
> double getHeading()
> void setHeading(float heading)
>```

**iOS**

>```objectivec
> @property (nonatomic) CLLocationDirection heading
>```

### Language

Specifies the language to be used when rendering locale-specific strings like country/region and city names.  
The string can be an ISO 639 two-letter lowercase culture code associated with a language. Example values: `"en"`,
`"fr"`, `"ja"`.  
The string can optionally be combined with an ISO 3166 two-letter uppercase subculture code associated with a country/region
or region (delimited by `-`). Example values: `"en-US"`, `"ko-KR"`, `"ja-JP"`.

**Android**

>```java
> String getLanguage()
> void setLanguage(String language)
>```

**iOS**

>```objectivec
> @property (nonatomic) NSString *language
>```

### CredentialsKey

Specifies the license key authorizing use of the map. Get credentials at [www.bingmapsportal.com](http://www.bingmapsportal.com/).

**Android**

>```java
> void setCredentialsKey(String credentialsKey)
>```

**iOS**

>```objectivec
> @property (nonatomic) IBInspectable NSString *credentialsKey
>```

### Layers
Returns developer-added layers of content for the map.  
Note that this concept of independent layers doesn't exist on the Windows version of the control.
Rather, on Windows, directly add any elements you may have the to the MapElements collection exposed
on the control.

_See also:_ [MapLayerCollection](MapLayerCollection-class.md)

**Android**

>```java
> MapLayerCollection getLayers()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) MSMapLayerCollection *layers
>```


### RenderMode

Determines whether to render maps using raster tiles or vector data. Raster tiles will generally give a faster framerate
at the expense of less readable text.

_See also:_ [MapRenderMode](MapRenderMode-enumeration.md)

**Android**

>```java
> MapRenderMode getMapRenderMode()  
> void setMapRenderMode(MapRenderMode mapRenderMode)
>```

**iOS**

>```objectivec
> @property (nonatomic) MSMapRenderMode renderMode
>```

### Projection

Specifies the projection used to render the map.

_See also:_ [MapProjection](MapProjection-enumeration.md)

**Android**

>```java
> MapProjection getMapProjection() 
> void setMapProjection(MapProjection mapProjection)
>```

**iOS**

>```objectivec
> @property (nonatomic) MSMapProjection projection
>```

### MapSize

Specifies the size of rendered map in device-independent pixels.

Note that in Android, class `android.graphics.Point` is used since `android.util.Size` is only available in API level 21.

**Android**

>```java
> Point getMapSize()  
> void setMapSize(Point size)
>```

**iOS**

>```objectivec 
> @property (nonatomic) CGSize mapSize
>```
<!--
### PermissionsDelegate (Android only)

Sets the delegate to handle permission requests. Clients should forward requests to the Android framework as appropriate.

>```java
> @RequiresApi(VERSION_CODES.M)
> void setPermissionsDelegate(MapPermissionsDelegate delegate)
>```

_See also:_
* [MapPermissionsDelegate](android/mappermissionsdelegate-interface.md)
* [MapPermissionsCallback](android/mappermissionscallback-interface.md)
* [MapPermissionsRequestArgs](android/mappermissionsrequestargs-class.md)
* [MapPermissionsRequestReason](android/mappermissionsrequestreason-enumeration.md)
-->
### Pitch

Specifies the pitch of the camera in degrees, where `0` is looking straight down (minimum) and `90` is looking towards
the horizon (maximum). Values outside of this range will cause an exception.  
Note that pitch may be limited in some views.

**Android**

>```java
> double getPitch()  
> void setPitch(double pitch)
>```

**iOS**

>```objectivec
> @property (nonatomic) double pitch
>```

### Region

Specifies the region of the world to display a map for. Different regions of the world have different views of the
world including borders and contested regions.  
The string can be an ISO 3166 two-letter uppercase code associated with a country or region. 
Example values: `"US"`, `"CA"`, `"FR"`.

**Android**

>```java
> String getRegion()
> void setRegion(String region)
>```

**iOS**

>```objectivec
> @property (nonatomic) NSString *region
>```

### TransitFeaturesVisible

Determines whether transit features (e.g., transit stops) are rendered on the map.

**Android**

>```java
> boolean isTransitFeaturesVisible()
> void setTransitFeaturesVisible(boolean visible)
>```

**iOS**

>```objectivec
> @property (nonatomic) BOOL transitFeaturesVisible
>```

### UserInterfaceOptions

Returns a container class that lets a developer access configuration controls for the map user interface.

_See also:_ [MapUserInterfaceOptions](MapUserInterfaceOptions-class.md)

**Android**

>```java
> MapUserInterfaceOptions getUserInterfaceOptions()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) MSMapUserInterfaceOptions *userInterfaceOptions
>```

### ViewPadding

Specifies the padding inside the map control in device-independent pixels.

**Android**

>```java
> void setViewPadding(ViewPadding viewPadding)
> ViewPadding getViewPadding()
> 
> @Deprecated
> void setViewPadding(double left, double top, double right, double bottom)
>```
_See also:_ [ViewPadding](ViewPadding-class.md)
**iOS**

>```objectivec
> @property (nonatomic) UIEdgeInsets viewPadding
>```

_See also:_ [UIEdgeInsets](https://developer.apple.com/documentation/uikit/uiedgeinsets)

### ZoomLevel

Returns the zoom level of the current view.

**Android**

>```java
> double getZoomLevel()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) double zoomLevel
>```

### StyleSheet

Specifies the style sheet that defines the style of the map, such as Road Light, Aerial, or other styles.

_See also:_ [MapStyleSheet](MapStyleSheet-class.md)

**Android**

>```java
> MapStyleSheet getMapStyleSheet()
> void setMapStyleSheet(MapStyleSheet mapStyleSheet)
>```

**iOS**

>```objectivec
> @property (nonatomic) MSMapStyleSheet *styleSheet
>```

### UserLocation

Returns an instance of the MapUserLocation class to access the user location API.

_See also:_ [MapUserLocation](mapuserlocation-class.md)

**Android**

>```java
> MapUserLocation getUserLocation()
>```

**iOS**

>```objectivec
> @property(nonatomic, readonly) MSMapUserLocation* userLocation
>```

## Lifecycle methods (Android only)

You must override lifecycle methods in parent activity or fragment, and call respective MapView methods listed below.

_See also:_ [Understand the Activity Lifecycle](https://developer.android.com/guide/components/activities/activity-lifecycle)

### OnCreate

Map handler for Create event.

_See also:_
* [android.app.Activity.onCreate(android.os.Bundle)](https://developer.android.com/reference/android/app/Activity#onCreate%28android.os.Bundle%29)
* [androidx.fragment.app.Fragment.onCreate(android.os.Bundle)](https://developer.android.com/reference/androidx/fragment/app/Fragment#onCreate%28android.os.Bundle%29)

>```java
> void onCreate(@Nullable Bundle savedInstanceState)
>```

### OnStart

Map handler for Start event. Starts the map, creating rendering resources as necessary.

_See also:_
* [android.app.Activity.onStart()](https://developer.android.com/reference/android/app/Activity#onStart%28%29)
* [androidx.fragment.app.Fragment.onStart()](https://developer.android.com/reference/androidx/fragment/app/Fragment#onStart%28%29)

>```java
> void onStart()
>```

### OnResume

Map handler for Resume event.

_See also:_
* [android.app.Activity.onResume()](https://developer.android.com/reference/android/app/Activity#onResume%28%29)
* [androidx.fragment.app.Fragment.onResume()](https://developer.android.com/reference/androidx/fragment/app/Fragment#onResume%28%29)

>```java
> void onResume()
>```

### OnPause

Map handler for Pause event.

_See also:_
* [android.app.Activity.onPause()](https://developer.android.com/reference/android/app/Activity#onPause%28%29)
* [androidx.fragment.app.Fragment.onPause()](https://developer.android.com/reference/androidx/fragment/app/Fragment#onPause%28%29)

>```java
> void onPause()
>```

### OnSaveInstanceState

Map handler for Save Instance State event.

_See also:_
* [android.app.Activity.onSaveInstanceState(android.os.Bundle)](https://developer.android.com/reference/android/app/Activity#onSaveInstanceState%28android.os.Bundle%29)
* [androidx.fragment.app.Fragment.onSaveInstanceState(android.os.Bundle)](https://developer.android.com/reference/androidx/fragment/app/Fragment#onSaveInstanceState%28android.os.Bundle%29)

>```java
> void onSaveInstanceState(Bundle outState)
>```

### OnStop

Map handler for Stop event. Suspends the map, freeing up resources as necessary.

_See also:_
* [android.app.Activity.onStop()](https://developer.android.com/reference/android/app/Activity#onStop%28%29)
* [androidx.fragment.app.Fragment.onStop()](https://developer.android.com/reference/androidx/fragment/app/Fragment#onStop%28%29)

>```java
> void onStop()
>```

### OnDestroy

Map handler for Destroy event. Disposes the map, releasing all resources.

_See also:_
* [android.app.Activity.onDestroy()](https://developer.android.com/reference/android/app/Activity#onDestroy%28%29)
* [androidx.fragment.app.Fragment.onDestroy()](https://developer.android.com/reference/androidx/fragment/app/Fragment#onDestroy%28%29)

>```java
> void onDestroy()
>```

### OnLowMemory

Map handler for Low Memory event.

_See also:_
* [android.app.Activity.onLowMemory()](https://developer.android.com/reference/android/app/Activity#onLowMemory%28%29)
* [androidx.fragment.app.Fragment.onLowMemory()](https://developer.android.com/reference/androidx/fragment/app/Fragment#onLowMemory%28%29)

>```java
> void onLowMemory()
>```

## Methods

### SetBackgroundColor

The background color of the map that is rendered if there is nothing else to render. As soon as map tiles are available to render the background color is controlled by the active MapStyleSheet instead.

**Android**

>```java
> void setBackgroundColor(int color)
>```

**iOS**

>```objectivec
> - (void)setMapBackgroundColor:(UIColor *)color
>```

### CancelAnimation

Cancels the active animation, if running. If an animation is not running, this method does nothing.

**Android**

>```java
> void cancelAnimation()
>```

**iOS**

>```objectivec
> - (void)cancelAnimation
>```

### CaptureImage

Begins an asynchronous operation to capture a screenshot of the MapView.

**Android**

>```java
> void beginCaptureImage(CaptureScreenShotListener listener)
>```

_See also:_ [CaptureScreenshotListener](Android/CaptureScreenShotListener-interface.md)

**iOS**

>```objectivec
> - (void)beginCaptureImageWithCompletionCallback:(MSMapDidCaptureImageCallback)callback
>```

_See also:_ [MSMapDidCaptureImageCallback](iOS/MSMapDidCaptureImageCallback-interface.md)

### FindMapElementsAtOffset

Returns the MapElements that are near a Point offset on the map. This API can be used to implement hit testing of MapElements. For example, on a Tapped event, it can be used to return the closest MapIcon and then that
MapIcon's flyout can be shown.

**Android**

>```java
> LinkedList<MapElement> findMapElementsAtOffset(Point offset)
>```

**iOS**

>```objectivec
> - (NSSet<MSMapElement *> *)findMapElementsAtOffset:(CGPoint)offset
>```

### IsLocationInView

Returns whether the given location is visible in the map view.

**Android**

>```java
> boolean isLocationInView(Geopoint location)
>```

**iOS**

>```objectivec
> - (BOOL)doesViewContainLocation:(MSGeopoint *)location
>```

### LocationFromOffset

Converts a point relative to the map view to a geographic location, with an option to select a desired altitude reference
system. Note that the return value can be null: for instance, a point in the sky will fail to return a location.

**Android**

These methods operate with screen pixels.

>```java
> @Nullable Geopoint getLocationFromOffset(Point offset)
> @Nullable Geopoint getLocationFromOffset(Point offset, AltitudeReferenceSystem desiredAltitudeReferenceSystem)
>```

**iOS**

These methods operate with device-independent points.

>```objectivec
> - (BOOL)tryToConvertOffset:(CGPoint)offset 
>               intoLocation:(MSGeopoint * _Nullable * _Nonnull)location  
> - (BOOL)tryToConvertOffset:(CGPoint)offset 
>     usingAltitudeReference:(MSAltitudeReferenceSystem)altitudeReferenceSystem 
>               intoLocation:(MSGeopoint * _Nullable * _Nonnull)location
>```

### OffsetFromLocation

Converts a geographic location to a point on the map (pixel offset). Note that the return value can be null, for instance, locations that are not in view will fail to return an offset.

**Android**

>```java
> @Nullable Point getOffsetFromLocation(Geopoint location)
>```

**iOS**

>```objectivec
> - (BOOL)tryToConvertLocation:(MSGeopoint *)location intoOffset:(CGPoint *)offset
>```

### Rotate

Rotates the map by the specified number of degrees.

**Android**

>```java
> void rotate(double degrees)
>```

**iOS**

>```objectivec
> - (void)rotateWithDegrees:(CLLocationDirection)degrees
>```

### RotateTo

Performs a rotate operation to a particular point. rotateTo(0) will put the MapView with north up.

**Android**

>```java
> void rotateTo(double angleInDegrees)
>```

**iOS**

>```objectivec
> - (void)rotateToDegrees:(CLLocationDirection)degrees
>```

### BeginRotate

Performs a rotate operation and invokes the callback when complete.

**Android**

>```java
> void beginRotate(double degrees, @Nullable OnMapSceneCompletedListener listener)
>```

_See also:_ [OnMapSceneCompletedListener](Android/OnMapSceneCompletedListener-interface.md)

**iOS**

>```objectivec
> - (void)beginRotateWithDegrees:(CLLocationDirection)degrees completionCallback:(MSMapDidChangeSceneCallback)callback
>```

_See also:_ [MSMapDidChangeSceneCallback](iOS/MSMapDidChangeSceneCallback-interface.md)

### BeginRotateTo

Perform a rotate operation to a particular point and invokes the callback when complete. beginRotateTo(0) will put the MapView with north up.

**Android**

>```java
> void beginRotateTo(double angle, @Nullable OnMapSceneCompletedListener listener)
>```

_See also:_ [OnMapSceneCompletedListener](Android/OnMapSceneCompletedListener-interface.md)

**iOS**

>```objectivec
> - (void)beginRotateToDegrees:(CLLocationDirection)degrees withCompletionCallback:(MSMapDidChangeSceneCallback)callback;
>```

_See also:_ [MSMapDidChangeSceneCallback](iOS/MSMapDidChangeSceneCallback-interface.md)

### SetMapStyleSheet

*DEPRECATED*  
Use the `StyleSheet` property instead.

Sets the style sheet that defines the style of the map, such as Road Light, Aerial, or other styles.

_See also:_ [MapStyleSheet](MapStyleSheet-class.md)

**Android**

>```java
> void setMapStyleSheet(MapStyleSheet mapStyleSheet)
>```

**iOS**

>```objectivec
> - (void)setStyleSheet:(MSMapStyleSheet*)mapStyleSheet;
>```

### SetScene

Sets the scene of the map based on the animation provided.

_See also:_
* [MapScene](MapScene-class.md)
* [MapAnimationKind](MapAnimationKind-enumeration.md)

**Android**

>```java
> void setScene(MapScene scene, MapAnimationKind kind)
>```

**iOS**

>```objectivec
> - (void)setScene:(MSMapScene *)scene withAnimationKind:(MSMapAnimationKind)kind
>```

### BeginSetScene

Sets the scene of the map based on the animation provided. When the scene has finished changing, the provided callback is invoked.

_See also:_
* [MapScene](MapScene-class.md)
* [MapAnimationKind](MapAnimationKind-enumeration.md)

**Android**

>```java
> void beginSetScene(MapScene scene, MapAnimationKind kind, @Nullable OnMapSceneCompletedListener listener)
>```

_See also:_ [OnMapSceneCompletedListener](Android/OnMapSceneCompletedListener-interface.md)

**iOS**

>```objectivec
> - (void)beginSetScene:(MSMapScene *)scene withAnimationKind:(MSMapAnimationKind)kind withCompletionCallback:(MSMapDidChangeSceneCallback)callback
>```

_See also:_ [MSMapDidChangeSceneCallback](iOS/MSMapDidChangeSceneCallback-interface.md)

### StartContinuousPan

Performs a continuous pan operation.

**Android**

>```java
> void startContinuousPan(double horizontalDeviceIndependentPixelsPerSecond, double verticalDeviceIndependentPixelsPerSecond)
>```

**iOS**

>```objectivec
> - (void)startContinuousPanWithHorizontalPointsPerSecond:(double)horizontalPointsPerSecond verticalPointsPerSecond:(double)verticalPointsPerSecond
>```

### StartContinuousRotate

Starts a continuous rotate operation.

**Android**

>```java
> void startContinuousRotate(double rateInDegreesPerSecond)
>```

**iOS**

>```objectivec
> - (void)startContinuousRotateWithDegreesPerSecond:(double)degreesPerSecond
>```

### StartContinuousTilt

Performs a continuous tilt operation. Call `stopContinuousTilt` to stop an in-progress tilt.

**Android**

>```java
> void startContinuousTilt(double rateInDegreesPerSecond)
>```

**iOS**

>```objectivec
> - (void)startContinuousTiltWithDegreesPerSecond:(double)degreesPerSecond
>```

### StartContinuousZoom

Performs an ongoing zoom operation.

**Android**

>```java
> void startContinuousZoom(double rateOfChangePerSecond)
>```

**iOS**

>```objectivec
> - (void)startContinuousZoomWithZoomLevelsPerSecond:(double)zoomLevelsPerSecond
>```

### StopContinuousPan

Stops a continuous pan operation.

**Android**

>```java
> void stopContinuousPan()
>```

**iOS**

>```objectivec
> - (void)stopContinuousPan
>```

### StopContinuousRotate

Stops a previously started rotate operation

**Android**

>```java
> void stopContinuousRotate()
>```

**iOS**

>```objectivec
> - (void)stopContinuousRotate
>```

### StopContinuousTilt

Stops an in-progress tilt operation.

**Android**

>```java
> void stopContinuousTilt()
>```

**iOS**

>```objectivec
> - (void)stopContinuousTilt
>```

### StopContinuousZoom

Stops a continuous zoom operation.

**Android**

>```java
> void stopContinuousZoom()
>```

**iOS**

>```objectivec
> - (void)stopContinuousZoom
>```

### Tilt

Performs an operation to tilt the map's camera from its current position. Valid values are between -90 and 90. Invalid values will be clamped.

**Android**

>```java
> void tilt(double degrees)
>```

**iOS**

>```objectivec
> - (void)tiltWithDegrees:(double)degrees
>```

### BeginTilt

Performs an operation to tilt the map's camera from its current position and invokes the callback when complete. Valid values are between -90 and 90. Invalid values will be clamped.

**Android**

>```java
> void beginTilt(double degrees, @Nullable OnMapSceneCompletedListener listener)
>```

_See also:_ [OnMapSceneCompletedListener](Android/OnMapSceneCompletedListener-interface.md)

**iOS**

>```objectivec
> - (void)beginTiltWithDegrees:(double)degrees completionCallback:(MSMapDidChangeSceneCallback)callback
>```

_See also:_ [MSMapDidChangeSceneCallback](iOS/MSMapDidChangeSceneCallback-interface.md)

### TiltTo

Performs a tilt operation to a particular point. `tiltTo(0)` to have the map face nadir. Valid values are between 0 and 90. Invalid values will be clamped.


**Android**

>```java
> void tiltTo(double degrees)
>```

**iOS**

>```objectivec
> - (void)tiltToDegrees:(double)degrees
>```

### BeginTiltTo

Performs a tiltTo operation and invokes the callback when complete. Valid values are between 0 and 90. Invalid values will be clamped.

**Android**

>```java
> void beginTiltTo(double degrees, @Nullable OnMapSceneCompletedListener listener)
>```

_See also:_ [OnMapSceneCompletedListener](Android/OnMapSceneCompletedListener-interface.md)

**iOS**

>```objectivec
> - (void)beginTiltToDegrees:(double)degrees withCompletionCallback:(MSMapDidChangeSceneCallback)callback
>```

_See also:_ [MSMapDidChangeSceneCallback](iOS/MSMapDidChangeSceneCallback-interface.md)

### CanTiltDown

Returns true if tilting down (away from nadir) is possible.

**Android**

>```java
> boolean canTiltDown()
>```

**iOS**

>```objectivec
> - (BOOL)canTiltDown
>```

### CanTiltUp

Returns true if tilting up (towards nadir) is possible.

**Android**

>```java
> boolean canTiltUp()
>```

**iOS**

>```objectivec
> - (BOOL)canTiltUp
>```

### ZoomIn

Performs a zoom in operation, equivalent to double tapping on the map.

Note that this void is also repeatable, such that if called multiple times in rapid order (e.g., the user repeatedly presses the zoom in button), the resulting operation is still smooth.

**Android**

>```java
> void zoomIn()
>```

**iOS**

>```objectivec
> - (void)zoomIn
>```

### ZoomOut

Performs a zoom out operation, equivalent to clicking the zoom out button on the map.
Note that this method is also repeatable, such that if called multiple times in rapid order (e.g., the user repeatedly presses the zoom out button), the resulting operation is still smooth.

**Android**

>```java
> void zoomOut()
>```

**iOS**

>```objectivec
> - (void)zoomOut
>```

### ZoomTo

Performs a zoom operation to the specified zoom level.

**Android**

>```java
> void zoomTo(double zoomLevel)
>```

**iOS**

>```objectivec
> - (void)zoomToLevel:(double)zoomLevel
>```

### BeginZoomIn

Performs a zoom in operation, equivalent to double tapping on the map, and invokes the provided callback when the zoom is complete.

**Android**

>```java
> void beginZoomIn(@Nullable OnMapSceneCompletedListener listener)
>```

_See also:_ [OnMapSceneCompletedListener](Android/OnMapSceneCompletedListener-interface.md)

**iOS**

>```objectivec
> - (void)beginZoomInWithCompletionCallback:(MSMapDidChangeSceneCallback)callback
>```

_See also:_ [MSMapDidChangeSceneCallback](iOS/MSMapDidChangeSceneCallback-interface.md)

### BeginZoomOut

Performs a zoom out operation, equivalent to double tapping on the map, and invokes the provided callback when the zoom is complete.

**Android**

>```java
> void beginZoomOut(@Nullable OnMapSceneCompletedListener listener)
>```

_See also:_ [OnMapSceneCompletedListener](Android/OnMapSceneCompletedListener-interface.md)

**iOS**

>```objectivec
> - (void)beginZoomOutWithCompletionCallback:(MSMapDidChangeSceneCallback)callback
>```

_See also:_ [MSMapDidChangeSceneCallback](iOS/MSMapDidChangeSceneCallback-interface.md)

### BeginZoomTo

Performs a zoom operation to the specified zoom level and invokes the provided callback when the zoom is complete.

**Android**

>```java
> void beginZoomTo(double zoomLevel, @Nullable OnMapSceneCompletedListener listener)
>```

_See also:_ [OnMapSceneCompletedListener](Android/OnMapSceneCompletedListener-interface.md)

**iOS**

>```objectivec
> - (void)beginZoomToLevel:(double)level, withCompletionCallback:(MSMapDidChangeSceneCallback)callback
>```

_See also:_ [MSMapDidChangeSceneCallback](iOS/MSMapDidChangeSceneCallback-interface.md)

### CanZoomIn
Returns true if calling zoomIn will affect camera.

**Android**

>```java
> boolean canZoomIn()
>```

**iOS**

>```objectivec
> - (BOOL)canZoomIn
>```

### CanZoomOut
Returns true if calling zoomOut will affect camera.

**Android**

>```java
> boolean canZoomOut()
>```

**iOS**

>```objectivec
> - (BOOL)canZoomOut
>```

### Pan

Perform a pan operation from the current location.

**Android**

>```java
> void pan(double horizontalDeviceIndependentPixels, double verticalDeviceIndependentPixels)
>```

**iOS**

>```objectivec
> - (void)panWithHorizontalPoints:(double)horizontalPoints verticalPoints:(double)verticalPoints
>```

### BeginPan

Perform a pan operation from the current location, and invokes the provided callback when the pan is complete.

**Android**

>```java
> void beginPan(double horizontalDeviceIndependentPixels, double verticalDeviceIndependentPixels, @Nullable OnMapSceneCompletedListener listener)
>```

_See also:_ [OnMapSceneCompletedListener](Android/OnMapSceneCompletedListener-interface.md)

**iOS**

>```objectivec
> -(void)beginPanWithHorizontalPoints:(double)horizontalPoints verticalPoints:(double)verticalPoints completionCallback:(MSMapDidChangeSceneCallback)callback
>```

_See also:_ [MSMapDidChangeSceneCallback](iOS/MSMapDidChangeSceneCallback-interface.md)

### PanTo

Perform a pan operation from the current location to the specified location.

**Android**

>```java
> void panTo(Geopoint location)
>```

**iOS**

>```objectivec
> - (void)panToLocation:(MSGeopoint *)location
>```

### BeginPanTo
Perform a pan operation from the current location to the specified location and invokes the provided callback when the pan is complete.

**Android**

>```java
> void beginPanTo(Geopoint location, @Nullable OnMapSceneCompletedListener listener)
>```

_See also:_ [OnMapSceneCompletedListener](Android/OnMapSceneCompletedListener-interface.md)

**iOS**

>```objectivec
>- (void)beginPanToLocation:(MSGeopoint *)location withCompletionCallback:(MSMapDidChangeSceneCallback)callback
>```

_See also:_ [MSMapDidChangeSceneCallback](iOS/MSMapDidChangeSceneCallback-interface.md)

## Events

### CameraChanged

Fired when the camera location changed.

**Android**

>```java
> void addOnMapCameraChangedListener(OnMapCameraChangedListener listener)
> void removeOnMapCameraChangedListener(OnMapCameraChangedListener listener)
>```
 
_See also:_ [OnMapCameraChangedListener](Android/OnMapCameraChangedListener-interface.md)

**iOS**

>```objectivec
> - (MSMapHandlerId)addCameraDidChangeHandler:(MSMapCameraDidChangeHandler)handler
> - (BOOL)removeCameraDidChangeHandler:(MSMapHandlerId)handlerId
>```

_See also:_ [MSMapCameraDidChangeHandler](iOS/MSMapCameraDidChangeHandler-interface.md)

### CameraChanging

Fired when the camera location is changing. This event is fired frequently and it is adviced to instead listen to cameraChanged and even then throttle the events and wait until the map is idle so as not to run code too frequently.

**Android**

>```java
> void addOnMapCameraChangingListener(OnMapCameraChangingListener listener)
> void removeOnMapCameraChangingListener(OnMapCameraChangingListener listener)
>```

_See also:_ [OnMapCameraChangingListener](Android/OnMapCameraChangingListener-interface.md)

**iOS**

>```objectivec
> - (MSMapHandlerId)addCameraWillChangeHandler:(MSMapCameraWillChangeHandler)handler
> - (BOOL)removeCameraWillChangeHandler:(MSMapHandlerId)handlerId
>```

_See also:_ [MSMapCameraWillChangeHandler](iOS/MSMapCameraWillChangeHandler-interface.md)

### DoubleTapped

Fired when the map is double tapped by the user.

**Android**

The `Position` value of this event's arguments is in screen pixels.

>```java
> void addOnMapDoubleTappedListener(OnMapDoubleTappedListener listener)
> void removeOnMapDoubleTappedListener(OnMapDoubleTappedListener listener)
>```

_See also:_ [OnMapDoubleTappedListener](Android/OnMapDoubleTappedListener-interface.md)

**iOS**

The `Position` value of this event's arguments is in device-independent points.

>```objectivec
> - (MSMapHandlerId)addUserDidDoubleTapHandler:(MSMapUserDidDoubleTapHandler)handler
> - (BOOL)removeUserDidDoubleTapHandler:(MSMapHandlerId)handlerId
>```

_See also:_ [MSMapUserDidDoubleTapHandler](iOS/MSMapUserDidDoubleTapHandler-interface.md)

### Holding

Fired when finger is held on the map by the user.

**Android**

The `Position` value of this event's arguments is in screen pixels.

>```java
> void addOnMapHoldingListener(OnMapHoldingListener listener)
> void removeOnMapHoldingListener(OnMapHoldingListener listener)
>```

_See also:_ [OnMapHoldingListener](Android/OnMapHoldingListener-interface.md)

**iOS**

The `Position` value of this event's arguments is in device-independent points.

>```objectivec
> - (MSMapHandlerId)addUserIsHoldingHandler:(MSMapUserIsHoldingHandler)handler
> - (BOOL)removeUserIsHoldingHandler:(MSMapHandlerId)handlerId
>```

_See also:_ [MSMapUserIsHoldingHandler](iOS/MSMapUserIsHoldingHandler-interface.md)

### LoadingStatusChanged

Fired when the loading status of the map has changed.

_See also:_ [MapLoadingStatus](MapLoadingStatus-enumeration.md)

**Android**

>```java
> void addOnMapLoadingStatusChangedListener(OnMapLoadingStatusChangedListener listener)
> void removeOnMapLoadingStatusChangedListener(OnMapLoadingStatusChangedListener listener)
>```

_See also:_ [MapLoadingStatusChangedListener](Android/OnMapLoadingStatusChangedListener-interface.md)

**iOS**

>```objectivec
> - (MSMapHandlerId)addLoadingStatusDidChangeHandler:(MSMapLoadingStatusDidChangeHandler)handler
> - (BOOL)removeLoadingStatusDidChangeHandler:(MSMapHandlerId)handlerId
>```

_See also:_ [MSMapLoadingStatusDidChangeHandler](iOS/MSMapLoadingStatusDidChangeHandler-interface.md)

### Tapped

Fired when the map is tapped by the user.

**Android**

The `Position` value of this event's arguments is in screen pixels.

>```java
> void addOnMapTappedListener(OnMapTappedListener listener)
> void removeOnMapTappedListener(OnMapTappedListener listener)
>```

_See also:_ [OnMapTappedListener](Android/OnMapTappedListener-interface.md)

**iOS**

The `Position` value of this event's arguments is in device-independent points.

>```objectivec
> - (MSMapHandlerId)addUserDidTapHandler:(MSMapUserDidTapHandler)handler
> - (BOOL)removeUserDidTapHandler:(MSMapHandlerId)handlerId
>```

_See also:_ [MSMapUserDidTapHandler](iOS/MSMapUserDidTapHandler-interface.md)


## Accessibility

MapView is accessible, supporting narrated scenarios as well as keyboard navigation.  
Currently, it exposes the following accessibility elements:

1. Map view itself, narrated as a description of the current view.
2. User map elements, potentially interactive.
3. Toolbar elements, interactive.

_See also:_ [MapElement - Accessibility](mapelement-class.md#accessibility)
