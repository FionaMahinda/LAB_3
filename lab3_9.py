def phrase():
    
    sentence = input("Enter your phrase:")
    words = sentence.split()
   
    for i in words:
        print(f"{i} =>", {len(i)})

phrase()
