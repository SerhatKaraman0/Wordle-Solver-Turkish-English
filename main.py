import wordle_solver, wordle_eng

print('Welcome to wordle solver..')
print("Wordle Türkçe Çözer'e hoşgeldiniz..")

language = input('Choose a language Turkish[tr] or English[en]: ')

if language == 'tr':
    wordle_solver.wordle_tr_runner()

if language == 'en':
    wordle_eng.wordle_eng_runner()
    
else:
    print('Language not available right now')


    
    