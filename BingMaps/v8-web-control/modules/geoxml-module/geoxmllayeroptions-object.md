---
title: "GeoXmlLayerOptions Object | Microsoft Docs"
description: Describes the GeoXmlLayerOptions object, used to customize how a GeoXmlLayer renders, with a description of each available property.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 9758b057-bb64-4bdc-8230-5f230c93a8a7
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# GeoXmlLayerOptions Object

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../../includes/bing-maps-web-control-sdk-retirement.md)]

Options used to customize how a GeoXmlLayer renders.

| Name                      | Type                  | Description   |
|---------------------------|-----------------------|---------------|
| `allowKmlScreenOverlays`  | boolean               | Specifies if KML ScreenOverlays should be read or ignored. Default: **true**                              |
| `autoUpdateMapView`       | boolean               | A boolean indicating if the map should automatically update the view when a data set is loaded. Default: **true**   |
| `captureGpxPathWaypoints` | boolean               | Specifies whether the individual waypoint data of a GPX Route or Track should be captured. If set to true, the shape will have a metadata.waypoints property that is an array of pushpins that contains the details of each waypoint along the track. Default: **false** |
| `defaultStyles`           | [StylesOptions](../../map-control-api/stylesoptions-object.md)         | The default styles to apply to shapes that don't have a defined style in the XML. |
| `error`                   | function(msg: string) | A callback function that is triggered when an error occurs when reading an XML document.  |
| `ignoreVisibility`        | boolean               | Specifies if shapes visible tags should be used to set the visible property of its equivalent Bing Maps shape. Default: **true** |
| `infoboxOptions`          | [InfoboxOptions](../../map-control-api/infoboxoptions-object.md)        | Options used to customize how the default infobox renders. |
| `layerName` | string | An optional name to identify the layer by. |
| `maxNetworkLinkDepth`     | number                | The maximum depth of network links in a KML file. Default: **3** Example: when set to 3 file1 links to file2 which links to file3 but won't open links in file3. |
| `maxNetworkLinks`         | number                | The maximum number of network links that a single KML file can have. Default: **10** |
| `setPushpinTitles`        | boolean               | Indicates if the pushpin title should be displayed on the map if a valid title or name value exits in the shapes metadata. Default: **true** |
| `suppressInfoboxes`       | boolean               | A boolean indicating if infoboxes should automatically appear when shapes clicked. Default: **false** |
| `visible`                 | boolean               | A boolean indicating if the layer is visible or not. Default: **true**   |
