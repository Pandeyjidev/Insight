# Insight Code Challenge
Link : https://github.com/InsightDataScience/find-political-donors
# Problem statement 
(As in the link above)
You’re a data engineer working for political consultants and you’ve been asked to help identify possible donors 
for a variety of upcoming election campaigns.The Federal Election Commission regularly publishes campaign contributions and while you don’t want to pull specific donors from those files — because using that information for fundraising or commercial purposes is illegal — you want to identify the areas (zip codes) that may be fertile ground for soliciting future donations for similar candidates.

Because those donations may come from specific events (e.g., high-dollar fundraising dinners) but aren’t marked as such in the data, you also want to identify which time periods are particularly lucrative so that an analyst might later correlate them to specific fundraising events.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Read Deployment for further details

### Prerequisites

What things you need to install the software and how to install them

1> Fork the Git repository [ Need a Git account ]

2> Pull it into your local system (Preferably Ubuntu)

3> Check for installed python ( Type "python -v" to check on command line )

### Installing

There are no major dependencies as such for this project. Incase you find any issue installing the project, kindly mail me at (utkarsh DOT pandey178 AT <gmail> DOT com)



## What should I do now?

### Run the shell script and provide your data

To run the code , kindly follow the steps below after you have the folder in your system.

1> Put your files into "/input"

2> Check if files in "/output" is blank or deleted (It overwrites to accomodate multiple files)

3> Incase your file is using any particular kind of seperator then open "/src/main.py" and change the "Delimeter" variable
at the bottom

4> Open the folder you just downloaded and type "./run.sh" to run the code

5> Check for outputs in "/output" folder

### Automated test script time !

1> Open "/insight_testsuite"
2> Type "./run_tests.sh" in command line 


## Ways to improve the project

1> This is my first project using python, so incase you find any time complexities or a better solution for algo/code. Kindly let me know so that I can make the necessary changes
2> We can use Multithreading to divide the data into chunks and then process accordingly to avoid buffer overflows.
3> One more way to avoid buffer overflow is to read no more than 10000 data into the array to clean/process in "main.py"
  - use chunks of data and save it in an intermediary file
  - before reading the next chunk load this data 
  - i've used a dictionary to help scale the code for further improvements
4> Can make better test cases
5> Can use chron_sort.py for chronological sorting
6> Can move Median fucntion to another file.
7> I'm sure there will be more, I will be glad if you mail me your honest feedback or any suggestion regarding the repository



## Authors

* **Judit Lantos**   - *Problem statement* - [jlantos](https://github.com/jlantos)
* **Hoa Nguyen**     - *Problem statement* - [emhoa](https://github.com/emhoa)

* **Utkarsh Pandey** - *Solution Contibutor* - [Pandeyjidev](https://github.com/Pandeyjidev)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is solely for Insight Code Challenge. Feel free to use my code (Don't forget to give me free stars <3).
