public class anagrams_scratch
{
    public static void main(String[] args)
    {
        System.out.println("Clint Eastwood and Old West Action: " + anagrams("Clint Eastwood", "Old West Action"));
        System.out.println("Dog and God: " + anagrams("dog", "God"));
        System.out.println("Public relations and crap built on lies: " + anagrams("Public relations", "crap built on lies"));
        System.out.println("Racecar and racecars: " + anagrams("Racecar", "racecars"));
        System.out.println("Cats and scat: " + anagrams("Cats", "scat"));
        System.out.println("Scars and racks: " + anagrams("scars", "racks"));
    }

    public static boolean anagrams(String string1, String string2)
    {
        // count letter frequencies of both strings, then match based on that
        string1 = string1.toLowerCase().replace(" ", "");
        string2 = string2.toLowerCase().replace(" ", "");

        if(string1.length() != string2.length())
        {
            return false;
        }

        boolean countFlag = true;
        int[] charFreqs1 = new int[26];
        int[] charFreqs2 = new int[26];
        
        for(int i = 0; i < string1.length(); i++)
        {
            charFreqs1[string1.charAt(i) - 'a'] += 1;
            charFreqs2[string2.charAt(i) - 'a'] += 1;
        }

        // check if the frequencies match
        for(int i = 0; i < 26; i++) {
            if(charFreqs1[i] != charFreqs2[i])
            {
                countFlag = false;
            }
        }

        return countFlag;
    }
}