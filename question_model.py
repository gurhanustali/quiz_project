class Question:

    question_bank=[]

    def __init__(self, text, answer):
        self.text=text
        self.answer=answer
        self.question_bank.append(self)


    def __str__(self):
        return str(f'{self.text}: {self.answer}')


Question("Windows bir işletim sistemi midir?","True")
Question("Güneş sisteminde dokuz gezegen mi vardır?","False")
Question("Gökhan 18 yaşından küçük müdür?","True")

