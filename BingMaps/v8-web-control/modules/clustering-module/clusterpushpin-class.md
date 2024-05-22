---
title: "ClusterPushpin Class | Microsoft Docs"
description: Describes the ClusterPushpin class, which extends the Pushpin class, and provides descriptions for each of its properties.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 1fff4a95-5869-4617-9909-8be022ed3d59
caps.latest.revision: 5
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# ClusterPushpin Class

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../../includes/bing-maps-web-control-sdk-retirement.md)]

This class extends the Pushpin class and has all the same methods and properties plus the following properties.

## Properties

Name                  | Type          | Description
--------------------- | ------------- | ------------------------------------
`containedPushpins`   | [Pushpin](../../map-control-api/pushpin-class.md)[]     | An array of all the pushpins that are in the cluster.
`gridKey`             | number        | The grid cell key that can be used retrieve the clustered pushpin(s) from the clustering layer. This is useful when creating a clickable list that link items in the list to clusters or pushpins on the map. Your list just needs to store the `gridKey` value.
