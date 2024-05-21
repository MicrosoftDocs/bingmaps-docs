---
title: "Data Binning Module Examples | Microsoft Docs"
description: Describes the Data Binning module, which handles the data binning process, and provides lists of code examples and related topics.
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

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../includes/bing-maps-web-control-sdk-retirement.md)]

Data binning, is the process of grouping point data into a symmetric gird of geometric shapes. An aggregate value can then be calculated from the pins in a bin and used to set the color or scale the of that bin to provide a visual representation of a data metric the bin contains. The two most common shapes used in data binning are squares and hexagons. When hexagons are used, this process is also referred to as hex binning. The data binning module provides a [DataBinningLayer](../../modules/data-binning-module/databinninglayer-class.md) class which makes it easy to create data bins from arrays of pushpins. The generated data bins extend from the polygon class and support all polygon options and events.

## Examples

* [Data Binning Layer Events](data-binning-layer-events.md)
* [Bivariant Data Binning](bivariant-data-binning.md)
* [Color Scale Gradient Data Bins](color-scale-gradient-data-bins.md)

## Related Topics

* [DataBinningLayer Class](../../modules/data-binning-module/databinninglayer-class.md)
* [DataBinningLayerOptions Object](../../modules/data-binning-module/databinningoptions-object.md)
* [DataBinInfo Object](../../modules/data-binning-module/databininfo-object.md)
* [DataBinMetric Object](../../modules/data-binning-module/databinmetrics-object.md)
* [DataBinPolygon Class](../../modules/data-binning-module/databinpolygon-class.md)
* [DataBinType Enumeration](../../modules/data-binning-module/databintype-enumeration.md) 