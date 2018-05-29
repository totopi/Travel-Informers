// All the scripts!

// Use the route /city to populate our dropdown menu for cities
let citySelect = document.querySelector("#citySelect");
d3.json("../static/data/city.json", function(error, cities) {
   // console.log(cities);
    if (error) throw error;
    let longness = cities.length;
    for (let i = 0; i < longness; i++) {
        if (cities[i]["country"] === "United States") {
            let city = d3.select("#selCity").append("option").attr("value", cities[i]["city_name"]).text(cities[i]["city_name"]);
        }//citySelect.append(city);
    }
});
let monthsList = [ 'January',
'February',
'March',
'April',
'May',
'June',
'July',
'August',
'September',
'October',
'November',
'December' ];

let monthSelect = document.querySelector("#monthSelect");
for (let i = 0; i < monthsList.length; i++) {
            d3.select("#selMonth")
            .append("option")
            .attr("value", monthsList[i])
            .text(monthsList[i])
        };

let typesList = ["temp", "wind", "humidity"]
let dataSelect = document.querySelector("#dataSelect");
for (let i = 0; i < typesList.length; i++) {
    d3.select("#selType")
    .append("option")
    .attr("value", typesList[i])
    .text(typesList[i])
};





// Initialize our graphs
function initGraphs(selectedCity, selectedMonth, selectedType) {
    // let url = `/${city}/${month}/${data_set}`
    let url = "../static/data/json.json"

    d3.json(url, function(json) {
        
        // First Graph
        let layout = {
            title: "Temperature vs Date", 
            xaxis: {
                title: "Dates",
            },
            yaxis: {
                title: "Temperature, Degrees Fahrenheit"
            }

        };
        Plotly.newPlot('first_graph', json[0], layout);

        // Second Graph 
        let layout2 = {
            title: "Temperature vs Number of Airport Delays",
            xaxis: {
                title: "Temperature"
            },
            yaxis: {
                title: "Number of Airport Delays"
            },
        };

        Plotly.newPlot('second_graph', json[1], layout2);

        // Third Plot
        let pie_layout = {
            title: "Frequency of Weather Conditions in Portland",
            height: 700,
            width: 800
        };
        Plotly.newPlot("third_graph", json[2], pie_layout)
    });
}
initGraphs("Portland", 05, "temp")

function cityChanged(selectedCity) {
    console.log(selectedCity)   
    let month = 05
    let type = "temp"
    // let url = `/${selectedCity}/${month}/${type}`
    let url = "../static/data/json.json"

    let lineDiv = document.getElementById("first_graph");
    d3.json(url, function(json) {
        Plotly.restyle(lineDiv, json[0])
    })
};

/*Example to Follow: 
 function updatePlotly(sample_id){
    let pieDiv = document.getElementById("pie_chart");
    let bubbleDiv = document.getElementById("bubble_chart")

        let url4 = `http://127.0.0.1:5000/samples/${sample_id}`
                      d3.json(url4, function(json_Data){

        let new_sample_values = json_Data[1].sample_values.slice(0,10);
        let new_otu_ids = json_Data[0].otu_ids.slice(0,10);

        Plotly.restyle(pieDiv, "values", [new_sample_values]);
        Plotly.restyle(pieDiv, "labels", [new_otu_ids]);
        Plotly.restyle(bubbleDiv, "x", [new_otu_ids]);
        Plotly.restyle(bubbleDiv, "y", [new_sample_values]);
        Plotly.restyle(bubbleDiv, "marker.size", [new_sample_values]);
        Plotly.restyle(bubbleDiv, 'marker.color', [new_otu_ids]);
  })
}; */