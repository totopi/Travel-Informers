// All the scripts!

// Use the route /city to populate our dropdown menu for cities
let citySelect = document.querySelector("#citySelect");
d3.json("/city", function(error, cities) {
    console.log(cities);
    if (error) throw error;
    let longness = cities.length;
    for (let i = 0; i < longness; i++) {
        if (cities[i]["country"] === "United States") {
            let city = d3.select("#selCity").append("option").attr("value", cities[i]["city_name"]).text(cities[i]["city_name"]);
        }//citySelect.append(city);
    }
})

// Initialize our graphs
function initGraphs() {
    let url = "/Portland/05/temp"

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
initGraphs()