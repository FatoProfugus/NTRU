from polynomial import *

def main():
	N = 251
	p = 3
	q = 257
	d = 5

	p_pol = Polynomial([-1, 0, 0, 1])
	
	q_coeff = [0 for i in range(258)]
	q_coeff[0] = -1
	q_coeff[257] = 1
	q_pol = Polynomial(q_coeff)  

	f_coeff = [0 for i in range(252)]
	f_coeff[2] = -1
	f_coeff[8] = -1
	f_coeff[44] = -1
	f_coeff[46] = -1
	f_coeff[57] = 1
	f_coeff[107] = 1
	f_coeff[134] = -1
	f_coeff[188] = 1
	f_coeff[211] = 1
	f_coeff[249] = 1
	f_coeff[251] = 1

	g_coeff = [0 for i in range(230)]
	g_coeff[29] = -1
	g_coeff[33] = 1
	g_coeff[74] = -1
	g_coeff[88] = 1
	g_coeff[92] = -1
	g_coeff[103] = 1
	g_coeff[128] = -1
	g_coeff[181] = 1
	g_coeff[192] = -1
	g_coeff[229] = 1

	m_coeff = [1, -1, 1, 1, 0, -1]

	r_coeff = [1, 1, 1, 1]

	f = Polynomial(f_coeff)
	g = Polynomial(g_coeff)
	m = Polynomial(m_coeff)
	r = Polynomial(r_coeff)

	red_N_coeff = [0 for i in range(252)]
	red_N_coeff[0] = -1
	red_N_coeff[251] = 1

	red_N = Polynomial(red_N_coeff)

	f_inv_p = f.inverse(red_N, p)
	f_inv_q = f.inverse(red_N, q)

	h = f_inv_q * g
	print("h = "+str(h))
	for i in range(len(h.coefficients)):
		h.coefficients[i] = p*h.coefficients[i]
	e_pre_mod_q = h*r+m
	for i in range(len(e_pre_mod_q.coefficients)):
		e_pre_mod_q.coefficients[i] = e_pre_mod_q.coefficients[i]%q
	e = e_pre_mod_q

	print("f_inv_p = "+str(f_inv_p))
	print("f_inv_q = "+str(f_inv_q))
	print("h = "+str(h))
	print("e = "+str(e))

if __name__ == "__main__":
	main()