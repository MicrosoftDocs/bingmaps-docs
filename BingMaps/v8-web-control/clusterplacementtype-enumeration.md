---
title: "ClusterPlacementType Enumeration | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: e388a20a-d702-4ab0-b292-d42a80d9cca2
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# ClusterPlacementType Enumeration
The `Microsoft.Maps.ClusterPlacementType` enumeration values can be used to specify how a clustered pushpin should be positioned.

Name                 | Description
-------------------- | ----------------------
`MeanAverage`        | Mean Average placement calculates the average position of a group of coordinates. This method creates a more realistic representation of the data, however requires more processing power and increases the chances of pushpins overlapping.
`FirstLocation`      | This method is the simplest way to represent a cluster. It places the cluster at the first location in the cluster. This method may not accurately represent the data but requires little processing power.

