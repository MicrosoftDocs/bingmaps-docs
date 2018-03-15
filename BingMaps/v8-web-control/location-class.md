---
title: "Location Class | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 848546f5-43af-42a1-a446-467f823866b9
caps.latest.revision: 6
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# Location Class
This class stores the coordinate information needed to mark locations on a map. The Location class consists of two properties: latitude and longitude. 

The latitude property is used to represent how far north or south a location is. This value is an angle measured around the center of the earth from the equator towards the poles. A positive value is in the northern hemisphere and a negative value is in the southern hemisphere. This value has a range of -90 to 90 degrees however due to the mathematics involved in representing the spherical globe as a flat 2D map, some calculations approach infinity as you approach polar latitudes. To avoid this, Bing Maps and many other mapping platforms that use the Mercator projection system clip the latitude coordinates to approximately -85 and 85 degrees. 

The longitude property stores the angle of horizontal offset from the prime meridian (0 degrees). This property has a value between -180 and 180 degrees. 

## Constructor

> `Location(latitude: number, longitude: number)`

## Properties

Name           | Type          | Description
-------------- | ------------- | --------------------
`latitude`     | number        | The latitude of the location.
`longitude`    | number        | The longitude of the location.

## Static Methods

The Location class has the following static methods.

Method                                       | Return Value  | Description
-------------------------------------------- | ------------- | --------------------------------
areEqual(loc1: [Location](../v8-web-control/location-class.md), loc2: [Location](../v8-web-control/location-class.md))   | boolean       | Determines if the specified [Location](../v8-web-control/location-class.md) objects are equal.
`normalizeLongitude(longitude: number)`       | number        | Normalizes the specified longitude so that it is between -180 and 180.
`parseLatLong(str: string)` | [Location](../v8-web-control/location-class.md) | Parses a location string of the form "lat,long". 

## Methods

The Location class has the following methods.

Method               | Return Value         | Description
-------------------- | -------------------- | ----------------------------------
`clone()`            | [Location](../v8-web-control/location-class.md)             | Returns a copy of the Location object.
`toString()`         | string               | Converts the Location object to a string.