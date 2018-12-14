---
title: "User Location | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: f843b959-0435-4901-b8db-e179c9eeba74
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# User Location

Obtaining a user's location can easily be done using the [W3C Geolocation API](https://www.w3.org/TR/geolocation-API/). This API is exposed through the `navigator.geolocation` property in the browser. The browser will display a notification to the user the first time this API tries to get the users location, and ask permission to share this data. The geolocation class has the following static methods.

Name	                      |           Return Type  | Description
----------------------------- | ---------------------- | -----------------------------------------
`getCurrentPosition(`<br/>`successCallback:function,`<br/>`errorCallback?:function,`<br/>`opt?:PositionOptions)` |  | Attempts to obtain the users location. If successful it will trigger the callback function. This callback will receive a Position object that contains coordinates of the user and possibly additional information such as accuracy speed, heading, altitude.
`watchPosition(`<br/>`successCallback:function,`<br/>`errorCallback?:function,`<br/>`opt?:PositionOptions)` | 	number | Monitors the users position and triggers the callback if the user location information changes. This method will return a number which is the ID of this task. It can be used to clear/stop this task. 
`clearWatch(watchId:number)`  |                        | Clears/stops a watch position task with the specified ID.

## PositionOptions Object

Name                          | Type                   | Description
----------------------------- | ---------------------- | --------------------------------------------------
`enableHighAccuracy`          | boolean                | This tells the browser that it would like to receive the best possible results. This may result in slower response times or increased power consumption. Default is false.
`timeout`                     | number                 | The maximum length of time (expressed in milliseconds) that is allowed to pass from the call until the corresponding successCallback is invoked. Default is Infinity.
`maximumAge`                  | number                 | Indicates that the application is willing to accept a cached position whose age is no greater than the specified time in milliseconds. Default is 0.

## Position Object

Name                          | Type                   | Description
----------------------------- | ---------------------- | ------------------------------------
`coords`                      | Coordinate             | Contains the geographic coordinate information.
`timestamp`                   |                        | The time when the position object was acquired.

## Coordinate Object

Name                          | Type                   | Description
----------------------------- | ---------------------- | ----------------------------
`latitude`                    | number                 | The latitude coordinate value.
`longitude`                   | number                 | The longitude coordinate value.
`altitude`                    | number                 | The altitude in meters above the WGS84 ellipsoid. This value is not always returned.
`accuracy`                    | number                 | Accuracy level of the latitude and longitude coordinates in meters.
`altitudeAccuracy`            | number                 | Accuracy of the altitude value in meters. This value is not always returned.
`heading`                     | number                 | The direction in which the device is pointed in degrees counting clockwise where true north is 0 degrees. This value is not always returned.
`speed`                       | number                 | The speed at which the device is travelling in meters per seconds. This value is not always returned.


## Examples

  *  [Displaying a User Location](displaying-a-user-location-example.md)
  *  [Continuously Tracking a Users' Location](continuously-tracking-a-user-location-example.md)

## See Also

  * [Geolocation Accuracy Circle Example](../spatial-math-module-examples/geolocation-accuracy-circle-example.md)