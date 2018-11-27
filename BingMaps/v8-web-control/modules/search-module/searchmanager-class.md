---
title: "SearchManager Class | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 0dd62d20-e99c-4c44-9e38-fdd4e5e70d6e
caps.latest.revision: 5
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# SearchManager Class

The **SearchManager** class is the primary class used for performing forward and reverse geocode searches in the Search module. 

## Constructor

> SearchManager(map: [Map](map-control-api/map-class.md))

## Methods

The **SearchManager** class has the following methods available:

Name                                          | Description
--------------------------------------------- | ------------------------
geocode(opt: [GeocodeRequestOptions](geocoderequestoptions-object.md))                  | Matches the address or place query in the specified request options to a location and returns the results to the request options callback function.
reverseGeocode(opt: [ReverseGeocodeRequestOptions](reversegeocoderequestoptions-object.md))    | Matches the specified location to an address and returns the address results to the specified request options callback function.
