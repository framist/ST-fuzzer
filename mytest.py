from fuzzingbook.Grammars import EXPR_EBNF_GRAMMAR, convert_ebnf_grammar, Grammar, Expansion
from fuzzingbook.Grammars import simple_grammar_fuzzer, is_valid_grammar, exp_string



expr_grammar = convert_ebnf_grammar(EXPR_EBNF_GRAMMAR)
print(expr_grammar)