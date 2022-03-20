def swapFileContents():
    file1 = input('Enter the first file \n')
    file2 = input('Enter the second file \n')

    file1File = open(file1)
    file2File = open(file2)

    file1Contents = file1File.readlines()
    file2Contents = file2File.readlines()

    file1Writable = open(file1, 'w')
    file2Writable = open(file2, 'w')

    file1Writable.writelines(file2Contents)
    file2Writable.writelines(file1Contents)

    print('The operation has been done :)')

swapFileContents()
