---
title: "GeoXml Class | Microsoft Docs"
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
| read(xml: string *or* ArrayBuffer, options: [GeoXmlReadOptions](../v8-web-control/geoxmlreadoptions-object.md)) | [GeoXmlDataSet](../v8-web-control/geoxmldataset-object.md) | Takes a geospatial XML string or a ArrayBuffer and parses the XML data into Bing Maps shapes. |
| readFromUrl(urlString: string, options: [GeoXmlReadOptions](../v8-web-control/geoxmlreadoptions-object.md), callback: (data: [GeoXmlDataSet](../v8-web-control/geoxmldataset-object.md)) =&gt; void) | | Takes an URL to an XML or zipped XML file and parses the XML data into Bing Maps shapes.      |
| write(shapes: Map *or* ([IPrimitive](../v8-web-control/iprimitive-class.md) *or* [IPrimitive](../v8-web-control/iprimitive-class.md)\[\] *or* [Layer](../v8-web-control/layer-class.md) *or* [GroundOverlay](../v8-web-control/groundoverlay-class.md))\[\] *or* [GeoXmlDataSet](../v8-web-control/geoxmldataset-object.md), options?: [GeoXmlWriteOptions](../v8-web-control/geoxmlwriteoptions-object.md)) | | Writes Bing Maps shape data as a geospatial XML string in the specified format.        |
| writeCompressed(shapes: [Map](../v8-web-control/map-class.md) *or* ([IPrimitive](../v8-web-control/iprimitive-class.md) *or* [IPrimitive](../v8-web-control/iprimitive-class.md)\[\] *or* [Layer](../v8-web-control/layer-class.md) *or* [GroundOverlay](../v8-web-control/groundoverlay-class.md))\[\] *or* [GeoXmlDataSet](../v8-web-control/geoxmldataset-object.md), compressFormat?: [GeoXmlCompressedFormat](../v8-web-control/geoxmlcompressedformat-enumeration.md), options?: GeoXmlWriteOptions) | string *or* ArrayBuffer *or* Blob | Writes Bing Maps shape data to a geospatial XML file embedded in a compressed file.           |
