while True:
    from googletrans import LANGUAGES, Translator
    import os
    os.system('cls')
    language1 = input('What language is the text you are translating? ').lower()
    if language1 not in LANGUAGES.values():
        print("Invalid language entered.")
        ask = input("Do you want to try again? ").lower()
        if ask == 'no':
            exit()
        elif ask == 'yes':
            print("Okay!")
        else:
            exit()
    language2 = input('What language do you want to translate the text to? ').lower()
    if language2 not in LANGUAGES.values():
        print("Invalid language entered.")
        ask = input("Do you want to try again? ").lower()
        if ask == 'no':
            exit()
        elif ask == 'yes':
            print("Okay!")
        else:
            exit()       
    text = input('What text do you want to translate? ')
    translator = Translator()
    translation = translator.translate(text, src=language1, dest=language2)
    os.system('cls')
    print(translation.text)
    ask = input("Do you want to try again? ").lower()
    if ask == 'no':
        exit()
    elif ask == 'yes':
        print("Okay!")
    else:
        exit()