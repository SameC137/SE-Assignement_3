import java.rmi.Remote;
import java.rmi.RemoteException;

public interface ServerClass extends Remote {
    String execute () throws RemoteException;
}