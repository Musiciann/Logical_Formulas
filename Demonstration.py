from Source import Logical_Formulas
from Source import Print_Table_Function

if __name__ == "__main__":
    expr = Logical_Formulas.get_expression()
    variables, results, combinations = Logical_Formulas.truth_table(expr)
    sdnf = Logical_Formulas.generate_sdnf(variables, results)
    sknf = Logical_Formulas.generate_sknf(variables, results)
    sknf_numeric = Logical_Formulas.generate_sknf_numeric(results, combinations)
    sdnf_numeric = Logical_Formulas.generate_sdnf_numeric(results, combinations)
    print(results)
    print(f"Simplified Disjunctive Normal Form (SDNF): {sdnf}")
    print(f"Simplified Conjunctive Normal Form (SCNF): {sknf}")
    print(f"Numeric Simplified Disjunctive Normal Form (SDNF): {sdnf_numeric}")
    print(f"Numeric Simplified Conjunctive Normal Form (SCNF): {sknf_numeric}")