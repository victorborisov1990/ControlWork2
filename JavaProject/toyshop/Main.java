package toyshop;

import toyshop.view.Console;
import toyshop.view.View;
public class Main {
    public static void main(String[] args) {
        View view = new Console();      
        view.start(); 
    }
}
