---
title: "Open Maps understanding ODbL | Microsoft Docs"
description: "Describes how to understand ODbL in Open Maps within Bing Maps and outlines what ODbL is, its requirements, and how to share ODbL data."
ms.custom: ""
ms.date: ""
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ""
author: "jesselgit"
ms.author: "jelevi"
manager: ""
ms.service: "bing-maps"
---
# Open Maps: understanding ODbL

**ODBL in Bing Maps**

Certain data available in the [Bing Maps v8 web control](../v8-web-control/index.md) API will be subject to the Open Database License (ODbL). This data will be identified as the **building layer.**  

## What is ODbL?

 The Open Database License (ODbL) is an open source data license that enables users to utilize the data in their products, services and applications, subject to certain license requirements. The ODbL was developed by Open Data Commons and is used by several open source mapping initiatives, such as OpenStreetMap and Paris Open Data. Microsoft is including map data from databases under ODbL licenses in its APIs in order to provide a robust mapping solution to users.

 >[!WARNING]
 > **This page is for informational purposes only**. It does not constitute legal advice or interpretation.  For information about using data subject to ODbL, seek the guidance of an attorney. Microsoft is not liable or responsible for your use of any data subject to ODbL.
 

## What are the requirements for use of ODbL data?

 **Attribute:** If you use data under an ODbL license, you must provide attribution to the source of the data. If you are using the [Bing Maps v8 web control](../v8-web-control/index.md) API, such credits are already listed in the Bing Suppliers Page (<https://bingexplore.azurewebsites.net/bing-data-suppliers/en/>) that is linked from the Bing Maps TOU that you must link to under the terms of the Bing Maps API agreement. However, Microsoft cannot give you specific guidelines about attribution, as the final method of attribution will vary based on your use case.

- **Share-Alike:** If you adapt any database that is subject to the ODbL, either by adding your own or third-party content, or by removing or modifying inaccurate content, the resulting adapted version of the database must also be released under the ODbL.

- **Other Requirements:** You should review the ODbL text at <https://opendatacommons.org/licenses/odbl/> to ensure that your usage of any ODbL content complies with the license terms.  

## Do I have to share my data if I use ODbL data?

You will not have to automatically share your data if you use data under the ODbL license in your application.  If you simply use the data as-is, without modifying the database or creating a hybrid database that combines multiple datasets, it is unlikely that you will have to share your contributed data. If you segregate your data from ODbL-licensed data or just use ODbL-licensed data to create a map, it is unlikely that you would have to share your segregated data or the output map.

However, if you combine a number of sources into a single, unified database or modify an existing ODbL database using other information, it is likely that you would need to release the resulting database under the ODbL license, which means that other people could see your data and use it. You should consult your legal representative to determine whether your specific use of ODbL data may subject you to share-alike terms.

## Where can I get more information about ODbL licensing rules?

Contact your legal representative if you have questions about using ODbL content in your application. Microsoft cannot provide you with any specific advice about usage of ODbL content.
