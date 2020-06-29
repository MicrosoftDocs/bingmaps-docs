---
title: "NavigationBarMode Enumeration | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 30314d77-1bf1-41d1-9ed5-9e7144ee78aa
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# NavigationBarMode Enumeration
The NavigationBarMode can be used to customize the layout and style of the navigation bar.

| Name | Description    | Example   
| ---- | -------------- | :------: |                                         
| `compact`  | A compact navigation bar that includes a smaller drop down for the map type and zoom buttons. Recommended for small maps or screen such as a mobile device. | ![Compact Navigation Bar](../media/compact-navigation-bar.PNG)
| `default`  | The default navigation bar that has a drop down for the map type, a locate me button, and zoom buttons. Recommended for medium to large maps in desktop browsers.  | ![Nav bar](../media/nav-bar.png)
| `minified` | A minified navigation bar that has a button to toggle between road and aerial maps, zoom buttons, and a button to turn traffic information on and off. Recommended for small maps or screen such as a mobile device. | ![Minified Nav Bar](../media/minified-nav-bar.png)
| `square` | A navigation bar that uses aligned square icons. It includes a drop down for map type, a locate me button, and zoom buttons. It is also the only mode that supports the floor switcher for [Venues](../../venues/index.md). | ![Square Nav Bar](../media/square-nav-bar.png)
