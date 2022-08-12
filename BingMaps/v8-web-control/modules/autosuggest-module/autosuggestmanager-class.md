---
title: "AutosuggestManager Class | Microsoft Docs"
description: Describes the AutosuggestManager class, which is the primary class in the Autosuggest module, and details its constructor and methods.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 9ff4ba1c-f285-4612-9070-de3d60d91270
caps.latest.revision: 6
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# AutosuggestManager Class

The AutosuggestManager is the primary class in the Autosuggest module.

## Constructor

> `AutosuggestManager(options?: AutosuggestOptions)`

## Methods

Name                            | Return Type            | Description
------------------------------- | ---------------------- | -----------------
`attachAutosuggest(suggestionBoxId: string, suggestionContainerId: string, selectedSuggestionCallback: function(result:SuggestionResult))` | |  Attaches the Autosuggest functionality to an input box.<br/><br/> • `suggestionBoxId` – The HTML element identifier of the input box.<br/> • `suggestionContainerId` – The Id of container where suggestions will be displayed.<br/> • `selectedSuggestionCallback` – A reference to a callback function that will be called when a user selects a suggestion from the Autosuggest UI. 
`detachAutosuggest()`             |                        | Detaches the autosuggest functionality from the input box, freeing any resources it has or events it has tied to.
`dispose()`                       |                        | Disposes the Autosuggest object, freeing any resources it has or events it has tied to.
`getOptions()`                    | AutosuggestOptions	 | Gets the options currently used by the autosuggest manager.
`getSuggestions(query: string, callback: function(suggestions: SuggestionResult[], query: string))` | | Programmatically retrieves suggestions for queries without the need to attach a textbox to the AutosuggestManager. Currently the suggestions returned by this function do not have their bestView property set and address suggestions do not have location coordinates. These suggestions can easily be enriched by using the Search module to geocode the suggestion.
`setOptions(options?: AutosuggestOptions)`	 |           | Sets the options currently used by the autosuggest manager.
