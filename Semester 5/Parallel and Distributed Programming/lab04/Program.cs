// Program.cs
using System;
using System.Collections.Generic;
using System.Threading;

class Program
{
    static void Main(string[] args)
    {
        Directory.CreateDirectory("Downloads");

        List<string> hosts = new List<string>
        {
            "http://cs.ubbcluj.ro/~rlupsa/edu/pdp",
            "https://learn.microsoft.com/en-us/dotnet/standard/parallel-programming/task-parallel-library-tpl",
            "https://reddit.com/r/programare/"
        };

        Console.WriteLine("Callbacks");
        EventDrivenDownloader.Run(hosts);

        Thread.Sleep(2500);

        Console.WriteLine("\nTPL");
        TaskDrivenDownloader.Run(hosts);

        Thread.Sleep(2500);

        Console.WriteLine("\nTPL Async");
        AsyncAwaitDownloader.Run(hosts);

        Console.WriteLine("\nAsync/Await Downloader");
        AsyncAwaitDownloader.Run(hosts);

        Console.WriteLine("\nEvent-Driven Downloader");
        EventDrivenDownloader.Run(hosts);

        Console.WriteLine("\nTask-Driven Downloader");
        TaskDrivenDownloader.Run(hosts);

        Console.WriteLine("Press Enter to exit...");
        Console.ReadLine();
    }
}
