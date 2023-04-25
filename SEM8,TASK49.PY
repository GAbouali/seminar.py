"""
Задача №49. Решение в группах
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
"""
# ---------------------------------------
def add_contact(): #function to add new contacts to the text file.
    file = open('Seminar 8.txt', 'a', encoding='UTF-8')# 1.open the text file to 'a' append or add cont in it.
    contact_name = input('enter contact name: ')
    contact_phone = input('enter contact phone: ')
    contact_comments = input('enter contact comments: ')
    data = '\n' + contact_name+'; '+contact_phone+'; '+contact_comments
    print(data)
    file.write(data)
    file.close()

def read_contact(): #function to read the data in text file.
    file = open('Seminar 8.txt', 'r', encoding='UTF-8')
    data = file.readlines() #    = read the file line by line. making list from each line.
    file.close() # close the file after our addition to save our work.

    for contact in data:    
        print(data)
read_contact()

def find_contact(): #function to search for contact in the text file,
    file = open('Seminar 8.txt', 'r', encoding='UTF-8')
    data = file.readlines() #read the file line by line. making list from each line.
    file.close() # close the file after our addition to save our work.
    contact_to_search = input('enter a data to search for: ')
    for contact in data: #
        if contact_to_search.lower() in contact.lower(): #.lower, to can find the data we search if the user entered it with capital or small letters, protection from the stupid users.
            print(contact)
find_contact() 


def change_contact():
    phone_book=[]
    #            file path.    , read file.       remember it as it is.
    file = open('Seminar 8.txt', 'r', encoding='UTF-8')
    #    = read the file line by line. making list from each line.
    data = file.readlines()
    file.close() # close the file after our addition to save our work.
    # 2. creat a list of dictionaries from the text file.
    for contact in data:
        #                    .clean the lines of sympols(./,'). split the elements on base of ;
        new_contact = contact.strip().split(';')# CREAT LIST FROM EACH ELEMENT IN DATA
        new_contact={'name' : new_contact[0], 
                     'phone' : new_contact[1], 
                     'comment' : new_contact[2]} # creat dictionary from each element in data
        phone_book.append(new_contact)# add the new contact to the dictionary
    print(phone_book)

change_contact()





# new_phone_book=[]
# for contact in phone_book:
#     new_phone_book={'name':contact_name,'phone':contact_phone,'comments':contact_comments}

# print (new_phone_book)
# file = open('Seminar 8.txt', 'w', encoding='UTF-8')
# file.write(new_phone_book)
# file.close()
