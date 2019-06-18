$(function(){
	//日期选择
    if($("#birthday").get(0)){
    	jeDate({
	        dateCell:"#birthday",
	        format:"YYYY-MM-DD",
	        minDate:"1900-1-1",
	        maxDate:jeDate.now(0),
	        ishmsVal:false, 
	    });
    };
    
    $("#birthday").one('blur',function(){
    	$(this).focus();  	
    });


    $("#birthday").trigger("click");
    if($("#graduate").get(0)){
    	jeDate({
	        dateCell:"#graduate",
	        format:"YYYY-MM",
	        minDate:"1900-1",
	        maxDate:jeDate.now(0),
	        ishmsVal:false, 
	    });
    };
    
    $("#graduate").one('blur',function(){
    	$(this).focus();  	
    });


    $("#graduate").trigger("click");
    $("body").trigger("click");

    
  
    


})











	
