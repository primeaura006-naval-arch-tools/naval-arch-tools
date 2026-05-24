def main():
 
  floating_sink()
 
def floating_sink():
    v=float(input("enter the volume in metre cube: "))
    mass = float(input("Enter ship mass in kg: "))
    w = mass * 9.81  # kg to Newtons convert
    g=9.81
    rho=1025
    FB=rho*v*g
    if FB > w:
      print("✅ Ship will FLOAT")
      print(f"Buoyancy Force : {FB:.2f} N")
      print(f"Ship Weight    : {w} N")
      print(f"Extra Margin   : {FB - w:.2f} N")
    else:
      print("❌ Ship will SINK")
      print(f"Buoyancy Force : {FB:.2f} N")
      print(f"Ship Weight    : {w} N")
      print(f"Deficit        : {w - FB:.2f} N")

if __name__ == "__main__":
 main()