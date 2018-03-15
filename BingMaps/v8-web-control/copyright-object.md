---
title: "Copyright Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 69999383-1bb3-43a5-be3d-cf4d98d20f7e
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# Copyright Object
Represents the copyright object for a boundary returned by the [GeoData API](../spatial-data-services/geodata-api.md). 

## Properties

Name                   | Type               | Description
---------------------- | ------------------ | ------------
`CopyrightURL`           | string             | The copyright URL for the GeoData service.
`Sources`                | [CopyrightSource](../v8-web-control/copyrightsource-object.md)[] | A collection of [CopyrightSource objects](../v8-web-control/copyrightsource-object.md) that give information about the sources of the polygon data that is returned.

