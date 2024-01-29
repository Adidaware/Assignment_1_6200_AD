""" Calculation of concentration and volume of NaCl and MgCl2 """
def main():
    """ Final volume of NaCl and MgCl2 """
    final_volume = float(input("Please enter the final volume of the solution (ml): "))

    # Code for the NaCl solution:
    nacl_solution = float(input('Please enter the NaCl stock (mM): '))
    nacl_final_solution = float(input("Please enter the NaCl final (mM): "))

    # Code for the MgCl2 solution:
    mg_solution = float(input('Please enter the MgCl2 stock (mM): '))
    mg_final_solution = float(input('Please enter the MgCl2 final (mM): '))

    # Mathematical Part:
    step1 = f"Add {(final_volume * (nacl_final_solution / nacl_solution))} ml NaCl\n"
    step2 = f"Add {(final_volume * (mg_final_solution / mg_solution))} ml MgCl2\n"
    step3 = f"Add water to a final volume of {final_volume} ml and mix"

    # Final output
    print(step1 + step2 + step3)

if __name__ == "__main__":
    main()
