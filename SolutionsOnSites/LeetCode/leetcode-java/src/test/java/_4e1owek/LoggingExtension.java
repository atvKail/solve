package _4e1owek;

import org.junit.jupiter.api.extension.ExtensionContext;
import org.junit.jupiter.api.extension.TestWatcher;

public class LoggingExtension implements TestWatcher {
    @Override
    public void testFailed(ExtensionContext context, Throwable cause) {
        System.err.println("[FAILED] " + context.getDisplayName());
    }

    @Override
    public void testSuccessful(ExtensionContext context) {
        System.out.println("[PASSED] " + context.getDisplayName());
    }
}
