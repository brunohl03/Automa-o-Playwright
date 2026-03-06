from pytest_bdd import scenarios
from steps.elements_steps import *  # ✅ Importação correta com wildcard

# caminho correto: está na pasta "features" da raiz, não dentro de "tests"
scenarios("../features/elements.feature")