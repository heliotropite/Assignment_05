#----------------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# AdamH, 2020-Feb-23, added functionality and changed
#        primary data structure to use dictionaries. 
#----------------------------------------------------#

# Declare variables
strChoice = '' # User input
lstTbl = []  # list of dicts to hold data
lstRow = []  # list of data row
dictRow = {} # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

objFile = open(strFileName, 'r')
for row in objFile:
    lstRow = row.strip().split(',')
    dictRow = {'id': int(lstRow[0]), 'album': str(lstRow[1]), 'band': str(lstRow[2])}
    lstTbl.append(dictRow)
objFile.close()

print ('Loaded from file - ', strFileName)

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # Display menu allowing the user to choose:
    print('\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'l': # 1. Load in inventory from the specified text file
        dictRow = ''
        lstTbl = []
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dictRow = {'id': int(lstRow[0]), 'album': str(lstRow[1]), 'band': str(lstRow[2])}
            lstTbl.append(dictRow)
        objFile.close()
        print ('Loaded from file - ', strFileName)

    elif strChoice == 'a': # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = int(input('Enter an ID: '))
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        dictRow = {'id': int(strID), 'album': strTitle, 'band': strArtist}
        lstTbl.append(dictRow)
        
    elif strChoice == 'i': #3. Display the current data to the user each time the user wants to display the data
        print('ID | CD Title | Artist')
        for row in lstTbl:
            print(row.get('id'), row.get('album'), row.get('band'), sep=' | ')
            
    elif strChoice == 'd': # 4. Allow users to delete rows out of their list of dictionaries
        choice = input('Which item ID do you want to delete?\n')
        deleted = False
        for row in lstTbl:
            if row.get('id') == int(choice):     
                delRow = lstTbl.index(row)
                lstTbl.pop(delRow)
                deleted = True
        if deleted == True:
            print('Deleted item with ID ', choice, end='.\n')
        else:
            print('Found no entries with that ID number.')

        
    elif strChoice == 's': # 5. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        lstRow = []
        for row in lstTbl:
            lstRow = row.values()
            strRow = ''
            for item in lstRow:
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        print('Saved current inventory list.')
        
    elif strChoice == 'x': # 6. Exit the program if the user chooses so
        break
    
    else:
        print('Please choose either l, a, i, d, s or x!')
