import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_1_No_entry_point(self):
        input = """
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))
        
    def test_2_No_entry_point(self):
        input = """
            func main()
            func main() begin
                number main
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 402))
        
    def test_3_No_entry_point(self):
        input = """
            func main(number a) begin
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 403))
        
    def test_4_No_entry_point(self):
        input = """
            func main() return 1   
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_5_No_entry_point(self):        
        input = """
            number VoTien
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_1_NoDefinition(self):
        input = """
            func foo(number a)
            func foo(number a) return     
        
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_2_NoDefinition(self):
        input = """
            func foo(number a) return   
        
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 407))
        
    def test_3_NoDefinition(self):
        input = """
            func foo(number a) 
        
            func main() return
        """
        expect = "No Function Definition: foo"
        self.assertTrue(TestChecker.test(input, expect, 408))
        
    def test_1_Redeclared(self):
        input = """
            number a
            string a 
            
            func main() return
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 410))
        
    def test_2_Redeclared(self):
        input = """
            func a()
            number a
            
            func main() return
        """
        expect = "No Function Definition: a"
        self.assertTrue(TestChecker.test(input, expect, 411))
        
    def test_3_Redeclared(self):
        input = """
            func foo() return
            func foo()
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_4_Redeclared(self): 
        input = """
            func foo()
            func foo()
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 413))
        
    def test_5_Redeclared(self): 
        input = """
            func foo() return
            func foo() return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_6_Redeclared(self):         
        input = """
            number foo
            func foo() return
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 415))
        
    def test_7_Redeclared(self):
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                number c
                string VoTien
                begin
                    number c
                    string VoTien
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 416))
        
    def test_8_Redeclared(self):
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                string a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 417))
        
    def test_9_Redeclared(self):
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                begin
                    number a
                end
                string a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 418))
        
    def test_10_Redeclared(self):
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                begin
                    number a
                    string a
                end
                
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 419))
        
    def test_11_Redeclared(self):
        input = """
            number a
            func VoTien(number a, number VoTien, number c)
            begin
                string c
            end
            
            func main() return
        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 420))
        
    def test_12_Redeclared(self):
        input = """
            number a
            func VoTien(number a, number VoTien, number c, string c)
            begin
            end
            
            func main() return
        """
        expect = "Redeclared Parameter: c"
        self.assertTrue(TestChecker.test(input, expect, 421))
        
    def test_13_Redeclared(self):
        input = """
            number a
            func VoTien(number a, number VoTien, number c)
            begin
                begin
                    number a
                end
                number a
            end
            
            func main() return
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_14_Redeclared(self):        
        input = """
            func foo(number a) 
            func foo(number b) return
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_15_Redeclared(self):        
        input = """
            func foo(number a) 
            func foo(string a) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 423))
        
    def test_16_Redeclared(self):        
        input = """
            func foo(number a) 
            func foo(number a, string c) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 424))
        
    def test_17_Redeclared(self):         
        input = """
            func foo(number a, string c) 
            func foo(number a) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 425))
        
    def test_1_Undeclared(self):
        input = """
            number a <- a
            func main() begin
                number b <- a
                number c <- e
            end
        """
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_2_Undeclared(self):
        input = """
            func a() return 1
            func main() begin
                number b <- a
            end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_3_Undeclared(self):
        input = """
            func a() return 1
            func main() begin
                number a
                begin 
                    number d
                end
                number b <- a
                number c <- d
            end
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 428))
        
    def test_4_Undeclared(self):
        input = """
            func a() begin
                a()
            end
            func main() begin
                a()
                b()
            end
        """
        expect = "Undeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_5_Undeclared(self):        
        input = """
            func a() return
            func main() begin
                number a
                a()
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_6_Undeclared(self):        
        input = """
            func a()
            func main() begin
                a()
            end
            func a() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_1_MustInLoop(self):
        input = """
            func main() begin
                var i <- 2
                for i until true by 1
                begin
                    break
                    continue
                    begin
                        break
                        continue
                    end
                    
                    for i until true by 1
                    begin
                        break
                        continue
                    end
                    break
                    continue
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 432))
    
    def test_2_MustInLoop(self):
        input = """
            func main() begin
                break
            end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 433))
    def test_3_MustInLoop(self):
        input = """
            func main() begin
                continue
            end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 434))
        
    def test_1_TypeCannotBeInferred(self):
        input = """
            dynamic VoTien
            var a <- VoTien

            func main() return
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, Id(VoTien))"
        self.assertTrue(TestChecker.test(input, expect, 435))
        
    def test_2_TypeCannotBeInferred(self):
        input = """
            number VoTien
            var a <- VoTien
            number b <- a

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 436))
        
    def test_3_TypeCannotBeInferred(self):
        input = """
            dynamic VoTien
            number a <- VoTien
            number b <- VoTien

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_4_TypeCannotBeInferred(self):
        input = """
            func foo() begin
                dynamic a
                return a
            end

            func main() return
        """
        expect = "Type Cannot Be Inferred: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 438))
        
    def test_5_TypeCannotBeInferred(self):
        input = """
            func foo() begin
                return 1
                dynamic a
                return a
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 439))
        
    def test_6_TypeCannotBeInferred(self):
        input = """
            func foo() begin
                number a
                return a
                return 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 440))
        
    def test_7_TypeCannotBeInferred(self):
        input = """
            func foo() begin
                dynamic a
                dynamic b
                a <- b
            end

            func main() return
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 441))
        
    def test_8_TypeCannotBeInferred(self):
        input = """
            func foo() begin
                number a
                dynamic b
                a <- b
                b <- 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 442))
        
    def test_9_TypeCannotBeInferred(self):
        input = """
            func foo() begin
                number a
                dynamic b
                b <- a
                b <- 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 443))
        
    def test_1_TypeMismatchInStatement(self):
        input = """
            number a <- "1"

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 444))
        
    def test_2_TypeMismatchInStatement(self):
        input = """
            number a[1,2] <- [[1,2]]

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 445))
        
    def test_3_TypeMismatchInStatement(self):
        input = """
            number a[1,2,3] <- [[1,2]]

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0, 2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_4_TypeMismatchInStatement(self):
        input = """
            number a[1] <- [[1,2]]

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))"
        self.assertTrue(TestChecker.test(input, expect, 447))       

    def test_5_TypeMismatchInStatement(self):
        input = """
            func foo() return

            func main()begin
                foo()
                foo(1)
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 448))    
        
    def test_6_TypeMismatchInStatement(self): 
        input = """
            func foo(number a) return

            func main()begin
                foo()
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 449))     
        
    def test_7_TypeMismatchInStatement(self):
        input = """
            func foo(number a) return

            func main()begin
                foo("1")
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 450))    
        
    def test_8_TypeMismatchInStatement(self): 
        input = """
            func foo(number a) return

            func main()begin
                dynamic a
                foo(a)
                number c <- a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 451))                

    def test_9_TypeMismatchInStatement(self):
        input = """
            func main()begin
                dynamic a
                if (a) return
                a <- true
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 452))     
        
    def test_10_TypeMismatchInStatement(self): 
        input = """
            func main()begin
                dynamic a <- 1
                if (a) return
            end
        """
        expect = "Type Mismatch In Statement: If((Id(a), Return()), [], None)"
        self.assertTrue(TestChecker.test(input, expect, 453))                 

    def test_11_TypeMismatchInStatement(self):
        input = """
            func main()begin
                dynamic a
                if (a) number a
                elif (a)  return
                else number a
                
                if(true) number a
                elif (1) number a
            end
        """
        expect = "Type Mismatch In Statement: If((BooleanLit(True), VarDecl(Id(a), NumberType, None, None)), [(NumLit(1.0), VarDecl(Id(a), NumberType, None, None))], None)"
        self.assertTrue(TestChecker.test(input, expect, 454)) 

    def test_12_TypeMismatchInStatement(self):
        input = """
            func foo() begin
                dynamic a
                dynamic b
                dynamic c
                for a until b by c return
                a <- 1
                b <- true
                c <- 1
            end
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 455))   
        
    def test_13_TypeMismatchInStatement(self):
        input = """
            func foo() begin
                dynamic a <- true
                dynamic b
                dynamic c
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 456))    
        
    def test_14_TypeMismatchInStatement(self):
        input = """
            func foo() begin
                dynamic a 
                dynamic b <- 2
                dynamic c
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 457))  

    def test_15_TypeMismatchInStatement(self):
        input = """
            func foo() begin
                dynamic a 
                dynamic b
                dynamic c <- "1"
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 458))    
        
    def test_16_TypeMismatchInStatement(self):
        input = """
            func foo() begin
                number a
                return 1
                return a
                return "!"
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: Return(StringLit(!))"
        self.assertTrue(TestChecker.test(input, expect, 459))  
        
    def test_17_TypeMismatchInStatement(self):        
        input = """
            func foo() begin
                number a
                a <- 1
                a <- true
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 460))  

    def test_1_TypeMismatchInExpression(self):
        input = """
            func foo() return 1

            func main() begin
                var a <- foo()
                var b <- foo(1)
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 461))
        
    def test_2_TypeMismatchInExpression(self):
        input = """
            func foo(number a) return 1

            func main() begin
                var a <- foo()
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 462))
        
    def test_3_TypeMismatchInExpression(self):
        input = """
            func foo(number a) return 1

            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 463))
        
    def test_4_TypeMismatchInExpression(self):
        input = """
            func foo(number a) return
            
            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 464))
        
    def test_5_TypeMismatchInExpression(self):
        input = """
            func foo(number a) return
            
            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 465))
        
    def test_6_TypeMismatchInExpression(self):
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- left + right
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_7_TypeMismatchInExpression(self):        
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- left + 1
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 467))
        
    def test_8_TypeMismatchInExpression(self):
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- 1 + right
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 468))
        
    def test_9_TypeMismatchInExpression(self):
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- - left
                left <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 469))
        
    def test_10_TypeMismatchInExpression(self):
        input = """
            func main() begin
                number a[1,2]
                number b
                var c <- b[1]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 470))
        
    def test_11_TypeMismatchInExpression(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- b[1]
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(c), None, var, ArrayCell(Id(b), [NumLit(1.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 471))
        
    def test_12_TypeMismatchInExpression(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[b, 1]
                b <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 472))
        
    def test_13_TypeMismatchInExpression(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a["1"]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 473))
        
    def test_14_TypeMismatchInExpression(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1,2,3]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0), NumLit(3.0)])"
        self.assertTrue(TestChecker.test(input, expect, 474))
        
    def test_15_TypeMismatchInExpression(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1,3]
                c <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 475))
        
    def test_16_TypeMismatchInExpression(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1]
                c <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 476))
        
    def test_17_TypeMismatchInExpression(self):
        input = """
            func VoTien()
            func main() begin
                number VoTien_ <- VoTien()
            end
            func VoTien() begin
            end
        """
        # expect = "???"
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 477))
        
    def test_18_TypeMismatchInExpression(self):
        input = """
            dynamic VoTien
            var x <- VoTien and (VoTien > VoTien)
        """
        expect = "Type Mismatch In Expression: BinaryOp(>, Id(VoTien), Id(VoTien))"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_19_TypeMismatchInExpression(self):
        input = """
            dynamic VoTien
            var x <- VoTien + VoTien * VoTien
            number y <- VoTien
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_20_TypeMismatchInExpression(self):
        input = """
            dynamic VoTien
            func a()
            var x <- VoTien + VoTien * a()
            func main()
            func a()
                return 2
            number y <- VoTien
        """
        expect = "No Function Definition: main"
        self.assertTrue(TestChecker.test(input, expect, 480))
        
    def test_21_TypeMismatchInExpression(self):
        input = """
            dynamic VoTien
            var x <- VoTien > VoTien ... VoTien < VoTien
        """
        expect = "Type Mismatch In Expression: BinaryOp(..., BinaryOp(>, Id(VoTien), Id(VoTien)), BinaryOp(<, Id(VoTien), Id(VoTien)))"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_22_TypeMismatchInExpression(self):
        input = """
            dynamic VoTien
            func a()
            var x <- -a()
            func main()
            func a()
                return 2
            number y <- VoTien
        """
        expect = "No Function Definition: main"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_1_full(self):
        input = """
            func areDivisors(number num1, number num2)
            return ((num1 % num2 = 0) or (num2 % num1 = 0))
            func main()
            begin
            var num1 <- readNumber()
            var num2 <- readNumber()
            if (areDivisors(num1, num2)) writeString("Yes")
            else writeString("No")
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))
        
    def test_2_full(self):
        input = """
func isPrime(number x)
func main()
begin
number x <- readNumber()
if (isPrime(x)) writeString("Yes")
else writeString("No")
end
func isPrime(number x)
begin
if (x <= 1) return false
var i <- 2
for i until i > x / 2 by 1
begin
if (x % i = 0) return false
end
return true
end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_3_full(self):
        input = """
            var VoTien <- VoTien
            func main() return
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(VoTien), None, var, Id(VoTien))"
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_4_full(self):
        input = """
            func main() return main()
        """
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(main), []))"
        self.assertTrue(TestChecker.test(input, expect, 499))
            
    def test_1_arraylit(self):
        input = """
            dynamic x
            number a <- [x]
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 501))        

    def test_2_arraylit(self):        
        input = """
            dynamic x
            number a[3] <- [x]
            func f()
            begin
                x <- [1,2,3]
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 502))        
        
    def test_3_arraylit(self):
        input = """
            dynamic x
            number a[3] <- [x, 1, 2]
            func  main()
            begin
                x <- 1
            end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 503))     
        
    def test_4_arraylit(self):
        input = """
            dynamic x
            number a[3] <- [x, x, x]
            func  main()
            begin
                x <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 504))   

    def test_5_arraylit(self):        
        input = """
            dynamic x
            number a[3] <- [x, x, "1"]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(Id(x), Id(x), StringLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 505))   
        
    def test_6_arraylit(self):
        input = """
            dynamic x
            number a[3] <- [x, 1, "1"]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), NumLit(1.0), StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 506))  
        
    def test_7_arraylit(self):
        input = """
            dynamic x
            number a[3] <- [x, [x,x], 1]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x), Id(x)), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 507))  

    def test_8_arraylit(self):
        input = """
            dynamic x
            number a[3] <- [1, [x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 508))    
        
    def test_9_arraylit(self):
        input = """
            dynamic x
            number a[3] <- [[1,2,3], [x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 509))     
        
    def test_10_arraylit(self):
        input = """
            dynamic x
            number a[3,3] <- [[1,2,3], x, x]
            func  main()
            begin
                x <- [1,2,3]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 510))     
        
    def test_11_arraylit(self):
        input = """
            dynamic x
            number a[2,3] <- [[1,2,3], [x,x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 511))  
        
    def test_12_arraylit(self):
        input = """
            dynamic x
            number a[2,3] <- [[1,2,3], 1]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 512)) 
        
    def test_13_arraylit(self):
        input = """
            dynamic x
            number a[2,3] <- [[1,2,3], [x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 513)) 
        
    def test_14_arraylit(self):
        input = """
            dynamic x
            number a[1,1,1,1] <- [[[x]]]
            func  main()
            begin
                x <- [1]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 514)) 
        
    def test_15_arraylit(self):
        input = """
            dynamic x
            number a[1,1,2,2] <- [[[[1,2], x]]]
            func  main()
            begin
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 515)) 
        
    def test_16_arraylit(self):
        input = """
            dynamic x
            number a[1,1,2,2] <- [[[x, x]]]
            func  main()
            begin
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 516)) 
  
    def test_17_arraylit(self):
        input = """
            dynamic x
            var a <- [x]
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 517))  
        
    def test_18_arraylit(self):
        input = """
            func foo() begin
                dynamic x
                return [x]                
            end
            func main() return 
        """
        expect = "Type Cannot Be Inferred: Return(ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 518))  
        
    def test_19_arraylit(self):
        input = """
            func foo() begin
                dynamic x
                return [x, [1,2]]                
            end
            func main() return 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 519))  
        
    def test_20_arraylit(self):
        input = """
            func foo() begin
                dynamic x
                dynamic y
                return [[y], [y]]
                return x
                return [[1], [2]]
            end
            func main() return 
        """
        expect = "Type Cannot Be Inferred: Return(ArrayLit(ArrayLit(Id(y)), ArrayLit(Id(y))))"
        self.assertTrue(TestChecker.test(input, expect, 520))  
        
    def test_21_arraylit(self):
        input = """
            func foo() begin
                dynamic x
                dynamic y
                return [[1], [2]]
                return [x, y]
                x <- [1]
                y <- x
            end
            func main() return 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 521)) 
        
    def test_22_arraylit(self):        
        input = """
            func foo() begin
                dynamic x
                dynamic y
                return [[1], [2]]
                return [x, [y]]
                x <- [1]
                y <- x
            end
            func main() return 
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(y), Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 522)) 
        
    def test_23_arraylit(self):
        input = """
            func foo(number a[2,2]) return
            func main() begin
                dynamic x
                foo(x)
                x <- [[2,2], [2,3]]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 523)) 
        
    def test_24_arraylit(self):
        input = """
            func foo(number a[2,2]) return
            func main() begin
                dynamic x
                foo([x])
                x <- [1]
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [ArrayLit(Id(x))])"
        self.assertTrue(TestChecker.test(input, expect, 524)) 

    def test_25_arraylit(self):
        input = """
            func foo(number a[2,2]) return
            func main() begin
                dynamic x
                foo([x, x])
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 525)) 
        
        input = """
            func foo(number a[2,2]) return 1
            func main() begin
                dynamic x
                var a <- foo([x, x])
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 526)) 
        
        input = """
            func foo(number a[2,2]) return 1
            func main() begin
                dynamic x
                var a <- foo(x)
                x <- [1,2]
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), ArrayLit(NumLit(1.0), NumLit(2.0)))"
        self.assertTrue(TestChecker.test(input, expect, 527)) 

    def test_return(self):
        input = """
            func main() begin 
                return
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 528))   

        input = """
            func main() begin 
                return 1
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 529))   

        input = """
            func main() begin 
                return 1
                begin
                    return "string"
                end
            end
        """
        expect = "Type Mismatch In Statement: Return(StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 530))    
        
        input = """
            func main() begin 
                dynamic i
                return 1
                return i
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 531))  
        
        input = """
            func fun() begin
                return 
                return
                return 1
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 532))       
        
        input = """
            func fun() begin
                return 1
                return "string"
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 533))    
        
        input = """
            func fun() begin
                number a[3]
                return [1, 4, 3]
                return a
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 534))   
        
        input = """
            func fun() begin
                number a[2,2]
                return [[1,2], [3,4]]
                return a
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 535))    
        
        input = """
            func fun() begin
                number a[3,2]
                return [[1,2], [3,4]]
                return a
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 536))  
        
        input = """
            func fun() begin
                number a[2,2]
                return a
                return [["1","2"], ["3","4"]]
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
        self.assertTrue(TestChecker.test(input, expect, 537))   
        
        input = """
            func fun() begin
                string a[2,2, 3]
                return a
                return [["1","2"], ["3","4"]]
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
        self.assertTrue(TestChecker.test(input, expect, 538))  
        
        input = """
            func fun() begin
                string a[2]
                return a
                return [["1","2"], ["3","4"]]
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
        self.assertTrue(TestChecker.test(input, expect, 539))   
        
        input = """
            func fun() begin
                string a[1,1,1,1,1]
                return a
                return [[[[["1"]]]]]
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 540))     
        
        input = """
            func fun() begin
                return [1,2]
                return [3,4]
            end
            
            func fun1() begin
                return [[1,2], [3,4]]
                return [[1,5], [3,4]]
            end
            
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 541)) 
        
        
        input = """
            func fun1() return 1
            func fun2() return
            func fun3()
            
            func main() begin 
               return fun3()
            end
        """
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(fun3), []))"
        self.assertTrue(TestChecker.test(input, expect, 542)) 
        
        input = """
            func fun1() return 1
            func fun2() return
            func fun3()
            
            func main() begin 
               return fun1()
            end
            func fun3() return 1   
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 543)) 

        input = """
            func fun1() return 1
            func fun2() return
            func fun3()
            
            func main() begin 
               number a <- fun3()
            end
            func fun3() return "1"  
        """
        expect = "Type Mismatch In Statement: Return(StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 544)) 
        
                
        input = """
            func fun1() return [1,2]
            func fun2() return [3,4]
            func fun3()
            
            func main() begin 
               return fun1()
               return fun2()
               return fun3()
            end 
        """
        expect = "No Function Definition: fun3"
        self.assertTrue(TestChecker.test(input, expect, 545)) 
        

    def test_Assign(self):
        input = """
            func main() begin 
                number a
                dynamic b
                dynamic c
                b <- c
            end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(b), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 546)) 
        

        input = """
            func main() begin 
                number a
                dynamic b
                dynamic c
                a <- c
                b <- c
                return a
                return b
                return c
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 547))   
        
        input = """
            func main() begin 
                number a
                string b
                dynamic c
                a <- c
                c <- b

            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(c), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 548))   
        
        input = """
            func main() begin 
                number a
                string b
                dynamic c
                c <- a
                b <- c

            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 549))      
        
        input = """
            func main() begin 
                number a[1,3]
                dynamic c
                c <- [[1,2,3]]
                c <- a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 550))   
        
        input = """
            func foo()
            func main() begin 
                number a[1,3]
                dynamic c
                c <- foo()
            end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(c), CallExpr(Id(foo), []))"
        self.assertTrue(TestChecker.test(input, expect, 551)) 
        
        input = """
            func foo()
            func main() begin 
                number a[1,3]
                dynamic c
                a <- foo()
            end
            func foo()
                return [[1,2,3]]
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 552))
        
        input = """
            func foo()
            func main() begin 
                number a[1,3]
                dynamic c
                a <- foo()
            end
            func foo()
                return [1,2,3]
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 553))

                
        input = """
            func foo(number x, string y)
            func foo(number x, number x)
            begin
                return [1,2,3]
            end
            func main() begin 
                number a[1,3]
            end
            
        """
        expect = "Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input, expect, 554))

        input = """
            func main() begin 
                dynamic a
                number x <- a[0]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 555))

        input = """
            func main() begin 
                dynamic a
                var x <- a[0]
                end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), None, var, ArrayCell(Id(a), [NumLit(0.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 556))

        input = """
            func main() begin 
                dynamic x
                number a[2,2] <- [x, [x,x]]
                end
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 557))
