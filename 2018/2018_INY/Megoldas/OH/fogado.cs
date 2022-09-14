using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace fogado
{
    class Program
    {
        static int sordb;
        struct foglalstruktura
        {
            public string nev;
            public string idopont;
            public string foglaslasido;
        }

        static foglalstruktura[] foglalasok = new foglalstruktura[500];


        static void Main(string[] args)
        {
            Feladat1_2();
            Console.WriteLine();
            Feladat3();
            Console.WriteLine();
            Feladat4();
            Console.WriteLine();
            Feladat5();
            Console.WriteLine();
            Feladat6();
            Console.WriteLine();


            Console.ReadLine();
        }

        static void Feladat1_2()
        {
            string egysor;
            string[] sordarabolt;


            StreamReader olvaso = new StreamReader(@"..\..\fogado.txt");

            sordb = 0;
            while (!olvaso.EndOfStream)
            {
                sordb++;
                egysor = olvaso.ReadLine();
                sordarabolt = egysor.Split(' ');
                foglalasok[sordb].nev = sordarabolt[0] + " " + sordarabolt[1];
                foglalasok[sordb].idopont = sordarabolt[2];
                foglalasok[sordb].foglaslasido = sordarabolt[3];
            }

            olvaso.Close();

            Console.WriteLine("2. feladat");
            Console.WriteLine("Foglalások száma: {0}", sordb);
        }

        static void Feladat3()
        {
            int db;
            string nev;

            Console.WriteLine("3. feladat");
            Console.Write("Adjon meg egy nevet: ");
            nev = Console.ReadLine();

            db = 0;
            for (int cv = 1; cv <= sordb; cv++)
            {
                if (foglalasok[cv].nev == nev)
                    db++;
            }

            if (db > 0)
                Console.WriteLine("{0} néven {1} időpontfoglalás van.", nev, db);
            else
                Console.WriteLine("A megadott néven nincs időpontfoglalás.");


        }

        static void Feladat4()
        {
            string idopont, idopontr, fileneve, csere;
            string[] nevsor = new string[501];
            int nevdb, hasonlit;

            Console.WriteLine("4. feladat");

            Console.Write("Adjon meg egy érvényes időpontot (pl. 17:10): ");
            idopont = Console.ReadLine();

            idopontr = idopont.Replace(":", "");

            fileneve = @"..\..\" + idopontr + ".txt";
            StreamWriter iro = new StreamWriter(fileneve);

            nevdb = 0;
            for (int cv = 1; cv <= sordb; cv++)
            {
                if (foglalasok[cv].idopont == idopont)
                {
                    nevdb++;
                    nevsor[nevdb] = foglalasok[cv].nev;
                }
            }

            for (int i = nevdb; i >= 2; i--)
                for (int j = 1; j <= i - 1; j++)
                {
                    hasonlit = nevsor[i].CompareTo(nevsor[j]);
                    if (hasonlit < 0)
                    {
                        csere = nevsor[i];
                        nevsor[i] = nevsor[j];
                        nevsor[j] = csere;

                    }
                }

            for (int cv = 1; cv <= nevdb; cv++)
            {
                Console.WriteLine(nevsor[cv]);
                iro.WriteLine(nevsor[cv]);
            }
            iro.Close();
        }

        static void Feladat5()
        {
            int hasonlit;
            foglalstruktura mini;

            mini = foglalasok[1];
            for (int cv = 1; cv <= sordb; cv++)
            {
                hasonlit = foglalasok[cv].foglaslasido.CompareTo(mini.foglaslasido);
                if (hasonlit < 0)
                    mini = foglalasok[cv];

            }
            Console.WriteLine("5. feladat");
            Console.WriteLine("Tanár neve: " + mini.nev);
            Console.WriteLine("Foglalt időpont: " + mini.idopont);
            Console.WriteLine("Foglalás ideje: " + mini.foglaslasido);
        }
        static void Feladat6()
        {
            int cvvissza;
            string[,] szabadido = new string[2, 13];
            szabadido[0, 0] = "16:00";
            szabadido[0, 1] = "16:10";
            szabadido[0, 2] = "16:20";
            szabadido[0, 3] = "16:30";
            szabadido[0, 4] = "16:40";
            szabadido[0, 5] = "16:50";
            szabadido[0, 6] = "17:00";
            szabadido[0, 7] = "17:10";
            szabadido[0, 8] = "17:20";
            szabadido[0, 9] = "17:30";
            szabadido[0, 10] = "17:40";
            szabadido[0, 11] = "17:50";
            szabadido[0, 12] = "18:00";

            for (int cvido = 0; cvido <= 11; cvido++)
                for (int cvsor = 1; cvsor <= sordb; cvsor++)
                    if (foglalasok[cvsor].nev == "Barna Eszter" && foglalasok[cvsor].idopont == szabadido[0, cvido])
                        szabadido[1, cvido] = "foglalt";

            Console.WriteLine("6. feladat");
            for (int cv = 0; cv <= 11; cv++)
                if (szabadido[1, cv] != "foglalt")
                    Console.WriteLine(szabadido[0, cv]);

            cvvissza = 12;
            while (szabadido[1, cvvissza] != "foglalt")
                cvvissza--;

            Console.WriteLine("Barna Eszter legkorábban távozhat: " + szabadido[0, cvvissza + 1]);



        }

    }
}
