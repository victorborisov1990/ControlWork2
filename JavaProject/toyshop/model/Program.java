package toyshop.model;

public class Program {
    public static void main(String[] args) {
        Service game = new Service();      
        game.addToy("Кукла  ", 90);
        game.addToy("Машинка", 50);
        game.addToy("Конструктор", 5);//самый редкий, должен выпадать в последнюю очередь
        System.out.println(game.showToys());
        game.addPrize(0);
        game.addPrize(1);
        game.addPrize(2);
        game.addPrize(1);
        game.addPrize(0);
        game.addPrize(0);
        game.addPrize(1);
        game.addPrize(2);
        game.addPrize(2);
        game.addPrize(0);
        System.out.print(game.getAllPrizes());
    }
}
