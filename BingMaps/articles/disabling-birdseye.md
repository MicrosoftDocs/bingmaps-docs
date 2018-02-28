---
title: "Disabling Birdseye | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 29649a6e-9cfd-4a17-be5b-8afa4cfff3dd
caps.latest.revision: 9
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Disabling Birdseye
If you need to disable bird's eye functionality in [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)], version 6.0 or lower, then follow the instructions below.  If you are using [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)], version 6.1 or higher, use the **VEMapOptions.EnableBirdseye** property instead.  
  
## Disabling Birdseye  
 To disable Birdseye you must trap the keyboard shortcuts that normally invoke Birdseye map style, 'b' and 'o'. The key code values for these are 66 and 79, respectively. The following function traps those two key code values.  
  
```  
function keydownCB(e)  
{  
   if(e.keyCode == 66 || e.keyCode == 79)  
   {  
      return true;  
   }  
}  
```  
  
 You must attach the **onkeydown** event to this function so as each key is pressed, the `keydown` function receives the key press, as shown in the following statement.  
  
```  
map.AttachEvent("onkeydown", keydownCB);  
```  
  
 In addition to trapping keyboard events, your code could create a custom map navigation control that avoid Birdseye in HTML, and then add the control to the map by calling the **VEMap.AddControl** method.