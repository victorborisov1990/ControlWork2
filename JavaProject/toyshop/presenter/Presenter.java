package toyshop.presenter;

import toyshop.model.Service;

public class Presenter {
    Service game;

    public Presenter(){
        this.game = new Service();
    }

    public void addToy(String title, int weight){
        game.addToy(title, weight);
    }

    public String addPrize(int id){
        return game.addPrize(id);
    }

    public void changeWeight (int id, int weight){
        game.changeWeight(id, weight);
    }

    public String getAllPrizes(){
        return game.getAllPrizes();
    }

    public String showToys(){
        return game.showToys();
    }

}
