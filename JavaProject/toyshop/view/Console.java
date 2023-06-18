package toyshop.view;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

import toyshop.presenter.Presenter;

public class Console implements View{
    private Scanner scanner;
    private Presenter presenter;
    private String pathToSave;
    private boolean work = true;

    public Console() {
        scanner = new Scanner(System.in, "cp866");
        presenter = new Presenter();
        pathToSave = "prizes.txt";
        print("Консоль готова к работе");
    }

    private void addToy(){
        print("Введите название игрушки: ");
        String title = inputText();
        print("Введите вес (шанс на плучение в %): ");
        int weight = inputInt();
        presenter.addToy(title, weight);
    }

    private void addPrize(){
        print("Введите номер игрушки: ");
        int id = inputInt();
        print(presenter.addPrize(id));
    }

    private void changeWeight(){
        print("Введите номер игрушки: ");
        int id = inputInt();
        print("Введите вес (шанс на плучение в %): ");
        int weight = inputInt();
        presenter.changeWeight(id, weight);
    }

    private void showPrizes(){
        String prizesList = presenter.getAllPrizes();
        print(prizesList);
        saveToFile(prizesList);
    }

    private void showToys(){
        print(presenter.showToys());
    }

    private void exit() {
        print("Работа завершена");
        scanner.close();
        work = false;
        //добавить сохранени в файл
    }

    private String inputText(){
        String text = scanner.nextLine();
        return text;
    }

    private int inputInt(){
        try {
            int number = scanner.nextInt();
            scanner.nextLine();
            return number;
        } catch (NumberFormatException e) {
            print("Ошибка : " + e.getMessage());
            return 0;
        }
    }

    private void saveToFile(String text){
        try (
        FileWriter fw = new FileWriter(pathToSave)) {
            fw.write(text);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void start() {
        while (work) {
            print("---------------------------------------------------\n" +
                    "1 - добавить новую игрушку\n" +
                    "2 - добавить игрушку к раздаче призов\n" +
                    "3 - изменить шанс выпадения игрушки\n" +
                    "4 - показать добавленные в аппарат игрушки\n" +
                    "5 - выдать призы\n" +
                    "6 - завершить работу");
                    System.out.print("Введите команду: ");
                    String choice = scanner.nextLine();
            switch (choice) {
                case "1":
                    addToy();
                    break;
                case "2":
                    addPrize();
                    break;
                case "3":
                    changeWeight();
                    break;
                case "4":
                    showToys();
                    break;
                case "5":
                    showPrizes();
                    break;
                case "6":
                    exit();
                    break;    
                default:
                    print("Ошибка ввода");
            }
        }
    }

    @Override
    public void print(String text) {
        System.out.println(text);
    }
    
}
