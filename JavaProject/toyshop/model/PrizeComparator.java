package toyshop.model;

import java.util.Comparator;

public class PrizeComparator implements Comparator<Prize>{

    @Override
    public int compare(Prize o1, Prize o2) {
        /*
         if(o1.getPriority() < o2.getPriority())//если приоритет o1 меньше приоритета o2
            return -1;
        if(o1.getPriority() == o2.getPriority()) //если приоритет o1 равен приоритету o2
            return 0;
        return 1;//если приоритет o1 больше приоритета o2
         */
        return o1.getPriority() - o2.getPriority();
    }
    
}
