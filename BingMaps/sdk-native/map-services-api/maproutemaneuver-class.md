---
title: MapRouteManeuver Class | Microsoft Docs
description: Describes the mapRouteManeuver class for Android and iOS and provides the class's properties and additional references.
ms.author: kezhang
---

# MapRouteManeuver Class

Contains actions to be taken along the path of a route leg.

## Properties

### EndHeading

Indicates the heading at the end of the maneuver in degrees, where 0 or 360 = North, 90 = East, 180 = South, and 270 = West.

**Android**

>```java
>double getEndHeading()
>```

**iOS**

>```objectivec
>@property(nonatomic) double endHeading;
>```

### ExitNumber

The exit number of route maneuver.

**Android**

>```java
>String getExitNumber()
>```

**iOS**

>```objectivec
>@property(nonatomic) NSString* exitNumber
>```

### InstructionText

The instruction text associated with the maneuver.

**Android**

>```java
>String getInstructionText()
>```

**iOS**

>```objectivec
>@property(nonatomic) NSString* instructionText
>```

### Kind  

The type of the maneuver.

_See also:_ [MapRouteManeuverKind](maproutemaneuverkind-enumeration.md)

**Android**

>```java
>MapRouteManeuverKind getMapRouteManeuverKind()
>```

**iOS**

>```objectivec
>@property(nonatomic) MSMapRouteManeuverKind mapRouteManeuverKind
>```

### LengthInMetersFromPreviousManeuver 

The distance in meters from the end of the previous maneuver.

**Android**

>```java
>double getDistanceInMetersFromPreviousManeuver()
>```

**iOS**

>```objectivec
>@property(nonatomic) double distanceInMetersFromPreviousManeuver
>```

### LengthInMetersToNextManeuver 

The distance in meters to the start of the next maneuver.

**Android**

>```java
>double getDistanceInMetersToNextManeuver()
>```

**iOS**

>```objectivec
>@property(nonatomic) double distanceInMetersToNextManeuver
>```

### ManeuverNotices  

The additional information associated with the maneuver.

_See also:_ [MapManeuverNotices](mapmaneuvernotices-enumeration.md)

**Android**

>```java
>@MapManeuverNotices int getManeuverNotices()
>```

**iOS**

>```objectivec
>@property(nonatomic) MSMapManeuverNotices maneuverNotices
>```

### StartHeading  

A value that indicates the heading at the start of the maneuver in degrees, where 0 or 360 = North, 90 = East, 180 = South, and 270 = West.

**Android**

>```java
>double getStartHeading()
>```

**iOS**

>```objectivec
>@property(nonatomic) double startHeading
>```

### StartingPoint  

The location where the maneuver starts.

**Android**

>```java
>Geopoint getStartingPoint()
>```

**iOS**

>```objectivec
>@property(nonatomic) MSGeopoint* startingPoint
>```


### CurrentRoadName  

The current road name specified in InstructionText, if available.

**Android**

>```java
>String getCurrentRoadName()
>```

**iOS**

>```objectivec
>@property(nonatomic) NSString* currentRoadName
>```

### TargetRoadName  

The target road name specified in InstructionText, if available.

**Android**

>```java
>String getTargetRoadName()
>```

**iOS**

>```objectivec
>@property(nonatomic) NSString* targetRoadName
>```

### Warnings  

A list of potential issues along a route leg.

_See also:_ [ManeuverWarning](maneuverwarning-class.md)

**Android**

>```java
>List<ManeuverWarning> getWarnings()
>```

**iOS**

>```objectivec
>@property(nonatomic) NSArray<MSMapManeuverWarning*>* warnings
>```

## See Also

* [MapRouteLeg](maprouteleg-class.md)