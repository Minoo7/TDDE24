# Write your code for lab 8C (remove) here.

from cal_abstraction import *
from cal_ui import *


def cd_remove_appointment(cal_day: CalendarDay, app_start: Time) -> CalendarDay:
    """
    Returns a copy of the given CalendarDay, where an appointment has been removed.
    """
    ensure_type(app_start, Time)
    ensure_type(cal_day, CalendarDay)

    def remove_appointment(app_start: Time, appointments: List[Appointment]):
        if not appointments:
            return []
        if app_start == ts_start(app_span(appointments[0])):
            print("Appointment removed.")
            return remove_appointment(app_start, appointments[1:])
        else:
            return [appointments[0]] + remove_appointment(app_start, appointments[1:])
    
    apps = remove_appointment(app_start, cal_day.appointments)

    return new_calendar_day(cd_day(cal_day), apps)


def remove(name: str, day: int, month: str, start: str): #cal_name, d, m, t1
    """ Remove an appointment in the calendar with the given name """
    day = new_day(day)
    month = new_month(month)
    start = new_time_from_string(start)
    cal_year = get_calendar(name)
    cal_month = cy_get_month(month, cal_year)
    cal_day = cm_get_day(cal_month, day)

    # Ensure that the date is proper.  If not, this will raise an exception.
    new_date(day, month)

    day = cd_remove_appointment(cal_day, start)
    month = cm_plus_cd(cal_month, day)
    year = cy_plus_cm(cal_year, month)
    insert_calendar(name, year)


if __name__ == "__main__":
    
    # Från studiematerial
    create("Jayne")
    book("Jayne", 20, "sep", "12:00", "14:00", "Rob train")
    book("Jayne", 20, "sep", "15:00", "16:00", "Escape with loot")
    show("Jayne", 20, "sep")
    remove("Jayne", 20, "sep", "15:00")
    book("Jayne", 20, "sep", "15:00", "16:00", "Return loot")
    show("Jayne", 20, "sep")

    # Egen 1
    create("Bob")
    # Visar utan någon bokning
    show("Bob", 20, "sep")
    book("Bob", 20, "sep", "12:00", "14:00", "Rob train")
    show("Bob", 20, "sep")
    book("Bob", 20, "sep", "14:00", "16:00", "Do nothing")
    show("Bob", 20, "sep")
    # Tar väck första bokningen
    remove("Bob", 20, "sep", "12:00")
    # Visar att den har tagits väck
    show("Bob", 20, "sep")
    # Tar väck andra bokningen
    remove("Bob", 20, "sep", "14:00")
    # Visar att bokningen tagits väck och att det nu inte finns några bokingar
    show("Bob", 20, "sep")

    # Egen 2
    create("Mike")
    # Bokar en tid
    book("Mike", 20, "sep", "00:00", "14:00", "Rob train")
    show("Mike", 20, "sep")
    # Försöker boka samma tid igen
    book("Mike", 20, "sep", "00:00", "14:00", "Rob train")
    # Visar att den inte har lagts in igen
    show("Mike", 20, "sep")
    # Försöker ta bort en tid med fel starttid
    remove("Mike", 20, "sep", "10:00")
    # Visar att inget har tagits bort
    show("Mike", 20, "sep")
