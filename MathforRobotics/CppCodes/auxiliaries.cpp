#include <iostream>
#include <Eigen/Dense>


using namespace Eigen;
using namespace std;

int main2()
{

	// SORU - 1: 0 ile 100 arasýnda rastgele sayýlardan oluþan 20x20 M isimli bir matris tanýmlayýnýz. Bu matrisi ekrana yazdýrýnýz. 
	//Bu matrisin boyutunu 100x100 olacak þekilde geniþletip 20x20 olan kýsmýna
	//müdahele etmeden geniþleyen yerlerdeki tüm deðerleri bir tamsayý deðiþkeninde saklanabilecek maksimum sayý ile deðiþtiriniz. 

	int HI = 100; // set HI and LO according to your problem.
	int LO = 1;
	int range = HI - LO;
	MatrixXd m = MatrixXd::Random(20, 20); // 3x3 Matrix filled with random numbers between (-1,1)
	m = (m + MatrixXd::Constant(20, 20, 1)) * range / 2; // add 1 to the matrix to have values between 0 and 2; multiply with range/2
	m = (m + MatrixXd::Constant(20, 20, LO)); //set LO as the lower bound (offset)
	cout << "m =\n" << m.cast<int>() << endl;






}