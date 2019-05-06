
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
> MapView(android.content.Context context)  
> MapView(android.content.Context context, android.util.AttributeSet attributes)
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
> boolean getBuildingsVisible()  
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
> boolean getBusinessLandmarksVisible()  
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

_See also:_ [Geolocation](Geolocation-class.md)

**Android**

>```java
> Geolocation getCenter()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) MSGeolocation *mapCenter
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
> @property (nonatomic) double heading
>```  

### Language

The language to be used when rendering locale-specific strings like country and city names. Example values: "en", "fr", "jp".

**Android**

>```java
> boolean setLanguage(String language)
>```

**iOS**

>```objectivec
> @property (nonatomic) NSString *language
>```  

### credentialsKey

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

Note that in Android, class `android.graphics.Point` is used since  `android.util.Size` is only available in API level 21.

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

The pitch in degrees where -90 is looking straight down and 0 is looking towards the horizon. Valid values are between -10 and -90.

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
> boolean setRegion(String region)
>```

**iOS**

>```objectivec
> @property (nonatomic) NSString *region
>```  

### TransitFeaturesVisible

Whether transit features (e.g., transit stops) are rendered on the map.

**Android**

>```java
> boolean getTransitFeaturesVisible()  
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

### UserLocationTrackingMode

Options for controlling how user location tracking is done.

_See also:_ [UserLocationTrackingMode](userlocationtrackingmode-enumeration.md)

**Android**

>```java
> UserLocationTrackingMode getUserLocationTrackingMode()  
> void setUserLocationTrackingMode(UserLocationTrackingMode mode)
>```

**iOS**

>```objectivec
> @property (nonatomic) MSMapUserLocationTrackingMode userLocationTrackingMode
>```

### UserLocationVisible

Whether the user's location is shown on the map.

**Android**

>```java
> boolean getUserLocationVisible()
> public LocationStatus setUserLocationVisible(boolean userLocationVisible, int permissionRequestCode)
>```

**iOS**

>```objectivec
> @property (nonatomic) IBInspectable BOOL userLocationVisible
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

> ```objectivec
> typedef void (^MSMapDidCaptureImageCallback)(UIImage * _Nullable)  
>  - (void)beginCaptureImageWithCompletionCallback:(MSMapDidCaptureImageCallback)callback
>```

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

### doesViewContainLocation

Whether the given location is visible in the MapView.

**Android**

>```java
> boolean isLocationInView(Geolocation location)
>```

**iOS**

>```objectivec
> - (BOOL)doesViewContainLocation:(MSGeolocation *)location
>```  

### locationFromOffset

Computes a location from point on the screen, with an option to select desired altitude reference system. Note that result value is not guaranteed (for example, if you try to get a location from a point that is in the sky).

**Android**

>```java
> Optional<Geolocation> locationFromOffset(Point offset)  
> Optional<Geolocation> locationFromOffset(Point offset, AltitudeReferenceSystem desiredAltitudeReferenceSystem)
>```

**iOS**

>```objectivec
> - (BOOL)tryToConvertOffset:(CGPoint)offset intoLocation:(MSGeolocation * _Nullable * _Nonnull)location  
> - (BOOL)tryToConvertOffset:(CGPoint)offset usingAltitudeReferenceSystem:(MSAltitudeReferenceSystem)altitudeReferenceSystem intoLocation:(MSGeolocation * _Nullable * _Nonnull)location
>```  

### offsetFromLocation

Returns the pixel offset of the location inside the MapView, if possible. Locations that are not in view will fail to return an offset.

**Android**

>```java
> Optional<Point> offsetFromLocation(Geolocation location)
>```

**iOS**

>```objectivec
> - (BOOL)tryToConvertLocation:(MSGeolocation *)location intoOffset:(CGPoint *)offset
>```  

### radiusFromViewCenter

Returns the radius of the current view if possible (horizontally, measured from the center point to the side of the screen). This method should be used in place of zoom level as is typically used on controls.

**Android**

>```java
> Optional<Double> getRadiusFromViewCenter()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) NSNumber *radiusFromViewCenter
>```

### resume (Android only)

Resumes after a previous call to suspend().

>```java
> void resume()
>```  
 
### rotate

Rotates the map by the specified number of degrees.

**Android**

>```java
> void rotate(double degrees)
>```

**iOS**

>```objectivec
> - (void)rotateDegrees:(double)degrees
>```  

### rotateTo

Performs a rotate operation to a particular point. rotateTo(0) will put the MapView with north up.

**Android**

>```java
> void rotateTo(double angleInDegrees)
>```

**iOS**

>```objectivec
> - (void)rotateTo:(double)degrees
>```  

### beginRotate

Performs a rotate operation and invokes the callback when complete.

**Android**

>```java
> void beginRotate(double degrees, SetSceneListener listener)
>```

**iOS**

>```objectivec
> - (void)beginRotateDegrees:(double)degrees withCompletionCallback:(MSMapDidChangeSceneCallback)callback
>```  

### beginRotateTo

Perform a rotate operation to a particular point and invokes the callback when complete. beginRotateTo(0) will put the MapView with north up.

**Android**

>```java
> void beginRotateTo(double angle, SetSceneListener listener)
>```

**iOS**

> ```objectivec
> - (void)beginRotateToDegrees:(double)degrees withCompletionCallback:(MSMapDidChangeSceneCallback)callback;
>```

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
> void beginSetScene(MapScene scene, MapAnimationKind kind, SetSceneListener listener)
>```

**iOS**

>```objectivec
> - (void)beginSetScene:(MSMapScene *)scene withAnimationKind:(MSMapAnimationKind)kind withCompletionCallback:(MSMapDidChangeSceneCallback)callback
>```  

### setSceneWithAnimation (Android only)

Sets the scene of the map with a specific animation. This allows customizing the duration of the animation.

_See also:_

* [MapScene](MapScene-class.md)
* [DefaultMapCameraAnimation](Android/DefaultMapCameraAnimation-class.md)

>```java
> void setSceneWithAnimation(MapScene scene, MapCameraAnimation animation)
>```  

### startContinuousPan

Performs an continuous pan operation.

**Android**

>```java
> void startContinuousPan(double horizontalPixelsPerSecond, double verticalPixelsPerSecond)
>```

**iOS**

> ```objectivec
> - (void)startContinuousPan:(double)horizontalPixelsPerSecond :(double)verticalPixelsPerSecond
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

### suspend(Android only)

Suspends the map, freeing up resources as necessary. This should be called if the app is being put in the background to allow the app to behave better while in the background.

>```java
> void suspend()
>```

### tilt

Performs a tilt operation.

**Android**

>```java
> `void tilt(double degrees)
>```

**iOS**

>```objectivec
> - (void)tiltDegrees:(double)degrees
>```  

### tiltTo (Android only)

Performs a tilt operation to a particular point. `tiltTo(0)` to have the map face nadir.

>```java
> void tiltTo(double angleInDegrees)
>```

### beginTilt

Performs a tilt operation and invokes the callback when complete.

**Android**

>```java
> `void beginTilt(double degrees, SetSceneListener listener)
>```

**iOS**

>```objectivec
> - (void)beginTiltDegrees:(double)degrees withCompletionCallback:(MSMapDidChangeSceneCallback)callback
>```  

### canTiltDown

Returns true if tilting down (away from nadir) is possible.

**Android**

>```java
> `boolean canTiltDown()
>```

**iOS**

>```objectivec
> - (BOOL)canTiltDown
>```  

### canTiltUp

Returns true if tilting up (towards nadir) is possible.

**Android**

>```java
> `boolean canTiltUp()
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
> `void zoomIn()
>```

**iOS**

>```objectivec
> - (void)zoomIn
>```  

#### zoomOut

Performs a zoom out operation, equivalent to clicking the zoom out button on the map.
Note that this method is also repeatable, such that if called multiple times in rapid order (e.g., the user repeatedly presses the zoom out button), the resulting operation is still smooth.

**Android**

>```java
> `void zoomOut()
>```

**iOS**

>```objectivec
> - (void)zoomOut
>```  

### beginZoomIn

Performs a zoom in operation, equivalent to double tapping on the map, and invokes the provided callback when the zoom is complete.

**Android**

>```java
> `void beginZoomIn(SetSceneListener listener)
>```

**iOS**

>```objectivec
> - (void)beginZoomInWithCompletionCallback:(MSMapDidChangeSceneCallback)callback
>```  

### beginZoomOut

Performs a zoom out operation, equivalent to double tapping on the map, and invokes the provided callback when the zoom is complete.

**Android**

>```java
> `void beginZoomOut(SetSceneListener listener)
>```

**iOS**

>```objectivec
> - (void)beginZoomOutWithCompletionCallback:(MSMapDidChangeSceneCallback)callback
>```  

### canZoomIn
Returns true if calling zoomIn will affect camera.

**Android**

>```java
> `boolean canZoomIn()
>```

**iOS**

>```objectivec
> - (BOOL)canZoomIn
>```

### canZoomOut
Returns true if calling zoomOut will affect camera.

**Android**

>```java
> `boolean canZoomOut()
>```

**iOS**

>```objectivec
> - (BOOL)canZoomOut
>```


### pan

Perform a pan operation from the current location.

**Android**

>```java
> `void pan(double horizontalPixels, double verticalPixels)
>```

**iOS**

>```objectivec
> - (void)pan:(double)horizontalPixels :(double)verticalPixels
>```

### beginPan

Perform a pan operation from the current location, and invokes the provided callback when the pan is complete.

**Android**

>```java
> `void beginPan(double horizontalPixels, double verticalPixels, SetSceneListener listener)
>```

**iOS**

>```objectivec
> -(void)beginPanWithCompletionCallback:(double)horizontalPixels :(double)verticalPixels :(MSMapDidChangeSceneCallback)callback
>```

### panTo

Perform a pan operation from the current location to the specified location.

**Android**

>```java
> `void panTo(Location location)
>```

**iOS**

>```objectivec
> - (void)panTo:(MSMapLocation *)location
>```

### beginPanTo
Perform a pan operation from the current location to the specified location and invokes the provided callback when the pan is complete.

**Android**

>```java
> ``void beginPanTo(Location location, SetSceneListener listener)
>```

**iOS**

>```objectivec
>- (void)beginPanToWithCompletionCallback:(MSMapLocation *)location :(MSMapDidChangeSceneCallback)callback
>```

## Events

### CameraChanged

Fired when the camera location changed.

**Android**

>```java
> void addOnCameraChangedListener(OnCameraChangedListener listener) 
> void removeOnCameraChangedListener(OnCameraChangedListener listener)
>```
 
_See also:_ [OnCameraChangedListener](Android/OnCameraChangedListener-interface.md)

**iOS**

>```objectivec
> typedef BOOL (^MSMapCameraDidChangeHandler)(MSMapCameraChangeCause)  
> - (MSMapHandlerId)addCameraDidChangeHandler:(MSMapCameraDidChangeHandler)handler  
> - (BOOL)removeCameraDidChangeHandler:(MSMapHandlerId)handlerId
>```  

### CameraChanging

Fired when the camera location is changing. This event is fired frequently and it is adviced to instead listen to cameraChanged and even then throttle the events and wait until the map is idle so as not to run code too frequently.

**Android**

>```java
> void addOnCameraChangingListener(OnCameraChangingListener listener)  
> void removeOnCameraChangingListener(OnCameraChangingListener listener)
>```

_See also:_ [OnCameraChangingListener](Android/OnCameraChangingListener-interface.md)

**iOS**

>```objectivec
> typedef BOOL (^MSMapCameraWillChangeHandler)(MSMapCameraChangeCause, BOOL)  
> - (MSMapHandlerId)addCameraWillChangeHandler:(MSMapCameraWillChangeHandler)handler  
> - (BOOL)removeCameraWillChangeHandler:(MSMapHandlerId)handlerId
>```  

### MapLoadingStatusChanged

Fired when the render states of the map has changed.

_See also:_ [MapLoadingStatus](MapLoadingStatus.md)

**Android**

>```java
> void addOnMapLoadingStatusChangedListener(OnMapLoadingStatusChangedListener listener)  
> void removeOnMapLoadingStatusChangedListener(OnMapLoadingStatusChangedListener listener)
>```

_See also:_ [MapLoadingStatusChangedListener](Android/OnMapLoadingStatusChangedListener-interface.md)

**iOS**

>```objectivec 
> typedef BOOL (^MSMapLoadingStatusDidChangeHandler)(MSMapLoadingStatus)
> - (MSMapHandlerId)addLoadingStatusDidChangeHandler:(MSMapLoadingStatusDidChangeHandler)handler 
> - (BOOL)removeLoadingStatusDidChangeHandler:(MSMapHandlerId)handlerId
>```  

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
> typedef BOOL (^MSMapUserDidDoubleTapHandler)(CGPoint) 
> - (MSMapHandlerId)addUserDidDoubleTapHandler:(MSMapUserDidDoubleTapHandler)handler
> - (BOOL)removeUserDidDoubleTapHandler:(MSMapHandlerId)handlerId
>```  

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
> typedef BOOL (^MSMapUserIsHoldingHandler)(CGPoint)
> - (MSMapHandlerId)addUserIsHoldingHandler:(MSMapUserIsHoldingHandler)handler
> - (BOOL)removeUserIsHoldingHandler:(MSMapHandlerId)handlerId
>```  

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
> typedef BOOL (^MSMapUserDidTapHandler)(CGPoint)
> - (MSMapHandlerId)addUserDidTapHandler:(MSMapUserDidTapHandler)handler
> - (BOOL)removeUserDidTapHandler:(MSMapHandlerId)handlerId
>```  
