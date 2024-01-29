""" Calculation of Average weight of protein sequence """
import sys

test_name = input("Please enter a name for the DNA sequence: ")

print("Your sequence is: ", test_name)

# length_sequence
length_sequence = float(input("Please enter the length of the sequence: "))

# If the length_sequence is not divisible by 3
if length_sequence % 3 != 0:
    print("\n\nError: the DNA sequence is not a multiple of 3", file=sys.stderr)
    sys.exit(1)

else:
    print("Your sequence length is: ", length_sequence)

length_protein = length_sequence / 3
print("The length of the DNA sequence is: ", length_protein)

# Given that, average molecular of amino acid is 110
Average_weight_kilodalton = (length_protein * 110) / 1000
print("The average weight of the protein sequence is:", Average_weight_kilodalton)
