using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Windows.Forms;
using ConsoleHotKey;

namespace Mouse_Keys
{
    class Program
    {
        static void Main(string[] args)
        {
            // register my hotkeys
            HotKeyManager.RegisterHotKey(Keys.A, KeyModifiers.Alt | KeyModifiers.Shift);
            HotKeyManager.RegisterHotKey(Keys.D, KeyModifiers.Alt | KeyModifiers.Shift);
            HotKeyManager.RegisterHotKey(Keys.W, KeyModifiers.Alt | KeyModifiers.Shift);
            HotKeyManager.RegisterHotKey(Keys.S, KeyModifiers.Alt | KeyModifiers.Shift);
            HotKeyManager.HotKeyPressed += new EventHandler<HotKeyEventArgs>(HotKeyManager_HotKeyPressed);

            // keep program running
            Console.ReadLine();
        }

        /// <summary>
        /// function that executes when one of the hotkeys is triggered
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        static void HotKeyManager_HotKeyPressed(object sender, HotKeyEventArgs e)
        {
            // checks to see
            switch (e.Key)
            {
                case Keys.W:
                    Console.WriteLine(e.Key);
                    break;

                case Keys.S:
                    Console.WriteLine(e.Key);
                    break;

                case Keys.A:
                    Console.WriteLine(e.Key);
                    break;

                case Keys.D:
                    Console.WriteLine(e.Key);
                    break;
            }
        }
    }
}
