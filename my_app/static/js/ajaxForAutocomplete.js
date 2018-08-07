/*
$(document).ready(function(){
$('#tagFilterForm').submit(function(e) {
    e.preventDefault();
    $.ajax({
        url: "/getTagsFromDB",
        type: 'GET',
        data: $('#tagFilterForm').serialize(),
        success:
            function (result) {
                searchResult(result)
            }
    });

}}));
*/

function searchResult(data) {
    $( "#tagSearch" ).autocomplete ({
        source: data
    });
}
