using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Globalization;

namespace eutazas
{
    class adatstruktura
    {
        public int megallo;
        public string menetdatum;
        public string kartyaazon;
        public string berletazon;
        public string ervdatum;
                
        public bool ervenyessegellenorzes()
        {
            if (ervdatum.Length <= 2)
                if (ervdatum == "0") return false;
                else return true;
            else
                if (DateTime.Compare(DateTime.ParseExact(menetdatum.Split('-')[0], "yyyyMMdd", CultureInfo.InvariantCulture), DateTime.ParseExact(ervdatum, "yyyyMMdd", CultureInfo.InvariantCulture)) > 0)
                    return false;   
            return true;
        }
        public bool ingyenes()
        {
            if (berletazon == "NYP" || berletazon == "RVS" || berletazon == "GYK")
                return true;
            return false;
        }
        public bool kedvezmenyes()
        {
            if (berletazon == "TAB" || berletazon == "NYB" )
                return true;
            return false;
        }

        public int napokszama(int e1, int h1, int n1, int e2, int h2, int n2)
        {
            h1 = (h1 + 9) % 12;
            e1 = e1 - h1 / 10;
            int d1 = 365 * e1 + e1 / 4 - e1 / 100 + e1 / 400 + (h1 * 306 + 5) / 10 + n1 - 1;
            h2 = (h2 + 9) % 12;
            e2 = e2 - h2 / 10;
            int d2 = 365 * e2 + e2 / 4 - e2 / 100 + e2 / 400 + (h2 * 306 + 5) / 10 + n2 - 1;
            return d2 - d1;
        }


        
        public bool figyelmeztetni()
        {
            if (ervdatum.Length > 2)
            {
                int e1 = Convert.ToInt32(menetdatum.Substring(0, 4));
                int e2 = Convert.ToInt32(ervdatum.Substring(0, 4));
                int h1 = Convert.ToInt32(menetdatum.Substring(4, 2));
                int h2 = Convert.ToInt32(ervdatum.Substring(4, 2));
                int n1 = Convert.ToInt32(menetdatum.Substring(6, 2));
                int n2 = Convert.ToInt32(ervdatum.Substring(6, 2));
                if (napokszama(e1, h1, n1, e2, h2, n2) >= 0 && napokszama(e1, h1, n1, e2, h2, n2) <= 3)
                    return true;
            }
            return false;
        }
    }
    class eutazas
    {
        public static List<adatstruktura> adatok = new List<adatstruktura>();
       
        public static void Feladat1()
        {   
           FileStream fs = new FileStream("utasadat.txt",FileMode.Open);
           StreamReader sr = new StreamReader(fs);
           string egysor;
           while ((egysor = sr.ReadLine()) != null)
           {
               string[] egysordarabok = egysor.Split(' ');
               adatstruktura egyutas = new adatstruktura();
               egyutas.megallo = Convert.ToInt32(egysordarabok[0]);
               egyutas.menetdatum = egysordarabok[1];
               egyutas.kartyaazon = egysordarabok[2];
               egyutas.berletazon = egysordarabok[3];
               egyutas.ervdatum = egysordarabok[4];
               adatok.Add(egyutas);
           }
           sr.Close();
           fs.Close(); 
        }
        public static int Feladat2()
        {
            return adatok.Count();
        }

        public static int Feladat3()
        {
            int ervenytelenek = 0;
            foreach (var utas in adatok)
                if (!utas.ervenyessegellenorzes()) ervenytelenek++;
            return ervenytelenek;
        }

        public static string Feladat4()
        {
            int maxutas = 0;
            int maxmegallo = 0;
            int utaspmo = 1;
            for (int i = 1; i < adatok.Count(); i++)
            {
                if (adatok[i-1].megallo == adatok[i].megallo)
                {
                    utaspmo++;
                }
                else
                {
                    if (utaspmo + 1 > maxutas)
                    {
                        maxutas = utaspmo + 1;
                        maxmegallo = adatok[i - 1].megallo;
                    }
                    utaspmo = 0;
                }
            }
            return "A legtöbb utas (" + maxutas.ToString() + " fő) a " + maxmegallo.ToString() + ". megállóban próbált felszállni.";
        }

        public static string Feladat5()
        {
            int ingyenesdb = 0;
            int kedvezmenydb = 0;
            foreach (var utas in adatok)
            {
                if (utas.ervenyessegellenorzes())
                {
                    if (utas.kedvezmenyes()) kedvezmenydb++;
                    if (utas.ingyenes()) ingyenesdb++;
                }
            }
            return "Ingyenesen utazók száma: " + ingyenesdb.ToString() + " fő\r\nA kedvezményesen utazók száma: " + kedvezmenydb.ToString() + " fő";
        }

        public static void Feladat7()
        {
            List<String> futasok = new List<String>();
            foreach (var utas in adatok)
            {
                if (utas.figyelmeztetni())
                {
                   futasok.Add(utas.kartyaazon + " " + DateTime.ParseExact(utas.ervdatum, "yyyyMMdd", CultureInfo.InvariantCulture).ToString("yyyy-MM-dd"));
                }
            }
            File.WriteAllLines("figyelmeztetes.txt", futasok);
        }

        static void Main(string[] args)
        {
            Feladat1();
            Console.WriteLine("2. feladat");
            Console.WriteLine("A buszra " + Feladat2().ToString() + " utas akart felszállni.");
            Console.WriteLine("3. feladat");
            Console.WriteLine("A buszra " + Feladat3().ToString() + " utas nem szállhatott fel.");
            Console.WriteLine("4. feladat");
            Console.WriteLine(Feladat4());
            Console.WriteLine("5. feladat");
            Console.WriteLine(Feladat5());
            Feladat7();
            
            Console.ReadLine();

        }
    }
}