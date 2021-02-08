import stanza
from function import * 

stanza.download('ko')
nlp = stanza.Pipeline('ko')
answer_teacher_txt = '물이 증발하면서 기화열을 흡수해서.'
necessary_key_word = ['기화열', '흡수']
dependency_key_word = [[['물', 'H2O'], ['증발', '기화', '기체화']], [['기화열'], ['흡수']]]

while(True):
    print("마당에 물을 뿌리면 주변이 시원해지는 원인을 한 문장으로 서술하시오.")
    answer_student_txt = input()
    answer_teacher = nlp(answer_teacher_txt)
    answer_student = nlp(answer_student_txt)
    print(checkDependencyKeyWord(answer_student, dependency_key_word) and checkNecessaryKeyWord(answer_student, necessary_key_word))
    print('\n')





