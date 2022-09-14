#include <iostream>
#include <fstream>
int szamjegyszam(int szam)
{
	int db=0;
	while(szam>0)
	{
		szam=szam/10;
		db++;
	}
	return db;
}
using namespace std;
struct Ttelek{
	int hossz;
	string szin;
};
struct Toldal{
	int db;
	Ttelek kerites[125];
};
int main()
{
	Toldal o[2];
	o[0].db=0; // paros oldal
	o[1].db=0; // paratlan oldal
	// 1. feladat
	ifstream be("kerites.txt");
	string szin;
	int oldal, hossz;
	while(be >> oldal >> hossz >> szin)
	{
		Ttelek telek;
		telek.hossz=hossz;
		telek.szin=szin;
		o[oldal].kerites[o[oldal].db]=telek;
		o[oldal].db++;
	}
	be.close();

	cout << "2. feladat" << endl;
	cout << "Az eladott telkek szama: " << o[0].db+o[1].db << endl;

	cout << "3. feladat" << endl;
	if(oldal==0)
	{
		cout << "A paros oldalon adtak el az utolso telket." << endl;
		cout << "Az utolso telek hazszama: " << o[0].db*2 << endl;
	}
	else
	{
		cout << "A paratlan oldalon adtak el az utolso telket." << endl;
		cout << "Az utolso telek hazszama: " << o[1].db*2-1 << endl;
	}

	cout << "4. feladat" << endl;
	cout << "A szomszedossal egyezik a kerites szine: ";
	for(int i=0; i<o[1].db-1; i++)
	{
		if( (o[1].kerites[i].szin==o[1].kerites[i+1].szin)
			and o[1].kerites[i].szin!="#" and o[1].kerites[i].szin!=":")
		{
			cout << 2*i+1 << " " << 2*i+3 << " ";
		}
	}
	cout << endl;

	cout << "5. feladat" << endl;
	cout << "Adjon meg egy hazszamot! ";
	int hazszam;
	cin >> hazszam;
	int melyikoldal=hazszam%2;
	cout << "A kerites szine / allapota: " << o[melyikoldal].kerites[(hazszam-1)/2].szin << endl;
	string szinek=o[melyikoldal].kerites[(hazszam-1)/2].szin;
	if(hazszam>2) { szinek=szinek+o[melyikoldal].kerites[(hazszam-2-1)/2].szin; }
	if( (hazszam+2-1)/2<o[melyikoldal].db) { szinek=szinek+o[melyikoldal].kerites[(hazszam+2-1)/2].szin; }

	string lehetsegesszin="ABCD";
	int melyikszin=0;
	while(szinek.find(lehetsegesszin[melyikszin])!=string::npos)
	{
		melyikszin++;
	}
	cout << "Egy lehetseges festesi szin: " << lehetsegesszin[melyikszin] << endl;

	// 6. feladat
	ofstream ki("utcakep.txt");

	for(int i=0; i<o[1].db; i++)
	{
		for(int j=0; j<o[1].kerites[i].hossz; j++)
		{
			ki << o[1].kerites[i].szin;
		}
	}
	ki << endl;

	for(int i=0; i<o[1].db; i++)
	{
		ki << 2*i+1;
		for(int j=szamjegyszam(2*i+1); j<o[1].kerites[i].hossz; j++)
		{
			ki << " ";
		}
	}
	ki << endl;

	ki.close();

    return 0;
}
