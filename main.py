try:
    a = 10
    if a < 18:
        raise ValueError("Baccha")
    else:
        print("Bada Baccha")

except ZeroDivisionError as e:
    print("Exception occured = > "+ str(e))

except:
    print("Exception occured = > Type unknown")

else:
    print("No exception")

finally:
    print("By Harman ltd")
