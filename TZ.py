
mounths = {
    '1':{'name':'January','day':31},
    '2':{'name':'February','day':28},# or 29
    '3':{'name':'March','day':31},
    '4':{'name':'April','day':30},
    '5':{'name':'May','day':31},
    '6':{'name':'June','day':30},
    '7':{'name':'July','day':31},
    '8':{'name':'August','day':31},
    '9':{'name':'September','day':30},
    '10':{'name':'October','day':31},
    '11':{'name':'November','day':30},
    '12':{'name':'December','day':31}, 
}

#if years division 4 or 400, 29 day in February
week_day = {
    '1':'Monday',
    '2':'Tuesday',
    '3':'Wednesday',
    '4':'Thursday',
    '5':'Friday',
    '6':'Saturday',
    '7':'Sunday' 
}


def amount_day_years(year)->int:
    count = 0
    for years in range(1900,year):
        if (years / 4) == round(years/4) and years != 1900:
           count += 366
        else:
            count += 365
    return count
    
    
def get_days(day,mounth,year)->int:
    count = 0
    if mounth >1:
        for x in range(1 ,mounth):
            y = mounths[str(x)]['day']
            count += y
        count += day 
    else:
        count += day
        
    if (year/4) == round(year/4):
        count += 1
          
    count = count%7
    return count
    
    
def getDayInfo(date:str):
    date = date.split('.') 
    day, mounth, year = date

    year = int(year)
    count = amount_day_years(year)
    days = get_days(int(day),int(mounth),int(year))
    
    day_of_week = (count+(int(days)))%7
    if day_of_week == 0:
        day_of_week = 7
    day_name = week_day[str(day_of_week)]
    mounth_name = mounths[mounth]['name']

    week_num = int(day)/7
    if week_num < 1:
        week_num = 1
    elif week_num > round(week_num):
        week_num = round(week_num)+1
    else:
        week_num = round(week_num)
        
    print(day_name,week_num,'week', mounth_name,year)

getDayInfo('29.8.1915')

