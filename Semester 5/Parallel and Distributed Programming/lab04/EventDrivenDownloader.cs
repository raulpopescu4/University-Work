using System;
using System.Collections.Generic;
using System.IO;
using System.Net;
using System.Threading;
using System.Threading.Tasks;

class EventDrivenDownloader
{
    public static void Run(List<string> urls)
    {
        Console.WriteLine("\nEvent-Driven Downloader");

        foreach (var url in urls)
        {
            try
            {
                var content = DownloadContent(url).GetAwaiter().GetResult();
                var contentLength = Parser.ContentLength(content);
                Console.WriteLine($"Downloaded {content.Length} bytes from {url}, Content Length: {contentLength}");

                // Save content to a file (optional)
                SaveContentToFile(url, content);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error downloading from {url}: {ex.Message}");
            }
        }
    }

    private static async Task<string> DownloadContent(string url)
    {
        using (var client = new WebClient())
        {
            var downloadTaskCompletionSource = new TaskCompletionSource<string>();

            client.DownloadStringCompleted += (sender, e) =>
            {
                if (e.Error != null)
                {
                    downloadTaskCompletionSource.SetException(e.Error);
                }
                else if (e.Cancelled)
                {
                    downloadTaskCompletionSource.SetCanceled();
                }
                else
                {
                    downloadTaskCompletionSource.SetResult(e.Result);
                }
            };

            client.DownloadStringAsync(new Uri(url));

            return await downloadTaskCompletionSource.Task;
        }
    }

    private static void SaveContentToFile(string url, string content)
    {
        var fileName = $"{Guid.NewGuid()}.html";
        File.WriteAllText(fileName, content);
        Console.WriteLine($"Saved content to file: {fileName}");
    }
}
