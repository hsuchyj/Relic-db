function updateRestrictions(){
    var table = document.getElementById("tagRequirements");
    var tagLevel = $("#tagFilter").val();
    var tagText = $("#tagSearch").val();
    var tagQuantity = $("#tagQuantity").val()

     $("#tagSearch").val("");//reset text after submission. =)
     $("#tagQuantity").val("")
    if(tagText.length == 0 ){//just a simple user case check to not add empty strings
        alert("check tag description");
        return;
    }
    if(tagQuantity.length == 0){
        alert("check quantity of questions");
        return;
    }
    //Create the restriction table row
    var row = table.insertRow(-1);
    var rowIndex = row.rowIndex;
    var cell1 = row.insertCell(0); //<label>units</label>
    var tagLevelLabel = document.createElement("label");
    var tagLevelLabelText = document.createTextNode(tagLevel);
    tagLevelLabel.appendChild(tagLevelLabelText);
    cell1.appendChild(tagLevelLabel);
    var cell2 = row.insertCell(1); //<label>:</label></td>
    var tagLevelLabel = document.createElement("label");
    var tagLevelLabelText = document.createTextNode(":");
    tagLevelLabel.appendChild(tagLevelLabelText);
    cell2.appendChild(tagLevelLabel);
    var cell3 = row.insertCell(2); //<label>Introduction to Python</label>
    var tagLevelLabel = document.createElement("label");
    var tagLevelLabelText = document.createTextNode(tagText);
    tagLevelLabel.appendChild(tagLevelLabelText);
    cell3.appendChild(tagLevelLabel);
    var cell4 = row.insertCell(3); //<button id="removeTag" onclick="deleteTags(\'' + this.parent  +'\')" class="tabHover">Remove</button>

    //the remove button for each row will remove the in the restrictions and the table itself
    var removeButton = document.createElement("button");
    var removeButtonText = document.createTextNode("Remove");
    removeButton.appendChild(removeButtonText);
    removeButton.addEventListener('click', function(){
        var deletedRowIndex = this.parentNode.parentNode.rowIndex;//reference to row index needs to be computed on delete time.
        // it can't be stored on creation.
        restrictions[tagLevel].splice(deletedRowIndex,1); //remove model
        table.deleteRow(deletedRowIndex); //remove view
        table.refresh();
        updateDisplayedQuestions();
    });
    //add restriction
    restrictions[tagLevel][rowIndex] = tagText;
    cell4.appendChild(removeButton);
    updateDisplayedQuestions();
};

function updateDisplayedQuestions(){
    //Hunter/Juan: insert code to refresh HTML/query database questions here
    alert(restrictions["units"]);
    alert(restrictions["unit_slos"]);
    alert(restrictions["skills"]);
    alert(restrictions["skills_slos"]);
}