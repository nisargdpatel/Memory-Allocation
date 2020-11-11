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

class MemoryMetrics():
    # Constructor with required fields
    def __init__(self, test):
        self.test = test
        self.totalMemory = 0
        self.memoryAllocated = 0
        self.percentMemoryInUse = 0
        self.requiredMemory = 0
        self.internalFragmentation = 0
        self.percentFreeMemory = 0
        self.externalFragmentation = 0
        self.largestSpace = 0
        self.smallestSpace = 0
        self.numberHeapAllocation = 0
        self.numberLostObj = 0
        self.totalMemorySizeLostObj = 0
        self.percentMemoryLostObj = 0
        self.codeMemory = 0
        self.stackMemory = 0
        self.heapEMemory = 0
        self.stackCodeMemory = 0

    # Generates memory size of each heap element
    def printMetrics(self):
        # PRINT PREFIL STEADY STATE METRICS
        print(self.test)
        print("Total amount of memory defined: ", self.totalMemory)
        print("Total amount of memory allocated: ", self.memoryAllocated)
        print("% of Memory in use: ", self.percentMemoryInUse)
        print("Required amount of memory: ", self.requiredMemory)
        print("% Internal fragmentation: ", self.internalFragmentation)
        print("% Memory free: ",self.percentFreeMemory)
        print("External Fragmentation (number of areas with free space): ", self.externalFragmentation)
        print("Largest Free Space: ", self.largestSpace)
        print("Smallest Free Space: ", self.smallestSpace)
        print("Number of Heap allocation: ", self.numberHeapAllocation)
        print("Number of Lost objects: ", self.numberLostObj)
        print("Total Memory Size of lost objects: ", self.totalMemorySizeLostObj)
        print("\n")

    def resetMetrics(self):
        self.memoryAllocated = 0
        self.percentMemoryInUse = 0
        self.requiredMemory = 0
        self.internalFragmentation = 0
        self.percentFreeMemory = 0
        self.externalFragmentation = 0
        self.largestSpace = 0
        self.smallestSpace = 0
        self.numberHeapAllocation = 0
        self.numberLostObj = 0
        self.totalMemorySizeLostObj = 0
        self.percentMemoryLostObj = 0
        self.codeMemory = 0
        self.stackMemory = 0
        self.heapEMemory = 0
        self.stackCodeMemory = 0



def runSimulation(testName, memoryUnitSize, memoryNumber, outputFile, logFile, lostObjects, smallJobs, mediumJobs, largeJobs):

    outFile = open(outputFile, 'w')
    ff = open('ff.txt', 'w')
    nf = open('nf.txt', 'w')
    bf = open('bf.txt', 'w')
    wf = open('wf.txt', 'w')
    log = open(logFile, 'a')
    log.truncate(0)
    num_lost_objects = 0
    total_memory_lost_objects = 0
    num_operations = 0
    alloc_operations = 0
    free_operations = 0
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
    ffmem = MemoryMetrics('First Fit')
    nfmem = MemoryMetrics('Next Fit')
    bfmem = MemoryMetrics('Best Fit')
    wfmem = MemoryMetrics('Worst Fit')

    ffe = MemoryMetrics('First Fit')
    nfe= MemoryMetrics('Next Fit')
    bfe= MemoryMetrics('Best Fit')
    wfe = MemoryMetrics('Worst Fit')

    ffmem.totalMemory = (memoryUnitSize*memoryNumber)
    nfmem.totalMemory = (memoryUnitSize*memoryNumber)
    bfmem.totalMemory = (memoryUnitSize*memoryNumber)
    wfmem.totalMemory = (memoryUnitSize*memoryNumber)

    jobTime = 0

    for currentTime in range(1,12001):
        print(currentTime, ": ")
        # Add a job and generate the next arrival time
        if currentTime == nextJob:
            # add job to job queue
            jobs.append(Job(random.choice(jobPercents)))

            # determine next arrival time
            nextJob = currentTime + (3 + ( random.choice([1, 2]) * random.choice([-1, 1]) ))

        # Add jobs to the memory unit if it is available
        if not memory and jobs:
            # Add job to the memory units if it can fit the code and stack size
            if (memoryUnitSize*memoryNumber) > (jobs[0].code_size + jobs[0].stack_size):
                for test in [ffmem, nfmem, bfmem, wfmem]:
                    test.resetMetrics()
                    test.totalMemory = (memoryUnitSize*memoryNumber)
                    test.memoryAllocated = (jobs[0].code_size + jobs[0].stack_size)
                jobTypes[jobs[0].size] = jobTypes[jobs[0].size] + 1
                memory.append(jobs.pop())
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
            # Heap elements are allocated evenly across run time
            for number in range(heapsPerUnit):
                # Attempt to allocate each heap element via the 4 algorithms
                heapElement = memory[0].heap_elements[heapCounter]
                #print(heapElement.memory)
                heapElement.ffLocation = alg.mallocFF(heapElement.memory)
                heapElement.nfLocation = alg.mallocNF(heapElement.memory)
                heapElement.bfLocation = alg.mallocBF(heapElement.memory)
                heapElement.wfLocation = alg.mallocWF(heapElement.memory)
                tests = []
                if heapElement.ffLocation != '':
                    tests.append(ffmem)
                    log.write(str(currentTime) + ' First Fit Allocation' + str(heapElement.ffLocation) + '\n')
                if heapElement.nfLocation != '':
                    tests.append(nfmem)
                    log.write(str(currentTime) + ' Next Fit Allocation' + str(heapElement.nfLocation) + '\n' )
                if heapElement.bfLocation != '':
                    tests.append(bfmem)
                    log.write(str(currentTime) + ' Best Fit Allocation' + str(heapElement.bfLocation) + '\n')
                if heapElement.wfLocation != '':
                    tests.append(wfmem)
                    log.write(str(currentTime) + ' Worst Fit Allocation' + str(heapElement.wfLocation) + '\n')
                for test in tests:
                    num_operations += 1
                    alloc_operations += 1
                    test.memoryAllocated += heapElement.memory
                    test.numberHeapAllocation += 1
                    heapElement.lifeTime = random.randint(1, memory[0].running_time)
                    heapCounter += 1

            # reduce the lifeTime as it has consumed 1 time unit
            for element in memory[0].heap_elements:
                element.lifeTime -= 1
                # if lifetime has completed, free up allocated memory
                if element.lifeTime == 0:
                    # if 100th job type skip memory freeing to simulate lost objects
                    if lostObjects and (jobTypes[memory[0].size] % 100) == 0:
                        num_lost_objects += 1
                        total_memory_lost_objects += element.memory
                        continue
                    else:
                        #print('deallocate')
                        alg.freeFF(element.ffLocation, memoryUnitSize)
                        alg.freeNF(element.nfLocation, memoryUnitSize)
                        alg.freeBF(element.bfLocation, memoryUnitSize)
                        alg.freeWF(element.wfLocation, memoryUnitSize)
                        ffmem.memoryAllocated -= element.memory
                        nfmem.memoryAllocated -= element.memory
                        bfmem.memoryAllocated -= element.memory
                        wfmem.memoryAllocated -= element.memory
                        log.write(str(currentTime) + ' First Fit Deallocation' + str(element.ffLocation) + '\n')
                        log.write(str(currentTime) + ' Next Fit Deallocation' + str(element.nfLocation) + '\n' )
                        log.write(str(currentTime) + ' Best Fit Deallocation' + str(element.bfLocation) + '\n')
                        log.write(str(currentTime) + ' Worst Fit Deallocation' + str(element.wfLocation) + '\n')
                        num_operations += 4
                        free_operations += 4


        if currentTime == 2000 or (((currentTime % 20) == 0) and currentTime > 2000):
            tests = [ffmem, nfmem, bfmem, wfmem]
            heapKeys = {
                    'First Fit': alg.ffHeap,
                    'Next Fit': alg.nfHeap,
                    'Best Fit': alg.bfHeap,
                    'Worst Fit': alg.wfHeap,
            }
            for test in tests:
                test.percentMemoryInUse = (test.memoryAllocated / test.totalMemory)*100
                test.requiredMemory = jobs[0].code_size + jobs[0].stack_size
                test.internalFragmentation = ((test.totalMemory - test.requiredMemory)/ test.memoryAllocated)*100 if  test.memoryAllocated > 0 else 0
                test.percentFreeMemory = 100 - test.percentMemoryInUse
                for unit in heapKeys[test.test]:
                    if int(unit) == int(memoryUnitSize):
                        test.externalFragmentation += 1
                test.largestSpace = max(heapKeys[test.test]) if heapKeys[test.test] else 0
                test.smallestSpace = min(heapKeys[test.test]) if heapKeys[test.test] else 0
                test.numberLostObj = num_lost_objects
                test.totalMemorySizeLostObj = total_memory_lost_objects
                test.percentMemoryLostObj = (total_memory_lost_objects / (memoryUnitSize*memoryNumber)) if (num_lost_objects > 0) else 0
                test.codeMemory = jobs[0].code_size
                test.stackMemory = jobs[0].stack_size
                test.heapEMemory = test.memoryAllocated - (jobs[0].code_size + jobs[0].stack_size)
                test.stackCodeMemory = jobs[0].code_size + jobs[0].stack_size
                test.printMetrics()
            print('\nEfficiency Metrics')
            print("Total Operations", num_operations)
            print("Number of Allocations", alloc_operations )
            print("Number of Allocation Operations", alg.a_ops )
            print("Number of Free Requests", free_operations )
            print("Number of Free Operations", alg.f_ops )
            print("Average of Allocations", alloc_operations/4 )
            print("Number of Free Requests", free_operations/4 )
            print("Percent of Allocations", (alloc_operations/num_operations)*100 )
            print("Percent of Free Requests", (free_operations/num_operations)*100)

        # Counter for the current running job
        jobTime -= 1

        # Clear out a job that has finished its run time
        if jobTime == 0 and memory:
            memory.pop(0)


    log.close()
    percent_memory_free = alg.ffHeap.__len__() / memoryUnitSize
    #UPDATE SUMMARY FILE once the full simulation is complete
    #ff.write(str(memoryUnitSize) + "\t" + str(total_memory) + "\t" + str(total_memory / memoryUnitSize) + "\t" + str((jobs[0].code_size + jobs[0].stack_size) / memoryNumber) + "\t" + str(percent_memory_free) + "\t" + str(num_lost_objects) + "\n")

    percent_memory_free = alg.nfHeap.__len__() / memoryUnitSize
    #nf.write(str(memoryUnitSize) + "\t" + str(total_memory) + "\t" + str(total_memory / memoryUnitSize) + "\t" + str((jobs[0].code_size + jobs[0].stack_size) / memoryNumber) + "\t" + str(percent_memory_free) + "\t" + str(num_lost_objects) + "\n")

    percent_memory_free = alg.bfHeap.__len__() / memoryUnitSize
    #bf.write(str(memoryUnitSize) + "\t" + str(total_memory) + "\t" + str(total_memory / memoryUnitSize) + "\t" + str((jobs[0].code_size + jobs[0].stack_size) / memoryNumber) + "\t" + str(percent_memory_free) + "\t" + str(num_lost_objects) + "\n")

    percent_memory_free = alg.wfHeap.__len__() / memoryUnitSize
    #wf.write(str(memoryUnitSize) + "\t" + str(total_memory) + "\t" + str(total_memory / memoryUnitSize) + "\t" + str((jobs[0].code_size + jobs[0].stack_size) / memoryNumber) + "\t" + str(percent_memory_free) + "\t" + str(num_lost_objects) + "\n")


class Algorithms:
    def __init__(self):
        self.ffHeap = []
        self.nfHeap = []
        self.nfPrevious = 0
        self.bfHeap = []
        self.wfHeap = []
        self.a_ops = 0
        self.f_ops = 0

    def mallocFF(self, size):
        r = ''
        for index, x in enumerate(self.ffHeap, 0):
            self.a_ops += 1
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
        for index, x in enumerate(self.nfHeap):
            self.a_ops += 1
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
            self.a_ops += 1
            if x >= size:
                r = self.bfHeap.index(x)
                self.bfHeap[self.bfHeap.index(x)] -= size
                break
        return r

    def mallocWF(self, size):
        r = ''
        for x in sorted(self.wfHeap, reverse=True):
            self.a_ops += 1
            if x >= size:
                r = self.wfHeap.index(x)
                self.wfHeap[self.wfHeap.index(x)] -= size
                break
        return r

    def freeFF(self, location, memoryUnitSize):
        if(location != ''):
            self.f_ops += 1
            self.ffHeap[int(location)] = memoryUnitSize

    def freeNF(self, location, memoryUnitSize):
        if(location != ''):
            self.f_ops += 1
            self.nfHeap[int(location)] = memoryUnitSize

    def freeBF(self, location, memoryUnitSize):
        if(location != ''):
            self.f_ops += 1
            self.bfHeap[int(location)] = memoryUnitSize

    def freeWF(self, location, memoryUnitSize):
        if(location != ''):
            self.f_ops += 1
            self.wfHeap[int(location)] = memoryUnitSize


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



    runSimulation(testName='TestRun', memoryUnitSize=64, memoryNumber=12, outputFile='outputFile.txt', logFile='summaryLog.txt', lostObjects=False, smallJobs=50, mediumJobs=25,largeJobs=25)

    ff = open('ff.txt', 'r')
    nf = open('nf.txt', 'r')
    bf = open('bf.txt', 'r')
    wf = open('wf.txt', 'r')
    print("\t\t\tFirst Fit\tNext Fit\tBest Fit\tWorst Fit")

    print("1\t", "TestRun\t8\t", ff.read(), "\t", ff.read(), "\t", ff.read(), "\t", ff.read(), "\t", ff.read(), "\t", ff.read())

    #runSimulation(testName='TestRun1', memoryUnitSize=10, memoryNumber=5, outputFile='outputFile1.txt', logFile='summaryLog1.txt', lostObjects=True, smallJobs=30, mediumJobs=20,largeJobs=20)
    print("2\t", "TestRun1\t8\t", ff.read(), "\t", ff.read(), "\t", ff.read(), "\t", ff.read(), "\t", ff.read(), "\t", ff.read())


    # memory_size = input("Please enter the memory unit size: ")
    # memory_units = input("Please enter the number of memory units available: ")




if __name__ == "__main__":
    main()
