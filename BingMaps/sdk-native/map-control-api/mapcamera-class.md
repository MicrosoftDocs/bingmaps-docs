---
title: "MapCamera Class | Microsoft Docs"
author: "bmnxplat"
---

# MapCamera Class

Describes a camera in a MapView.

**Android**

>```java
> public class MapCamera
>```

**iOS**

>```objectivec
> @interface MSMapCamera : NSObject

## Constructors

If not specified, Geopoint defaults to (latitude: 0, longitude: 0), Heading to 0, Pitch to -90, and VerticalFieldOfView defaults to not set (null).

**Android**

>```java
> MapCamera()
> MapCamera(Geopoint cameraLocation) 
> MapCamera(Geopoint cameraLocation, double heading, double pitch)
> MapCamera(Geopoint cameraLocation, double heading, double pitch, double verticalFieldOfView)
>```

**iOS**

>```objectivec + (instancetype)camera
> + (instancetype)cameraWithLocation:(MSGeopoint *)location
> + (instancetype)cameraWithLocation:(MSGeopoint *)location heading:(CLLocationDirection)heading pitch:(double)pitch
> + (instancetype)cameraWithLocation:(MSGeopoint *)location heading:(CLLocationDirection)heading pitch:(double)pitch verticalFieldOfView:(double)fov
>```

## Properties

### Heading

The heading in degrees. 0 corresponds to north, 90 to east, 180 to south, and 270 to west. Values less than 0 or greater than 360 are wrapped.

**Android**

>```java
> double getHeading()
> void setHeading(double heading)
>```

**iOS**

>```objectivec
> @property (nonatomic) CLLocationDirection heading
>```


### Location

The location of the MapCamera.  
_See also:_ [MSGeopoint](Geopoint-class.md)

**Android**

>```java
> Geopoint getLocation()
> void setLocation(Geopoint location)
>```

**iOS**

>```objectivec
> @property (nonatomic) MSGeopoint *location
>```

### Pitch

The pitch of the map in degrees, where 0 is looking straight down (minimum) and 90 is looking towards the horizon (maximum). Values outside of this range will throw an exception.
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
