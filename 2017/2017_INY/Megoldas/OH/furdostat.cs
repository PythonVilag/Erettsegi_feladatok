using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

namespace furdostat
{
    class Program
    {
        struct furdovendegadat
        {
            public int vendeg;
            public byte reszleg;
            public TimeSpan ido;
            public byte kibe;
        }
        static void Main(string[] args)
        {
            FileStream fajl = new FileStream("furdoadat.txt", FileMode.Open);
            StreamReader olvaso = new StreamReader(fajl);
            furdovendegadat[] adatok = new furdovendegadat[800];
            
            //1. feladat Fájlbeolvasás
            
            int db = 0;
            byte ora, perc, sec;
            while (!olvaso.EndOfStream)
            {
                String[] sorbe = olvaso.ReadLine().Split(' ');
                adatok[db].vendeg = int.Parse(sorbe[0]);
                adatok[db].reszleg = byte.Parse(sorbe[1]);
                adatok[db].kibe = byte.Parse(sorbe[2]);
                ora = byte.Parse(sorbe[3]);
                perc = byte.Parse(sorbe[4]);
                sec = byte.Parse(sorbe[5]);
                adatok[db].ido = new TimeSpan(ora, perc, sec);

                db++;
            }
            db--;
            olvaso.Close();
            fajl.Close();
            Console.WriteLine("1. feladat");
            Console.WriteLine("A fájl beolvasása megtörtént.");
                
            // 2. feladat

            Console.WriteLine("\r\n 2. feladat");
            Console.WriteLine("Az első vendég {0}-kor lépett ki az öltözőből.", adatok[0].ido);
            int utolso = adatok[db].vendeg;
            int cv = db;
            while (utolso == adatok[cv].vendeg)
            {
                cv--;
            }
            Console.WriteLine("Az utolsó vendég {0}-kor lépett ki az öltözőből.", adatok[cv+1].ido);
            
            //3. feladat
            
            int csakegyreszlegen = 0;
            cv = 1;
            while (cv < db)
            {
                int j = 1;
                while (adatok[cv].vendeg == adatok[cv - 1].vendeg)
                {
                    j++;
                    cv++;
                }
                if (j == 4) csakegyreszlegen++;
                cv++;
            }
            Console.WriteLine("\r\n 3. feladat");
            Console.WriteLine("A fürdőben {0} vendég járt csak egy részlegen.", csakegyreszlegen);
            
            //4. feladat

            TimeSpan maxido = new TimeSpan(0, 0, 0);
            TimeSpan beido, kiido;
            int maxvendeg = 0;
            cv = 1;
            while (cv < db)
            {
                beido = adatok[cv-1].ido;
                while (adatok[cv].vendeg == adatok[cv - 1].vendeg)
                   cv++;
                kiido = adatok[cv-1].ido;
                if (maxido < kiido - beido)
                {
                    maxido = kiido - beido;
                    maxvendeg = cv-1;
                }
                cv++;
            }
            Console.WriteLine("\r\n 4. feladat");
            Console.WriteLine("A legtöbb időt eltöltő vendég:");
            Console.WriteLine("{0}. vendég {1}", adatok[maxvendeg].vendeg, maxido);
            
            // 5. feladat

            int reggel = 0;
            int napkozben = 0;
            int este = 0;
            
            for (int i = 0; i < db; i++)
            {
                if (adatok[i].reszleg == 0 && adatok[i].kibe == 1)
                {
                    if (new TimeSpan(9, 0, 0) > adatok[i].ido)
                        reggel++;
                    else
                        if (new TimeSpan(16, 0, 0) > adatok[i].ido)
                            napkozben++;
                        else
                            este++;
                }
            }
            Console.WriteLine("\r\n 5. feladat");
            Console.WriteLine("6-9 óra között {0} vendég", reggel);
            Console.WriteLine("9-16 óra között {0} vendég", napkozben);
            Console.WriteLine("16-20 óra között {0} vendég", este);

            // 6. feladat

            FileStream kifajl = new FileStream("szauna.txt", FileMode.Create);
            StreamWriter iro = new StreamWriter(kifajl);

            cv = 0;
            while (cv < db)
            {
                TimeSpan szaunaido = new TimeSpan(0, 0, 0);
                while (adatok[cv].vendeg == adatok[cv + 1].vendeg)
                {
                    if (adatok[cv].reszleg == 2)
                    {
                        szaunaido += adatok[cv + 1].ido - adatok[cv].ido;
                        cv++;
                    }
                    cv++;
                }
                if (szaunaido > new TimeSpan(0, 0, 0))
                    iro.WriteLine("{0} {1}", adatok[cv].vendeg, szaunaido);

                cv++;
            }
            iro.Close();
            kifajl.Close();
            Console.WriteLine("\r\n 6. feladat");
            Console.WriteLine("A fájlba írás megtörtént.");
 

            // 7. feladat

            cv = 0;
            Boolean r1 = false;
            Boolean r2 = false;
            Boolean r3 = false;
            Boolean r4 = false;
            int dbr1, dbr2, dbr3, dbr4;
            dbr1 = 0; dbr2 = 0; dbr3 = 0; dbr4 = 0;
            while (cv < db)
            {
                while (adatok[cv].vendeg == adatok[cv + 1].vendeg)
                {
                    switch (adatok[cv].reszleg)
                    {
                        case 1:
                            {
                                if (!r1) dbr1++;
                                r1 = true;
                                break;
                            }
                        case 2:
                            {
                                if (!r2) dbr2++;
                                r2 = true;
                                break;
                            }
                        case 3:
                            {
                                if (!r3) dbr3++;
                                r3 = true;
                                break;
                            }
                        case 4:
                            {
                                if (!r4) dbr4++;
                                r4 = true;
                                break;
                            }
                    }
                    cv++;
                }
                r1 = false; r2 = false; r3 = false; r4 = false;
                cv++;
            }

            Console.WriteLine("\r\n 7. feladat");
            Console.WriteLine("Uszoda: {0}", dbr1);
            Console.WriteLine("Szaunák: {0}", dbr2);
            Console.WriteLine("Gyógyvizes medencék: {0}", dbr3);
            Console.WriteLine("Strand: {0}", dbr4);
            Console.ReadKey();
        }

    }
}
