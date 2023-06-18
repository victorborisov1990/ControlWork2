package toyshop.model;

public class Prize {//приз - единица какой-либо игрушки с приоритетом на выдачу
    private int id;//id выигранной игрушки
    private int priority;//чем выше приоритет, тем больше шанс на выпадение игрушки

    public Prize(int id, int priority){
        this.id = id;
        this.priority = priority;
    }

    public int getId() {
        return id;
    }

    public int getPriority() {
        return priority;
    }
}
