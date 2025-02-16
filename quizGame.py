questions = [
{
	"prompt": "what is the capital of France?",
	"options": ["A.Berlin" ,"B.Paris", "C.Madrid", "D.London"],
	"answer": "B"
}, 

{
	"prompt": "what is the smallest prime number?",
	"options": ["A.1" ,"B.3", "C.2", "D.5"],
	"answer": "A"
},

{
	"prompt": "which language is primparly spoken in Brazil?",
	"options": ["A.Spanish", "B.German", "C.Portuguese", "D.French"],
	"answer": "C"
}

]

def run_quiz(questions):
	score = 0
	for question in questions:
		print(question["prompt"])
		for option in question["options"]:
			print(option)
		answer = input("Enter the corrrect answer: ").upper()
		if answer == question["answer"]:
			print("Correct! \n")
			score +=1
		else: 
			print("Incorrect! the correct answer was: " , question["answer"], "\n")
	print(f"You got {score} out of {len(questions)} correct")




run_quiz(questions)