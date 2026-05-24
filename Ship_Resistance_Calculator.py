def main():
    resistance_ship()
def resistance_ship():
    rho = 1025 
    V   = float(input("enter the speed of the ship: "))
    Cd  = float(input("enter the drag coefficient: "))
    A   = float(input("enter the wetted surface area: "))
    R = 0.5 * rho * (V**2) * Cd * A
    P=R*V
    print(f"Ship Resistance : {R:.2f} N")
    print(f"Ship Speed      : {V:.2f} m/s")
    print(f"Surface Area    : {A:.2f} m²")
    print(f"power:   {P:.3f} W")
    print(f"power:   {P/1000:.3f} kW")
    if R > 1000000:
        print("⚠️ Very High Resistance — Reduce Speed!")
    elif R > 500000 :
        print("🟡 Moderate Resistance — Acceptable")
    else:
        print("✅ Low Resistance — Efficient Speed")
if __name__ == "__main__":
 main()