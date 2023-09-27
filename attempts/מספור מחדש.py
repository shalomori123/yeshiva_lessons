# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 20:27:47 2023

@author: Administrator
"""
import os
import shutil

ALEPHBET = ('א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י',
            'יא', 'יב', 'יג', 'יד', 'יהא', 'יוא', 'יז', 'יח', 'יט', 'כ',
            'כא', 'כב', 'כג', 'כד', 'כה', 'כו', 'כז', 'כח', 'כט', 'ל',
            'לא', 'לב', 'לג', 'לד', 'לה', 'לו', 'לז', 'לח', 'לט', 'מ',
            'מא', 'מב', 'מג', 'מד', 'מה', 'מו', 'מז', 'מח', 'מט', 'נ',
            'נא', 'נב', 'נג', 'נד', 'נה', 'נו', 'נז', 'נח', 'נט', 'ס',
            'סא', 'סב', 'סג', 'סד', 'סה', 'סו', 'סז', 'סח', 'סט', 'ע',
            'עא', 'עב', 'עג', 'עד', 'עה', 'עו', 'עז', 'עח', 'עט', 'פ',
            'פא', 'פב', 'פג', 'פד', 'פה', 'פו', 'פז', 'פח', 'פט', 'צ',
            'צא', 'צב', 'צג', 'צד', 'צה', 'צו', 'צז', 'צח', 'צט', 'ק')

MONTHS = ('אלול', 'תשרי', 'חשון', 'כסלו', 'טבת', 'שבט', 'אדר', 'ניסן', 'אייר', 'סיון', 'תמוז', 'אב') 

def rename_month(month):
    all_months = [["תשרי", "תישרי"],
                  ["חשון", "חשוון", "מרחשון", "מרחשוון"],
                  ["כסלו", "כסליו", "כיסלו", "כיסליו"],
                  ["טבת"],
                 ["שבט"],
                 ["אדר"],
                 ["ניסן"],
                 ["אייר", "איר"],
                 ["סיון", "סיוון"],
                 ["תמוז"],
                 ["אב", "מנחם אב"],
    ["אלול"]]

    for month_names in all_months:
        if month in month_names:
            month = month_names[0]
            return month

def get_month(file):
    date = file.split(" - ")[2]
    month = date.split(' ')[1]
    month = rename_month(month)
    return month

#def compare_month(month1, month2):
    

def compare(file1, file2):     
     month1 = get_month(file1)
     month2 = get_month(file2)
     if(month1 == month2):
         if(file1 < file2):
             return -1
         elif(file1 > file2):
             return 1
         elif(file1 == file2):
             return 0
     else:
         return 0
     
def sort_by_date(file):
    month = get_month(file)
    date = file.split(" - ")[2]
    day = date.split(' ')[0]
    if day == "ט''ו":
        day = "י''ה"
    if day == "ט''ז":
        day = "י''ו"
    for i, mon in enumerate(MONTHS):
        if month == mon:
           return ALEPHBET[i] + '-' + day 

def number_directory(directory):
    directory = directory + '\\'
    sorted_list = os.listdir(directory)
    sorted_list.sort(key = sort_by_date)
    for i, file in enumerate(sorted_list):
        name = ALEPHBET[i] + " - " + file
        os.rename(directory + file, directory + name)
    print("התיקייה " + directory.split('\\')[-2] +" מוספרה מחדש\n")
        
    
def remove_numbering(directory):  
    directory = directory + '\\'   
    for file in os.listdir(directory):
            name_list = file.split(' - ')
            if name_list[0] == '':
                try:
                        os.rename(directory + file, directory + file[3: ])
                       # print('המספור הוסר\n')
                except:
                        print("\n\nהשינוי בקובץ "+ file +" נכשל!\n\n")
            elif name_list[0][0] == '-':
                    try:
                            os.rename(directory + file, directory + file[2: ])
                           # print('המספור הוסר\n')
                    except:
                            print("\n\nהשינוי בקובץ "+ file +" נכשל!\n\n")
            elif name_list[0] in ALEPHBET:
                    try:
                            os.rename(directory + file, directory + file[len(name_list[0])+3: ])
                           # print('המספור הוסר\n')
                    except:
                            print("\n\nהשינוי בקובץ "+ file +" נכשל!\n\n")
            else:
                print("\nשם הקובץ " + file + " אינו תקין\n")
        
    print("המספור בתיקיית "+ directory.split('\\')[-2] +" הוסר")

def number_all(directory, folders_list = [], num_list = False):
    pass

def do_not_number(directory):
    print("רשימת התיקיות שבתיקייה {} שבחרת למספר: ".format(directory.split('\\')[-3]))
    rav_folders = os.listdir(directory)  #הדפסת כל התיקיות שבתייקיה שכתובתה נשלחה לפונקציה
    i = 0
    to_del = []
    for folder in rav_folders:
        if os.path.isdir(directory + folder):
            i = i + 1
            print("{}. {}".format(i, folder))
        else:
            to_del.append(folder)
    for item in to_del:
        rav_folders.remove(item)
        
    places = input("הכנס את מספרי התיקיות שאין ברצונך למספר (עם רווח אחד ביניהם). לסיום הקש enter: ").split(" ") #רשימת התיקיות שאינן למספור
    no_change = []
    for n in places:
        try: 
            no_change.append(rav_folders[int(n) - 1])
        except:
            print("כל התיקיות ימוספרו. אם ביקשת שלא למספר חלר מהתיקיות, כנראה שהקלט לא תקין\n אם כך הדבר, עצור את התוכנה! אחרת יתכן שחלק מהתיקיות ימוספרו. ")
    return no_change

def print_directories(directory):
    rav_folders = os.listdir(directory)  #הדפסת כל התיקיות שבספריה שכתובתה נשלחה לפונקציה
    i = 0
    for folder in rav_folders:
        if os.path.isdir(os.path.join(directory, folder)):
            i = i + 1
            print("{}. {}".format(i, folder))
        
def get_directories(directory, get_places):
    """ הפונקציה מקבלת כתובת של ספריה (directory), ורשימה של מספרים סידוריים (get_places)
    הפונקציה מחזירה רשימה (directories) של שמות התיקיות בספריה שמספרן הסידורי נמצא ברשימה שנקלטה """
    
    places = get_places.copy()
    directories = []
    i = 0
    rav_folders = os.listdir(directory)
    
    for folder in rav_folders:
        if os.path.isdir(directory + folder):
            i = i + 1
            if i in places:
                directories.append(folder)
    return directories

def get_one_directory(directory):
    folders = next(os.walk(directory))[1]
    dir_num = input("בחר את מספר התיקייה המבוקשת: ")
    while not dir_num.isnumeric():
        dir_num = input("קלט לא תקין. נסה שנית: ")
    dir_num = int(dir_num)
    while dir_num > len(folders) or dir_num < 1:
        dir_num = input("קלט לא תקין. נסה שנית: ")
        while not dir_num.isnumeric():
            dir_num = input("קלט לא תקין. נסה שנית: ")
        dir_num = int(dir_num)
    return os.path.join(directory, folders[dir_num - 1])
    
def f_get_option(options_list):
    for i, option in enumerate(options_list):
        print("{}. {}".format(i + 1, option))
    get_option = input("הכנס את מספרה של האפשרות הרצויה: ")
    while not get_option.isnumeric() or int(get_option) > len(options_list):
        get_option = input("קלט לא תקין. נסה שוב: ")
    return int(get_option)

def place_lst_norm(place_list):
    new_place_list = place_list.copy()
    for n in place_list:
        if not n.isnumeric():
            new_place_list.remove(n)
    for i, place in enumerate(new_place_list):
        new_place_list[i] = int(place)
    return new_place_list


def main():
    
    print('ברוך הבא לתוכנת מספור השיעורים!\n אשריך!')
    to_start = input('כדי להתחיל כתוב "התחל": ')
    while to_start != 'התחל':
            to_start = input('כדי להתחיל כתוב "התחל": ')
    # תיקיית מספור הקלטות
    directory = r"C:\Users\Administrator\Desktop\העלאת הקלטות - תוכנה\קבצים למספור\\"  
    # שיעורי הישיבה הגבוהה
    directory4 = r"C:\Users\Administrator\Desktop\שיעורי הישיבה הגבוהה\שיעורי הישיבה הגבוהה\שיעורים תשפ''ג 83\\" 

    # directory5 = r"C:\Users\Administrator\Desktop\שיעורי הישיבה הגבוהה\שיעורי הישיבה הגבוהה\שיעורים תשפ''ג 83\הרב יעקב סבתו\\"
    
    # DIRECTORY = directory4
    # options = ["כל תיקיות השיעורים","כל התיקיות של רב מסויים", "תיקייה מסויימת", "תיקיית מספור השיעורים"]
    # print("מה ברצונך למספר?")
    # get_option = f_get_option(options)

    # print("\nבחירתך: " + options[get_option - 1])
    # if get_option == 1:  # מספור הכל
    #     options1 = ["מספר הכל", "מספר תיקיות של רבנים מסויימים בלבד", "מספר הכל מלבד תיקיות של רבנים מסויימים"]
    #     get_option1 = f_get_option(options1)
    #     if get_option1 == 1:
    #         number_all(DIRECTORY)
    #     elif get_option1 == 2:  # מספור תיקיות של רבנים מסויימים
    #         print_directories(DIRECTORY)
    #         places_inp = input("הכנס את מספרי התיקיות שברצונך למספר (עם רווח אחד ביניהם). לסיום הקש enter: ")
    #         places = places_inp.split()
    #         places = place_lst_norm(places)
    #         folders_to_number = get_directories(DIRECTORY, places)
    #         number_all(DIRECTORY, folders_to_number, True)
    #     elif get_option1 == 3:  # מספור הכל מלבד תיקיות של רבנים מסויימים
    #         print_directories(DIRECTORY)
    #         places_inp = input("הכנס את מספרי התיקיות שאין ברצונך למספר (עם רווח אחד ביניהם). לסיום הקש enter: ")
    #         places = places_inp.split()
    #         places = place_lst_norm(places)
    #         no_change_folders = get_directories(DIRECTORY, places)
    #         number_all(DIRECTORY, no_change_folders)
    # elif get_option == 2:  # מספור תיקיות של רב מסויים
    #     print_directories(DIRECTORY)
    #     rav_directory = get_one_directory(DIRECTORY)    
    #     options2 = ["מספר הכל", "מספר הכל מלבד תיקיות של שיעורים מסויימים"]
    #     get_option2 = f_get_option(options2)
    #     if get_option2 == 1:
    #         number_all(rav_directory)
    #     elif get_option2 == 2:  # מספור תיקיות הרב שנבחר מלבד תיקיות של שיעורים מסויימים
    #         print_directories(rav_directory)
    #         places_inp = input("הכנס את מספרי התיקיות שאין ברצונך למספר (עם רווח אחד ביניהם). לסיום הקש enter: ")
    #         places = places_inp.split()
    #         places = place_lst_norm(places)
    #         no_change_folders = get_directories(rav_directory, places)
    #         number_all(rav_directory, no_change_folders)
    # elif get_option == 3:
    #     print_directories(DIRECTORY)
    #     rav_directory = get_one_directory(DIRECTORY)
    #     print_directories(rav_directory)
    #     lessons_directory = get_one_directory(rav_directory)
                
            

    no_change = do_not_number(directory4)
    
    for library in os.listdir(directory4): 
        directory0 = directory4 + library + "\\" 
        if library in no_change:
            continue
        try:
            for folder in os.listdir(directory0):
                try:
                    remove_numbering(directory0 + folder) 
                    number_directory(directory0 + folder)
                except:
                    print("תקלה במספור התיקייה " + folder)
        except:
            print("תקלה במספור התיקייה " + library)
   
    print("התיקייה " + directory4.split('\\')[-3] + " מוספרה מחדש") 
    
main()