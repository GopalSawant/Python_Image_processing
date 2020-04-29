from translate import Translator

translator= Translator(to_lang='ja')
try:

    with open("Test.txt", mode='r') as my_file:
        text=my_file.read()
        translation = translator.translate(text)
        print(translation)

except FileNotFoundError as err:
    print("File not found")

# with open("NewTest.txt",mode='r+') as new_file:
#     pass

#
# translator=Translator(to_lang='ja')
# translation=translator.translate("This is pen")


# to_lang = 'zh'
# secret = 'your secret from Microsoft'
# translator = Translator(provider='microsoft', to_lang=to_lang, secret_access_key=secret)
# translator.translate('the book is on the table')
