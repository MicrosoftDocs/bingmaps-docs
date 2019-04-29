
# MapCamera class

Describes a camera in a MapView.

**Android**

>```java
> public class MapCamera
>```

**iOS**

>```objectivec
> @interface MSMapCamera : NSObject

## Constructors

If not specified, Geolocation defaults to (latitude: 0, longitude: 0), Heading to 0, Pitch to -90, and VerticalFieldOfView defaults to not set (null).

**Android**

>```java
> MapCamera()
> MapCamera(Geolocation cameraLocation) 
> MapCamera(Geolocation cameraLocation, double heading, double pitch)
> MapCamera(Geolocation cameraLocation, double heading, double pitch, double verticalFieldOfView)
>```

**iOS**

>```objectivec + (instancetype)camera
> + (instancetype)cameraWithLocation:(MSGeolocation *)location
> + (instancetype)cameraWithLocation:(MSGeolocation *)location heading:(double)heading pitch:(double)pitch
> + (instancetype)cameraWithLocation:(MSGeolocation *)location heading:(double)heading pitch:(double)pitch verticalFieldOfView:(double)fov
>```  

## Properties

### Heading

The heading in degrees. 0 == north, 90 == east, 180 == south, 270 == west. Values less than 0 or greater than 360 are wrapped.

**Android**

>```java
> double getHeading()
> void setHeading(double heading)
>```

**iOS**

>```objectivec
> @property (nonatomic) double heading
>```  


### Location

The location of the MapCamera.  
_See also:_ [MSGeolocation](Geolocation.md)

**Android**

>```java
> Geolocation getLocation() 
> void setLocation(Geolocation location)
>```

**iOS**

>```objectivec
> @property (nonatomic) MSGeolocation *location
>```  

### Pitch

The pitch of the camera in degrees where -90 is looking straight down, 0 is looking at the tangent of the earth, and 90 is looking straight up.

**Android**

>````java
> double getPitch() 
> void setPitch(double pitch)
>```  

**iOS**

>```objectivec
> @property (nonatomic) double pitch
>```  

### VerticalFieldOfView

The vertical field of view in degrees. It may be null for MapCameras created without a vertical field of view.

**Android**

>```java
> Double getVerticalFieldOfView() 
> void setVerticalFieldOfView(double verticalFieldOfView)
>```

**iOS**

>```objectivec
> @property (nonatomic, nullable) NSNumber *verticalFieldOfView
>```  
