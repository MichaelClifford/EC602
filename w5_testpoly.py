import unittest
import sys


class PolynomialTestCase(unittest.TestCase):

	def test_basic(self):
		p = Polynomial([])
		self.assertEqual(p[0],0)

	def test_init(self):
		p = Polynomial([])
		self.assertIsInstance(p,Polynomial)
		a = Polynomial([1,2,3])
		b = Polynomial([])
		b[0] = 3
		b[1] = 2
		b[2] = 1
		self.assertEqual(a,b)
		
	def test_init2(self):
		e = Polynomial()
		e[1] = 1
		e[2] = 2
		e[2] = 3
		d = Polynomial()
		self.assertNotEqual(e,d)
		

	def test_add(self):
		a = Polynomial([5,1,2])
		b = Polynomial([3,4])
		c = Polynomial([5,4,6])
		self.assertEqual((a + b),c)
		self.assertNotEqual((a+c),b)
		self.assertEqual(a+b,b+a)
		self.assertNotEqual(a+b,a)
		self.assertIsInstance(a+b, Polynomial)
		

	def test_sub(self):

		a = Polynomial([5,1,2])
		b = Polynomial([3,4])
		c = Polynomial([5,4,6])
		self.assertEqual((c-b),a)
		self.assertNotEqual((a-c),b)
		self.assertIsInstance(a-b, Polynomial)

	def test_multi(self):
		a = Polynomial([1,2,-3])
		b = Polynomial([3,4])
		c = Polynomial([4,6])
		self.assertEqual(b*c, c*b)
		self.assertNotEqual(a*c,c*c)
		self.assertIsInstance(a*b, Polynomial)


	def test_Equal(self):
		a = Polynomial([1,2])
		b = Polynomial([3,4,4])
		self.assertTrue(a == a)
		self.assertFalse(a == b)
		c = Polynomial([])
		self.assertTrue(c == c)

		j = Polynomial([1,2,3])
		k = Polynomial([1,2,3])
		k[-1] = 5;
		self.assertNotEqual(j,k) 


	def test_sparse(self):
		a  = Polynomial([0,0,0,0,0,1])
		b = Polynomial([1])
		self.assertEqual(a,b)
		self.assertTrue(len(str(a)) == len(str(b))) 

	def test_sparse_zeros(self):
		n = 10000
		p = Polynomial([0]*n)
		q = Polynomial()

		p_size =sum(sys.getsizeof(getattr(p,x)) for x in vars(p))
		q_size =sum(sys.getsizeof(getattr(q,x)) for x in vars(q))		
		factor_increase = p_size/q_size
		self.assertEqual(p,q)
		self.assertLess(factor_increase,10,msg='Implementation not sparse, init with {} zeros'.format(n))
  
 

	def test_negative(self):
		a = Polynomial([1,2,3])
		a[1] = -1
		b = Polynomial([1,2,3])
		b[1] = -1
		self.assertEqual(a,b)

	def test_getitem(self):
		a = Polynomial([])
		b = Polynomial([1,2,3])
		self.assertEqual(a[5],0)
		self.assertEqual(b[0],3)


	def test_setitem(self):	
		a = Polynomial([1,2,3])
		b = Polynomial([1,2])
		b[0] = 3
		b[1] = 2
		b[2] = 1
		self.assertEqual(a,b)

		k = Polynomial([1,2,3,4,5])
		l = Polynomial([1,2,0,4,5])
		k[2] = 0
		self.assertEqual(l,k)
		

	def test_eval(self):
		a = Polynomial([1,2,3,4,-1])
		self.assertEqual(a.eval(2+3j),(-219-54j))

	def test_deriv(self):
		a = Polynomial([1,2,3,4,-1])
		a = a.deriv()
		b = Polynomial([])
		b[0] = 4
		b[1] = 6
		b[2] = 6
		b[3] = 4
		self.assertEqual(a,b)


if __name__ == '__main__':
	unittest.main()
