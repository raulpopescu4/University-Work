class AsyncAwaitDownloader
{
    public static async Task Run(List<string> urls)
    {
        Console.WriteLine("\nAsync/Await Downloader");

        foreach (var url in urls)
        {
            try
            {
                var content = await DownloadContentAsync(url);
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

    private static async Task<string> DownloadContentAsync(string url)
    {
        using (HttpClient httpClient = new HttpClient())
        {
            try
            {
                return await httpClient.GetStringAsync(url);
            }
            catch (HttpRequestException ex)
            {
                throw new Exception($"Download failed for {url}: {ex.Message}", ex);
            }
        }
    }

    private static void SaveContentToFile(string url, string content)
    {
        var fileName = $"{Guid.NewGuid()}.html";
        File.WriteAllText(fileName, content);
        Console.WriteLine($"Saved content to file: {fileName}");
    }
}
