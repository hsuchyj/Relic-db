

function updateRestrictions(){
    var table = document.getElementById("tagRequirements");
    var tagLevel = $("#tagFilter").val();
    var tagText = $("#tagSearch").val();
    var tagQuantity = $("#tagQuantity").val()
    var tagDifficulty = $("#tagDifficulty").val()

    if(tagText.length == 0 ){//just a simple user case check to not add empty strings
        alert("check tag description");
        return;
    }
    if(tagQuantity.length == 0){
        alert("check quantity of questions");
        return;
    }
    if(tagDifficulty.length == 0){
        alert("check quantity of questions");
        return;
    }

     $("#tagSearch").val("");//reset text after submission. =)
     $("#tagQuantity").val("")
     $("#tagDifficulty").val("")

    //Create the restriction table row
    var row = table.insertRow(-1);
    var rowIndex = row.rowIndex;

    var tagQuantityCell = row.insertCell(0); //<label>quantity</label>
    var tagDifficultyCell = row.insertCell(1);//<label>quantity</label>
    var tagLevelCell = row.insertCell(2); //<label>units</label>
    var tagLevelCell = row.insertCell(3);
    var tagTextCell = row.insertCell(4); //<label>Introduction to Python</label>
    var removeButtonCell = row.insertCell(5); //<button id="removeTag" onclick="deleteTags(\'' + this.parent  +'\')" class="tabHover">Remove</button>

    var tagQuantityLabel = document.createElement("label");
    var tagQuantityLabelText = document.createTextNode( tagQuantity + " Questions with ");
    tagQuantityLabel.appendChild(tagQuantityLabelText);
    tagQuantityCell.appendChild(tagQuantityLabel);

    var tagDifficultyLabel = document.createElement("label");
    var tagDifficultyLabelText = document.createTextNode( "Level " + tagDifficulty + " Difficulty");
    tagDifficultyLabel.appendChild(tagDifficultyLabelText);
    tagDifficultyCell.appendChild(tagDifficultyLabel);

    var tagLevelLabel = document.createElement("label");
    var tagLevelLabelText = document.createTextNode("("+ tagLevel +")");
    tagLevelLabel.appendChild(tagLevelLabelText);
    tagLevelCell.appendChild(tagLevelLabel);

    var tagTextLabel = document.createElement("label");
    var tagTextLabelText = document.createTextNode(tagText);
    tagTextLabel.appendChild(tagTextLabelText);
    tagTextCell.appendChild(tagTextLabel);


    //the remove button for each row will remove the in the restrictions and the table itself
    var removeButton = document.createElement("button");
    var removeButtonText = document.createTextNode("Remove");
    removeButton.appendChild(removeButtonText);
    removeButton.addEventListener('click', function(){
        var deletedRowIndex = this.parentNode.parentNode.rowIndex;//reference to row index needs to be computed on delete time.
        // it can't be stored on creation.
        restrictions.splice(deletedRowIndex,1); //remove model
        table.deleteRow(deletedRowIndex); //remove view
        $("#tagRequirements").hide().show(0);//refresh table view.
        updateDisplayedQuestions();
    });
    //add restriction
    restrictions[rowIndex] = tagText;
    removeButtonCell.appendChild(removeButton);
    updateDisplayedQuestions();
};

function updateDisplayedQuestions(){
    //Hunter/Juan: insert code to refresh HTML/query database questions here
    alert(restrictions);
}