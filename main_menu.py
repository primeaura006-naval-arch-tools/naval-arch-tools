from buoyancy import floating_sink
from Ship_Resistance_Calculator import resistance_ship
from ship_stability import metacentric_height

def main():
    while True:
        print("\n" + "="*35)
        print("  🚢 Naval Arch Master Tool 🚢")
        print("="*35)
        print("1. Buoyancy Calculator")
        print("2. Stability (GM) Calculator")
        print("3. Resistance & Power Calculator")
        print("4. Exit")
        print("="*35)
        
        choice = input("Enter your choice (1-4): ")
        
        # KHUD SE COMPLETE KAR YE PART 👇
        if choice == "1":
            floating_sink()
        elif choice == "2":
             metacentric_height()
        elif choice == "3":
            resistance_ship()
        elif choice == "4":
            break
        else:
            print("="*35)

if __name__ == "__main__":
    main()