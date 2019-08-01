import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.result_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()
        self.cb_var8 = tkinter.IntVar()
        self.cb_var9 = tkinter.IntVar()
        self.cb_var10 = tkinter.IntVar()
        self.cb_var11 = tkinter.IntVar()
        self.cb_var12 = tkinter.IntVar()
        self.cb_var13 = tkinter.IntVar()
        self.cb_var14 = tkinter.IntVar()
        self.cb_var15 = tkinter.IntVar()
        
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)
        self.cb_var8.set(0)
        self.cb_var9.set(0)
        self.cb_var10.set(0)
        self.cb_var11.set(0)
        self.cb_var12.set(0)
        self.cb_var13.set(0)
        self.cb_var14.set(0)
        self.cb_var14.set(0)
        
        self.cb1 = tkinter.Checkbutton(self.top_frame,
                                       text='Mean',
                                       variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame,
                                       text='Median',
                                       variable=self.cb_var2)
        self.cb4 = tkinter.Checkbutton(self.top_frame,
                                       text='Min',
                                       variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.top_frame,
                                       text='Max',
                                       variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.top_frame,
                                       text='Range',
                                       variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.top_frame,
                                       text='Sum',
                                       variable=self.cb_var7)
        self.cb8 = tkinter.Checkbutton(self.top_frame,
                                       text='Count',
                                       variable=self.cb_var8)
        self.cb9 = tkinter.Checkbutton(self.top_frame,
                                       text='1st Quartile',
                                       variable=self.cb_var9)
        self.cb10 = tkinter.Checkbutton(self.top_frame,
                                       text='Third Quartile',
                                       variable=self.cb_var10)
        self.cb11 = tkinter.Checkbutton(self.top_frame,
                                       text='Standard Deviation of population',
                                       variable=self.cb_var11)
        self.cb12 = tkinter.Checkbutton(self.top_frame,
                                       text='Variance of population',
                                       variable=self.cb_var12)
        self.cb13 = tkinter.Checkbutton(self.top_frame,
                                       text='Standard Deviation of sample',
                                       variable=self.cb_var13)
        self.cb14 = tkinter.Checkbutton(self.top_frame,
                                       text='Variance of sample',
                                       variable=self.cb_var14)
        self.cb15 = tkinter.Checkbutton(self.top_frame, text = 'Calculate all and print to file',
                                        variable = self.cb_var15)
        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text='Calculate',
                                        command=self.calc_result)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        self.result_label = tkinter.Label(self.result_frame,text='Result: ')
        self.result = tkinter.StringVar()
        self.result_amount_label = tkinter.Label(self.result_frame,textvariable=self.result)
        self.result_label.pack(side='left')
        self.result_amount_label.pack(side='left')

        self.cb1.pack()
        self.cb2.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()
        self.cb8.pack()
        self.cb9.pack()
        self.cb10.pack()
        self.cb11.pack()
        self.cb12.pack()
        self.cb13.pack()
        self.cb14.pack()
        self.cb15.pack()
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.top_frame.pack()
        self.result_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()
        
    def calc_result(self):
        
# Mean
        if self.cb_var1.get() == 1 or self.cb_var15.get() == 1:
            infile = open('C:/Users/Victor/Documents/project/numbers.txt', 'r')
            line = infile.readline()
            
            sumOfNum = float(line)
            counter = 1

            while line != '':
                line = infile.readline()
                if(line != ''):
                    sumOfNum = sumOfNum + float(line)
                    counter += 1
            if self.cb_var1.get() == 1:         
                self.result.set(sumOfNum/counter)
            if self.cb_var15.get() == 1:
                mean_to_print = sumOfNum/counter
            infile.close()

# Median
        if self.cb_var2.get() == 1 or self.cb_var15.get() == 1:
            infile = open('C:/Users/Victor/Documents/project/numbers.txt', 'r')
            line = infile.readline()

            listOfNum = [float(line)]

            while line != '':
                line = infile.readline()
                if(line != ''):
                    listOfNum.append(float(line))
            listOfNum.sort()        
            upperIndex = int(len(listOfNum) / 2)
            lowerIndex = int(len(listOfNum) / 2) - 1
          
            if(len(listOfNum) %2 == 0):
                if self.cb_var2.get() == 1:
                    self.result.set((listOfNum[upperIndex] +  listOfNum[lowerIndex]) / 2)
                if self.cb_var15.get() == 1:
                    median_to_print = (listOfNum[upperIndex] +  listOfNum[lowerIndex]) / 2
                
            if(len(listOfNum) %2 == 1):
                index = int(len(listOfNum) / 2)
                if self.cb_var2.get() == 1:                
                    self.result.set(listOfNum[index])
                if self.cb_var15.get() == 1:
                    median_to_print = listOfNum[index] 
            
            infile.close()
# Min        
        if self.cb_var4.get() == 1 or self.cb_var15.get() == 1:
            infile = open('C:/Users/Victor/Documents/project/numbers.txt', 'r')
            line = infile.readline()

            min = float(line)

            while line != '':
                line = infile.readline()
                if(line != ''):
                    if(min > float(line)):
                        min = float(line)
            if self.cb_var4.get() == 1:                        
                self.result.set(min)
            if self.cb_var15.get() == 1:
                min_to_print = min
            infile.close()
# Max
        if self.cb_var5.get() == 1 or self.cb_var15.get() == 1:
            infile = open('C:/Users/Victor/Documents/project/numbers.txt', 'r')
            line = infile.readline()

            max = float(line)

            while line != '':
                line = infile.readline()
                if(line != ''):
                    if(max < float(line)):
                        max = float(line)
            if self.cb_var5.get() == 1:
                self.result.set(max)
            if self.cb_var15.get() == 1:
                max_to_print = max
            infile.close()
# Range
        if self.cb_var6.get() == 1 or self.cb_var15.get() == 1:
            infile = open('C:/Users/Victor/Documents/project/numbers.txt', 'r')
            line = infile.readline()

            min = float(line)
            max = min

            while line != '':
                line = infile.readline()
                if(line != ''):
                    if(max < float(line)):
                        max = float(line)
                    if(min > float(line)):
                        min = float(line)
            if self.cb_var6.get() == 1:
                self.result.set(max-min)
            if self.cb_var15.get() == 1:
                range_to_print = max-min
            infile.close()
# Sum
        if self.cb_var7.get() == 1 or self.cb_var15.get() == 1:
            infile = open('C:/Users/Victor/Documents/project/numbers.txt', 'r')
            line = infile.readline()
            
            sumOfNum = float(line)

            while line != '':
                line = infile.readline()
                if(line != ''):
                    sumOfNum = sumOfNum + float(line)
            if self.cb_var7.get() == 1:
                self.result.set(sumOfNum)
            if self.cb_var15.get() == 1:
                sum_to_print = sumOfNum
            infile.close()
# Count 
        if self.cb_var8.get() == 1 or self.cb_var15.get() == 1:
            infile = open('C:/Users/Victor/Documents/project/numbers.txt', 'r')
            line = infile.readline()
            
            counter = 1

            while line != '':
                line = infile.readline()
                if(line != ''):
                    counter += 1
            if self.cb_var8.get() == 1:
                self.result.set(counter)
            if self.cb_var15.get() == 1:
                count_to_print = counter
            infile.close()    

# 1st Quartile
        if self.cb_var9.get() == 1 or self.cb_var15.get() == 1:
            infile = open('C:/Users/Victor/Documents/project/numbers.txt', 'r')
            line = infile.readline()

            listOfNum = [float(line)]

            while line != '':
                line = infile.readline()
                if(line != ''):
                    listOfNum.append(float(line))

            listOfNum.sort()
                    
            if(len(listOfNum) %2 == 0):
                upperIndex = int(len(listOfNum) / 2)
                lowerIndex = int(len(listOfNum) / 2) - 1

                firstQ = []
                for x in range(len(listOfNum)-(upperIndex)):
                    firstQ.append(listOfNum[x])
                if(len(firstQ) %2 == 0):
                    upperIndex = int(len(firstQ) / 2)
                    lowerIndex = int(len(firstQ) / 2) - 1
                    if self.cb_var9.get() == 1:
                        self.result.set((float((firstQ[upperIndex]) +  firstQ[lowerIndex])) / 2)
                    if self.cb_var15.get() == 1:
                        first_quartile = float(firstQ[upperIndex] +  firstQ[lowerIndex]) / 2
                
                if(len(firstQ) %2 == 1):
                    index = int(len(firstQ) / 2)
                    if self.cb_var9.get() == 1:
                        self.result.set(float(firstQ[index]))
                    if self.cb_var15.get() == 1:
                        first_quartile = float(firstQ[index])
                
            if(len(listOfNum) %2 == 1):
                index = int(len(listOfNum) / 2)

                firstQ = []
                for x in range(len(listOfNum)-(index + 1)):
                    firstQ.append(listOfNum[x])
                if(len(firstQ) %2 == 0):
                    upperIndex = int(len(firstQ) / 2)
                    lowerIndex = int(len(firstQ) / 2) - 1
                    if self.cb_var9.get() == 1:
                        self.result.set((float((firstQ[upperIndex]) +  firstQ[lowerIndex])) / 2)
                    if self.cb_var15.get() == 1:
                        first_quartile = (float((firstQ[upperIndex]) +  firstQ[lowerIndex])) / 2
                if(len(firstQ) %2 == 1):
                    index = int(len(firstQ) / 2)
                    if self.cb_var9.get() == 1:
                        self.result.set(float(firstQ[index]))
                    if self.cb_var15.get() == 1:
                        first_quartile = float(firstQ[index])
            infile.close()    

                  
# 3rd Quartile
        if self.cb_var10.get() == 1 or self.cb_var15.get() == 1:
            infile = open('C:/Users/Victor/Documents/project/numbers.txt', 'r')
            line = infile.readline()

            listOfNum = [float(line)]

            while line != '':
                line = infile.readline()
                if(line != ''):
                    listOfNum.append(float(line))

            listOfNum.sort()    
                    
            if(len(listOfNum) %2 == 0):
                upperIndex = int(len(listOfNum) / 2)
                lowerIndex = int(len(listOfNum) / 2) - 1

                thirdQ = []
                for x in range(len(listOfNum)-(upperIndex)):
                    thirdQ.append(listOfNum[x+upperIndex])
                if(len(thirdQ) %2 == 0):
                    upperIndex = int(len(thirdQ) / 2)
                    lowerIndex = int(len(thirdQ) / 2) - 1
                    if self.cb_var10.get() == 1:
                        self.result.set((float((thirdQ[upperIndex]) +  thirdQ[lowerIndex])) / 2)
                    if self.cb_var15.get() == 1:
                        third_quartile = (float((thirdQ[upperIndex]) +  thirdQ[lowerIndex])) / 2
                if(len(thirdQ) %2 == 1):
                    index = int(len(thirdQ) / 2)
                    if self.cb_var10.get() == 1:
                        self.result.set(float(thirdQ[index]))
                    if self.cb_var15.get() == 1:
                       third_quartile = float(thirdQ[index])
            if(len(listOfNum) %2 == 1):
                index = int(len(listOfNum) / 2)

                thirdQ = []
                for x in range(len(listOfNum)-(index + 1)):
                    thirdQ.append(listOfNum[x+index+1])
                if(len(thirdQ) %2 == 0):
                    upperIndex = int(len(thirdQ) / 2)
                    lowerIndex = int(len(thirdQ) / 2) - 1
                    if self.cb_var10.get() == 1:
                        self.result.set((float((thirdQ[upperIndex]) +  thirdQ[lowerIndex])) / 2)
                    if self.cb_var15.get() == 1:
                        third_quartile = (float((thirdQ[upperIndex]) +  thirdQ[lowerIndex])) / 2
                
                if(len(thirdQ) %2 == 1):
                    index = int(len(thirdQ) / 2)
                    if self.cb_var10.get() == 1:
                        self.result.set(float(thirdQ[index]))
                    if self.cb_var15.get() == 1:
                        third_quartile = float(thirdQ[index])
            infile.close()    

# Standard Deviation and variance
        if self.cb_var11.get() == 1 or self.cb_var12.get() == 1 or self.cb_var13.get() == 1 or self.cb_var14.get() == 1 or self.cb_var15.get() == 1:
            infile = open('C:/Users/Victor/Documents/project/numbers.txt', 'r')
            line = infile.readline()

            listOfNum = [float(line)]
            sumOfNum = float(line)
            sumOfSquares = 0
            mean = 0
            counter = 1

            while line != '':
                line = infile.readline()
                if(line != ''):
                    listOfNum.append(float(line))
                    sumOfNum = sumOfNum + float(line)
                    counter += 1
            mean =(sumOfNum/counter)

            for x in range(len(listOfNum)):
                diffSquared = (float(listOfNum[x]) - mean)**2
                sumOfSquares += diffSquared

            population_variance = round(sumOfSquares / counter, 5)
            sample_variance = round(sumOfSquares / (counter - 1), 5)
            population_stddev = round(population_variance **(1/2), 5)
            sample_stddev  = round(sample_variance **(1/2), 5)

            if self.cb_var11.get() == 1:
                self.result.set(population_stddev)
            if self.cb_var12.get() == 1:
                self.result.set(population_variance)
            if self.cb_var13.get() == 1:
                self.result.set(sample_stddev)
            if self.cb_var14.get() == 1:
                self.result.set(sample_variance)
            infile.close()    


# print to file
        if self.cb_var15.get() == 1:
            
            outfile = open('C:/Users/Victor/Documents/project/results.txt', 'w')

            outfile.write('Number of items in list: ' + str(count_to_print))
            outfile.write('\n\nMean: \t' + str(mean_to_print) + '\nRange: \t' + str(range_to_print) + '\nSum: \t' + str(sum_to_print))

            outfile.write('\n\nFIVE NUMBER SUMMARY:' + '\nMin: \t\t\t' + str(min_to_print) + '\nFirst Quartile: \t' + str(first_quartile)
                          + '\nMedian: \t\t' + str(median_to_print) + '\nThird Quartile: \t' + str(third_quartile) + '\nMax: \t\t\t' + str(max_to_print))
            
            outfile.write('\n\nStandard deviation (of a Population): \t' + str(population_stddev) + '\nVariance (of a Population): \t\t' + str(population_variance))
            outfile.write('\nStandard deviation (of a Sample): \t' + str(sample_stddev) + '\nVariance (of a Sample): \t\t' + str(sample_variance))

            
                   

            # Close the file.
            outfile.close()
my_gui = MyGUI()
