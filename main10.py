list = []
word = (input("type a word you want flipped")) #moddfied the padrome checker for this
wordlen = len(word)
lenlist = 100
while (True):
    choice = (input("1. to continue 2. to exit"))
    if choice == '1':
        print("ok")
        list = []
        word = (input("type a word you want flipped"))
        wordlen = len(word)
    elif choice == 2:
        break
    else:
        print ("invaled exiting...")
        break
    def checkdrome(word):
        for i in range (wordlen,1,-1):
            while(True):
                if i == len(list):
                    break
                else:
                    lenlist = len(list)
                    cow = 0
                list.append(word[i - 1 - lenlist])
            gosh = "".join(list)
            if gosh == word:
                print(gosh)
                lenlist = 100
                break
            else:
                print(gosh)
                lenlist = 100
                break
        
    
    checkdrome(word)
