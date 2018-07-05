function renderTable(results) {
    var url = "/api/temperatures";

    var width = 960;
    var height = 700;

    Plotly.d3.json(url, function(error, avgTemps) {
    	// setTable('United States');

        var values = [
        	[],
        	[],
        	[],
        	[],
        ];

        for (var i = 1; i < 500; i++) {

            values[0].push(avgTemps[i][0]);
            values[1].push(avgTemps[i][1]);
            values[2].push(avgTemps[i][2]);
            values[3].push(avgTemps[i][3]);

        };
        console.log(values);

        var headerColor = "steelblue";
        
        var data = [{
            type: 'table',
            columnorder: [1, 2, 3, 4],
            columnwidth: [75, 175, 175, 175],
            header: {
                values: ['ID', 'Country', 'Year', 'Avg Temp'],		   
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

        function setTable(countryName) {
        	var url = "/countries/<countryName>";
            Plotly.d3.json(url, function(error, groupByCountry) {
            	console.log(groupByCountry);
        		var width = 960;
            	var height = 700;
        	    
        	    var values = [
        	    	[],
        	    	[],
        	    	[],
        	    	[],
        	    	[],
        	    ];

        	    for (var i = 1; i < groupByCountry[i][1]; i++) {

        	        values[0].push(groupByCountry[i][0]);
        	        values[1].push(groupByCountry[i][1]);
        	        values[2].push(groupByCountry[i][2]);
        	        values[3].push(groupByCountry[i][3]);
        	        values[4].push(groupByCountry[i][4]);

        	    };
        	    console.log(values);

        	    var headerColor = "steelblue";	    

        	    var data = [{
        	        type: 'table',
        	        columnorder: [1, 2, 3, 4, 5],
        	        columnwidth: [120, 120, 120, 120, 120],
        	        header: {
        	            values: ['Country', 'Avg Temp', 'Max Avg', 'Min Avg', 'Difference'],
        	            // values: headerValues,		   
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
        	    Plotly.newPlot(TABLE, data);        	      		
    
			    var innerContainer = document.querySelector(groupByCountry[0][1]),
			    	plotEl = innerContainer.querySelector('.plot'),
			    	countrySelector = innerContainer.querySelector('.groupByCountry');

			    function assignOptions(textArray, selector) {
			    	for (var i = 0; i < textArray.length; i++) {
			    		var currentOption = document.createElement('optionB');
			    		currentOption.txt = textArray[i];
			    		selector.appendChild(currentOption);
			    	}
			    }

			    assignOptions(values[1], countrySelector);

			    function updateCountry() {
			    	setTable(countrySelector.value);
			    }

			    countrySelector.addEventListener('change',updateCountry,false); 
			});
        };
        setTable();
	});  
     
}
renderTable();














function dropDown() {
    var url = "/countries/<countryName>";
    Plotly.d3.json(url, function(error, groupByCountry) {

        for (i = 1; i < groupByCountry[i][1]; i++) {
            var option = $('<option></option>').text(groupByCountry[i][1])
            $('select').append(option);
        }

    });
}
dropDown();

// function getGroupByCountry() {
// 	var url = "/countries";
// 	$('select').bind('click', function() {
// 		getJson(url,
// 			renderTable("#country")
// 			)
// 	});
// }
