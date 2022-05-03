---
title: "Cross Platform Bing Maps V8 apps | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 89a7e744-eca7-4023-8309-db70225518fb
caps.latest.revision: 5
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Cross Platform Bing Maps V8 apps

The Bing Maps V8 web control has been designed to work well on mobile devices that support HTML5. Mobile devices typically have high resolution screens and limited computing power. As such the Bing Maps V8 control adapts to mobile environments by automatically doing the following:

* Enables the **liteMode** map option which disables vector labels and instead renders the map labels server side on the map tiles. You can override this behavior by setting this value to false when loading the map.
* The navigation bar (zoom buttons and map type dropdown) will switch into the **compact** [NavigationBarMode](../map-control-api/navigationbarmode-enumeration.md) which uses less space than the default navigation bar and is better suited for mobile apps.
* The map will load High DPI map tiles when the map is used on a high resolution screen.

A complete list of supported browsers can be found [here](../supported-browsers.md).

## Viewport metatag

The following viewport should be used in mobile apps.

```xml
<meta name="viewport" content="user-scalable=no, initial-scale=1, maximum-scale=1, minimum-scale=1, width=device-width"/>
```

This setting specifies that the map should be displayed full-screen and should not be resizable by the user. Note that the iPhone's Safari browser requires this &lt;meta&gt; tag be included within the page's &lt;head&gt; element.

## Location Capability

Ensure to enable the location capability in your app. If you don’t then hide the user location button that appears on the map by setting the **showLocateMeButton** map option to false.

## Security

Many platforms now have added security which blocks calls to external resources in HTML based apps. As such the URL domains used by Bing Maps must be allowlisted. Unfortunately, not all platforms handle allowlisting in the same way. All Bing Maps services use one of the following domains, often with one or more subdomains.

* https://\*.bing.com
* https://\*.virtualearth.net

## UWP Apps (JavaScript)

There are two ways to get Bing Maps V8 to run inside of a JavaScript based UWP app. The first is to host your map code inside of an iframe. This works fine if your map functionality is completely contained and you don't need to programmatically make changes to the map from your main app. UWP apps don’t allow communicating between the main app and JavaScript code in an iframe.

The second is to modify how you reference the start page in your app and instead of using a local context, use a web context. To do this, open the package.appxmanifest, and add "ms-appx-web:///" before the start page value. Likely "ms-appx-web:///index.html". This may limit your application from using some of the lower level features in JavaScript based UWP apps, like accessing the file system.

In both of these scenarios, add the following content URI's and set WinRT access to "All"; "https://*.bing.com" and "https://*.virtualearth.com" .

## Native UWP Apps via Apache Cordova

To allowlist these domains in a native Windows 10, open the **config.xml** file in your Cordova project and near top of the file you should see "&lt;access origin="\*" /&gt;" after this line add the following two lines:

```xml
<access origin="*.bing.com" subdomains="true" />
<access origin="*.virtualearth.net" subdomains="true" />
```

If you project doesn’t work after allowlisting these URLs ensure that the version of Windows that your app targets is 10. There is a preference property in the **config.xml** file that specifies the target version of Windows. Make sure it is set to 10.0 like this:

```xml
<preference name="windows-target-version" value="10.0" />
```

> [!TIP]
> If you are using Visual Studio and seeing a deployment error when trying to deploy to your Windows Phone, make sure the target platform in the build configuration of your project is set to Windows Phone (Universal).

> [!NOTE]
> It is possible to use the Bing Maps V8 control in a UWP app by hosting it inside of a WebView control and creating a communication layer to connect your .NET code to the JavaScript in a similar manner as discussed in the Using Bing Maps V8 in WinForm and WPF Apps section of this document. However, this is essentially what Apache Cordova does, so you may want to consider using that instead.

## iOS, Android and some Web Apps

Allowlisting is done using a Content Security Policy (CSP). The following CSP works well for iOS and Android apps.

```xml
<meta http-equiv="Content-Security-Policy" content="default-src 'self' data: gap: https://ssl.gstatic.com 'unsafe-eval' 'unsafe-inline' https://*.bing.com https://*.virtualearth.net; style-src 'self' 'unsafe-inline' https://*.bing.com https://*.virtualearth.net; media-src *">
```

## Sample Mobile HTML Page

Putting together the best practices mentioned above here is a simple code sample that loads a full screen map in a Cordova app.

```html
<!DOCTYPE html>
<html>
    <head>
        <title></title>

        <meta http-equiv="Content-Security-Policy" content="default-src 'self' data: gap: https://ssl.gstatic.com 'unsafe-eval' 'unsafe-inline' https://*.bing.com https://*.virtualearth.net; style-src 'self' 'unsafe-inline' https://*.bing.com https://*.virtualearth.net; media-src *">
        
        <meta name="viewport" content="user-scalable=no, initial-scale=1, maximum-scale=1, minimum-scale=1, width=device-width">

        <script type='text/javascript' src='https://www.bing.com/api/maps/mapcontrol?callback=GetMap' async defer></script>
        <script>
            var map;

            function GetMap() {
                map = new Microsoft.Maps.Map('#myMap', {
                    credentials: 'Your Bing Maps Key'
                });
            }
        </script>
        <style>
            body, html{
                padding:0;
                margin:0;
            }
        </style>
    </head>
    <body>
        <div id="myMap"></div>
    </body>
</html>
```

Some legacy web apps and environments may automatically run in compatibility mode. 

```xml
<meta charset="utf-8" http-equiv="X-UA-Compatible" content="IE=edge" />
```

## Using Bing Maps V8 in WinForm and WPF Apps

It is possible to add the Bing Maps V8 control to a WinForm or WPF app by hosting it in a WebBrowser control. The map code would still be in JavaScript, but it is possible to create a communication layer between your .NET code and JavaScript code. To call JavaScript from your .NET code the browsers [InvokeScript method](https://msdn.microsoft.com/library/4b1a88bz(v=vs.110).aspx) can be used. To send information from JavaScript back to your .NET code a [scripting object](https://msdn.microsoft.com/library/system.windows.forms.webbrowser.objectforscripting(v=vs.110).aspx) can be specified for the browser.

By default, the WebBrowser control in WinForm and WPF apps does not use the latest version of Internet Explorer and often uses a version that doesn’t support HTML5. As such, you need to add a metatag to the head of your HTML file which forces the browser to use the latest version of Internet Explorer available on the user’s machine.

```xml
<meta charset="utf-8" http-equiv="X-UA-Compatible" content="IE=edge" />
```

Here is a full code sample on [Using the Bing Maps V8 Web control in a WinForm application](https://code.msdn.microsoft.com/Using-the-Bing-Maps-V8-Web-07e21f3a?redir=0).
