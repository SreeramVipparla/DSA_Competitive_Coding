
/**
 * QUESTION

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 
 */


 /**
 * ANSWER
 */
import java.io.*;
import java.util.*;

public class Top_K_frequent_Elements {

  Map<Integer, Integer> countMap = new HashMap<>();
  List<Integer> ret = new ArrayList<>();
  for (int n : nums) {
      if (countMap.containsKey(n)) {
          countMap.put(n ,countMap.get(n)+1);
      } else {
          countMap.put(n ,1);
      }
  }
 PriorityQueue<Map.Entry<Integer, Integer>> pq =
          new PriorityQueue<Map.Entry<Integer, Integer>>((o1, o2) -> o2.getValue() - o1.getValue());
  pq.addAll(countMap.entrySet());
  
  List<Integer> ret = new ArrayList<>();
  for(int i = 0; i < k; i++){
      ret.add(pq.poll().getKey());
  }
  return ret;
}
 /**
 * SOURCE-LEETCODE
 */