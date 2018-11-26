
---
title: "Create an Optimized Itinerary | Microsoft Docs"
ms.custom: ""
ms.date: "11/26/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 64c43775-3911-4c76-a0b4-32dc5824a258
caps.latest.revision: 4
author: "v-chrfr"
ms.author: "v-chrfr"
manager: "stevelom"
ms.service: "bing-maps"
---

# Create an Optimized Itinerary

The Bing Maps [Optimized Itinerary API](../rest-services/routes/optimized-itinerary.md) returns a delivery schedule for a set of agents and itinerary times. 

This article demonstrates how to use this API with a POST request to create an optimized itinerary for three agents and seven itinerary items.

## Overview

The developer must provide specific information about each agent and itinerary item, summarized by the lists below:

### Agents:

* Name
* Starting Location (Query or Point)
* Ending Locaiton (Query or Point)
* For each shift:
    -- Shift ending time
    -- Shift starting time

### Itinerary Items: 

* Visit duration
* Business opening time
* Business ending time
* Location (Query of Point)
* Priority (on a scale from `1` to `99`, from lowest to highest priority)

...