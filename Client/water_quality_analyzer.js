function onClickAnalyzeQuality(){
    console.log("Analyze Quantity button clicked");
    var ph=document.getElementById("ph_val");
    var hardness=documemt.getElementById("hard_val")
    var solids=document.getElementById("solids_val")
    var chloroamines=document.getElementById("chlor_val");
    var sulfate=document.getElementById("sulfate_val");
    var conductivity=document.getElementById("cond_val");
    var organic=documet.getElementById("organic_val");
    var trihalomethames=document.getElementById("trihalo_val");
    var turbidity=document.getElementById("turbidity");
    var predpotability= getElementById("qanalyzed");

    var url= "http://127.0.0.1:5000/predict_water_potability";

    $.post(url,{
        ph: parseFloat(ph.value),
        hardness: parseFloat(hardness.value),
        solids: parseFloat(solids.value),
        chloroamines: parseFloat(chloroamines.value),
        sulfate: parseFloat(sulfate.value),
        conductivity: parseFloat(conductivity.value),
        organic: parseFloat(organic.value),
        trihalomethames: parseFloat(trihalomethames.value),
        turbidity: parseFloat(turbidity.value)

    },function(data,status){
        console.log(data.predicted_potability);
        predpotability.innerHTML= "<h2>" + data.predicted_potability.toString() + "</h2>";
        console.log(status);
    });
}

/*function onPageLoad(){
    console.log("Document Loaded")
}

window.onload= onPageLoad*/
