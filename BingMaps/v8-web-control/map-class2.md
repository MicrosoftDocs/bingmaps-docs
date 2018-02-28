---
title: "Map Class2 | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: acbece0c-cff8-4afc-9ac1-50abb04cc84f
caps.latest.revision: 21
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Map Class
The map object generates an interactive map within a specified DOM element. When loading the map you can reference the DOM element to render the map in by either referencing an element directly (i.e. document.getElementById), or by passing in a HTML ID selector (i.e. #myMap). This is normally a reference to an empty div. 

You can customize the map by passing in number of different options. Some of these options can be specified when creating the map while others can be changed at any time. When loading the map, you can specify settings from the MapOptions and ViewOptions objects.  

## Constuctor

> Map(containerElement: node _or_ string, options?: [MapOptions](MapOptions%20Object.md) | [ViewOptions](ViewOptions%20Object.md))

## Properties

Name	   | Type             | Description
-----------| ---------------- | -----------
`entities`   | [EntityCollection](EntityCollection%20Class.md) | Use this property to add or remove individual shapes to the default layer in the map. 
`layers`     | [LayerCollection](../v8-web-control/layercollection-class.md) | Use this property to add layers such as; data, tile, heat map and clustering layers to the map.  

## Static Methods

Method	                                                | Return Type  | Description
--------------------------------------------------------|--------------|-------------
`getClosestPanorama(bounds: LocationRect, success: function(panoramaInfo: IPanoramaInfo), missingCoverage: function())` | | Gets the streetside panorama information closest to the specified bounding box and returns using a success callback function. This information can then be used to set the map view to that streetside panorama.
`getVersion()` | string | Returns the branch name; release or experimental.


## Methods

Method	                                                | Return Type  | Description
--------------------------------------------------------|--------------|-------------
`dispose()`                                               |              | Deletes the Map object and releases any associated resources.
`getBounds()`                                             | [LocationRect](LocationRect%20Class.md) | Returns the location rectangle that defines the boundaries of the current map view.
`getCenter()`	                                            | [Location](Location%20Class.md)     | Returns the location of the center of the current map view.
`getCopyrights(callback: function(copyrights: string[]))` |      | Returns to the specified callback an array of strings representing the attributions of the imagery currently displayed on the map.
`getCredentials(callback: function(sessionId:string))`	|	           | Gets the session ID. This method takes in callback function and passes a session ID to it which can be used in place of a Bing Maps key when calling other Bing Maps services.  For example: <br/><br/>` map.getCredentials(function(sessionId)`<br />`{ `<br />`    //Use sessionId when calling REST services`<br />` });`<br /><br />
`getCulture()`	                                        | string       | Returns the users region setting.
`getHeading()`                                            | number       | Returns the heading of the current map view.
`getHeight()`	                                            | number       | Returns the height of the map control.
`getImageryId()`	                                        | string       | Returns a user friendly string that represents the imagery currently displayed on the map. For example; if the map is displaying aerial imagery, this function would return “Aerial”.
`getMapTypeId()`                                          | [MapTypeId](MapTypeId%20Enumeration.md)    | Returns a string that represents the current map type displayed on the map. Valid map types are listed in the [MapTypeId Enumeration](MapTypeId%20Enumeration.md) topic.
`getMetersPerPixel()`                                     | number       | Returns the current scale in meters per pixel of the center of the map.
`getOptions()`                                              | [MapOptions](MapOptions%20Object.md)   | Returns the map options that have been set. Note that if an option is not set, then the default value for that option is assumed and getOptions returns undefined for that option.
`getPageX()`                                              | number       | Returns the x coordinate of the top left corner of the map control, relative to the page.
`getPageY()`                                              | number       | Returns the y coordinate of the top left corner of the map control, relative to the page.
`getPitch()` | number | Returns the pitch of the current streetside map view.
`getRootElement()`                                        | HTMLElement  | Returns the map’s root node.
`getUserRegion()`                                         | string       | Returns the users region setting.
`getWidth()`	                                            | number       | Returns the width of the map control.
`getZoom()`                                               | number       | Returns the zoom level of the current map view.
`getZoomRange()`                                          | [Range](../v8-web-control/range-object.md)  | Returns the range of valid zoom levels for the current map view.
`isMercator()`                                              | boolean      | Returns a boolean indicating whether the map is in a regular Mercator nadir mode.
`isRotationEnabled()`                                     | boolean      | Returns true if the current map type allows the heading to change; false if the display heading is fixed.
setMapType(mapTypeId: [MapTypeId](MapTypeId%20Enumeration.md))                        |              | Sets the current map type. Takes in [MapTypeId enumeration](MapTypeId%20Enumeration.md).
setOptions(options: [MapOptions](MapOptions%20Object.md))	                    |              | Sets map options that modify how the map control works.
setView(viewOptions: [ViewOptions](ViewOptions%20Object.md))	                    |              | Sets the map view based on the specified view options.
tryLocationToPixel(location: [Location](Location%20Class.md) _or_ [Location](Location%20Class.md)[], reference?: [PixelReference](PixelReference%20Enumeration.md))  |  null, [Point](Point%20Class.md), or [Point](Point%20Class.md)[]      | Converts a specified Location to a Point on the map relative to the specified PixelReference. If reference is not specified, PixelReference.viewport is used. If the map is not able to convert the Location, null is returned.<br/><br/> Alternatively, it can also convert an array of Location objects and return an array of Points. If any of the conversions fail, null is returned.
tryPixelToLocation (point: [Point](Point%20Class.md) _or_ [Point](Point%20Class.md)[], reference?: PixelReference)          | null, [Location](Location%20Class.md), or [Location](Location%20Class.md)[] | Converts a specified Point to a Location on the map relative to the specified PixelReference. If reference is not specified, PixelReference.viewport is used. If the map is not able to convert the Point, null is returned.<br/><br/>Alternatively, it can also convert an array of Point objects and return an array of Locations. If any of the conversions fail, null is returned.

## Events

The following events are available on the map.

Name	        | Arguments  | Description
--------------- | ----------- | -----------
`click`           | [MouseEventArgs](https://msdn.microsoft.com/library/mt748664.aspx) | Occurs when the mouse is used to click the map or when a touch end event occurs over the map.
`dblclick`	    | [MouseEventArgs](https://msdn.microsoft.com/library/mt748664.aspx) | Occurs when the mouse is used to double click the map.
`mapresize` | | Occurs when the map has been resized. This will fire multiple times if dragging a window to resizie the map.
`maptypechanged`  | [MapTypeEventArgs](../v8-web-control/maptypeeventargs-object.md) | Occurs when the map type changes.
`mousedown`       | [MouseEventArgs](https://msdn.microsoft.com/library/mt748664.aspx) | Occurs when the left mouse button is pressed or a touch start event occurs on the map.
`mousemove`       | [MouseEventArgs](https://msdn.microsoft.com/library/mt748664.aspx) | Occurs when the mouse cursor moves or the touch move event occurs over the map.
`mouseout`        | [MouseEventArgs](https://msdn.microsoft.com/library/mt748664.aspx) | Occurs when the mouse cursor moves out of the area covered by the map.
`mouseover`        | [MouseEventArgs](https://msdn.microsoft.com/library/mt748664.aspx) | Occurs when the mouse cursor moves over of the area covered by the map.
`mouseup`         | [MouseEventArgs](https://msdn.microsoft.com/library/mt748664.aspx) | Occurs when the left mouse button is lifted up or when the  touch end event occurs over the map.
`mousewheel`      | [MouseEventArgs](https://msdn.microsoft.com/library/mt748664.aspx) | Occurs when the mouse wheel is used when the mouse cursor is over the map.
`rightclick`      | [MouseEventArgs](https://msdn.microsoft.com/library/mt748664.aspx) | Occurs when the right mouse button is used to click the map or when a long touch press occurs over the map.
`viewchange`      | | Occurs for every frame of a map view change.
`viewchangeend`   | | Occurs when the map view is done changing. This event occurs when a view is the same for one frame of a map view change. For example, if the mouse is used to drag the map to change the view, but pauses during the drag (without releasing the mouse button), viewchangeend occurs twice. You can use the addThrottledHandler method to customize the number of events that occur.
`viewchangestart`	| | Occurs when the map view starts changing.
