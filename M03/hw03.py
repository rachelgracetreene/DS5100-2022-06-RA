# Title: DS5100 HW03
# Name: Rachel Grace
# UserID: rg5xm

for count in range(0, 101):
    if count % 3 == 0 and count % 5 != 0:
        print('Wahoo')
    elif count % 5 == 0 and count % 3 != 0:
        print('wah!')
    elif count % 5 == 0 and count % 3 == 0:
        print('Wahoowah!')
    else:
        print(count)