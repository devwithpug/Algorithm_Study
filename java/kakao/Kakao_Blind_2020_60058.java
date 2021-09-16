// 2020 KAKAO BLIND RECRUITMENT 괄호 변환 https://programmers.co.kr/learn/courses/30/lessons/60058

class Solution {

    private String[] split(String w) {
        if (w.length() == 0) return new String[]{"", ""};
        int cnt = 0;
        String u = "";
        for (String s : w.split("")) {
            if (s.equals("(")) cnt++;
            else cnt--;
            u += s;
            if (cnt == 0) break;
        }
        String v = w.substring(u.length());

        return new String[]{u, v};
    }

    private boolean isValid(String u) {
        int cnt = 0;
        for (String s : u.split("")) {
            if (s.equals("(")) cnt ++;
            else if (s.equals(")")) cnt--;
            if (cnt < 0) return false;
        }
        return true;
    }

    private String progress(String w) {
        if (w.equals("")) return "";
        String[] split = split(w);
        String u = split[0];
        String v = split[1];

        if (isValid(u)) {
            return u + progress(v);
        } else {
            u = u.substring(1, u.length() - 1);
            String tmp = "(" + progress(v) + ")";
            for (String s : u.split("")) {
                if (s.length() == 0) break;
                tmp += s.equals("(") ? ")" : "(";
            }
            return tmp;
        }
    }

    public String solution(String p) {
        return progress(p);
    }
}
