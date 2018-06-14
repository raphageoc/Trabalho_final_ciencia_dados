
var myLayer;
var x;
var geo;


  var map = L.map("map", {
    center: [-25.45, -49.25],
    zoom: 14,

  });




  add_osm()
  function add_geojson (f){
    geo = f;
    x = L.geoJSON(geo);
    x.addTo(map);
  };






function add_osm ()
{
  var osmColorido = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(map);
};
