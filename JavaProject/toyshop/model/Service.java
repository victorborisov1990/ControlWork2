package toyshop.model;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Random;
import java.lang.StringBuilder;

public class Service {
    private PriorityQueue<Prize> toyDispenser;//хранит игрушки в порядке приоритета на выдачу. 
                                            // может содержать несколько одинаковых игрушек
    public List <Toy> aviableToys;//список уникальных игрушек, возможных к добавлению в диспенсер

    public Service(){
        Comparator<Prize> prizeComparator = new PrizeComparator();//для сортировки добавляемых призов
        this.toyDispenser = new PriorityQueue<>(10, prizeComparator.reversed());//иниц-я очереди при создании экземпляра сервиса
        this.aviableToys = new ArrayList<>();
    }

    public void addToy (String title, int weight){//добавление новой игрушки в список уникальных игрушек
        // проверка веса на правильность, возможно преобразование
        Toy toy = new Toy(title,weight);
        aviableToys.add(toy);
    }

    public String addPrize(int id){
        if(id < 0 || id >= aviableToys.size()){
            return "Некорректный номер игрушки.";
        }
        Toy toy = aviableToys.get(id);//выбираем игрушку из доступных по id
        Random rand = new Random();
        int prizeId = toy.getId();//id приза = id игрушки
        int weight = toy.getWeight();
        int priority = rand.nextInt(100 - weight + 1) + weight;//вычисляется приоритет в очереди на выдачу
        Prize prize =  new Prize(prizeId, priority);
        toyDispenser.add(prize);//добавление нового приза в очредь. при добавлении сортировка по приоритету
        return "добавлено успешно.";
    }

    public void changeWeight (int id, int weight){//редактирование веса у игрушки
        // проверка веса на правильность, возможно преобразование
        aviableToys.get(id).setWeight(weight);
    }

    public String showToys(){
        StringBuilder sb = new StringBuilder();
        for(Toy toy : aviableToys){
            sb.append(toy).append("\n");
        }
        return sb.toString();
    }

    private int getPrize(){
        Prize currentPrize = toyDispenser.poll();
        if(currentPrize == null) return 999;
        return currentPrize.getId(); //вернуть id приза. Далее уже по призу определить игрушку. 
    }

    public String getAllPrizes(){
        StringBuilder sb = new StringBuilder();
        int toyId = 0;
        int count = 1;
        while (toyId != 999){//пока не закончатся призы
            toyId = getPrize();//получить id очередного приза
            for (int i = 0; i < aviableToys.size(); i++){//в списке игрушек ищем по  id приза
                if(aviableToys.get(i).getId()==toyId){//если id приза и игрушки совпадают
                    sb.append(count++).append(") ").append(aviableToys.get(i)).append("\n");
                    //добавляем строку в список выданных призов
                }
            }
        }
        return sb.toString();
    }
    
}
