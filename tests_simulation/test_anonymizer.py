import sys
import os

# Ensure backend src is in path
sys.path.append(os.path.join(os.getcwd(), 'backend', 'src'))

from ai.security.anonymizer import Anonymizer

def run_anonymizer_tests():
    print("=============================================================")
    print("        TEST UNIFIER - MODULE D'ANONYMISATION ORIA           ")
    print("=============================================================")
    
    anonymizer = Anonymizer()
    
    # Test cases: (Input text, Expected output text)
    test_cases = [
        (
            "Mme Antoinette Durand, 88 ans, vit à Hyères.",
            "Mme A. D., 88 ans, vit à Hyères."
        ),
        (
            "M. Albert Vacek, 65 ans, habite à Toulon.",
            "M. A. V., 65 ans, habite à Toulon."
        ),
        (
            "Monsieur Jean-Pierre Le Pen est fatigué.",
            "Monsieur J. P. L. P. est fatigué."
        ),
        (
            "Mme Durand refuse de voir son médecin.",
            "Mme D. refuse de voir son médecin."
        ),
        (
            "Mademoiselle Sophie-Marie De L'Alba est sous curatelle.",
            "Mademoiselle S. M. D. L. A. est sous curatelle."
        ),
        (
            "La situation de M. Roux vit seule à Toulon.",
            "La situation de M. R. vit seule à Toulon."
        )
    ]
    
    passed_count = 0
    for idx, (input_text, expected) in enumerate(test_cases, 1):
        result = anonymizer.pseudonymize(input_text)
        if result == expected:
            print(f"[OK] Test {idx} réussi !")
            passed_count += 1
        else:
            print(f"[ERREUR] Test {idx} échoué !")
            print(f"  Entrée   : {input_text}")
            print(f"  Obtenu   : {result}")
            print(f"  Attendu  : {expected}")
            
    print("=============================================================")
    print(f"Résultat des tests : {passed_count}/{len(test_cases)} réussis.")
    print("=============================================================")
    
    return passed_count == len(test_cases)

if __name__ == "__main__":
    success = run_anonymizer_tests()
    sys.exit(0 if success else 1)
