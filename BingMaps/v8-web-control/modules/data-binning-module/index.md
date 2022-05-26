---
title: "Data Binning Module | Microsoft Docs"
description: Describes the data binning module and provides API reference documentation and links to code examples.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 7b42e3f0-ad3a-49b4-b171-faaac3ebbc05
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Data Binning Module

**Namespace**: Microsoft.Maps

**Module Name**: Microsoft.Maps.DataBinning

Data binning, is the process of grouping point data into a symmetric grid of geometric shapes. An aggregate value can then be calculated from the pins in a bin and used to set the color or scale the of that bin to provide a visual representation of a data metric the bin contains. The two most common shapes used in data binning are squares and hexagons. When hexagons are used, this process is also referred to as hex binning. The data binning module provides a [DataBinningLayer](databinninglayer-class.md) class which makes it easy to create data bins from arrays of pushpins. The generated data bins extend from the polygon class and support all polygon options and events.


## API Reference

* [DataBinningLayer Class](databinninglayer-class.md)
* [DataBinningLayerOptions Object](databinningoptions-object.md)
* [DataBinInfo Object](databininfo-object.md)
* [DataBinMetric Object](databinmetrics-object.md)
* [DataBinPolygon Class](databinpolygon-class.md)
* [DataBinType Enumeration](databintype-enumeration.md) 

## Examples

* [Data Binning Layer Events](../../map-control-concepts/data-binning-module-examples/data-binning-layer-events.md)
* [Bivariant Data Binning](../../map-control-concepts/data-binning-module-examples/bivariant-data-binning.md)
* [Color Scale Gradient Data Bins](../../map-control-concepts/data-binning-module-examples/color-scale-gradient-data-bins.md)
