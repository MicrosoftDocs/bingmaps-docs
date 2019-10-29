---
title: "MapView Class | Microsoft Docs"
author: "bmnxplat"
---

# MapView Class

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

Whether 3D buildings are rendered on the map.

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

Whether business landmarks (e.g., restaurants, hotels) are rendered on the map.

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

Gets the center of the current view.  Keep in mind that in oblique views (where some horizon is shown),
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

### Heading

The heading of the view in degrees where 0 is north, 90 is east, 180 is south, and 270 is west. Valid values are between 0 and 360.

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

The language to be used when rendering locale-specific strings like country and city names. Example values: "en", "fr", "jp".

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

The license key authorizing use of the map. Get credentials at [www.bingmapsportal.com](http://www.bingmapsportal.com/).

**Android**

>```java
> void setCredentialsKey(String credentialsKey)
>```

**iOS**

>```objectivec
> @property (nonatomic) IBInspectable NSString *credentialsKey
>```

### Layers
Gets developer-added layers of content for the map.  
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

Whether to render maps using raster tiles or vector data. Raster tiles will generally give a faster framerate at the expense
of less readable text.

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

The projection used to render the map.

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

Size of rendered map in pixels.

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

### Pitch

The pitch of the camera in degrees, where 0 is looking straight down (minimum) and 90 is looking towards the horizon (maximum). Values outside of this range will throw an exception.
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

The region of the world to display a map for. Different regions of the world have different views of the world including borders and contested regions. Example values: "us", "ca", "fr".

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

Whether transit features (e.g., transit stops) are rendered on the map.

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

Returns a container class that lets a developer access configuration controls for the map user
interface.

_See also:_ [MapUserInterfaceOptions](MapUserInterfaceOptions-class.md)

**Android**

>```java
> MapUserInterfaceOptions getUserInterfaceOptions()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) MSMapUserInterfaceOptions *userInterfaceOptions
>```

### ZoomLevel

Gets the zoom level of the current view.

**Android**

>```java
> double getZoomLevel()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) double zoomLevel
>```

## Life cycle methods (Android only)

You must override life cycle methods in parent fragment/activity and call respective MapView methods below from the callback.

_See also:_ https://developer.android.com/guide/components/activities/activity-lifecycle

### onCreate

Map handler for created state.

>```java
> void onCreate(Bundle savedInstanceState)
>```

### onStart

Map handler for started state.

>```java
> void onStart()
>```

### onResume

Map handler for resumed state. Start the map, creating the rendering resources as necessary.

>```java
> void onResume()
>```

### onPause

Map handler for paused state. Suspends the map, freeing up resources as necessary.

>```java
> void onPause()
>```

### onSaveInstanceState

Map handler for save instance state.

>```java
> void onSaveInstanceState(Bundle outState)
>```

### onStop

Map handler for stopped state.

>```java
> void onStop()
>```

### onDestroy

Map handler for destroyed state. Dispose the map, releasing all resources.

>```java
> void onDestroy()
>```

### onLowMemory

Map handler for low memory event.

>```java
> void onLowMemory()
>```

## Methods

### setBackgroundColor

The background color of the map that is rendered if there is nothing else to render. As soon as map tiles are available to render the background color is controlled by the active MapStyleSheet instead.

**Android**

>```java
> void setBackgroundColor(int color)
>```

**iOS**

>```objectivec
> - (void)setMapBackgroundColor:(UIColor *)color
>```


### cancelAnimation

Cancels the active animation, if running. If an animation is not running, this method does nothing.

**Android**

>```java
> void cancelAnimation()
>```

**iOS**

>```objectivec
> - (void)cancelAnimation
>```

### captureImage

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

### findMapElementsAtOffset

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

### isLocationInView

Whether the given location is visible in the MapView.

**Android**

>```java
> boolean isLocationInView(Geopoint location)
>```

**iOS**

>```objectivec
> - (BOOL)doesViewContainLocation:(MSGeopoint *)location
>```

### locationFromOffset

Converts a point on the map (pixel offset) to a geographic location, with an option to select a desired altitude reference system. Note that the return value can be null, for instance, a point in the sky will fail to return a location.

**Android**

>```java
> Geopoint getLocationFromOffset(Point offset)  
> Geopoint getLocationFromOffset(Point offset, AltitudeReferenceSystem desiredAltitudeReferenceSystem)
>```

**iOS**

>```objectivec
> - (BOOL)tryToConvertOffset:(CGPoint)offset 
>               intoLocation:(MSGeopoint * _Nullable * _Nonnull)location  
> - (BOOL)tryToConvertOffset:(CGPoint)offset 
>     usingAltitudeReference:(MSAltitudeReferenceSystem)altitudeReferenceSystem 
>               intoLocation:(MSGeopoint * _Nullable * _Nonnull)location
>```

### offsetFromLocation

Converts a geographic location to a point on the map (pixel offset). Note that the return value can be null, for instance, locations that are not in view will fail to return an offset.

**Android**

>```java
> Point getOffsetFromLocation(Geopoint location)
>```

**iOS**

>```objectivec
> - (BOOL)tryToConvertLocation:(MSGeopoint *)location intoOffset:(CGPoint *)offset
>```

### rotate

Rotates the map by the specified number of degrees.

**Android**

>```java
> void rotate(double degrees)
>```

**iOS**

>```objectivec
> - (void)rotateWithDegrees:(CLLocationDirection)degrees
>```

### rotateTo

Performs a rotate operation to a particular point. rotateTo(0) will put the MapView with north up.

**Android**

>```java
> void rotateTo(double angleInDegrees)
>```

**iOS**

>```objectivec
> - (void)rotateToDegrees:(CLLocationDirection)degrees
>```

### beginRotate

Performs a rotate operation and invokes the callback when complete.

**Android**

>```java
> void beginRotate(double degrees, OnMapSceneCompletedListener listener)
>```

_See also:_ [OnMapSceneCompletedListener](Android/OnMapSceneCompletedListener-interface.md)

**iOS**

>```objectivec
> - (void)beginRotateWithDegrees:(CLLocationDirection)degrees completionCallback:(MSMapDidChangeSceneCallback)callback
>```

_See also:_ [MSMapDidChangeSceneCallback](iOS/MSMapDidChangeSceneCallback-interface.md)

### beginRotateTo

Perform a rotate operation to a particular point and invokes the callback when complete. beginRotateTo(0) will put the MapView with north up.

**Android**

>```java
> void beginRotateTo(double angle, OnMapSceneCompletedListener listener)
>```

_See also:_ [OnMapSceneCompletedListener](Android/OnMapSceneCompletedListener-interface.md)

**iOS**

>```objectivec
> - (void)beginRotateToDegrees:(CLLocationDirection)degrees withCompletionCallback:(MSMapDidChangeSceneCallback)callback;
>```

_See also:_ [MSMapDidChangeSceneCallback](iOS/MSMapDidChangeSceneCallback-interface.md)

### setMapStyleSheet

Sets the style of the map, such as Road, Aerial, or other styles.

_See also:_ [MapStyleSheet](MapStyleSheet-class.md)

**Android**

>```java
> void setMapStyleSheet(MapStyleSheet mapStyleSheet)
>```

**iOS**

>```objectivec
> - (void)setStyleSheet:(MSMapStyleSheet*)mapStyleSheet;
>```

### setScene

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

### beginSetScene

Sets the scene of the map based on the animation provided. When the scene has finished changing, the provided callback is invoked.

_See also:_
* [MapScene](MapScene-class.md)
* [MapAnimationKind](MapAnimationKind-enumeration.md)

**Android**

>```java
> void beginSetScene(MapScene scene, MapAnimationKind kind, OnMapSceneCompletedListener listener)
>```

_See also:_ [OnMapSceneCompletedListener](Android/OnMapSceneCompletedListener-interface.md)

**iOS**

>```objectivec
> - (void)beginSetScene:(MSMapScene *)scene withAnimationKind:(MSMapAnimationKind)kind withCompletionCallback:(MSMapDidChangeSceneCallback)callback
>```

_See also:_ [MSMapDidChangeSceneCallback](iOS/MSMapDidChangeSceneCallback-interface.md)

### startContinuousPan

Performs an continuous pan operation.

**Android**

>```java
> void startContinuousPan(double horizontalPixelsPerSecond, double verticalPixelsPerSecond)
>```

**iOS**

>```objectivec
> - (void)startContinuousPanWithHorizontalPixelsPerSecond:(double)horizontalPixelsPerSecond verticalPixelsPerSecond:(double)verticalPixelsPerSecond
>```

### startContinuousRotate

Starts a continuous rotate operation.

**Android**

>```java
> void startContinuousRotate(double rateInDegreesPerSecond)
>```

**iOS**

>```objectivec
> - (void)startContinuousRotateWithDegreesPerSecond:(double)degreesPerSecond
>```

### startContinuousTilt

Performs a continuous tilt operation. Call `stopContinuousTilt` to stop an in-progress tilt.

**Android**

>```java
> void startContinuousTilt(double rateInDegreesPerSecond)
>```

**iOS**

>```objectivec
> - (void)startContinuousTiltWithDegreesPerSecond:(double)degreesPerSecond
>```

### startContinuousZoom

Performs an ongoing zoom operation.

**Android**

>```java
> void startContinuousZoom(double rateOfChangePerSecond)
>```

**iOS**

>```objectivec
> - (void)startContinuousZoomWithZoomLevelsPerSecond:(double)zoomLevelsPerSecond
>```

### stopContinuousPan

Stops a continuous pan operation.

**Android**

>```java
> void stopContinuousPan()
>```

**iOS**

>```objectivec
> - (void)stopContinuousPan
>```

### stopContinuousRotate

Stops a previously started rotate operation

**Android**

>```java
> void stopContinuousRotate()
>```

**iOS**

>```objectivec
> - (void)stopContinuousRotate
>```

### stopContinuousTilt

Stops an in-progress tilt operation.

**Android**

>```java
> void stopContinuousTilt()
>```

**iOS**

>```objectivec
> - (void)stopContinuousTilt
>```

### stopContinuousZoom

Stops a continuous zoom operation.

**Android**

>```java
> void stopContinuousZoom()
>```

**iOS**

>```objectivec
> - (void)stopContinuousZoom
>```

### tilt

Performs an operation to tilt the map's camera from its current position. Valid values are between -90 and 90. Invalid values will be clamped.

**Android**

>```java
> void tilt(double degrees)
>```

**iOS**

>```objectivec
> - (void)tiltWithDegrees:(double)degrees
>```

### beginTilt

Performs an operation to tilt the map's camera from its current position and invokes the callback when complete. Valid values are between -90 and 90. Invalid values will be clamped.

**Android**

>```java
> void beginTilt(double degrees, OnMapSceneCompletedListener listener)
>```

_See also:_ [OnMapSceneCompletedListener](Android/OnMapSceneCompletedListener-interface.md)

**iOS**

>```objectivec
> - (void)beginTiltWithDegrees:(double)degrees completionCallback:(MSMapDidChangeSceneCallback)callback
>```

_See also:_ [MSMapDidChangeSceneCallback](iOS/MSMapDidChangeSceneCallback-interface.md)

### tiltTo

Performs a tilt operation to a particular point. `tiltTo(0)` to have the map face nadir. Valid values are between 0 and 90. Invalid values will be clamped.


**Android**

>```java
> void tiltTo(double degrees)
>```

**iOS**

>```objectivec
> - (void)tiltToDegrees:(double)degrees
>```

### beginTiltTo

Performs a tiltTo operation and invokes the callback when complete. Valid values are between 0 and 90. Invalid values will be clamped.

**Android**

>```java
> void beginTiltTo(double degrees, OnMapSceneCompletedListener listener)
>```

_See also:_ [OnMapSceneCompletedListener](Android/OnMapSceneCompletedListener-interface.md)

**iOS**

>```objectivec
> - (void)beginTiltToDegrees:(double)degrees withCompletionCallback:(MSMapDidChangeSceneCallback)callback
>```

_See also:_ [MSMapDidChangeSceneCallback](iOS/MSMapDidChangeSceneCallback-interface.md)

### canTiltDown

Returns true if tilting down (away from nadir) is possible.

**Android**

>```java
> boolean canTiltDown()
>```

**iOS**

>```objectivec
> - (BOOL)canTiltDown
>```

### canTiltUp

Returns true if tilting up (towards nadir) is possible.

**Android**

>```java
> boolean canTiltUp()
>```

**iOS**

>```objectivec
> - (BOOL)canTiltUp
>```

### zoomIn

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

### zoomOut

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

### beginZoomIn

Performs a zoom in operation, equivalent to double tapping on the map, and invokes the provided callback when the zoom is complete.

**Android**

>```java
> void beginZoomIn(OnMapSceneCompletedListener listener)
>```

_See also:_ [OnMapSceneCompletedListener](Android/OnMapSceneCompletedListener-interface.md)

**iOS**

>```objectivec
> - (void)beginZoomInWithCompletionCallback:(MSMapDidChangeSceneCallback)callback
>```

_See also:_ [MSMapDidChangeSceneCallback](iOS/MSMapDidChangeSceneCallback-interface.md)

### beginZoomOut

Performs a zoom out operation, equivalent to double tapping on the map, and invokes the provided callback when the zoom is complete.

**Android**

>```java
> void beginZoomOut(OnMapSceneCompletedListener listener)
>```

_See also:_ [OnMapSceneCompletedListener](Android/OnMapSceneCompletedListener-interface.md)

**iOS**

>```objectivec
> - (void)beginZoomOutWithCompletionCallback:(MSMapDidChangeSceneCallback)callback
>```

_See also:_ [MSMapDidChangeSceneCallback](iOS/MSMapDidChangeSceneCallback-interface.md)

### canZoomIn
Returns true if calling zoomIn will affect camera.

**Android**

>```java
> boolean canZoomIn()
>```

**iOS**

>```objectivec
> - (BOOL)canZoomIn
>```

### canZoomOut
Returns true if calling zoomOut will affect camera.

**Android**

>```java
> boolean canZoomOut()
>```

**iOS**

>```objectivec
> - (BOOL)canZoomOut
>```


### pan

Perform a pan operation from the current location.

**Android**

>```java
> void pan(double horizontalPixels, double verticalPixels)
>```

**iOS**

>```objectivec
> - (void)panWithHorizontalPixels:(double)horizontalPixels verticalPixels:(double)verticalPixels
>```

### beginPan

Perform a pan operation from the current location, and invokes the provided callback when the pan is complete.

**Android**

>```java
> void beginPan(double horizontalPixels, double verticalPixels, OnMapSceneCompletedListener listener)
>```

_See also:_ [OnMapSceneCompletedListener](Android/OnMapSceneCompletedListener-interface.md)

**iOS**

>```objectivec
> -(void)beginPanWithHorizontalPixels:(double)horizontalPixels verticalPixels:(double)verticalPixels completionCallback:(MSMapDidChangeSceneCallback)callback
>```

_See also:_ [MSMapDidChangeSceneCallback](iOS/MSMapDidChangeSceneCallback-interface.md)

### panTo

Perform a pan operation from the current location to the specified location.

**Android**

>```java
> void panTo(Geopoint location)
>```

**iOS**

>```objectivec
> - (void)panToLocation:(MSGeopoint *)location
>```

### beginPanTo
Perform a pan operation from the current location to the specified location and invokes the provided callback when the pan is complete.

**Android**

>```java
> void beginPanTo(Geopoint location, OnMapSceneCompletedListener listener)
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

### MapLoadingStatusChanged

Fired when the render states of the map has changed.

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

### DoubleTapped

Fired when the map is double tapped by the user.

**Android**

>```java
> void addOnMapDoubleTappedListener(OnMapDoubleTappedListener listener)
> void removeOnMapDoubleTappedListener(OnMapDoubleTappedListener listener)
>```

_See also:_ [OnMapDoubleTappedListener](Android/OnMapDoubleTappedListener-interface.md)

**iOS**

>```objectivec
> - (MSMapHandlerId)addUserDidDoubleTapHandler:(MSMapUserDidDoubleTapHandler)handler
> - (BOOL)removeUserDidDoubleTapHandler:(MSMapHandlerId)handlerId
>```

_See also:_ [MSMapUserDidDoubleTapHandler](iOS/MSMapUserDidDoubleTapHandler-interface.md)

### Holding

Fired when finger is held on the map by the user.

**Android**

>```java
> void addOnMapHoldingListener(OnMapHoldingListener listener)
> void removeOnMapHoldingListener(OnMapHoldingListener listener)
>```

_See also:_ [OnMapHoldingListener](Android/OnMapHoldingListener-interface.md)

**iOS**

>```objectivec
> - (MSMapHandlerId)addUserIsHoldingHandler:(MSMapUserIsHoldingHandler)handler
> - (BOOL)removeUserIsHoldingHandler:(MSMapHandlerId)handlerId
>```

_See also:_ [MSMapUserIsHoldingHandler](iOS/MSMapUserIsHoldingHandler-interface.md)

### Tapped

Fired when the map is tapped by the user.

**Android**

>```java
> void addOnMapTappedListener(OnMapTappedListener listener)
> void removeOnMapTappedListener(OnMapTappedListener listener)
>```

_See also:_ [OnMapTappedListener](Android/OnMapTappedListener-interface.md)

**iOS**

>```objectivec
> - (MSMapHandlerId)addUserDidTapHandler:(MSMapUserDidTapHandler)handler
> - (BOOL)removeUserDidTapHandler:(MSMapHandlerId)handlerId
>```

_See also:_ [MSMapUserDidTapHandler](iOS/MSMapUserDidTapHandler-interface.md)
