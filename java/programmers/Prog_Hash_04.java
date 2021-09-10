package io.github.devwithpug;
// 프로그래머스 코딩테스트 해시 04 베스트앨범

// 문제 설명
// 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 
// 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.
// 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
// 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
// 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
// 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 
// 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.
// 제한사항
// genres[i]는 고유번호가 i인 노래의 장르입니다.
// plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
// genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
// 장르 종류는 100개 미만입니다.
// 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
// 모든 장르는 재생된 횟수가 다릅니다.
// 입출력 예
// genres	plays	return
// ["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]

import java.util.HashMap;
import java.util.Map.Entry;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

class Song {
    public int index;
    public String genre;
    public int plays;

    Song(int i, String g, int p) {
        this.index = i;
        this.genre = g;
        this.plays = p;
    }
}

class Solution_Hash_04 {
    public int[] solution(String[] genres, int[] plays) {
        List<Integer> list = new ArrayList<Integer>();
        HashMap<String, Integer> total_plays = new HashMap<String, Integer>();
        ArrayList<Song> arr = new ArrayList<Song>();

        for (int i = 0; i < genres.length; i++) {
            total_plays.put(genres[i], total_plays.getOrDefault(genres[i], 0) + plays[i]);
            arr.add(new Song(i, genres[i], plays[i]));
        }
        Collections.sort(arr, new Comparator<Song>() {
            public int compare(Song s1, Song s2) {
                return s2.plays - s1.plays;
            }
        });

        List<Entry<String, Integer>> list_entry = new ArrayList<Entry<String, Integer>>(total_plays.entrySet());
        Collections.sort(list_entry, new Comparator<Entry<String, Integer>>() {
            public int compare(Entry<String, Integer> obj1, Entry<String, Integer> obj2) {
                return obj2.getValue().compareTo(obj1.getValue());
            }
        });

        for (Entry<String, Integer> entry : list_entry) {
            int maximum_song = 0;
            for (Song i : arr) {
                if (entry.getKey().equals(i.genre) && maximum_song < 2) {
                    list.add(i.index);
                    maximum_song++;
                }
            }
        }
        int[] answer = list.stream().mapToInt(i -> i).toArray();
        return answer;
    }
}

public class Prog_Hash_04 {
    public static void main(String[] args) {
        Solution_Hash_04 sol = new Solution_Hash_04();
        String[] genres = { "classic", "pop", "classic", "classic", "pop" };
        int[] plays = { 500, 600, 150, 800, 2500 };
        sol.solution(genres, plays);
    }
}
