___

programmers 72410

```java
import java.util.*;
class Solution {
    public String solution(String new_id) {
        String result;

        result = new_id.toLowerCase(Locale.ROOT);
        result = result.replaceAll("[^-._[0-9][a-z]]", "");
        result = result.replaceAll("[.]{2,}", ".");

        if(result.startsWith(".")) {
            if(result.length() > 1) {
                result = result.substring(1);
            } else {
                result = "";
            }
        }
        if(result.endsWith(".")) {
            result = result.substring(0, result.length()-1);
        }

        if(result == "") {
            result = "a";
        }

        if(result.length() > 15) {
            result = result.substring(0, 15);
        }
        if(result.endsWith(".")) {
            result = result.substring(0, result.length()-1);
        }

        String rst = result.substring(result.length()-1);

        while(result.length() < 3) {
            result = result.concat(rst);
        }

        return result;
    }
}
```

