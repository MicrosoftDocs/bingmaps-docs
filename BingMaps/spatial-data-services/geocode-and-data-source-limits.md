---
title: "Geocode and Data Source Limits | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: a849e7ef-ad84-4e8b-ac9b-d2051b8261a7
caps.latest.revision: 28
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Geocode and Data Source Limits

This topic describes account limits for a Bing Maps Account when you use the Bing Spatial Data Services or the Bing Maps Dev Center at [https://www.bingmapsportal.com/](https://www.bingmapsportal.com/) to geocode entities and manage data sources.  

When you geocode entities or perform data source actions such as creating or updating a data source using either the Bing Spatial Data Services or the Bing Maps Dev Center, a job is created to perform the action. See [Get Job List](../spatial-data-services/get-job-list.md) for a list of jobs that count towards the following limits.

**Note:** The Bing Maps Spatial Data Services (i.e.: [Geocode Dataflow API](../spatial-data-services/geocode-dataflow-api) and [Data Source Management API](../spatial-data-services/data-source-management-api)) do not have a service level agreement (SLA) specifically for job processing completion time. However, smaller jobs will typically process faster than larger jobs. The processing completion time for each job can take up to 12 hours, generally much faster than that.

## Account Limits for Basic Keys  
  
-   Applicable data source and geocode jobs (see the list of applicable jobs in [Get Job List](../spatial-data-services/get-job-list.md)) that use Basic keys from the same Bing Maps Account have the following account limits:  
  
    -   You can have a total of 2 jobs in process at the same time.  
  
    -   You can run a total of 50 jobs in a 24 hour period.  
  
-   You can have a maximum of 5 data sources per Bing Maps Account.  
  
-   The maximum number of entities a data source can have is 2,500 entities.  
  
-   Data that is batch geocoded must use UTF-8 encoding, and can have a maximum of 50 entities. Compressed data files are accepted.  
  
-   You can download geocode results for up to 14 calendar days after a geocode job completes.  
  
## Account Limits for Enterprise Keys [Enterprise Account]  
  
-   Applicable data source and geocode jobs (see the list of applicable jobs in [Get Job List](../spatial-data-services/get-job-list.md) ) that use Enterprise keys from the same Bing Maps Account have the following account limits. Jobs that use Basic keys that belong to an Enterprise account have the limits described above and are also included in the following limits.  
  
    -   You can have a total of 10 jobs in process at the same time. This limit also includes jobs run with Basic keys.  
  
    -   You can run a total of 50 jobs in a 24 hour period. This limit also includes jobs run with Basic keys.  
  
-   You can have a maximum of 25 data sources per Bing Maps Account.  
  
-   Data that is geocoded or uploaded to a data source must use UTF-8 encoding, and can have up to 300 MB of uncompressed data and a maximum of 200,000 entities. Compressed data files are accepted, but the uncompressed limit applies.  
  
-   You can download geocode results for up to 14 calendar days after a geocode job completes.  
  
## View My Jobs  
 To get a list of all pending and completed jobs within the last 15 days, see [Get Job List](../spatial-data-services/get-job-list.md).  
  
 A job is **in process** until the status is set to "Completed" or "Aborted".
