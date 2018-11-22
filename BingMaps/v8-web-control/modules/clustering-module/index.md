---
title: "Clustering Module | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: fa817aae-7e8c-47db-ad8b-5915a2506d55
caps.latest.revision: 6
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Clustering Module
**Module Name**: Microsoft.Maps.Clustering

**Namespace**: Microsoft.Maps 

Often when adding a lot of pushpins to a map, the map can become cluttered and difficult to read. The performance of the map may also degrade if there is a significant number of pushpins displayed on the map. Clustering is a method where pushpins that are close together are grouped and represented as a single pushpin, often using a different icon to indicate that it is a cluster. These cluster will break apart into their individual pushpins as the user zooms into the map. This is a great way to improve both the user experience and the performance of the map.
 
There are a number of different ways to calculate clusters. Common algorithms that are used for clustering pushpins include grid base, point based, and k-means. Grid based clustering is one of the fastest and can handle the most data, this is what the Clustering module uses. Grid based clustering breaks the map into a grid, and if any two pushpins are in the same grid cell they are clustered together. Once all of the pushpins that are within a grid cell are known, it can then be positioned using a couple of different mechanisms. The most natural way of representing a cluster would be to position it at the average location of all the pushpins it represents. However, by doing this it is possible that if two grid cells have a number of pushpins along a shared edge, clustered pushpins may end up overlapping. A second method would be to simply use the location of the first pushpin in the cluster. This would require no calculation and would align with at least one pushpin in the cluster, but would also have the potential of overlapping of clustered pushpins. By default, the Clustering module uses the mean average position to position a cluster, however you can change this using the `clusterPlacementType` option on the layer.
lustered pushpins.

## API Reference

  * [ClusterLayer Class](clusterlayer-class.md)
  * [ClusterLayerOptions Object](clusterlayeroptions-object.md)
  * [ClusterPlacementType Enumeration](clusterplacementtype-enumeration.md)
  * [ClusterPushpin Class](clusterpushpin-class.md)

## Examples

  * [Basic Clustering Example](../../map-control-concepts/clustering-module-examples/basic-clustering-example.md)
  * [Customizing Clustered Pushpins](../../map-control-concepts/clustering-module-examples/customizing-clustered-pushpins.md)
  * [Clusters with a List and Linking](../../map-control-concepts/clustering-module-examples/clusters-with-a-list-and-linking.md)
  * [Zoom into Clusters](../../map-control-concepts/clustering-module-examples/zoom-into-clusters.md)
