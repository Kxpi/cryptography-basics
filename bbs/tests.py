from colorama import Fore, Style
from .utils.chunks import chunks

class Tests:

    def single_bit(self, bits):
        minValue = int(len(bits)*0.48625)
        maxValue = int(len(bits)*0.51375)
        print(Fore.YELLOW + '----------------------------TEST1----------------------------\n' + Style.RESET_ALL)
        countBit1 = 0
        print(f'''
        Test for single bits (1)
        Min value - {minValue}
        Max value - {maxValue}

        ''')
        
        for bit in bits:
            if(bit == 1):
                countBit1 += 1

        if(countBit1 > minValue and countBit1 < maxValue):
            print(Fore.GREEN + f'\tPASSED - The sum of ones is equal to {countBit1}\n' + Style.RESET_ALL)
        else:
            print(Fore.RED + f'\tFAILED - The sum of ones is equal to {countBit1}\n'  + Style.RESET_ALL)

        print(Fore.YELLOW + '-------------------------------------------------------------\n' + Style.RESET_ALL)

    def series(self, bits):
        print(Fore.YELLOW + '----------------------------TEST2----------------------------\n' + Style.RESET_ALL)

        print(f'''
        Test for max consecutive series of bits
        Allowed number of series for different series-lengths of 20k bits
         1 | 2315-2685
         2 | 1114-1386
         3 | 527-723
         4 | 240-384
         5 | 103-209
        >6 | 103-209
        
        ''')

        ranges = {
            1: {
                'min': 2135,
                'max': 2685
            },
            2: {
                'min': 1114,
                'max': 1386
            },
            3: {
                'min': 527,
                'max': 723
            },
            4: {
                'min': 240,
                'max': 384
            },
            5: {
                'min': 103,
                'max': 209
            },
            6: {
                'min': 103,
                'max': 209
            }
        }

        curr_series = 0
        bittttt = []
        series = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
        series_ones = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
        series_zeros = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
        
        for i in range(len(bits)):
            if i+1 == len(bits):
                break
            
            if bits[i]==bits[i+1]:
                bittttt.append(bits[i])
            else:
                bittttt.append(bits[i])
                curr_series = len(bittttt)
                if 1 in bittttt:
                    if curr_series>5:
                        series_ones[6] +=1
                    else:
                        series_ones[curr_series] +=1
                else: 
                    if curr_series>5:
                        series_zeros[6] +=1
                    else:
                        series_zeros[curr_series] +=1
                curr_series = 0
                bittttt = []

        for key in series.keys():
            series[key] = max(series_zeros[key], series_ones[key])
            if series[key] > ranges[key]['min'] and series[key] < ranges[key]['max']:
                print(Fore.GREEN + f'\tPASSED - series of length {key} is {series[key]} - [{ranges[key]["min"]}, {ranges[key]["min"]}]\n' + Style.RESET_ALL)
            else:
                print(Fore.GREEN + f'\tFAILED - series of length {key} is {series[key]} - [{ranges[key]["min"]}, {ranges[key]["min"]}]\n' + Style.RESET_ALL)

        print(Fore.YELLOW + '-------------------------------------------------------------\n' + Style.RESET_ALL)

    def longest_series(self, bits):
        index = 0
        nextIndex = 1
        longestSeries = 0
        currentSeries = 1
        value = bits[0]
        max_series = 26

        print(Fore.YELLOW + '----------------------------TEST3----------------------------\n' + Style.RESET_ALL)

        print(f'''
        Test for max consecutive series of bits
        Max allowed length of series - {max_series}
        
        ''')

        for i in bits:
            if(nextIndex < len(bits)):

                if(value is bits[nextIndex]):
                    currentSeries += 1
                    if(currentSeries > longestSeries):
                        longestSeries = currentSeries
                        value = i

                if(value is not bits[nextIndex]):
                    currentSeries = 1
                    value = bits[nextIndex]

            index += 1
            nextIndex += 1

        if(longestSeries < max_series):
            print(Fore.GREEN + f'\tPASSED - Longest series is {longestSeries}\n' + Style.RESET_ALL)
        else:
            print(Fore.RED + f'\tFAILED - Longest series is {longestSeries}\n'  + Style.RESET_ALL)


        print(Fore.YELLOW + '-------------------------------------------------------------\n' + Style.RESET_ALL)


    def poker(self, bits):
        print(Fore.YELLOW + '----------------------------TEST4----------------------------\n' + Style.RESET_ALL)
        nums = {}
        fours = list(chunks(bits, 4))
        unique_fours = list(set(fours))
        lower = 2.16
        upper = 46.17
        print(f'''
        Poker test

        ''')

        for i in unique_fours:
            nums[i] = fours.count(i)
        
        summed = 0

        for key in nums:
            summed += nums[key]**2

        X = (16*summed) / 5000 - 5000

        if(X > lower and X < upper):
            print(Fore.GREEN + f'\tPASSED - X is {round(X, 2)} - between {lower} and {upper} \n' + Style.RESET_ALL)
        else:
            print(Fore.RED + f'\tPASSED - X is {round(X, 2)} - not in between {lower} and {upper} \n'  + Style.RESET_ALL)

        print(Fore.YELLOW + '-------------------------------------------------------------\n' + Style.RESET_ALL)
