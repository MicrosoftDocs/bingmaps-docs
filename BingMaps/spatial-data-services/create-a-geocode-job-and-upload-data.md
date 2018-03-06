---
title: "Create a Geocode Job and Upload Data | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d2760fb6-15a4-43ac-9ad3-13d40181db1f
caps.latest.revision: 56
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Create a Geocode Job and Upload Data
Use the following URL to upload a set of spatial data and to create a job to geocode and reverse-geocode the data.  
  
## Supported HTTP Methods  
 POST  
  
## URL template  
  
> [!IMPORTANT]
>  This template supports both HTTP and HTTPS protocols. URLs in the response use HTTPS protocol.  
  
 A job is created when you geocode entity data.  Before using this API, review the job limits in [Geocode and Data Source Limits](../spatial-data-services/geocode-and-data-source-limits.md).  
  
 **Upload locations and points and create a geocode job.**  
  
 The data that you upload can contain both data to geocode and data to reverse geocode. The geocode process detects the type of data for each entry and performs the appropriate action.  
  
```  
http://spatial.virtualearth.net/REST/v1/Dataflows/Geocode?input=input&output=output&dataLocation=dataLocation&key=BingMapsKey  
```  
  
### Template Parameters  
  
> [!NOTE]
>  Parameter names and values are not case-sensitive except for the key parameter value.  
  
|Parameter|Alias|Description|Values|  
|---------------|-----------|-----------------|------------|  
|dataLocation||**Optional.** Specifies the location of the data to download. **Note:**  You must set the dataLocation parameter to the location of the data or include the data to process in the HTTP request. If you do both, the URL returns an error.|A Windows Azure™ Blob Service REST API location that contains the data to process. The data must be in XML format. The Blob Service REST API uses the following URL formats:<br /><br /> http://*account-name*.blob.core.windows.net/*myDataFile*<br /><br /> https://*account-name*.blob.core.windows.net/*myDataFile*<br /><br /> For more information, see [Addressing Blob Service Requests](http://msdn.microsoft.com/en-us/library/dd135731.aspx).<br /><br /> Before you make your request to start the dataflow job, make sure that the Blob Service URL is available publicly or shared with a signature key. If the URL is shared with a signature key, it must be encoded. For more information, see [Managing Access to Containers and Blobs](http://msdn.microsoft.com/en-us/library/ee393343.aspx).<br /><br /> The following content types are supported for data that is retrieved from an HTTP server.<br /><br /> -   application/xml<br />-   text/xml<br />-   text/plain<br />-   application/octet-stream [for compressed data]<br /><br /> **Example**: dataLocation=http://myServer.myDomain.com/spatialDataSource|  
|input||**Required.** The format of the input data file.|One of the following values:<br /><br /> -   xml<br />-   csv<br />-   tab<br />-   pipe<br /><br /> For more information about input files for a Geocode Dataflow, see [Data Schema  v2.0](../spatial-data-services/geocode-dataflow-data-schema-version-2-0.md).<br /><br /> **Example**: input=csv|  
|key||**Required.** A Bing Maps Key to use for the geocode job.|A Bing Maps Key obtained from the [Bing Maps Account Center](https://www.bingmapsportal.com/).|  
|output|o|**Optional**. The output format for the response.|One of the following values:<br /><br /> -   json **[default]**<br />-   xml<br /><br /> **Example**: output=xml|  
  
## Input  
 This URL supports the following input formats. For examples, see [Sample Input and Output v2.0](../spatial-data-services/geocode-dataflow-sample-input-and-output-data-version-2-0.md).  
  
 When you create the HTTP request to upload data and create a geocode job, you must post the input data in the body of the request or set the dataLocation parameter to a URL where your data can be retrieved. You must also set the content type in the request to one of the following values, depending on the format of the input data.  
  
-   XML (application/xml)  
  
-   Comma-delimited values (text/plain)  
  
-   Tab-delimited values (text/plain)  
  
-   Pipe-delimited values (text/plain)  
  
-   Binary (application/octet-stream) [Specify this format when you upload compressed data from a [Blob Service REST API](http://msdn.microsoft.com/en-us/library/dd135733.aspx) location using the dataLocation parameter.]  
  
## Examples  
 This example creates a geocode job for spatial data that is provided in an xml format.  
  
```  
http://spatial.virtualearth.net/REST/v1/Dataflows/Geocode?input=xml&key=BingMapsKey  
```  
  
 This example creates a geocode job for spatial data that is provided in an xml format and assigns a description “My dataflow” to the job.  
  
```  
http://spatial.virtualearth.net/REST/v1/Dataflows/Geocode?input=xml&key=BingMapsKey  
```  
  
## Response  
 The response to this URL contains a representation of the geocode dataflow job instance.  
  
 This URL supports the following response formats.  
  
-   JSON (application/json)  
  
-   XML (application/xml)  
  
 For information about the response, see [Response Data](../spatial-data-services/geocode-dataflow-response-description.md).  
  
## Sample Code  
 The following code shows how to create a job to geocode spatial data. The data you want to geocode is uploaded as part of the job creation process. This code is part of a complete Geocode Dataflow code sample. To view the complete code sample, see [Sample Code](../spatial-data-services/geocode-dataflow-sample-code.md). You may also want to read the [Walkthrough](../spatial-data-services/geocode-dataflow-walkthrough.md) to get a step-by-step description of how to use the Geocode Dataflow. The walkthrough includes example URLs and HTTP responses.  
  
```  
//Creates a geocode dataflow job and uploads spatial data to process.  
//Parameters:   
//   dataFilePath: The path to the file that contains the spatial data to geocode.  
//   dataFormat: The format of the input data. Possible values are xml, csv, tab and pipe.  
//   key: The Bing Maps Key to use for this job. The same key is used to get job status and download results.  
//   description: Text that is used to describe the geocode dataflow job.   
//Return value : A URL that defines the location of the geocode dataflow job that was created.  
static string CreateJob(string dataFilePath, string dataFormat, string key, string description)  
{  
    //Define parameters for the HTTP request  
    //  
    // The 'Content-Type' header of the HTTP Request must be "text/plain" or "application/xml"  
    // depending on the input data format.  
    //  
    string contentType = "text/plain";  
    if (dataFormat.Equals("xml", StringComparison.OrdinalIgnoreCase))  
        contentType = "application/xml";  
  
    StringBuilder queryStringBuilder = new StringBuilder();  
  
    //  
    // The 'input'(input format) and 'key' (Bing Maps Key) parameters are required.  
    //  
    queryStringBuilder.Append("input=").Append(Uri.EscapeUriString(dataFormat));  
    queryStringBuilder.Append("&");  
    queryStringBuilder.Append("key=").Append(Uri.EscapeUriString(key));  
  
    if (!String.IsNullOrEmpty(description))  
    {  
        //  
        // The 'description' parameter is optional.  
        //  
        queryStringBuilder.Append("&");  
  
    }  
  
    //Build the HTTP URI that will upload and create the geocode dataflow job  
    UriBuilder uriBuilder = new UriBuilder("http://spatial.virtualearth.net");  
    uriBuilder.Path = "/REST/v1/dataflows/geocode";  
    uriBuilder.Query = queryStringBuilder.ToString();  
  
    //Include the data to geocode in the HTTP request  
    using (FileStream dataStream = File.OpenRead(dataFilePath))  
    {  
        HttpWebRequest request = (HttpWebRequest)WebRequest.Create(uriBuilder.Uri);  
  
        //  
        // The HTTP method must be 'POST'.  
        //  
        request.Method = "POST";  
        request.ContentType = contentType;  
  
        using (Stream requestStream = request.GetRequestStream())  
        {  
            byte[] buffer = new byte[16384];  
            int bytesRead = dataStream.Read(buffer, 0, buffer.Length);  
            while (bytesRead > 0)  
            {  
                requestStream.Write(buffer, 0, bytesRead);  
  
                bytesRead = dataStream.Read(buffer, 0, buffer.Length);  
            }  
        }  
  
        //Submit the HTTP request and check if the job was created successfully.   
        using (HttpWebResponse response = (HttpWebResponse)request.GetResponse())  
        {  
            //  
            // If the job was created successfully, the status code should be  
            // 201 (Created) and the 'Location' header should contain a URL  
            // that defines the location of the new dataflow job. You use this   
            // URL with the Bing Maps Key to query the status of your job.  
            //  
            if (response.StatusCode != HttpStatusCode.Created)  
                throw new Exception ("An HTTP error status code was encountered when creating the geocode job.");  
  
            string dataflowJobLocation = response.GetResponseHeader("Location");  
            if (String.IsNullOrEmpty(dataflowJobLocation))  
                throw new Exception ("The 'Location' header is missing from the HTTP response when creating a goecode job.");  
  
            return dataflowJobLocation;  
        }  
    }  
}  
  
```  
  
## HTTP Status Codes  
  
> [!NOTE]
>  For more details about these HTTP status codes, see [Status Codes and Error Handling](../spatial-data-services/status-codes-and-error-handling.md).  
  
 When the request is successful, the following HTTP status code is returned.  
  
-   201  
  
 When the request is not successful, the response returns one of the following errors.  
  
-   400  
  
-   500  
  
-   503  
  
    > [!NOTE]
    >  The response may contain a 503 HTTP status error code when the number of pending geocode dataflow jobs is exceeded. The maximum number of pending geocode dataflow jobs that can be associated with a Bing Maps Key is 10.