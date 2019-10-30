---
title: "CaptureScreenshotListener Interface | Microsoft Docs"
author: "pablocan"
---

# CaptureScreenshotListener Interface (Android only)

Callback interface to notify when a Bitmap has been captured as a result of a call to MapView.captureImage.

>```java
> public interface CaptureScreenShotListener
> {
>     public void onCaptureScreenShot(android.graphics.Bitmap bitmap);
> }
>```

## See also

* [MapView](../MapView-class.md)