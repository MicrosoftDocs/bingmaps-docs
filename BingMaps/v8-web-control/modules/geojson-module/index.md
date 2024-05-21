---
title: "GeoJSON Module | Microsoft Docs"
description: Describes the GeoJSON module and provides the an example of a GeoJSON file, the module's static methods, and examples of the module in action.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: e2a05ab1-76ac-4c76-90cc-aa651aa39a0c
caps.latest.revision: 6
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# GeoJSON Module

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../../includes/bing-maps-web-control-sdk-retirement.md)]

**Module Name**: Microsoft.Maps.GeoJson

**Namespace**: Microsoft.Maps.GeoJSON

GeoJSON is a common file format used for storing spatial data as a JSON object. This file format tends to be more compact then its XML equivalents. This results in a much smaller file size, making it ideal for transferring spatial data to web and mobile applications. When storing in a file the **.js** or **.json** file extensions are usually used, however occasionally you may come across some files that use **.geojson**. The following is an example of a GeoJSON file containing the location of New York.

```json
{
    "type": "FeatureCollection",
    "features": [
      {
          "type": "Feature",
          "geometry": {
              "type": "Point",
              "coordinates": [-74.006393, 40.714172]
          },
          "properties": {
              "name": "New York",
              "description": "New York"
          }
      }
    ]
}
```

Additional information on this file format can be found [here](https://tools.ietf.org/html/rfc7946). 

This module allows you to easily read and write GeoJSON data. When reading GeoJSON data, it is parsed into Bing Maps shapes. Specifically, MultiPoint, MultiLineString, MultiPolygon, GeometryCollection and FeatureCollection GeoJSON types are parsed into an array of Bing Maps shapes. To write GeoJSON, simply pass in a Bing Maps shape or array of shapes and the GeoJSON equivalent will be returned.

Supported GeoJSON tags:

  * Point 
  * Linestring
  * Polygon
  * MultiPoint 
  * MultiLinestring 
  * MultiPolygon 
  * Geometrycollection
  * Feature
  * FeatureCollection

The GeoJSON module only has one static class called GeoJson that allows you to read and write GeoJSON data.

In addition to being able to set the default style for shapes when reading a GeoJSON object, any properties on a GeoJSON shape that aligns with one of the names of a Pushpin, Polyline, or Polygon option will automatically be used to in styling that shape. This allows you to define custom styles for individual shapes, directly in your GeoJSON. Here is a list of the supported options:

  * `draggable`: `boolean`
  * `icon`: `string`
  * `visible`: `boolean`
  * `title`: `string`
  * `subTitle`: `string`
  * `enableHoverStyle`: `boolean`
  * `enableClickedStyle`: `boolean`
  * `text`: `string`
  * `color`: `string`
  * `cursor`: `string`
  * `fillColor`: `string`
  * `strokeColor`: `string`
  * `strokeThickness`: `number`
  * `strokeDashArray`: `string` or `number[]`
  * `generalizable`: `boolean`

## Static Methods

The GeoJson class has the following static methods.

Name                                                             | Return Type                  | Description
---------------------------------------------------------------- | ---------------------------- | -----------------------------
read(geoJson: IGeoJsonObject _or_ string, styles?: [StylesOptions](../../map-control-api/stylesoptions-object.md))    | [IPrimitive](../../map-control-api/iprimitive-class.md) _or_ [IPrimitive](../../map-control-api/iprimitive-class.md)[] | Takes in a GeoJSON object or string of GeoJSON data and parses it into Bing Maps shapes (Pushpin, Polyline, Polygon). Default styles can be specified as an option. An array of shapes will be returned if the GeoJSON object is a multipart geometry, such as MultiPoint, MultiLineString, MultiLineString, GeometryCollection or FeatureCollection.
readFromUrl(url: string, callback: function(data: [IPrimitive](../../map-control-api/iprimitive-class.md) _or_ [IPrimitive](../../map-control-api/iprimitive-class.md)[]), jsonpQueryParam?: string, styles?: [StylesOptions](../../map-control-api/stylesoptions-object.md)) | | Takes a URL to GeoJSON file and downloads and parses it into Bing Maps shapes and then returns them through a callback function. If the GeoJSON file is hosted on a different domain, and [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) is not enabled, but does support [JSONP](https://en.wikipedia.org/wiki/JSONP), you will need to specify the name of JSONP URL parameter that can be used to download the file across different domains. Default styles can be specified as an option.
write(data: [IPrimitive](../../map-control-api/iprimitive-class.md) _or_ [IPrimitive](../../map-control-api/iprimitive-class.md)[])                              | IGeoJsonObject               | Takes a Bing Maps shape or array of shapes and converts them into a GeoJSON object. 


## Examples

  * [Read Local GeoJSON Object](../../map-control-concepts/geojson-module-examples/read-local-geojson-object-example.md)
  * [Read GeoJSON using HTML5 FileReader](../../map-control-concepts/geojson-module-examples/read-geojson-using-html5-filereader.md)
  * [Read GeoJSON from the Same Domain](../../map-control-concepts/geojson-module-examples/read-same-domain-geojson-example.md)
  * [Read GeoJSON using JSONP](../../map-control-concepts/geojson-module-examples/read-geojson-from-the-web-using-jsonp-example.md)
  * [Write a Bing Maps Shape as GeoJSON](../../map-control-concepts/geojson-module-examples/write-bing-maps-shape-as-geojson-example.md)
