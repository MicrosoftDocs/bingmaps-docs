---
title: "StylesOptions Object | Microsoft Docs"
description: "Describes the StylesOptions object and provides the object's properties and an example of the object's syntax."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 4d37e132-5241-4d0c-8280-9b54681ec305
caps.latest.revision: 5
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# StylesOptions Object

Setting the options for an individual shape is easy to do. However, sometimes you need to load a collection of shapes from a module.  To set the style for these, one option would be to loop through each shape and set the style for that shape individually.  This means writing extra code and looping through all of the entities in your high-volume data. To make it easier to set the default styles for loaded entities, many of the modules allow you to pass in an StylesOptions object. Some of the modules that support this include [GeoJSON](../modules/geojson-module/index.md), [Well Known Text](../modules/well-known-text-module.md), and the [Spatial Data Services](../modules/spatial-data-service-module/index.md) modules.

## Properties

This IStylesOptions object has the following properties.

Name                 | Type               | Description
-------------------- | ------------------ | ---------------------------------
`pushpinOptions`     | [PushpinOptions](pushpinoptions-object.md)    | Sets the options for all pushpins.
`polylineOptions`    | [PolylineOptions](polylineoptions-object.md)   | Sets the options for all polylines.
`polygonOptions`     | [PolygonOptions](polygonoptions-object.md)    | Sets the options for all polygons.

## Example

```javascript
var style = {
    pushpinOptions: {
        color: 'pink'
    },
    polylineOptions: {
        strokeColor: 'green'
    },
    polygonOptions: {
        fillColor: 'red',
        strokeColor: 'blue'
    }
};
```