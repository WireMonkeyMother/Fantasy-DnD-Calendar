#! python3
#DnDcalendarSystem.py - Maintains a calendar showing the date for a 360 day year, divided into twelve 3 week months

import os, time

dayNames = {'1':'Monus','2':'Dicus','3':'Tricus','4':'Quarus','5':'Pentus','6':'Hexus','7':'Septus','8':'Octus','9':'Nonus','10':'Decus'}
weekNames = {'1':'Unum','2':'Dosum','3':'Trisum'}
monthNames = {
    # Autumn
    '1': 'Vendémiaire',
    '2': 'Brumaire',
    '3': 'Frimaire',
    # Winter
    '4': 'Nivôse',
    '5': 'Pluviôse',
    '6': 'Ventôse',
    # Spring
    '7': 'Germinal',
    '8': 'Floréal',
    '9': 'Prairial',
    # Summer
    '10': 'Messidor',
    '11': 'Thermidor',
    '12': 'Fructidor',
}

dayNumbers = {v:k for k, v in dayNames.items()}
weekNumbers = {v:k for k,v in weekNames.items()}
monthNumbers = {v:k for k,v in monthNames.items()}

dayList = list(dayNames.values())
weekList = list(weekNames.values())
monthList = list(monthNames.values())

def createAdate(): #This allows the user to input the current date.
    while True: #Day
        print('What is the current day?')
        currentDay = input()
        if currentDay not in dayNames.values():
            print('That is not a valid input, check spelling and capitalization')
        else:
            SavetheDay = open('DnDcalendar.txt','w')
            SavetheDay.write(currentDay + '\n')
            SavetheDay.close()
            break  
    while True: #Week
        print('What is the current week?')
        currentWeek = input()
        if currentWeek not in weekNames.values():
            print('That is not a valid input, check spelling and capitalization')
        else:
            SavetheWeek = open('DnDcalendar.txt','a')
            SavetheWeek.write(currentWeek + '\n')
            SavetheWeek.close()
            break
    while True: #Month
        print('What is the current month?')
        currentMonth = input()
        if currentMonth not in monthNames.values():
            print('That is not a valid input, check spelling and capitalization')
        else:
            SavetheMonth = open('DnDcalendar.txt','a')
            SavetheMonth.write(currentMonth +'\n')
            SavetheMonth.close()
            break
    while True: #Year
        print('What is the current year')
        currentYear = input()
        if currentYear.isdecimal == False:
            print('That is not a valid input, please enter the year in digits')
        else:
            SavetheYear = open('DnDcalendar.txt','a')
            SavetheYear.write(currentYear)
            SavetheYear.close()
            break

#Introduction portion, ensures a uniform folder and checks to see if a date currently exists
print('Welcome to the calendar!')
os.chdir('C:\\Users')
if os.path.exists('C:\\Users\\DnDcalendar.txt') == False: #Checks to see if the folder doesn't exist
    print('It looks like you do not have a starting date yet, let us create one!')
    createAdate()
    OpenDate = open('DnDcalendar.txt')
    ExtractDate = OpenDate.readlines()
    currentDay = str(ExtractDate[0].strip())
    currentWeek = str(ExtractDate[1].strip())
    currentMonth = str(ExtractDate[2].strip())
    currentYear = str(ExtractDate[3].strip())
    OpenDate.close()
if os.stat('C:\\Users\\DnDcalendar.txt').st_size == 0: #Checks to see if the folder exists but is empty
    print('It looks like you do not have a starting date yet, let us create one!')
    createAdate()
    OpenDate = open('DnDcalendar.txt')
    ExtractDate = OpenDate.readlines()
    currentDay = str(ExtractDate[0].strip())
    currentWeek = str(ExtractDate[1].strip())
    currentMonth = str(ExtractDate[2].strip())
    currentYear = str(ExtractDate[3].strip())
    OpenDate.close()
else: #If the folder exists, tells you the date
    OpenDate = open('DnDcalendar.txt')
    ExtractDate = OpenDate.readlines()
    currentDay = str(ExtractDate[0].strip())
    currentWeek = str(ExtractDate[1].strip())
    currentMonth = str(ExtractDate[2].strip())
    currentYear = str(ExtractDate[3].strip())
    OpenDate.close()
    
#Current date
currentDayNumber = dayNumbers.get(currentDay, 0)
currentWeekNumber = weekNumbers.get(currentWeek, 0)
currentMonthNumber = monthNumbers.get(currentMonth, 0)  
currentDatename = ('The current date is ' + ' ' + currentDay + ' ' + currentWeek + ' ' + currentMonth + ' ' + currentYear)
currentDatenumber = (str(currentDayNumber) + '/' + str(currentWeekNumber) + '/' + str(currentMonthNumber) + '/' + str(currentYear))    
print(currentDatename)       
print(currentDatenumber)

#Allowing User to advance the date
print('Press Enter to advance the date by 1 day, or press any other key followed by Enter to break')
while True:
    OpenDate = open('DnDcalendar.txt')
    ExtractDate = OpenDate.readlines()
    currentDay = str(ExtractDate[0].strip())
    currentWeek = str(ExtractDate[1].strip())
    currentMonth = str(ExtractDate[2].strip())
    currentYear = str(ExtractDate[3].strip())
    OpenDate.close()
    dayPasser = input()
    if dayPasser == '':
        #Defining what the following day will be
        if currentDay == 'Decus' and currentWeek != 'Trisum':
            nextDay = 'Monus'
            nextWeek = weekList[weekList.index(str(currentWeek))+1]
            nextMonth = currentMonth
        if currentDay == 'Decus' and currentWeek == 'Trisum'and currentMonth != 'Dudecet':
            nextDay = 'Monus'
            nextWeek = 'Unum'
            nextMonth = monthList[monthList.index(str(currentMonth))+1]
        if currentDay != 'Decus':
            nextDay = dayList[dayList.index(str(currentDay))+1]
            nextWeek = currentWeek
            nextMonth = currentMonth
        if currentMonth == 'Dudecet' and currentWeek == 'Trisum' and currentDay == 'Decus':
            print('It is the end of the year, better luck next year!')
            nextDay = 'Monus'
            nextWeek = 'Unum'
            nextMonth = 'Primet'
            nextYear = int(currentYear) + 1
        else:
            nextYear = currentYear
            changeThedate = open('DnDcalendar.txt','w')
            changeThedate.write(nextDay + '\n' + nextWeek + '\n' + nextMonth + '\n' + nextYear)
            changeThedate.flush()
            changeThedate.close()


        nextDayNumber = dayNumbers.get(nextDay, 0)
        nextWeekNumber = weekNumbers.get(nextWeek, 0)
        nextMonthNumber = monthNumbers.get(nextMonth, 0)
        nextDatename = ('It is now' + ' ' + nextDay + ' ' + nextWeek + ' ' + nextMonth + ' ' + str(nextYear))
        nextDatenumber = (str(nextDayNumber) + '/' + str(nextWeekNumber) + '/' + str(nextMonthNumber) + '/' + str(nextYear))
        print(nextDatename)
        print(nextDatenumber)
    else:
        print('Goodbye Gamemaster, see you next session!')
        time.sleep(3)
        break
    

    
#TODO: Do a reverse dictionary (Done)
#TODO: Have program display current date in number and name format (Done)
#TODO: Have program save date to an outside file for reopening later (Done)
#TODO: Provide input to automatically move to next day (Done)
#TODO: Have program provide an input option for number of days to increase/decrease by
#TODO: Connect with weather
