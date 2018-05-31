import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

/**
 * Created by Same on 5/31/2018.
 */
public class Client {

    private Client() {}

    public static void main(String[] args) {

        String host = (args.length < 1) ? null : args[0];
        try {
            Registry registry = LocateRegistry.getRegistry(host);
            ServerClass stub = (ServerClass) registry.lookup("Server");
            String response = stub.execute();
            System.out.println("response: " + response);
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}