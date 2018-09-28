---
title: "Autosuggest Module Examples | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 517c0fc6-a075-4d69-8600-335fe41f44dd
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Autosuggest Module Examples
The **Autosuggest** module takes in a string of text and provides a list of suggested addresses or places that are similar to the provided string of text. This module can be used with a map, or independently on its own. When used with a map instance, the map view can be used to help influence the weight of the suggestions such that they are more relevant to where the user is looking on the map. For instance, if you pass in “London”, the expected top suggestion would “London, UK”, however, when taking the map view into consideration, and if the map is zoomed into Kentucky, the top suggestion may be “London, Kentucky”.

## Examples

  * [Default Autosuggest User Interface](../v8-web-control/default-autosuggest-user-interface-example.md)
  * [Filling in an Address Form](../v8-web-control/filling-in-an-address-form-example.md)  

## Related Topics

  * [AutosuggestManager Class](../v8-web-control/autosuggestmanager-class.md)
  * [AutosuggestOptions Object](../v8-web-control/autosuggestoptions-object.md)
  * [SuggestionResult Object](../v8-web-control/suggestionresult-object.md)
  * [Address Object](../v8-web-control/address-object.md)
