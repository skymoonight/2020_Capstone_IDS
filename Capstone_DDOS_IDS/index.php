<?php
/*
기본적으로 테이블에
index, w (와트 정보), a(암페어 정보) 넣어줬다고 했을때 코드
*/


$mozi=<<<eot
  <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
	<link href="https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700&display=swap" rel="stylesheet">
      <style>
      	html, body {margin: 10px; padding: 10px; font-family: 'Nanum Gothic', sans-serif;}
	div.wrap{position: relative;padding-top:50px;width:800px;height: 1000px;overflow: hidden;} 
	div.wrap > div {height: 300px;overflow: auto;} 
	table{width: 1000px} 
	thead tr{position: absolute;top: 0;display: block;background-color: #DEDEDE;width: 800px;height: 30px;} 
	thead th{width: 200px} 
	tbody{display: block;height: 300px;} 
	tbody tr{height: auto;} 
	tbody td{width: 200px;text-align: center;}
      </style>
    </head>
    <body>
	<h1>스마트 전력량계</h1>
	<hr/>
eot;
print $mozi;
$conn = mysqli_connect("localhost","user","1234","capston");
if (mysqli_connect_errno()){
echo "연결에 실패하였습니다." . mysqli_connect_error();
}
$result = mysqli_query($conn,"SELECT SUM(kilos) AS total_value FROM info");
$n = 1;
while($row = mysqli_fetch_array($result)){
echo "<h4> 현재 누적 전력량 : " . $row['total_value'] . "kWh</h4>";
$n++;
}
$mozi2=<<<eot


	<br/>
	
	<div class ="wrap">
	   <div>
	      <table id = "table1" class="table">
		  <thead class="thead-light">
		    <tr>
		      <th scope="col">인덱스</th>
		      <th scope="col">전류(A)</th>
		      <th scope="col">전력(W)</th>
		      <th scope="col">킬로수(kWh)</th>
		      <th scope="col">peakPower(W)</th>
		    </tr>
		  </thead>
		  </tbody>
eot;

print $mozi2;
$conn = mysqli_connect("localhost","user","1234","capston");
if (mysqli_connect_errno()){
echo "연결에 실패하였습니다." . mysqli_connect_error();
}
$result = mysqli_query($conn,"SELECT * FROM info");
$n = 1;
while($row = mysqli_fetch_array($result)){
echo "<tr>";
echo "<td>" . $row['_id'] . "</td>";
echo "<td>" . $row['RMSCurrent'] . "</td>";
echo "<td>" . $row['RMSPower'] . "</td>";
echo "<td>" . $row['kilos'] . "</td>";
echo "<td>" . $row['peakPower'] . "</td>";
echo "</tr>";
$n++;
}
echo "</tbody>";
echo "</table>";
echo "</div>";
echo "</div>";


mysqli_close($conn);

?>
