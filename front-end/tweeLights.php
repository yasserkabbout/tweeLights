<!doctype html>
<html lang="en">




<head>
	<meta charset="utf-8" />
	<link rel="icon" type="image/png" href="assets/img/favicon.ico">
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
	
	<title>tweeLights Contest Overview!</title>

	<meta content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0" name="viewport" />
    
    <link href="assets/css/bootstrap.css" rel="stylesheet" />
    <link href="assets/css/fresh-bootstrap-table.css" rel="stylesheet" />

    <!--     Fonts and icons     -->
    <link href="http://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">
    <link href='http://fonts.googleapis.com/css?family=Roboto:400,700,300' rel='stylesheet' type='text/css'>
        
</head>
<body>







<div class="wrapper">
    <div class="fresh-table full-color-azure full-screen-table">
    <!--    Available colors for the full background: full-color-blue, full-color-azure, full-color-green, full-color-red, full-color-orange                  
            Available colors only for the toolbar: toolbar-color-blue, toolbar-color-azure, toolbar-color-green, toolbar-color-red, toolbar-color-orange
    -->
        
        <div class="toolbar">
            <button id="alertBtn" class="btn btn-default">About</button>
        </div>
        
        <table id="fresh-table" class="table">
            <thead>
                <th data-field="id">ID</th>
            	<th data-field="name" data-sortable="true">Name</th>
            	<th data-field="salary" data-sortable="true">Country</th>
            	<th data-field="country" data-sortable="true">City</th>
            	<th data-field="city">Winner Color</th>
            	<th data-field="actions" data-formatter="operateFormatter" data-events="operateEvents">Share</th>
            </thead>
            <tbody>
                <tr>
                	<td>1</td>
                	<td>Amazon</td>
                	<td>America</td>
                	<td>Ny</td>
                	<td> 





<?php
$username = "yasser";
$password = "yasser";
$hostname = "yasserkabboutcom.ipagemysql.com"; 

//connection to the database
$dbhandle = mysql_connect($hostname, $username, $password) 
  or die("Unable to connect to MySQL");
$selected = mysql_select_db("twee_lights",$dbhandle) 
  or die("Could not select examples");
$result = mysql_query("SELECT winner_color FROM winners_colors WHERE store_id=1 order by record_id DESC limit 1;");
while ($row = mysql_fetch_object($result)) {
    echo $row->winner_color;
    
}

mysql_close($dbhandle);

?>





                            </td>
                	<td></td>
                </tr>
                <tr>
                	<td>2</td>
                	<td>eBay</td>
                	<td>Australia</td>
                	<td>Sydney</td>
                	<td>YELLOW</td>
                	<td></td>
                </tr>

<tr>
                	<td>3</td>
                	<td>Pending Store</td>
                	<td>Turkey</td>
                	<td>Istanbul</td>
                	<td>Awaiting RaspberryPi installation</td>
                	<td></td>
                </tr>

<tr>
                	<td>4</td>
                	<td>Pending Store</td>
                	<td>Turkey</td>
                	<td>Antalya</td>
                	<td>Awaiting RaspberryPi installation</td>
                	<td></td>
                </tr>

<tr>
                	<td>5</td>
                	<td>Pending Store</td>
                	<td>Turkey</td>
                	<td>Ankara</td>
                	<td>Awaiting RaspberryPi installation</td>
                	<td></td>
                </tr>

<tr>
                	<td>6</td>
                	<td>Pending Store</td>
                	<td>Lebanon</td>
                	<td>Beirut</td>
                	<td>Awaiting RaspberryPi installation</td>
                	<td></td>
                </tr>

<tr>
                	<td>7</td>
                	<td>Pending Store</td>
                	<td>Lebanon</td>
                	<td>Tripoli</td>
                	<td>Awaiting RaspberryPi installation</td>
                	<td></td>
                </tr>


<tr>
                	<td>8</td>
                	<td>Pending Store</td>
                	<td>AU</td>
                	<td>Melbourne</td>
                	<td>Awaiting RaspberryPi installation</td>
                	<td></td>
                </tr>

<tr>
                	<td>9</td>
                	<td>Pending Store</td>
                	<td>Kuwait</td>
                	<td>Kuwait City</td>
                	<td>Awaiting RaspberryPi installation</td>
                	<td></td>
                </tr>






            </tbody>


        </table>






    </div>
<div style="background-color: rgb(255, 255, 255);">
<div style="width: 900px;
    padding: 0px;
background-color: rgb(255, 206, 147),
   height:200px;
    margin: 0 auto;">
<canvas id="myChart" width="50" height="35"></canvas>
</div>
</div>

<div style="
    
background: black;
   height:40px;">
<p style="text-align:center;color:white;padding:10px;margin:auto;">A Project Developed from Scratch by <a href="https://www.linkedin.com/in/yasserkabbout/">Yasser El Kabbout</a></p>

</div>

    
</div>

<?php

$username = "yasser";
$password = "yasser";
$hostname = "yasserkabboutcom.ipagemysql.com"; 
$xAxisData= array();

//connection to the database
$dbhandle = mysql_connect($hostname, $username, $password) 
  or die("Unable to connect to MySQL");
$selected = mysql_select_db("twee_lights",$dbhandle) 
  or die("Could not select examples");
$result = mysql_query("SELECT winner_color, record_date FROM winners_colors WHERE store_id=1;");

while($row=mysql_fetch_assoc($result)) 
        {
     
           
            array_push($xAxisData,$row);
        }



//mysql_close($dbhandle);




?>





<script type="text/javascript" src="assets/js/Chart.js"></script>




<script>


var xAxisData= <?php 





echo json_encode($xAxisData); ?>;

console.log(xAxisData);

var xAxisDate=[];
var yAxisColor=[];


for (var i = 0; i < xAxisData.length; i++) {
    
    xAxisDate.push(xAxisData[i].record_date);
    yAxisColor.push(xAxisData[i].winner_color);
   
}

for(var i=0; i<yAxisColor.length; i++){

if(yAxisColor[i]==="RED")
yAxisColor[i]=1;

if(yAxisColor[i]==="GREEN")
yAxisColor[i]=2;


if(yAxisColor[i]==="YELLOW")
yAxisColor[i]=3;


}

for(var i=0; i<yAxisColor.length; i++){

console.log(yAxisColor[i]);


}



var ctx = document.getElementById('myChart').getContext('2d'); 
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: xAxisDate,
        datasets: [{
            label: 'Color Id: 1-RED | 2-GREEN | 3-YELLOW',
	    backgroundColor: 'rgb(48, 139, 233)',
	    steppedLine: true,
	    fill: false,
	    
         
            borderColor: 'rgb(48, 139, 233)',
            data: yAxisColor,
        }]
    },

    // Configuration options go here
    options: {

	

   responsive: true,
            legend: {
                display: true
            },
            title: {
                display: true,
                text: 'Color Variation over time for the Amazon Store'
            },
            animation: {
                animateScale: true
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: false,
			labelString: 'Color Id: 1->RED | 2->GREEN | 3->YELLOW',
					
                      
                        stepSize: 1
                    }
                }]
            }














}
});</script>












</body> 


    <script type="text/javascript" src="assets/js/jquery-1.11.2.min.js"></script>
    <script type="text/javascript" src="assets/js/bootstrap.js"></script>
    <script type="text/javascript" src="assets/js/bootstrap-table.js"></script>


        
    <script type="text/javascript">
        var $table = $('#fresh-table'),
            $alertBtn = $('#alertBtn'), 
            full_screen = false,
            window_height;
            
        $().ready(function(){
            
            window_height = $(window).height();
            table_height = window_height - 20;
            
            
            $table.bootstrapTable({
                toolbar: ".toolbar",

                showRefresh: false,
                search: true,
                showToggle: true,
                showColumns: true,
                pagination: true,
                striped: true,
                sortable: true,
                height: table_height,
                pageSize: 25,
                pageList: [25,50,100],
                
                formatShowingRows: function(pageFrom, pageTo, totalRows){
                    //do nothing here, we don't want to show the text "showing x of y from..." 
                },
                formatRecordsPerPage: function(pageNumber){
                    return pageNumber + " rows visible";
                },
                icons: {
                    refresh: 'fa fa-refresh',
                    toggle: 'fa fa-th-list',
                    columns: 'fa fa-columns',
                    detailOpen: 'fa fa-plus-circle',
                    detailClose: 'fa fa-minus-circle'
                }
            });
            
            window.operateEvents = {
                'click .like': function (e, value, row, index) {
                    alert('You click like icon, row: ' + JSON.stringify(row));
                    console.log(value, row, index);
                },
                'click .edit': function (e, value, row, index) {
                    alert('You click edit icon, row: ' + JSON.stringify(row));
                    console.log(value, row, index);    
                },
                'click .remove': function (e, value, row, index) {
                    $table.bootstrapTable('remove', {
                        field: 'id',
                        values: [row.id]
                    });
            
                }
            };
            
            $alertBtn.click(function () {
                alert("This tweeLights! a Project for SWE573 at Bogazici University. It is the first working prototype and be considered as version 1.0");
            });
        
            
            $(window).resize(function () {
                $table.bootstrapTable('resetView');
            });    
        });
        

        function operateFormatter(value, row, index) {
            return [
                '<a rel="tooltip" title="Like" class="table-action like" href="javascript:void(0)" title="Like">',
                    '<i class="fa fa-heart"></i>',
                '</a>',
                '<a rel="tooltip" title="Edit" class="table-action edit" href="javascript:void(0)" title="Edit">',
                    '<i class="fa fa-edit"></i>',
                '</a>',
                '<a rel="tooltip" title="Remove" class="table-action remove" href="javascript:void(0)" title="Remove">',
                    '<i class="fa fa-remove"></i>',
                '</a>'
            ].join('');
        }
       
    </script>
























</html> 
