---
title: "InfoboxActions Object | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 0c2af7da-b306-4815-a130-a5d771f195d3
caps.latest.revision: 5
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# InfoboxActions Object
The following is a list of infobox action properties that can be used to create clickable links in infoboxes.

Name           | Type      | Description
-------------- | --------- | ------------------------------
`label`          | string    | The text to display for the action.
`eventHandler`   | function  | The function to call when the label is clicked.

**Note**: InfoboxActions have been included in Bing Maps V8 primarily for backwards compatibility with V7. Instead it is recommended to use standard HTML buttons and links in the infobox description.