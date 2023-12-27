static class Parser
{
    // Default HTTP port
    public const int Port = 80;

    // HTTP request string
    public static string RequestString(string hostname, string endpoint) =>
        $"GET {endpoint} HTTP/1.1\r\n" +
        $"Host: {hostname}\r\n" +
        $"Content-Length: 0\r\n\r\n";

    // Parse the content to find the value of the length header
    public static int ContentLength(string content)
    {
        foreach (string responseLine in content.Split('\r', '\n'))
        {
            var headDetails = responseLine.Split(':');

            if (headDetails.Length == 2 && headDetails[0].Trim() == "Content-Length")
                return int.Parse(headDetails[1].Trim());
        }

        // If the header is not found, return a default value (e.g., -1)
        return -1;
    }

    // Check if a complete HTTP response has been received
    public static bool ReceivedFullResponse(string content) =>
        content.Contains("\r\n\r\n");
}
