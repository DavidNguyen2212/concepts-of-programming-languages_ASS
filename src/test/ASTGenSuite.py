import unittest
from TestUtils import TestAST
from main.zcode.utils.AST import *

class ASTGenSuite(unittest.TestCase):
	def test_301(self):
		input = '''
var V9 <- [31.5] % 69.47
func rjRw (number mDyN[79.53,68.85,81.7], number fvU, string AV[28.39,71.81])
	return

func yDa ()
	return
number k2S
func OQ (number HsP, bool EvE[20.42,78.07], string u_F)
	begin
		Hek(gys(86.28), gZSm, true)
		return
	end
'''
		expect = '''Program([VarDecl(Id(V9), None, var, BinaryOp(%, ArrayLit(NumLit(31.5)), NumLit(69.47))), FuncDecl(Id(rjRw), [VarDecl(Id(mDyN), ArrayType([79.53, 68.85, 81.7], NumberType), None, None), VarDecl(Id(fvU), NumberType, None, None), VarDecl(Id(AV), ArrayType([28.39, 71.81], StringType), None, None)], Return()), FuncDecl(Id(yDa), [], Return()), VarDecl(Id(k2S), NumberType, None, None), FuncDecl(Id(OQ), [VarDecl(Id(HsP), NumberType, None, None), VarDecl(Id(EvE), ArrayType([20.42, 78.07], BoolType), None, None), VarDecl(Id(u_F), StringType, None, None)], Block([CallStmt(Id(Hek), [CallExpr(Id(gys), [NumLit(86.28)]), Id(gZSm), BooleanLit(True)]), Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 301))

	def test_302(self):
		input = '''
string c7b
func sid2 (bool AO, bool SsIh[86.68])	return 16.18

func tydf (number TyC, bool EcE0, bool bZ_[95.13,39.56])
	return

func Ki ()
	return "P"

number hl[36.16,7.04]
'''
		expect = '''Program([VarDecl(Id(c7b), StringType, None, None), FuncDecl(Id(sid2), [VarDecl(Id(AO), BoolType, None, None), VarDecl(Id(SsIh), ArrayType([86.68], BoolType), None, None)], Return(NumLit(16.18))), FuncDecl(Id(tydf), [VarDecl(Id(TyC), NumberType, None, None), VarDecl(Id(EcE0), BoolType, None, None), VarDecl(Id(bZ_), ArrayType([95.13, 39.56], BoolType), None, None)], Return()), FuncDecl(Id(Ki), [], Return(StringLit(P))), VarDecl(Id(hl), ArrayType([36.16, 7.04], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 302))

	def test_303(self):
		input = '''
func JL (string h1k[12.92,53.25,57.99], string ILVr[47.42,50.55], bool zOp[19.61,27.87,24.58])
	return 19.49

var RR3 <- blF
'''
		expect = '''Program([FuncDecl(Id(JL), [VarDecl(Id(h1k), ArrayType([12.92, 53.25, 57.99], StringType), None, None), VarDecl(Id(ILVr), ArrayType([47.42, 50.55], StringType), None, None), VarDecl(Id(zOp), ArrayType([19.61, 27.87, 24.58], BoolType), None, None)], Return(NumLit(19.49))), VarDecl(Id(RR3), None, var, Id(blF))])'''
		self.assertTrue(TestAST.test(input, expect, 303))

	def test_304(self):
		input = '''
func r1Q (number eSA[26.07,91.38,82.16], bool elFC[41.75], number ZGsl)	return

func NFxF (string yWQR, number YQ[60.82])	return

'''
		expect = '''Program([FuncDecl(Id(r1Q), [VarDecl(Id(eSA), ArrayType([26.07, 91.38, 82.16], NumberType), None, None), VarDecl(Id(elFC), ArrayType([41.75], BoolType), None, None), VarDecl(Id(ZGsl), NumberType, None, None)], Return()), FuncDecl(Id(NFxF), [VarDecl(Id(yWQR), StringType, None, None), VarDecl(Id(YQ), ArrayType([60.82], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 304))

	def test_305(self):
		input = '''
func Kmy (string PYRA[4.34])
	return "PN"
func ftS (string isA[71.7], number ZIz[20.79,15.49], bool yn)	return false
func eM (bool Hy[3.26])	return
bool bYts[9.77] <- de9T
'''
		expect = '''Program([FuncDecl(Id(Kmy), [VarDecl(Id(PYRA), ArrayType([4.34], StringType), None, None)], Return(StringLit(PN))), FuncDecl(Id(ftS), [VarDecl(Id(isA), ArrayType([71.7], StringType), None, None), VarDecl(Id(ZIz), ArrayType([20.79, 15.49], NumberType), None, None), VarDecl(Id(yn), BoolType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(eM), [VarDecl(Id(Hy), ArrayType([3.26], BoolType), None, None)], Return()), VarDecl(Id(bYts), ArrayType([9.77], BoolType), None, Id(de9T))])'''
		self.assertTrue(TestAST.test(input, expect, 305))

	def test_306(self):
		input = '''
string e2py[52.93] <- "rr"
func Bn (string nk[61.56,1.79,83.09], string ju[4.57,38.47], number ao4[91.66,40.18])	return 19.77
number X3TX[15.05,29.72,51.82]
string MQun[52.88,5.73,77.33] <- false
'''
		expect = '''Program([VarDecl(Id(e2py), ArrayType([52.93], StringType), None, StringLit(rr)), FuncDecl(Id(Bn), [VarDecl(Id(nk), ArrayType([61.56, 1.79, 83.09], StringType), None, None), VarDecl(Id(ju), ArrayType([4.57, 38.47], StringType), None, None), VarDecl(Id(ao4), ArrayType([91.66, 40.18], NumberType), None, None)], Return(NumLit(19.77))), VarDecl(Id(X3TX), ArrayType([15.05, 29.72, 51.82], NumberType), None, None), VarDecl(Id(MQun), ArrayType([52.88, 5.73, 77.33], StringType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 306))

	def test_307(self):
		input = '''
func zv (number mYVi)	begin
		By7x("uVdeP", true, true)
		return
	end
'''
		expect = '''Program([FuncDecl(Id(zv), [VarDecl(Id(mYVi), NumberType, None, None)], Block([CallStmt(Id(By7x), [StringLit(uVdeP), BooleanLit(True), BooleanLit(True)]), Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 307))

	def test_308(self):
		input = '''
func LZ (string RG1U[32.82], number mXU[86.87], string FID)
	return

'''
		expect = '''Program([FuncDecl(Id(LZ), [VarDecl(Id(RG1U), ArrayType([32.82], StringType), None, None), VarDecl(Id(mXU), ArrayType([86.87], NumberType), None, None), VarDecl(Id(FID), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 308))

	def test_309(self):
		input = '''
func mphV (number b7u2, string Qk[7.83,37.1])	return Yf
func Yx8u (string VJ[57.42,80.58], string srr7[63.09])
	return

'''
		expect = '''Program([FuncDecl(Id(mphV), [VarDecl(Id(b7u2), NumberType, None, None), VarDecl(Id(Qk), ArrayType([7.83, 37.1], StringType), None, None)], Return(Id(Yf))), FuncDecl(Id(Yx8u), [VarDecl(Id(VJ), ArrayType([57.42, 80.58], StringType), None, None), VarDecl(Id(srr7), ArrayType([63.09], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 309))

	def test_310(self):
		input = '''
bool nCi[77.74,57.84]
dynamic CS9O <- "O"
number t9 <- Zkki
'''
		expect = '''Program([VarDecl(Id(nCi), ArrayType([77.74, 57.84], BoolType), None, None), VarDecl(Id(CS9O), None, dynamic, StringLit(O)), VarDecl(Id(t9), NumberType, None, Id(Zkki))])'''
		self.assertTrue(TestAST.test(input, expect, 310))

	def test_311(self):
		input = '''
func Yp50 (number bOcH[41.14,2.16], number l0, string X1D)
	return
dynamic Xc <- 83.84
'''
		expect = '''Program([FuncDecl(Id(Yp50), [VarDecl(Id(bOcH), ArrayType([41.14, 2.16], NumberType), None, None), VarDecl(Id(l0), NumberType, None, None), VarDecl(Id(X1D), StringType, None, None)], Return()), VarDecl(Id(Xc), None, dynamic, NumLit(83.84))])'''
		self.assertTrue(TestAST.test(input, expect, 311))

	def test_312(self):
		input = '''
number z8[99.16,74.92,22.44]
'''
		expect = '''Program([VarDecl(Id(z8), ArrayType([99.16, 74.92, 22.44], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 312))

	def test_313(self):
		input = '''
var ew <- "MgJA"
func Zl (number JT[84.33,0.93], string AY, number GC[53.93,48.79,91.97])
	return
func iDTq (number lYuy)
	return BU
number zu8[74.91,48.9]
number ElZU <- true
'''
		expect = '''Program([VarDecl(Id(ew), None, var, StringLit(MgJA)), FuncDecl(Id(Zl), [VarDecl(Id(JT), ArrayType([84.33, 0.93], NumberType), None, None), VarDecl(Id(AY), StringType, None, None), VarDecl(Id(GC), ArrayType([53.93, 48.79, 91.97], NumberType), None, None)], Return()), FuncDecl(Id(iDTq), [VarDecl(Id(lYuy), NumberType, None, None)], Return(Id(BU))), VarDecl(Id(zu8), ArrayType([74.91, 48.9], NumberType), None, None), VarDecl(Id(ElZU), NumberType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 313))

	def test_314(self):
		input = '''
string sWbP[27.02,65.39] <- mobl
'''
		expect = '''Program([VarDecl(Id(sWbP), ArrayType([27.02, 65.39], StringType), None, Id(mobl))])'''
		self.assertTrue(TestAST.test(input, expect, 314))

	def test_315(self):
		input = '''
var tJ <- "wrm"
func Cx (number DdB, string Mp)	begin
		begin
		end
		begin
			zs(true)
		end
		begin
		end
	end
string PSj[10.07,75.84,12.87]
'''
		expect = '''Program([VarDecl(Id(tJ), None, var, StringLit(wrm)), FuncDecl(Id(Cx), [VarDecl(Id(DdB), NumberType, None, None), VarDecl(Id(Mp), StringType, None, None)], Block([Block([]), Block([CallStmt(Id(zs), [BooleanLit(True)])]), Block([])])), VarDecl(Id(PSj), ArrayType([10.07, 75.84, 12.87], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 315))

	def test_316(self):
		input = '''
bool pWA3[20.46,24.52,43.94] <- fNpF
bool ztGp[18.77]
number MM8s[23.33,7.02,47.74] <- "CXGwV"
func p2l (number es, number s3_)
	begin
		if (v2) begin
			bool pJP[57.8,64.35] <- "Ap"
		end
		elif (52.74)
		for VG until false by "iScUw"
			begin
			end
		elif (54.9) break
		elif (22.45)
		tOM4()
		else break
	end
string Jvyg
'''
		expect = '''Program([VarDecl(Id(pWA3), ArrayType([20.46, 24.52, 43.94], BoolType), None, Id(fNpF)), VarDecl(Id(ztGp), ArrayType([18.77], BoolType), None, None), VarDecl(Id(MM8s), ArrayType([23.33, 7.02, 47.74], NumberType), None, StringLit(CXGwV)), FuncDecl(Id(p2l), [VarDecl(Id(es), NumberType, None, None), VarDecl(Id(s3_), NumberType, None, None)], Block([If((Id(v2), Block([VarDecl(Id(pJP), ArrayType([57.8, 64.35], BoolType), None, StringLit(Ap))])), [(NumLit(52.74), For(Id(VG), BooleanLit(False), StringLit(iScUw), Block([]))), (NumLit(54.9), Break), (NumLit(22.45), CallStmt(Id(tOM4), []))], Break)])), VarDecl(Id(Jvyg), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 316))

	def test_317(self):
		input = '''
func EKd ()	begin
	end

string ZaI <- 30.59
func scJ (number o5fS)
	begin
		bool l8Kd[32.65] <- "GcQ"
	end

func QCz (number FU, bool znW)	return true
'''
		expect = '''Program([FuncDecl(Id(EKd), [], Block([])), VarDecl(Id(ZaI), StringType, None, NumLit(30.59)), FuncDecl(Id(scJ), [VarDecl(Id(o5fS), NumberType, None, None)], Block([VarDecl(Id(l8Kd), ArrayType([32.65], BoolType), None, StringLit(GcQ))])), FuncDecl(Id(QCz), [VarDecl(Id(FU), NumberType, None, None), VarDecl(Id(znW), BoolType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 317))

	def test_318(self):
		input = '''
func om (bool Iul, number pjh[86.73], string Cly)
	return true
func fvuO (string T4P9[2.27,62.39], string zNYM, number wjS[33.8,5.92])	return "wyQXJ"

func FQMQ (string BMN[94.15,57.17,21.52])
	return "uvpsH"
func YPcg (string AEwL, string eMR)
	begin
		break
		if ("Alaj") continue
		elif (true) qva()
		elif (vDA) return "sjvoq"
		elif (89.51) GrQ[true, "jObbh", 85.59] <- "g"
		elif (OF)
		return
		elif (sp) jnY("v")
		O1(false, false)
	end
number lMor[3.2]
'''
		expect = '''Program([FuncDecl(Id(om), [VarDecl(Id(Iul), BoolType, None, None), VarDecl(Id(pjh), ArrayType([86.73], NumberType), None, None), VarDecl(Id(Cly), StringType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(fvuO), [VarDecl(Id(T4P9), ArrayType([2.27, 62.39], StringType), None, None), VarDecl(Id(zNYM), StringType, None, None), VarDecl(Id(wjS), ArrayType([33.8, 5.92], NumberType), None, None)], Return(StringLit(wyQXJ))), FuncDecl(Id(FQMQ), [VarDecl(Id(BMN), ArrayType([94.15, 57.17, 21.52], StringType), None, None)], Return(StringLit(uvpsH))), FuncDecl(Id(YPcg), [VarDecl(Id(AEwL), StringType, None, None), VarDecl(Id(eMR), StringType, None, None)], Block([Break, If((StringLit(Alaj), Continue), [(BooleanLit(True), CallStmt(Id(qva), [])), (Id(vDA), Return(StringLit(sjvoq))), (NumLit(89.51), AssignStmt(ArrayCell(Id(GrQ), [BooleanLit(True), StringLit(jObbh), NumLit(85.59)]), StringLit(g))), (Id(OF), Return()), (Id(sp), CallStmt(Id(jnY), [StringLit(v)]))], None), CallStmt(Id(O1), [BooleanLit(False), BooleanLit(False)])])), VarDecl(Id(lMor), ArrayType([3.2], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 318))

	def test_319(self):
		input = '''
number QP[13.25]
number Ia[35.74] <- "CP"
string XC
func gM (number i4, bool Pjba[61.32,15.44,29.65])
	return
dynamic sv
'''
		expect = '''Program([VarDecl(Id(QP), ArrayType([13.25], NumberType), None, None), VarDecl(Id(Ia), ArrayType([35.74], NumberType), None, StringLit(CP)), VarDecl(Id(XC), StringType, None, None), FuncDecl(Id(gM), [VarDecl(Id(i4), NumberType, None, None), VarDecl(Id(Pjba), ArrayType([61.32, 15.44, 29.65], BoolType), None, None)], Return()), VarDecl(Id(sv), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 319))

	def test_320(self):
		input = '''
func hLre (string pz[30.37,28.5,18.51])
	return "E"

'''
		expect = '''Program([FuncDecl(Id(hLre), [VarDecl(Id(pz), ArrayType([30.37, 28.5, 18.51], StringType), None, None)], Return(StringLit(E)))])'''
		self.assertTrue(TestAST.test(input, expect, 320))

	def test_321(self):
		input = '''
func j9 (string ytO[64.0,43.75,90.21], number dH)
	begin
		for l8zV until true by "sB"
			return
		Z9N()
		continue
	end
func P99 (bool IL)
	return ddD

func NzON (bool stI, bool hZ7e[0.37], bool TuCq)	return

number b7[64.88,39.15] <- 41.2
'''
		expect = '''Program([FuncDecl(Id(j9), [VarDecl(Id(ytO), ArrayType([64.0, 43.75, 90.21], StringType), None, None), VarDecl(Id(dH), NumberType, None, None)], Block([For(Id(l8zV), BooleanLit(True), StringLit(sB), Return()), CallStmt(Id(Z9N), []), Continue])), FuncDecl(Id(P99), [VarDecl(Id(IL), BoolType, None, None)], Return(Id(ddD))), FuncDecl(Id(NzON), [VarDecl(Id(stI), BoolType, None, None), VarDecl(Id(hZ7e), ArrayType([0.37], BoolType), None, None), VarDecl(Id(TuCq), BoolType, None, None)], Return()), VarDecl(Id(b7), ArrayType([64.88, 39.15], NumberType), None, NumLit(41.2))])'''
		self.assertTrue(TestAST.test(input, expect, 321))

	def test_322(self):
		input = '''
func Zhz (number iqh1)
	return false

func oGgF (bool ru[68.55], number gtk, number twu[80.71,44.91])
	begin
		for ufYf until 37.26 by 43.18
			return
	end
func e7 (string WV[36.73], string Xbmt[42.52,48.6], number BtaD)
	return I7
func iGX (string DnB[43.68,60.53,52.61])	return

func q0H (bool gw, number ufQ[94.96,68.6,59.4])
	return

'''
		expect = '''Program([FuncDecl(Id(Zhz), [VarDecl(Id(iqh1), NumberType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(oGgF), [VarDecl(Id(ru), ArrayType([68.55], BoolType), None, None), VarDecl(Id(gtk), NumberType, None, None), VarDecl(Id(twu), ArrayType([80.71, 44.91], NumberType), None, None)], Block([For(Id(ufYf), NumLit(37.26), NumLit(43.18), Return())])), FuncDecl(Id(e7), [VarDecl(Id(WV), ArrayType([36.73], StringType), None, None), VarDecl(Id(Xbmt), ArrayType([42.52, 48.6], StringType), None, None), VarDecl(Id(BtaD), NumberType, None, None)], Return(Id(I7))), FuncDecl(Id(iGX), [VarDecl(Id(DnB), ArrayType([43.68, 60.53, 52.61], StringType), None, None)], Return()), FuncDecl(Id(q0H), [VarDecl(Id(gw), BoolType, None, None), VarDecl(Id(ufQ), ArrayType([94.96, 68.6, 59.4], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 322))

	def test_323(self):
		input = '''
func Zuc (number gBst[11.91,16.55])	return
func pXH (string TbA[71.58])	return "IkT"

'''
		expect = '''Program([FuncDecl(Id(Zuc), [VarDecl(Id(gBst), ArrayType([11.91, 16.55], NumberType), None, None)], Return()), FuncDecl(Id(pXH), [VarDecl(Id(TbA), ArrayType([71.58], StringType), None, None)], Return(StringLit(IkT)))])'''
		self.assertTrue(TestAST.test(input, expect, 323))

	def test_324(self):
		input = '''
dynamic Jr <- Hji
number B_
string j8
'''
		expect = '''Program([VarDecl(Id(Jr), None, dynamic, Id(Hji)), VarDecl(Id(B_), NumberType, None, None), VarDecl(Id(j8), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 324))

	def test_325(self):
		input = '''
string U9 <- "VrCzn"
var da9 <- DXT
number lY
func TXy (number dd)
	return 47.28
'''
		expect = '''Program([VarDecl(Id(U9), StringType, None, StringLit(VrCzn)), VarDecl(Id(da9), None, var, Id(DXT)), VarDecl(Id(lY), NumberType, None, None), FuncDecl(Id(TXy), [VarDecl(Id(dd), NumberType, None, None)], Return(NumLit(47.28)))])'''
		self.assertTrue(TestAST.test(input, expect, 325))

	def test_326(self):
		input = '''
var gsH <- xaIc
func Fb7 (number XI[5.51,30.99], bool tPq)
	begin
		for Qaqj until true by false
			break
		SNf()
	end

dynamic mDZ <- "ZBElH"
string Whi
'''
		expect = '''Program([VarDecl(Id(gsH), None, var, Id(xaIc)), FuncDecl(Id(Fb7), [VarDecl(Id(XI), ArrayType([5.51, 30.99], NumberType), None, None), VarDecl(Id(tPq), BoolType, None, None)], Block([For(Id(Qaqj), BooleanLit(True), BooleanLit(False), Break), CallStmt(Id(SNf), [])])), VarDecl(Id(mDZ), None, dynamic, StringLit(ZBElH)), VarDecl(Id(Whi), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 326))

	def test_327(self):
		input = '''
func VeVg (bool lr[28.26,10.73], string gIm, string yx[99.01])	return

func kYY (string S3X, string kve[18.01,21.63])	begin
		begin
			continue
		end
		fLX(50.28, "fJmAV", true)
	end
'''
		expect = '''Program([FuncDecl(Id(VeVg), [VarDecl(Id(lr), ArrayType([28.26, 10.73], BoolType), None, None), VarDecl(Id(gIm), StringType, None, None), VarDecl(Id(yx), ArrayType([99.01], StringType), None, None)], Return()), FuncDecl(Id(kYY), [VarDecl(Id(S3X), StringType, None, None), VarDecl(Id(kve), ArrayType([18.01, 21.63], StringType), None, None)], Block([Block([Continue]), CallStmt(Id(fLX), [NumLit(50.28), StringLit(fJmAV), BooleanLit(True)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 327))

	def test_328(self):
		input = '''
var hD <- Dx
func KT3 (number M5Pk[9.81], bool vPE8, bool vO)
	begin
		continue
	end

func gZfY (string KQa[35.52,12.0,6.81])
	return ZaP
string I3c[65.71,98.57] <- sLEc
'''
		expect = '''Program([VarDecl(Id(hD), None, var, Id(Dx)), FuncDecl(Id(KT3), [VarDecl(Id(M5Pk), ArrayType([9.81], NumberType), None, None), VarDecl(Id(vPE8), BoolType, None, None), VarDecl(Id(vO), BoolType, None, None)], Block([Continue])), FuncDecl(Id(gZfY), [VarDecl(Id(KQa), ArrayType([35.52, 12.0, 6.81], StringType), None, None)], Return(Id(ZaP))), VarDecl(Id(I3c), ArrayType([65.71, 98.57], StringType), None, Id(sLEc))])'''
		self.assertTrue(TestAST.test(input, expect, 328))

	def test_329(self):
		input = '''
string GFh[64.63,72.43,94.54] <- sl
string gd[46.71] <- "JY"
'''
		expect = '''Program([VarDecl(Id(GFh), ArrayType([64.63, 72.43, 94.54], StringType), None, Id(sl)), VarDecl(Id(gd), ArrayType([46.71], StringType), None, StringLit(JY))])'''
		self.assertTrue(TestAST.test(input, expect, 329))

	def test_330(self):
		input = '''
func v4KO (bool Wf)
	return "Czfxv"
func fZ ()
	return

dynamic qMlq
func yhze (number wV0z[17.08,25.11], bool msD[25.24,45.25])
	begin
		break
	end

func ovRX (string bs[86.37,93.55], bool hrQ2[74.11,28.3], number Gz)
	return false
'''
		expect = '''Program([FuncDecl(Id(v4KO), [VarDecl(Id(Wf), BoolType, None, None)], Return(StringLit(Czfxv))), FuncDecl(Id(fZ), [], Return()), VarDecl(Id(qMlq), None, dynamic, None), FuncDecl(Id(yhze), [VarDecl(Id(wV0z), ArrayType([17.08, 25.11], NumberType), None, None), VarDecl(Id(msD), ArrayType([25.24, 45.25], BoolType), None, None)], Block([Break])), FuncDecl(Id(ovRX), [VarDecl(Id(bs), ArrayType([86.37, 93.55], StringType), None, None), VarDecl(Id(hrQ2), ArrayType([74.11, 28.3], BoolType), None, None), VarDecl(Id(Gz), NumberType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 330))

	def test_331(self):
		input = '''
func t5k (bool Zi, string Oh4[10.76,36.24,28.78])
	return JuG8
bool SW[19.29,41.02] <- false
func Bt8 (number L7qC, string KC, string twGl)	return

func kb2H (string qiMq, number d2aG[13.49,10.28,55.45])	begin
		AnhN[97.9] <- "rPv"
		if ("l") return "dCmG"
		elif ("ZE")
		for lxq until 5.31 by false
			for EQb until rs1 by "mETxD"
				continue
		elif (91.33)
		begin
			for ocXh until "HYi" by TD
				string Vxu
			break
		end
		elif ("mWqYd") return
		elif (25.64)
		if (false) return true
		elif (25.59) OK["H", "GbS", "Mqd"] <- 17.76
		elif ("GHVL") begin
			g3qg(LUP, true, true)
			continue
			bool RFv
		end
		else continue
	end

'''
		expect = '''Program([FuncDecl(Id(t5k), [VarDecl(Id(Zi), BoolType, None, None), VarDecl(Id(Oh4), ArrayType([10.76, 36.24, 28.78], StringType), None, None)], Return(Id(JuG8))), VarDecl(Id(SW), ArrayType([19.29, 41.02], BoolType), None, BooleanLit(False)), FuncDecl(Id(Bt8), [VarDecl(Id(L7qC), NumberType, None, None), VarDecl(Id(KC), StringType, None, None), VarDecl(Id(twGl), StringType, None, None)], Return()), FuncDecl(Id(kb2H), [VarDecl(Id(qiMq), StringType, None, None), VarDecl(Id(d2aG), ArrayType([13.49, 10.28, 55.45], NumberType), None, None)], Block([AssignStmt(ArrayCell(Id(AnhN), [NumLit(97.9)]), StringLit(rPv)), If((StringLit(l), Return(StringLit(dCmG))), [(StringLit(ZE), For(Id(lxq), NumLit(5.31), BooleanLit(False), For(Id(EQb), Id(rs1), StringLit(mETxD), Continue))), (NumLit(91.33), Block([For(Id(ocXh), StringLit(HYi), Id(TD), VarDecl(Id(Vxu), StringType, None, None)), Break])), (StringLit(mWqYd), Return()), (NumLit(25.64), If((BooleanLit(False), Return(BooleanLit(True))), [(NumLit(25.59), AssignStmt(ArrayCell(Id(OK), [StringLit(H), StringLit(GbS), StringLit(Mqd)]), NumLit(17.76))), (StringLit(GHVL), Block([CallStmt(Id(g3qg), [Id(LUP), BooleanLit(True), BooleanLit(True)]), Continue, VarDecl(Id(RFv), BoolType, None, None)]))], Continue))], None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 331))

	def test_332(self):
		input = '''
func jxy (number te3, bool mvAp[33.54])	return

func GLk ()	return m8Yq
number Z5E[79.08]
string M7[55.27] <- "qETip"
'''
		expect = '''Program([FuncDecl(Id(jxy), [VarDecl(Id(te3), NumberType, None, None), VarDecl(Id(mvAp), ArrayType([33.54], BoolType), None, None)], Return()), FuncDecl(Id(GLk), [], Return(Id(m8Yq))), VarDecl(Id(Z5E), ArrayType([79.08], NumberType), None, None), VarDecl(Id(M7), ArrayType([55.27], StringType), None, StringLit(qETip))])'''
		self.assertTrue(TestAST.test(input, expect, 332))

	def test_333(self):
		input = '''
bool e7 <- "E"
string yAa <- "ASpv"
dynamic rr
bool n1z[84.69] <- "Chk"
'''
		expect = '''Program([VarDecl(Id(e7), BoolType, None, StringLit(E)), VarDecl(Id(yAa), StringType, None, StringLit(ASpv)), VarDecl(Id(rr), None, dynamic, None), VarDecl(Id(n1z), ArrayType([84.69], BoolType), None, StringLit(Chk))])'''
		self.assertTrue(TestAST.test(input, expect, 333))

	def test_334(self):
		input = '''
bool XYTK[50.53,13.62,82.91]
'''
		expect = '''Program([VarDecl(Id(XYTK), ArrayType([50.53, 13.62, 82.91], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 334))

	def test_335(self):
		input = '''
bool Ln34[15.39,98.24] <- 43.34
var BA9 <- o8
func dQ3 ()
	return 62.18

bool vs[83.56] <- O8
'''
		expect = '''Program([VarDecl(Id(Ln34), ArrayType([15.39, 98.24], BoolType), None, NumLit(43.34)), VarDecl(Id(BA9), None, var, Id(o8)), FuncDecl(Id(dQ3), [], Return(NumLit(62.18))), VarDecl(Id(vs), ArrayType([83.56], BoolType), None, Id(O8))])'''
		self.assertTrue(TestAST.test(input, expect, 335))

	def test_336(self):
		input = '''
func HR ()
	return 41.56

func qlA (bool sXH, string CB[41.14,50.3,52.75], number Soww)
	begin
	end

var ntK1 <- "nA"
string WK[87.41] <- "l"
'''
		expect = '''Program([FuncDecl(Id(HR), [], Return(NumLit(41.56))), FuncDecl(Id(qlA), [VarDecl(Id(sXH), BoolType, None, None), VarDecl(Id(CB), ArrayType([41.14, 50.3, 52.75], StringType), None, None), VarDecl(Id(Soww), NumberType, None, None)], Block([])), VarDecl(Id(ntK1), None, var, StringLit(nA)), VarDecl(Id(WK), ArrayType([87.41], StringType), None, StringLit(l))])'''
		self.assertTrue(TestAST.test(input, expect, 336))

	def test_337(self):
		input = '''
func JgVP (bool RUSq[73.33,3.5,17.46], bool es, string pGkN[21.22,91.5])
	return
string iVW[6.25,28.59,63.23] <- false
func IFkY (bool vx)	begin
		QpJ(35.12)
	end

var z8 <- true
bool Rhe
'''
		expect = '''Program([FuncDecl(Id(JgVP), [VarDecl(Id(RUSq), ArrayType([73.33, 3.5, 17.46], BoolType), None, None), VarDecl(Id(es), BoolType, None, None), VarDecl(Id(pGkN), ArrayType([21.22, 91.5], StringType), None, None)], Return()), VarDecl(Id(iVW), ArrayType([6.25, 28.59, 63.23], StringType), None, BooleanLit(False)), FuncDecl(Id(IFkY), [VarDecl(Id(vx), BoolType, None, None)], Block([CallStmt(Id(QpJ), [NumLit(35.12)])])), VarDecl(Id(z8), None, var, BooleanLit(True)), VarDecl(Id(Rhe), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 337))

	def test_338(self):
		input = '''
func dd7z ()	begin
		continue
	end
'''
		expect = '''Program([FuncDecl(Id(dd7z), [], Block([Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 338))

	def test_339(self):
		input = '''
string zlHY[13.65,30.16,47.12]
'''
		expect = '''Program([VarDecl(Id(zlHY), ArrayType([13.65, 30.16, 47.12], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 339))

	def test_340(self):
		input = '''
func jx (string iU, bool kH, string Pyh_)
	return "nh"

var MI <- "xELp"
func Vb6c (number jpHA[33.2,70.45,68.28])	begin
		s8A[34.18, xV, 52.44] <- 16.11
	end

func hPxa (bool NbrY[3.12,71.79,10.52])
	return "tF"
number j9_[39.93,51.09] <- VyS
'''
		expect = '''Program([FuncDecl(Id(jx), [VarDecl(Id(iU), StringType, None, None), VarDecl(Id(kH), BoolType, None, None), VarDecl(Id(Pyh_), StringType, None, None)], Return(StringLit(nh))), VarDecl(Id(MI), None, var, StringLit(xELp)), FuncDecl(Id(Vb6c), [VarDecl(Id(jpHA), ArrayType([33.2, 70.45, 68.28], NumberType), None, None)], Block([AssignStmt(ArrayCell(Id(s8A), [NumLit(34.18), Id(xV), NumLit(52.44)]), NumLit(16.11))])), FuncDecl(Id(hPxa), [VarDecl(Id(NbrY), ArrayType([3.12, 71.79, 10.52], BoolType), None, None)], Return(StringLit(tF))), VarDecl(Id(j9_), ArrayType([39.93, 51.09], NumberType), None, Id(VyS))])'''
		self.assertTrue(TestAST.test(input, expect, 340))

	def test_341(self):
		input = '''
string XEh
func z8P (bool f9, number cpQK)
	return

number pI <- v0QM
'''
		expect = '''Program([VarDecl(Id(XEh), StringType, None, None), FuncDecl(Id(z8P), [VarDecl(Id(f9), BoolType, None, None), VarDecl(Id(cpQK), NumberType, None, None)], Return()), VarDecl(Id(pI), NumberType, None, Id(v0QM))])'''
		self.assertTrue(TestAST.test(input, expect, 341))

	def test_342(self):
		input = '''
number PUX2[29.63]
func TH (string LR1P, bool M3Cg, bool Q8VH)
	return "ly"
func mp (bool Fs)
	return vn

func zsr3 (string JR, string tcB[3.85,38.36,10.28])
	return
func t59 (bool woT[78.54,35.78,90.15], number e3, number r8H)	return

'''
		expect = '''Program([VarDecl(Id(PUX2), ArrayType([29.63], NumberType), None, None), FuncDecl(Id(TH), [VarDecl(Id(LR1P), StringType, None, None), VarDecl(Id(M3Cg), BoolType, None, None), VarDecl(Id(Q8VH), BoolType, None, None)], Return(StringLit(ly))), FuncDecl(Id(mp), [VarDecl(Id(Fs), BoolType, None, None)], Return(Id(vn))), FuncDecl(Id(zsr3), [VarDecl(Id(JR), StringType, None, None), VarDecl(Id(tcB), ArrayType([3.85, 38.36, 10.28], StringType), None, None)], Return()), FuncDecl(Id(t59), [VarDecl(Id(woT), ArrayType([78.54, 35.78, 90.15], BoolType), None, None), VarDecl(Id(e3), NumberType, None, None), VarDecl(Id(r8H), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 342))

	def test_343(self):
		input = '''
func jp (string dPq, bool h6tK[17.07,80.48])
	return
bool CcL8[17.62] <- qe
number rlj
func aWl (bool Vvl, bool f8O, string q4p[79.5,87.32])
	return

'''
		expect = '''Program([FuncDecl(Id(jp), [VarDecl(Id(dPq), StringType, None, None), VarDecl(Id(h6tK), ArrayType([17.07, 80.48], BoolType), None, None)], Return()), VarDecl(Id(CcL8), ArrayType([17.62], BoolType), None, Id(qe)), VarDecl(Id(rlj), NumberType, None, None), FuncDecl(Id(aWl), [VarDecl(Id(Vvl), BoolType, None, None), VarDecl(Id(f8O), BoolType, None, None), VarDecl(Id(q4p), ArrayType([79.5, 87.32], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 343))

	def test_344(self):
		input = '''
func aBh (number ATr, bool GoTT)	begin
	end

func YPO (string iPiP, bool i2p)
	begin
		number xgr[38.94] <- true
		for FS until true by zpK
			return
	end
func fu7 ()
	return 43.18

'''
		expect = '''Program([FuncDecl(Id(aBh), [VarDecl(Id(ATr), NumberType, None, None), VarDecl(Id(GoTT), BoolType, None, None)], Block([])), FuncDecl(Id(YPO), [VarDecl(Id(iPiP), StringType, None, None), VarDecl(Id(i2p), BoolType, None, None)], Block([VarDecl(Id(xgr), ArrayType([38.94], NumberType), None, BooleanLit(True)), For(Id(FS), BooleanLit(True), Id(zpK), Return())])), FuncDecl(Id(fu7), [], Return(NumLit(43.18)))])'''
		self.assertTrue(TestAST.test(input, expect, 344))

	def test_345(self):
		input = '''
dynamic adf <- false
number AWc
func lp (string ci_h, string fI[7.44,70.64,64.28])
	begin
		continue
	end

dynamic aX
number yR9[50.64,24.81]
'''
		expect = '''Program([VarDecl(Id(adf), None, dynamic, BooleanLit(False)), VarDecl(Id(AWc), NumberType, None, None), FuncDecl(Id(lp), [VarDecl(Id(ci_h), StringType, None, None), VarDecl(Id(fI), ArrayType([7.44, 70.64, 64.28], StringType), None, None)], Block([Continue])), VarDecl(Id(aX), None, dynamic, None), VarDecl(Id(yR9), ArrayType([50.64, 24.81], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 345))

	def test_346(self):
		input = '''
func o81 (bool nC, number xZ, string bPIU)
	return
func d3 ()
	return

func IPwP ()
	return

number Dm[64.69]
'''
		expect = '''Program([FuncDecl(Id(o81), [VarDecl(Id(nC), BoolType, None, None), VarDecl(Id(xZ), NumberType, None, None), VarDecl(Id(bPIU), StringType, None, None)], Return()), FuncDecl(Id(d3), [], Return()), FuncDecl(Id(IPwP), [], Return()), VarDecl(Id(Dm), ArrayType([64.69], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 346))

	def test_347(self):
		input = '''
string KH[61.73,86.76,66.27] <- 13.0
string UP[68.76,56.15] <- false
func h2W (number FaA3[37.36,38.54], bool LdY2, number RP)
	return

bool oJ6 <- 58.87
'''
		expect = '''Program([VarDecl(Id(KH), ArrayType([61.73, 86.76, 66.27], StringType), None, NumLit(13.0)), VarDecl(Id(UP), ArrayType([68.76, 56.15], StringType), None, BooleanLit(False)), FuncDecl(Id(h2W), [VarDecl(Id(FaA3), ArrayType([37.36, 38.54], NumberType), None, None), VarDecl(Id(LdY2), BoolType, None, None), VarDecl(Id(RP), NumberType, None, None)], Return()), VarDecl(Id(oJ6), BoolType, None, NumLit(58.87))])'''
		self.assertTrue(TestAST.test(input, expect, 347))

	def test_348(self):
		input = '''
func Li (string Kj[81.01])
	return 22.43

func re ()	return

func yl (bool M8[25.51,6.83])	begin
	end
var sF <- false
var gyf <- KW
'''
		expect = '''Program([FuncDecl(Id(Li), [VarDecl(Id(Kj), ArrayType([81.01], StringType), None, None)], Return(NumLit(22.43))), FuncDecl(Id(re), [], Return()), FuncDecl(Id(yl), [VarDecl(Id(M8), ArrayType([25.51, 6.83], BoolType), None, None)], Block([])), VarDecl(Id(sF), None, var, BooleanLit(False)), VarDecl(Id(gyf), None, var, Id(KW))])'''
		self.assertTrue(TestAST.test(input, expect, 348))

	def test_349(self):
		input = '''
var Tj <- true
'''
		expect = '''Program([VarDecl(Id(Tj), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 349))

	def test_350(self):
		input = '''
func z6mV (string gxf, bool sEf, string Ha)	return "iq"
'''
		expect = '''Program([FuncDecl(Id(z6mV), [VarDecl(Id(gxf), StringType, None, None), VarDecl(Id(sEf), BoolType, None, None), VarDecl(Id(Ha), StringType, None, None)], Return(StringLit(iq)))])'''
		self.assertTrue(TestAST.test(input, expect, 350))

	def test_351(self):
		input = '''
number ItZ[63.58] <- 78.6
string wp
number bwY[42.7]
string P2W[98.29,50.48,0.96]
'''
		expect = '''Program([VarDecl(Id(ItZ), ArrayType([63.58], NumberType), None, NumLit(78.6)), VarDecl(Id(wp), StringType, None, None), VarDecl(Id(bwY), ArrayType([42.7], NumberType), None, None), VarDecl(Id(P2W), ArrayType([98.29, 50.48, 0.96], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 351))

	def test_352(self):
		input = '''
number WO3Z[11.26,24.02,57.33] <- "ihoD"
'''
		expect = '''Program([VarDecl(Id(WO3Z), ArrayType([11.26, 24.02, 57.33], NumberType), None, StringLit(ihoD))])'''
		self.assertTrue(TestAST.test(input, expect, 352))

	def test_353(self):
		input = '''
string hQS9[67.1,84.11,29.85]
string lbz[6.91,79.68] <- false
string zlzH
func uE (number Uuco[98.28,33.15,81.76], number Qt)
	begin
	end
'''
		expect = '''Program([VarDecl(Id(hQS9), ArrayType([67.1, 84.11, 29.85], StringType), None, None), VarDecl(Id(lbz), ArrayType([6.91, 79.68], StringType), None, BooleanLit(False)), VarDecl(Id(zlzH), StringType, None, None), FuncDecl(Id(uE), [VarDecl(Id(Uuco), ArrayType([98.28, 33.15, 81.76], NumberType), None, None), VarDecl(Id(Qt), NumberType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 353))

	def test_354(self):
		input = '''
func UNX8 (bool LzDC)
	begin
		number xI
	end
number oB[15.67,34.38] <- true
dynamic HxkT
func db (number Qq[61.32,80.24], string wnih[25.36,75.93])	return
'''
		expect = '''Program([FuncDecl(Id(UNX8), [VarDecl(Id(LzDC), BoolType, None, None)], Block([VarDecl(Id(xI), NumberType, None, None)])), VarDecl(Id(oB), ArrayType([15.67, 34.38], NumberType), None, BooleanLit(True)), VarDecl(Id(HxkT), None, dynamic, None), FuncDecl(Id(db), [VarDecl(Id(Qq), ArrayType([61.32, 80.24], NumberType), None, None), VarDecl(Id(wnih), ArrayType([25.36, 75.93], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 354))

	def test_355(self):
		input = '''
func nHtu ()
	return bylO

var SHTk <- 64.1
func nDQl (string rqm, bool uLPA[75.52,50.35,17.8])	return 68.79
'''
		expect = '''Program([FuncDecl(Id(nHtu), [], Return(Id(bylO))), VarDecl(Id(SHTk), None, var, NumLit(64.1)), FuncDecl(Id(nDQl), [VarDecl(Id(rqm), StringType, None, None), VarDecl(Id(uLPA), ArrayType([75.52, 50.35, 17.8], BoolType), None, None)], Return(NumLit(68.79)))])'''
		self.assertTrue(TestAST.test(input, expect, 355))

	def test_356(self):
		input = '''
bool W_[39.7,31.09,97.52] <- false
string xdD[18.61,30.54,63.98]
func LgOl (string evU[97.03])	return 77.29

string A0A_ <- 32.13
dynamic Cw
'''
		expect = '''Program([VarDecl(Id(W_), ArrayType([39.7, 31.09, 97.52], BoolType), None, BooleanLit(False)), VarDecl(Id(xdD), ArrayType([18.61, 30.54, 63.98], StringType), None, None), FuncDecl(Id(LgOl), [VarDecl(Id(evU), ArrayType([97.03], StringType), None, None)], Return(NumLit(77.29))), VarDecl(Id(A0A_), StringType, None, NumLit(32.13)), VarDecl(Id(Cw), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 356))

	def test_357(self):
		input = '''
number au[69.93,72.06] <- 61.68
func yKoY (string zgy[34.65], string Te[4.26,55.55])
	begin
		for IC6J until true by 39.34
			for Fl until 84.39 by "dIXFX"
				break
		for Igux until false by false
			break
		ZG <- true
	end
bool SpJ[77.21,27.54]
'''
		expect = '''Program([VarDecl(Id(au), ArrayType([69.93, 72.06], NumberType), None, NumLit(61.68)), FuncDecl(Id(yKoY), [VarDecl(Id(zgy), ArrayType([34.65], StringType), None, None), VarDecl(Id(Te), ArrayType([4.26, 55.55], StringType), None, None)], Block([For(Id(IC6J), BooleanLit(True), NumLit(39.34), For(Id(Fl), NumLit(84.39), StringLit(dIXFX), Break)), For(Id(Igux), BooleanLit(False), BooleanLit(False), Break), AssignStmt(Id(ZG), BooleanLit(True))])), VarDecl(Id(SpJ), ArrayType([77.21, 27.54], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 357))

	def test_358(self):
		input = '''
func rL0 (bool Dk[69.54,45.72,15.33], bool ouk[45.81,26.47], number DmE0[60.59])	begin
	end
func zV ()	begin
		var jChv <- 58.92
		gG1B(BRqn)
	end

func DL ()	return
func kp (string wEJ)	return

'''
		expect = '''Program([FuncDecl(Id(rL0), [VarDecl(Id(Dk), ArrayType([69.54, 45.72, 15.33], BoolType), None, None), VarDecl(Id(ouk), ArrayType([45.81, 26.47], BoolType), None, None), VarDecl(Id(DmE0), ArrayType([60.59], NumberType), None, None)], Block([])), FuncDecl(Id(zV), [], Block([VarDecl(Id(jChv), None, var, NumLit(58.92)), CallStmt(Id(gG1B), [Id(BRqn)])])), FuncDecl(Id(DL), [], Return()), FuncDecl(Id(kp), [VarDecl(Id(wEJ), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 358))

	def test_359(self):
		input = '''
bool FRJ <- 29.68
string mwhX <- "D"
func ZX (string V8OI)	return

'''
		expect = '''Program([VarDecl(Id(FRJ), BoolType, None, NumLit(29.68)), VarDecl(Id(mwhX), StringType, None, StringLit(D)), FuncDecl(Id(ZX), [VarDecl(Id(V8OI), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 359))

	def test_360(self):
		input = '''
func Npt9 (number tcR, string C0F5, bool vX[20.24,42.43])
	begin
		begin
			dynamic Xk <- false
		end
		begin
		end
	end

func RUT (number s8L[86.4,1.03], string KS, number wA[72.74,54.14])
	return
number a0zM[49.12,83.83,64.04]
'''
		expect = '''Program([FuncDecl(Id(Npt9), [VarDecl(Id(tcR), NumberType, None, None), VarDecl(Id(C0F5), StringType, None, None), VarDecl(Id(vX), ArrayType([20.24, 42.43], BoolType), None, None)], Block([Block([VarDecl(Id(Xk), None, dynamic, BooleanLit(False))]), Block([])])), FuncDecl(Id(RUT), [VarDecl(Id(s8L), ArrayType([86.4, 1.03], NumberType), None, None), VarDecl(Id(KS), StringType, None, None), VarDecl(Id(wA), ArrayType([72.74, 54.14], NumberType), None, None)], Return()), VarDecl(Id(a0zM), ArrayType([49.12, 83.83, 64.04], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 360))

	def test_361(self):
		input = '''
number utu[48.3,90.38] <- hPh
'''
		expect = '''Program([VarDecl(Id(utu), ArrayType([48.3, 90.38], NumberType), None, Id(hPh))])'''
		self.assertTrue(TestAST.test(input, expect, 361))

	def test_362(self):
		input = '''
number caC
'''
		expect = '''Program([VarDecl(Id(caC), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 362))

	def test_363(self):
		input = '''
string lei
dynamic Pf <- 45.68
number Hzw[97.17,97.59] <- c3iL
'''
		expect = '''Program([VarDecl(Id(lei), StringType, None, None), VarDecl(Id(Pf), None, dynamic, NumLit(45.68)), VarDecl(Id(Hzw), ArrayType([97.17, 97.59], NumberType), None, Id(c3iL))])'''
		self.assertTrue(TestAST.test(input, expect, 363))

	def test_364(self):
		input = '''
func GW2 (string Qfwv)	return 35.46
string V6d2
bool JGkL[2.68]
func ztR ()	return false
'''
		expect = '''Program([FuncDecl(Id(GW2), [VarDecl(Id(Qfwv), StringType, None, None)], Return(NumLit(35.46))), VarDecl(Id(V6d2), StringType, None, None), VarDecl(Id(JGkL), ArrayType([2.68], BoolType), None, None), FuncDecl(Id(ztR), [], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 364))

	def test_365(self):
		input = '''
func KBRp (number iT, number JLCL[21.18], bool uaU[39.77])	begin
		ipe <- "HbPV"
		continue
		break
	end

func onLD (bool Mq, number atz[34.11])	return 13.65
'''
		expect = '''Program([FuncDecl(Id(KBRp), [VarDecl(Id(iT), NumberType, None, None), VarDecl(Id(JLCL), ArrayType([21.18], NumberType), None, None), VarDecl(Id(uaU), ArrayType([39.77], BoolType), None, None)], Block([AssignStmt(Id(ipe), StringLit(HbPV)), Continue, Break])), FuncDecl(Id(onLD), [VarDecl(Id(Mq), BoolType, None, None), VarDecl(Id(atz), ArrayType([34.11], NumberType), None, None)], Return(NumLit(13.65)))])'''
		self.assertTrue(TestAST.test(input, expect, 365))

	def test_366(self):
		input = '''
bool OxQ[76.76,11.46]
func ZIL0 (number cbH, number WJvG, bool QADY)
	return

var P2Ot <- "Ig"
'''
		expect = '''Program([VarDecl(Id(OxQ), ArrayType([76.76, 11.46], BoolType), None, None), FuncDecl(Id(ZIL0), [VarDecl(Id(cbH), NumberType, None, None), VarDecl(Id(WJvG), NumberType, None, None), VarDecl(Id(QADY), BoolType, None, None)], Return()), VarDecl(Id(P2Ot), None, var, StringLit(Ig))])'''
		self.assertTrue(TestAST.test(input, expect, 366))

	def test_367(self):
		input = '''
dynamic sJe1
'''
		expect = '''Program([VarDecl(Id(sJe1), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 367))

	def test_368(self):
		input = '''
func ez6 (string uAp, string mp)	begin
		break
	end

func sl (bool k2)
	return ghg
'''
		expect = '''Program([FuncDecl(Id(ez6), [VarDecl(Id(uAp), StringType, None, None), VarDecl(Id(mp), StringType, None, None)], Block([Break])), FuncDecl(Id(sl), [VarDecl(Id(k2), BoolType, None, None)], Return(Id(ghg)))])'''
		self.assertTrue(TestAST.test(input, expect, 368))

	def test_369(self):
		input = '''
string KhY3[56.73] <- "I"
string ZGeW[96.73,34.96,5.19]
number vce_ <- 97.34
number VWa[80.8,52.7] <- aqVW
string Q_Q[11.6,84.5,24.49] <- vz16
'''
		expect = '''Program([VarDecl(Id(KhY3), ArrayType([56.73], StringType), None, StringLit(I)), VarDecl(Id(ZGeW), ArrayType([96.73, 34.96, 5.19], StringType), None, None), VarDecl(Id(vce_), NumberType, None, NumLit(97.34)), VarDecl(Id(VWa), ArrayType([80.8, 52.7], NumberType), None, Id(aqVW)), VarDecl(Id(Q_Q), ArrayType([11.6, 84.5, 24.49], StringType), None, Id(vz16))])'''
		self.assertTrue(TestAST.test(input, expect, 369))

	def test_370(self):
		input = '''
var Tj <- 97.69
func tzkm (string dL)	return

bool Sjjm[99.36,84.16]
'''
		expect = '''Program([VarDecl(Id(Tj), None, var, NumLit(97.69)), FuncDecl(Id(tzkm), [VarDecl(Id(dL), StringType, None, None)], Return()), VarDecl(Id(Sjjm), ArrayType([99.36, 84.16], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 370))

	def test_371(self):
		input = '''
var ESsl <- true
number Tj3[34.7] <- zcyD
number Tb9[85.25,24.94,87.8]
'''
		expect = '''Program([VarDecl(Id(ESsl), None, var, BooleanLit(True)), VarDecl(Id(Tj3), ArrayType([34.7], NumberType), None, Id(zcyD)), VarDecl(Id(Tb9), ArrayType([85.25, 24.94, 87.8], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 371))

	def test_372(self):
		input = '''
func hX ()	return xCNu
func EpL_ (string zOd[62.88,48.73,65.4], string z_JJ)
	return 38.01

string C2[65.97] <- Dk
func Nb (string pm[91.64,36.08,87.85], bool is5F)
	return
func Ns (string sJe[16.07,98.22,47.05], bool jt2, bool S6)	return

'''
		expect = '''Program([FuncDecl(Id(hX), [], Return(Id(xCNu))), FuncDecl(Id(EpL_), [VarDecl(Id(zOd), ArrayType([62.88, 48.73, 65.4], StringType), None, None), VarDecl(Id(z_JJ), StringType, None, None)], Return(NumLit(38.01))), VarDecl(Id(C2), ArrayType([65.97], StringType), None, Id(Dk)), FuncDecl(Id(Nb), [VarDecl(Id(pm), ArrayType([91.64, 36.08, 87.85], StringType), None, None), VarDecl(Id(is5F), BoolType, None, None)], Return()), FuncDecl(Id(Ns), [VarDecl(Id(sJe), ArrayType([16.07, 98.22, 47.05], StringType), None, None), VarDecl(Id(jt2), BoolType, None, None), VarDecl(Id(S6), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 372))

	def test_373(self):
		input = '''
func XJh (number f9[93.58,58.74,10.79])	return

'''
		expect = '''Program([FuncDecl(Id(XJh), [VarDecl(Id(f9), ArrayType([93.58, 58.74, 10.79], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 373))

	def test_374(self):
		input = '''
dynamic HoW
func Xqqm (bool tvb)
	return

string ohRf[92.5,73.89,80.13]
func A6a (bool iu, string YVn[67.14], bool i_3[64.57,10.83,74.02])	begin
		oB(bC)
	end
'''
		expect = '''Program([VarDecl(Id(HoW), None, dynamic, None), FuncDecl(Id(Xqqm), [VarDecl(Id(tvb), BoolType, None, None)], Return()), VarDecl(Id(ohRf), ArrayType([92.5, 73.89, 80.13], StringType), None, None), FuncDecl(Id(A6a), [VarDecl(Id(iu), BoolType, None, None), VarDecl(Id(YVn), ArrayType([67.14], StringType), None, None), VarDecl(Id(i_3), ArrayType([64.57, 10.83, 74.02], BoolType), None, None)], Block([CallStmt(Id(oB), [Id(bC)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 374))

	def test_375(self):
		input = '''
func fQy ()
	return
'''
		expect = '''Program([FuncDecl(Id(fQy), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 375))

	def test_376(self):
		input = '''
number Jlk <- vQj
var nIBU <- "aqGrH"
bool ai[50.33] <- "ro"
func EpKg ()	begin
		return
		continue
	end
'''
		expect = '''Program([VarDecl(Id(Jlk), NumberType, None, Id(vQj)), VarDecl(Id(nIBU), None, var, StringLit(aqGrH)), VarDecl(Id(ai), ArrayType([50.33], BoolType), None, StringLit(ro)), FuncDecl(Id(EpKg), [], Block([Return(), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 376))

	def test_377(self):
		input = '''
func mpqE ()	begin
		number X_[49.16,72.42] <- 50.41
		var tU <- "Zh"
		KuKc(5.04)
	end

'''
		expect = '''Program([FuncDecl(Id(mpqE), [], Block([VarDecl(Id(X_), ArrayType([49.16, 72.42], NumberType), None, NumLit(50.41)), VarDecl(Id(tU), None, var, StringLit(Zh)), CallStmt(Id(KuKc), [NumLit(5.04)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 377))

	def test_378(self):
		input = '''
func QIm (bool tr[96.1,21.69,79.76], bool LvqN[22.96,92.19])	return

func Ukt ()	return
func xMf (bool f8wc[71.52], string xuCf[24.6,100.0,27.22], number Zubj[93.46,59.18,1.22])
	begin
	end
bool zzlz[60.27,0.46,86.24]
func tKf (string i3)
	return

'''
		expect = '''Program([FuncDecl(Id(QIm), [VarDecl(Id(tr), ArrayType([96.1, 21.69, 79.76], BoolType), None, None), VarDecl(Id(LvqN), ArrayType([22.96, 92.19], BoolType), None, None)], Return()), FuncDecl(Id(Ukt), [], Return()), FuncDecl(Id(xMf), [VarDecl(Id(f8wc), ArrayType([71.52], BoolType), None, None), VarDecl(Id(xuCf), ArrayType([24.6, 100.0, 27.22], StringType), None, None), VarDecl(Id(Zubj), ArrayType([93.46, 59.18, 1.22], NumberType), None, None)], Block([])), VarDecl(Id(zzlz), ArrayType([60.27, 0.46, 86.24], BoolType), None, None), FuncDecl(Id(tKf), [VarDecl(Id(i3), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 378))

	def test_379(self):
		input = '''
bool bJ <- "ymR"
func oZ4 (string Y0[98.73,56.52], number qBT[14.14,63.57,57.07])
	return true
'''
		expect = '''Program([VarDecl(Id(bJ), BoolType, None, StringLit(ymR)), FuncDecl(Id(oZ4), [VarDecl(Id(Y0), ArrayType([98.73, 56.52], StringType), None, None), VarDecl(Id(qBT), ArrayType([14.14, 63.57, 57.07], NumberType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 379))

	def test_380(self):
		input = '''
number S1A[87.88,62.8,34.44] <- false
bool JEn3
number iF <- pL
func da (string QL[50.5,73.76], bool Hox)	return pYIp
'''
		expect = '''Program([VarDecl(Id(S1A), ArrayType([87.88, 62.8, 34.44], NumberType), None, BooleanLit(False)), VarDecl(Id(JEn3), BoolType, None, None), VarDecl(Id(iF), NumberType, None, Id(pL)), FuncDecl(Id(da), [VarDecl(Id(QL), ArrayType([50.5, 73.76], StringType), None, None), VarDecl(Id(Hox), BoolType, None, None)], Return(Id(pYIp)))])'''
		self.assertTrue(TestAST.test(input, expect, 380))

	def test_381(self):
		input = '''
bool P2Ur[45.82,85.25] <- 6.12
func kOgg (number OJPJ)	return

func rtzp (string guZ0)
	return
string hTH[28.51]
func GSrg (bool uSHY[14.45])	return
'''
		expect = '''Program([VarDecl(Id(P2Ur), ArrayType([45.82, 85.25], BoolType), None, NumLit(6.12)), FuncDecl(Id(kOgg), [VarDecl(Id(OJPJ), NumberType, None, None)], Return()), FuncDecl(Id(rtzp), [VarDecl(Id(guZ0), StringType, None, None)], Return()), VarDecl(Id(hTH), ArrayType([28.51], StringType), None, None), FuncDecl(Id(GSrg), [VarDecl(Id(uSHY), ArrayType([14.45], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 381))

	def test_382(self):
		input = '''
string TV4[79.1]
'''
		expect = '''Program([VarDecl(Id(TV4), ArrayType([79.1], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 382))

	def test_383(self):
		input = '''
var E3 <- "mJ"
func h3 (string Eqa, string hF)
	begin
	end
func cY ()
	return JM

bool yZI[45.18,62.3,54.16]
'''
		expect = '''Program([VarDecl(Id(E3), None, var, StringLit(mJ)), FuncDecl(Id(h3), [VarDecl(Id(Eqa), StringType, None, None), VarDecl(Id(hF), StringType, None, None)], Block([])), FuncDecl(Id(cY), [], Return(Id(JM))), VarDecl(Id(yZI), ArrayType([45.18, 62.3, 54.16], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 383))

	def test_384(self):
		input = '''
number Huo
'''
		expect = '''Program([VarDecl(Id(Huo), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 384))

	def test_385(self):
		input = '''
func kZmu (string pA3[28.17])
	return yJK1

dynamic yR
func RLA ()	return sW

'''
		expect = '''Program([FuncDecl(Id(kZmu), [VarDecl(Id(pA3), ArrayType([28.17], StringType), None, None)], Return(Id(yJK1))), VarDecl(Id(yR), None, dynamic, None), FuncDecl(Id(RLA), [], Return(Id(sW)))])'''
		self.assertTrue(TestAST.test(input, expect, 385))

	def test_386(self):
		input = '''
string LzdT[47.31]
'''
		expect = '''Program([VarDecl(Id(LzdT), ArrayType([47.31], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 386))

	def test_387(self):
		input = '''
func xpry (bool zZg, bool Qp)	begin
	end

bool R1h[67.91,62.82] <- Tw
string kZe <- Al8
'''
		expect = '''Program([FuncDecl(Id(xpry), [VarDecl(Id(zZg), BoolType, None, None), VarDecl(Id(Qp), BoolType, None, None)], Block([])), VarDecl(Id(R1h), ArrayType([67.91, 62.82], BoolType), None, Id(Tw)), VarDecl(Id(kZe), StringType, None, Id(Al8))])'''
		self.assertTrue(TestAST.test(input, expect, 387))

	def test_388(self):
		input = '''
string TB
string Tbl[68.86,1.33] <- 76.47
var hE <- "khmWC"
number T3t <- "wAez"
'''
		expect = '''Program([VarDecl(Id(TB), StringType, None, None), VarDecl(Id(Tbl), ArrayType([68.86, 1.33], StringType), None, NumLit(76.47)), VarDecl(Id(hE), None, var, StringLit(khmWC)), VarDecl(Id(T3t), NumberType, None, StringLit(wAez))])'''
		self.assertTrue(TestAST.test(input, expect, 388))

	def test_389(self):
		input = '''
string VJ[51.39,28.15,70.74] <- 54.5
func OzW2 (string An[35.77], string OV)
	return
bool ka[64.67,74.0,41.15]
'''
		expect = '''Program([VarDecl(Id(VJ), ArrayType([51.39, 28.15, 70.74], StringType), None, NumLit(54.5)), FuncDecl(Id(OzW2), [VarDecl(Id(An), ArrayType([35.77], StringType), None, None), VarDecl(Id(OV), StringType, None, None)], Return()), VarDecl(Id(ka), ArrayType([64.67, 74.0, 41.15], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 389))

	def test_390(self):
		input = '''
var uWg <- "WGB"
bool XWhp[11.84,97.6,47.83]
var P9F <- 8.17
func u3br (number BUE1)
	return 12.75
func WQBw (bool VMT[9.76])
	begin
		var vFj <- "y"
		for kTa until 42.22 by "yzzR"
			kl3 <- "RD"
	end
'''
		expect = '''Program([VarDecl(Id(uWg), None, var, StringLit(WGB)), VarDecl(Id(XWhp), ArrayType([11.84, 97.6, 47.83], BoolType), None, None), VarDecl(Id(P9F), None, var, NumLit(8.17)), FuncDecl(Id(u3br), [VarDecl(Id(BUE1), NumberType, None, None)], Return(NumLit(12.75))), FuncDecl(Id(WQBw), [VarDecl(Id(VMT), ArrayType([9.76], BoolType), None, None)], Block([VarDecl(Id(vFj), None, var, StringLit(y)), For(Id(kTa), NumLit(42.22), StringLit(yzzR), AssignStmt(Id(kl3), StringLit(RD)))]))])'''
		self.assertTrue(TestAST.test(input, expect, 390))

	def test_391(self):
		input = '''
func LOg (string VNAv[18.68,7.85,41.93], number Rp[31.88,0.13,83.92])	return
func u7 ()
	begin
		return "Z"
		begin
			Ut8t("DN", 32.46, "gytNc")
		end
	end
'''
		expect = '''Program([FuncDecl(Id(LOg), [VarDecl(Id(VNAv), ArrayType([18.68, 7.85, 41.93], StringType), None, None), VarDecl(Id(Rp), ArrayType([31.88, 0.13, 83.92], NumberType), None, None)], Return()), FuncDecl(Id(u7), [], Block([Return(StringLit(Z)), Block([CallStmt(Id(Ut8t), [StringLit(DN), NumLit(32.46), StringLit(gytNc)])])]))])'''
		self.assertTrue(TestAST.test(input, expect, 391))

	def test_392(self):
		input = '''
number UJ
'''
		expect = '''Program([VarDecl(Id(UJ), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 392))

	def test_393(self):
		input = '''
number GgJ <- "qcR"
func jm (string bKv[0.28], bool UqDN)
	begin
		return
		N2(true, false)
	end

var aHRp <- "bQpvr"
func za (number UQ, number DzID[34.59,28.49])	return
'''
		expect = '''Program([VarDecl(Id(GgJ), NumberType, None, StringLit(qcR)), FuncDecl(Id(jm), [VarDecl(Id(bKv), ArrayType([0.28], StringType), None, None), VarDecl(Id(UqDN), BoolType, None, None)], Block([Return(), CallStmt(Id(N2), [BooleanLit(True), BooleanLit(False)])])), VarDecl(Id(aHRp), None, var, StringLit(bQpvr)), FuncDecl(Id(za), [VarDecl(Id(UQ), NumberType, None, None), VarDecl(Id(DzID), ArrayType([34.59, 28.49], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 393))

	def test_394(self):
		input = '''
number jM[50.61] <- zKVe
func SZqR (string K56T, bool dZ2X)
	return Ngs0
string k0X7[91.72] <- HWoY
'''
		expect = '''Program([VarDecl(Id(jM), ArrayType([50.61], NumberType), None, Id(zKVe)), FuncDecl(Id(SZqR), [VarDecl(Id(K56T), StringType, None, None), VarDecl(Id(dZ2X), BoolType, None, None)], Return(Id(Ngs0))), VarDecl(Id(k0X7), ArrayType([91.72], StringType), None, Id(HWoY))])'''
		self.assertTrue(TestAST.test(input, expect, 394))

	def test_395(self):
		input = '''
dynamic aC
func OTS3 (number db[61.03,25.07,34.01])
	begin
		continue
		number wJa <- true
		q6Um["wsYD", "rOQH"] <- false
	end
func tfBQ (string jb, string vB[82.24], string NR7I)
	return

'''
		expect = '''Program([VarDecl(Id(aC), None, dynamic, None), FuncDecl(Id(OTS3), [VarDecl(Id(db), ArrayType([61.03, 25.07, 34.01], NumberType), None, None)], Block([Continue, VarDecl(Id(wJa), NumberType, None, BooleanLit(True)), AssignStmt(ArrayCell(Id(q6Um), [StringLit(wsYD), StringLit(rOQH)]), BooleanLit(False))])), FuncDecl(Id(tfBQ), [VarDecl(Id(jb), StringType, None, None), VarDecl(Id(vB), ArrayType([82.24], StringType), None, None), VarDecl(Id(NR7I), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 395))

	def test_396(self):
		input = '''
func ewv (bool Xuq, bool q1z)	begin
	end

func KeCn (number Dx)
	begin
		begin
			for irx until pJ4 by "A"
				break
		end
		continue
		for zLKq until true by 82.63
			C1C <- "KR"
	end

func bxcS (bool LwwR, string xQ1Z)	begin
		begin
		end
		break
		string rD1l[43.77,47.01]
	end
func sI (string Lsat, bool g4[96.11,14.48,6.31], string riTW)
	return

bool zn[15.53,45.94] <- true
'''
		expect = '''Program([FuncDecl(Id(ewv), [VarDecl(Id(Xuq), BoolType, None, None), VarDecl(Id(q1z), BoolType, None, None)], Block([])), FuncDecl(Id(KeCn), [VarDecl(Id(Dx), NumberType, None, None)], Block([Block([For(Id(irx), Id(pJ4), StringLit(A), Break)]), Continue, For(Id(zLKq), BooleanLit(True), NumLit(82.63), AssignStmt(Id(C1C), StringLit(KR)))])), FuncDecl(Id(bxcS), [VarDecl(Id(LwwR), BoolType, None, None), VarDecl(Id(xQ1Z), StringType, None, None)], Block([Block([]), Break, VarDecl(Id(rD1l), ArrayType([43.77, 47.01], StringType), None, None)])), FuncDecl(Id(sI), [VarDecl(Id(Lsat), StringType, None, None), VarDecl(Id(g4), ArrayType([96.11, 14.48, 6.31], BoolType), None, None), VarDecl(Id(riTW), StringType, None, None)], Return()), VarDecl(Id(zn), ArrayType([15.53, 45.94], BoolType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 396))

	def test_397(self):
		input = '''
number d4Yf <- 31.75
'''
		expect = '''Program([VarDecl(Id(d4Yf), NumberType, None, NumLit(31.75))])'''
		self.assertTrue(TestAST.test(input, expect, 397))

	def test_398(self):
		input = '''
var QH <- false
func YLho (number Ly, bool cOB[36.22,26.74], string MAY)	return 70.46

string Qt[22.91]
func UDdo (bool sfH)
	begin
		for kC until false by true
			return
		break
		number Lpw[33.59,43.9]
	end
'''
		expect = '''Program([VarDecl(Id(QH), None, var, BooleanLit(False)), FuncDecl(Id(YLho), [VarDecl(Id(Ly), NumberType, None, None), VarDecl(Id(cOB), ArrayType([36.22, 26.74], BoolType), None, None), VarDecl(Id(MAY), StringType, None, None)], Return(NumLit(70.46))), VarDecl(Id(Qt), ArrayType([22.91], StringType), None, None), FuncDecl(Id(UDdo), [VarDecl(Id(sfH), BoolType, None, None)], Block([For(Id(kC), BooleanLit(False), BooleanLit(True), Return()), Break, VarDecl(Id(Lpw), ArrayType([33.59, 43.9], NumberType), None, None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 398))

	def test_399(self):
		input = '''
func BG ()
	begin
		Z4X(true, 26.68)
		if (true) bool V_[3.78] <- T71P
		elif (false)
		return 57.73
		elif ("KEdd") continue
		elif ("Q")
		if (true) for kp until "xQUEG" by 56.07
			GKl1 <- PW3
		elif (89.58) continue
		elif (MCEf) for E2L until "rWj" by Q5
			if ("iZ") continue
			elif (44.55) continue
			elif (false)
			number kk7V
		elif (true)
		if ("oKV") continue
		else J2i6["j", "nnSc"] <- true
		elif (0.68) vl <- true
		elif (true) if (66.42) M6Y[false, "AYlHF"] <- "LEsgQ"
		elif (77.39) number MB[59.33,26.38]
		elif (68.69) continue
		elif (true) for srRK until "Jag" by 65.64
			if (24.33) continue
			elif (reLS)
			if (94.29) break
			elif (false) gU2["q", "Lg"] <- ng
			elif (TM)
			for EPMk until 71.59 by "h"
				continue
			elif ("jUbCc") string VNB
			elif (false) if (35.9) VV_8[true, 0.04] <- A3G
			elif (true) return true
			else break
		elif (false) for wj until Mum1 by false
			d3("rT", false, "orQZB")
		elif (54.09) begin
			number Ij <- "A"
		end
		else break
		elif (59.79) odfP[13.2] <- 59.51
		else Em <- b4A0
		for SA until 71.18 by "w"
			for mo until "fXY" by MDxx
				break
	end

var BTwA <- true
number Ib[32.44]
'''
		expect = '''Program([FuncDecl(Id(BG), [], Block([CallStmt(Id(Z4X), [BooleanLit(True), NumLit(26.68)]), If((BooleanLit(True), VarDecl(Id(V_), ArrayType([3.78], BoolType), None, Id(T71P))), [(BooleanLit(False), Return(NumLit(57.73))), (StringLit(KEdd), Continue), (StringLit(Q), If((BooleanLit(True), For(Id(kp), StringLit(xQUEG), NumLit(56.07), AssignStmt(Id(GKl1), Id(PW3)))), [(NumLit(89.58), Continue), (Id(MCEf), For(Id(E2L), StringLit(rWj), Id(Q5), If((StringLit(iZ), Continue), [(NumLit(44.55), Continue), (BooleanLit(False), VarDecl(Id(kk7V), NumberType, None, None)), (BooleanLit(True), If((StringLit(oKV), Continue), [], AssignStmt(ArrayCell(Id(J2i6), [StringLit(j), StringLit(nnSc)]), BooleanLit(True)))), (NumLit(0.68), AssignStmt(Id(vl), BooleanLit(True))), (BooleanLit(True), If((NumLit(66.42), AssignStmt(ArrayCell(Id(M6Y), [BooleanLit(False), StringLit(AYlHF)]), StringLit(LEsgQ))), [(NumLit(77.39), VarDecl(Id(MB), ArrayType([59.33, 26.38], NumberType), None, None)), (NumLit(68.69), Continue), (BooleanLit(True), For(Id(srRK), StringLit(Jag), NumLit(65.64), If((NumLit(24.33), Continue), [(Id(reLS), If((NumLit(94.29), Break), [(BooleanLit(False), AssignStmt(ArrayCell(Id(gU2), [StringLit(q), StringLit(Lg)]), Id(ng))), (Id(TM), For(Id(EPMk), NumLit(71.59), StringLit(h), Continue)), (StringLit(jUbCc), VarDecl(Id(VNB), StringType, None, None)), (BooleanLit(False), If((NumLit(35.9), AssignStmt(ArrayCell(Id(VV_8), [BooleanLit(True), NumLit(0.04)]), Id(A3G))), [(BooleanLit(True), Return(BooleanLit(True)))], Break)), (BooleanLit(False), For(Id(wj), Id(Mum1), BooleanLit(False), CallStmt(Id(d3), [StringLit(rT), BooleanLit(False), StringLit(orQZB)]))), (NumLit(54.09), Block([VarDecl(Id(Ij), NumberType, None, StringLit(A))]))], Break)), (NumLit(59.79), AssignStmt(ArrayCell(Id(odfP), [NumLit(13.2)]), NumLit(59.51)))], AssignStmt(Id(Em), Id(b4A0)))))], None))], None)))], None))], None), For(Id(SA), NumLit(71.18), StringLit(w), For(Id(mo), StringLit(fXY), Id(MDxx), Break))])), VarDecl(Id(BTwA), None, var, BooleanLit(True)), VarDecl(Id(Ib), ArrayType([32.44], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 399))

	def test_400(self):
		input = '''
func Cv (number Hev[18.16])	begin
	end
'''
		expect = '''Program([FuncDecl(Id(Cv), [VarDecl(Id(Hev), ArrayType([18.16], NumberType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 400))
