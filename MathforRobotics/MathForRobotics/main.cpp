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

	// SORU - 1: 0 ile 100 arasýnda rastgele sayýlardan oluþan 20x20 M 
	// isimli bir matris tanýmlayýnýz. Bu matrisi ekrana yazdýrýnýz. 
	// Bu matrisin boyutunu 100x100 olacak þekilde geniþletip 20x20 olan kýsmýna
	// müdahele etmeden geniþleyen yerlerdeki tüm deðerleri bir tamsayý deðiþkeninde 
	// saklanabilecek maksimum sayý ile deðiþtiriniz. 

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

			


	//SORU - 2: M matrisinin 20x20 parçasýný sað alt köþeye (20x20) kopyalayýn. 
	//   Sað üst köþeye(20x20) sayýlarýn iki katýný, sol alt köþeye (20x20) 
	//   5 katýný atayarak yerleþtirin. 

	M1.block(80, 80, 20, 20) = M1.block(0, 0, 20, 20);
	M1.block(0, 80, 20, 20) = M1.block(0, 0, 20, 20)*2;
	M1.block(80, 0, 20, 20) = M1.block(0, 0, 20, 20) * 5;
	//cout << endl<<"M_CHANGE: \n" << M1 << endl;


	// SORU - 3: Bu matrisin köþegen elemanlarýnýn toplamýný bulunuz. 
	//cout << "Kosegen Elemanlari Toplami: \n" << M1.trace() << endl;


	//SORU - 4: Bu matrisin her bir satýrýnýn ortalamasý ve en küçük 
    //          deðerleri, her bir sütun için de en büyük deðerleri bulup ekrana yazdýrýn. 

	//cout << endl << "Satirlarin Ortalamasi" << endl;
	//cout << endl << M1.rowwise().mean() << endl;
	//cout << endl << "Sutunlarin Maksimumu" << endl;
	//cout << endl << M1.colwise().maxCoeff()<< endl;



	//SORU - 5: Rastgele deðerlerden oluþan 5x4 ve 4x8 iki matris üretin.
	// Bu matrislerin çarpýmý ile matrislerin elemanlarýnýn karþýlýklý 
	// çarpýmlarýný ayrý ayrý yazdýrýn.

	MatrixXd M5_1= MatrixXd::Random(5, 4);
	MatrixXd M5_2 = MatrixXd::Random(4, 8);

	//cout << endl << M5_1 << endl;
	//cout << endl << M5_2 << endl;
	//cout << endl << "Matrislerin Carpimi" << endl;
	//cout << endl << M5_1*M5_2 << endl;




	//SORU - 6: 10 boyutunda rastgele vektör oluþturun ve 
	//       maksimum deðeri 0 ile deðiþtirin.
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


	// SORU - 7: 100x150 boyutlu bir matrisinin her bir satýrýndaki 
	//    deðerleri satýr numarasý olacak 
	//    þekilde MM deðiþkeninde tanýmlayýnýz.

	MatrixXi M7_diagonal = MatrixXi(VectorXi::LinSpaced(100, 1, 100).asDiagonal());
	MatrixXi M7_ones = MatrixXi::Ones(100, 150);
	MatrixXi MM = M7_diagonal * M7_ones;

	//cout << MM << endl;


	//8. MM matrisinin dört parçaya bölündüðünü düþünün. Sað alt köþe 
	//   (25x25) ile sol üst köþeyi(25x25), sað üst köþe(25x25) ile sol 
	//   alt köþedeki(25x25) deðerlerin yerini deðiþtirin.

	MatrixXi  temp(25,25);

	temp = MM.topRightCorner(25, 25);
	MM.topRightCorner(25, 25) = MM.bottomLeftCorner(25, 25);
	MM.bottomLeftCorner(25, 25) = temp;

	temp = MM.topLeftCorner(25, 25);
	MM.topLeftCorner(25, 25) = MM.bottomRightCorner(25, 25);
	MM.bottomRightCorner(25, 25) = temp;

	//cout <<endl<< MM << endl;

	// 9. 10x10 bir matris içinde 1'den 100'e kadar rakamlarý saklayýn.
	// Bu matrisinin transpozunu yine ayný deðiþken içerisinde saklayýn.
	// Örtüþme olmadýðýndan emin olun.

	MatrixXd M9 = VectorXd::LinSpaced(100, 1, 100);
	M9.transposeInPlace();
	M9.resize(10,10);
	//cout << M9<<endl;

	M9 = M9.transpose().eval();
	//cout << endl << M9 << endl;



	// SORU - 10: opencv kütüphanesini kullanarak size verilen yeni_dunya.pgm dosyasýný okuyup eigen3 matris formatýna dönüþtürün. 

			Mat img_map = imread("yeni_dunya.pgm", IMREAD_GRAYSCALE);
			MatrixXi img_eigen;
			cv2eigen(img_map, img_eigen);
			//cout << img_eigen;

			//imshow("image", img_map);
			//waitKey(0);


	// SORU - 11: img_eigen matrisindeki gri, siyah ve beyaz renklere karþýlýk gelen tam sayý 
			//deðerlerini (örneðin 0,255 vb.) bulup bunlarý yorum satýrý ile koda yazdýðýnýz gibi 
			//ekrana da her bir renk için örnekleri ekrana indis deðerleri ile birlikte yazdýrýnýz. 
			//Örneðin : beyaz renkli deðerlerden birisi 500. satýr 800. sütunda img_eigen[500][800]=XXX  
			//deðeri ile saklanmaktadýr.


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




     // SORU - 12: img_eigen matrisindeki gri alanlardan siyah veya beyaz alanlara hangi indis deðerlerinde 
			//geçtiklerini bulun. Bu deðerler satýr ve sütunlara göre deðiþiklik gösterecektir. Aþaðýdaki resimde 
			//gösterildiði gibi seçilen kýsýmlara yaklaþýk olarak karþýlýk gelecek matris alt-bloðunu farklý bir 
			//matriste saklayýnýz.Bu blok iþleminde kullandýðýnýz rakamlarýn nasýl seçildiðini yorum satýrý ile tartýþýnýz. 
			//Bu matris dosyasýný yine openCV fonksiyonlarý kullanarak yeni_dunya2.pgm dosyasý olarak kaydediniz. 


					
				 /*Tüm resim içerisinde dolaþýlarak gri olmayan tüm hücrelerin satýr indis deðerleri "satir_degerleri" vektöründe,
			     sütun indis deðerleri "sutun_degerleri" vektöründe tutulmuþtur. Her iki vektörün boyutu resim içerisindeki gri olmayan
				 hücrelerin sayýsý kadardýr (int gri_olmayan_sayi). Sonra her iki vektöründe minimum ve maksimum
				 deðerleri dikkate alýnarak "img_eigen" matrisi içerisinden blok alma iþlemi uygulanmýþtýr.*/


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


	// SORU - 13: img_eigen matrisindeki siyah ile gösterilen yerlerin dýþarýya doðru þiþirilmesini saðlayýnýz. 
			//Kabaca bir örnek olarak aþaðýdaki þekli inceleyebilirsiniz. Bu resimdeki siyah renk ile ilgili 
			//gösterilen kýsýmlarýn içeriye doðru deðil sadece dýþarýya doðru siyah renk ile geniþletilmesi gerekmektedir. 
			//Bu þiþirme miktarýný bir parametreye baðlayýp seçilen deðere göre 10,50,100 birim þiþirme iþlemi gerçekleþtiriniz. 

				Mat img_map4 = imread("yeni_dunya.pgm", IMREAD_GRAYSCALE);
				MatrixXi img_eigen4;
				cv2eigen(img_map4, img_eigen4);

				int sisirme_parametresi = 35;/* Sisirme parametresi deðiþtirilerek taþma düzeyi belirlenebilir.
				Bu parametre maksimum 45 deðerini alabilmektedir.Daha yüksek bir deðer
				verilirse resmin dýþýna çýkýlacaðýndan hata vermektedir.*/


				//soldan saga tarama(Saða ve üste taþma yapýldý).
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

				//saðdan - sola tarama(sola ve alta taþma yapýldý).

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