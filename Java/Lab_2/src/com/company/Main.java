package com.company;

import java.io.*;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);
        System.out.print("Input file's name or full path to it: ");
        File file = new File(in.nextLine());

        if (!file.exists()) {
            System.out.println("No such file or directory");
            return;
        }

        FileReader reader = new FileReader(file);
        Scanner scanner = new Scanner(reader);

        int count_regular[] = new int[26];
        Arrays.fill(count_regular, 0);
        int count_capital[] = new int[26];
        Arrays.fill(count_capital, 0);

        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            for (int i = 0; i < line.length(); i++) {
                int ascii = (int) line.charAt(i);
                if (ascii > 96 && ascii < 123) {
                    count_regular[ascii - 97]++;
                } else if (ascii > 64 && ascii < 91) {
                    count_capital[ascii - 65]++;
                }
            }
        }

        File output = new File("output.txt");
        if (!output.exists()) {
            output.createNewFile();
        }

        FileWriter writer = new FileWriter(output);
        for (int i = 97; i < 123; i++) {
            String separator = "";
            for (int j = 0; j < 5 - ("" + count_regular[i - 97]).length(); j++)
                separator += " ";
            separator += "||    ";
            writer.write((char) i + " - " + count_regular[i - 97] +
                    separator + (char) (i - 32) + " - " + count_capital[i - 97] + '\n');
        }

        reader.close();
        writer.close();
        return;
    }
}
