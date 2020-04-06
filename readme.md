Run the run_main.bat file.
It will fetch the Covid-19 cases from MoHFW website every 15 minutes & show a desktop notifcation if there is a change in tally.

Every time, the data is fetched: it is stored in Log file.

If you want to use it through a scheduler:
Change Line 47,48 in main.py
from 

if __name__ == '__main__':
    run() #main()

to 
if __name__ == '__main__': 
    main()

It will directly execute the main function. You can schedule the task for every 10 minutes or so.


Thanks,
Rajat.
