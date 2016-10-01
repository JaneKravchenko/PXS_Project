
            var checkList = document.getElementById('list');
        checkList.getElementsByClassName('anchor')[0].onclick = function (evt) {
            if (checkList.classList.contains('visible'))
                checkList.classList.remove('visible');
            else
                checkList.classList.add('visible');

        };

        checkList.onblur = function(evt) {
            checkList.classList.add('visible');
        };


          var map = new OpenLayers.Map('map');
        var baseUrl = window.location.protocol + '//' + window.location.host;
        map.addControl(new OpenLayers.Control.LayerSwitcher({'ascending':false}));

        map.addControl(new OpenLayers.Control.OverviewMap());
        map.addControl(new OpenLayers.Control.KeyboardDefaults() );
map.addControl(new OpenLayers.Control.Attribution());
            map.addControl(new OpenLayers.Control.MousePosition() );
 map.addControl(new OpenLayers.Control.EditingToolbar([]));




           map.addControl(new OpenLayers.Control.ScaleLine());
            var gsat = new OpenLayers.Layer.Google(
        "Google Satellite",
        {type: google.maps.MapTypeId.SATELLITE, numZoomLevels: 22, tiled:true}
    );


 var wms = new OpenLayers.Layer.WMS( "OpenLayers WMS",
  "http://vmap0.tiles.osgeo.org/wms/vmap0",
  {'layers':'basic', 'projection': 'map.displayProjection', tiled: true} );

  tiled = new OpenLayers.Layer.WMS(
                    "pixelsolution:gtif - Tiled", "http://localhost:8080/geoserver/pixelsolution/wms",
                    { transparent: 'true', layers:'pixelsolution:gtif',
        format: "image/png", tiled:true});
	map.addLayers([wms, tiled]);


    map.setCenter(new OpenLayers.LonLat(30.59200, 48.46603), 13); */
