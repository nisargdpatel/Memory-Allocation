import random

class Job():
    # Constructor with required fields
    def __init__(self, size):
        self.size = size
        self.running_time = self.generate_running_time()
        self.code_size = self.generate_code_size()
        self.stack_size = self.generate_stack_size()
        self.heap_elements = self.generate_heap_elements()

    # Generates running time based on the job size
    def generate_running_time(self):
        if self.size.lower() == 'small':
            base = 5
        elif self.size.lower() == 'medium':
            base = 10
        elif self.size.lower() == 'large':
            base = 25
        return base + random.choice([-1, 0, 1])

    # Generates code size based on the job size
    def generate_code_size(self):
        if self.size.lower() == 'small':
            base = 60
            max_value = 20
        elif self.size.lower() == 'medium':
            base = 90
            max_value = 30
        elif self.size.lower() == 'large':
            base = 170
            max_value = 50
        return base + ( random.randint(0, max_value) * random.choice([-1, 1]) )

    # Generates stack size based on the job size
    def generate_stack_size(self):
        if self.size.lower() == 'small':
            base = 30
            max_value = 10
        elif self.size.lower() == 'medium':
            base = 60
            max_value = 20
        elif self.size.lower() == 'large':
            base = 90
            max_value = 30
        return base + ( random.randint(0, max_value) * random.choice([-1, 1]) )

    # Generates heap elements based on the job size
    def generate_heap_elements(self):
        if self.size.lower() == 'small':
            multiplier = 50
        elif self.size.lower() == 'medium':
            multiplier = 100
        elif self.size.lower() == 'large':
            multiplier = 250
        elements = []
        for i in range(0, (multiplier*self.running_time) ):
            elements.append(HeapElement())
        return elements


class HeapElement():
    # Constructor with required fields
    def __init__(self):
        self.memory = self.generate_memory()

    # Generates memory size of each heap element
    def generate_memory(self):
        return 35 + ( random.randint(0, 15) * random.choice([-1, 1]) )





def main():

    
    

    def printHeap(tempJo, tempOutFile):
        counter = 1
        print("Run Time: ", tempJo.running_time)
        tempOutFile.write("\nRun Time: " + str(tempJo.running_time) + "\n")
        print("Code Size: ", tempJo.code_size)
        tempOutFile.write("Code Size: " + str(tempJo.code_size) + "\n")
        print("Stack Size: ", tempJo.stack_size)
        tempOutFile.write("Stack Size: " + str(tempJo.stack_size) + "\n")

        if (tempJo.size.lower() == 'small'):
            multiplier = 50
        elif (tempJo.size.lower() == 'medium'):
            multiplier = 100
        elif (tempJo.size.lower() == 'large'):
            multiplier = 250

        print("Heap Elements: ", tempJo.running_time, " * ", multiplier, " = ", tempJo.running_time*multiplier, " heap elements")
        tempOutFile.write("Heap Elements: " + str(tempJo.running_time) + " * " + str(multiplier) + " = " + str(tempJo.running_time*multiplier) + " heap elements\n")
        print(multiplier, " heap elements arrive each time unit\n")
        tempOutFile.write(str(multiplier) + " heap elements arrive each time unit\n")

        for element in tempJo.heap_elements:
            
            if(element.memory < 20 or element.memory > 50):
                print("Heap element ", counter, ": ", element.memory, " memory\t->\tNot in the range 35+/-15")
                tempOutFile.write("Heap element " + str(counter) + ": " + str(element.memory) + " memory\t->\tNot in the range 35+/-15\n")
            else:
                print("Heap element ", counter, ": ", element.memory, " memory")
                tempOutFile.write("Heap element " + str(counter) + ": " + str(element.memory) + " memory\n")
            counter = counter+1

        


    jobSmall = Job("small")
    outFileSmall = open('small_jobs_output.txt', 'w')
    printHeap(jobSmall, outFileSmall)
    outFileSmall.close()

    jobMedium = Job("medium")
    outFileMedium = open('medium_jobs_output.txt', 'w')
    printHeap(jobMedium, outFileMedium)
    outFileMedium.close()

    jobLarge = Job("large")
    outFileLarge = open('large_jobs_output.txt', 'w')
    printHeap(jobLarge, outFileLarge)
    outFileLarge.close()

    # memory_size = input("Please enter the memory unit size: ")
    # memory_units = input("Please enter the number of memory units available: ")

    # determining next arrival time of a job
    # arrival_time = 3 + ( random.randint(0, 2) * random.choice([-1, 1]) )

    


if __name__ == "__main__":
    main()
