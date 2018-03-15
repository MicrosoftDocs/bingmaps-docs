---
title: "Modules | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 692dae4a-5fd6-4783-9b45-08844c101e59
caps.latest.revision: 10
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# Modules
The Bing Maps V8 web control use a modular framework as a way to minimize loading of a bunch of features and functionalities that may not be needed. The base map control consists of a number of core features such as support for pushpins, polylines, polygons, and tile layers.  Modules allow users to load only the features and functionalities they need, rather than loading everything up when the application starts. You can save yourself a lot of development time by using modules and avoid reinventing the wheel. 

Within the Bing Maps V8 web control, the following modules are provided:


Name                                   | Description
-------------------------------------- | --------------------- 
[Microsoft.Maps.Autosuggest](../v8-web-control/autosuggest-module.md)             | Provides location based suggestions as you type.
[Microsoft.Maps.Clustering](../v8-web-control/clustering-module.md)              | This module allows you to easily add in client side clustering to your application. Client Side Clustering is a method where pushpins that are close together are grouped and represented as a single pushpin, often using a different icon to indicate the cluster. This is a great way to improve both the user experience and performance of the map.
[Microsoft.Maps.Contour](../v8-web-control/contour-module.md) | This module makes it easy to take contour line data and visualize them on Bing Maps as non-overlapping colored areas.
[Microsoft.Maps.DataBinning](../v8-web-control/data-binning-module.md) | This module provides makes it easy to create data bins from arrays of pushpins and display them on the map. 
[Microsoft.Maps.Directions](../v8-web-control/directions-module.md) | Allows you to calculate a route and display it on the map. The route is draggable by default for easy customization. The instructions will also be nicely formatted.
[Microsoft.Maps.DrawingTools](../v8-web-control/drawing-tools-module.md) | Provides a set of tools for drawing and editing shapes on top of the map.
[Microsoft.Maps.GeoJson](../v8-web-control/geojson-module.md)	               | This module makes it easy to import or export data in GeoJson format.
[Microsoft.Maps.GeoXml](../v8-web-control/geoxml-module.md) | The GeoXml module makes it easy to read and write common geospatial XML file formats such as [KML (Keyhole Markup Language),](https://en.wikipedia.org/wiki/Keyhole_Markup_Language) KMZ (compressed KML), [GeoRSS](https://en.wikipedia.org/wiki/GeoRSS), [GML](https://en.wikipedia.org/wiki/Geography_Markup_Language) (Geography Markup Language, exposed via GeoRSS), and [GPX](https://en.wikipedia.org/wiki/GPS_Exchange_Format) (GPS Exchange Format).
[Microsoft.Maps.HeatMap](../v8-web-control/heat-map-module.md)            | The module allows you to render an array of Location objects as a density based heat map.
[Microsoft.Maps.Search](../v8-web-control/search-module.md)                  | Provides an easy method for geocoding address and reverse geocoding locations from JavaScript.
[Microsoft.Maps.SpatialDataService](../v8-web-control/spatial-data-service-module.md)      | This module wraps the Query and GeoData REST API’s in the Bing Spatial Dara Services and expose them as an easy to use JavaScript library.
[Microsoft.Maps.SpatialMath](../v8-web-control/spatial-math-module.md)             | The module provides a bunch of useful spatial math functions.
[Microsoft.Maps.Traffic](../v8-web-control/traffic-module.md) | Adds a traffic incident and flow data to the map.
[Microsoft.Maps.WellKnownText](../v8-web-control/well-known-text-module.md)           | This module makes it easy to import or export data in Well Known Text format.

You can also [create custom modules](../v8-web-control/creating-custom-modules.md), which is a really great way to promote code reuse. 
