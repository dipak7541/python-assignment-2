def find_out_leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print("{0} is the leap Year".format(year))
            else:
                print("{0} is not the leap Year".format(year))
        else:
            print("{0} is the leap Year".format(year))
    else:
        print("{0} is not the leap Year".format(year))


if __name__ == "__main__":
    find_out_leap(1992)
    find_out_leap(1900)
