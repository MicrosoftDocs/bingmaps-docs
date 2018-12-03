---
title: "GeoXml Module | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: b72263a6-08e2-4f83-97a8-aff3db27ae8e
caps.latest.revision: 7
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# GeoXml Module
**Module name**: Microsoft.Maps.GeoXml

**Namespace**: Microsoft.Maps

The GeoXml module makes it easy to read and write common geospatial XML file formats such as [KML (Keyhole Markup Language),](https://en.wikipedia.org/wiki/Keyhole_Markup_Language) KMZ (compressed KML), [GeoRSS](https://en.wikipedia.org/wiki/GeoRSS), [GML](https://en.wikipedia.org/wiki/Geography_Markup_Language) (Geography Markup Language, exposed via GeoRSS), and [GPX](https://en.wikipedia.org/wiki/GPS_Exchange_Format) (GPS Exchange Format).

There are two ways to make use of this module. The first is to use the static methods in the [GeoXml class](geoxml-class.md) to read/write the raw data. This gives you full control over the data and how it is rendered, if you choose to render it. The second option is to use the [GeoXmlLayer](geoxmllayer-class.md) which handles the importing of the XML data and generates a data layer which you can add to the map like any other layer. It handles all the rendering for you. This is a quick and easy way to get your geospatial XML data on the map with as little as 3 lines of code.

> [!TIP]
> If GeoJSON data is passed into the [GeoXmlLayer](geoxmllayer-class.md) or the read functions of the [GeoXml class](geoxml-class.md), it will automatically load the [GeoJSON module](../geojson-module/index.md) and read the data.

## API Reference

* [GeoXml Class](geoxml-class.md)
* [GeoXmlCompressedFormat Enumeration](geoxmlcompressedformat-enumeration.md)
* [GeoXmlDataSet Object](geoxmldataset-object.md)
* [GeoXmlFormat Enumeration](geoxmlformat-enumeration.md)
* [GeoXmlLayer Class](geoxmllayer-class.md)
* [GeoXmlLayerOptions Object](geoxmllayeroptions-object.md)
* [GeoXmlReadOptions Object](geoxmlreadoptions-object.md)
* [GeoXmlStats Object](geoxmlstats-object.md)
* [GeoXmlSummaryMetadata Object](geoxmlsummarymetadata-object.md)
* [GeoXmlWriteOptions Object](geoxmlwriteoptions-object.md)
* [KmlScreenOverlay Class](kmlscreenoverlay-class.md)
* [KmlScreenOverlayOptions Object](kmlscreenoverlayoptions-object.md)

## Examples

 * [Read Geospatial XML String](../../map-control-concepts/geoxml-module-examples/read-geospatial-xml-string.md)
 * [Read Geospatial XML from URL](../../map-control-concepts/geoxml-module-examples/read-geospatial-xml-from-url.md)
 * [Read GeoXmlLayer with XML String](../../map-control-concepts/geoxml-module-examples/read-geoxmllayer-with-xml-string.md)
 * [Read Geospatial XML Files from Same Domain](../../map-control-concepts/geoxml-module-examples/read-geospatial-xml-files-from-same-domain.md)
 * [Reading Geospatial XML Files Cross Domain](../../map-control-concepts/geoxml-module-examples/reading-geospatial-xml-files-cross-domain.md)
 * [Writing Geospatial XML data](../../map-control-concepts/geoxml-module-examples/writing-geospatial-xml-data.md)

## Supported Namespaces

The GeoXml module supports XML tags from the following namespaces.

| Namespace Prefix | Namespace URI   | Notes                                                                    |
|------------------|-----------------|--------------------------------------------------------------------------|
| `atom`             | `http://www.w3.org/2005/Atom`   |                                                        |
| `geo`              | `http://www.w3.org/2003/01/geo/wgs84_pos#`  | Read only support in GeoRSS files.       |
| `georss`           | `http://www.georss.org/georss`  |                                                        |
| `geourl`           | `http://geourl.org/rss/module/` | Read only support in GeoRSS files.                     |
| `gml`              | `http://www.opengis.net/gml`    | GML is supported when included in GeoRSS documents.    |
| `gpx`              | `http://www.topografix.com/GPX/1/1` |                                                    |
| `kml`              | `http://www.opengis.net/kml/2.2`    |                                                    |
| `mappoint`         | `http://virtualearth.msn.com/apis/annotate#`  | Read only support in GeoRSS files.      |
| `rss`              |                                 | Read only. GeoRSS writes using Atom format.            |
| `gpxx`             | `http://www.garmin.com/xmlschemas/GpxExtensions/v3` | Read only support in GPX files. Parses and uses DisplayColor. All other properties added to shape metadata. |
| `gpx_style`       | `http://www.topografix.com/GPX/gpx_style/0/2`      | Supported in GPX files. Uses line color. |

## Supported XML Elements

The GeoXml module supports the following XML elements. Any XML tags that are not supported will be converted into a JSON object and added to the metadata property of the parent shape or layer.

### KML Elements

The GeoXml module supports the following KML elements.

| Element Name         | Read    | Write   | Notes                                                                                                                      |
|----------------------|---------|---------|----------------------------------------------------------------------------------------------------------------------------|
| `address`            | partial | yes     | Object is parsed but is not used for positioning shape.                                                                    |
| `AddressDetails`     | partial | no      | Object is parsed but is not used for positioning shape.                                                                    |
| `atom:author`        | yes     | yes     |                                                                                                                            |
| `atom:link`          | yes     | yes     |                                                                                                                            |
| `atom:name`          | yes     | yes     |                                                                                                                            |
| `BalloonStyle`       | partial | yes     | Only supports `text` and `textColor`. Exposed through a balloonStyle and balloonDescription metadata property.             |
| `begin`              | yes     | yes     |                                                                                                                            |
| `color`              | yes     | yes     | Includes \#AABBGGRR and \#BBGGRR                                                                                           |
| `coordinates`        | yes     | yes     |                                                                                                                            |
| `Data`               | yes     | yes     |                                                                                                                            |
| `description`        | yes     | yes     |                                                                                                                            |
| `displayName`        | yes     | yes     |                                                                                                                            |
| `Document`           | yes     | yes     |                                                                                                                            |
| `east`               | yes     | yes     |                                                                                                                            |
| `end`                | yes     | yes     |                                                                                                                            |
| `ExtendedData`       | yes     | yes     | Supports untyped `Data`, `SimpleData` or `Schema`, and entity replacements of the form `$[dataName]`.                      |
| `fill`               | yes     | yes     |                                                                                                                            |
| `Folder`             | yes     | yes     |                                                                                                                            |
| `GroundOverlay`      | yes     | yes     | `drawOrder` not supported                                                                                                  |
| `heading`            | no      | no      |                                                                                                                            |
| `hotSpot`            | no | partial     | Only `pixel` units supported and is relative to the top left corner of the icon.                                                                                              |
| `href`               | yes     | yes     |                                                                                                                            |
| `Icon`               | partial | partial | Only `href` supported.                                                                                                     |
| `IconStyle`          | partial | partial | No support for `scale`, `heading`, `colorMode`, or fractional `hotspots`.                                                  |
| `innerBoundaryIs`    | yes     | yes     |                                                                                                                            |
| `kml`                | yes     | yes     |                                                                                                                            |
| `LabelStyle`         | no      | no      |                                                                                                                            |
| `LatLonBox`          | yes     | yes     |                                                                                                                            |
| `LinearRing`         | yes     | yes     |                                                                                                                            |
| `LineString`         | yes     | yes     |                                                                                                                            |
| `LineStyle`          | yes     | yes     | `colorMode` not supported.                                                                                                 |
| `Link`               | yes     | no      | Only the `href` property is supported for network links.                                                                   |
| `MultiGeometry`      | yes     | yes     |                                                                                                                            |
| `name`               | yes     | yes     |                                                                                                                            |
| `NetworkLink`        | yes     | no      | Links need to be on same domain as the document.                                                                           |
| `NetworkLinkControl` | no      | no      |                                                                                                                            |
| `north`              | yes     | yes     |                                                                                                                            |
| `open`               | yes     | yes     |                                                                                                                            |
| `outerBoundaryIs`    | yes     | yes     |                                                                                                                            |
| `outline`            | yes     | yes     |                                                                                                                            |
| `overlayXY`          | yes     | no      |                                                                                                                            |
| `Pair`               | partial | no      | Only the normal style in a `StyleMap` is supported.                                                                        |
| `phoneNumber`        | yes     | yes     |                                                                                                                            |
| `PhotoOverlay`       | no      | no      |                                                                                                                            |
| `Placemark`          | yes     | yes     |                                                                                                                            |
| `Point`              | yes     | yes     |                                                                                                                            |
| `Polygon`            | yes     | yes     |                                                                                                                            |
| `PolyStyle`          | yes     | yes     |                                                                                                                            |
| `Region`             | partial | partial | Region `LatLongBox` only supported at document level.                                                                      |
| `rotation`           | yes     | yes     |                                                                                                                            |
| `rotationXY`         | yes     | no      |                                                                                                                            |
| `scale`              | no      | no      |                                                                                                                            |
| `Schema`             | yes     | yes     |                                                                                                                            |
| `SchemaData`         | yes     | yes     |                                                                                                                            |
| `schemaUrl`          | partial | yes     | Does not support loading styles from external documents that are not included inside of a KMZ.                             |
| `ScreenOverlay`      | yes     | no      |                                                                                                                            |
| `screenXY`           | yes     | no      |                                                                                                                            |
| `SimpleData`         | yes     | yes     |                                                                                                                            |
| `SimpleField`        | yes     | yes     |                                                                                                                            |
| `size`               | yes     | no      |                                                                                                                            |
| `Snippet`            | partial | partial | `maxLines` attribute ignored.                                                                                              |
| `south`              | yes     | yes     |                                                                                                                            |
| `Style`              | yes     | yes     |                                                                                                                            |
| `StyleMap`           | partial | no      | Only the normal style in a `StyleMap` is supported.                                                                        |
| `styleUrl`           | partial | yes     | External style URL's not supported.                                                                                        |
| `text`               | yes     | yes     | Replacement of `$[geDirections]` is not supported                                                                          |
| `textColor`          | yes     | yes     |                                                                                                                            |
| `TimeSpan`           | yes     | yes     |                                                                                                                            |
| `TimeStamp`          | yes     | yes     |                                                                                                                            |
| `value`              | yes     | yes     |                                                                                                                            |
| `visibility`         | yes     | yes     |                                                                                                                            |
| `west`               | yes     | yes     |                                                                                                                            |
| `when`               | yes     | yes     |                                                                                                                            |
| `width`              | yes     | yes     |                                                                                                                            |

### GeoRSS Elements

The GeoXml module supports the following GeoRSS elements.

| Element Name             | Read    | Write | Notes                                                                                          |
|--------------------------|---------|-------|------------------------------------------------------------------------------------------------|
| `atom:author`            | yes     | yes   |                                                                                                |
| `atom:category`          | yes     | yes   |                                                                                                |
| `atom:content`           | yes     | yes   |                                                                                                |
| `atom:contributor`       | yes     | yes   |                                                                                                |
| `atom:email`             | yes     | yes   |                                                                                                |
| `atom:entry`             | yes     | yes   |                                                                                                |
| `atom:feed`              | yes     | yes   |                                                                                                |
| `atom:generator`         | yes     | no    |                                                                                                |
| `atom:icon`              | yes     | yes   |                                                                                                |
| `atom:id`                | yes     | yes   |                                                                                                |
| `atom:link`              | yes     | yes   |                                                                                                |
| `atom:logo`              | yes     | yes   |                                                                                                |
| `atom:name`              | yes     | yes   |                                                                                                |
| `atom:published`         | yes     | yes   |                                                                                                |
| `atom:rights`            | yes     | yes   |                                                                                                |
| `atom:source`            | yes     | yes   |                                                                                                |
| `atom:subtitle`          | yes     | yes   |                                                                                                |
| `atom:summary`           | yes     | yes   |                                                                                                |
| `atom:title`             | yes     | yes   |                                                                                                |
| `atom:updated`           | yes     | yes   |                                                                                                |
| `atom:uri`               | yes     | yes   |                                                                                                |
| `geo:lat`                | yes     | no    | Written as a `georss:point`.                                                                   |
| `geo:lon`                | yes     | no    | Written as a `georss:point`.                                                                   |
| `geo:long`               | yes     | no    | Written as a `georss:point`.                                                                   |
| `georss:box`             | partial | no    | When read, converted into a polygon.                                                           |
| `georss:circle`          | partial | no    | When read, converted into a polygon.                                                           |
| `georss:elev`            | yes     | yes   |                                                                                                |
| `georss:featurename`     | yes     | yes   |                                                                                                |
| `georss:featuretypetag`  | yes     | yes   |                                                                                                |
| `georss:floor`           | yes     | yes   |                                                                                                |
| `georss:line`            | yes     | yes   |                                                                                                |
| `georss:point`           | yes     | yes   |                                                                                                |
| `georss:polygon`         | yes     | yes   |                                                                                                |
| `georss:radius`          | yes     | yes   |                                                                                                |
| `georss:relationshiptag` | yes     | yes   |                                                                                                |
| `georss:where`           | yes     | yes   |                                                                                                |
| `geourl:latitude`        | yes     | no    | Written as a `georss:point`.                                                                   |
| `geourl:longitude`       | yes     | no    | Written as a `georss:point`.                                                                   |
| `mappoint:icon`          | yes     | no    | Written as an `atom:icon`.                                                                       |
| `position`               | yes     | no    | Some XML feeds will wrap GML with a position tag instead of with a georss:where tag. Will read this, but will write using a georss:where tag. |
| `rss`                    | yes     | no    | GeoRSS written in ATOM format.                                                                 |
| `rss:author`             | yes     | partial | Written as an `atom:author`.                                                                 |
| `rss:category`           | yes     | partial | Written as an `atom:category`.                                                               |
| `rss:channel`            | yes     | no    |                                                                                                |
| `rss:cloud`              | yes     | no    |                                                                                                |
| `rss:comments`           | yes     | no    |                                                                                                |
| `rss:copyright`          | yes     | partial | Written as an `atom:rights` if shape doesn't have an rights metadata property already.       |
| `rss:description`        | yes     | partial | Written as an `atom:content` if shape doesn't have a content metadata property already.      |
| `rss:docs`               | yes     | no    |                                                                                                |
| `rss:enclosure`          | yes     | no    |                                                                                                |
| `rss:generator`          | yes     | no    |                                                                                                |
| `rss:guid`               | yes     | partial | Written as an `atom:id` if shape doesn't have an id metadata property already.               |
| `rss:image`              | yes     | partial | Written as an `atom:logo` if shape doesn't have a logo metadata property already.            |
| `rss:item`               | yes     | partial | Written as an `atom:entry`.                                                                  |
| `rss:language`           | yes     | no    |                                                                                                |
| `rss:lastBuildDate`      | yes     | partial | Written as an `atom:updated` if shape doesn't have an updated metadata property already.     |
| `rss:link`               | yes     | partial | Written as an `atom:link`.                                                                   |
| `rss:managingEditor`     | yes     | partial | Written as an `atom:contributor`.                                                            |
| `rss:pubDate`            | yes     | partial | Written as an `atom:published` if shape doesn't have a published metadata property already.  |
| `rss:rating`             | yes     | no    |                                                                                                |
| `rss:skipDays`           | yes     | no    |                                                                                                |
| `rss:skipHours`          | yes     | no    |                                                                                                |
| `rss:source`             | yes     | partial | Written as an `atom:source` containing an `atom:link`.                                       |
| `rss:textInput`          | yes     | no    |                                                                                                |
| `rss:title`              | yes     | partial | Written as an `atom:title`.                                                                  |
| `rss:ttl`                | yes     | no    |                                                                                                |
| `rss:webMaster`          | yes     | no    |                                                                                                |

### GML Elements

The GeoXml module supports the following GML elements. GML is supported when included in GeoRSS documents.

| Element Name            | Read | Write | Notes                                                                                  |
|-------------------------|------|-------|----------------------------------------------------------------------------------------|
| `gml:coordinates`       | yes  | no    | Written using `gml:posList`.                                                           |
| `gml:exterior`          | yes  | yes   |                                                                                        |
| `gml:Feature`           | yes  | no    | Written as a shape.                                                                    |
| `gml:FeatureCollection` | yes  | no    | Written as a geometry collection.                                                      |
| `gml:featureMember`     | yes  | no    | Written as a geometry collection.                                                      |
| `gml:geometry`          | yes  | no    | Written as a shape.                                                                    |
| `gml:geometryMember`    | yes  | yes   |                                                                                        |
| `gml:innerBoundaryIs`   | yes  | no    | Written using `gml.interior`.                                                          |
| `gml:interior`          | yes  | yes   |                                                                                        |
| `gml:LinearRing`        | yes  | yes   |                                                                                        |
| `gml:LineString`        | yes  | yes   |                                                                                        |
| `gml:lineStringMember`  | yes  | yes   |                                                                                        |
| `gml:MultiGeometry`     | yes  | yes   |                                                                                        |
| `gml:MultiLineString`   | yes  | yes   |                                                                                        |
| `gml:MultiPoint`        | yes  | yes   |                                                                                        |
| `gml:MultiPolygon`      | yes  | yes   |                                                                                        |
| `gml:outerBoundaryIs`   | yes  | no    | Written using `gml.exterior`.                                                          |
| `gml:Point`             | yes  | yes   |                                                                                        |
| `gml:pointMember`       | yes  | yes   |                                                                                        |
| `gml:Polygon`           | yes  | yes   |                                                                                        |
| `gml:polygonMember`     | yes  | yes   |                                                                                        |
| `gml:pos`               | yes  | yes   | Reads coordinates that are in WGS84 decimal degrees format. Writes with `dimension="2"`. |
| `gml:posList`           | yes  | yes   | Reads coordinates that are in WGS84 decimal degrees format. Writes with `dimension="2"`. |

### GPX Elements

The GeoXml module supports the following GPX elements.

| Element Name             | Read    | Write   | Notes                                                                                       |
|--------------------------|---------|---------|---------------------------------------------------------------------------------------------|
| `gpx:ageofdgpsdata`      | yes     | yes     |                                                                                             |
| `gpx:author`             | yes     | yes     |                                                                                             |
| `gpx:bounds`             | yes     | yes     | Converted into a LocationRect when read.                                                    |
| `gpx:cmt`                | yes     | yes     |                                                                                             |
| `gpx:copyright`          | yes     | yes     |                                                                                             |
| `gpx:desc`               | yes     | yes     | Copied into a description property when read to align with other XML formats.               |
| `gpx:dgpsid`             | yes     | yes     |                                                                                             |
| `gpx:ele`                | yes     | yes     |                                                                                             |
| `gpx:extensions`         | partial | partial | When read, style information extracted. All other extensions flattened into a simple JSON object. Only shape style information is written. |
| `gpx:geoidheight`        | yes     | yes     |                                                                                             |
| `gpx:gpx`                | yes     | yes     |                                                                                             |
| `gpx:hdop`               | yes     | yes     |                                                                                             |
| `gpx:link`               | yes     | yes     |                                                                                             |
| `gpx:magvar`             | yes     | yes     |                                                                                             |
| `gpx:metadata`           | yes     | yes     |                                                                                             |
| `gpx:name`               | yes     | yes     |                                                                                             |
| `gpx:pdop`               | yes     | yes     |                                                                                             |
| `gpx:rte`                | yes     | yes     |                                                                                             |
| `gpx:rtept`              | yes     | yes     |                                                                                             |
| `gpx:sat`                | yes     | yes     |                                                                                             |
| `gpx:src`                | yes     | yes     |                                                                                             |
| `gpx:sym`                | yes     | yes     | Value is captured, but is not used to alter the pushpin icon.                               |
| `gpx:text`               | yes     | yes     |                                                                                             |
| `gpx:time`               | yes     | yes     |                                                                                             |
| `gpx:trk`                | yes     | yes     |                                                                                             |
| `gpx:trkpt`              | yes     | yes     |                                                                                             |
| `gpx:trkseg`             | yes     | yes     |                                                                                             |
| `gpx:type`               | yes     | yes     |                                                                                             |
| `gpx:vdop`               | yes     | yes     |                                                                                             |
| `gpx:wpt`                | yes     | yes     |                                                                                             |
| `gpx_style:color`        | yes     | yes     |                                                                                             |
| `gpx_style:line`         | partial | partial | `color`, `opacity` and `width` supported.                                                   |
| `gpx_style:opacity`      | yes     | yes     |                                                                                             |
| `gpx_style:width`        | partial | partial | If value is less than or equal to 1, will be multiplied by 5 and rounded.                   |
| `gpxx:DisplayColor`      | yes     | no      | Used to specify the color of a shape. When writing, line color will be used instead.        |
| `gpxx:RouteExtension`    | partial | no      | All properties are read into metadata. Only `DisplayColor` is used.                         |
| `gpxx:TrackExtension`    | partial | no      | All properties are read into metadata. Only `DisplayColor` is used.                         |
| `gpxx:WaypointExtension` | partial | no      | All properties are read into metadata. Only `DisplayColor` is used.                         |
| `gpx:keywords`           | yes     | yes     |                                                                                             |
| `gpx:fix`                | yes     | yes     |                                                                                             |
