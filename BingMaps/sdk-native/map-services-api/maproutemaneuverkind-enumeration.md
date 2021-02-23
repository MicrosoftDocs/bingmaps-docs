---
title: "MapRouteManeuverKind Enumeration | Microsoft Docs"
ms.author: "kezhang"
---

# MapRouteManeuverKind Enumeration

Describes the various types of maneuvers that can occur in a route. This enumeration provides values for the Kind property of a MapRouteManeuver instance.

_See also:_ [MapRouteManeuver](maproutemaneuver-class.md)

**Android**

>```java
>public enum MapRouteManeuverKind {
>  UNDEFINED(0),
>  START(1),
>  STOPOVER(2),
>  STOPOVER_RESUME(3),
>  END(4),
>  GO_STRAIGHT(5),
>  UTURN_LEFT(6),
>  UTURN_RIGHT(7),
>  TURN_KEEP_LEFT(8),
>  TURN_KEEP_RIGHT(9),
>  TURN_LIGHT_LEFT(10),
>  TURN_LIGHT_RIGHT(11),
>  TURN_LEFT(12),
>  TURN_RIGHT(13),
>  TURN_HARD_LEFT(14),
>  TURN_HARD_RIGHT(15),
>  FREEWAY_ENTER_LEFT(16),
>  FREEWAY_ENTER_RIGHT(17),
>  FREEWAY_LEAVE_LEFT(18),
>  FREEWAY_LEAVE_RIGHT(19),
>  FREEWAY_CONTINUE_LEFT(20),
>  FREEWAY_CONTINUE_RIGHT(21),
>  TRAFFIC_CIRCLE_LEFT(22),
>  TRAFFIC_CIRCLE_RIGHT(23),
>  TAKE_FERRY(24),
>  TAKE_TRANSIT(25),
>  TRANSFER(26),
>  WAIT(27),
>  WALK(28),
>  INVALID(29);
>}
>```

**iOS**

>```objectivec
>typedef NS_ENUM(NSInteger, MSMapRouteManeuverKind) {
>    MSMapRouteManeuverKindUndefined = 0,
>    MSMapRouteManeuverKindStart,
>    MSMapRouteManeuverKindStopover,
>    MSMapRouteManeuverKindStopoverResume,
>    MSMapRouteManeuverKindEnd,
>    MSMapRouteManeuverKindGoStraight,
>    MSMapRouteManeuverKindUturnLeft,
>    MSMapRouteManeuverKindUturnRight,
>    MSMapRouteManeuverKindTurnKeepLeft,
>    MSMapRouteManeuverKindTurnKeepRight,
>    MSMapRouteManeuverKindTurnLightLeft,
>    MSMapRouteManeuverKindTurnLightRight,
>    MSMapRouteManeuverKindTurnLeft,
>    MSMapRouteManeuverKindTurnRight,
>    MSMapRouteManeuverKindTurnHardLeft,
>    MSMapRouteManeuverKindTurnHardRight,
>    MSMapRouteManeuverKindFreewayEnterLeft,
>    MSMapRouteManeuverKindFreewayEnterRight,
>    MSMapRouteManeuverKindFreewayLeaveLeft,
>    MSMapRouteManeuverKindFreewayLeaveRight,
>    MSMapRouteManeuverKindFreewayContinueLeft,
>    MSMapRouteManeuverKindFreewayContinueRight,
>    MSMapRouteManeuverKindTrafficCircleLeft,
>    MSMapRouteManeuverKindTrafficCircleRight,
>    MSMapRouteManeuverKindTakeFerry,
>    MSMapRouteManeuverKindTakeTransit,
>    MSMapRouteManeuverKindTransfer,
>    MSMapRouteManeuverKindWait,
>    MSMapRouteManeuverKindWalk,
>    MSMapRouteManeuverKindInvalid
>};
>```

## Values

### Undefined

The maneuver is not defined.

### Start

The start of the route.

### Stopover

A stopover on the route.

### StopoverResume

The route has resumed after a stopover.

### End

The end of the route.

### GoStraight

Go straight.

### UTurnLeft

Make a U-turn to the left.

### UTurnRight

Make a U-turn to the right.

### TurnKeepLeft

Keep left.

### TurnKeepRight

Keep right.

### TurnLightLeft

Make a gentle left turn.

### TurnLightRight

Make a gentle right turn.

### TurnLeft

Turn left.

### TurnRight

Turn right.

### TurnHardLeft

Make a hard left turn.

### TurnHardRight

Make a hard right turn.

### FreewayEnterLeft

Enter the freeway on the left.

### FreewayEnterRight

Enter the freeway on the right.

### FreewayLeaveLeft

Leave the freeway on the left.

### FreewayLeaveRight

Leave the freeway on the right.

### FreewayContinueLeft

Continue on the freeway on the left.

### FreewayContinueRight

Continue on the freeway on the right.

### TrafficCircleLeft

Enter the traffic circle on the left.

### TrafficCircleRight

Enter the traffic circle on the right.

### TakeFerry

Take the ferry.

### TakeTransit

Take transit.

### Transfer

Transfer between public transit trips/runs at a transit stop.

### Wait 

Wait at a public transit stop, before taking a transit trip/run.

### Walk

Walk.

### Invalid

Invalid maneuver

## See Also

* [MapRouteManeuver](maproutemaneuver-class.md)