---
title: "Helpful Tips for Entity Data | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 9ce6e890-876e-4e61-9544-9b9931ac62f7
caps.latest.revision: 8
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Helpful Tips for Entity Data
Here are some tips to help you when you create entity data to use with the Bing Spatial Data Services.  
  
-   **Consider using pipe(&#124;)-delimited  or XML entity data files**. Entity data often contains commas (Example: Seattle, WA). Therefore, using the pipe (&#124;) character as a separator in entity data files is often a good choice. Similarly, XML files support the use of commas (,), hyphens (-), and pipe characters (&#124;) as part of entity data values.  
  
-   **Make sure you do not create more than the maximum number of 350 properties.** For a list of supported data types, see [Data Schema and Sample Input](../spatial-data-services/load-data-source-data-schema-and-sample-input.md). To reduce the number of string (Edm.String) properties, consider the following options.  
  
    -   Remove unnecessary or redundant properties.  
  
    -   Convert a property with 'yes' and 'no' string values to a Boolean property with true and false values.  
  
    -   Combine two or more string properties into a single string property by using a secondary delimiter, such as a dash (-).For example, if your entity data included an opening and closing time and you do not need to query on these values separately, you could combine them into a single string, such as '8:00 – 5:00'. If you needed to separate these values for a web application, use client-side parsing.  
  
         If you are using XML to format your entity data, you can also use the pipe (&#124;) character as a delimiter.  
  
    -   Consider converting numeric information such as phone numbers to an integer property. Note that a leading 0 in a number will not be stored in this scenario. However, you can accommodate for this if all the numbers are the same length. Also, if a number is not provided, the default value of zero (0) is stored.  
  
-   Make sure you specify a primary key in your data schema and that each set of entity data has a unique primary key value.  
  
-   **Make sure latitude and longitude properties are included in the data schema.**  The latitude and longitude properties do not count towards the maximum number of properties with a data type of double (Edm.Double).  
  
-   **Do not store HTML with entity data.**  HTML tags cannot be stored as entity data. If an entity value is used in the HTML of a web application, you can store the value in the data source, and then generate the HTML by using client-side processing. For example, you can store the URL for an image as entity data and then build the HTML image using client-side code.  
  
-   **When possible, reduce the resolution of latitude and longitude values to six decimal places or less.** This reduces the size of a data source query and reduces the response size. The response download time can be noticeable with mobile applications.