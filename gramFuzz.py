from fuzzingbook.fuzzingbook.bookutils import setup;
from fuzzingbook.fuzzingbook.GrammarFuzzer import GrammarFuzzer; 
from fuzzingbook.fuzzingbook.Parser import EarleyParser; 
from fuzzingbook.fuzzingbook import GrammarCoverageFuzzer;
from fuzzingbook.fuzzingbook.Grammars import EXPR_GRAMMAR,US_PHONE_GRAMMAR;

expression_fuzzer = GrammarFuzzer(EXPR_GRAMMAR) 
input = (expression_fuzzer.fuzz())

parser = EarleyParser(US_PHONE_GRAMMAR)
print(list(parser.parse(input)))
print("Input: ", input)
