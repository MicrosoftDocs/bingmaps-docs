---
title: "Data Binning Module Examples | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: e5d03a2e-a99a-4ec0-a3f3-5dce56b3b1a8
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Data Binning Module Examples
Data binning, is the process of grouping point data into a symmetric gird of geometric shapes. An aggregate value can then be calculated from the pins in a bin and used to set the color or scale the of that bin to provide a visual representation of a data metric the bin contains. The two most common shapes used in data binning are squares and hexagons. When hexagons are used, this process is also referred to as hex binning. The data binning module provides a [DataBinningLayer](../v8-web-control/databinninglayer-class.md) class which makes it easy to create data bins from arrays of pushpins. The generated data bins extend from the polygon class and support all polygon options and events.

## Examples

* [Data Binning Layer Events](../v8-web-control/data-binning-layer-events.md)
* [Bivariant Data Binning](../v8-web-control/bivariant-data-binning.md)
* [Color Scale Gradient Data Bins](../v8-web-control/color-scale-gradient-data-bins.md)

## Related Topics

* [DataBinningLayer Class](../v8-web-control/databinninglayer-class.md)
* [DataBinningLayerOptions Object](../v8-web-control/databinningoptions-object.md)
* [DataBinInfo Object](../v8-web-control/databininfo-object.md)
* [DataBinMetric Object](../v8-web-control/databinmetrics-object.md)
* [DataBinPolygon Class](../v8-web-control/databinpolygon-class.md)
* [DataBinType Enumeration](../v8-web-control/databintype-enumeration.md) 