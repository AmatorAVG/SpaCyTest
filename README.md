Test tasks for interview

Task 1.
Use English SpaCy lib, find all tokens with only digits and all proper nouns (PROPN, aka, personal nouns ) in the text, count it and output it right-aligned in the HTML.
For example, for the text "we need 2 tickets to Dublin, and 1/2 a spoon of milk" read from the stdin (use python myprogram.py < input.txt >output.html ) the program should output that "2" was found twice (output "2"), "1" was found once (output "1"), "Dublin" was found once (output "1").
Display it as an HTML table with 2 columns: the first column for the entry, and the second column for the number of times it was found.

Задача 2.
Написать программу на питоне, выдающую без повторений на stdout все различные перестановки N одинаковых (0) и N разных чисел (от 1 до N).
Запуск программы должен выглядеть так: "python permute.py 5"
Скажем, для N=5, это будут числа 0 0 0 0 0 1 2 3 4 5 .
Примеры таких перестановок: 0000012345 или 5012034000
Теперь выведите все такие перестановки для N=5 и сохраните их в файл.
Посчитайте с помощью wc количество строк в этом файле.
Сколько получилось?
Попробуйте оценить время, которое будет ваш алгоритм считаться для N=7 (это не значит, что ваш алгоритм должен быть самый лучший и быстрый, просто грубо оцените примерное время выполнения именно для вашего алгоритма, исходя из вашего понимания).

Для задачи №2 укажите количество строк при N=5
30240

Для задачи №2 укажите теоретическое время для N=7 в элементарных операциях и практическое ожидаемое время в секундах для N=7 для вашего алгоритма, и расскажите, как вы получили эти ответы.
Количество строк можно посчитать по формуле: factorial(2*N)//factorial(N)
Для N=7 получим 17297280 строк.
Для N=6 время выполнения на моем компьютере составило 5 секунд. Ожидаемое время для N=7 в 26 раз дольше, т.е. 130 секунд. На практике примерно так и получилось.

Задача 3:
Написать единый shell-файл для запуска первой и второй программы с параметрами, указанными выше, и получением нужных результатов.