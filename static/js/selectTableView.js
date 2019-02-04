	$(document).ready(function(){
		
		var tableView = $("#rangeTableView");
		var tableData=[];
		var operator_Unique = [];
		var area_unique = [];

		
		tableView.find(".tableRow").each(function(){
			//$(".tableRow").each(function(){
			        var currentRow=$(this);

			        var col1_value=currentRow.find("td:eq(0)").text();//operator
			        var col2_value=currentRow.find("td:eq(1)").text();//area code
			        var col3_value=currentRow.find("td:eq(2)").text();//start range
			        var col4_value=currentRow.find("td:eq(3)").text();//end range
			        var col5_value=currentRow.find("td:eq(4)").text();//from date
			        var col6_value=currentRow.find("td:eq(5)").text();//end date

			        removeDuplicates(col1_value, operator_Unique);//make set of operators
					removeDuplicates(col2_value, area_unique);
					
			        var obj={};
			        obj.col1=col1_value;
			        obj.col2=col2_value;
			        obj.col3=col3_value;
			        obj.col4=col4_value;
			        obj.col5=col5_value;
			        obj.col6=col6_value;


			        tableData.push(obj);

		});
		selectUniqueOperator();
		selectUniqueArea()
		
		function removeDuplicates(item, unique_array){
		  if(unique_array.indexOf(item) == -1){
			  unique_array.push(item);
		   }
		};
		
		function selectUniqueOperator(){
			var selectOperator = $(":input[name=operatorTable]");
			for(var i=0; i<operator_Unique.length; i++)
			{
				//$("#errInput").append("+for-" + operator_Unique[i] + "for+");
				var optionOperator = "<option class='oTable' value='ts'>" + operator_Unique[i] + "</option>";
				selectOperator.append(optionOperator);
			}
		};
		
		function selectUniqueArea(){
			var selectOperator = $(":input[name=selectAreaTable]");
			for(var i=0; i<area_unique.length; i++)
			{
				var optionOperator = "<option class='ndc-geo' value='ALL'>" + area_unique[i] + "</option>";
				selectOperator.append(optionOperator);
			}
		};
			
		$("form[name=tableForm]").change(changeTable);
		
		var startRangeTable ="";

		$("form[name=tableForm] :input[name=selectStartRange]").on('input',function () {
			changeTable();
        });	
		
		function changeTable(){
			var selectAreaTable = $(":input[name=selectAreaTable] option:selected").text();
			var operatorTable = $(":input[name=operatorTable] option:selected").text();
			startRangeTable = $(":input[name=selectStartRange]").val()

			
	        var selectedRows = "";

			//alert('change');
			for(var i=0; i<tableData.length; i++){
				var col1_value = tableData[i].col1;
				var col2_value = tableData[i].col2;
				var col3_value = tableData[i].col3;
		        var col4_value = tableData[i].col4;
		        var col5_value = tableData[i].col5;
		        var col6_value = tableData[i].col6;
		        
				if( (selectAreaTable == "ALL" || selectAreaTable == col2_value) &&
						col3_value.startsWith(startRangeTable) &&
						(operatorTable == "ALL" || operatorTable == col1_value)){
					 selectedRows = selectedRows + "<tr class='tableRow'>" +
						"<td>"+ col1_value + "</td>"+
						"<td>"+ col2_value + "</td>"+
						"<td>"+ col3_value + "</td>"+
						"<td>"+ col4_value + "</td>"+
						"<td>"+ col5_value + "</td>"+
						"<td>"+ col6_value + "</td>"+
						"</tr>";
				}
			}
			
			$(".tableRow").each(function(){
	        	var currentRow=$(this);
				currentRow.remove();
			});
			tableView.append(selectedRows);
		}// end of function  changeTable()
		
	});		
