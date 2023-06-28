from unittest import TestCase


from src.parser import parse
from src.parser import detect_imp

from src.imps import ImpHandler

# SHORT TEST CONSTANTS
B_STACK = ' '
B_FLOW = '\n'
B_ARITH = '\t '
B_HEAP = '\t\t'
B_IO = '\t\n'



class BaseImpDetectionTest(TestCase):
    def setUp(self):
        pass

    def test_b_stack(self):
        result = detect_imp(B_STACK)
        imp = result[0]
        self.assertEqual('stack', imp)


    def test_b_flow(self):
        result = detect_imp(B_FLOW)
        imp = result[0]
        self.assertEqual('flow', imp)


    def test_b_arith(self):
        result = detect_imp(B_ARITH)
        imp = result[0]
        self.assertEqual('arith', imp)

    
    def test_b_heap(self):
        result = detect_imp(B_HEAP)
        imp = result[0]
        self.assertEqual('heap', imp)
        

    
    def test_b_io(self):
        result = detect_imp(B_IO)
        imp = result[0]
        self.assertEqual('io', imp)
        


class BaseIMPClassDetection(TestCase):

    def setUp(self):
        self.handler = ImpHandler()

    def test_b_imp_stack(self):
        result = self.handler.detect_imp(B_STACK)
        imp = result[0]
        self.assertEqual('stack', imp.ident)


    def test_b_imp_flow(self):
        result = self.handler.detect_imp(B_FLOW)
        imp = result[0]
        self.assertEqual('flow', imp.ident)


    def test_b_imp_arith(self):
        result = self.handler.detect_imp(B_ARITH)
        imp = result[0]
        self.assertEqual('arith', imp.ident)

    
    def test_b_imp_heap(self):
        result = self.handler.detect_imp(B_HEAP)
        imp = result[0]
        self.assertEqual('heap', imp.ident)
        

    
    def test_b_imp_io(self):
        result = self.handler.detect_imp(B_IO)
        imp = result[0]
        self.assertEqual('io', imp.ident)
        

#def parse(buffer):
#    while len(buffer):
#       imp, buffer = detect_imp(buffer)

