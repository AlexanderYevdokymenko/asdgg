class Translator():
    def translate1(self, eng, rus, rus2):
        self.eng = eng
        self.rus = rus
        self.rus2 = rus2
        print(self.eng, self.rus, self.rus2)
        
    def translate2(self, eng, rus, rus2):
        self.eng = eng
        self.rus = rus
        self.rus2 = rus2
        print(self.eng, self.rus)
        
t = Translator()
print('Всі варіанти перекладу: ')
t.translate1('goal -', 'гол,', 'цель')
print('Один варіант перекладу: ')
t.translate2('line -', 'линия,', 'очередь')