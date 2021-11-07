// 2021 카카오 채용연계형 인턴십 - 거리두기 확인하기
// https://programmers.co.kr/learn/courses/30/lessons/81302

class Solution {

    private boolean check(String[][] map) {
        int[] m1_x = {-1, 0, 1, 0};
        int[] m1_y = {0, 1, 0, -1};

        int[] m2_x = {-2, 0, 2, 0};
        int[] m2_y = {0, 2, 0, -2};

        int[] m3_x = {-1, 1, 1, -1};
        int[] m3_y = {1, 1, -1, -1};

        for (int y = 0; y < map.length; y++) {
            for (int x = 0; x < map.length; x++) {

                if (map[y][x].equals("P")) {
                    for (int i = 0; i < 4; i++) {
                        int dx = x + m1_x[i];
                        int dy = y + m1_y[i];

                        if (map.length > dx && 0 <= dx && map.length > dy && 0 <= dy) {
                            if (map[dy][dx].equals("P")) {
                                return false;
                            }
                        }
                    }
                    for (int i = 0; i < 4; i++) {
                        int dx = x + m2_x[i];
                        int dy = y + m2_y[i];

                        if (map.length > dx && 0 <= dx && map.length > dy && 0 <= dy) {
                            if (map[dy][dx].equals("P")) {
                                if (!map[y + m1_y[i]][x + m1_x[i]].equals("X")) {
                                    return false;
                                }
                            }
                        }
                    }
                    for (int i = 0; i < 4; i++) {
                        int dx = x + m3_x[i];
                        int dy = y + m3_y[i];

                        if (map.length > dx && 0 <= dx && map.length > dy && 0 <= dy) {
                            if (map[dy][dx].equals("P")) {
                                if (!map[y + m1_y[i]][x + m1_x[i]].equals("X") || !map[y + m1_y[(i+1) % 4]][x + m1_x[(i+1) % 4]].equals("X")) {
                                    return false;
                                }
                            }
                        }
                    }
                }

            }
        }

        return true;
    }

    public int[] solution(String[][] places) {
        int[] answer = new int[places.length];
        
        for (int i = 0; i < places.length; i++) {

            String[][] map = new String[places.length][places.length];

            for (int j = 0; j < places.length; j++) {
                map[j] = places[i][j].split("");
            }

            answer[i] = (check(map)) ? 1 : 0;
        }
        return answer;
    }
}