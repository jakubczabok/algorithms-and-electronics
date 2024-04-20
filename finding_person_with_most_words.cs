// This is my solution to this leetcode problem https://leetcode.com/problems/sender-with-largest-word-count/description/
// I am using dictionary to calculate and return name of sender who sent the most words in his messages
// message[i] is sent by senders[i] etc.

public class Solution {
    public string LargestWordCount(string[] messages, string[] senders) {
                Dictionary<string, int> messenger = new Dictionary<string, int>();
        int j = 0;
        string result = "";
        for (int i = 0; i < senders.Length; i++)
        {
            if (!(messenger.ContainsKey(senders[i])))
            {
                messenger.Add(senders[i], CountWords(messages[i]));
                if (messenger[senders[i]]>j)
                {
                    j=messenger[senders[i]];
                    result = senders[i];
                    
                }
                else if (messenger[senders[i]]==j)
                {
                    for (int k = 0; k <  Math.Min(result.Length, senders[i].Length); k++)
                    {
                        if (result[k] > senders[i][k])
                        {
                            break;
                        }
                        if (result[k] < senders[i][k])
                        {
                            result = senders[i];
                            break;
                        }
                        if (k + 1 == result.Length)
                        {
                            if (senders[i].Length > result.Length)
                            {
                                result = senders[i];
                                break;
                            }
                        }
                    }
                }
                
            }
            else
            {
                messenger[senders[i]] += CountWords(messages[i]);
                if (messenger[senders[i]] > j)
                {
                    j = messenger[senders[i]];
                    result = senders[i];
                }
                else if (messenger[senders[i]] == j)
                {
                    for (int k = 0; k < Math.Min(result.Length, senders[i].Length); k++)
                    {
                        if (result[k] > senders[i][k])
                        {
                            break;
                        }
                        if (result[k] < senders[i][k])
                        {
                            result = senders[i];
                            break;
                        }
                        if (k+1==result.Length)
                        {
                            if (senders[i].Length>result.Length)
                            {
                                result = senders[i];
                                break;
                            }
                        }
                    }
                }
            }
           
        }
        return result;
    }
    public int CountWords(string message)
    {
        int count = 1;

        for (int i = 0; i < message.Length; i++)
        {
            if (message[i]==' ')
            {
                count++;
            }
        }
        return count;
    }
}
