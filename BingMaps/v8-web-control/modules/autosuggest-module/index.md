---
title: "Autosuggest Module | Microsoft Docs"
description: Describes the Autosuggest module, which provides a list of suggested addresses or places, and provides lists of API reference articles and examples.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ebbdff25-ca99-448c-bf06-3530dc03b1eb
caps.latest.revision: 7
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Autosuggest Module

**Module Name**: Microsoft.Maps.Autosuggest

**Namespace**: Microsoft.Maps 

The Autosuggest module takes in a string of text and provides a list of suggested addresses or places that are similar to the provided string of text. This module can be used with a map, or independently on its own. When used with a map instance, the map view can be used to help influence the weight of the suggestions such that they are more relevant to where the user is looking on the map. For instance, if you pass in “London”, the expected top suggestion would “London, UK”, however, when taking the map view into consideration, and if the map is zoomed into Kentucky, the top suggestion may be “London, Kentucky”.

## API Reference

  * [AutosuggestManager Class](autosuggestmanager-class.md)
  * [AutosuggestOptions Object](autosuggestoptions-object.md)
  * [SuggestionResult Object](suggestionresult-object.md)
  * [Address Object](address-object.md)

## Examples
  * [Default Autosuggest User Interface](../../map-control-concepts/autosuggest-module-examples/default-autosuggest-user-interface-example.md)
  * [Filling in an Address Form](../../map-control-concepts/autosuggest-module-examples/filling-in-an-address-form-example.md) 