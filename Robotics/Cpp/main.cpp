#include <iostream>
#include <Eigen/Dense>
#include <cstdlib> 
#include <ctime> 
#include <opencv2/opencv.hpp>
#include <opencv2/core/eigen.hpp>



using namespace Eigen;
using namespace std;

int main()
{

	// SORU - 1: 0 ile 100 aras�nda rastgele say�lardan olu�an 20x20 M isimli bir matris tan�mlay�n�z. Bu matrisi ekrana yazd�r�n�z. 
	//Bu matrisin boyutunu 100x100 olacak �ekilde geni�letip 20x20 olan k�sm�na
	//m�dahele etmeden geni�leyen yerlerdeki t�m de�erleri bir tamsay� de�i�keninde saklanabilecek maksimum say� ile de�i�tiriniz. 



	Eigen::MatrixXd M1(20, 20);
	srand((unsigned)time(0));
	int number = 0;

	for (int i = 0; i < 20; i++)
	{
		for (int j = 0; j < 20; j++)
		{
			number = (rand() % 100) + 1;
			M1(i, j) = number;
		}
	}

	cout << "SORU 1-------------------------------\n" << endl;
	cout << "M: \n" << M1 << endl;

	Eigen::MatrixXd temp1(20, 20);
	temp1 = M1.block(0, 0, 20, 20);
	M1.resize(100,100);
	M1.block(0, 0, 20, 20) = temp1;

	for (int i = 0; i <100 ; i++)
	{
		for (int j = 0; j < 100; j++)
		{
			if(i <= 20 && j >=20  || i >= 20 && j<=20 || i>=20 && j>=20)
				M1(i, j) = 5;  // �ekil olarak g�r�lebilmesi i�in INT_MAX yerine 5 de�eri atanm��t�r.
		}
	}

	cout << "\n\n\nSekil olarak gorulebilmesi icin INT_MAX degeri yerine 5 degeri atanmistir\n\n";
	cout << endl << "Cevap icin alt satirdaki yorum satirini calistiriniz.\n" << endl;
	//cout << "M_EXPAND: \n" << M1 << endl;
	

	//2. M matrisinin 20x20 par�as�n� sa� alt k��eye (20x20) kopyalay�n. Sa� �st k��eye(20x20) say�lar�n iki kat�n�, sol alt k��eye (20x20) 5 kat�n� atayarak yerle�tirin. 


	M1.block(80, 80, 20, 20) = M1.block(0, 0, 20, 20);
	M1.block(0, 80, 20, 20) = M1.block(0, 0, 20, 20)*2;
	M1.block(80, 0, 20, 20) = M1.block(0, 0, 20, 20) * 5;
	cout << "SORU 2-------------------------------\n" << endl;
	cout << endl << "Cevap icin alt satirdaki yorum satirini calistiriniz.\n" << endl;
	//cout << "M_CHANGE: \n" << M1 << endl;


	// 3. Bu matrisin k��egen elemanlar�n�n toplam�n� bulunuz. 


	cout << endl<< "SORU 3-------------------------------\n" << endl;
	cout << "M_Trace: \n" << M1.trace() << endl;

	//4. Bu matrisin her bir sat�r�n�n ortalamas� ve en k���k de�erleri, her bir s�tun i�in de en b�y�k de�erleri bulup ekrana yazd�r�n. 

	Matrix < float, 1, 100 > row_mean_vector;
	Matrix < float, 1, 100 > min_value_vector;
	Matrix < float, 1, 100 > max_value_vector;

	float row_sum = 0;
	float min_value;
	float max_value;

	for (int i = 0; i < 100; i++)
	{
		min_value = M1(i,0);
		for (int j = 0; j < 100; j++)
		{
			row_sum += M1(j, i);
			if (M1(i,j) < min_value)
				min_value = M1(i,j);
		}
			
		row_mean_vector(i) = row_sum / 100;
		min_value_vector(i) = min_value;
	}

	for (int i = 0; i < 100; i++)
	{
		max_value = M1(0, i);
		for (int j = 0; j < 100; j++)
		{
			if (M1(j,i) > max_value)
				max_value = M1(j,i);
		}
		max_value_vector(i) = max_value;
	}


	cout << endl << "SORU 4-------------------------------\n" << endl;
	cout << "Satir Ortalamalari: \n" << row_mean_vector << endl;
	cout << "\n\nEn Kucuk Degerler (Satir): \n" << min_value_vector << endl;
	cout << "\n\nEn Buyuk Degerler (Sutun) : \n" << max_value_vector << endl;


	//SORU - 5: Rastgele de�erlerden olu�an 5x4 ve 4x8 iki matris �retin.Bu matrislerin �arp�m� ile 
	//matrislerin elemanlar�n�n kar��l�kl� �arp�mlar�n� ayr� ayr� yazd�r�n.

	Matrix < float , 5, 4 > M5_1;

	for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			number = (rand() % 100) + 1;
			M5_1(i, j) = number;
		}
	}


	Matrix < float, 4, 8 > M5_2;

	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 8; j++)
		{
			number = (rand() % 100) + 1;
			M5_2(i, j) = number;
		}
	}

	Matrix < float, 5, 8 > result5;
	result5 = M5_1 * M5_2;

	cout << endl<< "SORU 5-------------------------------\n" << endl;
	cout << "Matris1\n" << M5_1 << endl;
	cout << "Matris2\n" << M5_2 << endl;
	cout << "Carpim\n" << result5 << endl;
	cout << "Karsilikli Carpim\n" << M5_1.block(0,0,4,4) * M5_2.block(0, 0, 4, 4) << endl;

	//Soru 6: 10 boyutunda rastgele vekt�r olu�turun ve maksimum de�eri 0 ile de�i�tirin.



	Matrix < float, 1, 10 > M6;
	for (int i = 0; i < 10; i++)
	{
		number = (rand() % 100) + 1;
		M6(i) = number;

	}
	cout << endl << "SORU 6-------------------------------\n" << endl;
	cout << "M6: " << M6 << endl;

	int indis = 0;
	int enbuyuk = M6(0);

	for (int i = 1; i < 10; i++)
	{
		if (M6(i) > enbuyuk)
		{
			enbuyuk = M6(i);
			indis = i;
		}
	}

	M6(indis) = 0;
	cout << "M6 Yeni: " << M6 << endl;


	// 7. 100x150 boyutlu bir matrisinin her bir sat�r�ndaki de�erleri sat�r numaras� olacak �ekilde MM de�i�keninde tan�mlay�n�z.

	Matrix < float, 100, 150 > MM;
	MM.setOnes();
	for (int i = 0; i < 100; i++)
	{
		for (int j = 0; j < 150; j++)
			MM(i, j) = MM(i, j) * (i+1);

	}

	cout << endl << "SORU 7-------------------------------\n" << endl;
	cout << endl << "Cevap icin alt satirdaki yorum satirini calistiriniz.\n" << endl;
	//cout << "MM:\n" << MM << endl;

	//8. MM matrisinin d�rt par�aya b�l�nd���n� d���n�n. Sa� alt k��e (25x25) ile sol �st k��eyi(25x25), 
	// sa� �st k��e(25x25) ile sol alt k��edeki(25x25) de�erlerin yerini de�i�tirin.

	Matrix < float, 25, 25 > temp;

	temp = MM.block(0, 0, 25, 25);
	MM.block(0, 0, 25, 25) = MM.block(74, 124, 25, 25);
	MM.block(74, 124, 25, 25) = temp;

	temp = MM.block(0, 74, 25, 25);
	MM.block(0, 74, 25, 25) = MM.block(74, 0, 25, 25);
	MM.block(74, 0, 25, 25) = temp;


	cout << endl << "SORU 8-------------------------------\n" << endl;
	cout << endl << "Cevap icin alt satirdaki yorum satirini calistiriniz.\n" << endl;
	//cout << "MM Yeni:\n" << MM << endl;

	// 9. 10x10 bir matris i�inde 1'den 100'e kadar rakamlar� saklay�n.Bu matrisinin 
	// transpozunu yine ayn� de�i�ken i�erisinde saklay�n.�rt��me olmad���ndan emin olun.

	MatrixXd M10(1, 100);

	for (int i = 0; i < 100; i++)
	{
		M10(i) = i+1;

	}

	M10.resize(10, 10);

	cout << endl << "SORU 9-------------------------------\n" << endl;
	cout << "M10 :\n " << M10 << endl;
	cout << "M10_Transpoze :\n " << M10.transpose() << endl;


	// 10. opencv k�t�phanesini kullanarak size verilen yeni_dunya.pgm dosyas�n� okuyup eigen3 matris format�na d�n��t�r�n. 

	Mat img_map = imread("yeni_dunya.pgm");
	nameWindow("image", WINDOW_NORMAL);
	imshow("image", img);
	waitKey(0);



	return 0;
	
}