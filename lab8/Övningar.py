#%%
from cal_ui import *

#---Övning 801---
#calhelp()
#Ger en påminnelse om vilka kommandon (funktioner) som finns.

#show_calendars()
#Visar vilka almanackor som finns.

#create(cal_name)
#Skapar en ny almanacka med det angivna namnet.
#Exempel: create("Kaylee")

#show(cal_name, d, m)
#Visar alla bokningar för den angivna dagen.
#Exempel: show("Inara", 1, "jul")

#book(cal_name, d, m, t1, t2, subject_text)
#Bokar ett nytt möte i den angivna almanackan.
#Exempel: book("Kaylee", 12, "nov", "19:00", "21:00",
#        "Repair engine")

#remove(cal_name, d, m, start)
#Avbokar ett möte med given starttid i almanackan. Denna implementerar du i 8C.
#Exempel: remove("Kaylee",
#        12, "nov", "19:00")

#save(filename)
#Sparar samtliga existerande almanackor i en extern fil.
#Exempel: save("testdata")

#load(filename)
#Laddar in almanackor från en extern fil. Detta ersätter alla nuvarande almanackor.
#Exempel: load("testdata")

if __name__ == "__main__":
    #create("Adam")
    #book("Adam", 24, "dec", "12:00", "15:00", "Jul")
    #calhelp() prints all reminder of options
    #show_calendars()
    #save("testdata.txt")
    #load("testdata")
    #show("Adam", 24, "dec")
    
    #h1 = new_hour(16)
    #m1 = new_minute(15)
    #t1 = new_time(h1, m1)

    #h2 = new_hour(19)
    #m2 = new_minute(30)
    #t2 = new_time(h2, m2)

    #time_span = new_time_span(t1, t2)
    #sub = new_subject("Rob bank")
    #app = new_appointment(time_span, sub)
    #print(app_subject(app))
    #print(subject_text(app_subject(app)))
    
    global t1315
    t1315 = new_time(new_hour(13), new_minute(15))

    global ts1315
    ts1315 = new_time_span(
        new_time(new_hour(13), new_minute(30)),
        new_time(new_hour(15), new_minute(00))
    )
    
    global cd15
    cd15 = new_calendar_day(new_day(10))
    cd15 = cd_plus_appointment(
        cd15,
        new_appointment(
            new_time_span(
                new_time(new_hour(8), new_minute(15)),
                new_time(new_hour(9), new_minute(30))
            ),
            new_subject("Redovisning av uppgift")
        ),
    )
    cd15 = cd_plus_appointment(
        cd15,
        new_appointment(
            new_time_span(
                new_time(new_hour(13), new_minute(15)),
                new_time(new_hour(15), new_minute(0))
            ),
            new_subject("Seminarium i Python")
        ),
    )
    print(cd15)
    pass
#%%