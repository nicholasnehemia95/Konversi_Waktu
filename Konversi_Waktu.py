
def time(a):
    hour=a//3600
    a-=(hour*3600)
    minute=a//60
    a-=(minute*60)

    hour=str(hour)
    minute=str(minute)
    a=str(a)

    if len(hour)<=1:
        hour=('0'+hour)
    if len(minute)<=1:
        minute=('0'+minute)
    if len(a)<=1:
        a=('0'+a)
    hasil=(f"{hour}:{minute}:{a}")
    return hasil

try:
    second=int(input('Masukkan nilai detik : '))
    if second>359999 or second<0:
        print('Invalid input!!')
    else:
        print('Konversi : ',time(second))
except:
    print('Invalid Input!!')
