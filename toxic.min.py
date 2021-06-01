J=print
F=range
C=len
def A(liters,bottles):
	D=liters;A=bottles;K=I();E=-1
	if D>0 and C(A)>0:
		G=0
		if D%2==0:
			for B in F(C(A)):
				if A[B]%2==0 and A[B]<=D:G=1;break
		else:
			for B in F(C(A)):
				if A[B]%2!=0 and A[B]<=D:G=1;break
		if G==1:
			H=K.getCombinationSum(D,A)
			for B in F(C(H)):
				if C(H[B])<E or E==-1:E=C(H[B])
		J('exited:'+str(E))
	return E
class I:
	def getCombinationSum(C,sum_goal,set_integers):A=set_integers;A=list(set(A));B=[];C.findCombinations(A,sum_goal,B,{});return B
	def findCombinations(J,set_integers,sum_goal,combinations,unique,i=0,current=[]):
		H=combinations;G=unique;E=sum_goal;D=set_integers;B=current
		if E==0:
			A=[A for A in B];K=A;A.sort();A=tuple(A)
			if A not in G:G[A]=1;H.append(K)
			return
		if E<0:return
		for I in F(i,C(D)):B.append(D[I]);L=E-D[I];J.findCombinations(D,L,H,G,i,B);B.pop(C(B)-1)

def B():B='Should be -1';assert A(18,[1,2,5,10])==4,'Should be 4';assert A(127,[2,4,6,8])==-1,B;assert A(9,[1,4,6])==3,'Should be 3';assert A(1,[1,2,7])==1,'Should be 1';assert A(0,[1,2,7])==-1,B;assert A(-1,[1,2,7])==-1,B;J('Test passed')
B()