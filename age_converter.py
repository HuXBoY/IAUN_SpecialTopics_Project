while 1:
    age_in_years = int(input("Enter Age: "))
    age_in_days = age_in_years * 365.25
    age_in_hours = int(age_in_days * 24)
    age_in_minutes = age_in_hours * 60
    age_in_seconds = age_in_minutes * 60

    print(f"age in Years: {age_in_years}, age in Hours: {age_in_hours}, age in Minutes: {age_in_minutes}, age in Seconds: {age_in_seconds}")
