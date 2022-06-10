---
title: CaptureScreenshotListener Interface | Microsoft Docs
description: Describes the CaptureScreenshotListener interface for Android and provides the syntax for the interface and the MapView resource.
ms.author: pablocan
---

# CaptureScreenshotListener Interface (Android only)

Callback interface to notify when a Bitmap has been captured as a result of a call to MapView.captureImage.

>```java
> public interface CaptureScreenShotListener
> {
>     void onCaptureScreenShot(@Nullable android.graphics.Bitmap bitmap);
> }
>```

## See Also

* [MapView](../MapView-class.md)
