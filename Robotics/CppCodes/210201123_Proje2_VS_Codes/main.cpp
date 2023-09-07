#include <iostream>
#include <Eigen/Dense>
#include <cstdlib> 
#include <ctime> 
#include <opencv2/opencv.hpp>
#include <opencv2/core/eigen.hpp>




using namespace Eigen;
using namespace std;
using namespace cv;

int main()
{

	// SORU - 1: 0 ile 100 aras�nda rastgele say�lardan olu�an 20x20 M 
	// isimli bir matris tan�mlay�n�z. Bu matrisi ekrana yazd�r�n�z. 
	// Bu matrisin boyutunu 100x100 olacak �ekilde geni�letip 20x20 olan k�sm�na
	// m�dahele etmeden geni�leyen yerlerdeki t�m de�erleri bir tamsay� de�i�keninde 
	// saklanabilecek maksimum say� ile de�i�tiriniz. 

	MatrixXd M = (MatrixXd::Random(20, 20) + MatrixXd::Ones(20, 20)) * 50;
	MatrixXi M1 = M.cast<int>();
	//cout << M1 << endl;

	MatrixXi temp1(20, 20);
	temp1 = M1.block(0, 0, 20, 20);
	M1.resize(100,100);
	M1.block(0, 0, 20, 20) = temp1;
	M1.block(0, 20, 100,80) = MatrixXi::Constant(100, 80, 1);;
	M1.block(20, 0, 80, 20) = MatrixXi::Constant(80, 20, 1);;
	//cout << endl<< M1 << endl;

			


	//SORU - 2: M matrisinin 20x20 par�as�n� sa� alt k��eye (20x20) kopyalay�n. 
	//   Sa� �st k��eye(20x20) say�lar�n iki kat�n�, sol alt k��eye (20x20) 
	//   5 kat�n� atayarak yerle�tirin. 

	M1.block(80, 80, 20, 20) = M1.block(0, 0, 20, 20);
	M1.block(0, 80, 20, 20) = M1.block(0, 0, 20, 20)*2;
	M1.block(80, 0, 20, 20) = M1.block(0, 0, 20, 20) * 5;
	//cout << endl<<"M_CHANGE: \n" << M1 << endl;


	// SORU - 3: Bu matrisin k��egen elemanlar�n�n toplam�n� bulunuz. 
	//cout << "Kosegen Elemanlari Toplami: \n" << M1.trace() << endl;


	//SORU - 4: Bu matrisin her bir sat�r�n�n ortalamas� ve en k���k 
    //          de�erleri, her bir s�tun i�in de en b�y�k de�erleri bulup ekrana yazd�r�n. 

	//cout << endl << "Satirlarin Ortalamasi" << endl;
	//cout << endl << M1.rowwise().mean() << endl;
	//cout << endl << "Sutunlarin Maksimumu" << endl;
	//cout << endl << M1.colwise().maxCoeff()<< endl;



	//SORU - 5: Rastgele de�erlerden olu�an 5x4 ve 4x8 iki matris �retin.
	// Bu matrislerin �arp�m� ile matrislerin elemanlar�n�n kar��l�kl� 
	// �arp�mlar�n� ayr� ayr� yazd�r�n.

	MatrixXd M5_1= MatrixXd::Random(5, 4);
	MatrixXd M5_2 = MatrixXd::Random(4, 8);

	//cout << endl << M5_1 << endl;
	//cout << endl << M5_2 << endl;
	//cout << endl << "Matrislerin Carpimi" << endl;
	//cout << endl << M5_1*M5_2 << endl;




	//SORU - 6: 10 boyutunda rastgele vekt�r olu�turun ve 
	//       maksimum de�eri 0 ile de�i�tirin.
	VectorXi M6 = VectorXi::Random(10);

	//cout << "Vektor M6: " << M6.transpose() << endl;
	//cout << endl << "En Buyuk Deger: " << M6.colwise().maxCoeff() << endl;

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
	//cout <<endl<< "Vector M6 Yeni: " << M6.transpose() << endl;


	// SORU - 7: 100x150 boyutlu bir matrisinin her bir sat�r�ndaki 
	//    de�erleri sat�r numaras� olacak 
	//    �ekilde MM de�i�keninde tan�mlay�n�z.

	MatrixXi M7_diagonal = MatrixXi(VectorXi::LinSpaced(100, 1, 100).asDiagonal());
	MatrixXi M7_ones = MatrixXi::Ones(100, 150);
	MatrixXi MM = M7_diagonal * M7_ones;

	//cout << MM << endl;


	//8. MM matrisinin d�rt par�aya b�l�nd���n� d���n�n. Sa� alt k��e 
	//   (25x25) ile sol �st k��eyi(25x25), sa� �st k��e(25x25) ile sol 
	//   alt k��edeki(25x25) de�erlerin yerini de�i�tirin.

	MatrixXi  temp(25,25);

	temp = MM.topRightCorner(25, 25);
	MM.topRightCorner(25, 25) = MM.bottomLeftCorner(25, 25);
	MM.bottomLeftCorner(25, 25) = temp;

	temp = MM.topLeftCorner(25, 25);
	MM.topLeftCorner(25, 25) = MM.bottomRightCorner(25, 25);
	MM.bottomRightCorner(25, 25) = temp;

	//cout <<endl<< MM << endl;

	// 9. 10x10 bir matris i�inde 1'den 100'e kadar rakamlar� saklay�n.
	// Bu matrisinin transpozunu yine ayn� de�i�ken i�erisinde saklay�n.
	// �rt��me olmad���ndan emin olun.

	MatrixXd M9 = VectorXd::LinSpaced(100, 1, 100);
	M9.transposeInPlace();
	M9.resize(10,10);
	//cout << M9<<endl;

	M9 = M9.transpose().eval();
	//cout << endl << M9 << endl;



	// SORU - 10: opencv k�t�phanesini kullanarak size verilen yeni_dunya.pgm dosyas�n� okuyup eigen3 matris format�na d�n��t�r�n. 

			Mat img_map = imread("yeni_dunya.pgm", IMREAD_GRAYSCALE);
			MatrixXi img_eigen;
			cv2eigen(img_map, img_eigen);
			//cout << img_eigen;

			//imshow("image", img_map);
			//waitKey(0);


	// SORU - 11: img_eigen matrisindeki gri, siyah ve beyaz renklere kar��l�k gelen tam say� 
			//de�erlerini (�rne�in 0,255 vb.) bulup bunlar� yorum sat�r� ile koda yazd���n�z gibi 
			//ekrana da her bir renk i�in �rnekleri ekrana indis de�erleri ile birlikte yazd�r�n�z. 
			//�rne�in : beyaz renkli de�erlerden birisi 500. sat�r 800. s�tunda img_eigen[500][800]=XXX  
			//de�eri ile saklanmaktad�r.


				Mat img_map2 = imread("yeni_dunya.pgm", IMREAD_GRAYSCALE);
				MatrixXi img_eigen2;
				cv2eigen(img_map2, img_eigen2);

				for (int i = 0; i < img_eigen2.rows(); i++)
				{

					for (int j = 0; j < img_eigen2.cols(); j++)
					{
						/*printf("[%d][%d]: %d\n", i, j, img_eigen2(i, j));*/
					}

					if (i == 2)
						break;

				}




     // SORU - 12: img_eigen matrisindeki gri alanlardan siyah veya beyaz alanlara hangi indis de�erlerinde 
			//ge�tiklerini bulun. Bu de�erler sat�r ve s�tunlara g�re de�i�iklik g�sterecektir. A�a��daki resimde 
			//g�sterildi�i gibi se�ilen k�s�mlara yakla��k olarak kar��l�k gelecek matris alt-blo�unu farkl� bir 
			//matriste saklay�n�z.Bu blok i�leminde kulland���n�z rakamlar�n nas�l se�ildi�ini yorum sat�r� ile tart���n�z. 
			//Bu matris dosyas�n� yine openCV fonksiyonlar� kullanarak yeni_dunya2.pgm dosyas� olarak kaydediniz. 


					
				 /*T�m resim i�erisinde dola��larak gri olmayan t�m h�crelerin sat�r indis de�erleri "satir_degerleri" vekt�r�nde,
			     s�tun indis de�erleri "sutun_degerleri" vekt�r�nde tutulmu�tur. Her iki vekt�r�n boyutu resim i�erisindeki gri olmayan
				 h�crelerin say�s� kadard�r (int gri_olmayan_sayi). Sonra her iki vekt�r�nde minimum ve maksimum
				 de�erleri dikkate al�narak "img_eigen" matrisi i�erisinden blok alma i�lemi uygulanm��t�r.*/


				Mat img_map3 = imread("yeni_dunya.pgm", IMREAD_GRAYSCALE);
				MatrixXi img_eigen3;
				cv2eigen(img_map3, img_eigen3);

				int gri_olmayan_sayi = 0;

				for (int i = 0; i < img_eigen3.rows(); i++)
				{
					for (int j = 0; j < img_eigen3.cols(); j++)
					{
						
						if (img_eigen3(i, j) != 205)
							gri_olmayan_sayi++;


					}

				}

				VectorXi satir_degerleri = VectorXi::Ones(gri_olmayan_sayi) ;
				VectorXi sutun_degerleri = VectorXi::Ones(gri_olmayan_sayi);
				int row_index = 0;
				int col_index = 0;


				for (int i = 0; i < img_eigen3.rows(); i++)
				{
					for (int j = 0; j < img_eigen3.cols(); j++)
					{

						if (img_eigen3(i, j) != 205)
						{
							satir_degerleri(row_index) = i;
							sutun_degerleri(col_index) = j;
							row_index++;
							col_index++;
						}
					}
				}

				int min_row = satir_degerleri.minCoeff();
				int max_row = satir_degerleri.maxCoeff();
				int min_col = sutun_degerleri.minCoeff();
				int max_col = sutun_degerleri.maxCoeff();


				MatrixXi alt_blok;
				alt_blok = img_eigen3.block(min_row, min_col, max_row - min_row, max_col - min_col);
				//cout << alt_blok << endl;
				Mat img_alt_blok;
				eigen2cv(alt_blok, img_alt_blok); 

				//imwrite("alt_blok.jpg", img_alt_blok);
				//Mat img_map3_yeni = imread("alt_blok.jpg", IMREAD_GRAYSCALE);
				//imshow("image", img_map3_yeni);
				//waitKey(0);


	// SORU - 13: img_eigen matrisindeki siyah ile g�sterilen yerlerin d��ar�ya do�ru �i�irilmesini sa�lay�n�z. 
			//Kabaca bir �rnek olarak a�a��daki �ekli inceleyebilirsiniz. Bu resimdeki siyah renk ile ilgili 
			//g�sterilen k�s�mlar�n i�eriye do�ru de�il sadece d��ar�ya do�ru siyah renk ile geni�letilmesi gerekmektedir. 
			//Bu �i�irme miktar�n� bir parametreye ba�lay�p se�ilen de�ere g�re 10,50,100 birim �i�irme i�lemi ger�ekle�tiriniz. 

				Mat img_map4 = imread("yeni_dunya.pgm", IMREAD_GRAYSCALE);
				MatrixXi img_eigen4;
				cv2eigen(img_map4, img_eigen4);

				int sisirme_parametresi = 35;/* Sisirme parametresi de�i�tirilerek ta�ma d�zeyi belirlenebilir.
				Bu parametre maksimum 45 de�erini alabilmektedir.Daha y�ksek bir de�er
				verilirse resmin d���na ��k�laca��ndan hata vermektedir.*/


				//soldan saga tarama(Sa�a ve �ste ta�ma yap�ld�).
				int sol, ust;

				for (int i = 0; i < img_eigen4.rows(); i++)
				{
					for (int j = 0; j < img_eigen4.cols(); j++)
					{

						if (img_eigen4(i, j) == 0)
						{
							sol = img_eigen4(i, j - 1);
							ust = img_eigen4(i-1, j);

							if (ust == 205)
							{
								for (int x = 1; x <= sisirme_parametresi; x++)
									img_eigen4(i - x, j) = 0;
							}
							else if (sol == 205)
							{
								for (int x = 1; x <= sisirme_parametresi; x++)
									img_eigen4(i, j - x) = 0;

							}
						}
					}
				}

				//sa�dan - sola tarama(sola ve alta ta�ma yap�ld�).

				int sag, alt;
				for (int i = img_eigen4.rows()-1; i >= 0; i--)
				{
					for (int j = img_eigen4.cols()-1; j >= 0; j--)
					{

						if (img_eigen4(i, j) == 0)
						{
							sag = img_eigen4(i, j + 1);
							alt = img_eigen4(i + 1, j);

							if (alt == 205)
							{
								for (int x = 1; x <= sisirme_parametresi; x++)
									img_eigen4(i + x, j) = 0;
							}
							else if (sag == 205)
							{
								for (int x = 1; x <= sisirme_parametresi; x++)
									img_eigen4(i, j + x) = 0;

							}
						}
					}
				}

				//Mat img_sisirilmis;
				//eigen2cv(img_eigen4, img_sisirilmis); 

				//imwrite("img_sisirilmis.jpg", img_sisirilmis);
				//Mat img_map4_yeni = imread("img_sisirilmis.jpg", IMREAD_GRAYSCALE);
				//imshow("image", img_map4_yeni);
				//waitKey(0);















	return 0;
	
}