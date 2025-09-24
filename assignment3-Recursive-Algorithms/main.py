from Q1_Palindrome import is_palindrome_iter, is_palindrome_rec
from Q2_nQueens import solve_n_queens

if __name__ == "__main__":
    print("Palindrome quick checks:")
    for w in ["rotor", "motor", "abba", "abca"]:
        print(f"{w!r}: iter={is_palindrome_iter(w)}  rec={is_palindrome_rec(w)}")

    print("\nN-Queens n=4:")
    sols = solve_n_queens(4)
    print(f"Solutions: {len(sols)}")
    for s in sols:
        print(*s, sep="\n")
        print("-")
