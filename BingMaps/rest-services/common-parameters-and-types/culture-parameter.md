---
title: "Culture Parameter | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "reference"
ms.assetid: 6b3b4fe0-cb22-4f1e-a02b-e27adcfb0b10
caps.latest.revision: 28
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Culture Parameter

Use the culture parameter to specify a culture for your request. The culture parameter provides the following strings in the language of the culture for:  
  
1. Geographic entities and place names returned by the Bing Maps REST Services  
  
2. Map labels on map images  
  
3. Route instructions  
  
 You can use the alias to shorten the length of the culture parameter.

> For example, `culture=da` can be shortened to `c=da`.  
  
|Parameter|Alias|Description|Values|  
|---------------|-----------|-----------------|------------|  
|`culture`|`c`|**Optional**. The culture to use for the request.|For a list of supported cultures, see [Supported Culture Codes](supported-culture-codes.md).|
  
## Example

 The following example finds the location for an address string and provides the information in German, which is the language associated with the culture code `de`.  

```url
http://dev.virtualearth.net/REST/v1/Locations/Börsenplatz%201%20Frankfurt%20am%20Main%20Hessen%2060313?c=de&key={BingMapsKey}  
```