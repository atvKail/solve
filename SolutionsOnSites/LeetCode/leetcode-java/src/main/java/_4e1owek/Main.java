package _4e1owek;

import java.io.PrintWriter;
import java.util.Scanner;

import static org.junit.platform.engine.discovery.DiscoverySelectors.selectClass;
import org.junit.platform.launcher.Launcher;
import org.junit.platform.launcher.LauncherDiscoveryRequest;
import org.junit.platform.launcher.core.LauncherDiscoveryRequestBuilder;
import org.junit.platform.launcher.core.LauncherFactory;
import org.junit.platform.launcher.listeners.SummaryGeneratingListener;
import org.junit.platform.launcher.listeners.TestExecutionSummary;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Номер теста=");
        String testClassName = "_4e1owek.solutions.ProblemN" + scanner.nextLine() + "Test";
        scanner.close();

        try {
            Class<?> testClass = Class.forName(testClassName);

            LauncherDiscoveryRequest request = LauncherDiscoveryRequestBuilder.request()
                    .selectors(selectClass(testClass))
                    .build();

            Launcher launcher = LauncherFactory.create();
            SummaryGeneratingListener listener = new SummaryGeneratingListener();
            launcher.registerTestExecutionListeners(listener);
            launcher.execute(request);

            TestExecutionSummary summary = listener.getSummary();
            summary.printTo(new PrintWriter(System.out));
        } catch (ClassNotFoundException e) {
            System.err.println("Класс теста не найден: " + testClassName);
        }
    }
}