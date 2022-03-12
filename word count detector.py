def wordCountDetector(text):

    word=""
    wordList=[]
    
    for i in range(len(text)):
        #here i represents an individual character, letter of punctuation or space
    
        if(ord(text[i])>=97 and ord(text[i])<=122) or(ord(text[i])>=65 and ord(text[i])<=90):
            word=word+text[i]
    
        else:
            #This will work only for after first word in the paragraph is over.
            if len(wordList)==0:
                wordList.append([word,1])
                #print(word)
                word=""

            #This case will work for subsequent words in the paragraph.
            else:
            #check if j is in the wordList
                flag=False
                for j in range(len(wordList)):
                    #Check if the word is in the wordList
                    if word in wordList[j][0]:
                        wordList[j][1]+=1
                        flag=True
                        word=""
                        break

                #If the word is not in the list, then append a new list (word, count)
                #to the list
                if flag==False:
                    wordList.append([word,1])
                    #print(word)
                    word=""
    
    return wordList

message=input("Start typing your message. When completed, press enter:")

wordList=wordCountDetector(message)

for i in wordList:
    if i[1]>1:
        print(i[0]+" appears "+str(i[1])+" times.")

    else:
        print(i[0]+" appears "+str(i[1])+" time.")
