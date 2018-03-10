---
title: "Map Control API Reference | Microsoft Docs"
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
---
# Map Control API Reference
The Bing Maps V8 web control uses the `Microsoft.Maps` namespace to expose its API. This namespace has the following static properties and methods:

## Static Properties

| Name |  Type | Description |
|------|-------|--------------|
| ConfigurableMap | [ConfigurableMap](../v8-web-control/configurablemap-class.md) | Generate a map using a configuration file. See [Configuration Driven Maps framework](../v8-web-control/configuration-driven-maps-framework.md) for more details. |
| Credentials | string  | The Bing Maps key specified in the map API script URL or used to load the map. |

## Static Methods  

| Name |  Return Type | Description |
|------|--------------|--------------|
| getIsBirdseyeAvailable(loc: [Location](../v8-web-control/location-class.md), heading: [Heading](../v8-web-control/heading-enumeration.md) _or_ number, callback: function(isAvailable: boolean)) | | Checks to see if Birdseye imagery is available at a specified location and heading. |
| loadModule(moduleKey: string _or_ string\[\], options?: [ModuleOptions](../v8-web-control/moduleoptions-object.md) _or_ function()) | | Loads the specified registered module, making its functionality available. You can provide the name of a single module or an array of names in. Options or a callback function that is called when the module is loaded can be specified.<br/><br/>To register a custom module, use the registerModule method before calling the loadModule method. |
| moduleLoaded(moduleKey: string) | | Signals that the specified module has been loaded and if specified, calls the callback function in loadModule. Call this method at the end of your custom module script. |
| registerModule(moduleKey: string, scriptURL: string, options: \{ styleURLs:string\[\] \}) | | Registers a module with the map control. The name of the module is specified in moduleKey, the module script is defined in scriptURL, and the options provides the location of a *.css file to load with the module.<br/><br/>Tip: To minimize possible conflicts with other custom modules, choose a unique module name (defined in moduleKey). For example, you can use your company name in the name of the module.<br/><br/>Once you have registered a module, you can make its functionality available by loading it using loadModule. |


## API Components

The following is a list of the core components in the Bing Maps V8 web control. Additional functionalities are also available as [modules](../v8-web-control/modules.md). 

Type          | Description
--------------| -----------
[AnimatedTileLayer Class](../v8-web-control/animatedtilelayer-class.md) | Provides a layer which can smoothly animate through an array of tile layer sources.
[AnimatedTileLayerOptions Object](../v8-web-control/animatedtilelayeroptions-object.md) | An object that defines the options for an [AnimatedTileLayer Class](../v8-web-control/animatedtilelayer-class.md) .
[AnimatedFrameEventArgs Object](../v8-web-control/animatedframeeventargs-object.md) | The event arguments for when a layer frame is being loaded in an [AnimatedTileLayerOptions Object](../v8-web-control/animatedtilelayeroptions-object.md).
[Color Class](../v8-web-control/color-class.md) | Utility structure for working with colors across various Map objects.
[CustomOverlay Class](../v8-web-control/customoverlay-class.md) | A class that can be used to create custom rendering layers on the map. These can be static overlays such as custom navigation bars, or dynamic overlays such as custom visualization layers. 
[CustomOverlayOptions Object](../v8-web-control/customoverlayoptions-object.md) | Object used to define the settings of a [CustomOverlay](../v8-web-control/customoverlay-class.md).
[Events Class](../v8-web-control/events-class.md) | A static class exposed through the `Microsoft.Maps` namespace that provides an interface for attaching events to the map, pushpins, polylines, polygons, layers and modules.
[GroundOverlay Class](../v8-web-control/groundoverlay-class.md) | A map overlay that binds an image to a bounding box area on the map.
[GroundOverlayOptions Object ](../v8-web-control/groundoverlayoptions-object.md)| The options that specify how to render a ground overlay on the map.
[Heading Enumeration](../v8-web-control/heading-enumeration.md) | Standard compass headings; north, south, east, west.
[Infobox Class](../v8-web-control/infobox-class.md) | Describes the operation of a pop-up user interface.
[InfoboxActions Object](../v8-web-control/infoboxactions-object.md) | Object used to define callback actions for an [Infobox](../v8-web-control/infoboxes.md).
[InfoboxEventArgs Object](../v8-web-control/infoboxeventargs-object.md) | An object that contains information about an infobox event.
[InfoboxOptions Object](../v8-web-control/infoboxoptions-object.md) | Object used to define default settings and options for an [Infobox](../v8-web-control/infoboxes.md).
[IPrimitive Class](../v8-web-control/iprimitive-class.md) | An interface in which pushpins, polylines and polygons are derived from.
[IPrimitiveChangedEventArgs Object](../v8-web-control/iprimitivechangedeventargs-object.md) | An object that is returned when a `changed` event occurs on an [IPrimitive](../v8-web-control/iprimitive-class.md) shape. |
[LabelOverlay Enumeration](../v8-web-control/labeloverlay-enumeration.md) | Defines how map labels are displayed. 
[Layer Class](../v8-web-control/layer-class.md) | An overlay of image-based data on a map.
[LayerCollection Class](../v8-web-control/layercollection-class.md) | A static class that is exposed through the `map.layers` property and allows you to add layers such as; data, heat map, and tile layers.
[Location Class](../v8-web-control/location-class.md) | Represents a geographic location.
[LocationRect Class](../v8-web-control/locationrect-class.md) | Represents a rectangular geographic area.
[Map Class](../v8-web-control/map-class.md)    | Main object for manipulating a view of a map on a page.
[MapOptions Object](../v8-web-control/mapoptions-object.md) | Initial options for configuring a map.
[MapTypeEventArgs Object](../v8-web-control/maptypeeventargs-object.md) | An object is returned by the map event handler when using the `maptypechanged` event.  
[MapTypeId Enumerations](../v8-web-control/maptypeid-enumeration.md) | Various options for configuring the base map visuals.
[ModuleOptions Object](../v8-web-control/moduleoptions-object.md) | Options used for instantiating a [module](../v8-web-control/modular-framework.md).
[MouseEventArgs Object](../v8-web-control/mouseeventargs-object.md) | An object that is returned to event handlers when a mouse event is attached to a map, pushpin, polyline, or polygon. 
[NavigationBarMode Enumeration](../v8-web-control/navigationbarmode-enumeration.md) | Used to customize the layout and style of the navigation bar.  
[NavigationBarOrientation Enumeration](../v8-web-control/navigationbarorientation-enumeration.md) | Define how the navigation bar controls are laid out.
[OverviewMapMode Enumeration](../v8-web-control/overviewmapmode-enumeration.md) | Describes how an overview map mode is displayed on a Streetside-based view.
[PanoramaInfo Object](../v8-web-control/panoramainfo-object.md) | An object tthat contains information about a streetside scene.
[PixelReference Enumeration](../v8-web-control/pixelreference-enumeration.md) | Describes what a pixel-based reference is relative to on the screen.
[Point Object](../v8-web-control/point-class.md) | Represents a pixel coordinate.
[PointCompression Class](../v8-web-control/pointcompression-class.md) | A static class that provides a compression algorithm to encodes/decodes a collection of Location objects into a string and back. This algorithm is used for generating a compressed collection of locations for use with the Bing Maps REST Elevation Service. This algorithm is also used for decoding the compressed coordinates returned by the GeoData API. 
[Polygon Class](../v8-web-control/polygon-class.md) | An enclosed geographic area on a map.
[PolygonOptions Object](../v8-web-control/polygonoptions-object.md) | Initial options for creating a map polygon.
[Polyline Class](../v8-web-control/polyline-class.md) | A line across geographic points on a map.
[PolylineOptions Object](../v8-web-control/polylineoptions-object.md) | Initial options for creating a map polyline. 
[Pushpin Class](../v8-web-control/pushpin-class.md) | A graphical/text representation of a geographic point on a map.
[PushpinOptions Object](../v8-web-control/pushpinoptions-object.md) | A set of options that define a pushpin on a map.
[PyramidTileId Class](../v8-web-control/pyramidtileid-class.md) | Additional information about a tile during a TileSource-related operation.
[Range Object](../v8-web-control/range-object.md) | Used to specify a min and max value range.
[StreetsideOptions Object](../v8-web-control/streetsideoptions-object.md)| Initial options for configuring a Streetside view.
[StylesOptions Object](../v8-web-control/stylesoptions-object.md)| Options for configuring a bulk set of polylines and polygons.
[TestDataGenerator Class](../v8-web-control/testdatagenerator-class.md) | A static class that makes it easy to generate random test data in the form of colors, locations, pushpins, plylines, polygons, and polygons with holes. 
[TileLayer Class](../v8-web-control/tilelayer-class.md) | Represents an overlay of image-based data on a map.
[TileLayerOptions Object](../v8-web-control/tilelayeroptions-object.md) | Options for configuring a tile layer overlay for a map.
[TileSource Class](../v8-web-control/tilesource-class.md) | Represents a source of URLs for a tile layer.
[TileSourceOptions Object](../v8-web-control/tilesourceoptions-object.md) | Options for configuring the source of URLs used to supply a tile layer overlay on a map.
[ViewOptions Object](../v8-web-control/viewoptions-object.md) | Options for configuring a view of the map. 


 