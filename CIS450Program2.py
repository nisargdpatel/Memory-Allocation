import random, math
from itertools import cycle

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
        self.ffLocation = ''
        self.nfLocation = ''
        self.bfLocation = ''
        self.wfLocation = ''
        self.lifeTime = 0

    # Generates memory size of each heap element
    def generate_memory(self):
        return 35 + ( random.randint(0, 15) * random.choice([-1, 1]) )

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

def runSimulation(testName, memoryUnitSize, memoryNumber, outputFile, logFile, lostObjects, smallJobs, mediumJobs, largeJobs):
    total_memory = 0
    total_free_memory = 0
    num_lost_objects = 0
    total_memory_lost_objects = 0
    jobPercents = []
    jobPercents.extend('small' for x in range(smallJobs))
    jobPercents.extend('medium' for x in range(mediumJobs))
    jobPercents.extend('large' for x in range(largeJobs))
    jobs = []
    nextJob = 3 + ( random.choice([1, 2]) * random.choice([-1, 1]) )
    memory = []
    jobTypes = {
                "small":0,
                "medium":0,
                "large":0,
            }

    alg = Algorithms()
    jobTime = 0

    for currentTime in range(1,12001):
        print(currentTime, ": ")
        # Add a job and generate the next arrival time
        if currentTime == nextJob:
            # add job to job queue
            jobs.append(Job(random.choice(jobPercents)))

            # determine next arrival time
            nextJob = currentTime + (3 + ( random.choice([1, 2]) * random.choice([-1, 1]) ))

        # Clear out a job that has finished its run time
        if jobTime == 0 and memory:
            memory.pop()

        # Add jobs to the memory unit if it is available
        if not memory and jobs:
            total_free_memory += 1
            # Add job to the memory units if it can fit the code and stack size
            if (memoryUnitSize*memoryNumber) > (jobs[0].code_size + jobs[0].stack_size):
                jobTypes[jobs[0].size] = jobTypes[jobs[0].size] + 1
                memory.append(jobs.pop())
                total_memory += 1
                jobTime = memory[0].running_time
                heapsPerUnit = math.ceil(len(memory[0].heap_elements) / jobTime)
                heapCounter = 0
                heap = [memoryUnitSize] * (memoryNumber - (math.ceil(memory[0].code_size / memoryUnitSize) + math.ceil(memory[0].stack_size / memoryUnitSize)))
                alg.ffHeap = heap
                alg.nfHeap = heap
                alg.bfHeap = heap
                alg.wfHeap = heap
                alg.nfPrevious = 0
            else:
                # Job cannot fit in the memory units so move it to the end of the queue
                jobs.append(jobs.pop())

        # If there is a job in memory, begin allocation/deallocation
        if memory:
            total_memory += 1
            # Heap elements are allocated evenly across run time
            for number in range(heapsPerUnit):
                # Attempt to allocate each heap element via the 4 algorithms
                heapElement = memory[0].heap_elements[heapCounter]
                heapElement.ffLocation = alg.mallocFF(heapElement.memory)
                heapElement.nfLocation = alg.mallocNF(heapElement.memory)
                heapElement.bfLocation = alg.mallocBF(heapElement.memory)
                heapElement.wfLocation = alg.mallocWF(heapElement.memory)
                heapElement.lifeTime = random.randint(1, memory[0].jobTime)
                heapCounter += 1

            # reduce the lifeTime as it has consumed 1 time unit
            for element in memory[0].heap_elements:
                element.lifeTime -= 1
                total_memory += 1
                # if lifetime has completed, free up allocated memory
                if element.lifeTime == 0:
                    # if 100th job type skip memory freeing to simulate lost objects
                    if lostObjects and (jobTypes[memory[0].size] % 100) == 0:
                        num_lost_objects += 1
                        total_memory_lost_objects += element.memory
                        continue
                    else:
                        freeFF(element.ffLocation, memoryUnitSize)
                        freeNF(element.nfLocation, memoryUnitSize)
                        freeBF(element.bfLocation, memoryUnitSize)
                        freeWF(element.wfLocation, memoryUnitSize)
                        total_free_memory += 1

        # Counter for the current running job
        jobTime -= 1

        if ((currentTime % 20) == 0) and currentTime > 2000:
            # PRINT METRICS FOR EVERY 20 TIME UNITS
            print("Steady state:")
            print("Total amount of memory defined: ", memoryUnitSize)
            print("Total amount of memory allocated: ", total_memory)
            print("% of Memory in use: ", total_memory / memoryUnitSize)
            print("Required amount of memory: ", (jobs[0].code_size + jobs[0].stack_size) / memoryNumber)
            # print("% Internal fragmentation: ", (total_memory - ((jobs[0].code_size + jobs[0].stack_size) / memoryNumber))/total_memory)
            print("% Memory free: ", total_free_memory / memoryUnitSize)
            print("External Fragmentation (number of areas with free space): ")
            print("Largest Free Space: ")
            print("Smallest Free Space: ")
            print("Number of Heap allocation: ")
            print("Number of Lost objects: ", num_lost_objects)
            if (total_memory_lost_objects != 0):
               print("Total Memory Size of lost objects: ", total_memory_lost_objects) 
               print("% Memory of lost objects: ", total_memory / total_memory_lost_objects)
            pass


        if currentTime == 2000:
            # PRINT PREFIL STEADY STATE METRICS
            print("Steady state:")
            print("Total amount of memory defined: ", memoryUnitSize)
            print("Total amount of memory allocated: ", total_memory)
            print("% of Memory in use: ", total_memory / memoryUnitSize)
            print("Required amount of memory: ", (jobs[0].code_size + jobs[0].stack_size) / memoryNumber)
            # print("% Internal fragmentation: ", (total_memory - ((jobs[0].code_size + jobs[0].stack_size) / memoryNumber))/total_memory)
            print("% Memory free: ", total_free_memory / memoryUnitSize)
            print("External Fragmentation (number of areas with free space): ")
            print("Largest Free Space: ")
            print("Smallest Free Space: ")
            print("Number of Heap allocation: ")
            print("Number of Lost objects: ", num_lost_objects)
            if (total_memory_lost_objects != 0):
               print("Total Memory Size of lost objects: ", total_memory_lost_objects) 
               print("% Memory of lost objects: ", total_memory / total_memory_lost_objects)
            
            pass

    #UPDATE SUMMARY FILE once the full simulation is complete
   
    print("\t\t\tFirst Fit\tNext Fit\tBest Fit\tWorst Fit")
    print(testName, "\t", alg.ffHeap, "\t", alg.nfHeap, "\t", alg.bfHeap, "\t", alg.wfHeap)
    # print("# of small jobs:")
    # print("# of medium jobs:")
    # print("# of large jobs:")
    # print("total amount of memory defined:")
    # print("amount of memory allocated:")
    # print("% memory in use:")
    # print("required amount of memory:")
    # print("% internal fragmentation:")
    # print("% memory free:")
    # print("external fragmentation:")
    # print("")


class Algorithms:
    def __init__(self):
        self.ffHeap = []
        self.nfHeap = []
        self.nfPrevious = 0
        self.bfHeap = []
        self.wfHeap = []

    def mallocFF(self, size):
        r = ''
        for index, x in enumerate(self.ffHeap):
            if x >= size:
                self.ffHeap[index] -= size
                r = index
                break
        return r

    def mallocNF(self, size):
        r = ''
        index = self.nfPrevious
        nfHeapE = self.nfHeap[0:self.nfPrevious]
        del self.nfHeap[0:self.nfPrevious]
        self.nfHeap.extend(nfHeapE)
        for index, x in enumerate(cycle(self.nfHeap)):
            if index >= len(self.nfHeap)-1:
                index = 0
            if x >= size:
                self.nfHeap[index] -= size
                self.nfPrevious = index
                r = index
                break
        return r

    def mallocBF(self, size):
        r = ''
        for x in sorted(self.bfHeap):
            if x >= size:
                r = self.bfHeap.index(x)
                self.bfHeap[self.bfHeap.index(x)] -= size
                break
        return r

    def mallocWF(self, size):
        r = ''
        for x in sorted(self.wfHeap, reverse=True):
            if x >= size:
                r = self.wfHeap.index(x)
                self.wfHeap[self.wfHeap.index(x)] -= size
                break
        return r

    def freeFF(self, location, memoryUnitSize):
        ffHeap[location] = memoryUnitSize

    def freeNF(self, location, memoryUnitSize):
        nfHeap[location] = memoryUnitSize

    def freeBF(self, location, memoryUnitSize):
        bfHeap[location] = memoryUnitSize

    def freeWF(self, location, memoryUnitSize):
        wfHeap[location] = memoryUnitSize

def main():
    """jobSmall = Job("small")
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
    outFileLarge.close()"""

    # test_name = input("Enter test name: ")
    # print(test_name)
    # memory_unit_size = input("Enter memory unit size: ")
    # print(memory_unit_size)
    # memory_number = input("Enter memory number: ")
    # print(memory_number)
    # output_file_name = input("Enter output file name")
    # print(output_file_name)
    # log_file_name = input("Enter log file name: ")
    # print(log_file_name)
    # want_lost_objects = input("Enter 1 if you want lost objects and 2 if you don't: ")
    # print(want_lost_objects)
    # if (want_lost_objects == "1"):
    #     lost_objects = True
    # else:
    #     lost_objects = False
    # print(lost_objects)
    # small_jobs = input("Enter number of small jobs: ")
    # medium_jobs = input("Enter number of medium jobs: ")
    # large_jobs = input("Enter number of large jobs: ")


    # runSimulation(str(test_name), int(memory_unit_size), int(memory_number), str(output_file_name), str(log_file_name), bool(lost_objects), int(small_jobs), int(medium_jobs), int(large_jobs))

    print("\t\t\tFirst Fit\tNext Fit\tBest Fit\tWorst Fit")
    print("1\t", end='')
    runSimulation(testName='TestRun', memoryUnitSize=8, memoryNumber=15, outputFile='', logFile='', lostObjects=False, smallJobs=50, mediumJobs=25,largeJobs=25)

    


    # memory_size = input("Please enter the memory unit size: ")
    # memory_units = input("Please enter the number of memory units available: ")




if __name__ == "__main__":
    main()
