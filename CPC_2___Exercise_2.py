
# Setup for primary class
class Question: 

    def __init__(self) :
        self._text = " "
        self._answer = " "

    def setText(self, questionText) :
        self._text = questionText

    def setAnswer(self, correctResponse) :
        self._answer = correctResponse

    def checkAnswer(self, response) :
        return response == self._answer 

    def display(self) :
        print(self._text)

# Class I'll acttually be using
class ChoiceQuestion(Question):

    def __init__(self) :
        super().__init__()
        self._choices = []

    def addChoice(self, choice, correct) :
        self._choices.append(choice)
        if correct:
            choiceString = str(len(self._choices))
            self.setAnswer(choiceString)

    def display(self) :
        super().display()

        for i in range(len(self._choices)) :
            choiceNumber = i + 1
            print("%d: %s" %(choiceNumber, self._choices[i]))


# The actual questions
def main() :
    first = ChoiceQuestion()
    first.setText("100 x 0")
    first.addChoice("0", True)
    first.addChoice("69", False)
    first.addChoice("420", False)

    second = ChoiceQuestion()
    second.setText("100 x 20")
    second.addChoice("20", True)
    second.addChoice("67", False)
    second.addChoice("19.32", False)

    third = ChoiceQuestion()
    third.setText("25 X 5")
    third.addChoice("100", True)
    third.addChoice("33", False)
    third.addChoice("11", False)

    fourth = ChoiceQuestion()
    fourth.setText("11 x 22")
    fourth.addChoice("242", True)
    fourth.addChouie("71", False)
    fourth.addChoice("88", False)

    fifth = ChoiceQuestion()
    fifth.setText("33 x 7")
    fifth.addChoice("69", True)
    fifth.addChoice("50", False)
    fifth.addChoice("11", False)

    # Class to present questions
    def presentQuestion(q):
        q.display()
        response = input("Your Answer: ")
        if q.checkAnswer(response) == False:
            print(q.checkAnswer(response))
            presentQuestion(q)
        elif q.checkAnswer(response) == True:
            print(q.checkAnswer(response))

    
    # Presents the questions        
    presentQuestion(first)
    presentQuestion(second)
    presentQuestion(third)
    presentQuestion(fourth)
    presentQuestion(fifth)


# Program starts
main()