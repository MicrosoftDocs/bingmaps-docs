---
title: "ClusterLayerOptions Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 36955a77-b4c7-4ac1-8512-3b84a3765a62
caps.latest.revision: 5
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# ClusterLayerOptions Object
The following is a list of properties that are available in the ClusterLayerOptions object.

Name                     | Type                            | Description
------------------------ | ------------------------------- | ------------------------
`callback`               | function()                      | A callback function that is fired after the clustering for a map view has completed. This is useful if you want to generate a list of locations based on what is in the current view.
`clusteredPinCallback`   | function(pin: [ClusterPushpin](clusterpushpin-class.md))   | A callback function that allows you to process a clustered pushpin before it is added to a layer. This is useful if you want to add events or set style options on the clustered pushpin.
`clusteringEnabled`      | boolean                         | Indicates if the layer should cluster the locations or not. Default: **true**
`clusterPlacementType`   | [ClusterPlacementType](clusterplacementtype-enumeration.md)            | Defines how clusters are positioned on the map. Default: **MeanAverage**
`gridSize`               | number                          | The width and height of the gird cells used for clustering in pixels. Default: **45**
`layerOffset`            | Point                           | Offsets the placement of clustered pushpins by a set number of pixels. This option is only available when the placement type is set to GridCenter. This is useful if you have multiple cluster layers on the map and you want to offset the clustered pushpins between the layers so that they are visible, otherwise the clusters from the different layers would overlap completely.
`visible`                | boolean                         | A boolean indicating if the layer is visible or not. 
`zIndex`                 | number	                       | The z-index of the layer. See also: [zIndexing in Bing Maps V8](../../articles/zindexing-in-bing-maps-v8.md) 

