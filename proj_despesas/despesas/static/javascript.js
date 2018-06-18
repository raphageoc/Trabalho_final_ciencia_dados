

// adiciona o slider time
 // $("#slider").dateRangeSlider();
 // $("#slider").editRangeSlider({
 //  defaultValues:{
 //    min: new Date(2012, 8, 1),
 //    max: new Date(2018, 5, 31)
 //  }});


var months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"];
  $("#slider").dateRangeSlider({
    bounds: {min: new Date(2012, 0, 1), max: new Date(2018, 11, 31,)},
    defaultValues: {min: new Date(2012, 1, 10), max: new Date(2015, 4, 22)},
    scales: [{
      first: function(value){ return value; },
      end: function(value) {return value; },
      next: function(value){
        var next = new Date(value);
        return new Date(next.setMonth(value.getMonth() + 1));
      },
      label: function(value){
        return months[value.getMonth()];
      },
      format: function(tickContainer, tickStart, tickEnd){
        tickContainer.addClass("myCustomClass");
      }
    }]
  });

// pegar valores minimos e maximos do dateRangeSlider



// funcao transformar a data javascript para python
function trans_data(D){
  var y = D.getFullYear()
  var m = D.getMonth()+1
  var d = D.getDate()
  Data = y + '-' +  m + '-' + d
  return Data
}

function alerta_data (){
// var dateSliderMax = $("#slider").dateRangeSlider("max");
var basicValues = $("#slider").dateRangeSlider("values");
var opcao= document.getElementById("tema").value;




}


 // funcao para popular um dropdown
 function popula_tema(o){
   var $seletor = $("#tema");
   $.each(o, function() {
       $seletor.append($("<option />").val(this).text(this));
     }
   );
 }


// instanciar um novo objeto mapa
  var map = L.map("map", {
    center: [-25.45, -49.25],
    zoom: 14,

  });

  // adicionar uma camada osm ao map
  var osmColorido = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(map);

  // adicionar um layer geojson vazio

  var layer_geojson = L.geoJson();

// funçao para adicionar o geodjson ao mapa
  function add_geojson (f){




    var geojsonMarkerOptions = {
    radius: 8,
    fillColor: "#ff7800",
    color: "#000",
    weight: 1,
    opacity: 1,
    fillOpacity: 0.8
};

    var geo = f;
    layer_geojson.clearLayers();

    layer_geojson = L.geoJSON(geo, {

		style: function (feature) {
			return feature.properties && feature.properties.style;
		},
    onEachFeature: function (feicao, camada){
  	    camada.bindTooltip(feicao.properties.nome_empresa +" " +feicao.properties.sum)
        return L.circleMarker(camada, geojsonMarkerOptions)},

		pointToLayer: function (feature, latlng) {
      // var r=0;
      // 	if (Math.ceil(100 * (feature.properties.sum/feature.properties.max) ) <20) { r = Math.ceil(100 * (feature.properties.sum/feature.properties.max)/10};
      //   if (Math.ceil(100 * (feature.properties.sum/feature.properties.max) ) >=20 && (Math.ceil(100 * (feature.properties.sum/feature.properties.max) ) <65 )) { r = 20};
      //   if (Math.ceil(100 * (feature.properties.sum/feature.properties.max) ) >=65 && (Math.ceil(100 * (feature.properties.sum/feature.properties.max) ) <101 )) { r = 30};
			return L.circleMarker(latlng, {
			radius: Math.ceil(100 * (feature.properties.sum/feature.properties.max))/5,
				fillColor: "#ff7800",
				color: "#000",
				weight: 1,
				opacity: 1,
				fillOpacity: 0.8
			});
		}
	}).addTo(map);
   map.fitBounds(layer_geojson.getBounds());


  };
// PEGAR MAXIMO E MINIMO JSON


// funcao ajax para enviar parametros pro python e retornar geojson
 function Consulta_tema_data () {

    var basicValues = $("#slider").dateRangeSlider("values");
    var opcao= document.getElementById("tema").value;
    var data_inicial = trans_data(basicValues.min);
    var data_final = trans_data(basicValues.max);



    $.get('consulta', {consulta_tema: opcao, d_i:data_inicial, d_f:data_final }, function(data){

      add_geojson(data)
    }
  )
}
