<?php
require 'C:\xampp\htdocs\phpmongodb\vendor\autoload.php';
$client = new MongoDB\CLient("mongodb://127.0.0.1:27017");
$db = $client->relic;
$collection = $db->questions;
#echo isset($_POST["search"]);

class Question
{
	public $questionText;
	public $answers;
}

if(!empty($_POST["search"]))
{
	$keyword = $_POST["search"];
	
	
	
	
	$regex = new MongoDB\BSON\Regex($keyword);
	$cursor = $collection->find(array('question_text'=> $regex));
	$resultQuestions = array();
	foreach ($cursor as $doc) {
		$question = new Question();
    // do something to each document
	#make question a variable
		$question->questionText = $doc->question_text;
		#echo $doc->question_text;
		#$ansCount= 'a';
		$question->answers = $doc["answers"];
		#foreach($doc["answers"] as $answer)
		#{
			#tab spacing for answers for readibility
			#echo "<pre class = 'answers'>         ",$ansCount,") ",$answer["text"],"</pre>";
			#new line for answers
			#$ansCount++;		
		#}
		array_push($resultQuestions,$question);
}
	echo json_encode($resultQuestions);
}
#header("Location:http://localhost/htm.html")
?>