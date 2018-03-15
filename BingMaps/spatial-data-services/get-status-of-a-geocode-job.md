---
title: "Get Status of a Geocode Job | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 41bdab65-ca4c-4951-89e9-a2a75d9ea61c
caps.latest.revision: 32
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# Get Status of a Geocode Job
Use the following URL to get the status of a geocode job.  
  
## Supported HTTP Methods  
 GET  
  
## URL template  
  
> [!NOTE]
>  This template supports both HTTP and HTTPS protocols. URLs in the response use HTTPS protocol.  
  
 **Get status information for a geocode job.**  
  
 The Bing Maps Key that you specify must be the same Bing Maps Key that you used to create the job. A URL in the following format without the Bing Maps Key is provided in the response to the URL request that you made to [Create Job](../spatial-data-services/create-a-geocode-job-and-upload-data.md). The URL is specified in a `link` field with an attribute of `self`. For more information, see [Response Data](../spatial-data-services/geocode-dataflow-response-description.md).  
  
```  
http://spatial.virtualearth.net/REST/v1/Dataflows/Geocode/jobID?output=output&key=BingMapsKey  
```  
  
### Template Parameters  
  
> [!NOTE]
>  Parameter names and values are not case-sensitive except for the key parameter value.  
  
|Parameter|Alias|Description|Values|  
|---------------|-----------|-----------------|------------|  
|jobID||**Required.** The ID of the job.|When you request a dataflow job, the job ID is returned in the ID field of the response. For more information, see [Response Data](../spatial-data-services/geocode-dataflow-response-description.md).<br /><br /> **Example**: e14b1d9bd65c4b9d99d267bbb8102ccf|  
|key||**Required**. The Bing Maps Key that you used to create the geocode job.|A Bing Maps Key from the [Bing Maps Account Center](http://www.bingmapsportal.com).<br /><br /> **Example**: key=abc123def456ghi789abc123def456ghi789|  
|output|o|**Optional**. The output format for the response.|One of the following values:<br /><br /> -   json **[default]**<br />-   xml<br /><br /> **Example**: o=xml|  
  
## Examples  
 This example requests resource information for the job with an ID of e14b1d9bd65c4b9d99d267bbb8102ccf that was created by using the Bing Maps Key b1c323ea234b1c323ea234b1c323ea234.  
  
```  
http://spatial.virtualearth.net/REST/v1/Dataflows/Geocode/e14b1d9bd65c4b9d99d267bbb8102ccf?key=b1c323ea234b1c323ea234b1c323ea234  
```  
  
## Response  
 This URL supports the following response formats.  
  
-   JSON: **application/json**  
  
-   XML: **application/xml**  
  
 For information about the response, see [Response Data](../spatial-data-services/geocode-dataflow-response-description.md).  
  
## Sample Code  
 The following code shows how to get the status of a geocode job. This code is part of a complete Geocode Dataflow code sample. To view the complete code sample, see [Sample Code](../spatial-data-services/geocode-dataflow-sample-code.md). You may also want to read the [Walkthrough](../spatial-data-services/geocode-dataflow-walkthrough.md) to get a step-by-step description of how to use the Geocode Dataflow. The walkthrough includes example URLs and HTTP responses.  
  
```  
class DownloadDetails  
{  
    public string jobStatus { get; set; }  
    public string suceededlink { get; set; }  
    public string failedlink { get; set; }  
  
}  
  
```  
  
```  
//Checks the status of a dataflow job and defines the URLs to use to download results when the job is completed.  
//Parameters:   
//   dataflowJobLocation: The URL to use to check status for a job.  
//   key: The Bing Maps Key for this job. The same key is used to create the job and download results.    
//Return value: A DownloadDetails object that contains the status of the geocode dataflow job (Completed, Pending, Aborted).  
//              When the status is set to Completed, DownloadDetails also contains the links to download the results  
  
static DownloadDetails CheckStatus(string dataflowJobLocation, string key)  
{  
  
    DownloadDetails statusDetails = new DownloadDetails();  
    statusDetails.jobStatus = "Pending";  
  
    //Build the HTTP Request to get job status  
    UriBuilder uriBuilder = new UriBuilder(dataflowJobLocation + @"?key=" + key + "&output=xml");  
    HttpWebRequest request = (HttpWebRequest)WebRequest.Create(uriBuilder.Uri);  
  
    request.Method = "GET";  
  
    //Submit the request and read the response to get job status and to retrieve the links for   
    //  downloading the job results  
    //Note: The following conditional statements make use of the fact that the 'Status' field will    
    //  always appear after the 'Link' fields in the HTTP response.  
    using (HttpWebResponse response = (HttpWebResponse)request.GetResponse())  
    {  
  
        if (response.StatusCode != HttpStatusCode.OK)  
            throw new Exception ("An HTTP error status code was encountered when checking job status.");  
  
        using (Stream receiveStream = response.GetResponseStream())  
        {  
            XmlTextReader reader = new XmlTextReader(receiveStream);  
            while (reader.Read())  
            {  
                if (reader.IsStartElement())  
                {  
                    if (reader.Name.Equals("Status"))  
                    {  
                        //return job status  
                        statusDetails.jobStatus = reader.ReadString();  
  
                        return (statusDetails);  
                    }  
                    else if (reader.Name.Equals("Link"))  
                    {  
                        //Set the URL location values for retrieving   
                        // successful and failed job results  
                        reader.MoveToFirstAttribute();  
                        if (reader.Value.Equals("output"))  
                        {  
                            reader.MoveToNextAttribute();  
                            if (reader.Value.Equals("succeeded"))  
                            {  
                                statusDetails.suceededlink = reader.ReadString();  
  
                            }  
                            else if (reader.Value.Equals("failed"))  
                            {  
                                statusDetails.failedlink = reader.ReadString();  
                            }  
                        }  
                    }  
                }  
            }  
  
        }  
  
    }  
    return (statusDetails);  
}  
  
```  
  
## HTTP Status Codes  
  
> [!NOTE]
>  For more details about these HTTP status codes, see [Status Codes and Error Handling](../spatial-data-services/status-codes-and-error-handling.md).  
  
 When the request is successful, the following HTTP status code is returned.  
  
-   200  
  
 When the request is not successful, the response returns one of the following HTTP status codes.  
  
-   400  
  
-   500  
  
-   503