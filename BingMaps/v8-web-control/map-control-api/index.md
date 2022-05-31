---
title: "Map Control API Reference | Microsoft Docs"
description: "This article describes static properties, static methods, and API components related to Map Control API Reference."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 12c53ca8-491e-4d73-a658-0de6c5b9d708
caps.latest.revision: 18
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Map Control API Reference (Microsoft Docs)

The Bing Maps V8 web control uses the `Microsoft.Maps` namespace to expose its API. This namespace has the following static properties and methods:

## Static Properties

| Name |  Type | Description |
|------|-------|--------------|
| ConfigurableMap | [ConfigurableMap](configurablemap-class.md) | Generate a map using a configuration file. See [Configuration Driven Maps framework](../map-control-concepts/configuration-driven-maps-framework/index.md) for more details. |
| Credentials | string  | The Bing Maps key specified in the map API script URL or used to load the map. |

## Static Methods  

| Name |  Return Type | Description |
|------|--------------|--------------|
| getIsBirdseyeAvailable(loc: [Location](location-class.md), heading: [Heading](heading-enumeration.md) _or_ number, callback: function(isAvailable: boolean)) | | Checks to see if Birdseye imagery is available at a specified location and heading. |
| loadModule(moduleKey: string _or_ string\[\], options?: [ModuleOptions](moduleoptions-object.md) _or_ function()) | | Loads the specified registered module, making its functionality available. You can provide the name of a single module or an array of names in. Options or a callback function that is called when the module is loaded can be specified.<br/><br/>To register a custom module, use the registerModule method before calling the loadModule method. |
| moduleLoaded(moduleKey: string) | | Signals that the specified module has been loaded and if specified, calls the callback function in loadModule. Call this method at the end of your custom module script. |
| registerModule(moduleKey: string, scriptURL: string, options: \{ styleURLs:string\[\] \}) | | Registers a module with the map control. The name of the module is specified in moduleKey, the module script is defined in scriptURL, and the options provides the location of a *.css file to load with the module.<br/><br/>Tip: To minimize possible conflicts with other custom modules, choose a unique module name (defined in moduleKey). For example, you can use your company name in the name of the module.<br/><br/>Once you have registered a module, you can make its functionality available by loading it using loadModule. |


## API Components

The following is a list of the core components in the Bing Maps V8 web control. Additional functionalities are also available as [modules](../modules/index.md). 

Type          | Description
--------------| -----------
[AnimatedTileLayer Class](animatedtilelayer-class.md) | Provides a layer which can smoothly animate through an array of tile layer sources.
[AnimatedTileLayerOptions Object](animatedtilelayeroptions-object.md) | An object that defines the options for an [AnimatedTileLayer Class](animatedtilelayer-class.md) .
[AnimatedFrameEventArgs Object](animatedframeeventargs-object.md) | The event arguments for when a layer frame is being loaded in an [AnimatedTileLayerOptions Object](animatedtilelayeroptions-object.md).
[Color Class](color-class.md) | Utility structure for working with colors across various Map objects.
[CustomOverlay Class](customoverlay-class.md) | A class that can be used to create custom rendering layers on the map. These can be static overlays such as custom navigation bars, or dynamic overlays such as custom visualization layers. 
[CustomOverlayOptions Object](customoverlayoptions-object.md) | Object used to define the settings of a [CustomOverlay](customoverlay-class.md).
[Events Class](events-class.md) | A static class exposed through the `Microsoft.Maps` namespace that provides an interface for attaching events to the map, pushpins, polylines, polygons, layers and modules.
[GroundOverlay Class](groundoverlay-class.md) | A map overlay that binds an image to a bounding box area on the map.
[GroundOverlayOptions Object ](groundoverlayoptions-object.md)| The options that specify how to render a ground overlay on the map.
[Heading Enumeration](heading-enumeration.md) | Standard compass headings; north, south, east, west.
[Infobox Class](infobox-class.md) | Describes the operation of a pop-up user interface.
[InfoboxActions Object](infoboxactions-object.md) | Object used to define callback actions for an [Infobox](../map-control-concepts/infoboxes/index.md).
[InfoboxEventArgs Object](infoboxeventargs-object.md) | An object that contains information about an infobox event.
[InfoboxOptions Object](infoboxoptions-object.md) | Object used to define default settings and options for an [Infobox](../map-control-concepts/infoboxes/index.md).
[IPrimitive Class](iprimitive-class.md) | An interface in which pushpins, polylines and polygons are derived from.
[IPrimitiveChangedEventArgs Object](iprimitivechangedeventargs-object.md) | An object that is returned when a `changed` event occurs on an [IPrimitive](iprimitive-class.md) shape. |
[LabelOverlay Enumeration](labeloverlay-enumeration.md) | Defines how map labels are displayed. 
[Layer Class](layer-class.md) | An overlay of image-based data on a map.
[LayerCollection Class](layercollection-class.md) | A static class that is exposed through the `map.layers` property and allows you to add layers such as; data, heat map, and tile layers.
[Location Class](location-class.md) | Represents a geographic location.
[LocationRect Class](locationrect-class.md) | Represents a rectangular geographic area.
[Map Class](map-class.md)    | Main object for manipulating a view of a map on a page.
[MapOptions Object](mapoptions-object.md) | Initial options for configuring a map.
[MapTypeEventArgs Object](maptypeeventargs-object.md) | An object is returned by the map event handler when using the `maptypechanged` event.  
[MapTypeId Enumerations](maptypeid-enumeration.md) | Various options for configuring the base map visuals.
[ModuleOptions Object](moduleoptions-object.md) | Options used for instantiating a [module](../map-control-concepts/modular-framework/index.md).
[MouseEventArgs Object](mouseeventargs-object.md) | An object that is returned to event handlers when a mouse event is attached to a map, pushpin, polyline, or polygon. 
[NavigationBarMode Enumeration](navigationbarmode-enumeration.md) | Used to customize the layout and style of the navigation bar.  
[NavigationBarOrientation Enumeration](navigationbarorientation-enumeration.md) | Define how the navigation bar controls are laid out.
[OverviewMapMode Enumeration](overviewmapmode-enumeration.md) | Describes how an overview map mode is displayed on a Streetside-based view.
[PanoramaInfo Object](panoramainfo-object.md) | An object tthat contains information about a streetside scene.
[PixelReference Enumeration](pixelreference-enumeration.md) | Describes what a pixel-based reference is relative to on the screen.
[Point Object](point-class.md) | Represents a pixel coordinate.
[PointCompression Class](pointcompression-class.md) | A static class that provides a compression algorithm to encodes/decodes a collection of Location objects into a string and back. This algorithm is used for generating a compressed collection of locations for use with the Bing Maps REST Elevation Service. This algorithm is also used for decoding the compressed coordinates returned by the GeoData API. 
[Polygon Class](polygon-class.md) | An enclosed geographic area on a map.
[PolygonOptions Object](polygonoptions-object.md) | Initial options for creating a map polygon.
[Polyline Class](polyline-class.md) | A line across geographic points on a map.
[PolylineOptions Object](polylineoptions-object.md) | Initial options for creating a map polyline. 
[Pushpin Class](pushpin-class.md) | A graphical/text representation of a geographic point on a map.
[PushpinOptions Object](pushpinoptions-object.md) | A set of options that define a pushpin on a map.
[PyramidTileId Class](pyramidtileid-class.md) | Additional information about a tile during a TileSource-related operation.
[Range Object](range-object.md) | Used to specify a min and max value range.
[StreetsideOptions Object](streetsideoptions-object.md)| Initial options for configuring a Streetside view.
[StylesOptions Object](stylesoptions-object.md)| Options for configuring a bulk set of polylines and polygons.
[TestDataGenerator Class](testdatagenerator-class.md) | A static class that makes it easy to generate random test data in the form of colors, locations, pushpins, plylines, polygons, and polygons with holes. 
[TileLayer Class](tilelayer-class.md) | Represents an overlay of image-based data on a map.
[TileLayerOptions Object](tilelayeroptions-object.md) | Options for configuring a tile layer overlay for a map.
[TileSource Class](tilesource-class.md) | Represents a source of URLs for a tile layer.
[TileSourceOptions Object](tilesourceoptions-object.md) | Options for configuring the source of URLs used to supply a tile layer overlay on a map.
[ViewOptions Object](viewoptions-object.md) | Options for configuring a view of the map. 


 