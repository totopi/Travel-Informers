

d3.json("/city", function(data) {
    makeMap(data);
})

function makeMap(data) {
    console.log(data);

    let markers = [];
    for (let i = 0, ii = data.length; i < ii; i++) {
        let datum = data[i];
        markers.push(
            L.marker([datum.lat, datum.lon], {
                draggable: false,
                title: datum.city_name
            }).bindPopup(`<strong>${datum.city_name}, ${datum.country}</strong><hr>`)
        )
    }

    let startCoords = [34.052231, -118.243683];
    let startZoom = 6;

    let streetMap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoidG90b3BpIiwiYSI6ImNqaDFhaGh6ejAxcW4yeHJ5aDl4bjZ2YngifQ.ssPdnszdafCcNm4753AVJA");

    let darkMap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/dark-v9/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoidG90b3BpIiwiYSI6ImNqaDFhaGh6ejAxcW4yeHJ5aDl4bjZ2YngifQ.ssPdnszdafCcNm4753AVJA");

    let cityLayer = L.layerGroup(markers);

    let baseMaps = {
        "Street Map": streetMap,
        "Dark Map": darkMap
    };

    let overlayMaps = {
        "Cities": cityLayer
    };

    let myMap = L.map('map', {
        center: startCoords,
        zoom: startZoom,
        layers: [streetMap, cityLayer]
    });
    L.control.layers(baseMaps, overlayMaps).addTo(myMap);

}