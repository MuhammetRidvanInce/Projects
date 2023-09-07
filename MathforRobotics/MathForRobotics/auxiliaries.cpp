#include <iostream>
#include <Eigen/Dense>


using namespace Eigen;
using namespace std;

int main2()
{

	// SORU - 1: 0 ile 100 aras�nda rastgele say�lardan olu�an 20x20 M isimli bir matris tan�mlay�n�z. Bu matrisi ekrana yazd�r�n�z. 
	//Bu matrisin boyutunu 100x100 olacak �ekilde geni�letip 20x20 olan k�sm�na
	//m�dahele etmeden geni�leyen yerlerdeki t�m de�erleri bir tamsay� de�i�keninde saklanabilecek maksimum say� ile de�i�tiriniz. 

	int HI = 100; // set HI and LO according to your problem.
	int LO = 1;
	int range = HI - LO;
	MatrixXd m = MatrixXd::Random(20, 20); // 3x3 Matrix filled with random numbers between (-1,1)
	m = (m + MatrixXd::Constant(20, 20, 1)) * range / 2; // add 1 to the matrix to have values between 0 and 2; multiply with range/2
	m = (m + MatrixXd::Constant(20, 20, LO)); //set LO as the lower bound (offset)
	cout << "m =\n" << m.cast<int>() << endl;






}