import csv 

inputCSV = open('rotation.csv', 'r')
outputCSV = open('gcal.csv', 'w')
reader = csv.reader(inputCSV)
writer = csv.writer(outputCSV)
writer.writerow(['Subject', 'StartDate', 'Start Time', 'End Date', 'End Time', 'All day event', 'Description', 'Location'])
for row in reader:
    if( row[1].isdigit() ):
        day = int(row[1])
        date = row[0]
        
        blocks = ['A','B','C','D','E','F','G']
        drop = 'H'
        for i in range(1,day):
            blocks.insert(0, drop)
            drop = blocks.pop()

        if( row[2] == 'n'):
            
          writer.writerow(['Day ' + str(day), date, '', date, '', 'TRUE', '', ''])    
          writer.writerow([blocks[0] + ' Block',  date , '7:34:00 AM',  date,  '8:21:00 AM','' ,'' ,''])
          writer.writerow([blocks[1] + ' Block',  date , '8:25:00 AM', date, '9:12:00 AM','' ,'' ,''])
          writer.writerow([blocks[2] + ' Block',  date ,  '9:16:00 AM', date, '10:03:00 AM', '' ,'' ,''])
          writer.writerow([blocks[3] + ' Block',  date , '10:07:00 AM', date, '10:54:00 AM', '' ,'' ,''])
          writer.writerow([blocks[4] + ' Block',  date , '10:54:00 AM', date, '12:19:00 PM','' ,'' ,''])
          writer.writerow([blocks[5] + ' Block',  date , '12:23:00 PM', date, '1:10:00 PM', '' ,'' ,''])
          writer.writerow([blocks[6] + ' Block',  date , '1:14:00 PM', date, '2:02:00 PM', '' ,'' ,''])
        else:
          writer.writerow(['Day ' + str(day) + ' (Early Release)', date, '', date, '', 'TRUE', '', ''])
          writer.writerow([blocks[0] + ' Block',  date , '7:34:00 AM',  date,  '8:08:00 AM','' ,'' ,''])
          writer.writerow([blocks[1] + ' Block',  date , '8:12:00 AM', date, '8:45:00 AM','' ,'' ,''])
          writer.writerow([blocks[2] + ' Block',  date ,  '8:49:00 AM', date, '9:23:00 AM', '' ,'' ,''])
          writer.writerow([blocks[3] + ' Block',  date , '9:27:00 AM', date, '10:00:00 AM', '' ,'' ,''])
          writer.writerow([blocks[4] + ' Block',  date , '10:04:00 AM', date, '10:38:00 AM','' ,'' ,''])
          writer.writerow([blocks[5] + ' Block',  date , '10:42:00 AM', date, '11:15:00 AM', '' ,'' ,''])
          writer.writerow([blocks[6] + ' Block',  date , '11:15:00 AM', date, '12:42:00 PM', '' ,'' ,''])
  
    else:
        day = row[1]
        date = row[0]
        writer.writerow([day, date, '', date, '', 'TRUE', '', ''])

inputCSV.close()    
outputCSV.close()

