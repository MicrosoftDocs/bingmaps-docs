
# OnMapDoubleTappedListener interface (Android only)

Listener used with MapView.DoubleTapped event. Return true from this event to prevent other OnMapDoubleTappedListeners from receiving this event or false to allow other listeners to receive his notification as well. Events are processed in the order they were attached to the MapView.

>```java
> public interface OnMapDoubleTappedListener
> {
>     /** Called when map is double tapped. */
>     public boolean onMapDoubleTapped(MapDoubleTappedEventArgs e);
> }
>```

## See also

* [MapDoubleTappedEventArgs](MapDoubleTappedEventArgs-class.md)
* [MapView](../MapView-class.md)