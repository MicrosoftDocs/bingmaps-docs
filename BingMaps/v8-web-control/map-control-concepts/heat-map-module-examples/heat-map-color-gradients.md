---
title: "Heat Map Color Gradients | Microsoft Docs"
description: Describes heat map color gradients, which are used to colorize the intensity of the heatmap and provides several examples of color gradients that demonstrate how they are implemented and what they look like.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: c2e8848e-7187-44be-96a6-d8539451465e
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Heat Map Color Gradients

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../../includes/bing-maps-web-control-sdk-retirement.md)]

The color gradient heat map option is used to colorize the intensity of the heatmap. The following are some examples of color gradients that you may find useful.

Description	               | Value	                                                                       | Gradient scale
--------------------------- | ---------------------------------------------------------------------------- | -----------------------------------
Black Aqua White           | `{`<br/>&nbsp; `'0': 'Black',`<br/>&nbsp; `'0.5': 'Aqua',`<br/>&nbsp; `'1': 'White`'<br/>`}`     | ![Black Aqua White Gradient](../../media/bmv8-heatmapcolorgradients-blackaquawhite.png)	 
Blue Red                   | `{`<br/>&nbsp; `'0.0': 'blue',`<br/>&nbsp; `'1': 'red`'<br/>`}`                             | ![Blue Red Gradient](../../media/bmv8-heatmapcolorgradients-bluered.png)	 
Deep Sea                   | `{`<br/>&nbsp; `'0.0': 'rgb(0, 0, 0)',`<br/>&nbsp; `'0.6': 'rgb(24, 53, 103)',`<br/>&nbsp; `'0.75': 'rgb(46, 100, 158)',`<br/>&nbsp; `'0.9': 'rgb(23, 173, 203)',`<br/>&nbsp; `'1.0': 'rgb(0, 250, 250)`'<br/>`}` | ![Deep Sea Gradient](../../media/bmv8-heatmapcolorgradients-deepsea.png) 	 
Color Spectrum             | `{`<br/>&nbsp; `'0': 'Navy',`<br/>&nbsp; `'0.25': 'Blue',`<br/>&nbsp; `'0.5': 'Green',`<br/>&nbsp; `'0.75': 'Yellow',`<br/>&nbsp; `'1': 'Red`'<br/>`}`  | ![Color Spectrum Gradient](../../media/bmv8-heatmapcolorgradients-colorspectrum.png)
Incandescent               | `{`<br/>&nbsp; `'0': 'Black',`<br/>&nbsp; `'0.33': 'DarkRed',`<br/>&nbsp; `'0.66': 'Yellow',`<br/>&nbsp; `'1': 'White`'<br/>`}`   | ![Incandescent Gradient](../../media/bmv8-heatmapcolorgradients-incandescent.png)	 
Heated Metal               | `{`<br/>&nbsp; `'0': 'Black',`<br/>&nbsp; `'0.4': 'Purple',`<br/>&nbsp; `'0.6': 'Red',`<br/>&nbsp; `'0.8': 'Yellow',`<br/>&nbsp; `'1': 'White`'<br/>`}` | ![Heated Metal Gradient](../../media/bmv8-heatmapcolorgradients-heatedmetal.png)	 
Sunrise	                   | `{`<br/>&nbsp; `'0': 'Red',`<br/>&nbsp; `'0.66': 'Yellow',`<br/>&nbsp; `'1': 'White`'<br/>`}`    | ![Sunrise Gradient](../../media/bmv8-heatmapcolorgradients-sunrise.png)	 
Stepped Colors             | `{`<br/>&nbsp; `'0': 'Navy',    '0.25': 'Navy',`<br/>&nbsp; `'0.26': 'Green',`<br/>&nbsp; `'0.5': 'Green',`<br/>&nbsp; `'0.51': 'Yellow',`<br/>&nbsp; `'0.75': 'Yellow',`<br/>&nbsp; `'0.76': 'Red',`<br/>&nbsp; `'1': 'Red`'<br/>`}`  | ![Stepped Colors Gradient](../../media/bmv8-heatmapcolorgradients-steppedcolors.png)	  	 
Visible Spectrum (Default) | `{`<br/>&nbsp; `'0.00': 'rgb(255,0,255)',`<br/>&nbsp; `'0.25': 'rgb(0,0,255)',`<br/>&nbsp; `'0.50': 'rgb(0,255,0)',`<br/>&nbsp; `'0.75': 'rgb(255,255,0)',`<br/>&nbsp; ` '1.00': 'rgb(255,0,0)'  `<br/>`}` | ![Visible Spectrum Gradient](../../media/bmv8-heatmapcolorgradients-visiblespectrum.png)	