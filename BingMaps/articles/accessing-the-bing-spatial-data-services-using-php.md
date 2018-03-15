---
title: "Accessing the Bing Spatial Data Services using PHP | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 632951d6-9a20-4c32-8f7a-1096379cb09b
caps.latest.revision: 11
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# Accessing the Bing Spatial Data Services using PHP
This article will describe how to write a PHP application that can interact with the Bing Spatial Data Services Geocode Dataflow API.  
  
 The Bing Spatial Data Services is a RESTful web service. Representational State Transfer (REST) is an architecture for distributed systems. It follows a stateless client-server model, meaning that there is no memory (context) of past requests stored on the server between client requests. A RESTful web service is a collection of resources, stored under a central URL, which supports a set of operations all of which can be activated using HTTP methods (POST, GET, etc.).  
  
 The Bing Spatial Data Services includes a Geocode Dataflow API that allows you to “batch” geocode large sets of spatial data. Use of this API involves starting geocode “jobs” on large lists of spatial data, waiting for the job to complete, and then accessing the successfully (or unsuccessfully) geocoded locations when the job is complete. Spatial data can be uploaded in a variety of formats, including XML, CSV, tab-delimited and pipe-delimited files. These files can be accessed using HTTP GET requests that include a URI and parameters indicating what information is to be returned.  
  
 This article will describe how to construct PHP pages that interact with the Bing Spatial Data Services Geocode Dataflow API.  
  
 For a complete description of the Bing Spatial Data Services including an API reference, see the Bing Spatial Data Services documentation at [Bing Spatial Data Services](../spatial-data-services/index.md).  
  
## Setting Up Your Environment  
 Before continuing with this article, you should ensure that you have the correct software installed and environment setup to develop and host PHP pages that will connect to the Bing Spatial Data Services Geocode Dataflow API.  
  
### Required Software  
 To work with and run the sample applications in this article, you will need a PHP-enabled web server. To develop the samples, we used **WampServer** (http://www.wampserver.com), a Windows-based development environment that includes Apache, PHP, and MySQL Database. It is easy to install and has everything you need to create and host PHP applications quickly and easily.  
  
 **Microsoft IIS 6 or 7** can also be used to host PHP applications, and we tested several of the examples on it to confirm that they work. If you are using IIS to host PHP, you may also want to install **FastCGI**, which improves performance of CGI applications in IIS. You can find a very detailed set of instructions for installing and configuring FastCGI and PHP at:  
  
-   IIS 6 - [http://learn.iis.net/page.aspx/247/using-fastcgi-to-host-php-applications-on-iis-60/](http://learn.iis.net/page.aspx/247/using-fastcgi-to-host-php-applications-on-iis-60/)  
  
-   IIS 7 - [http://learn.iis.net/page.aspx/246/using-fastcgi-to-host-php-applications-on-iis-7/](http://learn.iis.net/page.aspx/246/using-fastcgi-to-host-php-applications-on-iis-7/)  
  
 To use the code in this article in the Windows environment, you will need to download the php_http extension from [http://downlaods.php.net/pierre](http://downloads.php.net/pierre/). For more information about which download to choose, see the **Which version do I choose?** on the PHP for Windows download page: [http://windows.php.net/download/](http://windows.php.net/download/).  
  
 You will also need to activate the php_openssl extension. If you are using Wampserver, you can activate the php_openssl extension by selecting it from the WampServer taskbar menu under PHP->PHP extensions->php_openssl.  
  
 There are many other servers that can be configured to host PHP, and you are free to use any of those instead if you are more familiar with their functionality.  
  
 Finally, in terms of a development environment, you can use anything from a text editor such as Windows Notepad to a full-fledged PHP IDE such as PHP Designer to write your code.  
  
### PHP Starter Code  
 This article contains numerous samples of interacting with Bing Spatial Data Services Geocode Dataflow API using PHP. If you are already familiar with PHP, you may not need any assistance creating and setting up a PHP page in which to include your Bing Maps code. However, if you need assistance getting started, you may want to begin with the following simple PHP structure which includes a Bing Maps Key that will be discussed in the following section.  
  
 **Listing 1 - PHP starter code for working with Bing Spatial Data Services Geocode Dataflow API**  
  
```  
<<html>  
  <head><title>Using the Bing Spatial Data Geocode Dataflow API</title></head>  
  <body>  
    <?php  
       $key = "yourKeyHere";  
  // Additional code goes here  
    ?>  
  </body>  
</html>  
```  
  
## Authentication  
 All Bing Spatial Data Services require authentication from the client each time they are called. In order to authenticate against the Bing Spatial Data Services Geocode Dataflow API, you will need a Bing Maps Key. For information about how to sign up for a Bing Maps Developer Account and get a Bing Maps Key, see [Getting a Bing Maps Key](http://msdn.microsoft.com/en-us/library/ff428642.aspx).  
  
 When you send an HTTP request to the Geocode Dataflow API, which we will discuss in the next section of this article, you must include the Bing Maps Key as a parameter. For example, you might send an HTTP request like the one shown in Listing 2.  
  
 **Listing 2 - Authenticating using a Bing Maps Key**  
  
```  
http://spatial.virtualearth.net/REST/v1/Dataflows/Geocode?description=description&input=input&key=YourBingMapsKeyHere  
  
```  
  
 In all of the examples in this article, you will see the Bing Maps Key sent to the Bing Spatial Data Services Geocode Dataflow API in this way.  
  
## Working with the Geocode Dataflow API  
 The Geocode Dataflow API is a REST web service that allows you to pass in a list of addresses to be geocoded. The API will attempt to geocode each of the requests and, when finished, provide a link to two sets of data: one set of data lists the results of the successfully geocoded addresses, and another lists any addresses that were not geocoded successfully. You can provide this data in XML, CSV, tab-delimited or pipe-delimited formats. The geocoded data is returned in the same format. As explained below, the Geocode Dataflow API requires that you include additional information in your HTTP request beyond the URI with parameters.  
  
 Working with the Geocode Dataflow API involves the following steps:  
  
1.  Start the batch geocode by sending the addresses to be geocoded using the following URI format:  
  
     **Listing 3 - URI format for starting a geocode job with the Geocode Dataflow API**  
  
    ```  
    http://spatial.virtualearth.net/REST/v1/Dataflows/Geocode?description=description&input=input&key=BingMapsKey  
  
    ```  
  
     This call to the Geocode Dataflow API will create a geocode job, which the API will begin processing. You may have up to 10 simultaneously running geocode jobs for a single Bing Maps Key.  
  
2.  Check the status of your job in progress using the following URI format:  
  
     **Listing 4 - URI format for checking the status of a geocode job**  
  
    ```  
    http://spatial.virtualearth.net/REST/v1/Dataflows/Geocode/JobId?key=BingMapsKey  
    ```  
  
     The *JobId* for a geocode job is returned as part of the response when you initially create the job. The status of a geocode job will start out as “Pending” and eventually change to “Completed” when processing is complete.  
  
3.  When the status of your geocode job is set to “Completed”, the result data from the status check in listing 4 will include two links:  
  
    1.  The **succeeded** link will provide a list of result data for all addresses or places that were successfully geocoded.  
  
    2.  The **failed** link will provide a list of addresses or places that could not be successfully geocoded.  
  
### Example: Creating a Geocode Job and Obtaining Results  
 We will now walk through a simple example of how to create a geocode job, check on its status, and obtain results when it has completed.  
  
 We will start with the following data file, which consists of three correctly formatted XML blocks describing three addresses that we want to geocode. To use this data, save it in a file named geocodeFeed.xml.  
  
 **Listing 5 - Sample XML file to be used as input for the Geocode Dataflow API**  
  
```  
<GeocodeFeed>  
  <GeocodeEntity Id="001"  
             xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode">  
    <GeocodeRequest Culture="en US">  
      <Address AddressLine="291 Broadway" AdminDistrict="NY" Locality="New York"  
               PostalCode="10007" />  
    </GeocodeRequest>  
  </GeocodeEntity>  
  <GeocodeEntity Id="002"  
             xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode">  
    <GeocodeRequest Culture="en US">  
      <Address AddressLine="599 Broadway" AdminDistrict="NY" Locality="New York" />  
      <ConfidenceFilter MinimumConfidence="High" xmlns="" />  
    </GeocodeRequest>  
  </GeocodeEntity>  
  <GeocodeEntity Id="003"  
            xmlns="http://schemas.microsoft.com/search/local/2010/5/geocode">  
    <GeocodeRequest Culture="en US" Query="Empire State Building" />  
  </GeocodeEntity>  
</GeocodeFeed>  
  
```  
  
 The Geocode Dataflow API accepts input in the following formats:  
  
-   XML (as shown in Listing 5)  
  
-   Comma-separated values (CSV)  
  
-   Pipe-delimited  
  
-   Tab-delimited  
  
 You can get complete details on the data structure required by the Geocode Dataflow API for all these formats at [Data Schema v1.0](../spatial-data-services/geocode-dataflow-data-schema-version-1-0.md).  
  
 To begin a geocode job, we can use the following PHP code:  
  
 **Listing 6 - Starting a geocode job using the Geocode Dataflow API**  
  
```  
$key = "Insert Your Bing Maps Key Here";  
$url = "http://spatial.virtualearth.net/REST/v1/Dataflows/Geocode?description=MyJob&input=xml&output=xml&key=".$key;  
  
// STEP 1 - Create a geocode job  
  
// Get the contents of an XML data file  
$myfile = "geocodefeed.xml";  
$data = file_get_contents($myfile);  
  
// Call custom function to generate an HTTP request and get back an HTTP response  
$response = do_post_request($url, $data);  
  
// This function constructs and sends an HTTP request with a provided URL and data, and returns an HTTP response object   
// This function uses the php_http extension   
function do_post_request($url, $data, $optional_headers = null)  
{  
  $request = new HttpRequest($url, HttpRequest::METH_POST);  
  $request->setBody($data);  
  $response = $request->send();  
  return $response->getBody();  
}  
```  
  
 The sample code in Listing 6 includes a custom function, **do_post_request**, which generates and sends an HTTP request using the classes provided by the **php_http** extension. If this extension is not included in your version of PHP, you can download it from [http://downloads.php.net/pierre/](http://downloads.php.net/pierre/).  
  
 The $response object returned in Listing 6 is an HTTP response. You can pull information out of it by extracting its body (which is in XML format) and then using the PHP XML classes to extract what you need, as shown in Listing 7.  
  
 **Listing 7 - Working with response data from the Geocode Dataflow request to start a geocode job**  
  
```  
// Convert the response body into an XML element so we can extract data  
$responseBody = new SimpleXMLElement($response);  
  
// Get data (such as job id, status description, and job status) from the response  
$statusDescription = $responseBody->StatusDescription;  
$jobId = $responseBody->ResourceSets->ResourceSet->Resources->DataflowJob->Id;  
$jobStatus = $responseBody->ResourceSets->ResourceSet->Resources->DataflowJob->Status;  
  
echo "Job Created:<br>";  
echo " Request Status: ".$statusDescription."<br>";  
echo " Job ID: ".$jobId."<br>";  
echo " Job Status: ".$jobStatus."<br><br>";  
```  
  
 Once you have started one or more geocode jobs, you can check on their statuses using the URL described in the previous section. You will need a JobId in order to check the status of a job, which you can obtain using the code from Listing 7. For example, the following PHP code checks the status of a specific job, prints the job description and status, and repeats until the status of the job is “Completed” (instead of “Pending”).  
  
 **Listing 8 - Checking the status of your geocode job**  
  
```  
// Call the API to determine the status of all geocode jobs associated with a Bing Maps key  
echo "Checking status until complete...<br>";  
while ($jobStatus != "Completed")   
{  
  // Wait 5 seconds, then check the job’s status  
  sleep(5);  
  
  // Construct the URL to check the job status, including the jobId  
  $checkUrl = "http://spatial.virtualearth.net/REST/v1/Dataflows/Geocode/".$jobId."?output=xml&key=".$key;  
  $checkResponse = file_get_contents($checkUrl);  
  $responseBody = new SimpleXMLElement($checkResponse);  
  
  // Get and print the description and current status of the job    
  $jobDesc = $responseBody->ResourceSets->ResourceSet->Resources->DataflowJob->Description;  
  $jobStatus = $responseBody->ResourceSets->ResourceSet->Resources->DataflowJob->Status;  
  
  echo $jobDesc." - ".$jobStatus."<br>";  
}  
```  
  
 The code in Listing 8 might produce output something like Figure 1.  
  
 **Figure 1 - Output from code to check status of geocode job**  
  
 ![Output from code to check status of geocode job](../articles/media/restphparticlefig3.png "Output from code to check status of geocode job")  
  
 Once you have a job that has completed its run, you can obtain the URL to the successfully geocoded locations (as well as, if needed, the URL for the list of unsuccessful items) from the XML. For example, you could use the PHP code in Listing 9 to obtain the URL to the successfully geocoded results for the geocode job.  
  
 **Listing 9 - Obtaining the URL to the successfully geocoded results for a geocode job**  
  
```  
  
//Iterate through the links provided with the first geocode job and extract the 'succeeded' link  
$Links = $responseBody->ResourceSets->ResourceSet->Resources->DataflowJob->Link;  
foreach ($Links as $Link) {  
  if ($Link['name'] == "succeeded")   
  {   
     $successUrl = $Link;   
     break;   
  }  
}  
```  
  
 Once you have the URL for the successfully geocoded results, you can append your Bing Maps Key to it and send it to the Geocode Dataflow API in order to access the results.  
  
 **Listing 10 - Getting the successfully geocoded results of a job**  
  
```  
// Access the URL for the successful requests, and convert response to an XML element  
$successUrl .= "?output=xml&key=".$key;  
$successResponse = file_get_contents($successUrl);  
$successResponseBody = new SimpleXMLElement($successResponse);  
```  
  
 In Listing 10 we (yet again) convert the results from the Geocode Dataflow API call into an XML element so that we can use the PHP XML API to extract results from it. For example, if you wanted to iterate through all of the successfully geocoded results and print out the geocoded addresses and their coordinates (latitude and longitude), you could use the code shown in Listing 11.  
  
 **Listing 11 - Extracting data from successful geocode job results**  
  
```  
// Loop through the geocoded results and output addresses and lat/long coordinates  
foreach ($successResponseBody->GeocodeEntity as $entity) {  
  echo $entity->GeocodeResponse->Address['FormattedAddress'],"<br>";  
  if (!$entity->GeocodeResponse->RooftopLocation) {  
    echo $entity->GeocodeResponse->InterpolatedLocation['Longitude'].", ";  
    echo $entity->GeocodeResponse->InterpolatedLocation['Latitude']."<br>";  
  }  
  else {  
    echo $entity->GeocodeResponse->RooftopLocation['Longitude'].", ";  
    echo $entity->GeocodeResponse->RooftopLocation['Latitude']."<br>";  
  }  
}  
```  
  
 Note that in Listing 11, we need to check which type of location has been provided with each result. Some results may include Rooftop Location coordinates, while others will have Interpolated Location coordinates. The code in Listing 11 prefers Rooftop Location coordinates, and only prints out Interpolated Location coordinates it the Rooftop ones do not exist.You can find complete information on the Geocode Dataflow API, as well as additional data samples and walkthroughs, in the Bing Spatial Data Services documentation at [Bing Spatial Data Services](../spatial-data-services/index.md).  
  
## Conclusions and Further Reading  
 This article has demonstrated how to use PHP to access the Bing Spatial Data Services Geocode Dataflow API.  
  
 You can find full API documentation for the Bing Spatial Data Services at:  [Bing Spatial Data Services](../spatial-data-services/index.md)  
  
 The author of this article is Craig Wills at [Infusion Development](http://www.infusion.com/).  
  
## Complete PHP Sample Code  
 The following is the complete code sample discussed in this article. This sample runs off the data provided in Listing 5. You must also replace the placeholder text with your Bing Maps Key.  
  
```  
<html>  
  <head>  
    <title>Using the Bing Spatial Data Geocode Dataflow API</title>  
  </head>  
  <body>  
    <?php  
  
$key = "Insert Bing Maps Key Here";  
$url = "http://spatial.virtualearth.net/REST/v1/Dataflows/Geocode?description=MyJob&input=xml&output=xml&key=".$key;  
  
// STEP 1 - Create a geocode job  
  
// Get the contents of an XML data file  
$myfile = "geocodefeed.xml";  
$data = file_get_contents($myfile);  
  
// Call custom function to generate an HTTP request and get back an HTTP response  
$response = do_post_request($url, $data);  
  
// This function constructs and sends an HTTP request with a provided URL and data, and returns an HTTP response object  
// This function uses the php_http extension   
function do_post_request($url, $data, $optional_headers = null) {  
  $request = new HttpRequest($url, HttpRequest::METH_POST);  
  $request->setBody($data);  
  $response = $request->send();  
  return $response->getBody();  
}  
  
// Convert the response body into an XML element so we can extract data  
$responseBody = new SimpleXMLElement($response);  
  
// Get data (such as job id, status description, and job status) from the response  
$statusDescription = $responseBody->StatusDescription;  
$jobId = $responseBody->ResourceSets->ResourceSet->Resources->DataflowJob->Id;  
$jobStatus = $responseBody->ResourceSets->ResourceSet->Resources->DataflowJob->Status;  
  
echo "Job Created:<br>";  
echo " Request Status: ".$statusDescription."<br>";  
echo " Job ID: ".$jobId."<br>";  
echo " Job Status: ".$jobStatus."<br><br>";  
  
// STEP 2 - Get the status of geocode job(s)  
  
// Call the API to determine the status of all geocode jobs associated with a Bing Maps key  
echo "Checking status until complete...<br>";  
while ($jobStatus != "Completed") {  
  
  // Wait 5 seconds, then check the job’s status  
  sleep(5);  
  
  // Construct the URL to check the job status, including the jobId  
  $checkUrl = "http://spatial.virtualearth.net/REST/v1/Dataflows/Geocode/".$jobId."?output=xml&key=".$key;  
  $checkResponse = file_get_contents($checkUrl);  
  $responseBody = new SimpleXMLElement($checkResponse);  
  
  // Get and print the description and current status of the job    
  $jobDesc = $responseBody->ResourceSets->ResourceSet->Resources->DataflowJob->Description;  
  $jobStatus = $responseBody->ResourceSets->ResourceSet->Resources->DataflowJob->Status;  
  
  echo $jobDesc." - ".$jobStatus."<br>";  
  
}  
  
// STEP 3 - Obtain results from a successfully geocoded set of data  
  
//Iterate through the links provided with the first geocode job and extract the 'succeeded' link  
$Links = $responseBody->ResourceSets->ResourceSet->Resources->DataflowJob->Link;  
foreach ($Links as $Link) {  
  if ($Link['name'] == "succeeded")   
  {   
    $successUrl = $Link;   
    break;   
  }  
}  
  
// Access the URL for the successful requests, and convert response to an XML element  
$successUrl .= "?output=xml&key=".$key;  
$successResponse = file_get_contents($successUrl);  
$successResponseBody = new SimpleXMLElement($successResponse);  
  
// Loop through the geocoded results and output addresses and lat/long coordinates  
foreach ($successResponseBody->GeocodeEntity as $entity) {  
  echo $entity->GeocodeResponse->Address['FormattedAddress'],"<br>";  
  if (!$entity->GeocodeResponse->RooftopLocation) {  
    echo $entity->GeocodeResponse->InterpolatedLocation['Longitude'].", ";  
    echo $entity->GeocodeResponse->InterpolatedLocation['Latitude']."<br>";  
  }  
  else {  
    echo $entity->GeocodeResponse->RooftopLocation['Longitude'].", ";  
    echo $entity->GeocodeResponse->RooftopLocation['Latitude']."<br>";  
  }  
}  
  
?>  
  
  </body>  
</html>  
```