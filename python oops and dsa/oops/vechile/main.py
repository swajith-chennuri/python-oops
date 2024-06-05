from vehicle import bike ,car ,scooty
def main():
    Xpulse=bike(color="Black",num_tyre=2,gears=5)
    XUV700=car(color="white",num_tyre=4,gears=6)
    Activa=scooty(color="blue",num_tyre=2,gears=0)

    XUV700.display_details()
    print("------------------------------------------------------------")
    Xpulse.display_details()
    print("------------------------------------------------------------")
    Activa.display_details()

main()