#                                                             1. function to rad the data from text file.
def read_data_from_file(file_name):
    data = []
    try:
        with open('Seminar 8.txt', 'r') as file:
            for line in file:
                line = line.strip().split(',')
                data.append(line)
                
    except FileNotFoundError:
        print(f"File {'Seminar 8.txt'} not found.")
    return data
# read_data_from_file('Seminar 8.txt')
# print(read_data_from_file('Seminar 8.txt'))

#                                                                2.function to add data
def write_data_to_file(file_name, data):
    with open('Seminar 8.txt', 'a') as file:
        for item in data:
            file.write('\n'+''.join(item) )
data=['Alex; 7777; cont 4']
write_data_to_file('Seminar 8.txt',data )
data=['Alexander; 11111; cont 5']
write_data_to_file('Seminar 8.txt',data )



#                                        3.function to search for some query in the data
def find_data(data, query):
    result = []
    for item in data:
        for field in item:
            if query in field:
                result.append(item)
                
    return result
# query=input('enter contact to search for: ')
# find_data('Seminar 8.txt', query )

def find_contact(): #function to search for contact in the text file,
    file = open('Seminar 8.txt', 'r', encoding='UTF-8')
    data = file.readlines() #read the file line by line. making list from each line.
    file.close() # close the file after our addition to save our work.
    contact_to_search = input('enter a data to search for: ')
    for contact in data: #
        if contact_to_search.lower() in contact.lower(): #.lower, to can find the data we search if the user entered it with capital or small letters, protection from the stupid users.
            print(contact)
find_contact() 

