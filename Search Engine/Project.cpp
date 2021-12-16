#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <unordered_map>
#include <map>
#include <vector>
using namespace std;

//these are global variables that store all the websites and keywords, used at points in the algorithim where a number corespondence is needed,
//a work around would have been to create a type of struct where strings hold some values without the need of arrays, due both being a small list i kept it as is
string websitelist[30] = {"www.geeksforgeeks.com", "www.algorithms.com", "www.hardware.com", "www.hardwareshop.com",
                          "www.programming.com", "www.computergate.com", "www.datascientist.org", "www.computerscience.net", "www.programmer.org",
                          "www.javatpoint.com", "www.software.com", "www.leetcode.com", "www.towardscomputerscience.com", "www.udicity.com", "www.computer.org",
                          "www.wikipedia.org", "www.udemy.com", "www.w3schools.com", "www.cplusplus.com", "www.isocpp.org", "www.programiz.com",
                          "www.learncpp.com", "www.stackoverflow.com", "www.java.com", "www.python.org", "www.tutorialspoint.com",
                          "www.softwaretesting.com", "www.uiprogrammer.org", "www.github.com", "www.wired.com"};

//struct that will be used to store the website content
struct Website
{
    double clicks = 1;      //number of clicks also read in from file after first run and initially has a value of one before first run
    double impression;      //impressions read in from file
    double rank;            //the rank of the website after all calculations are completed
    double connections = 0; //amount of webbistes the website is connected to
    double inconnect = 0;   //amount of websites connected to this website
    double pr;              //used for when iteration is finished
    double prevpr;          //used for during the current iteration
    double multiplier;
};
string keywordlist[17] = {"c++", "java", "data", "data structure", "algorithm",
                          "structure", "programming", "dynamic programming",
                          "python", "machine", "machine learning", "struct", "ai", "object",
                          "class", "graph", "complexity"};
map<string, Website> websiteranks;
/*
 ^^^^^^^here is where a first issue was solved. As noted the website struct cant necessarly be global
what I mean by this is I cant search "website: geeksforgeeks.com" and it would just show up we would  need a way of storing all these websites
so i used a map to store all these websites with their values and in order to search for a specfic website all you would do is plug in its website name, 
found in website list
*/
class PageRank
{
private:
    vector<int> v;
    vector<vector<int> > graph;

public:
    PageRank(string fullfile)
    {
        //The following code was used before using a general PR in a file, since i couldnt comment on a comment i put the commented version in another file called Pagerankwithcomments.txt
        /*
        graph.resize(30);
        ifstream input;
        input.open(impressionfile); 
        string all = "";
        while (getline(input, all))
        {
            stringstream current(all);             
            string currentwebsite;                
            string temp;                           
            getline(current, currentwebsite, ','); 
            while (!current.eof())
            {
                getline(current, temp, ',');                          
                websiteranks[currentwebsite].impression = stoi(temp); 
            }
        }
        input.close();
        input.open(graphfile);
        all = "";
        while (getline(input, all)) 
        {
            stringstream current(all);
            string first;
            string second;

            bool flag1, flag2 = false;    
            getline(current, first, ','); 
            getline(current, second);     
            int indexi, indexj;           
            for (int i = 0; i < 30; i++) 
            {
                if (first == websitelist[i])
                {
                    indexi = i;
                    flag1 = true;
                    break;
                }
            }
            for (int i = 0; i < 30; i++)
            {
                if (second == websitelist[i])
                {
                    indexj = i;
                    flag2 = true;
                    break;
                }
            }
            if (!flag1 || !flag2) 
            {
                continue;
            }
            graph[indexi].push_back(indexj);                 
            websiteranks[websitelist[indexj]].connections++; 
            websiteranks[websitelist[indexi]].inconnect++; 
        }
        double itsum = 0.0;
        for (int i = 0; i < 30; i++)
        {
            websiteranks[websitelist[i]].prevpr = websiteranks[websitelist[i]].inconnect; 
            websiteranks[websitelist[i]].pr = websiteranks[websitelist[i]].prevpr;
        }
        for (int i = 0; i < 100; i++) 
        {
            bool allless = false;        
            for (int j = 0; j < 30; j++) 
            {
                for (int k = 0; k < 30; k++)
                {
                    websiteranks[websitelist[k]].multiplier = (double)(websiteranks[websitelist[k]].prevpr * 0.85) / (double)websiteranks[websitelist[k]].connections;
                }
                for (int k = 0; k < 30; k++)
                {
                    if (find(graph[j].begin(), graph[j].end(), k) != graph[j].end())
                    {
                        itsum += websiteranks[websitelist[k]].multiplier;
                    }
                }
                websiteranks[websitelist[j]].pr = itsum + 0.15;
                itsum = 0;
            }
            for (int j = 0; j < 30; j++)
            {
                if (websiteranks[websitelist[j]].pr + 0.01 < (websiteranks[websitelist[j]].prevpr))
                {
                    break; 
                }
                if (j == 29)
                {
                    allless = true; 
                }
            }
            if (allless)
            {
                break;
            }
            for (int j = 0; j < 30; j++)
            {
                websiteranks[websitelist[j]].prevpr = websiteranks[websitelist[j]].pr; 
            }
        }
        double max = -1;
        double min = 99999999;
        for (int i = 0; i < 30; i++)
        {
            if (websiteranks[websitelist[i]].pr > max)
            {
                max = websiteranks[websitelist[i]].pr;
            }
            if (websiteranks[websitelist[i]].pr < min)
            {
                min = websiteranks[websitelist[i]].pr;
            }
        }
        for (int i = 0; i < 30; i++)
        {
            websiteranks[websitelist[i]].pr = (websiteranks[websitelist[i]].pr - min) / (max - min);
            double pr = websiteranks[websitelist[i]].pr;
            double currentimp = (double)websiteranks[websitelist[i]].impression;
            websiteranks[websitelist[i]].rank = 0.4 * pr + ((1.0 - ((0.1 * currentimp) / (1.0 + (0.1 * currentimp)))) * pr + ((0.1 * currentimp) / (1.0 + (0.1 * currentimp))) * (double)websiteranks[websitelist[i]].clicks) * 0.6;
        }
        */

        //this is used in the case that the program was initilized at least once
        //just read from input file with all values
        ifstream input(fullfile);
        for (int i = 0; i < 30; i++)
        {
            input >> websiteranks[websitelist[i]].pr >> websiteranks[websitelist[i]].impression >> websiteranks[websitelist[i]].clicks;
            double pr = (double)websiteranks[websitelist[i]].pr;
            double currentimp = (double)websiteranks[websitelist[i]].impression;
            double ctr = (double)websiteranks[websitelist[i]].clicks / currentimp;
            websiteranks[websitelist[i]].rank = 0.4 * pr + ((1.0 - ((0.1 * currentimp) / (1.0 + (0.1 * currentimp)))) * pr + ((0.1 * currentimp) / (1.0 + (0.1 * currentimp))) * ctr) * 0.6;
        }
        input.close();
    }
    void exitcase(string ogfile)
    {
        //if there is an exit then print all the data to a file we can read later
        ofstream output(ogfile);
        for (int i = 0; i < 30; i++)
        {
            output << websiteranks[websitelist[i]].pr << " " << websiteranks[websitelist[i]].impression << " " << websiteranks[websitelist[i]].clicks << endl;
        }
        output.close();
    }
};
//this a struct used for sorting the websites according to the rank
struct Ranklist
{
    double rank;
    string name;
};
//used for the #include algorithims sort() function
bool websiteCompare(Ranklist &left, Ranklist &right)
{
    return (left.rank > right.rank);
}

class SearchEngine
{
private:
    multimap<string, string> wordtree;       //initial wordtree
    multimap<string, string> sortedwordtree; //sorted wordtree which will be used for the rest of time

    int amount = 0; //this was used for testing purposes

public:
    vector<string> currentview; //this vector will be where the websites are stored incase a user decides to "click"
    SearchEngine(string file)
    {

        //read from the input file with the keywords
        ifstream input(file);
        string all = "";
        while (getline(input, all)) //while you can store a line in variable "all" do it
        {
            stringstream current(all);             //turn all into a stringstream
            string currentwebsite;                 //this is where the first word in the line is stored (the first word is a website url)
            string temp;                           //this is where all the rest of the words will be stored but will alternate according to the below while loop
            getline(current, currentwebsite, ','); //store the word up until the first comma in currentwebsite (again this will be the url)
            while (!current.eof())
            {
                getline(current, temp, ','); //if a comma is found store everything before that in a variable temp (this will be a keyword)
                for (int i = 0; i < 18; i++) //iterate through the keyword wordlist and see which word it coresponds to this is a failsafe incase a blank character is found and accidentally stored
                {
                    if (temp == keywordlist[i])
                    {
                        wordtree.insert(make_pair(temp, currentwebsite)); //store the website in the temp key-> temp (keyword) value-> (website), since this is a multimap the website is inserted at the end of the node
                        break;
                    }
                }
            }
        }
        string prevfirst = "ai";    //we know the first word is ai so i did this, but check finalsort() function for an example of how you would do this if you didnt know what the first was
        vector<string> store;       //array of strings which will be used to rinsert into a tree after sorting
        vector<Ranklist> finalsort; //this is a vector that wi;; be used to sort

        for (const auto &x : wordtree) //this function is why I regret using a wordtree, the basic point of it is to iterate through a wordtree,
        //then in each node sort all the websites, and finally place it into a new wordtree, later we will erase the now useless unsorted wordtree, however iterating was very hard
        {
            store.push_back(x.second); //keep pushing the value (websites) onto a vector as long as
            if (x.first != prevfirst)  //if the first value is not equal to "prevfirst" we know that the key has officially changed so we must sort
            {
                for (vector<string>::iterator it = store.begin(); it != store.end(); ++it)
                {
                    //now we will pass all the strings in the vector to the "sorting struct"
                    Ranklist x;
                    x.rank = websiteranks[*it].rank; //it takes the rank
                    x.name = *it;                    //and the name
                    finalsort.push_back(x);
                }
                store.erase(store.begin(), store.end());                  //finally we can erase the string vector so we can use it for the next key
                sort(finalsort.begin(), finalsort.end(), websiteCompare); //and we sort the things we passed into the "sorting struct"
                //the sort function sorts in nlogn time and it does so using my websitecompare function because you cant "sort a struct" unless you have some way of comparing them
                for (vector<Ranklist>::iterator it = finalsort.begin(); it != finalsort.end(); ++it)
                {
                    sortedwordtree.insert(make_pair(prevfirst, it->name)); //now that its sorted we can just place it back in a tree that is now sorted
                }
                finalsort.erase(finalsort.begin(), finalsort.end());
            }
            prevfirst = x.first; //set the prevfirst to the current first so we can compare it to the next first
        }
        //have to do it one more time because one vector is ignored due to it not having prevfirst!=x.first (because vectors are finished)
        for (vector<string>::iterator it = store.begin(); it != store.end(); ++it)
        {
            Ranklist x;
            x.rank = websiteranks[*it].rank;
            x.name = *it;
            finalsort.push_back(x);
        }
        store.erase(store.begin(), store.end());
        sort(finalsort.begin(), finalsort.end(), websiteCompare);
        for (vector<Ranklist>::iterator it = finalsort.begin(); it != finalsort.end(); ++it)
        {
            sortedwordtree.insert(make_pair(prevfirst, it->name));
        }
        finalsort.erase(finalsort.begin(), finalsort.end());
    }
    void sortall()
    {
        //after printing the search results we will sort since all the values change
        for (int i = 0; i < 30; i++) //first we need to calculte the rank so we will use the normalized pr and ctr current impressions calculation
        {
            double pr = (double)websiteranks[websitelist[i]].pr;
            double currentimp = (double)websiteranks[websitelist[i]].impression;
            double ctr = (double)websiteranks[websitelist[i]].clicks / currentimp;
            websiteranks[websitelist[i]].rank = 0.4 * pr + ((1.0 - ((0.1 * currentimp) / (1.0 + (0.1 * currentimp)))) * pr + ((0.1 * currentimp) / (1.0 + (0.1 * currentimp))) * ctr) * 0.6;
        }

        vector<string> store;
        vector<Ranklist> finalsort;
        multimap<string, string> temp;
        temp = sortedwordtree;  //we will create a temporary word tree and copy all the elements that way we can use this one
        sortedwordtree.clear(); // we weill empty out the sortedwordtree since we will be filling it with new values
        bool flag = false;
        string prevfirst;
        //the rest of the logic is the same as initilization but with temp, and with the added bonus of us not knowing what the first value will be
        for (const auto &x : temp)
        {
            if (!flag) //flag here checks if we have ever had a "prevfirst" if we havent then we know that we just entered the tree and this is the first
            {
                prevfirst = x.first;
                flag = true; //setting it to true so this if statement is never entered after;
            }
            if (x.first != prevfirst)
            {
                for (vector<string>::iterator it = store.begin(); it != store.end(); ++it)
                {
                    Ranklist x;
                    x.rank = websiteranks[*it].rank;
                    x.name = *it;
                    finalsort.push_back(x);
                }
                store.clear();
                sort(finalsort.begin(), finalsort.end(), websiteCompare);
                for (vector<Ranklist>::iterator it = finalsort.begin(); it != finalsort.end(); ++it)
                {
                    sortedwordtree.insert(make_pair(prevfirst, it->name));
                }
                finalsort.clear();
            }
            store.push_back(x.second);
            prevfirst = x.first;
        }
        //have to do it one more time because one vector is ignored due to it not having prevfirst!=x.first (because vectors are finished)
        for (vector<string>::iterator it = store.begin(); it != store.end(); ++it)
        {
            Ranklist x;
            x.rank = websiteranks[*it].rank;
            x.name = *it;
            finalsort.push_back(x);
        }
        store.clear();
        sort(finalsort.begin(), finalsort.end(), websiteCompare);
        for (vector<Ranklist>::iterator it = finalsort.begin(); it != finalsort.end(); ++it)
        {
            sortedwordtree.insert(make_pair(prevfirst, it->name));
        }
        finalsort.erase(finalsort.begin(), finalsort.end());
    }
    void search_through(string value)
    {
        cout << "----------------------------------------" << endl;
        int i = 0;
        if (value.find("AND") != string::npos) //we have entered the "AND" case
        {
            unordered_map<string, string> checkrep; //create a hashmap this will check for collisions later
            string current = "";
            string temp;
            bool flag = false;
            int it = 0;
            string prev = "";
            for (auto j : value)
            {
                /*
                A lot of the time you will see me reference prev and temp, these are just for logic purposes and incase a user puts a space inbeteween a word
                like data structures this will also be repeated in the the rest of the scenarios, for clairty sake just look at it like only the
                word "prev" is used everything else is deleted because it is not going to be searched for in the map
                */
                it++;         //used to check if we finished iterating through "value" which is just the keyword the user passed
                if (j == ' ') //if we enter are now standing on a spacebar
                {
                    current = temp;
                    if (current == "AND") // if the word we have is "AND" we can now check the previous word because this word is a word other than AND
                    {
                        auto itr1 = sortedwordtree.lower_bound(prev); //for a multumap we specify the first part which we iterate through
                        auto itr2 = sortedwordtree.upper_bound(prev); //and the second part we will iterate through
                        /*
                        for example lets say key java, java -> wwwtest.com, www.test3.com, www.test4.com
                        the lower bound will be right before test.com and the upper bound after test4.com each in logn time then we just iterate through in n time
                        */
                        while (itr1 != itr2)
                        {
                            if (checkrep.find(itr1->second) != checkrep.end()) //if this value has no collisions its the first time we see it so we dont print it out because AND means its present in both
                            {
                                //since there was a collision in this case
                                cout << ++i << "- " << itr1->second << endl; //print the website name
                                websiteranks[itr1->second].impression++;     //increase its impressions
                                currentview.push_back(itr1->second);         //put it in the vector declared all the way at the top so if a user clicks we know what theyre clicking
                            }
                            else
                            {
                                //no collision so add it to the hashmap for later
                                checkrep[itr1->second] = itr1->second;
                            }
                            itr1++;
                        }
                        prev.erase();
                        current.erase();
                    }
                    else
                    {
                        if (prev == "")
                        {
                            prev = current;
                        }
                        else
                        {
                            prev.append(" " + current);
                        }
                    }
                    temp.erase();
                }
                else
                {
                    temp = temp + j;
                    if (it == value.size())
                    {
                        if (prev == "")
                        {
                            prev = temp;
                        }
                        else
                        {
                            prev.append(" " + temp);
                        }
                    }
                }
            }
            //we will do it one more time since the last word will always be ignored in the above loop
            auto itr1 = sortedwordtree.lower_bound(prev);
            auto itr2 = sortedwordtree.upper_bound(prev);
            while (itr1 != itr2)
            {
                if (checkrep.find(itr1->second) != checkrep.end())
                {
                    cout << ++i << "- " << itr1->second << endl;
                    websiteranks[itr1->second].impression++;
                    currentview.push_back(itr1->second);
                }
                else
                {
                    checkrep[itr1->second] = itr1->second;
                }
                itr1++;
            }
        }
        else if (value.find("OR") != string::npos)
        {
            unordered_map<string, string> checkrep; //hashmap for collision handling
            string current = "";
            string temp;
            bool flag = false;
            int it = 0;
            string prev = "";
            vector<Ranklist> a, b, c; //these will be used to merge the website lists
            /*
            further explanation: pretend we dont find a collision so we will print this website, but if we go to the next word the website we just found's rank
            may be more than all the previous ones' ranks, so that means we cant just print them. We now have the case of 2 sorted arrays so we can just merge them
            */
            for (auto j : value)
            {
                it++;
                if (j == ' ')
                {
                    current = temp;
                    if (current == "OR") //we can now look at the word that is after "OR"
                    //its important to understand some of this logic may not be used now but it is left like this in the case that this program
                    //can be one day further improved to check multiple AND's (it currently cant)
                    {
                        auto itr1 = sortedwordtree.lower_bound(prev);
                        auto itr2 = sortedwordtree.upper_bound(prev);
                        while (itr1 != itr2)
                        {
                            if (checkrep.find(itr1->second) == checkrep.end()) //if there is no collision
                            {
                                checkrep[itr1->second] = itr1->second;   //store it in the hashmap for later collision testing
                                websiteranks[itr1->second].impression++; //increase the impressions for that website
                                Ranklist current;                        //we will do some sorting so keep track of name and rank and store it in the "Ranking struct"
                                current.name = itr1->second;
                                current.rank = websiteranks[itr1->second].rank;
                                a.push_back(current);
                            }
                            itr1++;
                        }
                        //at the end of this loop we know hava an array of sorted websites in "a"
                        prev.erase();
                        current.erase();
                    }
                    else
                    {
                        if (prev == "")
                        {
                            prev = current;
                        }
                        else
                        {
                            prev.append(" " + current);
                        }
                    }
                    temp.erase();
                }
                else
                {
                    temp = temp + j;
                    if (it == value.size())
                    {
                        if (prev == "")
                        {
                            prev = temp;
                        }
                        else
                        {
                            prev.append(" " + temp);
                        }
                    }
                }
            }
            auto itr1 = sortedwordtree.lower_bound(prev);
            auto itr2 = sortedwordtree.upper_bound(prev);
            //same logic apllies but this time it is stored in b vector
            while (itr1 != itr2)
            {
                if (checkrep.find(itr1->second) == checkrep.end())
                {
                    checkrep[itr1->second] = itr1->second;
                    websiteranks[itr1->second].impression++;
                    Ranklist current;
                    current.name = itr1->second;
                    current.rank = websiteranks[itr1->second].rank;
                    b.push_back(current);
                }
                itr1++;
            }
            //since we have two sorted vectors we can merge them and store them in a vector c
            merge(a.begin(), a.end(), b.begin(), b.end(), back_inserter(c), websiteCompare);
            for (int i = 0; i < (a.size() + b.size()); i++)
            {
                //now we print the name of these sorted vectors which is the website name
                cout << i + 1 << "- " << c[i].name << endl;
                currentview.push_back(c[i].name); //and we store it in the array declared on top incase a user wants to use it
            }
        }
        else if (value.find("\"") != string::npos)
        {
            //this is the easiest once and is the best case in terms of time
            unordered_map<string, string> checkrep; //create the hashmap again
            string temp = "";
            for (int i = 0; i < value.size(); i++)
            {
                if (value[i] != ('"')) //this just makes sure no quotation is in the "temp" keyword which we will search ie: "java" becomes java
                {
                    temp = temp + value[i];
                }
            }
            auto itr1 = sortedwordtree.lower_bound(temp);
            auto itr2 = sortedwordtree.upper_bound(temp);
            while (itr1 != itr2)
            {
                if (checkrep.find(itr1->second) == checkrep.end())
                {
                    cout << ++i << "- " << itr1->second << endl; //print it
                    checkrep[itr1->second] = itr1->second;       //store it in the hashmap to check for collisions later this is unlikely to be needed but is a corner case handler
                    currentview.push_back(itr1->second);
                }
                itr1++;
            }
        }
        else
        {
            //the following code is the scanario if a user puts a word or series of words with no quottions, this will be handled like the OR scenario so the code is about the same
            unordered_map<string, string> checkrep;
            vector<Ranklist> a, b, c;
            string temp;
            int it = 0;
            for (auto j : value)
            {
                it++;
                if (j == ' ')
                {
                    auto itr1 = sortedwordtree.lower_bound(temp);
                    auto itr2 = sortedwordtree.upper_bound(temp);
                    while (itr1 != itr2)
                    {
                        if (checkrep.find(itr1->second) == checkrep.end())
                        {
                            checkrep[itr1->second] = itr1->second;
                            websiteranks[itr1->second].impression++;
                            Ranklist current;
                            current.name = itr1->second;
                            current.rank = websiteranks[itr1->second].rank;
                            a.push_back(current);
                        }
                        itr1++;
                    }
                    temp.erase();
                }
                else
                {
                    temp = temp + j;
                }
            }
            auto itr1 = sortedwordtree.lower_bound(temp);
            auto itr2 = sortedwordtree.upper_bound(temp);
            while (itr1 != itr2)
            {
                if (checkrep.find(itr1->second) == checkrep.end())
                {
                    checkrep[itr1->second] = itr1->second;
                    websiteranks[itr1->second].impression++;
                    Ranklist current;
                    current.name = itr1->second;
                    current.rank = websiteranks[itr1->second].rank;
                    b.push_back(current);
                }
                itr1++;
            }
            merge(a.begin(), a.end(), b.begin(), b.end(), back_inserter(c), websiteCompare);
            for (int i = 0; i < (a.size() + b.size()); i++)
            {
                cout << i + 1 << "- " << c[i].name << endl;
                currentview.push_back(c[i].name);
            }
        }
        cout << "----------------------------------------" << endl;
    }
    void click(int index)
    {
        websiteranks[currentview[index - 1]].clicks++; //go to the index of where theres a click, theres a word stored there take that word (itll be a website), find its struct and increase its clicks
    }
    void resultagain() //a small inprovement can be made here, but i wasnr sure if it made sense, if the results are printed again sorting
    //might be needed the reason it wasnt done is because currentview would still stay the same
    {
        cout << "----------------------------------------" << endl;
        for (int i = 0; i < currentview.size(); i++)
        {
            cout << i + 1 << "- " << currentview[i] << endl;
            websiteranks[currentview[i]].impression++;
        }
        cout << "----------------------------------------" << endl;
    }
    void eraseold()
    {
        currentview.erase(currentview.begin(), currentview.end()); //since this varable is declared in the class we need to erase it once the user decides to make a new search
    }
};

//functions decleration
void search(SearchEngine, PageRank, string);
void results(SearchEngine, PageRank, string);
void viewing(SearchEngine, string, PageRank, string);
void search(SearchEngine x, PageRank y, string file)
{
    string term; //this is what a user searches
    cout << "Please enter a term to search: ";
    cin.ignore();
    getline(cin, term); //take in the word or series of  words
    cout << "Search results: " << endl;
    x.search_through(term); //put them in the function at the top for the searchengine class that handles are the searching
    x.sortall();            //now its printed for the user and we can sort
    results(x, y, file);    // this goes to results page which asks the user what they now want to do
}

void viewing(SearchEngine x, string y, PageRank z, string file)
{
    int choice;
    cout << "You are now viewing: " << y << "." << endl;
    cout << "Would you like to" << endl;
    cout << "1. Back to results\n2. New Search\n3. Exit" << endl;
    cout << "Type in your choice: ";
    cin >> choice;
    switch (choice)
    {
    case 1:
        cout << "Search results:" << endl;
        x.resultagain();
        results(x, z, file);
        break;
    case 2:
        x.eraseold();
        search(x, z, file);
        break;
    default:
        cout << "Program closed." << endl;
        z.exitcase(file);
        return;
    }
}
void results(SearchEngine x, PageRank y, string file)
{
    int choice;
    cout << "Would you like to" << endl;
    cout << "1. Choose a webpage to open\n2. New Search \n3. Exit\n";
    cout << "Type in your choice: ";
    cin >> choice;
    switch (choice)
    {
    case 1:
        cout << "Choose one of the webpages to click." << endl;
        cin >> choice;
        x.click(choice);                                //take the choice increiment the clicks
        viewing(x, x.currentview[choice - 1], y, file); //trigger the viewing function which will say "you are now viewing...."
        break;
    case 2:
        x.eraseold();       //since the user doesnt need the previous results we can clear the vector
        search(x, y, file); //go to search case
        break;
    default:
        cout << "Program closed." << endl; //the program closes
        y.exitcase(file);                  //all the info is stored to a file
        return;
    }
}
int main()
{
    string file = "temp.csv"; //this is where all the data is stored
    PageRank rank(file);
    SearchEngine fakegoogle("keywords.csv"); //this is the search engine, the constructer takes in the keywords
    int choice;                              //we can now ask the user what they want to do initially
    cout
        << "What would you like to do?" << endl;
    cout << "1. New Search\n2. Exit" << endl;
    cout << "Type in your choice: ";
    cin >> choice;
    switch (choice)
    {
    case 1:
        search(fakegoogle, rank, file);
        break;
    default:
        cout << "Program closed." << endl;
        rank.exitcase(file);

        break;
    }
    return 0;
}
