---
title: MapRouteSegment Class | Microsoft Docs
description: Describes the MapRouteSegment class for Android and iOS and provides the class's properties and additional references.
ms.author: pablocan
---

# MapRouteSegment Class

[!INCLUDE [bing-maps-sdk-for-android-iOS-retirement](../../includes/bing-maps-sdk-for-android-iOS-retirement.md)]

Represents a road segment displayed on the map.

**Android**

>```java
> class MapRouteSegment
>```

**iOS**

>```objectivec
> @interface MSMapRouteSegment : NSObject
>```

## Properties

### MapStyleSheetEntry

Gets or sets the name of an entry in the map's style sheet that you'd like to apply to this MapRouteSegment. Set this property to a string or to any of the property values available in the [MapStyleSheetEntries](/uwp/api/windows.ui.xaml.controls.maps.mapstylesheetentries) class.

**Android**

>```java
> String getMapStyleSheetEntry()
> void setMapStyleSheetEntry(@Nullable String mapStyleSheetEntry)
>```

**iOS**

>```objectivec
> @property (nonatomic, nullable) NSString *mapStyleSheetEntry;
>```

_See also:_ 
* [MapStyleSheet](MapStyleSheet-class.md)
* [Map Style Sheet Reference](/bingmaps/styling/map-style-sheet-entries)  

### MapStyleSheetEntryState

Gets or sets the name of the state of this MapRouteSegment. If the style sheet defines a style for that state, that style is applied to this element. Values defined in the style sheet for the state override values defined in the MapStyleSheetEntry.

**Android**

>```java
> String getMapStyleSheetEntryState()
> void setMapStyleSheetEntryState(@Nullable String mapStyleSheetEntryState)
>```

**iOS**

>```objectivec
> @property (nonatomic, nullable) id mapStyleSheetEntryState;
>```

_See also:_ 
* [MapStyleSheet](MapStyleSheet-class.md)
* [Map Style Sheet Reference](/bingmaps/styling/map-style-sheet-entries)  

### Path

The path making up this MapRouteSegment.

**Android**

>```java
> @Nullable Geopath getPath()
> void setPath(Geopath path)
>```

**iOS**

>```objectivec
> @property (nonatomic) MSGeopath *path  
>```

_See also:_ [Geopath](Geopath-class.md)

### TrafficCongestion

**Android**

Sets or gets travel mode which is used to set the name of the state of this MapRouteSegment. If MapStyleSheetEntryState is also set, this value gets ignored.

>```java
> MapRouteLineTrafficCongestion getTrafficCongestion()
> void setTrafficCongestion(MapRouteLineTrafficCongestion trafficCongestion)
>```

**iOS**
>```objectivec
> @property(nonatomic) MSMapRouteLineTrafficCongestion trafficCongestion  
>```

### TravelMode

**Android**

Sets or gets travel mode which is used to set the name of the entry of this MapRouteSegment. If MapStyleSheetEntry is also set, this value gets ignored.

>```java
> MapRouteLineTravelMode getTravelMode()
> void setTravelMode(MapRouteLineTravelMode travelMode)
>```

**iOS**
>```objectivec
> @property(nonatomic) MSMapRouteLineTravelMode travelMode  
>```

## See Also

* [MapRouteLine](MapRouteLine-class.md)
