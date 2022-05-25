---
title: "GeoXml Class | Microsoft Docs"
description: Describes the GeoXml class, which exposes geospatial XML reading and writing static methods, and provides a list of the stat methods.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 7d4bb2c6-796c-4387-b48d-2698ca611131
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# GeoXml Class

This class exposes static methods for reading and writing geospatial XML data.

## Static Methods

|Name  | Return Type                       | Description                                                                                   |
|------|-----------------------------------|-----------------------------------------------------------------------------------------------|
| read(xml: string *or* ArrayBuffer, options: [GeoXmlReadOptions](geoxmlreadoptions-object.md)) | [GeoXmlDataSet](geoxmldataset-object.md) | Takes a geospatial XML string or a ArrayBuffer and parses the XML data into Bing Maps shapes. |
| readFromUrl(urlString: string, options: [GeoXmlReadOptions](geoxmlreadoptions-object.md), callback: (data: [GeoXmlDataSet](geoxmldataset-object.md)) =&gt; void) | | Takes an URL to an XML or zipped XML file and parses the XML data into Bing Maps shapes.      |
| write(shapes: Map *or* ([IPrimitive](../../map-control-api/iprimitive-class.md) *or* [IPrimitive](../../map-control-api/iprimitive-class.md)\[\] *or* [Layer](../../map-control-api/layer-class.md) *or* [GroundOverlay](../../map-control-api/groundoverlay-class.md))\[\] *or* [GeoXmlDataSet](geoxmldataset-object.md), options?: [GeoXmlWriteOptions](geoxmlwriteoptions-object.md)) | | Writes Bing Maps shape data as a geospatial XML string in the specified format.        |
| writeCompressed(shapes: [Map](../../map-control-api/map-class.md) *or* ([IPrimitive](../../map-control-api/iprimitive-class.md) *or* [IPrimitive](../../map-control-api/iprimitive-class.md)\[\] *or* [Layer](../../map-control-api/layer-class.md) *or* [GroundOverlay](../../map-control-api/groundoverlay-class.md))\[\] *or* [GeoXmlDataSet](geoxmldataset-object.md), compressFormat?: [GeoXmlCompressedFormat](geoxmlcompressedformat-enumeration.md), options?: GeoXmlWriteOptions) | string *or* ArrayBuffer *or* Blob | Writes Bing Maps shape data to a geospatial XML file embedded in a compressed file.           |
