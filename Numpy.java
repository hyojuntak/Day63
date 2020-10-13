package JC.Day63;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;

/**
 * Day63
 */
public class Day63 {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        HashMap <String, Integer> hash = new HashMap<String, Integer>();

        for (int i = 0; i < N; i++) {
            hash.put(sc.next(), sc.nextInt());
        }
        System.out.println(hash);
        
        List<Integer> valueList = new ArrayList<>(hash.values());
        valueList.sort(Integer::compareTo);
        for (Integer value : valueList) {
            for (String key : hash.keySet()) {
                if(hash.get(key).equals(value))
                    System.out.print(key);
            }   
        }
    }
}














