/**
 * Created by Same on 5/31/2018.
 */
import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class Server implements ServerClass {

    public Server() {}

    public String execute() {
        return "Executed Procedure call";
    }

    public static void main(String args[]) {

        try {
            Server obj = new Server();
            ServerClass stub = (ServerClass) UnicastRemoteObject.exportObject(obj, 0);

            // Bind the remote object's stub in the registry
            Registry registry = LocateRegistry.getRegistry();
            registry.bind("Server", stub);

            System.out.println("Server ready");
        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
