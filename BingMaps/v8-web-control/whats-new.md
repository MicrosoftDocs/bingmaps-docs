---
title: "What's New | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: e2542a65-9565-499b-8ad1-b0b01ffba2be
caps.latest.revision: 22
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# What&#39;s New

The following is a list of key features added to the Bing Maps V8 Web control dring one of its regular updates. Details about smaller changes to the API interface (i.e. new function parameters) can be found in the [Bing Maps V8 TypeScript Definition commit history](https://github.com/Microsoft/Bing-Maps-V8-TypeScript-Definitions/commits/master). 

## January 2018

**Configuration Driven Maps Framework**

Configuration driven maps allow you to quickly and easily create a map with your data with little to no coding required. Instead create a JSON configuration fill that species the data sets you want to render along with some map options and then easily generate a map from this. Find out more [here](map-control-concepts/configuration-driven-maps-framework/index.md). 

## November 2017

**Specify Bing Maps Key in Map Script URL**

By specifying your Bing Maps key as a URL parameter in the map script reference, it will allow for live site issues reported to the Bing Maps Enterprise support team by licensed customers to be migrated faster.

## October 2017

This release contains several new features and many smaller bug fixes. 

**Birds Eye map type now in dropdown**

Birds eye imagery has been available in V8 since May, but had to be enabled programmatically. Now it is available in the map type dropdown just like all other map types. This option will be disabled (appear faded) when the map is centered over a location that does not have birds eye imagery.

**Limit Autosuggest suggestions to a single country**

The Autosuggest manager now lets you specify a country to limit suggestions to using the new `countryCode` option.  

**Enable CORs on tile layers**

This new map option enables CORs (Cross Resource Sharing) on the base map tiles, as well as on all tile layers. This allows accessing the pixel data of the map canvas without any browser security issues. Check out [this demo](https://bingmapsv8samples.azurewebsites.net/#Map%20Image%20Generator) that uses this and the map canvas to generate a static image of the map. See [map options](map-control-api/mapoptions-object.md) for more details.

**Customize the Drawing toolbar**

You can now limit which toolbar options appear in the drawing toolbar. [Code Sample](https://bingmapsv8samples.azurewebsites.net/#Custom%20Drawing%20Toolbar)

**GeoXmlLayer Events**

The GeoXmlLayer class now supports all the same events as the Layer class.

**Access Direction Pushpins**

Access the pushpins of all waypoints rendered by the directions manager using the new `getAllPushpins()` function. Customize their look and feel or add events to them.

## July 2017

This release contains several new features and bug fixes. 

**GeoXml Module**

Easily import and export common spatial file formats such as KML, KMZ, GeoRSS, GML (via GeoRSS) and GPX. Load it as a layer on the map or directly access the data with just a few lines of code.

[Try it now](https://bingmapsv8samples.azurewebsites.net/#GeoXmlLayer%20-%20Local%20Data) | [Documentation](modules/geoxml-module/index.md)

**Ground Overlays**

Overlay georeferenced images on top of the map so that they move and scale as you pan and zoom the map. This is great for building floor plans, overlaying old maps, or imagery from a drone.

[Try it now](https://bingmapsv8samples.azurewebsites.net/#Basic%20Ground%20Overlay) | [Documentation](map-control-api/groundoverlay-class.md)

**LocationRect class improvements**

Two new static methods have been added the LocationRect class. The first is called `fromShapes` and lets you easily generate a LocationRect from an array of shapes. The second is called `merge` and makes it easy to combine two LocationRect objects together to generate the minimum bounding LocationRect. 

[Documentation](map-control-api/locationrect-class.md) 

**Get Autosuggest suggestions programmatically**

The autosuggest manager in Bing Maps has a `getSuggestions` function which can be used to retrieve autosuggest suggestions without having to attach a textbox to the autosuggestion manager. Currently the suggestions returned by this function do not have their bestView property set and address suggestions do not have location coordinates. These suggestions can easily be enriched by using the Search module to geocode the suggestion.

**TypeScript Definitions Updated**

The [Bing Maps V8 TypeScript definition](https://github.com/Microsoft/Bing-Maps-V8-TypeScript-Definitions/commit/0621d4ddc1a8057bc7add3d9e89ceaf9b19ea3d3) have been updated and can provided additional details around API changes that have occurred as part of this release.

## June 2017

This release contains several new features and bug fixes. 

**Birdseye Map Type**

Thee Birdseye map type provides high resolution imagery that is taken at a 45 degree angle to the horizon with view points from 4 different directions (north, south, east west). A lot of the new imagery is still being processed and not yet online. As such this map type can only be enabled programmatically and does not show up in the map type drop down at this time. 

[Try it now](https://www.bing.com/api/maps/sdkrelease/mapcontrol/isdk#birdseyeV2+JS)

**Custom Map Styles**

The Bing Maps V8 control has a new map option called **customMapStyle** which can be used to customize elements of the map such as road color, visibility of certain types of labels and much more. 

[Try it now](https://bingmapsv8samples.azurewebsites.net/#Simple%20Style%20Editor)

**Direction Route Line & Waypoint Style Options**

With this release the route line and waypoints can be customized using the [DirectionsRenderOptions](modules/directions-module/directionsrenderoptions-object.md). 

**Postal Code support added to Auto Suggest module**

Address queries now return postal code information for the selected suggestion.

**TypeScript Definitions Updated**

The [Bing Maps V8 TypeScript definition](https://github.com/Microsoft/Bing-Maps-V8-TypeScript-Definitions/commit/e6d7cc457f867a83a332ac078dc47d0b3c1412b1) have been updated and can provided additional details around API changes that have occurred as part of this release.


## January 2017

This release primarily consisted of bug fixes and performance improvements. 

**RoutePath Locations**

When you calculate a route using the directions manager you can now easily get an array of locations that make up the route path. This is useful if you want to create a custom styled route line on the map, or if you want to perform route based calculations such as search for data along or near a route. Combine this with the Bing Maps REST elevation service and easily generate route elevation profiles. This is documented as part of the Route response object  [here](modules/directions-module/route-object.md).

**Cardinal Splines**

The Spatial Math module has a new function that calculates a cardinal spline that passes through a specified array of locations. 

[Try it now](https://www.bing.com/api/maps/mapcontrol/isdk?autoRedirect=false#getCardinalSpline+JS)

**Multiple Map Support**

Bing Maps V8 now supports loading multiple map instances on a single page. 

**US Census Data**

The Bing Maps team has made 2010 US Census data available through the Bing Spatial Data Services for easy use in your application. This data has been exposed through 4 different data sources, each containing census data based on a different type of geographical region; states, counties, ZCTA5 (Zip code tabulation area), and the 111th Congressional districts. 

[Documentation](../spatial-data-services/public-data-sources/2010-us-census-data-sources.md) | [Code Samples](map-control-concepts/spatial-data-services-module-examples/query-api/choropleth-map-example.md) | [Try it now](https://www.bing.com/api/maps/sdk/mapcontrol/isdk#sdsChoroplethMap+JS)

## October 2016

**Map Lite Mode**

The Bing Maps V8 control by default will usually use vector map labels depending on the browser and device the user is using. A new `liteMode` map option has been added which when set to true will disable vector map labels and instead will render the labels directly on the map tiles. Doing this improves the overall performance of the map control, but will disable vector label specific features such as label collision detection with pushpins. The map automatically will load into `liteMode` when the map is used in slower browsers or devices. You can override this behavior by setting this option to false. You can find out more about vector map labels in Bing Maps V8 [here](articles/vector-map-labels.md).

**Hide/Show Minified Navigation Bar Traffic button**

The minified navigation bar shows a traffic button by default. A map option called `showTrafficButton` has been created. When set to false, the traffic button will not be displayed in the minified navigation bar.

**Platform Improvements**

The Bing Maps team has spent most of October improving the Bing Maps V8 platform to increase the overall stability and scalability. One of these improves consisted of adding several additional automated tests to the platform which can help identify issues early.

**Holiday Season Code Freeze**

The team plans to put the main release branch into a code freeze for the months of November and December due to the peak holiday season. During this time the team will focus on bug fixes and adding smaller high priority features.
 
## September 2016

**Data Binning Module**

This module provides makes it easy to create data bins from arrays of pushpins and display them on the map.
 
[Documentation](modules/data-binning-module/index.md) | [Code Samples](map-control-concepts/data-binning-module-examples/index.md) | [Try it now](https://www.bing.com/api/maps/sdk/mapcontrol/isdk#gradientColorScaleBinning+JS)

**Contour Module**

This module makes it easy to take contour line data and visualize it on Bing Maps as non-overlapping colored areas. 

[Documentation](modules/contour-module/index.md) | [Code Samples](map-control-concepts/contour-module-examples/index.md) | [Try it now](https://www.bing.com/api/maps/sdk/mapcontrol/isdk#basicContourLayer+JS)

**Double Click Support**

All IPrimitive shapes (pushpins, polylines, polygons), and the Layer Class now support double click events.

**Spatial Math Contains Calculation**

A contains calculation was added to the Geometry section of the Spatial Math library. This function determines if one shape is completely contained within the boundaries of another.

**Directions Input Panel Waypoint bug fix**

The Directions input panel has been updated to sync with the waypoint data that is passed into the Directions Manager programmatically.

## August 2016

This update includes 30+ bug fixes and several new features. The [TypeScript defintions](https://github.com/Microsoft/Bing-Maps-V8-TypeScript-Definitions) have been updated and are also now available as an npm package.

**Animated Tile Layers**

Makes it easy to smoothly animate through and array of tile layers. 

[Try it now](https://www.bing.com/api/maps/sdk/mapcontrol/isdk#weatherRadarMap+JS)

**High Contrast Support**

To make Bing Maps more accessible, high contrast support has been added. When the users computer is in high contrast mode, a high contrast version of the road maps will be displayed. 

**New Road Map Styles**

Three new road map styles have been added; grayscale, canvasDark and canvasLight. These are designed to make it easy to focus on the data you overlay on top of the map and are much better suited for business intelligence type scenarios than the default road map style. You can find documentation [here](map-control-api/maptypeid-enumeration.md). 

**Infobox improvements**

The infobox class now supports HTML descriptions values. The infobox class also automatically scales to fit it's content. Maximum width and height values can be specified. 

[Try it now](https://www.bing.com/api/maps/sdk/mapcontrol/isdk#infoboxWithIFrame+JS)

 **Polygon & Polyline generalization**
 
By default polylines and polygons are generalized (simplified) when rendered based on the current zoom level. This provides a performance enhancement when these shapes have more than just a few locations in them. If you are working with a lot of simple shapes (i.e. triangles) consider disabling this feature by setting the `generalizable` option of the shape to **false** as this optimization will not provide any benefit in this case. 

**DrawingTools improvements**

The DrawingTools class has had a number of improvements which make it much easier to create individual shapes and attach events to them.  

**Disable Streetside options**

There are two new map options for disabling streetside functionality. The first, `disableStreetside`, completely disables this feature and removes it as an option in the navigation bar. The second, `disableStreetsideAutoCoverage`, disables the automatic streetside coverage layer that appears when zoomed in at lower zoom levels.

**Microsoft Maps CSS namespacing**

All CSS classes used by the Bing Maps V8 SDK have been namespaced with a MicrosoftMaps namespace to reduce the likelihood of naming collisions with CSS classes from other libraries.

## July 2016

This is the first regular update to the main release branch of V8 since the initial production release in June. 

**Spatial Math Geometry**

The Spatial Math module has had a massive addition consisting of 24 spatial geometry calculations, bringing the total number of calculations available in the spatial math module to 47. Some of these calculations include: binary operations of shapes (intersection, difference, union), convex and concave hulls, Voronoi diagrams, shape validation and much more. 

[Try it now](https://www.bing.com/api/maps/sdk/mapcontrol/isdk#binaryOperations+JS).
 
**Draggable Pushpins**

Easily move drag pushpins around on the map by setting the `draggable` pushpin option to true. 

[Try it now](https://www.bing.com/api/maps/sdk/mapcontrol/isdk#pushpinDragEvents+JS).

**Custom Overlays**

Custom overlays allow you to create your own custom rendering layers with the map control. Why might you want to do this you ask? Several years ago one of our Microsoft Bing Maps MVP’s created an open source heat map layer for Bing Maps V7. In order to get this to work correctly he needed to insert an HTML5 canvas into the DOM structure of the map control. There was no supported way to do this and as such a hacky solution was implemented. This solution ended up breaking 3 times over the lifetime of Bing Maps V7. With this feature we have added a supported way to create custom rendering layers so that developers can easily create and experiment with new custom data visualizations.

**TypeScript Definitions**

Last week we released TypeScript definitions available for Bing Maps V8 on GitHub. You can find the announcement [here](https://blogs.bing.com/maps/August-2016/TypeScript-Definitions-for-Bing-Maps-V8-Released-o). These definitions have been updated to include all the new features that are in this release. 

**Transit Direction support in Japan**

Public transit is one of the most common ways of traveling in Japan. You can now easily calculate transit directions in Japan now. 

**Clickable Pushpin area**

Often, when using custom pushpins, the clickable area of the pushpin is rectangular, as the image used to create custom pushpins has a rectangular shape. This can often cause issues when using mouse events because often the actual drawn image may not be a rectangle itself and as such has some whitespace around it which will block the mouse events from getting to the pushpins below it. With this in mind, V8 now lets you specify that a rounded click area should be used instead. Early testing has found that this drastically reduces false clicks on pushpins and thus creates a much better user experience. Find our more [here](map-control-api/pushpinoptions-object.md).
 
**GeoJSON and Query API Shape Styling**

Until now, styling of data that came from the GeoJSON module or Query API in Bing Maps V8 was limited to specifying a single default style that is used by all shapes. If you wanted to style individual shapes, you had to loop through the results and apply the logic to style each shape individually. Now, with this update, any Pushpin, Polyline or Polygon option can be specified for individual shapes through the shapes GeoJSON properties or as a data source column in the Bing Spatial Data Services. 

**Mercator Map Type**

Bing Maps provides road and aerial maps which are great in most cases, but sometimes you may want to hide these all together. Perhaps you have your own custom tile layer that you want to display instead, or perhaps you simply want to view your data on its own without a map background. You can easily do this now by setting the map type id of the map to `mercator`. 

**Mouse over cursors for shapes**

When hovering over a shape that has any mouse events attached to it, the mouse cursor will change to a pointer. You can now specify for each individual shape what CSS cursor should appear when hovering over it. 

**Change the background color of the map**

Use the `backgroundColor` map option to change the color of the map canvas that is displayed when behind the maps. 

**Easily parse locations from strings**

The Location class now has a static `parseLatLong` function which creates a Location object from a string that has the format “latitude,longitude”.

**Bug Fixes**

Since the initial release of V8 many developers have been proactive in reporting bugs and testing the fixes in the experimental branch. With this release there are over 60 bug fixes.

## June 2016

This is the first production ready release of the Bing Maps V8 Web control. V8 offers many new features not available in previous versions of Bing Maps.

**Performance improvements**

In the past, the Bing Maps web controls used traditional DOM elements such as images and SVG's to render the map and the content on it. These work well working with small data sets but as you add more data to the map the browser needs to keep track of and update a lot more DOM elements. It doesn't take long before there is a noticeable performance hit.

Bing Maps V8 uses the HTML5 Canvas for rendering. This provides the ability to render significantly more data and also allows a lot more advance features to be added to Bing Maps.

Additionally the V8 control also supports asynchronous loading. 

There is however one limitation of using the HTML5 canvas, HTML DOM elements can't be rendered on the map canvas. As such custom pushpins in V8 do not support HTML content. There are however a number of other options for creating custom pushpins in V8 as you can see in the examples [here](map-control-concepts/pushpins/index.md).

**Code Optimizations**

While developing the Bing Maps V8 SDK the development team focused on streamlining the API to align with common customer scenarios. By doing this the team was able to significantly reduce the amount of code required to create a mapping app when compared to writing an equivalent app using a previous versions of Bing Maps or a competitors mapping platform. See the [Code Optimizations in V8 article](articles/code-optimizations-in-v8.md) for more details.

**New Branching System**

There are three branches of the Bing Maps V8 SDK that can be accessed. This provides the option to access new features as soon as they are available, even if those features have not been thoroughly tested or completed. Learn more about this new branching system [here](creating-and-hosting-map-controls/map-control-branches.md).

**Vector Labels**

The map labels in the Bing Maps V8 SDK are separate from the base map and sit above the data on the map. This helps ensures that the labels can be clearly visible no matter what data is added to the map. When pushpins overlap labels the labels can detect this and move out of the way. If it is a road label it will move along the road. If it is a city name it may move up a bit. If there a lot of pushpins in an area the label may be hidden entirely. Find out more about this feature [here](articles/vector-map-labels.md). 

**Streetside Imagery**

Explore 360-degrees of street level imagery.

**Improved Mobile Support**

Many developers use the Bing Maps web control in cross platform mobile apps. V8 includes a number of improvements for mobile including; better support for higher resolution screens, automatically switches to lite mode which renders labels on the map tiles instead of using vector labels (provides better performance on lower power devices), automatically changes the navigation bar to a more mobile device friendly layout.   

**Automatic User Culture and Region Detection**

Not everyone sees the world the same. There are many disputed names and borders around the world. The Bing Maps V8 SDK automatically detects the user region when available and ensures that the base map data aligns with the view of the user’s region.
  
**Additional Navigation Bar styles**

 In V8 we have added additional navigation bar styles and layouts. Some are ideal for large maps in a desktop browser while others are better suited for use in mobile browsers. Find out more [here](map-control-api/navigationbarmode-enumeration.md).

**New Modules**
Name                                   | Description
-------------------------------------- | --------------------- 
[Microsoft.Maps.Autosuggest](modules/autosuggest-module/index.md)             | Provides location based suggestions as you type.
[Microsoft.Maps.Clustering](modules/clustering-module/index.md)              | This module allows you to easily add in client side clustering to your application. Client Side Clustering is a method where pushpins that are close together are grouped and represented as a single pushpin, often using a different icon to indicate the cluster. This is a great way to improve both the user experience and performance of the map.
[Microsoft.Maps.DrawingTools](modules/drawing-tools-module/index.md) | Provides a set of tools for drawing and editing shapes on top of the map.
[Microsoft.Maps.GeoJSON](modules/geojson-module/index.md)	               | This module makes it easy to import or export data in GeoJSON format.
[Microsoft.Maps.HeatMap](modules/heat-map-module/index.md)            | The module allows you to render an array of Location objects as a density based heat map.
[Microsoft.Maps.SpatialDataService](modules/spatial-data-service-module/index.md)      | This module wraps the Query and GeoData REST API’s in the Bing Spatial Dara Services and expose them as an easy to use JavaScript library. 
[Microsoft.Maps.SpatialMath](modules/spatial-math-module/index.md)             | The module provides a bunch of useful spatial math functions.
[Microsoft.Maps.WellKnownText](modules/well-known-text-module.md)           | This module makes it easy to import or export data in Well Known Text format.) 

**Directions Module improvements**

The Directions module in V8 has many new improvements such as the optional input panel which provides suggestions as you type. Take a look at the [Directions Input Panel example](map-control-concepts/directions-module-examples/directions-input-panel.md).

**Test Data Generator**

Creating a demo or testing out some custom code and need some test data? Use the built in Test Data Generator to create random pushpins, polygons and more. Find out more [here](map-control-api/testdatagenerator-class.md).

**Backwards Compatibility**

Bing Maps V8 is approximately 90% backwards compatible with V7. For information about V7 features that have been deprecated, please see the [Bing Maps V7 to V8 Migration Guide](https://social.technet.microsoft.com/wiki/contents/articles/34563.bing-maps-v7-to-v8-migration-guide.aspx).