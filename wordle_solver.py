from wordlist import wordlist
from pro_guesser import word_score_tr


class Wordle:
    def __init__(self):
        self.wordlist = wordlist #List we remove elements from
        self.word_tuple = tuple(self.wordlist) #We wouldn't wanna remove elements from the list we iterate 
    
    def solver(self):
        counter = 6
        seen_words = set()
        color_letters = {} #to eliminate the letters we used before we will store the letters which we mark them 'green, yellow, red'
        color_letters['g'] = []
        color_letters['y'] = []
        color_letters['r'] = []
        
        

        while counter > 0:
            
            min_ = [float('inf'),' ']
            count_dict = word_score_tr()

            for wrd in count_dict.keys():
                if wrd == 'çağan':
                    continue

                if count_dict[wrd] < min_[0]:
                    min_[0] = count_dict[wrd]
                    min_[1] = wrd
                
            print(f'Önerilen kelime: {min_[1]}')

            word = input('Kelime: ')
            colors = input('Renk kombinasyonu: ')

            
            if colors == 'eeeee':
                del count_dict[word]
                continue

            if colors == 'ggggg':
                print(f'🎉 Tebrikler {counter - 5} denemede buldun 🎉')
                break
            
            

            for i in range(5): #Creating the dictionary
                if colors[i] == 'g':
                    if word[i] in seen_words:
                        continue
                    else:
                        color_letters['g'].append((i,word[i]))
                        seen_words.add(word[i])

                if colors[i] == 'y':
                    if word[i] in seen_words:
                        continue
                    else:
                        color_letters['y'].append((i,word[i]))
                        seen_words.add(word[i])

                if colors[i] == 'r':
                    if word[i] in seen_words:
                        continue
                    else:
                        color_letters['r'].append((i,word[i]))
                        seen_words.add(word[i])

            for w in self.word_tuple:
                w = w.lower()
                for key in color_letters.keys():
                    if color_letters[key] != []:
                        if key == 'g':
                            for index, letter in color_letters['g']: #color_letters['g'] = [(1,'a'),(2,'b'),(3,'c')]
                                if w[index] != letter and w in self.wordlist and w in count_dict.keys(): # after the and part we want to check again if the word still in wordlist 
                                    self.wordlist.remove(w) # if we don't check program will try to remove the same word 
                                    del count_dict[w]
                                    break

                        if key == 'r':
                            for index, letter in color_letters['r']:
                                if letter in w and w in self.wordlist and w in count_dict.keys():
                                    self.wordlist.remove(w)
                                    del count_dict[w]
                                    break
                        
                        if key == 'y':
                            for index, letter in color_letters['y']:
                                if w[index] == letter and w in self.wordlist and w in count_dict.keys():
                                    self.wordlist.remove(w)
                                    del count_dict[w]
                                    break
                                elif letter not in w and w in self.wordlist and w in count_dict.keys():
                                    self.wordlist.remove(w)
                                    del count_dict[w]
                                    break

            if self.wordlist == []:
                print('Unfortunately there is no word that meets the criterias..')

            else:
                print(self.wordlist)

            counter -= 1 

    

    # def another_solver(self):
    #     for i in range(5):
    #         word = input('Word: ')
    #         colors = input('Color combination: ')
    #         for w in self.word_tuple:
    #             for i in range(5):
    #                 if colors[i] == 'r' and word[i] in w:
    #                     self.wordlist.remove(w)
    #                     break

    #                 elif colors[i] == 'g' and word[i] != w[i]:
    #                     self.wordlist.remove(w)
    #                     break

    #                 elif colors[i] == 'y' and word[i] not in w:
    #                     self.wordlist.remove(w)
    #                     break

    #                 elif colors[i] == 'y' and word[i] == w[i]:
    #                     self.wordlist.remove(w)
    #                     break
    #         return self.wordlist

def wordle_tr_runner():
    w = Wordle()
    w.solver()




        



        