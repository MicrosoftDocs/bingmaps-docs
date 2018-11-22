---
title: "GeoXmlReadOptions Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 922a2fc0-714b-4611-aa9c-3023027a5384
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# GeoXmlReadOptions Object
Options that customize how XML files are read and parsed.

| Name                      | Type                  | Description     |
|---------------------------|-----------------------|-----------------|
| `allowKmlScreenOverlays`  | boolean               | Specifies if KML ScreenOverlays should be read or ignored. Default: **true** |
| `captureGpxPathWaypoints` | boolean               | Specifies whether the individual waypoint data of a GPX Route or Track should be captured. If set to true, the shape will have a metadata.waypoints property that is an array of pushpins that contains the details of each waypoint along the track. Default: **false** |
| `defaultStyles`           | [StylesOptions](../../map-control-api/stylesoptions-object.md)         | The default styles to apply to shapes that don't have a defined style in the XML. |
| `error`                   | function(msg: string) | A callback function that is triggered when an error occurs when reading an XML document.     |
| `ignoreVisibility`        | boolean               | Specifies if shapes visible tags should be used to set the visible property of its equivalent Bing Maps shape. Default: **true** |
| `maxNetworkLinkDepth`     | number                | The maximum depth of network links in a KML file. Default: **3** Example: when set to 3 file1 links to file2 which links to file3 but won't open links in file3. |
| `maxNetworkLinks`         | number                | The maximum number of network links that a single KML file can have. Default: **10**  |
| `setPushpinTitles`        | boolean               | Indicates if the pushpin title should be displayed on the map if a valid title or name value exits in the shapes metadata. Default: **true** |