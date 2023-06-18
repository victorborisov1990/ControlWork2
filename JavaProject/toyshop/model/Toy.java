package toyshop.model;

import java.lang.StringBuilder;

public class Toy {
    private static int idCounter;
    private int id;
    private String title;
    private int weight;


    public Toy (String title, int weight){
        id = idCounter++;
        this.title = title;//название
        this.weight = weight;//вес в контексте: шанс на выпадение данной игрушки
    }

    public int getId() {
        return id;
    }

    public int getWeight() {
        return weight;
    }

    public String getTitle (){
        return title;
    }

    public void setWeight(int weight){
        this.weight = weight;
    }

    public void setTitle (String title){
        this.title = title;
    }

    
    
    @Override
    public String toString(){
        StringBuilder sb = new StringBuilder();
        sb.append("id: ")
            .append(getId())
            .append("\tназвание: ")
            .append(getTitle())
            .append("\tвес (в %): ")
            .append(getWeight());
        return sb.toString();     
    }
    
}