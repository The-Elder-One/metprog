import random
import json
import timeit

code_to_test = """
import random
import json

with open('list_for_sort.txt', 'r') as fr:
    random_players = json.load(fr)
    
    
class Player:
    def __init__(self, player_info):
        '''
        Структура данных игрока:
        {'country' : страна,
        'NAME' : ФИО,
        'club' : клуб,
        'role' : амплуа,
        'matches' : кол-во матчей,
        'goals' : кол-во мячей}
        '''
        self.player = player_info

    def __lt__(self, other):
        if self.player['matches'] < other.player['matches']:
            return True
        elif self.player['matches'] == other.player['matches']:
            if self.player['NAME'].lower() < other.player['NAME'].lower():
                return True
            elif self.player['NAME'].lower() == other.player['NAME'].lower():
                return self.player['goals'] > other.player['goals']

    def __le__(self, other):
        return self.__lt__(other) or (self.player['matches'] == other.player['matches'] and
                                      self.player['NAME'] == other.player['NAME'] and
                                      self.player['goals'] == other.player['goals'])

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)


random_Players = [Player(x) for x in random_players]


class HeapSort:
    def heapify(self, nums, heap_size, root_index):
        # Индекс наибольшего элемента считаем корневым индексом
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2

        # Если левый потомок корня — допустимый индекс, а элемент больше,
        # чем текущий наибольший, обновляем наибольший элемент
        if left_child < heap_size and nums[left_child] > nums[largest]:
            largest = left_child

        # То же самое для правого потомка корня
        if right_child < heap_size and nums[right_child] > nums[largest]:
            largest = right_child

        # Если наибольший элемент больше не корневой, они меняются местами
        if largest != root_index:
            nums[root_index], nums[largest] = nums[largest], nums[root_index]
            # Heapify the new root element to ensure it's the largest
            self.heapify(nums, heap_size, largest)

        return nums

    def heapsort(self, nums):
        n = len(nums)

        # Создаём Max Heap из списка
        # Второй аргумент означает остановку алгоритма перед элементом -1, т.е.
        # перед первым элементом списка
        # 3-й аргумент означает повторный проход по списку в обратном направлении,
        # уменьшая счётчик i на 1
        for i in range(n, -1, -1):
            self.heapify(nums, n, i)

        # Перемещаем корень Max Heap в конец списка
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums, i, 0)

        return nums
        
д = [x.player for x in HeapSort().heapsort(random_Players)]

with open('outputHeap.txt', 'w') as fw:
    json.dump(д, fw)
"""
elapsed_time = timeit.timeit(code_to_test, number=1)
print(elapsed_time)

code_to_test = """
import random
import json

with open('list_for_sort.txt', 'r') as fr:
    random_players = json.load(fr)


class Player:
    def __init__(self, player_info):
        '''
        Структура данных игрока:
        {'country' : страна,
        'NAME' : ФИО,
        'club' : клуб,
        'role' : амплуа,
        'matches' : кол-во матчей,
        'goals' : кол-во мячей}
        '''
        self.player = player_info

    def __lt__(self, other):
        if self.player['matches'] < other.player['matches']:
            return True
        elif self.player['matches'] == other.player['matches']:
            if self.player['NAME'].lower() < other.player['NAME'].lower():
                return True
            elif self.player['NAME'].lower() == other.player['NAME'].lower():
                return self.player['goals'] > other.player['goals']

    def __le__(self, other):
        return self.__lt__(other) or (self.player['matches'] == other.player['matches'] and
                                      self.player['NAME'] == other.player['NAME'] and
                                      self.player['goals'] == other.player['goals'])

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)


random_Players = [Player(x) for x in random_players]


class QuickSort:
    def quicksort(self, nums):
        if len(nums) <= 1:
            return nums
        else:
            q = random.choice(nums)
        l_nums = [n for n in nums if n < q]

        e_nums = [q] * nums.count(q)
        b_nums = [n for n in nums if n > q]
        return self.quicksort(l_nums) + e_nums + self.quicksort(b_nums)


е = [x.player for x in QuickSort().quicksort(random_Players)]

with open('outputQuick.txt', 'w') as fw:
    json.dump(е, fw)
"""
elapsed_time = timeit.timeit(code_to_test, number=1)
print(elapsed_time)

code_to_test = """
import random
import json

with open('list_for_sort.txt', 'r') as fr:
    random_players = json.load(fr)
    

class Player:
    def __init__(self, player_info):
        '''
        Структура данных игрока:
        {'country' : страна,
        'NAME' : ФИО,
        'club' : клуб,
        'role' : амплуа,
        'matches' : кол-во матчей,
        'goals' : кол-во мячей}
        '''
        self.player = player_info

    def __lt__(self, other):
        if self.player['matches'] < other.player['matches']:
            return True
        elif self.player['matches'] == other.player['matches']:
            if self.player['NAME'].lower() < other.player['NAME'].lower():
                return True
            elif self.player['NAME'].lower() == other.player['NAME'].lower():
                return self.player['goals'] > other.player['goals']

    def __le__(self, other):
        return self.__lt__(other) or (self.player['matches'] == other.player['matches'] and
                                      self.player['NAME'] == other.player['NAME'] and
                                      self.player['goals'] == other.player['goals'])

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)


random_Players = [Player(x) for x in random_players]


class MergeSort:
    def mergesort(self, L):
        if len(L) < 2:
            return L[:]
        else:
            middle = int(len(L) / 2)
            left = self.mergesort(L[:middle])
            right = self.mergesort(L[middle:])
            return self.merge(left, right)

    @staticmethod
    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1

        return result


ж = [x.player for x in MergeSort().mergesort(random_Players)]

with open('outputMerge.txt', 'w') as fw:
    json.dump(ж, fw)
"""
elapsed_time = timeit.timeit(code_to_test, number=1)
print(elapsed_time)
