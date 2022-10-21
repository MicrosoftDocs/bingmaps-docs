---
title: "Bing Maps on Azure Marketplace | Microsoft Docs"
description: Learn about the deprecation of the Bing Maps for Enterprise product licensing option through Azure Marketplace.
ms.custom: ""
ms.date: "08/31/2020"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: conceptual
ms.assetid: ""
caps.latest.revision: ""
author: "DRMap"
ms.author: v-munksteve
manager: "donnali"
ms.service: "bing-maps"
---
# Bing Maps for Enterprise on Azure Marketplace

## Announcement
The Bing Maps for Enterprise product licensing option through Azure Marketplace has been scheduled for deprecation and will be discontinued.

## What does this mean for you?
Bing Maps for Enterprise will be removed as an offering on Azure Marketplace and your existing keys will stop working according to the timeline below.

## Recommendations
We are recommending that our Azure Marketplace customers transition their mapping solutions to utilize [Azure Maps](https://azure.microsoft.com/services/azure-maps/) and license it through the [Azure Portal](https://portal.azure.com/#home). Customers who still require Bing Maps APIs, please review our other Bing Maps for [Enterprise licensing](https://www.microsoft.com/maps/licensing) options.

## Timeline
The timeline is as follows:
- October 5, 2020
  - New Bing Maps for Enterprise resources (subscriptions) can no longer be created on Azure Marketplace.
  
- November 2, 2020:
  - Free tier:
    - Free tier (non-paid) resources are shut down. These include the levels “Public Website Transactions Level 1” and “Internal Website Transactions Level 1”. This means the resource will no longer be visible in the Azure Portal.
    - The generated keys remain functional within key limits until January 31, 2021.
  - Paid tier:       
    - Existing resources and keys remain available.
    - Changes in pricing tiers are no longer possible.
    - Customers can actively delete their resources. This will also disable the respective key.
    
- January 11, 2021: 
  - All remaining Bing Maps Enterprise resources licensed through the Azure Marketplace will be removed in the Azure Portal.
  - Customers can no longer access the respective resources in the Azure Portal.
  - The generated keys remain functional within key limits until January 31, 2021 after which the keys will be disabled.

## Why is this happening?
Bing Maps for Enterprise licensing through Azure Marketplace was first released before Azure Maps was created and was used as an easy way to license an enterprise mapping solution within the Azure portal. Then, in early 2018, Azure Maps was launched as a native Azure mapping solution and has become the enterprise mapping solution of choice for our Azure customers.

## Resources

### Azure Maps
- [Azure Maps product overview](https://azure.microsoft.com/services/azure-maps/)
- [Azure Maps documentation](/azure/azure-maps/)
- [Azure Maps quick start](/azure/azure-maps/quick-demo-map-app)
- [Azure Maps pricing](https://azure.microsoft.com/pricing/details/azure-maps/)

### Bing Maps
- [Bing Maps for Enterprise licensing options](https://www.microsoft.com/maps/licensing)
- To contact the Bing Maps for Enterprise licensing team please go to [this page](https://www.microsoft.com/maps/contact-us) or contact us at maplic@microsoft.com for customers in the Americas and mapemea@microsoft.com for all other regions
- [Bing Maps for Enterprise documentation](/bingmaps/)
- [Bing Maps for Enterprise technical support](https://support.microsoft.com/supportforbusiness/productselection?sapId=a2a88740-f135-42df-37d0-430a1b6cffc1)
- Customers that are interested to continue to use Bing Maps for Enterprise are encouraged to sign up for an account/key at the [Bing Maps portal](https://www.bingmapsportal.com/)
