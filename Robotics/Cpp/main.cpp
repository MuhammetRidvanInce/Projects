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

	// SORU - 1: 0 ile 100 arasýnda rastgele sayýlardan oluþan 20x20 M isimli bir matris tanýmlayýnýz. Bu matrisi ekrana yazdýrýnýz. 
	//Bu matrisin boyutunu 100x100 olacak þekilde geniþletip 20x20 olan kýsmýna
	//müdahele etmeden geniþleyen yerlerdeki tüm deðerleri bir tamsayý deðiþkeninde saklanabilecek maksimum sayý ile deðiþtiriniz. 



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
				M1(i, j) = 5;  // Þekil olarak görülebilmesi için INT_MAX yerine 5 deðeri atanmýþtýr.
		}
	}

	cout << "\n\n\nSekil olarak gorulebilmesi icin INT_MAX degeri yerine 5 degeri atanmistir\n\n";
	cout << endl << "Cevap icin alt satirdaki yorum satirini calistiriniz.\n" << endl;
	//cout << "M_EXPAND: \n" << M1 << endl;
	

	//2. M matrisinin 20x20 parçasýný sað alt köþeye (20x20) kopyalayýn. Sað üst köþeye(20x20) sayýlarýn iki katýný, sol alt köþeye (20x20) 5 katýný atayarak yerleþtirin. 


	M1.block(80, 80, 20, 20) = M1.block(0, 0, 20, 20);
	M1.block(0, 80, 20, 20) = M1.block(0, 0, 20, 20)*2;
	M1.block(80, 0, 20, 20) = M1.block(0, 0, 20, 20) * 5;
	cout << "SORU 2-------------------------------\n" << endl;
	cout << endl << "Cevap icin alt satirdaki yorum satirini calistiriniz.\n" << endl;
	//cout << "M_CHANGE: \n" << M1 << endl;


	// 3. Bu matrisin köþegen elemanlarýnýn toplamýný bulunuz. 


	cout << endl<< "SORU 3-------------------------------\n" << endl;
	cout << "M_Trace: \n" << M1.trace() << endl;

	//4. Bu matrisin her bir satýrýnýn ortalamasý ve en küçük deðerleri, her bir sütun için de en büyük deðerleri bulup ekrana yazdýrýn. 

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


	//SORU - 5: Rastgele deðerlerden oluþan 5x4 ve 4x8 iki matris üretin.Bu matrislerin çarpýmý ile 
	//matrislerin elemanlarýnýn karþýlýklý çarpýmlarýný ayrý ayrý yazdýrýn.

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

	//Soru 6: 10 boyutunda rastgele vektör oluþturun ve maksimum deðeri 0 ile deðiþtirin.



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


	// 7. 100x150 boyutlu bir matrisinin her bir satýrýndaki deðerleri satýr numarasý olacak þekilde MM deðiþkeninde tanýmlayýnýz.

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

	//8. MM matrisinin dört parçaya bölündüðünü düþünün. Sað alt köþe (25x25) ile sol üst köþeyi(25x25), 
	// sað üst köþe(25x25) ile sol alt köþedeki(25x25) deðerlerin yerini deðiþtirin.

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

	// 9. 10x10 bir matris içinde 1'den 100'e kadar rakamlarý saklayýn.Bu matrisinin 
	// transpozunu yine ayný deðiþken içerisinde saklayýn.Örtüþme olmadýðýndan emin olun.

	MatrixXd M10(1, 100);

	for (int i = 0; i < 100; i++)
	{
		M10(i) = i+1;

	}

	M10.resize(10, 10);

	cout << endl << "SORU 9-------------------------------\n" << endl;
	cout << "M10 :\n " << M10 << endl;
	cout << "M10_Transpoze :\n " << M10.transpose() << endl;


	// 10. opencv kütüphanesini kullanarak size verilen yeni_dunya.pgm dosyasýný okuyup eigen3 matris formatýna dönüþtürün. 

	Mat img_map = imread("yeni_dunya.pgm");
	nameWindow("image", WINDOW_NORMAL);
	imshow("image", img);
	waitKey(0);



	return 0;
	
}