using System;
using System.IO;

namespace Hiányzások
{
    class Program
    {
        //Beolvasott adatok tárolása
        struct Egyhiányzás
        {
            public int hónap;
            public int nap;
            public string név;
            public string jelen;
        }

        static Egyhiányzás[] hiányzás = new Egyhiányzás[500];
        static int n = 0;

        //Tanulónkénti hiányzások
        struct Egystat
        {
            public string név;
            public int mulasztás;
        }
        static Egystat[] stat = new Egystat[50];
        static int m = 0;

        static void Main(string[] args)
        {
            Feladat1();
            Feladat2();
            Feladat3();
            Feladat5();
            Feladat6();
            Feladat7();

            Console.ReadKey();
        }


        static void Feladat7()
        {
            //Hiányzások tanulónként
            for (int i = 0; i < n; i++)
            {
                int j = 0;
                while (j < m && hiányzás[i].név != stat[j].név) j++;
                if (j == m)
                {
                    stat[m].név = hiányzás[i].név;
                    m++;
                }
                for (int k = 0; k < hiányzás[i].jelen.Length; k++)
                    if (hiányzás[i].jelen[k] != 'O') stat[j].mulasztás++;
            }

            //Legtöbb hiányzás
            int max = stat[0].mulasztás;
            for (int i = 0; i < m; i++)
                if (stat[i].mulasztás > max) 
                    max = stat[i].mulasztás;
            Console.Write("7. feladat\nA legtöbbet hiányzó tanulók:");
            for (int i = 0; i < m; i++)
                if (stat[i].mulasztás == max)
                    Console.Write(" " + stat[i].név);
        }

        static void Feladat6()
        {
            Console.WriteLine("6. feladat");
            Console.Write("A nap neve=");
            string napnév = Console.ReadLine();
            Console.Write("Az óra sorszáma=");
            int óraszám = Convert.ToInt32(Console.ReadLine())-1;
            int db=0;

            for (int i = 0; i < n; i++)
                if (napnév == hetnapja(hiányzás[i].hónap, hiányzás[i].nap) && 
                        (hiányzás[i].jelen[óraszám] == 'X' || hiányzás[i].jelen[óraszám] == 'I' ))
                    db++;
            Console.WriteLine("Ekkor összesen {0} óra hiányzás történt.", db);
        }

        static void Feladat5()
        {
            Console.WriteLine("5. feladat");
            Console.Write("A hónap sorszáma=");
            int x = Convert.ToInt32(Console.ReadLine());
            Console.Write("A nap sorszáma="); 
            int y = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Azon a napon " + hetnapja(x, y) + " volt.");
        }

        static string hetnapja(int hónap, int nap)
        {
            string[] napnév = new string[] {"vasárnap", "hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat"};
            int[] napszám = new int[] {0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335};
            int napsorszám = (napszám[hónap - 1] + nap) % 7;
            return napnév[napsorszám];
        }

        static void Feladat3()
        {
            int ig = 0;
            int il = 0;
            for (int i = 0; i < n; i++)
                for (int j = 0; j < hiányzás[i].jelen.Length; j++)
                {
                    if (hiányzás[i].jelen[j] == 'X') ig++;
                    if (hiányzás[i].jelen[j] == 'I') il++;
                }
            Console.WriteLine("3. feladat");
            Console.WriteLine("Az igazolt hiányzások száma {0}, az igazolatlanoké {1} óra.", ig, il);
        }

        static void Feladat2()
        {
            Console.WriteLine("2. feladat\nA naplóban {0} bejegyzés van.", n);
        }

        static void Feladat1()
        {
            StreamReader sr = new StreamReader("naplo.txt");
            string[] sor1 = new string[3];
            string[] sor2 = new string[3];
            while (sr.Peek() != -1)
            {
                sor1 = sr.ReadLine().Split(' ');
                while (sr.Peek() != -1 && sr.Peek() != '#')
                {
                    sor2 = sr.ReadLine().Split(' ');
                    hiányzás[n].hónap = Convert.ToInt32(sor1[1]);
                    hiányzás[n].nap = Convert.ToInt32(sor1[2]);
                    hiányzás[n].név = sor2[0] + " " + sor2[1];
                    hiányzás[n].jelen = sor2[2];
                    n++;
                }
            }
            sr.Close();
        }
    }
}
