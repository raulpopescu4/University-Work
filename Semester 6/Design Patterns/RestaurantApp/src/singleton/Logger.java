package singleton;

import java.io.FileOutputStream;
import java.io.OutputStream;

public class Logger {
    private static OutputStream output;
    private static Logger logger;

    private Logger() {
        initOutput();
    }

    private void initOutput() {
        try {
            output = new FileOutputStream("log\\data.txt");
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }
    }

    public static Logger getInstance() {
        if (Logger.logger == null) {
            Logger.logger = new Logger();
        }

        return Logger.logger;
    }

    public void log(String data) {
        if (output == null) {
            initOutput();
        }
        try {
            data += "\n";
            Logger.output.write(data.getBytes(), 0, data.length());
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }
    }
}
