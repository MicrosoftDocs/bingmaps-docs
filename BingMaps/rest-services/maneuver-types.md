---
title: "Maneuver Types | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 64c43775-3911-4c76-a0b4-32dc5824a258
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Maneuver Types
The following maneuver type values are returned the [Routes](../rest-services/routes-api.md) in the maneuverType field in the HTTP response. For more information about the values returned in the Routes API response, see [Route Data](../rest-services/route-data.md).  
  
|Maneuver Type|Instruction|  
|-------------------|-----------------|  
|ArriveFinish|Arrive at the final destination.|  
|ArriveIntermediate|Arrive at an intermediate waypoint.|  
|BearLeft|Bear left.|  
|BearLeftThenBearLeft|Bear left and then bear left again.|  
|BearLeftThenBearRight|Bear left and then bear right.|  
|BearLeftThenTurnLeft|Bear left and then turn left.|  
|BearLeftThenTurnRight|Bear left and then turn right.|  
|BearRight|Bear right.|  
|BearRightThenBearLeft|Bear right and then bear left.|  
|BearRightThenBearRight|Bear right and then bear right again.|  
|BearRightThenTurnLeft|Bear right and then turn left.|  
|BearRightThenTurnRight|Bear right and then turn right.|  
|BearThenKeep|Bear instruction and then a keep instruction|  
|BearThenMerge|Bear instruction and then a merge instruction.|  
|Continue|Continue on the current road.|  
|DepartIntermediateStop|Leave an intermediate waypoint in a different direction and road than you arrived on.|  
|DepartIntermediateStopReturning|Leave an intermediate waypoint in the same direction and on the same road that you arrived on.|  
|DepartStart|Leave the starting point.|  
|EnterRoundabout|Enter a roundabout.|  
|ExitRoundabout|Exit a roundabout.|  
|EnterThenExitRoundabout|Enter and exit a roundabout.|  
|KeepLeft|Keep left onto a different road.|  
|KeepOnRampLeft|Keep left and continue onto ramp.|  
|KeepOnRampRight|Keep right and continue onto ramp.|  
|KeepOnRampStraight|Keep straight and continue onto ramp.|  
|KeepRight|Keep right onto a different road.|  
|KeepStraight|Keep straight onto a different road.|  
|KeepToStayLeft|Keep left to stay on the same road.|  
|KeepToStayRight|Keep right to stay on the same road.|  
|KeepToStayStraight|Keep straight to stay on the same road.|  
|Merge|Merge onto a highway.|  
|None|No instruction.|  
|RampThenHighwayLeft|Take left ramp onto highway. This is part of a combined instruction.|  
|RampThenHighwayRight|Take right ramp onto highway. This is part of a combined instruction.|  
|RampThenHighwayStraight|Stay straight to take ramp onto highway. This is part of a combined instruction.|  
|RoadNameChange|Road name changes.|  
|Take|Take the road. This instruction is used when you are entering or exiting a ferry.<br /><br /> For example the following two route instructions use the Take maneuver to tell the user to take the Seattle-Bainbridge ferry and then to exit the ferry onto Olympic Drive.<br /><br /> -   Take Seattle-Bainbridge Ferry.<br />-   Take Olympic Drive.|  
|TakeRampLeft|Take ramp to the left.|  
|TakeRampRight|Take ramp to the right.|  
|TakeRampStraight|Stay straight to take ramp.|  
|TakeTransit|Take transit.|  
|Transfer|Transfer between public transit at transit stop.|  
|TransitArrive|Get off public transit at transit stop.|  
|TransitDepart|Get on public transit at transit stop.|  
|TurnBack|Turn back sharply.|  
|TurnLeft|Turn left.|  
|TurnLeftThenBearLeft|Turn left and then bear left.|  
|TurnLeftThenBearRight|Turn left and then bear right.|  
|TurnLeftThenTurnLeft|Turn left and then turn left again.|  
|TurnLeftThenTurnRight|Turn left and then turn right.|  
|TurnRight|Turn right.|  
|TurnRightThenBearLeft|Turn right and then bear left.|  
|TurnRightThenBearRight|Turn right and then bear right.|  
|TurnRightThenTurnLeft|Turn right and then turn left.|  
|TurnRightThenTurnRight|Turn right and then turn right again|  
|TurnThenMerge|Turn instruction followed by a merge instruction.|  
|TurnToStayLeft|Turn left to stay on the same road.|  
|TurnToStayRight|Turn right to stay on the same road.|  
|Unknown|The instruction is unknown.|  
|UTurn|Make a u-turn to go in the opposite direction.|  
|Wait|Wait at a transit stop.|  
|Walk|Walk.|