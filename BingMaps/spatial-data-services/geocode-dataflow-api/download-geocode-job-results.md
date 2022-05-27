---
title: "Download Geocode Job Results | Microsoft Docs"
description: "Describes how to download Geocode job results and provides sample code for how to download job results in XML and JSON."
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: b762102b-810d-47eb-8bbc-5417015e5e68
caps.latest.revision: 11
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Download Geocode Job Results

The URLs to download results from a Geocode Job are provided when your job has completed and you request job status. When your job has completed, the `Status` field in the job status response is set to `Completed` and the URLs to use to download processed data are defined in the response as XML `Link` values, or as part of a JSON `links` collection. You can distinguish these link elements in the response because they have the attribute `role` set to `output`. These link elements also specify the `name` attribute and set it to `succeeded` or `failed` to identify a download URL for data that was processed successfully or for data that encountered errors during processing. A link does not appear if there is no data to download. Therefore, if all your data was processed successfully, a link with the `name` attribute and set it to `failed` will not appear in the response. The following are examples of these link elements.  
  
 **XML**  
  
```xml
<Link role="output" name="succeeded">https://spatial.virtualearth.net/REST/v1/dataflows/Geocode/5bf10c37df944083b1879fbb0556e67e/output/succeeded</Link>  
<Link role="output" name="failed">https://spatial.virtualearth.net/REST/v1/dataflows/Geocode/5bf10c37df944083b1879fbb0556e67e/output/failed</Link>  
  
```  
  
 **JSON**  
  
```json
"links":[  
      {  
         "name":"succeeded",  
         "role":"output",  
         "url":"https:\/\/spatial.virtualearth.net\/REST\/v1\/dataflows\/Geocode\/5bf10c37df944083b1879fbb0556e67e\/output\/succeeded"  
      },  
      {  
         "name":"failed",  
         "role":"output",  
         "url":"https:\/\/spatial.virtualearth.net\/REST\/v1\/dataflows\/Geocode\/5bf10c37df944083b1879fbb0556e67e\/output\/failed"  
      }  
]  
  
```  
  
 To use these URLs, you must add the Bing Maps Key parameter that you used to create the job. For example, to download the data that was processed successfully in the above example, you would add the parameter key *MyDataflowJobKey* where *MyDataflowJobKey* is the Bing Maps Key that you used to create the job.  
  
```url
https://spatial.virtualearth.net/REST/v1/dataflows/Geocode/5bf10c37df944083b1879fbb0556e67e/output/succeeded?key=MyDataflowJobKey  
```  
  
 For information about the Geocode Dataflow data schema, see [Data Schema  v2.0](../geocode-dataflow-api/geocode-dataflow-data-schema-version-2-0.md).  
  
## Sample Code  
 The following code shows how to download the results of a geocode job. The geocoded results are saved in text files. This code is part of a complete Geocode Dataflow code sample. To view the complete code sample, see [Sample Code](../geocode-dataflow-api/geocode-dataflow-sample-code.md). You may also want to read the [Walkthrough](../geocode-dataflow-api/geocode-dataflow-walkthrough.md) to get a step-by-step description of how to use the Geocode Dataflow. The walkthrough includes example URLs and HTTP responses.  
  
```csharp
//Downloads job results to files names Success.txt (successfully geocoded results) and   
//   Failed.txt (info about spatial data that was not geocoded successfully).  
//Parameters:   
//   statusDetails: Inclues job status and the URLs to use to download all geocoded results.  
//   key: The Bing Maps Key for this job. The same key is used to create the job and get job status.     
  
static void DownloadResults(DownloadDetails statusDetails, string key)  
{  
    //Write the results for data that was geocoded successfully to a file named Success.xml  
    if (statusDetails.suceededlink != null && !statusDetails.suceededlink.Equals(String.Empty))  
    {  
        //Create a request to download successfully geocoded data. You must add the Bing Maps Key to the   
        //  download location URL provided in the response to the job status request.  
        UriBuilder successUriBuilder = new UriBuilder(statusDetails.suceededlink + @"?key=" + key);  
        HttpWebRequest request1 = (HttpWebRequest)WebRequest.Create(successUriBuilder.Uri);  
  
        request1.Method = "GET";  
  
        using (HttpWebResponse response = (HttpWebResponse)request1.GetResponse())  
        {  
            if (response.StatusCode != HttpStatusCode.OK)  
                throw new Exception ("An HTTP error status code was encountered when downloading results.");  
  
            using (Stream receiveStream = response.GetResponseStream())  
            {  
                StreamWriter successfile = new StreamWriter("Success.txt");  
                using (StreamReader r = new StreamReader(receiveStream))  
                {  
                    string line;  
                    while ((line = r.ReadLine()) != null)  
                    {  
                        successfile.Write(line);  
                    }  
                }  
                successfile.Close();  
            }  
  
        }  
    }  
  
    //If some spatial data could not be geocoded, write the error information to a file called Failed.xml  
    if (statusDetails.failedlink != null && !statusDetails.failedlink.Equals(String.Empty))  
    {  
        //Create an HTTP request to download error information. You must add the Bing Maps Key to the   
        //  download location URL provided in the response to the job status request.  
        UriBuilder failedUriBuilder = new UriBuilder(statusDetails.failedlink + @"?key=" + key);  
        HttpWebRequest request2 = (HttpWebRequest)WebRequest.Create(failedUriBuilder.Uri);  
  
        request2.Method = "GET";  
  
        using (HttpWebResponse response = (HttpWebResponse)request2.GetResponse())  
        {  
            if (response.StatusCode != HttpStatusCode.OK)  
                throw new Exception ("An HTTP error status code was encountered when downloading results.");  
  
            using (Stream receiveStream = response.GetResponseStream())  
            {  
                StreamWriter failedfile = new StreamWriter("Failed.txt");  
                using (StreamReader r = new StreamReader(receiveStream))  
                {  
                    string line;  
                    while ((line = r.ReadLine()) != null)  
                    {  
                        failedfile.Write(line);  
                        }  
                }  
                failedfile.Close();  
            }  
  
        }  
    }  
}  
  
```