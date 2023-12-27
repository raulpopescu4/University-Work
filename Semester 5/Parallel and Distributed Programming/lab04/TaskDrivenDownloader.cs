using System.Net;

class TaskDrivenDownloader
{
    public static void Run(List<string> urls)
    {
        Console.WriteLine("\nTask-Driven Downloader");

        var downloadTasks = new List<Task>();

        foreach (var url in urls)
        {
            downloadTasks.Add(Task.Run(() => DownloadAndSave(url)));
        }

        try
        {
            Task.WaitAll(downloadTasks.ToArray());
        }
        catch (AggregateException ex)
        {
            foreach (var innerException in ex.InnerExceptions)
            {
                Console.WriteLine($"Error downloading: {innerException.Message}");
            }
        }
    }

    private static void DownloadAndSave(string url)
    {
        try
        {
            var content = DownloadContent(url);
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

    private static string DownloadContent(string url)
    {
        try
        {
            using (var client = new WebClient())
            {
                return client.DownloadString(url);
            }
        }
        catch (WebException ex)
        {
            throw new Exception($"Download failed for {url}: {ex.Message}", ex);
        }
    }

    private static void SaveContentToFile(string url, string content)
    {
        var fileName = $"{Guid.NewGuid()}.html";
        File.WriteAllText(fileName, content);
        Console.WriteLine($"Saved content to file: {fileName}");
    }
}
