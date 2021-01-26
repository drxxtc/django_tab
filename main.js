$.ajax({
        method:'post',
        url: 'progmod/urls.py'
        data: { "from": $.datapicker,
        "to": $.datepicker1
                }
        serialized-data}).done(function(response){
                console.log(response.data),
        
       });
function checkUpdates()
{
	var xhttp;
	xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() 
	{
		if (this.readyState == 4 && this.status == 200) {
			var ajaxRes = JSON.parse(this.responseText);
			console.log(ajaxRes);
			let specific_tbody = document.getElementById("myTable");
			$(".mytable-tr").remove(); 
			
			ajaxRes.forEach(function(entry) {
				let row = specific_tbody.insertRow(-1);
				row.className = "mytable-tr";
				row.insertCell(0).appendChild(  document.createTextNode(entry.pk)  );
				row.insertCell(-1).appendChild(  document.createTextNode(entry.fields.project_name)  );
				row.insertCell(-1).appendChild(  document.createTextNode(entry.fields.status)  );
				let date = new Date(entry.fields.created_at);
				
				row.insertCell(-1).appendChild(  document.createTextNode(formatDate(date))  );
			});
			try
			{
				$("#myInput").keyup();
			}
			catch{}
		}
	};
	xhttp.open("GET", "/progmod/list", true);
	xhttp.send();   
}
function formatDate(date) {
  var hours = date.getHours();
  var minutes = date.getMinutes();
  var ampm = hours >= 12 ? 'p.m.' : 'a.m.';
  hours = hours % 12;
  hours = hours ? hours : 12; // the hour '0' should be '12'
  minutes = minutes < 10 ? '0'+minutes : minutes;
  var strTime = hours + ':' + minutes + ' ' + ampm;
  var month = date.toLocaleString('default', { month: 'short'})
  //Dec. 27, 2020, 6:08 p.m.
  return month + ". " + date.getDate() + ", " + date.getFullYear() + ",  " + strTime;
}

$(document).ready(function () {
    $("#myInput").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#myTable tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
	checkUpdates();
	
});

var timer;
if (!timer)
	timer = setInterval(checkUpdates, 5000);
    
//$('#"dataform"').text(function(e){
 //       e.preventDefault();
   //     $.ajax({
     //           method:'post',
       //         url: 'progmod/urls.py'
         //       data: serialized-data,
           //     dataType:"html",
             //   succes:function(result)
               //});
//});
    
function SendDateStart()
{
	var xhttp;
	xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() 
	{
		if (this.readyState == 4 && this.status == 200) {
			var ajaxRes = JSON.parse(this.responseText);
			console.log(ajaxRes);
			let specific_tbody =document.getElementById("myTable");
			$(".mytable-tr").remove(); 
            ajaxRes.forEach(function(entry) {
				let row = specific_tbody.insertRow(-1);
				row.className = "mytable-tr";
				row.insertCell(0).appendChild(  document.createTextNode(entry.pk)  );
				row.insertCell(-1).appendChild(  document.createTextNode(entry.fields.project_name)  );
				row.insertCell(-1).appendChild(  document.createTextNode(entry.fields.status)  );
				let date = new Date(entry.fields.created_at);
				
				row.insertCell(-1).appendChild(  document.createTextNode(formatDate(date))  );
			});
			try
			{
				$("#datapicker").keyup();
			}
			catch{}
		}
	};
	xhttp.open("GET", "/progmod/datesfilter", true);
	xhttp.send();   
}
function SendDateEnd()
{
	var xh;
	xh = new XMLHttpRequest();
	xh.onreadystatechange = function() 
	{
		if (this.readyState == 4 && this.status == 200) {
			var ajaxRes = JSON.parse(this.responseText);
			console.log(ajaxRes);
			let specific_tbody = document.qetElementById("myTable");
			$(".mytable-tr").remove(); 
            ajaxRes.forEach(function(entry) {
				let row = specific_tbody.insertRow(-1);
				row.className = "mytable-tr";
				row.insertCell(0).appendChild(  document.createTextNode(entry.pk)  );
				row.insertCell(-1).appendChild(  document.createTextNode(entry.fields.project_name)  );
				row.insertCell(-1).appendChild(  document.createTextNode(entry.fields.status)  );
				let date = new Date(entry.fields.created_at);
				
				row.insertCell(-1).appendChild(  document.createTextNode(formatDate(date))  );
			});
                try
			{
				$("#datapicker1").keyup();
			}
			catch{}
		}
	};
	xh.open("GET", "/progmod/datesfilter", true);
	xh.send();   
}
