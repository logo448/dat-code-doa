using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Windows.Forms;
using ConsoleHotKey;
using System.Drawing;

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
            // get current cursor position
            Point pos = Cursor.Position;

            // switch statement that checks to see which command was executed
            switch (e.Key)
            {
                // check W
                case Keys.W:
                    {
                        pos.Y = pos.Y - 20;
                        Cursor.Position = pos;
                        break;
                    }                   

                // check S
                case Keys.S:
                    {
                        pos.Y = pos.Y + 20;
                        Cursor.Position = pos;
                        break;
                    }

                // check A
                case Keys.A:
                    {
                        pos.X = pos.X - 20;
                        Cursor.Position = pos;
                        break;
                    }

                // check D
                case Keys.D:
                    {
                        pos.X = pos.X + 20;
                        Cursor.Position = pos;
                        break;
                    }
            }
        }
    }
}
