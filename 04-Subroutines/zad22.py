def month(n):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    wynik = ""
    if n >=1 and n <=12:
        wynik += months[n-1]
    return wynik

