


function renderTable() {
    var url = "/api/temperatures";

    var width = 960;
    var height = 960;

    Plotly.d3.json(url, function(error, avgTemps) {
        console.log(avgTemps);
        // setTable('United States');

        var values = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        ];

		avgTemps.forEach((row, i) => {
			row.forEach((col, j) => {
				values[j].push(row[j])
			})
		})

        var headerColor = "steelblue";
        var data = [{
            type: 'table',
            columnorder: [1, 2, 3, 4, 5, 6, 7],
            columnwidth: [70, 105, 105, 105, 105, 105, 105],
            header: {
                values: ['ID', 'Country', 'Year', 'Avg Temp', 'High', 'Low', 'Difference'],
                align: "center",
                height: 28,
                line: { width: 1, color: 'black' },
                fill: { color: headerColor },
                font: { family: "Raleway", size: 12, color: "white" }
            },
            cells: {
                values: values,
                align: "center",
                height: 25,
                line: { color: "black", width: 1 },
                fill: {
                    color: ['rgb(244,109,67)', 'rgb(254,224,144)']
                },
                font: { family: "Raleway", size: 11, color: ["black"] }
            }
        }]

        var TABLE = document.getElementById('table');
        Plotly.plot(TABLE, data);

		function getCountry(countryName) {
			var url = "/countries/<countryName>";
			Plotly.d3.json(url, function(error, results) {
				console.log(results);

				var values = [
				    [],
				    [],
				    [],
				    [],
				    [],
				    [],
				    [],
				];

				results.forEach((row, i) => {
					row.forEach((col, j) => {
						values[j].push(row[j])
					})
				})
			});
		};

		function setTable(countryName) {
			getCountry(countryName);

			var headerColor = "steelblue";
	        var data = [{
	            type: 'table',
	            columnorder: [1, 2, 3, 4, 5, 6, 7],
	            columnwidth: [70, 105, 105, 105, 105, 105, 105],
	            header: {
	                values: ['ID', 'Country', 'Year', 'Avg Temp', 'High', 'Low', 'Difference'],
	                align: "center",
	                height: 28,
	                line: { width: 1, color: 'black' },
	                fill: { color: headerColor },
	                font: { family: "Raleway", size: 12, color: "white" }
	            },
	            cells: {
	                values: values,
	                align: "center",
	                height: 25,
	                line: { color: "black", width: 1 },
	                fill: {
	                    color: ['rgb(244,109,67)', 'rgb(254,224,144)']
	                },
	                font: { family: "Raleway", size: 11, color: ["black"] }
	            }
	        }]
	        Plotly.newPlot(TABLE, data);

		};
		var innerContainer = document.querySelector('[data-num="0"'),
			plotEl = innerContainer.querySelector('.table'),
			getCountry = innerContainer.querySelector('.dropdown-item');

		function assignOptions(textArray, selector) {
			for (var i = 0; i < textArray.length; i++) {
				var currentOption = document.createElement('optionB');
				currentOption.txt = textArray[i];
				selector.appendChild(currentOption);
			}
		}
		
		assignOptions(countrySelector);

		function updateCountry() {
			setTable(countrySelector.value);
		}

		countrySelector.addEventListener('change',updateCountry, false);

    });
}


renderTable();


function dropDown() {
    var url = "/countryName/<countryName>";
    Plotly.d3.json(url, function(error, results) {
        console.log(results)

        for (i = 0; i < 100; i++) {
            var option = $('<option></option>').text(results[0])
            $('select').append(option);
        }

    });
}
// dropDown();

// function getGroupByCountry() {
// 	var url = "/countries";
// 	$('select').bind('click', function() {
// 		getJson(url,
// 			renderTable("#country")
// 			)
// 	});
// }