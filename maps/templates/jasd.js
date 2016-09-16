/**
 * Created by jane on 10.09.16.
 */


map = new OpenLayers.Map('map');
var bounds = new OpenLayers.Bounds(41, 44, 48, 48);
var graphic;
graphic = new OpenLayers.Layer.GML(
    "OpenLayers KML",
    "http://localhost:8080/geoserver/geonode/wms?service=WMS&version=1.1.0&request=GetMap&layers=geonode:app_map_worldborderl&styles=&bbox=-181.800003051758,-90.8681182861328,181.800003051758,84.4917144775391&width=768&height=370&srs=EPSG:42310&format=application/openlayers",
    {format: OpenLayers.Format.KML};
graphic.setIsBaseLayer(true);
map.addLayers([graphic]);
map.zoomToExtent(bounds);
