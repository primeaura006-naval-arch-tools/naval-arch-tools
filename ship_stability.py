def main():
    metacentric_height()
    
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

if __name__ == "__main__":
 main()