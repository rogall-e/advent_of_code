with open("data/day8.txt") as f:
    data = f.read()

test_data_1 = '''acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
'''

test_data_2 = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

data = data.split('\n')
data.remove('')
signal_lst = []
digit_lst = []
for item in data:
    _item = item.split(' | ')
    signal_lst.append(_item[0].split(' '))
    digit_lst.append(_item[1].split(' '))

    
def get_simple_digits(signal):
    counter = 0
    for item in signal:
        item = [len(x) for x in item]
        for _ in item:
            if _ == 2 or _ == 3 or _ == 4 or _ == 7:
                counter += 1
    return counter



   
    


def get_signal_output(signal_lst, digit_lst):
    sorted_signal = []
    for (idx_digit, digit), (idx_signal,signal) in zip(enumerate(digit_lst), enumerate(signal_lst)):
        digit_output ={
                '0': '',
                '1' : '',
                '2' : '',
                '3' : '',
                '4' : '',
                '5' : '',
                '6' : '',
                '7' : '',
                '8' : '',
                '9' : ''
            }
        while '' in digit_output.values():
            for i_signal, signal_item in enumerate(signal):
                if len(signal_item) == 2:
                    digit_output['1'] = signal[i_signal]
                elif len(signal_item) == 4:
                    digit_output['4'] = signal[i_signal]
                elif len(signal_item) == 3:
                    digit_output['7'] = signal[i_signal]
                elif len(signal_item) == 7:
                    digit_output['8'] = signal[i_signal]
                elif len(signal_item) == 5:
                    # len of 5 are 2,3,5 
                    if len(set(sorted(digit_output['1'])).intersection(set(sorted(signal_item)))) == 2:
                        digit_output['3'] = signal[i_signal]
                    if len(set(sorted(digit_output['1'])).intersection(set(sorted(signal_item)))) == 1 and len(set(sorted(digit_output['6'])).intersection(set(sorted(signal_item)))) == 5:
                        digit_output['5'] = signal[i_signal]
                    if len(set(sorted(digit_output['6'])).intersection(set(sorted(signal_item)))) == 4 and len(set(sorted(digit_output['1'])).intersection(set(sorted(signal_item)))) == 1:
                        digit_output['2'] = signal[i_signal]
                elif len(signal_item) == 6:
                    # len of 6 are 0,6,9
                    if len(set(sorted(digit_output['4'])).intersection(set(sorted(signal_item)))) == 4:
                        digit_output['9'] = signal[i_signal]
                    if len(set(sorted(digit_output['4'])).intersection(set(sorted(signal_item)))) == 3 and len(set(sorted(digit_output['1'])).intersection(set(sorted(signal_item)))) == 2:
                        digit_output['0'] = signal[i_signal]
                    if len(set(sorted(digit_output['4'])).intersection(set(sorted(signal_item)))) == 3 and len(set(sorted(digit_output['1'])).intersection(set(sorted(signal_item)))) == 1:
                        digit_output['6'] = signal[i_signal]
            
        for idx_digit_2, digit_item in enumerate(digit):
            for k,v in digit_output.items():
                if sorted(digit_item) == sorted(v):
                    digit[idx_digit_2] = k
  
        sorted_signal.append(int(''.join(digit)))                   
   
    
    return sum(sorted_signal)
        

print(get_simple_digits(digit_lst))
print(get_signal_output(signal_lst, digit_lst))