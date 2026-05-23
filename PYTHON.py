def main():
 
  metacentric_height()
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

def print_results(KM, KG, GM):
    print(f"KM is {KM:.2f} units")
    print(f"KG is {KG:.2f} units")
    print(f"GM is {GM:.2f} units")
    print("-" * 30)

def metacentric_height():
    KM = float(input("enter the value of KM: "))
    KG = float(input("enter the value of KG: "))
    GM = KM - KG
    if GM > 0:
        if GM > 1.0:
           stability = "Very Highly Stable 💪"
           print(f"Stability Status: {stability}")
  
        elif GM > 0.5:
           stability = "Moderately Stable ✅"
           print(f"Stability Status: {stability}")
 
        else:
            stability = "Slightly Stable ⚠️"
            print(f"Stability Status: {stability}")
            
    elif GM == 0:
       print("it is dangerous")
    
    else:
       print("it is dangerous and very risky ❌⚠")

    print_results(KM,KG,GM)
         
main()