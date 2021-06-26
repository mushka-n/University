package com.company;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;
import java.util.Scanner;


public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        ////////// NAME //////////

        System.out.print("Input full name: ");
        String input_fullName = in.nextLine();

        ArrayList<String> fullName = new ArrayList<>(
                Arrays.asList(input_fullName.split(" ")));

        ////////// BIRTH DATE //////////

        SimpleDateFormat format_birthDate = new SimpleDateFormat("dd/MM/yyyy");
        format_birthDate.setLenient(false);
        Date birthDate;

        while (true) {
            birthDate = null;
            System.out.print("Input birth date in DD/MM/YYYY format: ");
            String input_birthDate = in.nextLine();
            try {
                birthDate = format_birthDate.parse(input_birthDate);
                break;
            } catch (ParseException ignored) {}
            System.out.println("Inserted date is invalid");
        }

        ////////// AGE //////////

        long passed = new Date().getTime() - birthDate.getTime();
        long msecs_per_year = 24L * 60 * 60 * 1000 * 365;
        int years = (int) (passed / msecs_per_year);

        ////////// SEX //////////

        String sex, maleEnd = "ич", femaleEnd = "на";
        String otchestvo = fullName.get(fullName.size() - 1);
        String inputEnd = otchestvo.substring(otchestvo.length() - 2);
        if (inputEnd.equals(maleEnd)) sex = "Мужчина";
        else if (inputEnd.equals(femaleEnd)) sex = "Женщина";
        else sex = "Не определено";


        ////////// OUTPUT //////////

        System.out.println("Surname:   " + fullName.get(0));
        System.out.print("Initials:  ");
        for (String part : fullName) System.out.print(part.charAt(0) + ".");
        System.out.println();
        System.out.println("Sex:       " + sex);
        System.out.println("Age:       " + years);
    }
}
